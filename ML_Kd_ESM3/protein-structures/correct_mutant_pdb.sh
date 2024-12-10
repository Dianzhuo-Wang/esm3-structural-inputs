#! /bin/bash
#SBATCH -o log/analysis_%j.out
#SBATCH -e log/analysis_%j.err
#SBATCH -p sapphire
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1000
#SBATCH -t 0-00:30:00

module load gcc/13.2.0-fasrc01
module load cmake/3.27.5-fasrc01
module load intel-mkl/23.2.0-fasrc01
module load cuda/12.2.0-fasrc01
module load openmpi/4.1.5-fasrc03
export GROMACSHOME=/n/holylabs/LABS/shakhnovich_lab/Lab/gromacs-2023_installation/bin/
# export PATH=/net/shakfs1/shakfs1/share/plumed_installation/bin:$PATH
source $GROMACSHOME/GMXRC

export path=/n/holyscratch01/shakhnovich_lab/thomasloux/shakhnovitch-research/ML_Kd_ESM3/protein-structures/mutant-evoEf-6xf5-rbd-only
export replicas=256
export index=$((SLURM_ARRAY_TASK_ID*replicas+1))
export directory="mutant-evoEf-6xf5-rbd-only"

for i in $(seq $index $(($index+$replicas-1)))
do
    # echo $directory/$i/${i}.gro
    gmx_mpi editconf -f $directory/$i/${i}.gro -o $directory/$i/${i}_correct_mutant_no_relax.pdb
done
