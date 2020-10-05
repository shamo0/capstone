from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#APIKEY=NBNgPGCBeGv80PcsYU3QWU94d
#APIKEYSECRET = lvAaoSInlF9mPonoMMldFq5ZE96oAAl30TLh6ynVwK2tauvOQC
#BearerTOken = AAAAAAAAAAAAAAAAAAAAAAZPIQEAAAAAiHQ21xYSjxqhKSHWSPXUDiTRzhM%3DDMUucbFBHGSbyjl0nHF8V4lWyoOLyfmBHBwKrvm4TmJtTVjor6

#consumer key, consumer secret, access token, access secret.
ckey="NBNgPGCBeGv80PcsYU3QWU94d"
csecret="lvAaoSInlF9mPonoMMldFq5ZE96oAAl30TLh6ynVwK2tauvOQC"
atoken="1311728151265832961-AaFHXfZtozEgfoVZoFnNqzqRZEWQAr"
asecret="Az8Ezlg77NtkZ8coTqXGsXW2wVh7Wbpm3JTsAkoPsrq7z"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]

        print(tweet)

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
