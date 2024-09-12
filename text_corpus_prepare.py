import pandas as pd
from tqdm import trange
from rdkit.Chem import MolFromSmiles as s2m
from helpers import get_new_smiles_rep
import pickle
import argparse

def process_data(csv_path, save_path):
    df = pd.read_csv(csv_path)
    df.reset_index(inplace=True)
    df.drop(columns=['index'], inplace=True)

    CORPUS = []
    for i in trange(len(df)):
        sm = df.loc[i, 'SMILES']
        mol = s2m(sm)
        if mol is not None:
            new_smiles = get_new_smiles_rep(mol)
            if len(new_smiles.split()) > 512:
                new_smiles = ' '.join(new_smiles.split()[:512])
            CORPUS.append(new_smiles.strip())
    
    with open(save_path, 'wb') as f:
        pickle.dump(CORPUS, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process molecular data and save it as a pickle file.')
    parser.add_argument('csv_path', type=str, help='Path to the input CSV file containing molecule data.')
    parser.add_argument('save_path', type=str, help='Path to save the output pickle file.')

    args = parser.parse_args()
    
    process_data(args.csv_path, args.save_path)
