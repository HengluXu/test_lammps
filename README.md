# TEST LAMMPS

## STANDARDIZED INPUT
* ./nvt_CuBTC_Ar_NP40
* ./gcmc_CuBTC_Xe
    * dynamic dof
    * hybrid nvt
* ./cvt_data2lammpstrj


## temp files
tests of different lammps commands

* fix adapt
* fix deposit
* restart
* ps: post-processing scripts
    * ./convert_temp2Ek.py NP temperature
    * ./plot_Ek_dis.py NP temperature
    * ./compute_log_thermo.py NP temperature

## fix deposit
## fix adapt
