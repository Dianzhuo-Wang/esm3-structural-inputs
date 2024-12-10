#! /bin/bash
#SBATCH -o log/analysis_%j.out
#SBATCH -e log/analysis_%j.err
#SBATCH -p gpu_requeue
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=1G
#SBATCH -t 0-12:00:00

module load gcc/13.2.0-fasrc01
module load cmake/3.27.5-fasrc01
module load intel-mkl/23.2.0-fasrc01
module load cuda/12.2.0-fasrc01
module load openmpi/4.1.5-fasrc03
export GROMACSHOME=/n/holylabs/LABS/shakhnovich_lab/Lab/gromacs-2023_installation/bin/
# export PATH=/net/shakfs1/shakfs1/share/plumed_installation/bin:$PATH
source $GROMACSHOME/GMXRC

export path=$1
export file_name=$2

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

bash prepare.sh $path $file_name

# Energy minimization: run on cpu
gmx_mpi grompp -f template/1.minim.mdp -c $path/$file_name-solv-ions.gro -p $path/topol.top -o $path/minim.tpr
gmx_mpi mdrun -deffnm $path/minim

# Equilibration constant volume: run on gpu
gmx_mpi grompp -f template/2.equil.nvt.mdp -c $path/minim.gro -p $path/topol.top -o $path/nvt.tpr -r $path/minim.gro
gmx_mpi mdrun -deffnm $path/nvt

# Equilibration constant pressure: run on gpu
gmx_mpi grompp -f template/3.equil.npt.mdp -c $path/nvt.gro -p $path/topol.top -o $path/npt.tpr -r $path/nvt.gro
gmx_mpi mdrun -deffnm $path/npt

# # Production: run on gpu
gmx_mpi grompp -f template/4.production.mdp -c $path/npt.gro -p $path/topol.top -o $path/prod.tpr -r $path/npt.gro
gmx_mpi mdrun -deffnm $path/prod