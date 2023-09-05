import pandas as pd

cores_78 = pd.read_csv('cores_78.csv', sep = ';')
cores_78 = cores_78.filter(['Peptide', 'Core']).drop_duplicates()
cores_81 = pd.read_csv('cores_81.csv', sep = ';')
cores_81 = cores_81.filter(['Peptide', 'Core']).drop_duplicates()
cores_78_1 = pd.read_csv('cores_78(precipetation)_in_phage_display_r1.csv', sep = ';')
cores_78_1 = cores_78_1.filter(['Core'])
cores_78_2 = pd.read_csv('cores_78(precipetation)_in_phage_display_r2.csv', sep = ';')
cores_78_2 = cores_78_2.filter(['Core'])
cores_81_1 = pd.read_csv('cores_81(gel-filtration)_in_phage_display_r1.csv', sep = ';')
cores_81_1 = cores_81_1.filter(['Core'])
cores_81_2 = pd.read_csv('cores_81(gel-filtration)_in_phage_display_r2.csv', sep = ';')
cores_81_2 = cores_81_2.filter(['Core'])


cores_76 = pd.read_csv('cores_76.csv', sep = ';')
cores_76 = cores_76.filter(['Core']).drop_duplicates()
cores_79 = pd.read_csv('cores_79.csv', sep = ';')
cores_79 = cores_79.filter(['Core']).drop_duplicates()

