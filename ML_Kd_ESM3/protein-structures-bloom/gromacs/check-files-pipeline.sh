export GROMACSHOME=/n/holylabs/LABS/shakhnovich_lab/Lab/gromacs-2023_installation/bin/
# export PATH=/net/shakfs1/shakfs1/share/plumed_installation/bin:$PATH
source $GROMACSHOME/GMXRC

number_variant=$(wc -l < ../variants.txt)

directory="../mutant-evoEf-6xf5"

for index in $(seq 1 $number_variant); do
	if [ ! -d "$directory/$index" ]; then
		echo "$index is not present"
	fi
    if [ ! -f "$directory/$index/${index}_minim_gromacs.pdb" ]; then
		echo "$index final relax is not present"
#         gmx_mpi trjconv -s ../mutant-evoEf-6xf5-rbd-only/$index/minim.tpr -f ../mutant-evoEf-6xf5-rbd-only/$index/minim.gro -o ../mutant-evoEf-6xf5-rbd-only/$index/${index}_minim_gromacs.pdb <<EOF
# 1
# 1
# EOF
        # sbatch sbatch-run-one-em.sh $index
        # sleep 1
	fi
	if (( index%500 == 0 )); then
		echo "step $index"
	fi
done 
