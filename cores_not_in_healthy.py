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
nothealthy_peps_78_1_no76.to_csv('peps_precipetation&PD1_not_in_76.csv', index = False)

nothealthy_peps_78_2_no76 = res_78_2_except_76.merge(cores_78, how = 'inner', on = 'Core')
nothealthy_peps_78_2_no76.to_csv('peps_precipetation&PD2_not_in_76.csv', index = False)

nothealthy_peps_78_1_no79 = res_78_1_except_79.merge(cores_78, how = 'inner', on = 'Core')
nothealthy_peps_78_1_no79.to_csv('peps_precipetation&PD1_not_in_79.csv', index = False)

nothealthy_peps_78_2_no79 = res_78_2_except_79.merge(cores_78, how = 'inner', on = 'Core')
nothealthy_peps_78_2_no79.to_csv('peps_precipetation&PD2_not_in_79.csv', index = False)

nothealthy_peps_81_1_no76 = res_81_1_except_76.merge(cores_81, how = 'inner', on = 'Core')
nothealthy_peps_81_1_no76.to_csv('peps_gelfiltration&PD1_not_in_76.csv', index = False)

nothealthy_peps_81_2_no76 = res_81_2_except_76.merge(cores_81, how = 'inner', on = 'Core')
nothealthy_peps_81_2_no76.to_csv('peps_gelfiltration&PD2_not_in_76.csv', index = False)

nothealthy_peps_81_1_no79 = res_81_1_except_79.merge(cores_81, how = 'inner', on = 'Core')
nothealthy_peps_81_1_no79.to_csv('peps_gelfiltration&PD1_not_in_79.csv', index = False)

nothealthy_peps_81_2_no79 = res_81_2_except_79.merge(cores_81, how = 'inner', on = 'Core')
nothealthy_peps_81_2_no79.to_csv('peps_gelfiltration&PD2_not_in_79.csv', index = False)

#ищем супер-пептиды (которые есть в нескольких файлах), но сперва найдем те, которые есть лишь в раундах ФД,
# масс-спектрах больных и отсутствуют  МС здоровых
nothealthy_peps78_r1 = nothealthy_peps_78_1_no76.merge(nothealthy_peps_78_1_no79, how = 'inner', on = ['Core', 'Peptide'])
nothealthy_peps78_r1 = nothealthy_peps78_r1.filter(['Core', 'Peptide'])
nothealthy_peps78_r1.to_csv('nothealthy_peps&cores_from_78(precipetation)r1.csv', index = False)

nothealthy_peps78_r2 = nothealthy_peps_78_2_no76.merge(nothealthy_peps_78_2_no79, how = 'inner', on = ['Core', 'Peptide'])
nothealthy_peps78_r2 = nothealthy_peps78_r2.filter(['Core', 'Peptide'])
#print(nothealthy_peps78_r2)
nothealthy_peps78_r2.to_csv('nothealthy_peps&cores_from_78(precipetation)r2.csv', index = False)

#пептиды и коры, которые есть в обоих раундах и которых нет в МС здоровых
nothealthy_peps78 = nothealthy_peps78_r1.merge(nothealthy_peps78_r2, how = 'inner', on = ['Core', 'Peptide'])
#print(nothealthy_peps78)
nothealthy_peps78.to_csv('nothealthy_peps&cores_from_78(precipetation)_both_rounds.csv', index = False)

nothealthy_peps81_r1 = nothealthy_peps_81_1_no76.merge(nothealthy_peps_81_1_no79, how = 'inner', on = ['Core', 'Peptide'])
nothealthy_peps81_r1 = nothealthy_peps81_r1.filter(['Core', 'Peptide'])
nothealthy_peps81_r1.to_csv('nothealthy_peps&cores_from_81(gel-filtration)r1.csv', index = False)

nothealthy_peps81_r2 = nothealthy_peps_81_2_no76.merge(nothealthy_peps_81_2_no79, how = 'inner', on = ['Core', 'Peptide'])
nothealthy_peps81_r2 = nothealthy_peps81_r2.filter(['Core', 'Peptide'])
#print(nothealthy_peps78_r2)
nothealthy_peps81_r2.to_csv('nothealthy_peps&cores_from_81(gel-filtration)r2.csv', index = False)

#пептиды и коры, которые есть в обоих раундах и которых нет в МС здоровых
nothealthy_peps81 = nothealthy_peps81_r1.merge(nothealthy_peps81_r2, how = 'inner', on = ['Core', 'Peptide'])
#print(nothealthy_peps81)
nothealthy_peps81.to_csv('nothealthy_peps&cores_from_81(gel-filtration)_both_rounds.csv', index = False)

nothealthy_peps81_78_r1 = nothealthy_peps81_r1.merge(nothealthy_peps78_r1, how = 'inner', on = ['Core', 'Peptide'])
print(nothealthy_peps81_78_r1)

nothealthy_peps81_78_r2 = nothealthy_peps81_r2.merge(nothealthy_peps78_r2, how = 'inner', on = ['Core', 'Peptide'])
print(nothealthy_peps81_78_r2)

#пойдем другим способом: сперва сделаем left join коров, входящих в МС больных и здоровых,
#найдя коры, которые есть только в МС больных, и затем будем их искать в раундах ФД
