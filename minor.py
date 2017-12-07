## random streaming zooi



hashtag_total = {"shit": 5}
tweet = "dit is een test #shit"
sentiment = .8
for key in hashtag_total:
    if hashtag_total[key] >= 5:
        output = open(str(key % hashtag_total)+".txt", "a")
        output.write(tweet)
        output.write(" ")
        output.write(str(sentiment))
        output.write("\n")
        output.close()
