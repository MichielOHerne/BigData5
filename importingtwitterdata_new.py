from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from operations import clean_str
from operations import clear_dump
import json
from time import time

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
        if time() - t0 >= max_time:
            t0 = time()
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


def stop_running(key, json_data):
    if key == 'No':
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
            list_of_words = ['the', 'i', 'to', 'a', 'and', 'is', 'in', 'it', 'you', 'of', 'tinyurl.com', 'for', 'on',\
                            'my', 'â€˜s', 'that', 'at', 'with', 'me', 'do', 'have', 'just', 'this', 'be', 'nâ€™t', 'so',\
                             'are', 'â€˜m', 'not', 'was', 'but', 'out', 'up', 'what', 'now', 'new', 'from', 'your', 'like',\
                             'good', 'no', 'get', 'all', 'about', 'we', 'if', 'time', 'as', 'day', 'will', 'one', 'twitter',\
                             'how', 'can', 'some', 'an', 'am', 'by', 'going', 'they', 'go', 'or', 'has', 'rt', 'know', 'today', \
                             'there', 'love', 'more', 'work', '=', 'too', 'got', 'he', '2', 'back', 'think', 'did', 'lol', 'when',\
                             'see', 'really', 'had', 'great', 'off', 'would', 'need', 'here', 'thanks', 'been', 'blog', 'still',\
                             'people', 'who', 'night', 'â€˜ll', 'want', 'why', 'bit.ly', 'home', 'â€˜re', 'should', 'well', '3',\
                             'oh', 'much', 'u', 'â€˜ve', 'then', 'right', 'make', 'last', 'over', 'way', 'canâ€™t', 'does', 'getting',\
                             'watching', '1', 'its', 'only', 'her', 'post', 'his', 'morning', 'very', 'she', 'them', 'could', 'first',\
                             'than', 'better', 'after', 'tonight', 'our', 'again', 'down', 'twitpic.com', 'news', 'man', '4', 'im',\
                             'looking', 'us', 'tomorrow', 'best', 'into', 'any', 'hope', 'week', 'nice', 'show', 'yes', 'where',\
                             'take', 'check', 'come', '10', 'trying', 'fun', 'say', 'working', 'next', 'happy', 'were', 'even',\
                             'live', 'watch', 'feel', 'thing', 'life', 'little', 'never', 'something', 'bad', 'free', 'doing', \
                             'world', 'ff.im', '5', 'video', 'sure', 'yeah', 'bed', 'let', 'use', 'their', 'look', 'being', 'long',\
                             'done', 'sleep', 'before', 'year', 'find', 'awesome', 'big', 'un', '+', 'things', 'ok', 'another', 'â€˜d',\
                             'him', 'cool', 'old', 'ever', 'help', 'anyone', 'made', 'ready', 'days', 'die', 'other', 'read', 'because',\
                             'two', 'playing', 'though', 'is.gd', 'house', 'always', 'also', 'listening', 'maybe', 'please', 'wow', 'haha',\
                             'having', 'thank', 'pretty', 'game', 'someone', 'school', 'those', 'snow', 'twurl.nl', 'gonna', 'hey', '7',\
                             'many', 'start', 'wait', 'while', 'google', 'finally', 'everyone', 'para', 'try', '30', 'god', 'weekend',\
                             'most', 'iphone', 'stuff', 'around', 'music', 'looks', 'may', 'thought', 'keep', 'yet', 'reading', 'must',\
                             'which', 'same', 'real', 'follow', 'bit', 'hours', 'might', 'actually', 'online', 'job', 'friends', 'said',\
                             'obama', 'coffee', 'hate', 'hard', 'soon', 'tweet', 'por', 'making', 'wish', 'call', 'movie', 'tell', 'thinking',\
                             'via', 'site', '20', 'facebook', 'few', 'found', 'these', 'tv', 'sorry', 'through', 'already', '12', 'lot',\
                             '6', 'makes', 'give', 'put', 'waiting', 'stop', 'play', 'says', 'away', 'coming', 'early', 'dinner', 'phone',\
                             '8', 'cold', 'using', 'times', 'book', 'kids', 'went', 'nothing', 'every', 'years', 'top', 'office', '11', \
                             'friend', 'talk', 'feeling', 'hour', 'head', 'web', 'food', 'amazing', 'car', 'lost', '09', 'end', 'girl', \
                             'since', 'guess', 'lunch', 'hot', 'sounds', 'b', 'funny', 'idea', 'glad', 'saw', 'hear', 'mean', 'name',\
                             'damn', 'myself', 'guy', 'song', 'yay', 'least', 'business', 'run', 'place', 'friday', 'buy', 'enough', \
                             'anything', 'late', 'photo', 'party', 'link', 'interesting', 'used', 'shit', 'tired', '15', 'internet',\
                             'following', 'left', 'guys', 'money', 'far', 'own', 'seems', 'media', 'baby', 'class', 'x', 'social', 'seen',\
                             'miss', 'forward', 'part', 'until', 'open', 'win', 'hi', 'almost', 'dont', 'n']
            json_data = twitterStream.filter(languages=["en"], track=list_of_words)
    except:
        pass
    return


def set_t0():
    global t0
    t0 = time()
    return t0


def set_max_time(set_time):
    global max_time
    max_time = set_time
    return max_time
