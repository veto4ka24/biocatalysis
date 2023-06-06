import pandas as pd

df1 = pd.read_csv('gene_atlas_merge_uniprot.csv', sep=';') #заносим в переменную базу
# антиген атласа с юниротом
df2 = pd.read_csv('healthy76_in_antigenatlas.csv', sep = ';') #гены в иммунопреципетации здоровых
df3 = pd.read_csv('healthy79_in_antigenatlas.csv', sep = ';') #гены в гель-фильтрации здоровых
df4 = pd.read_csv('MZ81_merge_antigenatlas.csv', sep = ';') #
df5 = pd.read_csv('intersect_uniprot_immpr_ms.csv', sep = ';').filter(['gene', 'uniprot']).drop_duplicates() #гены и юнипрот белки в пересечении ГФ и ИП больных
#df6 = pd.read_csv('MZ78_sle_protein_peptide_precipetation.csv', sep = ';').filter([''])
df7 = pd.read_csv('genes_from_DRB1r2_&MZ78.csv', sep = ' ').filter(['gene', 'protein']) #гены в ИП и
# ФД 2 раунд
df8 = pd.read_csv('genes_DRB1_r1&MZ78.csv', sep = ';').filter(['gene', 'protein']) #гены в ИП и ФД 1 раунд
df9 = pd.read_csv('MZ78_merge_antigenatlas.csv', sep = ';') #гены и юнипрот белки в ИП больных
#поскольку не было найдено генов, общих хотя бы для одного раунда ФД и ГФ больных, для них не
#создаем датафрейм

res1 = df5.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res2 = df5.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
#ищем гены, отсутствующие в ИП (res1) и ГФ (res2) здоровых, но присутствующие в пересечении ИП и
# ГФ больных
res3 = df7.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res4 = df7.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
#ищем гены, отсутствующие в ИП (res3) и ГФ (res4) здоровых, но присутствующие в пересечении ИП и
# ФД 2 раунда
res5 = df8.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res6 = df8.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
#ищем гены, отсутствующие в ИП (res5) и ГФ (res6) здоровых, но присутствующие в пересечении ИП и
# ФД 1 раунда
res7 = df9.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res8 = df9.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
#ищем гены, отсутствующие в ИП (res7) и ГФ (res8) здоровых, но присутствующие в ИП больных
res9 = df4.merge(df2, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
res10 = df4.merge(df3, how = 'left', on = 'gene', indicator = True).query("_merge == 'left_only'")
#ищем гены, отсутствующие в ИП (res9) и ГФ (res10) здоровых, но присутствующие в ГФ больных

df_76_78 = pd.read_csv('not_in_MZ76_but_in_MZ78.csv', sep = ';')
df_76_81 = pd.read_csv('not_in_MZ76_but_in_MZ81.csv', sep = ';')
df_79_78 = pd.read_csv('not_in_MZ79_but_in_MZ78.csv', sep = ';')
df_79_81 = pd.read_csv('not_in_MZ79_but_in_MZ81.csv', sep = ';')

res11 = df_79_81.merge(df_79_78, how = 'inner', on = ['protein', 'gene'])
#ищем гены, которые есть в ГФ и ИП больных, но отсутствуют в ГФ здоровых
res12 = df_76_81.merge(df_76_78, how = 'inner', on = ['protein', 'gene'])
#ищем гены, которые есть в ГФ и ИП больных, но отсутствуют в ИП здоровых

print(res3)
print(res4)
print(res3.merge(res4, how = 'inner', on = 'gene'))
print(res5)
print(res6)
print(res5.merge(res6, how = 'inner', on = 'gene'))