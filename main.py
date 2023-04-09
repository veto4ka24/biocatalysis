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
#result_1 = pd.merge(df_10, df_20, how = 'inner', on = ['protein', 'pepide'])
#print(result_2)

df11 = pd.read_csv('MZ78_sle_protein_peptide_precipetation_2.txt', sep=';')
df21 = pd.read_csv('MZ81_sle_protein_peptide_superdex75_2.txt', sep=';')
df11 = df11.filter(['Peptide']).drop_duplicates()
df21 = df21.filter(['Peptide']).drop_duplicates()

long_pept1 = pd.read_csv('Anton_DRB1_1501_round1_count.csv', sep = ',')
long_pept1 = long_pept1.filter(['Sequence']).drop_duplicates()
print(long_pept1)

for i in range(df11.size):
    for j in range(long_pept1.size):
        long_pept1[j].str.contains(str(df11[i]), na = False)
        print()




