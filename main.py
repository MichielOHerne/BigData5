from sort_for_graphing import open_json, open_json_for_hashtag
from importingtwitterdata_new import import_data, set_max_time, set_t0
all_hashtags = []


def sort_hash(data, col):
    new_data = []
    new_data.extend(sorted(data[0:], key=lambda data: -data[col]))
    return new_data


def import_time(time):
    max_time = set_max_time(time)
    t0 = set_t0()
    data = import_data()


def sort_hashtags(json):
    sorted_all_hashtags = []
    all_hashtags = []
    all_hashtags = open_json_for_hashtag(json)
    sorted_all_hashtags = sort_hash(all_hashtags, 1)
    return sorted_all_hashtags


def filter_hashtags(selected_hashtag):
    sent_tweets = []
    sent_tweets = open_json("twitterdata.json", selected_hashtag)
    return sent_tweets
