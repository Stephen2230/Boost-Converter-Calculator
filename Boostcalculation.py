#!/usr/bin/python

import os
import numpy as np
import matplotlib as np
import math
import csv


x = input("Enter 'dual' dual boost converter or 'single' for single boost converter? ")

def single(vin1, vout1, fs1, Ioutmax1):      #Function for single stage boost converter
    D = (1 - ((vin1) * (.8)) / (vout1))   #Duty Cycle calculation
    diL = (0.2) * (Ioutmax1) * ((vout1) / (vin1))  #Change in inductor current calculation
    L = (vin1 * (vout1 - vin1)) / ((diL) * (fs1) * (vout1))  #Inductor calculation
    dvout = vout1 * 0.0005  #change in output voltage caclculation
    C = (Ioutmax1 * D) / (fs1 * dvout)  #capacitor calculation

    print("The value for you 1st stage inductor is ", float(L))
    print("The value of capacitor is ", float(C))
    print("The duty cycle of first stage booster is ", float(D))

    data=[float(vin1), float(vout1), float(fs1), float(Ioutmax1), float(diL),   #excel format for which the data will be stored
           float(D),float(C), float(L), float(dvout)]

    with open('Single Booster Data.csv',newline='') as f:   #opening and excel file for reading
        r = csv.read(f)
        data = [line for line in r]

    with open('Single Booster Data.csv', 'w',newline='') as f:   #writing the latest data in excel
        ssb = csv.writer(f)
        ssb.writerow(['Vin','Vout','Switching Freqeuncy','Output Current', 'diL',
                      'Duty Cycle','Capacitor', 'Inductor','dvout'])
        ssb.writerow(data)      
      
def dual(vin1, vout1, fs1, Ioutmax1, vin2, vout2, fs2, Ioutmax2):  #function for two stage boost converter
    D1 = (1 - ((vin1) * (.8)) / (vout1))
    diL1 = (0.2) * (Ioutmax1) * ((vout1) / (vin1))
    L1 = (vin1 * (vout1 - vin1)) / ((diL1) * (fs1) * (vout1))
    dvout1 = vout1 * 0.0005
    C1 = (Ioutmax1 * D1) / (fs1 * dvout1)

    D2 = 1 - ((vin2) * (.8)) / (vout2)
    diL2 = (0.2) * (Ioutmax2) * (vout2 / vin2)
    L2 = (vin2 * (vout2 - vin2)) / ((diL2) * (fs2) * (vout2))
    dvout2 = vout2 * 0.0005
    C2 = (Ioutmax2 * D2) / (fs2 * dvout2)
    
    data=[float(vin1), float(vout1), float(fs1), float(Ioutmax1),            #excel format for which the data will be stored
           float(diL1),float(D1), float(C1), float(L1), float(dvout1),
           float(vin2), float(vout2), float(fs2), float(Ioutmax2),
           float(diL2),float(D2), float(C2), float(L2), float(dvout2)]


    with open('SDual Booster Data.csv',newline='') as f:                 #opening and excel file for reading
        r = csv.read(f)
        data = [line for line in r]

    with open('Dual Booster Data.csv', 'w') as f:       #writing the latest data in excel
        ssb = csv.writer(f)
        ssb.writerow(['Vin1','Vout1','Switching Freqeuncy1','Output Current1', 'diL1',
                      'Duty Cycle1','Capacitor1', 'Inductor1','dvout','dvout1','vin2'
                      'vout2','Switching Freqency 2','Output Current2','diL2','Duty Cycle1'
                      'Capacitor2','Inductor2','dvout2'])
        ssb.writerow(data) 

    print("The value for you 1st stage inductor is ", float(L1))
    print("The value of capacitor is ", float(C1))
    print("The duty cycle of first stage booster is ", float(D1))

    print("The value of your inductor is ", float(L2))
    print("The value of capacitor is ", float(C2))
    print("The duty cycle of first stage booster is ", float(D2))

if x == 'single':       #Promotes user for information to do calculation for stage boost converter
    print("This is calculation for single boost converter.")
    vin1 = float(input("Please enter input voltage: "))
    vout1 = float(input("Please enter the output volatge your trying acheive: "))
    fs1 = float(input("Please enter the switching freqeuncy: "))
    Ioutmax1 = float(input("Please enter maximum output for current: "))
    single(vin1, vout1, fs1, Ioutmax1)
        
elif x == 'dual':       #Promotes user for information to do calculation for two stage boost converter
    print("This is calculation for dual boost converter.")
    vin1 = float(input("Please enter input voltage: "))
    vout1 = float(input("Please enter the output volatge your trying acheive: "))
    fs1 = float(input("Please enter the switching freqeuncy: "))
    Ioutmax1 = float(input("Please enter maximum output for current: "))

    vin2 = float(input("Please enter input voltage for the second stage: "))
    vout2 = float(input("Please enter the output volatge for the second stage: "))
    fs2 = float(input("Please enter the switching freqeuncy: "))
    Ioutmax2 = float(input("Please enter maximum output for current: "))
    dual(vin1, vout1, fs1, Ioutmax1, vin2, vout2, fs2, Ioutmax2)

else:
    print("No match.")

  



