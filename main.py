import sys
from flask import Flask, jsonify, render_template, request, Response
import meetup as mtup
import random, json

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
	browser = mtup.getBrowser()
	# print(type(browser))
	print(datas)
	print("email:")
	print(email)
	print("password:")
	print(password)
	sId = mtup.login(browser,email, password)
	for organizer in organizers:
		for message in messages:
			if organizer!='':
				if message!='':
					mtup.sendMessage(browser, organizer, message, sId)
					print("organizer:")
					print(organizer)
					print("message:")
					print(message)
	return "ok"

@app.route("/sendMessageMembers", methods=['POST'])
def sendMessageMembers():
	data = request.get_json()
	email = data['email']
	password = data['password']
	members = data['members']
	messages = data['messages']
	return "ok"

@app.route("/stop", methods=['POST'])
def stop():
	print("stop")

if __name__ == '__main__':
    app.run(debug=True)