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
proteins_78 = pd.read_csv('MZ78_sle_protein_peptide_precipetation.csv', header = 0, names = ['protein', 'peptide'], sep = ';', usecols = [2, 3])
df_20 = pd.DataFrame(proteins_78)
result_1 = pd.merge(df_10, df_20, how = 'inner', on = ['protein', 'peptide'])
#print(result_1)

df11 = pd.read_csv('MZ78_sle_protein_peptide_precipetation_2.csv', sep=';')
df21 = pd.read_csv('MZ81_sle_protein_peptide_superdex75_2.csv', sep=';')
df11 = df11.filter(['Peptide']).drop_duplicates()
df21 = df21.filter(['Peptide']).drop_duplicates()

long_pept1 = pd.read_csv('Anton_DRB1_1501_round1_count.csv', sep = ',')
long_pept1 = long_pept1.filter(['Sequence']).drop_duplicates()
print(long_pept1)
long_pept2 = pd.read_csv('Anton_DRB1_1501_round2_count.csv', sep = ',')
long_pept2 = long_pept2.filter(['Sequence']).drop_duplicates()

res1 = result_1['peptide'].str.replace('.', '')

df10 = df1.filter(['Protein Accession']).drop_duplicates()
#print(df10.to_string())
