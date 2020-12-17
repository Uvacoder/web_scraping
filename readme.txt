#lines.select('#mw-toc-heading')

#for i in lines.select('#mw-toc-heading'):


lines.select('.kn')
for i in lines.select('.kn'):
    print(i.text)



for link in sup.find_all('a', herf = True):
    print(link['herf'])


text-white fadeInLeft

kn
href=True


res.text

https://web.learncodeonline.in


mw-headline
https://en.wikipedia.org/wiki/Web_scraping






for link in soup.find_all('a', href=True):

    first_two_char = link['href'][:2]

    if "#" not in link['href']:
        if first_two_char != '//':
            print(link['href'])

    if(first_two_char == '//'):
        base_link = 'www.google.co.in/'
        final_link = base_link + link['href'][2:]
        print(final_link)



