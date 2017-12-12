from time import time, sleep
from re import findall
#time is stored in seconds
t0 = time()
hashtag_total = [['shit', 3, t0]]
tweet = "dit is een test #shit #test"
sentiment = .8

def sorting(hashtag_total, tweet, sentiment):
    all_tags = findall(r"#(\w+)", tweet)
    for i in range(len(hashtag_total)):
        for j in range(len(all_tags)):
            if all_tags[j] == hashtag_total[i][0]:
                if time() - hashtag_total[i][2] >= 1:#adjust this value to the max time that should be between the occurence of a hashtag
                    hashtag_total[i][1] = 1
                    hashtag_total[0][2] = time()
                else:
                    hashtag_total[i][1] += 1
                    hashtag_total[0][2] = time()
                if hashtag_total[i][1] >= 5:     #adjust this value to the minimum number of occurences
                    output = open(hashtag_total[i][0][0] + ".txt", "a")
                    output.write(tweet)
                    output.write(" ")
                    output.write(str(sentiment))
                    output.write("\n")
                    output.close()
            else:
                hashtag_total.append([[all_tags[j], 1, time()]])
print(hashtag_total)
