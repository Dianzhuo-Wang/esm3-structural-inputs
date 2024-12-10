## Was only use to extract the dataset from the save folding (embedding_savings) but otherwise this file is useless
import numpy as np
import torch


import pandas as pd

import os

df = pd.read_parquet("df_Desai_15loci_complete.parquet")

df.drop(columns=['Unnamed: 0', 'count',
       'real_f', 'pred_f', 'average_date', 'cls_representation',
       'mean_representation', 'max_representation',
       'mean_delta_representation', 'max_delta_representation', 'probs',
       'wildtype_probs', 'grammaticality', 'semantic_change'], inplace=True)

# Make batch of 50 examples
batch_size = 50
n_batches = len(df) // batch_size + 1

save_folder = "embedding_savings"

# Read all files and concatenate
embeddings = []
embeddings_norm_layer = []

for i in range(n_batches):
    embeddings.append(torch.load(f"{save_folder}/embeddings_{i}.pt"))
    embeddings_norm_layer.append(torch.load(f"{save_folder}/embeddings_norm_layer_{i}.pt"))

embeddings = torch.cat(embeddings, dim=0).numpy()
embeddings_norm_layer = torch.cat(embeddings_norm_layer, dim=0).numpy()

embeddings_withCoordinates = []
embeddings_norm_layer_withCoordinates = []

for i in range(n_batches):
    embeddings_withCoordinates.append(torch.load(f"{save_folder}/embeddings_{i}_withCoordinates.pt"))
    embeddings_norm_layer_withCoordinates.append(torch.load(f"{save_folder}/embeddings_norm_layer_{i}_withCoordinates.pt"))

embeddings_withCoordinates = torch.cat(embeddings_withCoordinates, dim=0).numpy()
embeddings_norm_layer_withCoordinates = torch.cat(embeddings_norm_layer_withCoordinates, dim=0).numpy()

df["embeddings"] = [str(embeddings[i].tolist()) for i in range(len(embeddings))]
df["embeddings_norm"] = [str(embeddings_norm_layer[i].tolist()) for i in range(len(embeddings_norm_layer))]
df["embeddings_withCoordinates"] = [str(embeddings_withCoordinates[i].tolist()) for i in range(len(embeddings_withCoordinates))]
df["embeddings_norm_withCoordinates"] = [str(embeddings_norm_layer_withCoordinates[i].tolist()) for i in range(len(embeddings_norm_layer_withCoordinates))]

df.to_parquet("df_Desai_15loci_complete_embeddings_esm3.parquet")