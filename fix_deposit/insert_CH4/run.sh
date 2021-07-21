#!/bin/bash 

cpu=4
input='in.*'

# export OMP_NUM_THREADS=${cpu}

mpirun -np ${cpu} ~/Research/lammps/src/lmp_master -in ${input}
