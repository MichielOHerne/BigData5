from time import time, sleep
from re import findall
from operations import clear_dump
from nltk import sentiment
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import shutil
import os


def count_hashtags(tweet, hashtag_total):
    for z in range(len(tweet)):
        all_tags = findall(r"#(\w+)", tweet[z])
        for j in range(len(all_tags)):
            found = False
            for i in range(len(hashtag_total)):
                if all_tags[j] == hashtag_total[i][0]:
                    found = True
                    hashtag_total[i][1] += 1
                    break
            if not found:
                hashtag_total.append([all_tags[j], 1])
    return hashtag_total