#ищем коры, которые есть в ФД 1 и 2 раундов и в ИП больных, но нет в ГФ здоровых
res_78_1_except_76 = cores_78_1.merge(cores_76, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
res_78_1_except_76.to_csv("cores_78&r1_except_76.csv", index=False)
res_78_2_except_76 = cores_78_2.merge(cores_76, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
res_78_2_except_76.to_csv("cores_78&r2_except_76.csv", index=False)

#ищем коры, которые есть в ФД 1 и 2 раундов и в ИП больных, но нет в ИП здоровых
res_78_1_except_79 = cores_78_1.merge(cores_79, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
res_78_1_except_79.to_csv("cores_78&r1_except_79.csv", index=False)
res_78_2_except_79 = cores_78_2.merge(cores_79, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
res_78_1_except_79.to_csv("cores_78&r2_except_79.csv", index=False)

#ищем коры, которые есть в ФД 1 и 2 раундов и в ГФ больных, но нет в ИП здоровых
res_81_1_except_79 = cores_81_1.merge(cores_79, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
res_81_1_except_79.to_csv("cores_81&r1_except_79.csv", index=False)
res_81_2_except_79 = cores_81_2.merge(cores_79, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
res_81_2_except_79.to_csv("cores_81&r2_except_79.csv", index=False)

#ищем коры, которые есть в ФД 1 и 2 раундов и в ГФ больных, но нет в ГФ здоровых
res_81_1_except_76 = cores_81_1.merge(cores_76, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
res_81_1_except_76.to_csv("cores_81&r1_except_76.csv", index=False)
res_81_2_except_76 = cores_81_2.merge(cores_76, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
res_81_2_except_76.to_csv("cores_81&r2_except_76.csv", index=False)

#ищем пептиды, к которым относятся эти коры
nothealthy_peps_78_1_no76 = res_78_1_except_76.merge(cores_78, how = 'inner', on = 'Core')
#nothealthy_peps_78_1_no76.to_csv('peps_precipetation&PD1_not_in_76.csv', index = False)

nothealthy_peps_78_2_no76 = res_78_2_except_76.merge(cores_78, how = 'inner', on = 'Core')
#nothealthy_peps_78_2_no76.to_csv('peps_precipetation&PD2_not_in_76.csv', index = False)

nothealthy_peps_78_1_no79 = res_78_1_except_79.merge(cores_78, how = 'inner', on = 'Core')
#nothealthy_peps_78_1_no79.to_csv('peps_precipetation&PD1_not_in_79.csv', index = False)

nothealthy_peps_78_2_no79 = res_78_2_except_79.merge(cores_78, how = 'inner', on = 'Core')
#nothealthy_peps_78_2_no79.to_csv('peps_precipetation&PD2_not_in_79.csv', index = False)

nothealthy_peps_81_1_no76 = res_81_1_except_76.merge(cores_81, how = 'inner', on = 'Core')
#nothealthy_peps_81_1_no76.to_csv('peps_gelfiltration&PD1_not_in_76.csv', index = False)

nothealthy_peps_81_2_no76 = res_81_2_except_76.merge(cores_81, how = 'inner', on = 'Core')
#nothealthy_peps_81_2_no76.to_csv('peps_gelfiltration&PD2_not_in_76.csv', index = False)

nothealthy_peps_81_1_no79 = res_81_1_except_79.merge(cores_81, how = 'inner', on = 'Core')
#nothealthy_peps_81_1_no79.to_csv('peps_gelfiltration&PD1_not_in_79.csv', index = False)

nothealthy_peps_81_2_no79 = res_81_2_except_79.merge(cores_81, how = 'inner', on = 'Core')
#nothealthy_peps_81_2_no79.to_csv('peps_gelfiltration&PD2_not_in_79.csv', index = False)

#ищем супер-пептиды (которые есть в нескольких файлах), но сперва найдем те, которые есть лишь в раундах ФД,
# масс-спектрах больных и отсутствуют в МС здоровых
nothealthy_peps78_r1 = nothealthy_peps_78_1_no76.merge(nothealthy_peps_78_1_no79, how = 'inner', on = ['Core', 'Peptide'])
nothealthy_peps78_r1 = nothealthy_peps78_r1.filter(['Core', 'Peptide'])
#nothealthy_peps78_r1.to_csv('nothealthy_peps&cores_from_78(precipetation)r1.csv', index = False)

nothealthy_peps78_r2 = nothealthy_peps_78_2_no76.merge(nothealthy_peps_78_2_no79, how = 'inner', on = ['Core', 'Peptide'])
nothealthy_peps78_r2 = nothealthy_peps78_r2.filter(['Core', 'Peptide'])
#print(nothealthy_peps78_r2)
#nothealthy_peps78_r2.to_csv('nothealthy_peps&cores_from_78(precipetation)r2.csv', index = False)

#пептиды и коры, которые есть в обоих раундах и которых нет в МС здоровых
nothealthy_peps78 = nothealthy_peps78_r1.merge(nothealthy_peps78_r2, how = 'inner', on = ['Core', 'Peptide'])
#print(nothealthy_peps78)
#nothealthy_peps78.to_csv('nothealthy_peps&cores_from_78(precipetation)_both_rounds.csv', index = False)

nothealthy_peps81_r1 = nothealthy_peps_81_1_no76.merge(nothealthy_peps_81_1_no79, how = 'inner', on = ['Core', 'Peptide'])
nothealthy_peps81_r1 = nothealthy_peps81_r1.filter(['Core', 'Peptide'])
#nothealthy_peps81_r1.to_csv('nothealthy_peps&cores_from_81(gel-filtration)r1.csv', index = False)

nothealthy_peps81_r2 = nothealthy_peps_81_2_no76.merge(nothealthy_peps_81_2_no79, how = 'inner', on = ['Core', 'Peptide'])
nothealthy_peps81_r2 = nothealthy_peps81_r2.filter(['Core', 'Peptide'])
#print(nothealthy_peps78_r2)
#nothealthy_peps81_r2.to_csv('nothealthy_peps&cores_from_81(gel-filtration)r2.csv', index = False)

#пептиды и коры, которые есть в обоих раундах и которых нет в МС здоровых
nothealthy_peps81 = nothealthy_peps81_r1.merge(nothealthy_peps81_r2, how = 'inner', on = ['Core', 'Peptide'])
#print(nothealthy_peps81)
#nothealthy_peps81.to_csv('nothealthy_peps&cores_from_81(gel-filtration)_both_rounds.csv', index = False)

nothealthy_peps81_78_r1 = nothealthy_peps81_r1.merge(nothealthy_peps78_r1, how = 'inner', on = ['Core', 'Peptide'])
#print(nothealthy_peps81_78_r1)

nothealthy_peps81_78_r2 = nothealthy_peps81_r2.merge(nothealthy_peps78_r2, how = 'inner', on = ['Core', 'Peptide'])
#print(nothealthy_peps81_78_r2)

#пойдем другим способом: сперва сделаем left join коров, входящих в МС больных и здоровых,
#найдя коры, которые есть только в МС больных, и затем будем их искать в раундах ФД
cores_78_except_76 = cores_78.merge(cores_76, how = 'left', on = ['Core'])
cores_78_except_79 = cores_78.merge(cores_79, how = 'left', on = ['Core'])
cores_78_only = cores_78_except_79.merge(cores_78_except_76, how = 'inner', on = ['Peptide', 'Core'])
#print(cores_78_only)

cores_81_except_76 = cores_81.merge(cores_76, how = 'left', on = ['Core'])
cores_81_except_79 = cores_81.merge(cores_79, how = 'left', on = ['Core'])
cores_81_only = cores_81_except_79.merge(cores_81_except_76, how = 'inner', on = ['Peptide', 'Core'])
#print(cores_81_only)

cores_peps_81_78 = cores_81_only.merge(cores_78_only, how = 'inner', on = ['Peptide', 'Core'])
#print(cores_peps_81_78)
cores_peps_81_78.to_csv('cores&peps_78&81_except_76&79.csv', index = False)

long_pept1 = pd.read_csv('Anton_DRB1_1501_round1_count.csv', sep = ',')
long_pept1 = long_pept1.filter(['Sequence']).drop_duplicates()
long_pept2 = pd.read_csv('Anton_DRB1_1501_round2_count.csv', sep = ',')
long_pept2 = long_pept2.filter(['Sequence']).drop_duplicates()

Ira_cores = pd.read_csv('Ира_2022_пептиды СКВ.csv', sep = ';')
Ira_cores = Ira_cores.filter(['15 core Seq'])
Ira_cores.rename(columns = {'15 core Seq':'core_seq'}, inplace = True)
nh_cores_78 = pd.read_csv('nothealthy_peps&cores_from_78(precipetation)r1.csv', sep = ',')
nh_cores_78 = nh_cores_78.filter(['Core'])
nh_cores_81 = pd.read_csv('nothealthy_peps&cores_from_81(gel-filtration)r1.csv', sep = ',')
nh_cores_81 = nh_cores_81.filter(['Core'])

for sub in nh_cores_78.Core:
    for seq in Ira_cores.core_seq:
        if sub in seq:
            print(seq, sub, sep = ' ')

print('___')

for sub in nh_cores_81.Core:
    for seq in Ira_cores.core_seq:
        if sub in seq:
            print(seq, sub, sep = ' ')

print('___')

for core in cores_peps_81_78.Core:
    sub = core
    for j in long_pept1.Sequence:
        seq = j
        if sub in seq:
            print(seq, sub, sep = ' ')

print('___')

for i in cores_peps_81_78.Core:
    sub = i
    for j in long_pept2.Sequence:
        seq = j
        if sub in seq:
            print(seq, sub, sep = ' ')

nh_cores_r1 = pd.read_csv('nh_cores_in_r1.csv', sep = ' ').filter(['Core'])
nh_cores_peps_r1 = nh_cores_r1.merge(cores_peps_81_78, how = 'inner', on = ['Core'])
#print(nh_cores_r1.merge(cores_peps_81_78, how = 'inner', on = ['Core']))
#nh_cores_peps_r1.to_csv('vers2_peps&cores_78&81_except_76&79_r1.csv', index = False)

nh_cores_r2 = pd.read_csv('nh_cores_in_r2.csv', sep = ' ').filter(['Core'])
nh_cores_peps_r2 = nh_cores_r2.merge(cores_peps_81_78, how = 'inner', on = ['Core'])
#print(nh_cores_r2.merge(cores_peps_81_78, how = 'inner', on = ['Core']))
#nh_cores_peps_r2.to_csv('vers2_peps&cores_78&81_except_76&79_r2.csv', index = False)

super_peps = nh_cores_peps_r2.merge(nh_cores_peps_r1, how = 'inner', on = ['Peptide', 'Core'])
super_peps = super_peps.drop_duplicates()
#print(super_peps)

