from flask import Flask, render_template, url_for, request, redirect, send_file
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from operator import itemgetter, attrgetter
import csv
from lcapy import *
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# PROGRAMMED BY KWABENA GYASI BAWUAH

app = Flask(__name__)       # Use the flask Python web framework

testVar = None
testVar2 = None

# Renders the home web page
@app.route('/')
def home():
    return render_template('home.html')

# pdf
@app.route('/send-pdf')
def send_pdf():
    print('In send-pdf route')
    return send_file('./test.pdf', attachment_filename='test.pdf')

#upload
#@app.route('/upload')
#def upload_file():
#    return render_template('simulate.html')

# Render main simulator page; Add component to the netlist if one was added
@app.route('/simulate', methods=['POST', 'GET'])
def simulate():
    global testVar
    global testVar2
    if request.method == 'POST': 
        netlistArray = request.json["netlistArray"]
        valueArray = request.json["valueArray"]

        #print(request.method)
        print(netlistArray)
        print(valueArray)

        #------------------------
        #test_circuit = '''      
        #V1 1 0; down
        #R1 1 2; left=2, i=I_1, v=V_{R_1}
        #R2 1 3; right=2, i=I_2, v=V_{R_2}
        #L1 2 0_1; down, i=I_1, v=V_{L_1}
        #L2 3 0_3; down, i=I_1, v=V_{L_2}
        #W 0 0_3; right
        #W 0 0_1; left
        #    '''
        #netlistArray = [y for y in (x.strip() for x in test_circuit.splitlines()) if y]

        #------------------------
        if len(netlistArray) > 0 :
            mna = Circuit()
            #to iterate user input 
            length = len(netlistArray)
            for line in range(length):
                mna.add(str(netlistArray[line]))

            mna.draw("test.pdf")
            #---------------------------

            #to write netlist array to csv
            #with open("circuitnetlist.csv","w",newline = "") as new_file:
            #    csv_writer = csv.writer(new_file, delimiter = " ")
            #    for line in netlistArray:
            #        csv_writer.writerow(line.split(" "))
            
            #---------------------------
            #to read netlist array to csv
            #with open("circuitnetlist.csv","r",newline = "") as csv_file:        
            #    csv_reader = csv.reader(csv_file, delimiter=',')
            #    for row in csv_reader:
            #        mna.add(row)

            #---------------------------
            #Running from csv file
        else: 
            mna = Circuit('circuitnetlist.csv')
            mna.draw("test.pdf")



        testVar = mna.dc().equations()
        
        #testVar2 = mna.R1.V
        print("Test Var2 works")

        #tried ploting
        #tv = linspace(0, 1, 100)
        #results = mna.sim(tv)
        #ax = mna.R1.v.plot(tv, label='analytic')
        #ax.plot(tv, results.R1.v, label='simulated')
        #ax.legend()

        #savefig('sim1.png')

        return redirect (url_for("run"))
    else:
        return render_template('simulate.html')

# Run simulation using the simulation parameters given
@app.route('/run', methods=['POST', 'GET'])
def run():
    global testVar
    #global testVar2
    print(testVar)
    print(testVar2)
    return render_template('run.html',testVar = testVar,testVar2 = testVar2)


# Renders the AboutUs web page
@app.route('/about')
def about():
    return render_template('about.html')


# Run the main program
if __name__ == "__main__":
    app.run(debug=True) # Add Port 8080 to run virtualenv on the Google Cloud App platform