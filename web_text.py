from bs4 import BeautifulSoup
import requests

url = 'https://byjus.com/ncert-solutions-class-12-maths/'
request = requests.get(url)
html_data = request.content

soup = BeautifulSoup(html_data,'html.parser')
text = soup.find_all(text = True)
set([t.parent.name for t in text])
result = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    'style'
]
for t in text:
    if t.parent.name not in blacklist:
        result += '{} '.format(t)

print(result)