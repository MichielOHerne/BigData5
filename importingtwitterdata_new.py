from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from operations import clean_str
from sorting import sorting
from operations import clear_dump
import json
from time import time
import atexit
import cProfile

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
f = open('twitterdata.json', 'w')
# f.write('[')
# f.close()


first = True
json_data = []
t0 = time()
max_time = 0


class Listener(StreamListener):
    def on_data(self, data):
        global t0
        all_data = json.loads(data)
        json_data.append(all_data)
        try:
            tweet = [clean_str(all_data["text"], False)]
            time_stamp = all_data["created_at"]
            sorting(tweet, hashtag_total, time_stamp)
        except:
            pass
        # change this       \/ to change runtime
        if time() - t0 >= max_time:
            t0 = time()
            # stop_running(input("do you want more data?[No]"), json_data)
            stop_running("No", json_data)
        return True, json_data

    def on_error(self, status):
        print(status)


def exit_handler(json_data):
    print("ended program")
    json.dump(json_data, "twitterdata.json")
    print("created json file")


run = True

## Setting api keys to acces tweet stream
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
hashtag_total = [['0', 0, 0]]
#
# twitterStream = Stream(auth, Listener())
# json_data = twitterStream.filter(languages=["en"], track=["a", "the", "I", "you"])
# atexit.register(exit_handler(json_data))
# f = open('twitterdata.json', 'w')
# f.write(']')
# f.close()


def stop_running(key, json_data):
    if key == 'No':
        # print(json_data)
        with open('twitterdata.json', 'w') as outfile:
            json.dump(json_data, outfile)
        print("done")
        exit()
    else:
        pass


def import_data():
    try:
        while run:
            t0 = time()
            print("stream is running")
            twitterStream = Stream(auth, Listener())
            json_data = twitterStream.filter(languages=["en"], track=["a", "the", "I", "you"])
    # except KeyboardInterrupt:
    #     with open('twitterdatatest.json', 'w') as outfile:
    #         json.dump(json_data, outfile)
    #     print("done")
    except:
        pass
    return


def set_max_time(set_time):
    global max_time
    max_time = set_time
    return max_time
