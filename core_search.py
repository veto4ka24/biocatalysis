import pandas as pd

#из всех файлов с масс-спектров вытаскиваем ТОЛЬКО колонки с пептидами
peptides_78 = pd.read_csv('MZ78_sle_protein_peptide_precipetation_2.csv', sep = ';')
peptides_78 = peptides_78.filter(['Peptide']).drop_duplicates()
peptides_78 = peptides_78['Peptide'].replace('[^a-zA-Z]', '', regex=True)
peptides_78 = peptides_78[peptides_78.str.len().between(9, 30)]
#peptides_78['Peptide'] = peptides_78['Peptide'].astype('string') + ','
#peptides_78.to_csv("peptides_78.csv", index=False)

peptides_81 = pd.read_csv('MZ81_sle_protein_peptide_superdex75_2.csv', sep = ';')
peptides_81 = peptides_81.filter(['Peptide']).drop_duplicates()
peptides_81 = peptides_81['Peptide'].replace('[^a-zA-Z]', '', regex=True)
peptides_81 = peptides_81[peptides_81.str.len().between(9, 30)]
#peptides_81.to_csv("peptides_81.csv", index=False)

peptides_79 = pd.read_csv('MZ79_Healthy_gel_filtration.csv', sep = ';')
peptides_79 = peptides_79.filter(['Peptide']).drop_duplicates()
peptides_79 = peptides_79['Peptide'].replace('[^a-zA-Z]', '', regex=True)
peptides_79 = peptides_79[peptides_79.str.len().between(9, 30)]
#peptides_79.to_csv("peptides_79.csv", index=False)

peptides_76 = pd.read_csv('MZ76_Healthy_precipetation.csv', sep = ';')
peptides_76 = peptides_76.filter(['Peptide']).drop_duplicates()
peptides_76 = peptides_76['Peptide'].replace('[^a-zA-Z]', '', regex=True)
peptides_76 = peptides_76[peptides_76.str.len().between(9, 30)]
#peptides_76.to_csv("peptides_76.csv", index=False)

