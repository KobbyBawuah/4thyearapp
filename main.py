from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from operator import itemgetter, attrgetter
import csv
from lcapy import Circuit 

# PROGRAMMED BY KWABENA GYASI BAWUAH

app = Flask(__name__)       # Use the flask Python web framework

testVar = None

# Renders the home web page
@app.route('/')
def home():
    return render_template('home.html')

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

        #run lcappy functions here i guess.
        mna = Circuit()

        #with open("circuitnetlist.csv","w",newline = "") as new_file:
        #    csv_writer = csv.writer(new_file, delimiter = " ")
        #    for line in netlistArray:
        #        csv_writer.writerow(line.split(" "))

        length = len(netlistArray)
        for line in range(length):
            mna.add(str(netlistArray[line]))
                
        mna.draw("test.pdf")
        
        #mna.V1.V

        #print(mna.V1.V)
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