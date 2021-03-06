from flask import Flask, render_template, url_for, request, redirect, send_file
from datetime import datetime
from operator import itemgetter, attrgetter
import csv
from lcapy import *

# PROGRAMMED BY KWABENA GYASI BAWUAH

app = Flask(__name__)       # Use the flask Python web framework

testVar = None

# Renders the home web page
@app.route('/')
def home():
    return render_template('home.html')

# pdf
@app.route('/send-pdf')
def send_pdf():
    print('In send-pdf route')
    return send_file('./test.pdf', attachment_filename='test.pdf')

# Render main simulator page; Add component to the netlist if one was added
@app.route('/simulate', methods=['POST', 'GET'])
def simulate():
    global testVar
    if request.method == 'POST': 
        netlistArray = request.json["netlistArray"]
        valueArray = request.json["valueArray"]
        #print(request.method)
        print(netlistArray)
        print(valueArray)

        test_circuit = '''      
        V1 1 0_1 dc 3; down, i=i_x
        R1 1 2 4; right
        R2 2 0 2; down
        I1 2_1 0_2 dc 2; down
        W 0 0_1; left
        W 0 0_2; right
        W 2 2_1; right
            '''

        netlistArray = [y for y in (x.strip() for x in test_circuit.splitlines()) if y]
        
        #run lcappy functions here i guess.
        mna = Circuit(test_circuit)

        #with open("circuitnetlist.csv","w",newline = "") as new_file:
        #    csv_writer = csv.writer(new_file, delimiter = " ")
        #    for line in netlistArray:
        #        csv_writer.writerow(line.split(" "))

        #length = len(netlistArray)
        #for line in range(length):
        #    mna.add(str(netlistArray[line]))
                
        mna.draw("test.pdf")

        testVar = mna.dc().equations()

        return redirect (url_for("run"))
    else:
        return render_template('simulate.html')

# Run simulation using the simulation parameters given
@app.route('/run', methods=['POST', 'GET'])
def run():
    global testVar
    print(testVar)
    return render_template('run.html',testVar = testVar)


# Renders the AboutUs web page
@app.route('/about')
def about():
    return render_template('about.html')


# Run the main program
if __name__ == "__main__":
    app.run(debug=True) # Add Port 8080 to run virtualenv on the Google Cloud App platform