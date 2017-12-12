from time import time, sleep
from re import findall
#time is stored in seconds
# t0 = time()
# hashtag_total = [['shit', 3, t0]]
# tweet = "dit is een test #shit #test"
# sentiment = .8
tweets = open("test_file.txt").readlines()

sentiments = 1


def sorting(tweet, sentiment):
    hashtag_total = [[0, 0, 0]]
    for z in range(len(tweet)):
        #print("first Loop")
        all_tags = findall(r"#(\w+)", tweet[z])
        for j in range(len(all_tags)):
            #print("second Loop")
            found = False
            for i in range(len(hashtag_total)):
                #print("third Loop")
                if all_tags[j] == hashtag_total[i][0]:
                    found = True
                    if time() - hashtag_total[i][2] >= 1000:#adjust this value to the max time that should be between the occurence of a hashtag
                        hashtag_total[i][1] = 1
                        hashtag_total[0][2] = time()
                    else:
                        hashtag_total[i][1] += 1
                        hashtag_total[0][2] = time()
                        #print("added to total")
                    if hashtag_total[i][1] >= 5:     #adjust this value to the minimum number of occurences
                        output = open(hashtag_total[i][0][0] + ".txt", "a")
                        output.write(tweet[z])
                        output.write(" ")
                        output.write(str(sentiment))
                        output.write("\n")
                        output.close()
                        #print("appended to txt")
            if not found:
                hashtag_total.append([all_tags[j], 1, time()])
                #print("appended to list")
    return hashtag_total

print(tweets[2])
# print(hashtag_total)
hold = sorting(tweets, sentiments)
#print(hold)
