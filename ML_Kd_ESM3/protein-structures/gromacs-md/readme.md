# Run MD simulaton
You can run the simulation on the cluster with the following command:
```bash
sbatch sbatch-run-on-gpu-md.sh rbd-only-6xf5 6xf5_rbd_only
```

All configuration files are inspired by Justin Lemkul's tutorials (http://www.mdtutorials.com/gmx/).

## to export 
% there are 50 000 frames so 50000-32768 = 17232
```bash
gmx_mpi trjconv -s prod.tpr -f prod.xtc -sep yes -dt 1 -b 17232 -o export/.pdb -center -pbc mol
```

You can then run the mv-md-frames.sh script to move the frames to the export folder.
