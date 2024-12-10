# Projet: assess the effects of structure information with ESM3

We will use the Desai dataset in order to evaluate that.


## Commands
Make sure to salloc a gpu first
```bash
python embed-different-structures.py --chain-id=A --embeddings-save-file-name=first_relax_rbd_mutated_WT_6xf5 --suffix-file-to-embed=_first_relax.pdb --directory-structure=protein-structures/mutant-evoEf-6xf5-rbd-only

python embed-different-structures.py --chain-id=A --embeddings-save-file-name=final_relax_rbd_mutated_WT_6xf5 --suffix-file-to-embed=_final_relax.pdb --directory-structure=protein-structures/mutant-evoEf-6xf5-rbd-only

python embed-different-structures.py --chain-id=A --embeddings-save-file-name=noisy_WT_6xf5 --suffix-file-to-embed=_noisy.pdb --directory-structure=protein-structures/6xf5-rbd-only-noisy

sbatch --dependency=afterok:43088845 sbatch-embed-different-structures.sh _minim_gromacs.pdb A minim_gromacs_mutated_6xf5 protein-structures/mutant-evoEf-6xf5-rbd-only
# Or
python embed-different-structures.py --chain-id="" --embeddings-save-file-name=minim_gromacs__WT_6xf5 --suffix-file-to-embed=_minim_gromacs.pdb --directory-structure=protein-structures/mutant-evoEf-6xf5-rbd-only

python embed-different-structures.py --chain-id="" --embeddings-save-file-name=no_relax_WT_6xf5 --suffix-file-to-embed=_correct_mutant_no_relax.pdb --directory-structure=protein-structures/mutant-evoEf-6xf5-rbd-only

####### I've just figured out the error in the code for "embed-different-structures.py" so I will re-run the following commands
sbatch sbatch-embed-different-structures.sh _minim_gromacs.pdb "" minim_gromacs_mutated_6xf5 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-different-structures.sh _correct_mutant_no_relax.pdb "" no_relax_WT_6xf5 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-different-structures.sh _noisy.pdb A noisy_WT_6xf5 protein-structures/6xf5-rbd-only-noisy df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-different-structures.sh _final_relax.pdb A final_relax_rbd_mutated_WT_6xf5 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-different-structures.sh _first_relax.pdb A first_relax_rbd_mutated_WT_6xf5 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-different-structures.sh _md_frame_WT.pdb ""  _md_frame_WT_6xf5 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-different-structures.sh _noisy_0.1.pdb "" noisy_WT_6xf5_01 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-different-structures.sh _noisy_0.05.pdb "" noisy_WT_6xf5_005 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-different-structures.sh _noisy.pdb A noisy_WT_6xf5_CORRECT protein-structures/6xf5-rbd-only-noisy df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-different-structures.sh _md_frame_WT.pdb ""  md_frame_WT_6xf5_CORRECT protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data
```

// this is for the serial version of the python script (not the batched one)
sbatch sbatch-embed-different-structures.sh _final_relax.pdb A serial_final_relax_rbd_mutated_WT_6xf5
sbatch sbatch-embed-different-structures.sh _first_relax.pdb A serial_first_relax_rbd_mutated_WT_6xf5 


## Download directly embeddings from GG drive
use gdown

## Embed sequence only

```bash
python embed-sequence-only.py --embeddings-save-file-name=esm3 --sequences-to-embed=single_mutant_bloom_sequences.npy --folder-for-embeddings=data-bloom
```

## Embed different structures for Bloom dataset

```bash
sbatch sbatch-embed-different-structures.sh _minim_gromacs.pdb "" minim_gromacs_mutated_6xf5 protein-structures-bloom/mutant-evoEf-6xf5 single_mutant_bloom_sequences.npy data-bloom
```

## Embed same structure but entire complex
    
