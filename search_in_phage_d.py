import pandas as pd

long_pept1 = pd.read_csv('Anton_DRB1_1501_round1_count.csv', sep = ',')
long_pept1 = long_pept1.filter(['Sequence']).drop_duplicates()
#long_pept1 = long_pept1['Sequence'].astype('string')
long_pept2 = pd.read_csv('Anton_DRB1_1501_round2_count.csv', sep = ',')
long_pept2 = long_pept2.filter(['Sequence']).drop_duplicates()

cores_78 = pd.read_csv('cores_78.csv', sep = ';')
cores_78 = cores_78.filter(['Core']).drop_duplicates()
cores_81 = pd.read_csv('cores_81.csv', sep = ';')
cores_81 = cores_81.filter(['Core']).drop_duplicates()
#с помощью цикла перебираем коры, выданные нейросетью для пептидов с масс-спектров,
# на предмет их вхождения в фаговый пептид
for core in cores_78.Core:
    sub = core
    for j in long_pept1.Sequence:
        seq = j
      #  if sub in seq:
      #      print(seq, sub, sep = ' ')

#print('___')

for i in cores_78.Core:
    sub = i
    for j in long_pept2.Sequence:
        seq = j
        #if sub in seq:
         #   print(seq, sub, sep = ' ')

for core in cores_81.Core:
    sub = core
    for j in long_pept1.Sequence:
        seq = j
        if sub in seq:
            print(seq, sub, sep = ' ')

print('___')

for i in cores_81.Core:
    sub = i
    for j in long_pept2.Sequence:
        seq = j
        if sub in seq:
            print(seq, sub, sep = ' ')