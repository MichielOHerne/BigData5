from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

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
search_var = "#metoo"
search_var2 = "meow"
search_var3 = "house"
search_var4 = "obama"
search_var5 = "women"

## Tweet Streaming and writing to file
class listener(StreamListener):

	def on_data(self, data):
		all_data = json.loads(data)
		
		tweet = all_data["text"]
		
## in tweet stream analyser if loop, ## to get all tweets
#		sentiment_value, confidence = s.sentiment(tweet)
#		if confidence*100 >= 80:
#			output = open("tweets_sentiment-out.txt", "a")
#			output.write(sentiment_value)
#			output.write('\n')
#			output.close()
	
## normal tweet writing metho
		output = open("tweets-out-" + str(search_var+"-"+search_var2+"-"+search_var3+"-"+search_var4+"-"+search_var5) + ".txt", "a")	
		output.write(str(tweet))
		output.write('\n')
## extra \n for clarity for tweets containing \n
		output.write('\n')
		output.close()
	
		print((tweet))
		return True


	def on_error(self, status):
		print(status)

## Setting api keys to acces tweet stream
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=[search_var, search_var2])










