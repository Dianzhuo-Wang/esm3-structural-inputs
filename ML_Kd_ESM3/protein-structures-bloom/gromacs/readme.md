run gromacs

sbatch --array=0-3802 sbatch-run-em.sh  

## Correction

MET as a starting or ending residue in the sequence is not recognized by gromacs. You need to interactively choose the correct residue name. N term : NH3+ and C term : COO-.

gmx_mpi pdb2gmx -f ../mutant-evoEf-6xf5/11/11.pdb -o ../mutant-evoEf-6xf5/11/11.gro -water tip3p -ignh -ff charmm36-jul2022 -p ../mutant-evoEf-6xf5/11/topol.top -i ../mutant-evoEf-6xf5/11/posre.itp -ter

gmx_mpi pdb2gmx -f ../mutant-evoEf-6xf5/3795/3795.pdb -o ../mutant-evoEf-6xf5/3795/3795.gro -water tip3p -ignh -ff charmm36-jul2022 -p ../mutant-evoEf-6xf5/3795/topol.top -i ../mutant-evoEf-6xf5/3795/posre.itp -ter