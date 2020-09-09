import csv
import sys
import ast

def main():
    usernameList = []

    with open(sys.argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            try:
                cell = ast.literal_eval(row[4])
                username = cell['user_mentions'][0]['screen_name']
                usernameList.append(username)
                line_count += 1
            except Exception:
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
    
  
    for key, value in freq.items(): 
        print ("% s : % d"%(key, value)) 

main()