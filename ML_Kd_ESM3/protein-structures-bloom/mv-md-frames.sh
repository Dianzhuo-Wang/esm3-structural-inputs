for i in {1..3803}; do
    mv ../protein-structures/gromacs-md/rbd-only-6xf5/export/${i}.pdb mutant-evoEf-6xf5/${i}/${i}_md_frame_WT.pdb
    if (( i%1000 == 0 )); then
        echo "Moved ${i} frames"
    fi
done