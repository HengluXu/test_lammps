# test lammps

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

## directory
### ./insert_CH4
### ./nvt_CH4

* MFI structures, 16 CH4

## scripts
```bash
./convert_temp2Ek.py 16 298     # input: np, temperature
./plot_Ek_dis.py
```
