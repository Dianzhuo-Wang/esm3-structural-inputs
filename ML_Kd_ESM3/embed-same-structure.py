
## Remove is you use an installed version of esm3
import sys
sys.path.append("./esm3")
##

import numpy as np
import torch

from esm.utils.structure.protein_chain import ProteinChain
from esm.models.esm3 import ESM3
from esm.sdk import client
from esm.sdk.api import (
    ESMProtein
)
from esm.utils import encoding

import pandas as pd

import os
from tqdm import tqdm

import argparse
from math import ceil

# Argparse
parser = argparse.ArgumentParser(description='Embed sequences with ESM3')
parser.add_argument('--protein-pdb-file', type=str, required=True,
                    help='The pdb file of the protein')
parser.add_argument('--chain-id', type=str, required=True,
                    help='The chain id of the protein')
parser.add_argument('--embeddings-save-file-name', type=str, required=True,
                    help='The name of the file where to save the embeddings, ex: cov555.pt')
parser.add_argument('--sequences-to-embed', type=str, required=True,
                    help='Sequences to embed, ex: df_Desai_15loci_sequence.npy')
parser.add_argument('--folder-for-embeddings', type=str, required=True,
                    help='Folder to load sequences and save embeddings, ex: data')

args = parser.parse_args()

protein_pdb_file = args.protein_pdb_file
chain_id = args.chain_id
# folder_for_embeddings = "data"
folder_for_embeddings = args.folder_for_embeddings
# sequences_to_embed = folder_for_embeddings + "/" + "df_Desai_15loci_sequence.npy"
sequences_to_embed = folder_for_embeddings + "/" + args.sequences_to_embed 
embeddings_save_file_name = args.embeddings_save_file_name
# You should not change this
main_saving_folder = "savings"
# you can change this
save_folder = "embedding_savings_" + embeddings_save_file_name.split(".")[0] + folder_for_embeddings # remove the extension
# Make sure to choose the right indexes (you can check interactively with check-protein-structure.ipynb)
rbd_residue_index_starting_desai_sequences = 331
rbd_residue_index_ending_desai_sequences = 531 # included
index_start = 3
index_stop = -5

# Protein
protein_chain = ProteinChain.from_pdb(protein_pdb_file, chain_id=chain_id)
protein_chain = protein_chain.select_residue_indices(
    range(rbd_residue_index_starting_desai_sequences + index_start,
    rbd_residue_index_ending_desai_sequences + index_stop + 1))
protein = ESMProtein.from_protein_chain(protein_chain)

assert protein_chain.residue_index[0] >= rbd_residue_index_starting_desai_sequences + index_start, "The protein does not start at the right index"
assert protein_chain.residue_index[-1] <= rbd_residue_index_ending_desai_sequences + index_stop, "The protein does not end at the right index"

# Sequences
sequences = np.load(sequences_to_embed, allow_pickle=True)

len_sequence = len(sequences[0])


# def get_loci(sequences) -> (np.ndarray, np.ndarray):
#     """
#     Get the index of the loci that are mutated in the dataset
#     """
#     sequences_int = np.array([[ord(aa) for aa in seq] for seq in sequences])
#     mean_order_seq = np.mean(sequences_int, axis=0)
#     index_loci = np.where(mean_order_seq != sequences_int[0])[0]

#     # Find the possibilities of mutations at each locus
#     # We know that for each locus, there is two mutations, with the same proportion
#     # We compare the first sequence with the rest of the sequences
#     mutated_loci_int = mean_order_seq*2 - sequences_int[0]
#     mutated_loci = np.array([chr(int(aa)) for aa in mutated_loci_int])[index_loci]
#     wild_type = np.array(list(sequences[0]))[index_loci]

#     return index_loci, wild_type, mutated_loci
# index_loci, wild_type, mutated_loci = get_loci(sequences)
# # Check that all mutations are within the selected portion of sequence in the pdb
# # Sequences have the same length
# assert all([index_start <= loci for loci in index_loci])
# assert all([loci <= index_stop+len_sequence for loci in index_loci])
# assert len(sequences[0][index_start:index_stop]) == len(protein.sequence)

