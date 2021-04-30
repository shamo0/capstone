# Analyzing Twitter’s Influence on the 2020 Election

![poster](Poster.jpg)


## Purpose

- Analyze data from social media sites to understand how certain groups are trying to manipulate the election. 
- Once initial data has been analyzed, form a hypothesis on what we believe affected the 2020 election results. 

We utilize machine learning algorithms to break down data sets coherently and come to logical conclusions.

## Social Media Data Scraping

In order to perform analysis we had to get all the necessary data from the different social network platforms. 

Our group used Application Programming Interfaces (APIs) to scrape information related to the elections using certain hashtags and keywords from Twitter, Instagram, Tiktok, etc.

Using all this data we can later determine which users were the most active, what were the different ways they tried to influence the elections etc.


## Data Sources

Twitter: Data collected by using tweepy 
https://github.com/tweepy/tweepy

Instagram: Data collected by using instagram-scraper from GitHub
https://github.com/arc298/instagram-scraper

Tik Tok: Data collected by using tiktok scraper
https://github.com/drawrowfly/tiktok-scraper	

(Initially project was focused on all social media, however we eventually narrowed the scope down to Twitter)


## Data Analysis

### Sentiment Analysis
Sentiment analysis is a process of computationally categorizing opinions in a piece of text. It is used as a measure of writer’s attitude towards a particular topic. We used Natural Language toolkit library to analyse the sentiment of the data over the different time periods. NLTK employs several methods of extracting positive, negative and neutral sentiments from an electronic text. 


### Wordcloud
Visual representation of the captured tweets over the months of September, October, November. The more often the w ord is encountered in the data the larger the word will be in the cloud. Wordcloud was generated using more than 4 million tweets gathered over the months of September, October and November.  Wordcloud gives us a good representation election related data by the use of the popular tag words encountered on the twitter platform. 
The word clouds can be found under wordcloud directory in Jupyter Notebooks.

### Disruptive Users
In an effort to identify popular users that were spreading disinformation, we needed to score twitter accounts that we captured based on their tweets. Bot sentinel is a nonpartisan platform that uses machine learning to classify Twitter accounts, analyzing them on disinformation and targeted harassment. Of the active accounts that we collected tweets from, a very small percentage actually had disruptive bot sentinel score.

## Outside Impacts
* Twitter
  1. Deleted fake accounts
  2. Labeled Tweets as potentially fake or misleading and had banners over them
  3. Added more context to trending Tweets 
* Government
  1. FBI, DNI, DHS
  2. Protect Your Voice campaign to spread information to U.S. citizens
  3. Protecting Americans from foreign influence


## Conclusion
By analysing research of social media’s impact during the 2016 presidential election, gathering data from the most recent election, and taking into account the actions of Twitter and government agencies, we found Twitter had a negligible effect on the outcome of the 2020 presidential election.

### Authors:
- Genadi Shamugia
- Ryan Serrato
- Ezrah Itkowsky
- Jackson Stallone



