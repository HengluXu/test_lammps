# test for `dof` in lammps

## lammps branch
* master
* master_print
    * print different `dof`
* dof_print
    * change `dof=3N`
    * print different `dof`
* dof_pull
    * change `dof=3N`

## input
* MFI structures, 16 CH4


## scripts
* `./convert_temp2Ek.py`
    * $*.py NP temperature
    * $*.py 16 298
