# Does Structural Information Improve ESM3 for Protein Binding Affinity Prediction?

This repository contains the code and data used in the paper "Does Structural Information Improve ESM3 for Protein Binding Affinity Prediction?" by Thomas Loux, Dianzhuo Wang, and Eugene Shakhnovich. The paper is available on [bioRxiv]().

## Requirements

I run the code on the Harvard FASRC cluster. The code is written in Python 3.11
You will need the following programs:
EvoEF2 : https://github.com/tommyhuangthu/EvoEF2
Rosetta (release-371): https://docs.rosettacommons.org/docs/latest/getting_started/Getting-Started
Gromacs (2023 version): https://manual.gromacs.org/documentation/current/install-guide/index.html
All these programs need to be compiled and installed on your system, which may take some time. You should follow the instructions on their respective websites. The EvoEF2, Rosetta Relax command and Gromacs energy-minimization are not too computationally intensive, it can run on CPU only. If you ever want to run actual MD simulations with Gromacs, you will need GPU installation.

Regarding ESM3, one need to obtain a embedding from a protein. After this work was done, I've realised you can do it easily directly from ESM3 (https://github.com/evolutionaryscale/esm/issues/2). I've actually slightly modified the code on my own to do it, so that you need to install my version (https://github.com/thomasloux/esm3) if you want to reproduce the results.

## Structures
The complete pipeline to obtain structures is not fully automated. You should carefully follow the instructions in the README.md file in the protein-structures folder that contains the PDB files for Desai dataset. Only the actual mutation with EvoEF2 will change for Bloom dataset.

