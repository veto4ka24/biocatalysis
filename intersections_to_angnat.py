import pandas as pd

df1 = pd.read_csv('gene_atlas_merge_uniprot.csv', sep=';')
df2 = pd.read_csv('task2_lab.csv', sep=' ')
#df1 = df1.filter(['gene', 'protein'])
df2 = df2.filter(['protein'])

#print(df2.to_string())
#print(df1.to_string())

for i in df1.protein:
    sub = i
    for j in df2.protein:
        seq = j
        if sub in seq:
            gene = (df1[df1['protein'] == sub]).filter(['gene'])
            print(seq, sub, gene, sep = ' ')