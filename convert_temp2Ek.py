#!/usr/bin/env python
# coding: utf-8

import os
import sys

def convert_temp2Ek(np,temp):
    Ek_ExForce=(0.5*1.38064852*6.02214076*temp)*(3*np)/(1000*4.184)
    Ek_NoExForce=(0.5*1.38064852*6.02214076*temp)*(3*np-3)/(1000*4.184)
    print("At %.2f K, Ek(tot) of %i CH4 is:"%(temp,np))
    print("with external field, \t\t %.4f\t kcal/mol"%(Ek_ExForce))
    print("without external field, \t %.4f\t kcal/mol"%(Ek_NoExForce))
    return 0

if __name__ == '__main__':

    '''
    Ek(tot)=(1/2*k_B*T*N_A)*N(DOF)  # kJ/mol
    Ek(tot)/(10^3*4.184)            # kcal/mol
    N_A=6.02214076×10^23 mol^(-1)   # Avogadro constant
    k_B=1.38064852×10^(−23) J/K     # Boltzmann constant
    '''

    np=int(sys.argv[1])
    temp=float(sys.argv[2])

    convert_temp2Ek(np,temp)
