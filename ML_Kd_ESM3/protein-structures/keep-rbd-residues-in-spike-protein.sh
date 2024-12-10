#!/bin/bash

# Define residue range
residue_number_start=331
residue_number_end=531
output_dir="mutant-evoEf-6xf5-rbd-only"

# Function to extract residues from a PDB file
extract_residues() {
    local pdb_file=$1
    local residue_number_start=$2
    local residue_number_end=$3
    local output_dir=$4

    # Extract the base name of the file (without path and extension)
    local base_name=$(basename "$pdb_file" .pdb)

    # Define the output file name
    local output_subset="$output_dir/${base_name}_RBD.pdb"

    # Extract residues from residue_number_start to residue_number_end
    awk -v start="$residue_number_start" -v end="$residue_number_end" \
        '($1 == "ATOM" || $1 == "HETATM") && $6 >= start && $6 <= end' "$pdb_file" > "$output_subset"
}

extract_residues "6xf5_spike_only.pdb" $residue_number_start $residue_number_end . 