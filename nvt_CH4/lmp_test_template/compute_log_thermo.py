#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np

NP=int(sys.argv[1])
TEMPERATURE=float(sys.argv[2])

data=np.loadtxt("./thermo.txt",dtype=float)[1000:]
Ek=np.loadtxt("./Ek_%i.txt"%NP,dtype=float)

with open('Average_thermo_pps.txt','w') as fp:
    fp.write('Canonical distribution\n')
    fp.write('\t temp       %.2f K\n'%(TEMPERATURE))
    fp.write('\t ke         %.2f kJ/mol\n'%(1.5*1.38064852*6.02214076*TEMPERATURE/1000))
    fp.write('# LAMMPS SETUP\n')
    fp.write('# compute         allTemp all temp\n')
    fp.write('# compute         CH4Temp CH4 temp\n')
    fp.write('# compute         framTemp fram temp \n')
    fp.write('# compute         CH4ke CH4 ke \n')
#    fp.write('# thermo_style    custom atoms step temp c_allTemp c_CH4Temp c_framTemp ke c_CH4ke v_CH4Vcm v_CH4Xcm\n')
    fp.write('Average properties calculated from log.lammps thermo output\n')
    fp.write('\t temp       %.2f K\n'%(np.average(data[:,2])))
    fp.write('\t alltemp    %.2f K\n'%(np.average(data[:,3])))
    fp.write('\t CH4temp    %.2f K\n'%(np.average(data[:,4])))
    fp.write('\t framtemp   %.2f K\n'%(np.average(data[:,5])))
    fp.write('\t ke         %.2f kJ/mol\n'%(np.average(data[:,6])*4.184/NP))
    fp.write('\t CH4ke      %.2f kJ/mol\n'%(np.average(data[:,7])*4.184/NP))
    fp.write('\t fixTemp    %.2f k\n'%(np.average(data[:,8])))
    fp.write('Average Ek calculated from CH4_velocities.dat\n')
    fp.write('\t ke         %.2f kJ/mol\n'%(np.average(Ek)))
