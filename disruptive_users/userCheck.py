#!/usr/bin/env python3

import requests 
import time 

#/analyze?twitterHandleInput=https%3A%2F%2Ftwitter.com%2Figuideclaus2020
problemUsers = {}
allUsers = []
url = 'https://botsentinel.com/analyze?twitterHandleInput=https://twitter.com/'

with open('output.csv') as file: 
	for line in file: 
		if line.startswith(','): 
			continue 
		user = line.split(',')[0]
		allUsers.append(user.strip())

for user in allUsers:
	try:  
		time.sleep(5)
		print(f'Checking user {user} at url: {url+user}')
		req = requests.get(url+user, verify=False) 
		data = req.json()
		if data['success'] == False: 
			print('User not found by bot sentinel')
			continue

		score = data['data']['score']

		try: 
			if score >= 15:
				problemUsers[user] = score
		except: 
			print(f'Error occured checking user {user}')
			continue
	except: 
		continue 

print(f'Number of problem users found in our tweet database: {len(problemUsers)}')

with open('users.txt', 'w') as file: 
	for k,v in problemUsers.items(): 
		file.write(f'{k} : {v}')

