import tweepy
from textblob import TextBlob
import csv

a = []


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("ENTER HASHTAG:")
hashtag = input()
htag = '#' + hashtag
fname = hashtag + '.csv'
print(htag, fname)
# Open/Create a file to append data
csvFile = open(fname, 'w', newline='')
# Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q=htag, count=200, lang="en", since="2020-02-02",
                           ).items():
    analysis = TextBlob(tweet.text)
    print(tweet.created_at, tweet.text)

    csvWriter.writerow([tweet.created_at, tweet.text.encode('ascii', 'ignore'), 1])
csvFile.close()

#geocode="19.1136,72.8697,20km
