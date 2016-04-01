import requests
import robot
def send_simple_message(subject, text):
	with open('/home/ubuntu/documents/robot-vegetarian/emails.txt','r') as efile, \
	     open('/home/ubuntu/documents/robot-vegetarian/mailgun_apikey.txt','r') as apifile:
		emails = efile.read().split('\n')[:-1]
		apikey = apifile.read().split('\n')[0]
		return requests.post(
        	"https://api.mailgun.net/v3/sandbox26d5624408cd4278947603488d35a53c.mailgun.org/messages",
        	auth=("api", apikey),
        	data={"from": "Vegetarian Robot <postmaster@sandbox26d5624408cd4278947603488d35a53c.mailgun.org>",
              	"to": emails,
              	"subject": subject,
              	"text": text})

if __name__ == '__main__':
	timeStamp = ''
	with open ('/home/ubuntu/documents/robot-vegetarian/timeStamp.txt','r') as rfile:
		timeStamp = rfile.read().split('\n')[0]

	# store(title,storeName,publishedTime,info,lng,lat,content_url,website)
	stores = robot.robot_vegetarianStore()

	subject = '[發現新素食店]'
	text = ''
	newTimeStamps = list()
	for store in stores:
		if timeStamp < store[2]:
			text += """文章標題：{7}\n店名：{0}\n{1}\n座標：{2},{3}\n發文時間：{4}\n網站來源：{5}\n臉書或blog:{6}\n\n"""\
			.format(store[1],store[3],store[4],store[5],store[2],store[6],store[7],store[0])
			newTimeStamp.append(store[2])
	if len(text) > 0:
		send_simple_message(subject, text)
		with open('/home/ubuntu/documents/robot-vegetarian/timeStamp.txt','w') as wfile:
			wfile.write(max(newTimeStamps))



