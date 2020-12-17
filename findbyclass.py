import requests
import bs4

inputurl = input('Give the URL:- ')
open = requests.get(inputurl)
lines = bs4.BeautifulSoup(open.text, 'lxml')

inputclass = input('  The class name is:-')
lines.select('.'+inputclass)
for i in lines.select('.'+inputclass):
    print(i.text)








