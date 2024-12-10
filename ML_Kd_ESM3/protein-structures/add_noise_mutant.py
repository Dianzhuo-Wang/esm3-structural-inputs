from biopandas.pdb import PandasPdb
import numpy as np
import os
from tqdm import tqdm
from multiprocessing import Pool, cpu_count



# Add noise to the structure
# Order of magnitude of noise is 0.1 Angstroms
# Which yields a 0.17 RMSD 

def add_noise(i):
    pdb_file = f"mutant-evoEf-6xf5-rbd-only/{i}/{i}_correct_mutant_no_relax.pdb"
    noises = [0.1, 0.05]
    for noise in noises:
        structure = PandasPdb().read_pdb(pdb_file)
        structure_atom = structure.df["ATOM"]
        
        structure_variant = structure.df["ATOM"].copy()
        structure_variant["x_coord"] += noise * np.random.randn(len(structure_variant))
        structure_variant["y_coord"] += noise * np.random.randn(len(structure_variant))
        structure_variant["z_coord"] += noise * np.random.randn(len(structure_variant))
        
        # Round to 3 decimal places
        structure_variant = structure_variant.round(3)

        new_pdb = PandasPdb()
        new_pdb.df["ATOM"] = structure_variant

        new_pdb.to_pdb(path=f"mutant-evoEf-6xf5-rbd-only/{i}/{i}_noisy_{noise}.pdb", records=["ATOM"])


if __name__ == '__main__':
    with Pool(cpu_count()) as pool:
        list(tqdm(pool.imap_unordered(add_noise, range(1, 2**15+1)), total=2**15))
    # add_noise(16385)
    # add_noise(16386)