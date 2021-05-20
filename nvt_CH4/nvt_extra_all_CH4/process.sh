#!/bin/bash

NP=16
TEMPERATURE=298

source ~/venv_python3/bin/activate

echo -e "## Calculate Ek distribution and average Ek from lammps trajectory (CH4_velocities.dat)\n"
./plot_Ek_dis_local.py ${NP} ${TEMPERATURE}

echo -e "\n## Calculate average thermo properties from log.lammps (thermo commands)\n"
grep -e '\s\+320\+\s\+[0-9]' log.lammps > thermo.txt
./compute_log_thermo.py ${NP} ${TEMPERATURE}

echo -e "Results in Average_thermo_pps.txt"
echo -e "Ek distribution in Ek_dis.png"
