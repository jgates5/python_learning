"""
#type python

import requests

from bs4 import BeautifulSoup

r = requests.get('http://www.dailysmarty.com/topics/python') 
r.text
soup = BeautifulSoup(r.text, 'html.parser')
soup
links = soup.find_all('a')
links
for link in links:
    print(link['href'])
create

"""
"""
import requests
from bs4 import BeautifulSoup

#creating a genreator for posts
def titles_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            titles.append(url)

    for link in links:
        post_formatter(link['href'])
        #print(link['href'])

    return titles

r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')

#titles_generator(links)
print(titles_generator(links))


#for link in links:
 #   print(link['href'])
 """
# import requests
# from bs4 import BeautifulSoup
# from inflection import titleize

# def titles_generator(links):
#     titles = []

#     def post_formatter(url):
#         if 'posts' in url:
#             url = url.split('/')[-1]
#             url = url.replace('-', ' ')
#             url = titleize(url)
#             titles.append(url)


#     for link in links:
#         post_formatter(link["href"])

#     return titles


# r = requests.get('http://www.dailysmarty.com/topics/python')
# soup = BeautifulSoup(r.text, 'html.parser')
# links = soup.find_all('a')

# titles = titles_generator(links)

# for title in titles:
#     print(title)

import requests  
import inflection
from bs4 import BeautifulSoup 

page = requests.get('http://www.dailysmarty.com/topics/python') 
soup = BeautifulSoup(page.text, 'html.parser')

for a in soup.select('.post-link-title h2 a'): 
    print(inflection.titleize((a['href'].replace('/posts/', '"')).replace('-', ' ')) + '"')
    