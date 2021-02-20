from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from operator import itemgetter, attrgetter
import csv

# PROGRAMMED BY JUSTIN SWARD and KWABENA GYASI BAWUAH

app = Flask(__name__)       # Use the flask Python web framework
# Definition of the Part class
# @param input partType The type of part (0=VDC, 1=VAC, 2=Resistor, 3=Capacitor,4=Inductor)
# @param input partId The instance of the part within that type
# @param input partValue The absolute value in base units (Ohms, Farads, Henries) of the part
# @param input node1 The numerical value of the positive or first node the part is connected
# @param input node2 The numerical value of the negative or second node the part is connected
class Part:
    number_of_parts = 0 # Keeps track of the number of parts

    def __init__(self, partType, partId,partValue, node1, node2):
        self.partType = partType        # Component type (V,R,C,L,...)
        self.partId = partId            # Component numeric identifier
        self.partValue = partValue      # Component value (numeric)
        self.node1 = node1              # Component first node (+ve if applicable)
        self.node2 = node2              # Component second node (-ve if applicable)
        Part.number_of_parts += 1       # Increment the number of parts in the Part class

    def getType(self):
        return self.partType

    def getId(self):
        return self.partId
    
    def getValue(self):
        return self.partValue

    def getNode1(self):
        return self.node1

    def getNode2(self):
        return self.node2

    # Returns a string value for the units based on the part type
    def getUnits(self):
        if self.partType == "V":
            return "V"
        elif self.partType == "R":
            return "\u03A9"
        elif self.partType == "C":
            return "F"
        elif self.partType == "L":
            return "H"
    
    # Returns the full part name based on the part type and ID
    def getPartName(self):
        return str(self.partType) + str(self.partId)


class Simulation:
    def __init__(self, simtype, simnode, simstartfreq, simendfreq):
        self.simtype = simtype              # Simulation Type
        self.simnode = simnode              # Simulation Node
        self.simstartfreq = simstartfreq    # Simulation Start (low) frequency
        self.simendfreq = simendfreq        # Simulation End (high) frequency

    # Return string description of the simulation type being run
    def getType(self):
        if self.simtype == "1":
            return "Voltage Reading"
        elif self.simtype == "2":
            return "Time Domain Analysis"
        elif self.simtype == "3":
            return "Frequency Domain Analysis"
        else:
            return "Something went wrong!"

    # Return string of the node to be simulated
    def getNode(self):
        return str(self.simnode)
    
    # Return string of the simulation start frequency
    def getStart(self):
        return str(self.simstartfreq)
    
    # Return string of the simulation end frequency
    def getEnd(self):
        return str(self.simendfreq)


# Renders the home web page
@app.route('/')
def home():
    return render_template('home.html')



# Render main simulator page; Add component to the netlist if one was added
@app.route('/simulate', methods=['POST', 'GET'])
def simulate():
    if request.method == 'POST': 
        array = request.json
        print(request.method)
        print(array)
        with open("circuitnetlist.csv","w",newline = "") as new_file:
            csv_writer = csv.writer(new_file, delimiter = ",")
            for line in array:
                csv_writer.writerow(line.split(" "))
        return redirect (url_for("run"))
    else:
        return render_template('simulate.html')

# Run simulation using the simulation parameters given
@app.route('/run', methods=['POST', 'GET'])
def run():
    if request.method == 'POST':
        sim.simtype = request.form['simtype']
        sim.simnode = request.form['simnode']
        sim.simstartfreq = request.form['simstartfreq']
        sim.simendfreq = request.form['simendfreq']
    return render_template('run.html', simHTML = sim)


# Delete all parts in the net list (clear netlist)
@app.route('/clear')
def clearList():
    part_array.clear()
    Part.number_of_parts = 0
    return redirect('/simulate')


# Delete requested from main page to delete part in net list
@app.route('/delete/<toDelete>')
def deletePart(toDelete):
    for part in part_array:
        if part.getPartName() == toDelete:
            index = part_array.index(part)
            print("Index is: " + str(index))
            part_array.pop(index)
            Part.number_of_parts -= 1
            break
    return redirect('/simulate')



@app.route('/undo') # BROKEN CURRENTLY -- REMOVES THE WRONG COMPONENT !!!
def undoAdd():
    part_array.pop()
    Part.number_of_parts -= 1
    return redirect('/')



# Renders the AboutUs web page
@app.route('/about')
def about():
    return render_template('about.html')


# Run the main program
if __name__ == "__main__":
    part_array = []             # Establish the netlist holding the parts and their information (Parts objects)
    sim = Simulation("0",0,0,0) # Keeps track of the simulation settings - establish defaults
    app.run(debug=True) # Add Port 8080 to run virtualenv on the Google Cloud App platform