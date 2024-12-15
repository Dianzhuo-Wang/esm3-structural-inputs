# Does Structural Information Improve ESM3 for Protein Binding Affinity Prediction?

This repository contains the code and data used in the paper "Does Structural Information Improve ESM3 for Protein Binding Affinity Prediction?" by Thomas Loux, Dianzhuo Wang, and Eugene Shakhnovich. The paper is available on [bioRxiv](https://www.biorxiv.org/content/10.1101/2024.12.09.627585v1).

# Installation and Setup Guide for Protein Structure Analysis Pipeline

## Software Requirements

### Core Programs

#### EvoEF2
* Repository: [EvoEF2](https://github.com/tommyhuangthu/EvoEF2)
* Follow repository instructions for compilation and installation
* CPU-only operation is sufficient

#### Rosetta (release-371)
* Download: [Rosetta Documentation](https://docs.rosettacommons.org/docs/latest/getting_started/Getting-Started)
* Primary use: Relax command 
* CPU-only operation is sufficient
* Requires academic or commercial license

#### Gromacs (2023)
* Installation guide: [Gromacs Manual](https://manual.gromacs.org/documentation/current/install-guide/index.html)
* CPU installation sufficient for energy minimization
* GPU required only if running full MD simulations
* Follow official compilation instructions

### Additional Requirements

#### ESM3 (Modified Version)
* Use custom fork: [Modified ESM3](https://github.com/thomasloux/esm3)
* Required for obtaining protein embeddings
* Note: One could also direct embedding with original ESM3 (evolutionaryscale/esm#2)

## System Requirements

* Platform: Validated on Harvard FASRC cluster
* Python Version: 3.11
* Hardware:
  * CPU required for all basic operations
  * GPU only needed for full MD simulations in Gromacs

## Structure Generation Pipeline

### Initial Setup
1. Download and install all required programs following their respective documentation
2. Compilation and installation may require significant time
3. Verify all installations before proceeding

### Dataset Processing

#### Desai Dataset
* Navigate to the protein-structures folder containing PDB files
* Follow README.md instructions precisely
* Process involves using EvoEF2, Rosetta Relax, and Gromacs energy-minimization

#### Bloom Dataset
* Use same pipeline as Desai dataset
* Modify EvoEF2 mutation parameters as needed
* Refer to dataset-specific documentation for parameter adjustments

## Important Notes

* Follow README.md instructions in protein-structures folder carefully
* Back up intermediate results regularly
* Computational requirements:
  * EvoEF2: CPU-only, lightweight
  * Rosetta Relax: CPU-only, moderate resources
  * Gromacs energy-minimization: CPU-only, moderate resources
  * Full MD simulations: Requires GPU installation

---

@article{loux2024more,
  title={More Structures, Less Accuracy: ESM3's Binding Prediction Paradox},
  author={Loux, Thomas and Wang, Dianzhuo and Shakhnovich, Eugene},
  journal={bioRxiv},
  pages={2024--12},
  year={2024},
  publisher={Cold Spring Harbor Laboratory}
}