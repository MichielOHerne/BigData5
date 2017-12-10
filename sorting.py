from time import time, sleep
from re import findall
#time is stored in seconds
t0 = time()
hashtag_total = [[['shit'], 5, t0]]
tweet = "dit is een test #shit"
sentiment = .8
sleep(3)
print(hashtag_total[0][2])

for i in range(len(hashtag_total)):
    if findall(r"#(\w+)", tweet) == hashtag_total[i][0]:
        if time() - hashtag_total[i][2] >= 1:           #adjust this value to the max time
            hashtag_total[i][1] = 1
            hashtag_total[0][2] = time()
        else:
            hashtag_total[i][1] += 1
            hashtag_total[0][2] = time()
        if hashtag_total[i][1] >= 5:
            output = open(hashtag_total[i][0][0] + ".txt", "a")
            output.write(tweet)
            output.write(" ")
            output.write(str(sentiment))
            output.write("\n")
            output.close()
    else:
        hashtag_total.append([[findall(r"#(\w+)", tweet), 1, time()]])
print(hashtag_total)
