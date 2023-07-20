import pandas as pd

long_pept1 = pd.read_csv('Anton_DRB1_1501_round1_count.csv', sep = ',')
long_pept1 = long_pept1.filter(['Sequence']).drop_duplicates()
#long_pept1 = long_pept1['Sequence'].astype('string')

#с помощью цикла перебираем коры, выданные нейросетью для пептидов с масс-спектров,
# на предмет их вхождения в фаговый пептид

