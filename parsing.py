from bs4 import BeautifulSoup
import requests

#print(response)

url = 'http://biokb.ncpsb.org.cn/aagatlas/index.php/Home/Search/gene/geneid/YBX1'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')
print(bs)

#genes = bs.find('Gene name', "top right")
prot = bs.find_all('a', rel = "nofollow", target="_blank")
gene = bs.find('h3')
print(gene.text)
print(*prot, sep = ';')
