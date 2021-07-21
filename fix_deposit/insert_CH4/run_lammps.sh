#!/bin/bash

cpu=4
input='in.*'

# export OMP_NUM_THREADS=${cpu}

mpirun -np ${cpu} ${HOME}/Research/lammps-29Oct20/src/lmp_mpi -in ${input}
