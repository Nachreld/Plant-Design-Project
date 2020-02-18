#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np

def DMEMW():
    return [46.06844,"kg/kmol"]

def DMETc():
    return [400.1,"K"]

def DMETp():
    return [5370000,"Pa"]

def DMENormBP():
    return [248.31,"K"]

def DMEMP():
    return [131.66,"K"]

def DMETripT():
    return [131.65,"K"]

def DMETripP():
    return [3.04959,"Pa"]

def DMEHf():
    return [-184.10,"kJ/mol"]

def DMELFLVol():
    return [3.3,"vol % in air"]

def DMELFL():
    return [191.3,"K"]

def DMEUFLVol():
    return [26.2,"vol % in air"]

def DMEUFL():
    return [221.3,"K"]

def DMEAutoIgn():
    return [499.15,"K"]

def DMEρL(T):
    A,B,C,D = [1.5693,0.2679,400.1,0.2882]
    return [A/(B**(1 + (1 - T/C)**D)),"kmol/m^3","131.65—400.1 K"]

def DMEρV(T,P):
    R = 8.31447*1000
    return [P/(R*T),"kmol/m^3","Based on Ideal Gas Law"]

def DMECpV(T):
    A,B,C,D,E,F,G = [33257.8886,25892.87252,383.550806,73860.952768,1606.474746,64223.377662,3686.558861]
    return [A + B*(((C/T)**2 * np.exp(C/T))/(np.exp(C/T) - 1)**2) + D*(((E/T)**2 * np.exp(E/T))/(np.exp(E/T) - 1)**2) + F*(((G/T)**2 * np.exp(G/T))/(np.exp(G/T) - 1)**2),"J/kmol*K","20—1500 K"]

def DMECpL(T):
    A,B,C,D,E = [110100,-157.47,0.51853,0.0,0.0]
    return [A + B*T + C*T**2 + D*T**3 + E*T**4,"J/kmol*K","131.65—250 K"]

def DMEHvap(T):
    A,B,C,D,E = [26377000,-0.072806,0.54324,-0.13977,0.0]
    Tr = T/DMETc()[0]
    return [A*(1-Tr)**(B + C*Tr + D*Tr**2 + E*Tr**3),"J/kmol","131.65—400.1 K"]

def DMEPsat(T):
    A,B,C,D,E = [44.704,-3525.6,-3.4444,5.4574E-17,6]
    return [np.exp(A + B/T + C*np.log(T) + D*T**E),"Pa","131.65—400.1 K"]

def DMEμL(T):
    A,B,C,D,E = [-10.62,448.99,8.3967E-05,0.0,0.0]
    return [np.exp(A + B/T + C*np.log(T) + D*T**E),"Pa*S","131.65—248.31 K"]

def DMEμV(T):
    A,B,C,D = [2.68e-6,0.3975,534,0.0]
    return [(A*T**B)/(1 + C/T + D/T**2),"Pa*s","131.65—1000 K"]

