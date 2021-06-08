#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Canonical distribution at given temperature
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def MaxBolDis(arr_Ek,f_temp):
    '''
    N_A     =6.02214076×10^23 mol^(-1)   # Avogadro constant
    k_B     =1.38064852×10^(−23) J/K     # Boltzmann constant
    beta    =1/(kB*T*NA) kJ/mol

    P=2[(1/kT)^(3/2)]*[(E/pi)^(1/2)]*exp(-E/kT)
    '''
    beta=1000/(1.38064852*6.02214076*f_temp)
    arr_P=np.zeros(arr_Ek.shape)
    for i,item in enumerate(arr_Ek):
        arr_P[i]=2*pow(beta,3/2)*np.sqrt(item/np.pi)*np.exp(-item*beta)
    return arr_P
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def compute_Ek(int_np):
    with open('./CH4_velocities.dat') as fi:
        data=fi.readlines()
    # extract velocities
    list_coords=[]
    for i,item in enumerate(data):
        if item.startswith('ITEM: ATOMS'):
            for j in range(1,1+int_np):
               list_coords.append(data[i+j].strip().split())
    arr_coords=np.asarray(list_coords,dtype=float)
    print("There are %i data points in the histogram."%(arr_coords.shape)[0])
    # fix atom order, doesn't matter here
    # if want to trace a particular CH4, it should work
    for i in range(int(len(arr_coords)/int_np)):
        arr_coords_arg=np.argsort(arr_coords[i*int_np:(i+1)*int_np,0])+i*int_np
        arr_coords[i*int_np:(i+1)*int_np]=arr_coords[arr_coords_arg]
    # compute kinetic energy
    arr_Ek=np.sum((arr_coords*arr_coords)[:,2:5],axis=1)*16*10000/(2)
    np.savetxt('Ek_%i.txt'%int_np,arr_Ek)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    ## ./CH4_velocities.dat
    ## run by $*.py 16 298
    # SETTINGS
    NP=int(sys.argv[1])
    TEMPERATURE=float(sys.argv[2])

    # generate histogram
    lim_x=20
    grid_bin=100
    grid_size=lim_x/grid_bin

    # Ek_*.txt
    compute_Ek(NP)

    plt_Ek=np.arange(0,lim_x,grid_size)[:-1]
    plt_P=MaxBolDis(plt_Ek, TEMPERATURE)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# plot Ek distribution
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    plt.figure()

    # theoretical
    plt.plot(plt_Ek, plt_P)

    # Ek from MD, to generate histogram
    tmp=np.loadtxt('Ek_%i.txt'%(NP),dtype=float)
    n1, bin1, patch1 =plt.hist(tmp,
            edgecolor='m',
            facecolor="None",
            bins=np.arange(0,lim_x,grid_size),
            density=True)# alpha=0.35
    # collect density
    plt_Ek=np.concatenate((plt_Ek,n1))

    plt.legend(['T=%.1f K'%TEMPERATURE])
    plt.xlabel(r'kinetic energy of CH$_4$ molecules (kJ/mol)')
    plt.ylabel(r'# of molecules (normalized)')
    plt.savefig('Ek_dis.png',format='png')
    plt.close()

    print("Generate Ek distribution from CH4_velocities.dat\n")
    ave_Ek=np.average(tmp)
    print("Average Ek of   %s CH4   is   %.2f  kJ/mol"%(NP, ave_Ek))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# plot difference between MD and theoretical distribution
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    plt_Ek=plt_Ek.reshape((2,grid_bin-1)).T

    fig,ax=plt.subplots()
    ax.axhline(0,color='black',lw=0.5, ls='--')
    ax.plot(plt_Ek[:,0],
            plt_Ek[:,1]-plt_P,
            color="m")

    plt.xlabel(r'kinetic energy of CH$_4$ molecules (kJ/mol)')
    plt.ylabel(r'differences')
    plt.title('Difference between # and theoretical distribution')
    plt.savefig('Ek_diff.png',format="png")
    plt.close()
