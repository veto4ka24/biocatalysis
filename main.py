import pandas as pd

proteins_81 = pd.read_csv('MZ81_sle_protein_peptide_superdex75.csv', header = 0, names = ['protein', 'peptide'], sep = ';', usecols = [2, 3])
df_10 = pd.DataFrame(proteins_81)
proteins_78 = pd.read_csv('MZ78_sle_protein_peptide_precipetation.csv', header = 0, names = ['protein', 'peptide'], sep = ';', usecols = [2, 3])
df_20 = pd.DataFrame(proteins_78)
result_1 = pd.merge(df_10, df_20, how = 'inner', on = ['protein', 'peptide'])
print(result_1)