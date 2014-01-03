#!/usr/bin/env python
import smtplib
import argparse
import json
from email.MIMEMultipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

import os

from email.MIMEText import MIMEText

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Send gmail email via command line")

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-c', '--conf', help="the json formatted config file with sending details", type=file)

	args = parser.parse_args()

	conf = json.load(args.conf)


	msg = MIMEMultipart('alternative') #html email mimetype
	msg['From'] = conf.get('from')
	msg['To'] = conf.get('to')
	msg['Subject'] = conf.get('subject')
	# html_file = open(conf.get('html_body_file'))
	with open(conf.get('html_body_file'), 'r') as html_file:
		# msg.attach( MIMEText('this is the text alternative', 'plain') ) #text version
		msg.attach( MIMEText( html_file.read(), 'html') ) #html version




	# #attach image
	# img_file = open("./email-button.jpg") #asset for the html
	# msg.attach(MIMEImage(img_file.read()))
	# img_file.close()



	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(os.environ['OFFICE_MAIL'], os.environ['OFFICE_MAIL_PASS'])
	server.sendmail(conf.get('from'), conf.get('to'), msg.as_string())
	server.quit()