```bash
# For the Desai dataset
sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures/7kmg.pdb C,A,B 7kmg_desai.pt df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures/7soc.pdb A,L,H 7soc_desai.pt df_Desai_15loci_sequence.npy data

## sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures/7tly.pdb I,B,A 7tly_desai.pt df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures/7w9i.pdb E,A 7w9i_desai.pt df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures/7whh.pdb E,A 7whh_desai.pt df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures/7xck.pdb M,B,A 7xck_desai.pt df_Desai_15loci_sequence.npy data

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures/7xeg.pdb A,D,C 7xeg_desai.pt df_Desai_15loci_sequence.npy data




# For the Bloom dataset
sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures-bloom/7kmg.pdb C,A,B 7kmg_bloom.pt single_mutant_bloom_sequences.npy data-bloom

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures-bloom/7soc.pdb A,L,H 7soc_bloom.pt single_mutant_bloom_sequences.npy data-bloom

## sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures-bloom/7tly.pdb I,B,A 7tly_bloom.pt single_mutant_bloom_sequences.npy data-bloom

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures-bloom/7w9i.pdb E,A 7w9i_bloom.pt single_mutant_bloom_sequences.npy data-bloom

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures-bloom/7whh.pdb E,A 7whh_bloom.pt single_mutant_bloom_sequences.npy data-bloom

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures-bloom/7xck.pdb M,B,A 7xck_bloom.pt single_mutant_bloom_sequences.npy data-bloom

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures-bloom/7xeg.pdb A,D,C 7xeg_bloom.pt single_mutant_bloom_sequences.npy data-bloom
```

## Embed for mean and max pooling

```bash
# For the Desai dataset

## Different structures
sbatch sbatch-embed-different-structures.sh _minim_gromacs.pdb "" minim_gromacs_mutated_6xf5 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data-with-max-pooling

sbatch sbatch-embed-different-structures.sh _correct_mutant_no_relax.pdb "" no_relax_WT_6xf5 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data-with-max-pooling

sbatch sbatch-embed-different-structures.sh _noisy_0.1.pdb "" noisy_WT_6xf5 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data-with-max-pooling

sbatch sbatch-embed-different-structures.sh _first_relax.pdb A first_relax_rbd_mutated_WT_6xf5 protein-structures/mutant-evoEf-6xf5-rbd-only df_Desai_15loci_sequence.npy data-with-max-pooling

## Same structure
sbatch 2.sbatch-embed-same-structure.sh protein-structures/6xf5.pdb A Isolated_WT_down_state_6xf5.pt df_Desai_15loci_sequence.npy data-with-max-pooling

sbatch 2.sbatch-embed-same-structure.sh protein-structures/7kmg.pdb C 7kmg_desai.pt df_Desai_15loci_sequence.npy data-with-max-pooling

sbatch 2.sbatch-embed-same-structure.sh protein-structures/7soc.pdb A 7soc_desai.pt df_Desai_15loci_sequence.npy data-with-max-pooling

sbatch 2.sbatch-embed-same-structure.sh protein-structures/7w9i.pdb E 7w9i_desai.pt df_Desai_15loci_sequence.npy data-with-max-pooling

## Whole complex
sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures/7kmg.pdb C,A,B 7kmg_desai.pt df_Desai_15loci_sequence.npy data-with-max-pooling

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures/7soc.pdb A,L,H 7soc_desai.pt df_Desai_15loci_sequence.npy data-with-max-pooling

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures/7w9i.pdb E,A 7w9i_desai.pt df_Desai_15loci_sequence.npy data-with-max-pooling

# For the Bloom dataset
sbatch sbatch-embed-different-structures.sh _minim_gromacs.pdb "" minim_gromacs_mutated_6xf5 protein-structures-bloom/mutant-evoEf-6xf5 single_mutant_bloom_sequences.npy data-bloom-with-max-pooling

sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7kmg.pdb C 7kmg_bloom.pt single_mutant_bloom_sequences.npy data-bloom-with-max-pooling

sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7soc.pdb A 7soc_bloom.pt single_mutant_bloom_sequences.npy data-bloom-with-max-pooling

sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7w9i.pdb E 7w9i_bloom.pt single_mutant_bloom_sequences.npy data-bloom-with-max-pooling

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures-bloom/7kmg.pdb C,A,B 7kmg_bloom.pt single_mutant_bloom_sequences.npy data-bloom-with-max-pooling

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures-bloom/7soc.pdb A,L,H 7soc_bloom.pt single_mutant_bloom_sequences.npy data-bloom-with-max-pooling

sbatch sbatch-embed-same-structure-entire-complex.sh protein-structures-bloom/7w9i.pdb E,A 7w9i_bloom.pt single_mutant_bloom_sequences.npy data-bloom-with-max-pooling
```