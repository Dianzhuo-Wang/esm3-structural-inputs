#! /bin/bash
#SBATCH -o log/analysis_%j.out
#SBATCH -e log/analysis_%j.err
#SBATCH -p sapphire
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH -t 0-01:40:00


module load gcc/13.2.0-fasrc01
module load cmake/3.27.5-fasrc01
module load intel-mkl/23.2.0-fasrc01
module load cuda/12.2.0-fasrc01
module load openmpi/4.1.5-fasrc03
export GROMACSHOME=/n/holylabs/LABS/shakhnovich_lab/Lab/gromacs-2023_installation/bin/
# export PATH=/net/shakfs1/shakfs1/share/plumed_installation/bin:$PATH
source $GROMACSHOME/GMXRC

export path=/n/holyscratch01/shakhnovich_lab/thomasloux/shakhnovitch-research/ML_Kd_ESM3/protein-structures-bloom/mutant-evoEf-6xf5
export replicas=1
export index=$((SLURM_ARRAY_TASK_ID*replicas+1))

export GMX_MAXBACKUP=-1

run-em () {
    local path=$1
    local index=$2
    if [ ! -d "$path" ]; then
        echo "$index is not present"
        return
    fi
    if [ -f "$path/minim.gro" ]; then
        echo "$index already minimized"
        return
    fi
    bash prepare.sh $path
    # Energy minimization: run on cpu
    gmx_mpi grompp -f 1.minim.mdp -c $path/$index-solv-ions.gro -p $path/topol.top -o $path/minim.tpr
    gmx_mpi mdrun -deffnm $path/minim

    # output pdb with only the protein
    gmx_mpi trjconv -s $path/minim.tpr -f $path/minim.gro -o $path/${index}_minim_gromacs.pdb <<EOF
1
1
EOF
}

for i in $(seq 0 $((replicas-1)))
do
    run-em $path/$((index+i)) $((index+i))
done