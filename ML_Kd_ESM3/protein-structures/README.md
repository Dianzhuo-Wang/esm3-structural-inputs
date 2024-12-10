# Obtaining structures for RBD and variants from Desai

Steps to obtain the structures:
1. Download the PDBs
2. Extract the RBD from the PDBs (relevant chain and residues at position 331 to 531 inclusive)
3. Mutate in-silico the residues of interest using EvoEF2
4. Minimize using either Rosetta or Gromacs

Additional independant tests:
- Compare to frames from MD simulation
- Add random noise to the structure 

## RBD structures

As far as this analysis was conducted, here are the PDB files available for the Cov555, S309, CB6, ACE2 complexes with RBD and isolated RBD. When needed, the RBD chain is explicitly mentioned. I did not find a simpler way to extract the RBD chain then manually checking the PDB files. I did not select the structures with missing residues for simplicity.

Cov555
- 7kmg: Wuhan variant with Cov 555
Note: Actually the problem is that there is only one PDB file with Cov 555.

S309
- 7soc: SARS-CoV-2 S RBD B.1.617.1 kappa variant with S309
- 7yad: S309-RBD for Omicron, chain C 
- 8vyg: SARS-CoV-2 S RBD (C.37 Lambda variant) with S309 (Lack residues between 473 to 482)
- 7xck: Cryo-EM structure of SARS-CoV-2 Omicron RBD in complex with S309 fab (local refinement), chain M
- 7xsw: Structure of SARS-CoV-2 antibody S309 with GX/P2V/2017 RBD (but missing residues)
- 7TLY: SARS-CoV-2 S B.1.1.529 Omicron variant with S309 (only one exactly in the dataset)
   - Note: this variant has missing residues around the interface. We might investigate missing residues later.

CB6 (Cov016)
- 7XEG: SARS-CoV-2-Beta-RBD with CB6
- 7XEI: SARS-CoV-2-prototyped-RBD (Wuhan) with CB6

ACE2
- 7WHH: SARS-CoV-2 S omiceron RBD with ACE2, RBD: chain E
- 7w9i: SARS-CoV-2 Delta S-RBD-ACE2, chain E

Isolated RBD (actually in a trimer state)
- 6XF5: Wuhan RBD in down state
- 6XF6: Wuhan RBD in up state (not used in the end)
Note: beware of missing residues in other trimer structures

## Alignment analysis
alignment-rbd.pdb is a multiple header pdb with align RBD extracted from multiple complexes (see the file for reference to the original PDBs).
-> They are all very similar. RMSD for all bound RBD (either with ACE2 or antibody) is around 0.4A (Pymol command align with 5 cycles). RMSD is around 0.6A for the isolated RBD (down state) 

## Extract only one chain 
Change A to the chain you want to extract
```bash
grep -E '^ATOM.{17}A' 6xf5.pdb > 6xf5_rbd_only.pdb
```
We take advantage of the fact that the chain is always at position 17 in the ATOM line.

## Keep only residues 331 to 531
Run keep-rbd-residues-in-spke-portein.py

## Run EvoEF2
You need first to create a variant.txt file containing the mutations you want to perform. This can be obtained by running buildMutantEvoEF-desai.py

Once you have the variants.txt file, you can run EvoEF2 with the following command:
```bash
srun -c 1 -n 1 -p shakhnovich /n/holyscratch01/shakhnovich_lab/thomasloux/shakhnovitch-research/ML_Kd_ESM3/EvoEF2/EvoEF2 --command=BuildMutant --pdb=../6xf5_rbd_only.pdb --mutant_file=../variants.txt
```
I use only one core since EvoEF2 is not parallelized. 

Possible mutations in Desai's dataset:
First letter is the reference, residue index in Spike Protein, Mutated residue
```
G339D
S371L
S373P
S375F
K417N
N440K
G446S
S477N
T478K
E484A
Q493R
G496S
Q498R
N501Y
Y505H
```

## Run Rosetta
You can run the following command to run Rosetta on the EvoEF2 output:
```bash
sbatch --array=1-32768 pipeline-rosetta.sh
```

# Run gromacs minimization
```bash
cd /n/holyscratch01/shakhnovich_lab/thomasloux/shakhnovitch-research/ML_Kd_ESM3/protein-structures/gromacs
sbatch --array=0-8191 sbatch-run-em.sh
# because we run 4 minimization per job serially
```

## Verify mutants
make sure to run check-sequence-pdbfiles.py
There is a bug with EvoEF2, if you mutate a pdb file but with 0 actual mutation, it will follow the next line.

I had to copy paste by hand the index 16385 (so folder called 16385)