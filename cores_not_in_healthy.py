import pandas as pd

cores_78_1 = pd.read_csv('cores_78(precipetation)_in_phage_display_r1.csv', sep = ';')
cores_78_1 = cores_78_1.filter(['Core']).drop_duplicates()
cores_78_2 = pd.read_csv('cores_78(precipetation)_in_phage_display_r2.csv', sep = ';')
cores_78_2 = cores_78_2.filter(['Core']).drop_duplicates()
cores_81_1 = pd.read_csv('cores_81(gel-filtration)_in_phage_display_r1.csv', sep = ';')
cores_81_1 = cores_81_1.filter(['Core']).drop_duplicates()
cores_81_2 = pd.read_csv('cores_81(gel-filtration)_in_phage_display_r2.csv', sep = ';')
cores_81_2 = cores_81_2.filter(['Core']).drop_duplicates()

cores_76 = pd.read_csv('cores_76.csv', sep = ';')
cores_76 = cores_76.filter(['Core']).drop_duplicates()
cores_79 = pd.read_csv('cores_79.csv', sep = ';')
cores_79 = cores_79.filter(['Core']).drop_duplicates()

#ищем коры, которые есть в ФД 1 и 2 раундов и в ИП больных, но нет в ГФ здоровых
res_78_1_except_76 = cores_78_1.merge(cores_76, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
#res_78_1_except_76.to_csv("cores_78&r1_except_76.csv", index=False)
res_78_2_except_76 = cores_78_2.merge(cores_76, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
#res_78_2_except_76.to_csv("cores_78&r2_except_76.csv", index=False)

#ищем коры, которые есть в ФД 1 и 2 раундов и в ИП больных, но нет в ИП здоровых
res_78_1_except_79 = cores_78_1.merge(cores_79, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
#res_78_1_except_79.to_csv("cores_78&r1_except_79.csv", index=False)
res_78_2_except_79 = cores_78_2.merge(cores_79, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
#res_78_1_except_79.to_csv("cores_78&r2_except_79.csv", index=False)

#ищем коры, которые есть в ФД 1 и 2 раундов и в ГФ больных, но нет в ИП здоровых
res_81_1_except_79 = cores_81_1.merge(cores_79, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
#res_81_1_except_79.to_csv("cores_81&r1_except_79.csv", index=False)
res_81_2_except_79 = cores_81_2.merge(cores_79, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
#res_81_2_except_79.to_csv("cores_81&r2_except_79.csv", index=False)

#ищем коры, которые есть в ФД 1 и 2 раундов и в ГФ больных, но нет в ГФ здоровых
res_81_1_except_76 = cores_81_1.merge(cores_76, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
#res_81_1_except_76.to_csv("cores_81&r1_except_76.csv", index=False)
res_81_2_except_76 = cores_81_2.merge(cores_76, how = 'left', on = 'Core', indicator = True).query("_merge == 'left_only'")
#res_81_2_except_76.to_csv("cores_81&r2_except_76.csv", index=False)

