#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np

def MethMW():
    return [32.04186,"kg/kmol"]

def MethTc():
    return [512.5,"K"]

def MethTp():
    return [8084000,"Pa"]

def MethNormBP():
    return [337.85,"K"]

def MethMP():
    return [175.47,"K"]

def MethTripT():
    return [175.47,"K"]

def MethTripP():
    return [0.111264,"Pa"]

def MethHf():
    return [-239.10,"kJ/mol"]

def MethLFLVol():
    return [7.18,"vol % in air"]

def MethLFL():
    return [283,"K"]

def MethUFLVol():
    return [36.5,"vol % in air"]

def MethUFL():
    return [314,"K"]

def MethAutoIgn():
    return [737,"K"]

def MethρL(T):
    A,B,C,D = [2.3267,0.27073,512.5,0.24713]
    return [A/(B**(1 + (1 - T/C)**D)),"kmol/m^3","175.47—512.5 K"]

def MethρV(T,P):
    R = 8.31447*1000
    return [P/(R*T),"kmol/m^3","Based on Ideal Gas Law"]

def MethCpV(T):
    A,B,C,D,E,F,G = [33257.89,36199,1205.7,15373000,3212.2,-15318000,3212.2]
    return [A + B*(((C/T)**2 * np.exp(C/T))/(np.exp(C/T) - 1)**2) + D*(((E/T)**2 * np.exp(E/T))/(np.exp(E/T) - 1)**2) + F*(((G/T)**2 * np.exp(G/T))/(np.exp(G/T) - 1)**2),"J/kmol*K","20-1500 K"]

def MethCpL(T):
    A,B,C,D,E = [256040,-2741.4,14.777,-0.035078,3.2719e-5]
    return [A + B*T + C*T**2 + D*T**3 + E*T**4,"J/kmol*K","175.47—503.15 K"]

def MethHvap(T):
    A,B,C,D,E = [32615000,-1.0407,1.8695,-0.60801,0]
    Tr = T/MethTc()[0]
    return [A*(1-Tr)**(B + C*Tr + D*Tr**2 + E*Tr**3),"J/kmol","175.47—512.5 K"]

def MethPsat(T):
    A,B,C,D,E = [82.718,-6904.5,-8.8622,7.4664e-6,2]
    return [np.exp(A + B/T + C*np.log(T) + D*T**E),"Pa","175.47—512.5 K"]

def MethμL(T):
    A,B,C,D,E = [-25.317,1789.2,2.069,0.0,0.0]
    return [np.exp(A + B/T + C*np.log(T) + D*T**E),"Pa*S","175.47—337.85 K"]

def MethμV(T):
    A,B,C,D = [3.0663e-7,0.69655,205,0.0]
    return [(A*T**B)/(1 + C/T + D/T**2),"Pa*s","240—1000 K"]

