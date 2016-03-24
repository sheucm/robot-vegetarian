import requests
import robot

def send_simple_message(subject, text):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox26d5624408cd4278947603488d35a53c.mailgun.org/messages",
        auth=("api", "key-6b8f571839aa0f405f77c30f847e6f09"),
        data={"from": "Vegetarian Robot <postmaster@sandbox26d5624408cd4278947603488d35a53c.mailgun.org>",
              "to": ["st0502123@gmail.com"],
              "subject": subject,
              "text": text})


if __name__ == '__main__':
	timeStamp = ''
	with open ('timeStamp.txt','r') as rfile:
		timeStamp = rfile.read().split('\n')[0]
	print (timeStamp)

	# store(title,storeName,publishedTime,info,lng,lat,content_url,website)
	stores = robot.robot_vegetarianStore()

	subject = '[發現新素食店]'
	text = ''
	for store in stores:
		if timeStamp < store[2]:
			text += """文章標題：{7}\n店名：{0}\n{1}\n座標：{2},{3}\n發文時間：{4}\n網站來源：{5}\n臉書或blog:{6}\n\n"""\
			.format(store[1],store[3],store[4],store[5],store[2],store[6],store[7],store[0])

	send_simple_message(subject, text)




