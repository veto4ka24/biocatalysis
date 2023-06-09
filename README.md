# biocatalysis
проекты для статей лаборатории

Файл 'res_peptides.csv' содержит пересечения белков в таблицах MZ81 и MZ78, при этом каждому белку в соответствие поставлены все возможные пептиды из обоих файлов.

Файл 'task2_lab.txt' содержит пересечения двух исходных файлов по белкам и пептидам одновременно, т.е. на выходе имеем таблицу, где каждому белку соответствует один или несколько пептидов, и такие пары присутствуют в обоих сырых файлах.

Файлы с названием вида 'MZpq_in_DRB1_roundk' -- содержание пептида из таблиц MZ81 и MZ78 в сиквенсах фагового дисплея.

Файлы с названием вида 'MZ78_merge_MZ81_in_DRB1_roundk' -- содержание пептида, который есть в обеих таблицах MZ81 и MZ78, в сиквенсах фагового дисплея.

Последние актуальные изменения: в файлах, добавленных после середины мая, исследуются пересечения генов из антиген атласа с генами из файлов с пробами здоровых и больных людей. При отсутствии генов, которые есть в антиген атласе и присутствуют в пробах больных людей, в пробах здоровых, данные гены считаются связанными с наличием у пациентов заболевания СКВ (системной красной волчанки). Однако присутствие таких генов еще и в отборах фаговым дисплеем делает их "супергенами", поскольку они есть во всех отборах больных. Таких генов не обнаружено. Есть лишь гены, содержащиеся в иммунопреципетации больных (MZ78) и гель-фильтрации (MZ81) одновременно, но не входящие ни в одну из проб здоровых пациентов (MZ79, MZ76). Данные гены приведены в файлах "not_in_MZ76(9)_but_in_MZ81&MZ78", и в обоих файлах эти гены одинаковы -- CALR и RPS13. Повторную проверку отсутствия других "супергенов" осуществляем с помощью  поисков пересечений экспрессируемых пептидов в раундах фагового дисплея с пептидами на масс-спектрах больных и затем сравнения списка генов, экспрессирующих данные пептиды, с генами из антиген атласа. Повторная проверка дала иной результат, который записан в файле findings.md.