# Select the portion of the sequence that is in the pdb
sequences = [seq[index_start:index_stop] for seq in sequences]

# # Create ESMProteins and embeddings for desai old
model =  ESM3.from_pretrained("esm3_sm_open_v1", device=torch.device("cuda"))

# Make batch of 50 examples
batch_size = 15
n_batches = ceil(len(sequences) / batch_size)

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

def get_esm_protein(sequence):
    variant = ESMProtein()
    variant.sequence = sequence
    return variant

def get_structure_embedding(coordinates, model):
    coordinates, _, structure_tokens = encoding.tokenize_structure(
        coordinates,
        model.get_structure_encoder(),
        structure_tokenizer=model.tokenizers.structure,
        reference_sequence="",
        add_special_tokens=True,
    )
    return coordinates, structure_tokens

coordinates, structure_tokens = get_structure_embedding(protein.coordinates, model)

for i in tqdm(range(n_batches)):
    start = i*batch_size
    end = min((i+1)*batch_size, len(sequences))

    batch = sequences[start:min(end, len(sequences))]
    batch = [get_esm_protein(seq) for seq in batch]
    batch = [model.encode(seq) for seq in batch]

    # with torch.no_grad():
    #     embeddings, embeddings_norm_layer = model.get_embeddings_batched(batch)

    # embeddings = embeddings.mean(dim=1)
    # # embeddings_norm_layer = embeddings_norm_layer.mean(dim=1)

    # torch.save(embeddings, f"{save_folder}/embeddings_{i}.pt")
    # torch.save(embeddings_norm_layer, f"{save_folder}/embeddings_norm_layer_{i}.pt")

    for var in batch:
        var.coordinates = coordinates
        var.structure_tokens = structure_tokens

    with torch.no_grad():
        embeddings, embeddings_norm_layer = model.get_embeddings_batched(batch)

    max_pooling_embeddings = embeddings.max(dim=1).values
    embeddings = embeddings.mean(dim=1)
    # embeddings_norm_layer = embeddings_norm_layer.mean(dim=1)

    torch.save(max_pooling_embeddings, f"{save_folder}/embeddings_{i}_max_pooling.pt")
    torch.save(embeddings, f"{save_folder}/embeddings_{i}_withCoordinates.pt")
    # torch.save(embeddings_norm_layer, f"{save_folder}/embeddings_norm_layer_{i}_withCoordinates.pt")


# # Read all files and concatenate
# embeddings = []
# # embeddings_norm_layer = []

# for i in range(n_batches):
#     embeddings.append(torch.load(f"{save_folder}/embeddings_{i}.pt"))
#     # embeddings_norm_layer.append(torch.load(f"{save_folder}/embeddings_norm_layer_{i}.pt"))

# embeddings = torch.cat(embeddings, dim=0).numpy()
# # embeddings_norm_layer = torch.cat(embeddings_norm_layer, dim=0).numpy()

embeddings_withCoordinates = []
embeddings_max_pooling = []
# embeddings_norm_layer_withCoordinates = []

for i in range(n_batches):
    embeddings_max_pooling.append(torch.load(f"{save_folder}/embeddings_{i}_max_pooling.pt"))
    embeddings_withCoordinates.append(torch.load(f"{save_folder}/embeddings_{i}_withCoordinates.pt"))
    # embeddings_norm_layer_withCoordinates.append(torch.load(f"{save_folder}/embeddings_norm_layer_{i}_withCoordinates.pt"))

embeddings_withCoordinates = torch.cat(embeddings_withCoordinates, dim=0)
embeddings_max_pooling = torch.cat(embeddings_max_pooling, dim=0)
# embeddings_norm_layer_withCoordinates = torch.cat(embeddings_norm_layer_withCoordinates, dim=0)

# torch.save(embeddings, folder_for_embeddings + "/embeddings_sequence_only_" + embeddings_save_file_name)
torch.save(embeddings_max_pooling, folder_for_embeddings + "/embeddings_max_pooling_" + embeddings_save_file_name)
torch.save(embeddings_withCoordinates, folder_for_embeddings + "/embeddings_withCoordinates_" + embeddings_save_file_name)
