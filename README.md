# robot-vegetarian

### Main to scape the vegetarian website of http://clnote.tw/.
### It will notify the users with emails in emails.txt file if there are latest posts after the date in timestamp.txt.
### Notified content includes post title, store name, address, geometry location, opening time, telephone, website of store, and url of this post.

## How to run this project
- git clone our project.
- Install virtualenv to get create the virtual environment of python. 
	`virtualenv ENV --python=/your/python3/path/`
- Enter the virtual mode:
	'''
	source ENV/bin/activate
	'''
- Get the requirements of python package
	'''
	pip install -r requirements.txt
	'''
- Create emails.txt for your notified users. 
	'''
	exmaple1@email.com
	example2@email.com
	'''
- Apply mailgun api key in its website, and put it in the mailgun_apikey.txt file. (Just copy it to the file.)
- Apply google geocode api key, and put it in the geocoding_apikey.txt file.
## How to set crontab to scrap it routinely
	- Install all of the requirements of python package out of the virtual environment.
	- Get into the crontab
	'''
	crontab -e
	'''
	- For example, daily scrap the website.
	'''
	1 1 * * * python3 ~/documents/robot-vegetarian/mailgun.py
	'''
	- See the crontab log
	'''
	grep CRON /var/log/syslog
	'''