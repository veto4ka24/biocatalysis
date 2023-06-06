import pandas as pd

df1 = pd.read_csv('gene_atlas_merge_uniprot.csv', sep=';')
df2 = pd.read_csv('healthy76_in_antigenatlas.csv', sep = ';')
df3 = pd.read_csv('healthy79_in_antigenatlas.csv', sep = ';')
df4 = pd.read_csv('MZ81_merge_antigenatlas.csv', sep = ';')
df5 = pd.read_csv('intersect_uniprot_immpr_ms.csv', sep = ';').filter(['gene', 'uniprot']).drop_duplicates()
#df6 = pd.read_csv('MZ78_sle_protein_peptide_precipetation.csv', sep = ';').filter([''])
df7 = pd.read_csv('genes_from_DRB1r2_&MZ78.csv', sep = ' ').filter(['gene', 'protein'])
df8 = pd.read_csv('genes_DRB1_r1&MZ78.csv', sep = ';').filter(['gene', 'protein'])
df9 = pd.read_csv('MZ78_merge_antigenatlas.csv', sep = ';')

res1 = df5.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res2 = df5.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res3 = df7.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res4 = df7.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res5 = df8.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res6 = df8.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res7 = df9.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res8 = df9.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res9 = df4.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res10 = df4.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")

df_76_78 = pd.read_csv('not_in_MZ76_but_in_MZ78.csv', sep = ' ').filter(['gene'])
df_76_81 = pd.read_csv('not_in_MZ76_but_in_MZ81.csv', sep = ' ').filter(['gene'])
df_79_78 = pd.read_csv('not_in_MZ79_but_in_MZ78.csv', sep = ' ').filter(['gene'])
df_79_81 = pd.read_csv('not_in_MZ79_but_in_MZ81.csv', sep = ' ').filter(['gene'])

print(df_79_81.merge(df_79_78, how = 'inner', on = 'gene'))
