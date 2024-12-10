#! /bin/bash
#SBATCH -o log/analysis_%j.out
#SBATCH -e log/analysis_%j.err
#SBATCH -p sapphire
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=1G
#SBATCH -t 0-00:40:00


module load gcc/13.2.0-fasrc01
module load cmake/3.27.5-fasrc01
module load intel-mkl/23.2.0-fasrc01
module load cuda/12.2.0-fasrc01
module load openmpi/4.1.5-fasrc03
export GROMACSHOME=/n/holylabs/LABS/shakhnovich_lab/Lab/gromacs-2023_installation/bin/
# export PATH=/net/shakfs1/shakfs1/share/plumed_installation/bin:$PATH
source $GROMACSHOME/GMXRC

export path=/n/holyscratch01/shakhnovich_lab/thomasloux/shakhnovitch-research/ML_Kd_ESM3/protein-structures/mutant-evoEf-6xf5-rbd-only
export index=$1

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

run-em () {
    local path=$1
    local index=$2
    if [ -f "$path/minim.gro" ]; then
        echo "$index already minimized"
        return
    fi
    bash prepare.sh $path
    # Energy minimization: run on cpu
    gmx_mpi grompp -f 1.minim.mdp -c $path/$index-solv-ions.gro -p $path/topol.top -o $path/minim.tpr
    gmx_mpi mdrun -deffnm $path/minim

    # output pdb with only the protein
    gmx_mpi editconf -f $path/minim.gro -o $path/${index}_minim_gromacs.pdb
}

run-em $path/$index $index