import pandas as pd
from functools import reduce
from typing import Union

df1 = pd.read_csv('MZ78_sle_protein_peptide_precipetation.csv', sep=';')
df2 = pd.read_csv('MZ81_sle_protein_peptide_superdex75.csv', sep=';')
df1 = df1.filter(['Protein Accession', 'Peptide']).drop_duplicates()
df2 = df2.filter(['Protein Accession', 'Peptide']).drop_duplicates()
df2.head()

result_2 = pd.merge(df1, df2, on = 'Protein Accession', how='inner')

proteins_81 = pd.read_csv('MZ81_sle_protein_peptide_superdex75.csv', header = 0, names = ['protein', 'peptide'], sep = ';', usecols = [2, 3])
df_10 = pd.DataFrame(proteins_81)
prot_81 = pd.read_csv('MZ81_sle_protein_peptide_superdex75.csv', header = 0, names = ['protein'])
df_11 = pd.DataFrame(prot_81)
proteins_78 = pd.read_csv('MZ78_sle_protein_peptide_precipetation.csv', header = 0, names = ['protein', 'peptide'], sep = ';', usecols = [2, 3])
df_20 = pd.DataFrame(proteins_78)
prot_78 = pd.read_csv('MZ78_sle_protein_peptide_precipetation.csv', header = 0, names = ['protein'])
df_21 = pd.DataFrame(prot_78)
#result_1 = pd.merge(df_10, df_20, how = 'inner', on = ['protein', 'pepide'])
print(result_2)

