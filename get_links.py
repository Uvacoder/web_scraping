import requests
import bs4

inputlink = input('Give the URL :- ' )

res = requests.get(inputlink)
sup = bs4.BeautifulSoup(res.text, 'lxml')
print('The links are:- ')

for link in sup.find_all('a', href=True):                      #Use bs4 to get links
    first_two_word = link['href'][:2]                          #Put first 2 word

    if (first_two_word != '/#'):                               #Identify the links
        if (first_two_word == 'ht'):
            print(link['href'])

        if (first_two_word != 'ht'):
            main_link = inputlink
            final_link = main_link + link['href']
            print(final_link)


