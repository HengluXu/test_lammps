# test lammps

## to-do
* nvt_CH4 submit calcs
* improve plot_Ek_dis.py

## lammps branch
Modified lammps [repo link](https://github.com/HengluXu/lammps.git)
``` bash
git branch name
    master
    master_print
        # print different `dof`
        dof_print   #  --> for testing dof
        # change `dof=3N`
        # print different `dof`
        dof_pull    # --> for use
        # change `dof=3N`
/path_to/lammps/src/lmp_${branch_name} -in in.*
```

## lammps command
```
compute_modify compute-ID extra/dof N dynamic/dof yes
```
Since `extra/dof` is applied to compute-ID, it should not affect the inner integration of particles, but only work on the outputs of thermodynamcal properties.

## simulations
* ./insert_CH4
* ./nvt_CH4
```bash
./run.sh
./process.sh
./clean.sh
```

## post-processing scripts
```bash
./convert_temp2Ek.py 16 298     # input: np, temperature
./plot_Ek_dis.py
```

## result analysis
The relationship between the following properties.
* Ek(tot)
* Ek(tot)_print
* temperature-target
* temperature-current
* temperature_print
* degree of freedom (DOF)
* degree of freedom (DOF)_constrained
* ?? compute_modify is working on ??
