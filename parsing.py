from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#print(response)
with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get(
        "http://biokb.ncpsb.org.cn/aagatlas/index.php/Home/Search/search?diseaseTerm=do~doid:9074")  # Открываем страницу
    time.sleep(120)  # Время на прогрузку страницы
    soup = BeautifulSoup(driver.page_source, 'html.parser')

#url = 'http://biokb.ncpsb.org.cn/aagatlas/index.php/Home/Search/gene/geneid/YBX1'
#url = 'http://biokb.ncpsb.org.cn/aagatlas/index.php/Home/Search/search?diseaseTerm=do~doid:9074'
#response = requests.get(url)
#bs = BeautifulSoup(response.text, 'lxml')
#print(bs)

#genes = bs.find('Gene name', "top right")
#prot = bs.find_all('a', rel = "nofollow", target="_blank")
genes_table = soup.find('table', id = "resultTable", class_ = "table table-hover")
#genes = genes_table.find_all('tr')
for i in range(260):
    ind = genes_table.find('tr', "data-index = " + str(i))
    gene = ind.find('a')
    print(gene.text)
#print(*prot, sep = ';')
