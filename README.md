# TEST LAMMPS

tests of different lammps commands

* fix adapt
* fix deposit
* fix gcmc
* fix nvt
* restart
* ps: post-processing scripts
    * ./convert_temp2Ek.py NP temperature
    * ./plot_Ek_dis.py NP temperature
    * ./compute_log_thermo.py NP temperature

## fix gcmc


## fix deposit
## fix adapt


## fix nvt
```
fix ID Group nvt temp ...
compute_modify fix-ID_temp extra/dof N
```
One should be clear that different modifications work on different variables, e.g. fix-ID_temp, compute-ID, thermo_temp etc.

In each test directory, three `bash` scripts to execute
```bash
./run.sh
./process.sh
./clean.sh
```
<!--
## lammps branch
Modified lammps source code [(repo link)](https://github.com/HengluXu/lammps.git)
* master
* master_print    # print different `dof`
* dof_print       #  -> for testing dof
    * change `dof=3N`
    * print different `dof`
-->
