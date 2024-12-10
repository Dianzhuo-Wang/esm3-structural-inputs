export GROMACSHOME=/n/holylabs/LABS/shakhnovich_lab/Lab/gromacs-2023_installation/bin/
# export PATH=/net/shakfs1/shakfs1/share/plumed_installation/bin:$PATH
source $GROMACSHOME/GMXRC

for index in {1..32768}; do
	if [ ! -d "mutant-evoEf-6xf5-rbd-only/$index" ]; then
		echo "$index is not present"
	fi
    # if [ ! -f "mutant-evoEf-6xf5-rbd-only/6xf5_rbd_only_Model_${index}_RBD.pdb" ]; then
	# 	echo "$index PDB is not present"
	# fi
    # if [ ! -f "mutant-evoEf-6xf5-rbd-only/$index/${index}_first_relax.pdb" ]; then
	# 	echo "$index first relax is not present"
	# fi
    if [ ! -f "mutant-evoEf-6xf5-rbd-only/$index/${index}_correct_mutant_no_relax.pdb" ]; then
		echo "$index final relax is not present"
        # gmx_mpi editconf -f mutant-evoEf-6xf5-rbd-only/$index/${index}.gro -o mutant-evoEf-6xf5-rbd-only/$index/${index}_correct_mutant_no_relax.pdb
        # sbatch gromacs/sbatch-run-one-em.sh $index
	fi
	if (( index%1500 == 0 )); then
		echo "step $index"
	fi
done 
