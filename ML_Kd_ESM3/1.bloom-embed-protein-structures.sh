export sequences_to_embed="single_mutant_bloom_sequences.npy"
export folder_for_embeddings="data-bloom"

# sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/6xf5.pdb A Isolated_WT_down_state_6xf5.pt $sequences_to_embed $folder_for_embeddings
# sleep 2
# sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7kmg.pdb C Cov555_WT_7kmg.pt $sequences_to_embed $folder_for_embeddings
# sleep 2
# sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7soc.pdb A S309_kappa_7soc.pt  $sequences_to_embed $folder_for_embeddings
# sleep 2
# sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7whh.pdb E ACE2_omicron_7whh.pt $sequences_to_embed $folder_for_embeddings
# sleep 2
sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7tly.pdb I S309_omicron_7tly.pt $sequences_to_embed $folder_for_embeddings
sleep 2 ## There has been a problem with this one. #44167479
# sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7xeg.pdb A CB6_beta_7xeg.pt $sequences_to_embed $folder_for_embeddings
# sleep 2
# sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7xei.pdb A CB6_WT_7xei.pt $sequences_to_embed $folder_for_embeddings
# sleep 2
# sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7yad.pdb M S309_Omicron_7yad.pt $sequences_to_embed $folder_for_embeddings
# sleep 2
# sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7xck.pdb M S309_Omicron_7xck.pt $sequences_to_embed $folder_for_embeddings
# sleep 2
# sbatch 2.sbatch-embed-same-structure.sh protein-structures-bloom/7w9i.pdb E ACE2_Delta_7w9i.pt $sequences_to_embed $folder_for_embeddings
# sleep 2