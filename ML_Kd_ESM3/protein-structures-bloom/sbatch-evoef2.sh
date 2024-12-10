#! /bin/bash
#SBATCH -o log/analysis_%j.out
#SBATCH -e log/analysis_%j.err
#SBATCH -p shakhnovich
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4000
#SBATCH -t 1-00:00:00
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=thomas.loux@polytechnique.edu

/n/holyscratch01/shakhnovich_lab/thomasloux/shakhnovitch-research/ML_Kd_ESM3/EvoEF2/EvoEF2 --command=BuildMutant --pdb=../6xf5_rbd_only.pdb --mutant_file=../variants.txt