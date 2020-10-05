#!/usr/bin/python3
'''
Author: Shamugia Genadi
Project: User Frequency Calculator
Description: Program takes csv files which are twitter scraper captures and counts the number of occurances of each username. 
'''
#Importing used librarires
import csv
import sys
import ast
import os
import glob

def main():

    path = sys.argv[1]
    files = os.listdir(path)

    # files_csv = [i for i in files if i.endswith('.csv')]
    usernameList = [] #List for all the usernames
    #Open and read the csv file.
    for f in files:
        if f.endswith('.csv'):
            print('Reading file ' + f + '. Please wait...')
            with open(path+'/'+str(f)) as csv_file: 
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    try:
                        cell = ast.literal_eval(row[4])
                        username = cell['user_mentions'][0]['screen_name'] #grab the username
                        usernameList.append(username)
                        line_count += 1
                    except Exception: #Exception for unusual cases
                        line_count +=1
                        pass
    
    CountFrequency(usernameList) 

def CountFrequency(my_list): 
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1

    #order the Dictionary by Value in descending order
    sorted_orders = sorted(freq.items(), key=lambda x:x[1],reverse=True)
    # print(type(sorted_orders))


    #Write to a csv file one row at a time 
    with open("output.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerows(sorted_orders)
    fp.close()
main()