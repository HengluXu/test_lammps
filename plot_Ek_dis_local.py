#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def MaxwellBoltzmann(array,temp):
    beta=1000/(1.38*6.022*temp)     #1/(kB*T*NA), kJ/mol
    P=np.zeros(array.shape)         # P=2[(1/kT)^(3/2)]*[(E/pi)^(1/2)]*exp(-E/kT)

    for i,item in enumerate(array):
        P[i]=2*pow(beta,3/2)*np.sqrt(item/np.pi)*np.exp(-item*beta)
    return P
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def compute_Ek(filename,num_CH4):
    with open('./%s/linker109_C_linker32_C_qtz_relaxed_ch_00/CH4_velocities.dat'%filename) as fi:
        data=fi.readlines()
    # extract velocities    
    coords=[]
    for i,item in enumerate(data):
        if item.startswith('ITEM: ATOMS'):
            for j in range(1,1+num_CH4):
               coords.append(data[i+j].strip().split())
    coords=np.asarray(coords,dtype=float)
    print(coords.shape)
    # fix atom order, doesn't matter here
    # if want to trace a particular CH4, it should work
    for i in range(int(len(coords)/num_CH4)):
        coords_arg=np.argsort(coords[i*num_CH4:(i+1)*num_CH4,0])+i*num_CH4
        coords[i*num_CH4:(i+1)*num_CH4]=coords[coords_arg]  
    # compute kinetic energy
    Ek=np.sum((coords*coords)[:,2:5],axis=1)*16*10000/(2)
    np.savetxt('Ek_%s.txt'%(filename),Ek)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    # settings
    structure='linker109_C_linker32_C_qtz_relaxed_ch'
    # data list
    # compare
    list_data=[
        'NH_1CH4_100ns_298K',
        'NH_1CH4_200ns_298K',
        'NH_2CH4_100ns_298K',
        'NH_2CH4_200ns_298K',
        'NH_3CH4_100ns_298K',
        'NH_3CH4_200ns_298K',
        ]
    list_legend=list_data
    list_num=[1,1,2,2,3,3]#,8,16,160]

    list_color=['b','g','r','c','m','y','pink']

    # generate histogram
    x_range=20
    grid=100
    grid_size=x_range/grid

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    for index, filename in enumerate(list_data):
        # --> Ek_*.txt
        num_CH4=list_num[index]
        try:
            os.stat('Ek_%s.txt'%(filename))
        except:
            compute_Ek(filename, num_CH4)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# plot Ek distribution
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    array_grid=np.arange(0,x_range,grid_size)[:-1]
    P=MaxwellBoltzmann(array_grid, 298)

    plt.figure()

    array_temp=array_grid
    for index, filename in enumerate(list_data):
        temp=np.loadtxt('Ek_%s.txt'%(filename),dtype=float)
        n1, bin1, patch1 =plt.hist(temp,
                edgecolor=list_color[index], 
                facecolor="None",
                bins=np.arange(0,x_range,grid_size), 
                density=True)# alpha=0.35
        print(np.sum(n1)*grid_size)
        # collect density
        array_temp=np.concatenate((array_temp,n1))

    plt.plot(array_grid, P)#MaxwellBoltzmann(diff_all[:,0], 298))
    plt.legend(['T=298 K']+list_legend)

    plt.xlabel(r'kinetic energy of CH$_4$ molecules (kJ/mol)')
    plt.ylabel(r'# of molecules (normalized)')
    plt.savefig('Ek_dis.pdf',format='pdf')
    plt.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# plot difference between MD and theoretical distribution
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    diff_all=array_temp.reshape((len(list_data)+1,grid-1)).T
    np.savetxt('diff.txt',diff_all)

    file=open('integral_draft.txt', 'a+')

    fig,ax=plt.subplots()
    ax.axhline(0,color='black',lw=0.5, ls='--')
    for index in np.arange(0,len(list_data),1):
        temp_diff=diff_all[:,index+1]-P
        ax.plot(diff_all[:,0],
                temp_diff,
                color=list_color[index])
        temp_sum =grid_size*np.sum(np.absolute(temp_diff))
        file.write('%s %10f\n'%(format(list_data[index],"<30"),temp_sum))
        print(list_data[index])

    file.close()
    os.system('sort -n ./integral_draft.txt | uniq > integral_diff.txt')
    
    plt.legend(['']+list_legend)
    plt.xlabel(r'kinetic energy of CH$_4$ molecules (kJ/mol)')
    plt.ylabel(r'differences')
#    plt.ylim([-0.01,0.03])
    plt.title('Difference between # and theoretical distribution')
    plt.savefig('diff.pdf',format="pdf")
    plt.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
