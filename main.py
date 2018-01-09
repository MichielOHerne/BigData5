from sort_for_graphing import open_json, open_json_for_hashtag
from importingtwitterdata_new import import_data
from plot_bar import plot_bar
from plot_line import plot_line
from plot_pie import plot_pie
from plot_world import plot_world
all_hashtags = []


def sort_hash(data, col):
    new_data = []
    new_data.extend(sorted(data[0:], key=lambda data: -data[col]))
    return new_data


data = import_data()
all_hashtags = open_json_for_hashtag("twitterdata.json", all_hashtags)
print(all_hashtags)
sorted_all_hashtags = sort_hash(all_hashtags, 1)
print(sorted_all_hashtags)

sent_tweets = open_json("twitterdata.json", [sorted_all_hashtags[0][0]])
plot_line(sent_tweets)
plot_bar(sent_tweets)
plot_pie(sent_tweets)
plot_world(sent_tweets)


# for i in range(len(sorted_all_hashtags)):
#     if all_hashtags[i][1] >= 20:
#         sent_tweets = open_json("twitterdata.json", [sorted_all_hashtags[i][0]])
#         plot_line(sent_tweets)
#         plot_bar(sent_tweets)
#         plot_pie(sent_tweets)
#         plot_world(sent_tweets)
