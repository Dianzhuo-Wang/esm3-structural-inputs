import numpy as np
# Load sequences
folder_save = '../data/'
sequences = np.load(folder_save + 'df_Desai_15loci_sequence.npy', allow_pickle=True)
# For now only mutate 6xf5
file_to_mutate = '6xf5.pdb'
chain_rbd = 'A'

# Load possible mutations
# index 0 is the wildtype amino acid, index 1 is the mutant amino acid
possible_mutations = {
    339: ['G', 'D'],
    371: ['S', 'L'],
    373: ['S', 'P'],
    375: ['S', 'F'],
    417: ['K', 'N'],
    440: ['N', 'K'],
    446: ['G', 'S'],
    477: ['S', 'N'],
    478: ['T', 'K'],
    484: ['E', 'A'],
    493: ['Q', 'R'],
    496: ['G', 'S'],
    498: ['Q', 'R'],
    501: ['N', 'Y'],
    505: ['Y', 'H'],
}
rbd_residue_index_starting_desai_sequences = 331
rbd_residue_index_ending_desai_sequences = 531  # included
possible_mutations_0_based_index = {k - rbd_residue_index_starting_desai_sequences: v for k, v in possible_mutations.items()}

weird_mutations = []
with open("variants.txt", "w") as f:
    for sequence in sequences:
        # Write to file
        # ex: KC417N where K is the wildtype amino acid, C is the chain, 417 is the position, N is the mutant amino acid

        listMutations = [f"{aa[0]}{chain_rbd}{str(position+rbd_residue_index_starting_desai_sequences)}{aa[1]}" for position, aa in possible_mutations_0_based_index.items() if sequence[position] != aa[0]]
        f.write(",".join(listMutations) + ";" + "\n")

# Run the script
# mkdir mutant-evoEf
# cd mutant-evoEf
# EvoEF2 --command=BuildMutant --pdb=../6xf5_rbd_only.pdb --mutant_file=../variants.txt

