for i in {1..32768}; do
    mv gromacs-md/rbd-only-6xf5/export/${i}.pdb mutant-evoEf-6xf5-rbd-only/${i}/${i}_md_frame_WT.pdb
    if (( i%5000 == 0 )); then
        echo "Moved ${i} frames"
    fi
done