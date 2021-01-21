import tweepy #https://github.com/tweepy/tweepy
import csv
import pandas as pd
# Used for progress bar
import time
import sys

#Twitter API credentials
consumer_key = "NBNgPGCBeGv80PcsYU3QWU94d"
consumer_secret = "lvAaoSInlF9mPonoMMldFq5ZE96oAAl30TLh6ynVwK2tauvOQC"
access_key = "1311728151265832961-AaFHXfZtozEgfoVZoFnNqzqRZEWQAr"
access_secret = "Az8Ezlg77NtkZ8coTqXGsXW2wVh7Wbpm3JTsAkoPsrq7z"

OAUTH_KEYS = {'consumer_key':consumer_key, 'consumer_secret':consumer_secret,
 'access_token_key':access_key, 'access_token_secret':access_secret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = tweepy.Cursor(api.search, q='#Trump').items(4000)


# Create lists for each field desired from the tweets.
sn = []
text = []
timestamp =[]
for tweet in search:
    #print tweet.user.screen_name, tweet.created_at, tweet.text
    timestamp.append(tweet.created_at)
    sn.append(tweet.user.screen_name)
    text.append(tweet.text)

# Convert lists to dataframe
df = pd.DataFrame()
df['timestamp'] = timestamp
df['sn'] = sn
df['text'] = text

# Prepare ford date filtering. Adding an EST time column since chat hosted by people in that time zone.
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['EST'] = df['timestamp'] - pd.Timedelta(hours=5) #Convert to EST

df['EST'] = pd.to_datetime(df['EST'])

# Subset for the dates required. Can select a specific date or time to examine.
import time
df = df[(pd.to_datetime("2015-12-14 20:00:00", format='%Y-%m-%d %H:%M:%S') < df['EST']) & (df['EST'] < pd.to_datetime("2015-12-14 21:00:00", format='%Y-%m-%d %H:%M:%S'))]


# Write out Tweets in case they are needed later.
df.to_csv('edtechtweets.csv',index = False,encoding='utf-8')

# Create a list of the unique usernames in order to see which users we need to retrieve friends for.
allNames = list(df['sn'].unique())

# Initialize dataframe of users that will hold the edge relationships
dfUsers = pd.DataFrame()
dfUsers['userFromName'] =[]
dfUsers['userFromId'] =[]
dfUsers['userToId'] = []
count = 0

nameCount = len(allNames)
# The choice to retrieve friends (who the user is following) rather than followers is intentional.
# Either would work. However, many Twitter users follow fewer users than are following them, especially the most popular accounts. 
# This reduces the number of very large calls to Twitter API, which seemed to cause problems.
for name in allNames:
    # Build list of friends    
    currentFriends = []
    for page in tweepy.Cursor(api.friends_ids, screen_name=name).pages():
        currentFriends.extend(page)
    currentId = api.get_user(screen_name=name).id
    currentId = [currentId] * len(currentFriends)
    currentName = [name] * len(currentFriends)   
    dfTemp = pd.DataFrame()
    dfTemp['userFromName'] = currentName
    dfTemp['userFromId'] = currentId
    dfTemp['userToId'] = currentFriends
    dfUsers = pd.concat([dfUsers,dfTemp])
    time.sleep(70) # avoids hitting Twitter rate limit
    # Progress bar to track approximate progress
    count +=1
    per = round(count*100.0/nameCount,1)
    sys.stdout.write("\rTwitter call %s%% complete." % per)
    sys.stdout.flush()

# Again, to limit the number of calls to Twitter API, just do lookups on followers that connect to those in our user group.
# We are not interested in "friends" that are not part of this community.
fromId = dfUsers['userFromId'].unique()
dfChat = dfUsers[dfUsers['userToId'].apply(lambda x: x in fromId)]

# No more Twitter API lookups are necessary. Create a lookup table that we will use to get the verify the userToName
dfLookup = dfChat[['userFromName','userFromId']]
dfLookup = dfLookup.drop_duplicates()
dfLookup.columns = ['userToName','userToId']
dfCommunity = dfUsers.merge(dfLookup, on='userToId')

dfCommunity.to_csv('dfCommunity.csv',index = False,encoding='utf-8')