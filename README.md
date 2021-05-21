# test lammps

## to-do
* print degree of freedom (DOF)
* print degree of freedom (DOF)_constrained

## lammps branch
Modified lammps source code [(repo link)](https://github.com/HengluXu/lammps.git)
``` bash
git branch -a
    master
    master_print    # print different `dof`
    dof_print       #  --> for testing dof
        # change `dof=3N`
        # print different `dof`
    dof_pull        # --> for use
        # change `dof=3N`
mpirun -np 4 /path_to/lammps/src/lmp_${branch_name} -in in.*
```

### testing of lammps commands
`compute_modify compute-ID extra/dof N dynamic/dof yes`
* Since `extra/dof` is applied to compute-ID, it should not affect the inner integration of particles, but only work on the outputs of thermodynamical properties.

## MD tests
In each test directory, three `bash` scripts to execute
```bash
./run.sh
./process.sh
./clean.sh
```

* ./nvt_CH4
    * data.MFI_CH4
    * in.MFI_CH4
* ./insert_CH4
    * inserting CH4 into frameworks, preparation for NVT simulation.
* post-processing scripts
    * ./convert_temp2Ek.py NP temperature
    * ./plot_Ek_dis.py NP temperature
    * ./compute_log_thermo.py NP temperature
