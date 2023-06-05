import pandas as pd

df1 = pd.read_csv('gene_atlas_merge_uniprot.csv', sep=';')
df2 = pd.read_csv('healthy76_in_antigenatlas.csv', sep = ';')
df3 = pd.read_csv('healthy79_in_antigenatlas.csv', sep = ';')
df4 = pd.read_csv('MZ81_merge_antigenatlas.csv', sep = ';')
df5 = pd.read_csv('intersect_uniprot_immpr_ms.csv', sep = ';').filter(['gene', 'uniprot']).drop_duplicates()
df6 = pd.read_csv('MZ78_sle_protein_peptide_precipetation.csv', sep = ';').filter([''])

res1 = df5.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res2 = df5.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res3 = df6.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
print(res3)
