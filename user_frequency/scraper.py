#!/usr/bin/env python3

import json
import collections
from collections import Counter
import operator
import os
import os.path
from os import path
#tiktok-scraper hashtag CONSERVATIVE -t json -f conservative -n 0


def parser(filename):
	with open(filename) as file:
		data = json.load(file)
		print(filename)

	authors = []
	#print(len(data))
	for i in range(len(data)):
		#print(i , "Data: " , data[i], "\n\n")
		authors.append(data[i]["authorMeta"]["name"])

	actives = {}
	actives = Counter(authors)
	final = {}
	#unique = ([item for item, count in collections.Counter(authors).items() if count > 1])
	for key,val in actives.items():
		if val > 5:
			final[key] = val

	sorted_final = sorted(final.items(), key=operator.itemgetter(1), reverse=True)
	sorted_dict = collections.OrderedDict(sorted_final)
	accountsOfInterest(sorted_dict, filename)
	return sorted_dict

def accountsOfInterest(accounts, filename):
	with open("accountsOfInterest.txt", "a") as file:
		file.write("\n\n" + str(filename) + "\n\n")
		for k, v in accounts.items():
			file.write(str(k) + ": " + str(v) + "\n")


def main():
	directory = os.fsencode(".")
	for file in os.listdir(directory):
	     filename = os.fsdecode(file)
	     if filename.endswith(".json"):
	       parser(filename)
	     else:
	         continue
main()
