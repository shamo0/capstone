#!/bin/bash
tiktok-scraper hashtag BIDEN -t json -f biden -n 0
tiktok-scraper hashtag CONSERVATIVE -t json -f conservative -n 0
tiktok-scraper hashtag DEMOCRAT -t json -f democrat -n 0
tiktok-scraper hashtag ELECTION -t json -f election -n 0
tiktok-scraper hashtag LIBERAL -t json -f liberal -n 0
tiktok-scraper hashtag REPUBLICAN -t json -f republican -n 0
tiktok-scraper hashtag TRUMP -t json -f trump -n 0
rm -f accountsOfInterest.txt
./scraper.py
