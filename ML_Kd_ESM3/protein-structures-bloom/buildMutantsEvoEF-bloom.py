import subprocess
import numpy as np
# Load sequences
folder_save = '../data-bloom/'
sequences = np.load(folder_save + 'single_mutant_bloom_sequences.npy', allow_pickle=True)
# For now only mutate 6xf5
file_to_mutate= '6xf5_rbd_only.pdb'
chain_rbd = 'A'


rbd_residue_index_starting_desai_sequences = 331
rbd_residue_index_ending_desai_sequences = 531 # included

unique_aa = np.sort(np.unique([seq[0] for seq in sequences[:25]]))
aa_to_index = {aa: index for index, aa in enumerate(unique_aa)}

wt_sequence = "NITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKST"
wt_sequence_encoding = np.array([aa_to_index[a] for a in wt_sequence])

index_wt = 11

assert sequences[index_wt] == wt_sequence

# Transform to letter for fast detection of mutations
one_hot_encoding = np.stack([[aa_to_index[a] for a in seq] for seq in sequences])
is_mutated = ((one_hot_encoding - wt_sequence_encoding.reshape(1, -1)) != 0)

with open("variants.txt", "w") as f:
    for ind, mutated in enumerate(is_mutated):
        listMutations = [f"{wt_sequence[i]}{chain_rbd}{i+rbd_residue_index_starting_desai_sequences}{sequences[ind][i]}" for i in range(len(wt_sequence)) if mutated[i]]
        f.write(",".join(listMutations) + ";" + "\n")




# Run the script
# mkdir mutant-evoEf
# cd mutant-evoEf
# EvoEF2 --command=BuildMutant --pdb=../6xf5_rbd_only.pdb --mutant_file=../variants.txt

