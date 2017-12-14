from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from operations import clean_str
from sorting import sorting
from operations import clear_dump
import json

clear_dump("dump/")
## optional in tweet stream analyser (needs files run from nltk)
#import sentiment_mod as s

## twitter keys
## IMPORTANT: kijk uit met hiermee aankutten, als er te vaak wordt geconnect met deze keys blocked twitter mń account
ckey = "DuzXWGxPd69VLoupzuMKKD9zT"
csecret = "mJfdpWml56fuP8WWTzj0UqqjIruJEhp28tx9Qy8wKIioe3Rum2"
atoken = "935421440282816512-oLfnr0Cq1GVWbDA4xeSPqow3MjgZrms"
asecret = "J9tznxnFd8Om0hcw7QID7ol9mLmev76YJLlCsdnqD2829"

## Search_var is the str on which the stream gets filtered
## It also appends the filtered upon words to the data file to which the tweets are outputted
## more filter words can be added, however they need to be added in the output aswell
search_var = "snow"
search_var2 = "meow"
search_var3 = "house"
search_var4 = "obama"
search_var5 = "women"


class Listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        try:
            tweet = [clean_str(all_data["text"], False)]
            sorting(tweet, hashtag_total)
        except:
            pass
        return True

    def on_error(self, status):
        print(status)



## Setting api keys to acces tweet stream
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
hashtag_total = [['0', 0, 0]]

twitterStream = Stream(auth, Listener())
twitterStream.filter(languages=["en"], track=["I"])











