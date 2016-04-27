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
		print ("Sent mail to {0}".format(emails))
if __name__ == '__main__':
	timeStamp = ''
	with open ('/home/ubuntu/documents/robot-vegetarian/timeStamp.txt','r') as rfile:
		timeStamp = rfile.read().split('\n')[0]
	print ("timestamp: {0}".format(timeStamp))
	# store(title,storeName,publishedTime,info,lng,lat,content_url,website)
	stores = robot.robot_vegetarianStore(timeStamp)

	print ("Preparing content of mail...")
	subject = '[發現新素食店]'
	text = ''
	newTimeStamps = list()
	print ("len of stores:{0}".format(len(stores)))
	for store in stores:
		text += """文章標題：{7}\n店名：{0}\n{1}\n座標：{2},{3}\n發文時間：{4}\n網站來源：{5}\n臉書或blog:{6}\n\n"""\
		.format(store[1],store[3],store[4],store[5],store[2],store[6],store[7],store[0])
		newTimeStamps.append(store[2])

		# Push data to lab api (instants)			
		#r = requests.post('http://52.192.20.250/chat/create/robot/', data = {
		#	'robot_id':'108143422899450',
		#	'content':store[0],
		#	'lng':store[4],
		#	'lat':store[5]
		#})
	print ("Sending emails...")
	if len(text) > 0:
		send_simple_message(subject, text)
		with open('/home/ubuntu/documents/robot-vegetarian/timeStamp.txt','w') as wfile:
			wfile.write(max(newTimeStamps))

