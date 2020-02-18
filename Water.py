#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np

def WatMW():
    return [18.01528,"kg/kmol"]

def WatTc():
    return [647.096,"K"]

def WatTp():
    return [22064000,"Pa"]

def WatNormBP():
    return [373.15,"K"]

def WatMP():
    return [273.15,"K"]

def WatTripT():
    return [273.16,"K"]

def WatTripP():
    return [611.73,"Pa"]

def WatHf():
    return [-285.83,"kJ/mol"]

def WatLFLVol():
    return "You're an Idiot"

def WatLFL():
    return "You're an Idiot"

def WatUFLVol():
    return "You're an Idiot"

def WatUFL():
    return "You're an Idiot"

def WatAutoIgn():
    return "You're an Idiot"

def WatρL(T):
    A,B,C,D,E = [-13.851,0.64038,-0.0019124,1.8211e-6,0.0]
    return [A + B*T + C*T**2 + D*T**3 + E*T**4,"kmol/m^3","273.16—353.15 K"]

def WatρV(T,P):
    R = 8.31447*1000
    return [P/(R*T),"kmol/m^3","Based on Ideal Gas Law"]

def WatCpV(T):
    A,B,C,D,E = [33363,26790,2610.5,8896,1169]
    return [A + B*((C/T)/np.sinh(C/T))**2 + D*((E/T)/np.cosh((E/T)))**2,"J/kmol*K","100—2273.15 K"]

def WatCpL(T):
    A,B,C,D,E = [276370,-2090.1,8.125,-0.014116,9.3701e-6]
    return [A + B*T + C*T**2 + D*T**3 + E*T**4,"J/kmol*K","273.16—533.15 K"]

def WatHvap(T):
    A,B,C,D,E = [56600000,0.612041,-0.625697,0.398804,0.0]
    Tr = T/WatTc()[0]
    return [A*(1-Tr)**(B + C*Tr + D*Tr**2 + E*Tr**3),"J/kmol","273.16—647.096 K"]

def WatPsat(T):
    A,B,C,D,E = [73.649,-7258.2,-7.3037,4.1653e-6,2]
    return [np.exp(A + B/T + C*np.log(T) + D*T**E),"Pa","273.16—647.096 K"]

def WatμL(T):
    A,B,C,D,E = [-52.843,3703.6,5.866,-5.879e-29,10]
    return [np.exp(A + B/T + C*np.log(T) + D*T**E),"Pa*S","273.16—646.15 K"]

def WatμV(T):
    A,B,C,D = [1.7096e-8,1.1146,0.0,0.0]
    return [(A*T**B)/(1 + C/T + D/T**2),"Pa*s","273.16—1073.15 K"]

