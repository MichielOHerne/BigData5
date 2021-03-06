from operations import clean_str
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from time import strptime
from re import findall
import calendar
from hashtag_list import count_hashtags

def sort_into_list(tweet, hashtag_total, time_tweet, country):
    for z in range(len(tweet)):
        tweet_sent = []
        my_regex = r"" + hashtag_total[0]
        tag = findall(my_regex, tweet[z])
        try:
            if tag[0] == hashtag_total[0]:
                tweet_sent.append(tweet[z])
                sentiment = []
                sid = SentimentIntensityAnalyzer()
                ss = sid.polarity_scores(tweet[z])
                for k in sorted(ss):
                    sentiment.append(ss[k])
                tweet_sent.append(sentiment)
                split_date = time_tweet.split(" ")
                string_date = split_date[1] + " " + split_date[2] + ", " + split_date[5] + ", " + split_date[3]
                strptime_object = strptime(string_date, "%b %d, %Y, %H:%M:%S")
                timestamp = calendar.timegm(strptime_object)
                tweet_sent.append(timestamp)
                tweet_sent.append(country)
                hashtag_total.append(tweet_sent)
        except:
            pass

        return hashtag_total


def open_json(data, hashtag):
    with open(data) as data_file:
        hold = json.load(data_file)
        for i in range(len(hold)):
            try:
                tweet = [clean_str(hold[i]["text"], False)]
                time_tweet = hold[i]["created_at"]
                try:
                    country = hold[i]["place"]["country"]
                except:
                    country = "Unknown"
                sort_into_list(tweet, hashtag, time_tweet, country)
            except:
                pass
    return hashtag

def open_json_for_hashtag(data):
    hashtag = []
    with open(data) as data_file:
        hold = json.load(data_file)
        for i in range(len(hold)):
            try:
                tweet = [clean_str(hold[i]["text"], False)]
                count_hashtags(tweet, hashtag)
            except:
                pass
    return hashtag
