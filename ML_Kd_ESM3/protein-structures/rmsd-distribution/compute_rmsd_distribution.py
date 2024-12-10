import sys
sys.path.append("../../esm3")

from esm.utils.structure.protein_chain import ProteinChain
import pandas as pd
import numpy as np
from tqdm import tqdm

from multiprocessing import Pool, cpu_count

### To define
index_wt = 2**14 + 1
directory = "../mutant-evoEf-6xf5-rbd-only"
number_of_samples = 3000
###

number_of_structures = 2**15
# number_of_structures = len([name for name in os.listdir("mutant-evoEf-6xf5-rbd-only") if os.path.isdir(f"mutant-evoEf-6xf5-rbd-only/{name}")])
def compute_rmsd(structure_wt, index, suffix, directory):
    structure = ProteinChain.from_pdb(f"{directory}/{index}/{index}_{suffix}.pdb")
    return structure_wt.rmsd(structure)

def compute_rmsd_distribution(suffix, index_choice, index_wt, directory):
    structure_wt = ProteinChain.from_pdb(f"{directory}/{index_wt}/{index_wt}_{suffix}.pdb")
    
    with Pool(cpu_count()) as pool:
        rmsd = list(pool.starmap(compute_rmsd, tqdm([(structure_wt, index, suffix, directory) for index in index_choice], total=len(index_choice))))
    return rmsd

suffixes = [
    "correct_mutant_no_relax",
    "final_relax",
    "first_relax",
    "md_frame_WT",
    "minim_gromacs",
    "noisy_0.05",
    "noisy_0.1",
]
index_choice = np.random.randint(1, number_of_structures + 1, number_of_samples)
rmsd_distributions = {suffix: compute_rmsd_distribution(suffix, index_choice, index_wt, directory) for suffix in suffixes}
rmsd_distributions["index_choice"] = index_choice
df = pd.DataFrame(rmsd_distributions)
df.to_csv("rmsd_distributions.csv", index=False)