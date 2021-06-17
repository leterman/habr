KEYWORDS = ['дизайн', 'фото', 'Web', 'Python']

import requests
from bs4 import BeautifulSoup

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise RuntimeError('error')

text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

text_list = []
for text1 in soup.find_all('div', class_='post__text'):
    text_list.append(text1.get_text().strip())
mylist=[]
myset = set(mylist)

text_list = []
for text1 in soup.find_all('article', class_='post_preview'):
    text_list.append(text1.get_text().strip())
mylist=[]
for words in set(text_list):
    for keys in KEYWORDS:
        if keys in words:
            mylist.append(words)

myset = set(mylist)
mylist1 = list(myset)
list2 =[]
for xx in mylist1:
    finish = xx.replace('\n', ' ')
    finish = finish.split('  ')
    list2.append(finish)

time_list = []
for list3 in list2:
    time_name = list3[1:3]
    time_list.append(time_name)

new_list = []
for elem in time_list:
    for ele in elem:
        new_list.append(ele.lstrip())

link_list = []
for article in articles:
    hubs = [h.text.strip() for h in article.find_all('a', class_='hub-link')]
    a = article.find('a', class_ ='post__title_link')
    headline = list(a)
    linkk = a.attrs.get('href')
    b = article.find('span', class_ ='post__time')
    h = list(b)
    list10 = [h, headline, linkk]
    link_list.append(list10)

for linkss in link_list:
    for kin in linkss[1]:
        if kin in new_list:
            print(linkss)