import pandas as pd

#объявление датафреймов
peptides_78_r1 = pd.read_csv('nothealthy_peps&cores_from_78(precipetation)r1.csv', sep = ',')
peptides_78_r1 = peptides_78_r1.filter(['Peptide'])
peptides_78_r2 = pd.read_csv('nothealthy_peps&cores_from_78(precipetation)r2.csv', sep = ',')
peptides_78_r2 = peptides_78_r2.filter(['Peptide'])
peptides_78_br = pd.read_csv('nothealthy_peps&cores_from_78(precipetation)_both_rounds.csv', sep = ',')
peptides_78_br = peptides_78_br.filter(['Peptide'])
peptides_81_r1 = pd.read_csv('nothealthy_peps&cores_from_81(gel-filtration)r1.csv', sep = ',')
peptides_81_r1 = peptides_81_r1.filter(['Peptide'])
peptides_81_r2 = pd.read_csv('nothealthy_peps&cores_from_81(gel-filtration)r2.csv', sep = ',')
peptides_81_r2 = peptides_81_r2.filter(['Peptide'])
peptides_81_br = pd.read_csv('nothealthy_peps&cores_from_81(gel-filtration)_both_rounds.csv', sep = ',')
peptides_81_br = peptides_81_br.filter(['Peptide'])
prot_pep_78 = pd.read_csv('MZ78_sle_protein_peptide_precipetation_2.csv', sep = ';')
prot_pep_78 = prot_pep_78.filter(['Protein Accession', 'Peptide'])
prot_pep_78['Peptide'] = prot_pep_78['Peptide'].replace('[^a-zA-Z]', '', regex=True)
prot_pep_81 = pd.read_csv('MZ81_sle_protein_peptide_superdex75_2.csv', sep = ';')
prot_pep_81 = prot_pep_81.filter(['Protein Accession', 'Peptide'])
prot_pep_81['Peptide'] = prot_pep_81['Peptide'].replace('[^a-zA-Z]', '', regex=True)
uniprots_78 = pd.read_csv('MZ78_merge_antigenatlas.csv', sep = ';')
uniprots_78.rename(columns = {'protein':'Protein Accession'}, inplace = True)
uniprots_81 = pd.read_csv('MZ81_merge_antigenatlas.csv', sep = ';')
uniprots_81.rename(columns = {'protein':'Protein Accession'}, inplace = True)

target_prots_78_1 = peptides_78_r1.merge(prot_pep_78,  how = 'inner', on = 'Peptide', indicator = True)
print(target_prots_78_1)
target_prots_78_2 = peptides_78_r2.merge(prot_pep_78,  how = 'inner', on = 'Peptide', indicator = True)
print(target_prots_78_2)
target_br_78 = peptides_78_br.merge(prot_pep_78,  how = 'inner', on = 'Peptide', indicator = True)
print(target_br_78)
target_prots_81_1 = peptides_81_r1.merge(prot_pep_81,  how = 'inner', on = 'Peptide', indicator = True)
print(target_prots_81_1)
target_prots_81_2 = peptides_81_r2.merge(prot_pep_81,  how = 'inner', on = 'Peptide', indicator = True)
print(target_prots_81_2)
target_br_81 = peptides_81_br.merge(prot_pep_81,  how = 'inner', on = 'Peptide', indicator = True)
print(target_br_81)

genes_peps_prots_81r1 = target_prots_81_1.merge(uniprots_81, how = 'inner', on = 'Protein Accession')
print(genes_peps_prots_81r1)
genes_peps_prots_81r2 = target_prots_81_2.merge(uniprots_81, how = 'inner', on = 'Protein Accession')
print(genes_peps_prots_81r2)
genes_peps_prots_81br = target_br_81.merge(uniprots_81, how = 'inner', on = 'Protein Accession')
print(genes_peps_prots_81br)