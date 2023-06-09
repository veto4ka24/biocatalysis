import pandas as pd

df0 = pd.read_csv('intersect_uniprot_immpr_ms.csv', sep = ';')
df1 = pd.read_csv('gene_atlas_merge_uniprot.csv', sep=';')
df1_1 = pd.read_csv('MZ78_merge_antigenatlas.csv', sep = ';')
df1_2 = pd.read_csv('MZ81_merge_antigenatlas.csv', sep = ';')
df2 = pd.read_csv('task2_lab.csv', sep=' ')
#df1 = df1.filter(['gene', 'protein'])
df2 = df2.filter(['protein'])
df3 = pd.read_csv('MZ76_Healthy_precipetation.csv', sep = ';')
df3_1 = df3.filter(['Protein Accession']).drop_duplicates()
df4 = pd.read_csv('MZ78_merge_MZ81_in_DRB1_round2.csv', sep = ' ')
df4 = df4.filter(['Peptide'])
df5_1 = pd.read_csv('MZ81_sle_protein_peptide_superdex75_2.csv', sep = ';')
df5_1 = df5_1.filter(['Protein Accession', 'Peptide']).drop_duplicates()
df5_2 = pd.read_csv('MZ78_sle_protein_peptide_precipetation_2.csv', sep = ';')
df5_2 = df5_2.filter(['Protein Accession', 'Peptide']).drop_duplicates()
#df5['Peptide'] = df5['Peptide'].astype(str)
df6 = pd.read_csv('MZ79_Healthy_gel_filtration.csv', sep = ';')
df6_1 = df6.filter(['Protein Accession']).drop_duplicates()
df7 = pd.read_csv('MZ78_sle_protein_peptide_precipetation_2.csv', sep = ';')
df7 = df7.filter(['Protein Accession', 'Peptide']).drop_duplicates()
df8 = pd.read_csv('MZ78_merge_MZ81_in_DRB1_round1.csv', sep = ' ').filter(['Peptide'])
df9_1 = pd.read_csv('MZ78_in_DRB1_round1.csv', sep = ' ')
df9_2 = pd.read_csv('MZ78_in_DRB1_round2.csv', sep = ' ')
df10_1 = pd.read_csv('MZ81_in_DRB1_round1.csv', sep = ' ')
df10_2 = pd.read_csv('MZ81_in_DRB1_round2.csv', sep = ' ')

#print(df2.to_string())
#print(df1.to_string())

res1 = df5_1.merge(df4, how = 'inner', on = 'Peptide', indicator = True)
res1 = res1.filter(['Protein Accession'])
res1 = res1.rename(columns = {'Protein Accession' : 'protein'})
#пытаюсь найти белки юнипрот, соответствующие в ФД 2 раунде пересечению ИП и ГФ больных
res2 = df5_1.merge(df8, how = 'inner', on = 'Peptide', indicator = True)
res2 = res2.filter(['Protein Accession'])
res2 = res2.rename(columns = {'Protein Accession' : 'protein'})
#пытаюсь найти белки юнипрот, соответствующие в ФД 1 раунде пересечению ИП и ГФ больных
#res2.to_csv("UNIproteins_from_DRB1_1.csv", index=False)

res1_1 = df5_2.merge(df9_1, how = 'inner', on = 'Peptide', indicator = True)
res1_1 = res1_1.filter(['Protein Accession'])
res1_1 = res1_1.rename(columns = {'Protein Accession' : 'protein'})
#ищем белки юнипрот, которые соответствуют пептидам ИП больных, экспрессирующие пептиды в ФД 1 раунде
res1_2 = df5_2.merge(df9_2, how = 'inner', on = 'Peptide', indicator = True)
res1_2 = res1_2.filter(['Protein Accession'])
res1_2 = res1_2.rename(columns = {'Protein Accession' : 'protein'})
#ищем белки юнипрот, которые соответствуют пептидам ИП больных, экспрессирующие пептиды в ФД 2 раунде
#res1_2.to_csv("UNIproteins_from_DRB1_2_only_from_MZ78.csv", index=False)

res2_1 = df5_2.merge(df10_1, how = 'inner', on = 'Peptide', indicator = True)
res2_1 = res2_1.filter(['Protein Accession'])
res2_1 = res2_1.rename(columns = {'Protein Accession' : 'protein'})
#ищем белки юнипрот, которые соответствуют пептидам ГФ больных, экспрессирующие пептиды в ФД 1 раунде
res2_2 = df5_2.merge(df10_2, how = 'inner', on = 'Peptide', indicator = True)
res2_2 = res2_2.filter(['Protein Accession'])
res2_2 = res2_2.rename(columns = {'Protein Accession' : 'protein'})
#ищем белки юнипрот, которые соответствуют пептидам ГФ больных, экспрессирующие пептиды в ФД 2 раунде
#res2_2.to_csv("UNIproteins_from_DRB1_2_only_from_MZ81.csv", index=False)

df_phdis_1 = pd.read_csv('UNIproteins_from_DRB1_1.csv', sep = ';').filter(['protein'])

#заносим в датафреймы результаты поиска белков, экспрессирующих нужные пептиды в ФД, которые были найдены
#в предыдущей итерации (то есть содержатся в пробах на ИП и ГФ больных)
df_phdis_21_mz81 = pd.read_csv('UNIproteins_from_DRB1_1_only_from_MZ81.csv', sep = ';').filter(['protein'])
df_phdis_22_mz81 = pd.read_csv('UNIproteins_from_DRB1_2_only_from_MZ81.csv', sep = ';').filter(['protein'])
df_phdis_11_mz78 = pd.read_csv('UNIproteins_from_DRB1_1_only_from_MZ78.csv', sep = ';').filter(['protein'])
df_phdis_12_mz78 = pd.read_csv('UNIproteins_from_DRB1_2_only_from_MZ78.csv', sep = ';').filter(['protein'])

df_phdis_2 = pd.read_csv('UNIproteins_from_DRB1_2.csv', sep = ';').filter(['protein'])

phdis_2_genes = df_phdis_2.merge(df1, how = 'inner', on = 'protein')
#ищем гены, соответствующие найденным в предыдущей итерации белкам
phdis_1_genes78 = df_phdis_11_mz78.merge(df1_1, how = 'inner', on = 'protein')
phdis_2_genes78 = df_phdis_12_mz78.merge(df1_1, how = 'inner', on = 'protein')
phdis_1_genes81 = df_phdis_21_mz81.merge(df1_2, how = 'inner', on = 'protein')
phdis_2_genes81 = df_phdis_22_mz81.merge(df1_2, how = 'inner', on = 'protein')
print(phdis_2_genes81)