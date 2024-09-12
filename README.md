# FG_aware_tokenization
This Python script processes molecular data from a CSV file, generates a Functional Module-Aware SMILES representation, and saves the output to a pickle file. It is designed to handle molecular structures provided in the SMILES format.

## Input File Format
The input CSV file must contain at least one column named SMILES, which stores the SMILES strings representing molecular structures. The script processes these SMILES strings and generates a modified SMILES representation.

## Usage
Run the script with the following command:
`python process_molecule_data.py <csv_path> <save_path>`
* <csv_path>: Path to the input CSV file containing molecule data. The file must contain a column named SMILES.
* <save_path>: Path where the output pickle file will be saved.
  
## Notes:
* The get_new_smiles_rep function (from the helpers module) is used to generate the new SMILES representation for each molecule.
* If a SMILES string generates more than 512 tokens, the representation will be truncated to the first 512 tokens.
* The resulting SMILES strings are saved in the specified pickle file as a list. 
