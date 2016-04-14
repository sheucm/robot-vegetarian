import requests
import dryscrape
from bs4 import BeautifulSoup
import json
import re
import sys

if 'linux' in sys.platform:
	dryscrape.start_xvfb()

def __is_info(p):
	pattern = re.compile(r'(.*\n)?(.+：.+\n)+')
	r = pattern.match(p)
	return True if r is not None else False

def __extract_info(p_all):
	result = []
	for p in p_all:
		if __is_info(p.text) is True:
			result.append(p)
	return result

def robot_vegetarianStore(timeStamp = '2016-03-01'):
	WEBSITE = 'http://clnote.tw/'
	results = list()
	req = requests.get(WEBSITE)
	soup = BeautifulSoup(req.text, 'html.parser')
	articles = soup.find('div',{'id':'main', 'class':'site-main'}).find_all('article')


	API_KEY = ''
	with open('/home/ubuntu/documents/robot-vegetarian/geocoding_apikey.txt','r') as rfile:
		API_KEY = rfile.read().split('\n')[0]

	for idx, article in enumerate(articles):
		title = article.h1.text.encode('latin1').decode('utf8')
		publishedTime = article.span.a.find('time',{'class':'entry-date published'}).text
		content_url = article.h1.a['href']

		if publishedTime < timeStamp:
			continue

		print ("drive to article content")
		session = dryscrape.Session(base_url = 'http://google.com')
		session.visit(content_url)
		content = BeautifulSoup(session.body(), 'html.parser')
		p_all = content.find('div',{'class':'entry-content'}).find_all('p')

		infos = __extract_info(p_all)

		info = infos[0]  # Extract one for example if there are many infos
		# Extract info
		storeName = info.strong.text
		address = info.text.split('\n')[1].split('：')[1][:-4]
		openingTime = info.text.split('\n')[2].split('：')[1]
		phone = info.text.split('\n')[3].split('：')[1]
		website = info.text.split('\n')[4].split('：')[1]


		geocoding_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address,API_KEY)
		geocode = requests.get(geocoding_url)
		jsonGeo = json.loads(geocode.text)
		lng = jsonGeo['results'][0]['geometry']['location']['lng']
		lat = jsonGeo['results'][0]['geometry']['location']['lat']

		print ("{0}\n{1}\n{2}\n{3}\n{4},{5}\n\n".format(title,publishedTime,content_url,address,lng,lat))
		results.append((title,storeName,publishedTime,info.text,lng,lat,content_url,website))
		
		if idx == 1:
			break		
	return results


if __name__ == '__main__':
	timeStamp = ''
	with open ('/home/ubuntu/documents/robot-vegetarian/timeStamp.txt','r') as rfile:
		timeStamp = rfile.read().split('\n')[0]
	print (timeStamp)
	results = robot_vegetarianStore()
	print (results[0])
	if timeStamp < results[0][2]:
		print ('New found store')



