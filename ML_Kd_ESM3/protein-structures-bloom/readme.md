# Obtaining structures for RBD and variants from Bloom

You should follow the same instructions as in the protein-structures folder. The only difference is the buildMutant file that only generates single-mutant variants.

## Mutations

Don't forget to replace index 12 wt by the actual variant.
```bash
sbatch --array=1-3803 pipeline-rosetta.sh
```
