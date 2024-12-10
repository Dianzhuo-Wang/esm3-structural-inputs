#! /bin/bash
#SBATCH -o log/analysis_%j.out
#SBATCH -e log/analysis_%j.err
#SBATCH -p gpu_requeue
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=15
#SBATCH --mem-per-cpu=2000
#SBATCH -t 0-04:00:00


# Load mamba
__conda_setup="$('/n/sw/Mambaforge-23.11.0-0/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/n/sw/Mambaforge-23.11.0-0/etc/profile.d/conda.sh" ]; then
        . "/n/sw/Mambaforge-23.11.0-0/etc/profile.d/conda.sh"
    else
        export PATH="/n/sw/Mambaforge-23.11.0-0/bin:$PATH"
    fi
fi
unset __conda_setup
if [ -f "/n/sw/Mambaforge-23.11.0-0/etc/profile.d/mamba.sh" ]; then
    . "/n/sw/Mambaforge-23.11.0-0/etc/profile.d/mamba.sh"
fi

# Envrionment dependant
export protein=$1
export chain_ids=$2
export embeddings_save_file_name=$3
export sequences_to_embed=$4
export folder_for_embeddings=$5
mamba activate esm


# if [ ${#chain_id} -eq 0 ]; then
#     python embed-same-structure-entire-complex.py \
#         --suffix-file-to-embed $protein \
#         --chain-id="" \
#         --embeddings-save-file-name $embeddings_save_file_name \
#         --directory-structure $directory_structure \
#         --sequences-to-embed $sequences_to_embed \
#         --folder-for-embeddings $folder_for_embeddings
# else
python embed-same-structure-entire-complex.py \
    --protein-pdb-file $protein \
    --chain-ids $chain_ids \
    --embeddings-save-file-name $embeddings_save_file_name \
    --sequences-to-embed $sequences_to_embed \
    --folder-for-embeddings $folder_for_embeddings
# fi
