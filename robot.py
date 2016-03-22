import requests
from bs4 import BeautifulSoup

website = 'http://clnote.tw/'

req = requests.get(website)
soup = BeautifulSoup(req.text, 'html.parser')

articles = soup.find('div',{'id':'main', 'class':'site-main'}).find_all('article')


for article in articles:
	title = article.h1.text
	postTime = article.span.a.text
	content_url = article.h1.a['href']
	content = BeautifulSoup(requests.get(content_url).text, 'html.parser')
	