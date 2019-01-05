import sys
from flask import Flask, jsonify, render_template, request, Response
import meetup as mtup
import random, json
import pastebin as pb
import time

app = Flask(__name__)

@app.route('/')
def home():
	print("home")
	return render_template('index.html')

@app.route("/sendMessageOrg", methods=['POST'])
def sendMessageOrg():
	datas = request.get_json()
	email = datas['email']
	password = datas['password']
	organizers = datas['organizers']
	messages = datas['messages']
	timespaces = datas['timespaces']
	for timespace in timespaces:
		timespace = timespace[:-12]
	print("TimeSpaces")
	print(timespaces)
	print("-------------------")
	# print(type(browser))
	msg_urls = list()
	#upload messages to pasted.co and get url of messages
	browser = pb.getBrowser()
	for message in messages:
		temp = list()
		for organizer in organizers:
			if organizer!='':
				temp.append(pb.createMessageURL(browser, message))
		msg_urls.append(temp)
	timelist=list()
	for timespace in timespaces:
		temp = list()
		for organizer in organizers:
			if organizer!='':
				temp.append(timespace[:-12])
		timelist.append(temp)
	pb.closeBrowser(browser)
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print(msg_urls)
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print(timelist)
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	#Meetup Automation
	browser = mtup.getBrowser()
	print(datas)
	print("email:")
	print(email)
	print("password:")
	print(password)
	time.sleep(5)
	sId = mtup.login(browser,email, password)
	print(sId)
	index = 0
	for msg_url in msg_urls:
		for message in msg_url:
			for organizer in organizers:
				if organizer!='':
					mtup.sendMessage(browser, organizer, message, sId)
			time.sleep(60)
	mtup.closeBrowser(browser)
	return "ok"

@app.route("/sendMessageMembers", methods=['POST'])
def sendMessageMembers():
	data = request.get_json()
	email = data['email']
	password = data['password']
	members = data['members']
	messages = data['messages']
	timespaces = data['timespaces']
	browser = mtup.getBrowser()
	msg_urls = list()
	#upload messages to pasted.co and get url of messages
	for message in messages:
		if message!='':
			msg_urls.append(pb.createMessageURL(browser, message))
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print(msg_urls)
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	# print(type(browser))
	print(datas)
	print("email:")
	print(email)
	print("password:")
	print(password)
	sId = mtup.login(browser,email, password)
	for member in members:
		for msg_url in msg_urls:
			if member!='':
				if msg_url!='':
					mtup.sendMessage(browser, member, msg_url, sId)
					print("member:")
					print(member)
					print("message:")
					print(msg_url)
	mtup.closeBrowser(browser)
	return "ok"

@app.route("/stop", methods=['POST'])
def stop():
	print("stop")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)