from time import time, sleep
from re import findall
from operations import clear_dump
from nltk import sentiment
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import shutil
import os
#time is stored in seconds
# t0 = time()
# hashtag_total = [['shit', 3, t0]]
# tweet = "dit is een test #shit #test"
# sentiment = .8
# tweets = open("test_file.txt").readlines()
#
# sentiments = 1
# clear_dump("dump/")


def sorting(tweet, hashtag_total):
    for z in range(len(tweet)):
        sentiment = ""
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(tweet[z])
        for k in sorted(ss):
            sentiment = sentiment + '{0}: {1}, '.format(k, ss[k])
        #print("first Loop")
        all_tags = findall(r"#(\w+)", tweet[z])
        for j in range(len(all_tags)):
            #print("second Loop")
            found = False
            for i in range(len(hashtag_total)):
                #print("third Loop")
                if all_tags[j] == hashtag_total[i][0]:
                    found = True
                    if time() - hashtag_total[i][2] >= 30:#adjust this value to the max time that should be between the occurence of a hashtag
                        try:
                            t = str(time())
                            output = open("dump/" + all_tags[j] + "_" + t + ".txt", "w")
                            # output.write("dump/" + all_tags[j] + ".txt")
                            output.close()
                            shutil.copy("dump/" + all_tags[j] + ".txt", "dump/" + all_tags[j] + "_" + t + ".txt")
                            os.remove("dump/" + all_tags[j] + ".txt")
                            #output = open("dump/" + all_tags[j] + ".txt", "w")
                            output.close()
                            print("emptied file")
                        except:
                            pass
                        hashtag_total[i][1] = 1
                        hashtag_total[0][2] = time()
                        # open("dump/" + all_tags[j] + ".txt", "w").close()
                        # os.rename("dump/" + all_tags[j] + ".txt", "dump/" + all_tags[j] + "_" + str(time()) + ".txt")
                    else:
                        hashtag_total[i][1] += 1
                        hashtag_total[0][2] = time()
                        #print("added to total")
                    if hashtag_total[i][1] >= 5:     #adjust this value to the minimum number of occurences
                        output = open("dump/" + all_tags[j] + ".txt", "a")
                        output.write(tweet[z])
                        output.write(" ")
                        output.write(str(sentiment))
                        output.write("\n")
                        output.close()
                        #print("appended to txt")
                    break
            if not found:
                #print([all_tags[j], 1, time()])
                hashtag_total.append([all_tags[j], 1, time()])
                #print("appended to list")
    return hashtag_total

# print(tweets[2])
# # print(hashtag_total)
# hold = sorting(tweets)
# #print(hold)
