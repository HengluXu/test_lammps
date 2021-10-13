#!/bin/bash

cpu=4
input='in.nh'

export OMP_NUM_THREADS=${cpu}

mpirun -np ${cpu} ${HOME}/Research/lammps-stable_29Oct2020/src/lmp_mpi -in ${input}
