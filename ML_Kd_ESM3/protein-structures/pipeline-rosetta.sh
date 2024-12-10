#! /bin/bash
#SBATCH -o log/analysis_%j.out
#SBATCH -e log/analysis_%j.err
#SBATCH -p sapphire
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1000
#SBATCH -t 0-00:20:00

# Define input and output files
rosetta_home=/n/holylabs/LABS/shakhnovich_lab/Lab/rosetta/rosetta.source.release-371/main/source/bin

index=$SLURM_ARRAY_TASK_ID

cd mutant-evoEf-6xf5
cd $index

# Run minimization
$rosetta_home/relax.default.linuxgccrelease -s $index.pdb -nstruct 1 -relax:default_repeats 10 -out:suffix _first_relax
# output file is ${index}_first_relax_0001.pdb
mv ${index}_first_relax_0001.pdb ${index}_first_relax.pdb

