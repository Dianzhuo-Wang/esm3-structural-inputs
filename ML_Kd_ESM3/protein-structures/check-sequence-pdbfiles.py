from biopandas.pdb import PandasPdb
import numpy as np
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

conversion_amino_acids = {
    'ALA': 'A',
    'ARG': 'R',
    'ASN': 'N',
    'ASP': 'D',
    'CYS': 'C',
    'GLN': 'Q',
    'GLU': 'E',
    'GLY': 'G',
    'HIS': 'H',
    'ILE': 'I',
    'LEU': 'L',
    'LYS': 'K',
    'MET': 'M',
    'PHE': 'F',
    'PRO': 'P',
    'SER': 'S',
    'THR': 'T',
    'TRP': 'W',
    'TYR': 'Y',
    'VAL': 'V'
}

sequences = np.load("../data/df_Desai_15loci_sequence.npy", allow_pickle=True)

def check_sequence_index(index):
    suffix_file_to_embed = ".pdb"
    directory_structure = "mutant-evoEf-6xf5-rbd-only"
    
    test = PandasPdb().read_pdb(f'{directory_structure}/{index}/{index}{suffix_file_to_embed}')
    sequence_pdb = test.df['ATOM'][['residue_number', 'residue_name']].groupby('residue_number').first().values.flatten()
    sequence_pdb = "".join([conversion_amino_acids[residue] for residue in sequence_pdb])
    
    if not sequences[index - 1] == sequence_pdb:
        print(f"Index {index} is different")
    # print("sequence from npy")
    # print(f"{sequences[index - 1]}")
    # print("sequence from pdb")
    # print(f"{sequence_pdb}")

if __name__ == '__main__':
    with Pool(cpu_count()) as pool:
        list(tqdm(pool.imap_unordered(check_sequence_index, range(1, 2**15+1)), total=2**15))
    # check_sequence_index(16385)
    # check_sequence_index(16386)