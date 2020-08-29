#fw=open('q3atextfile.txt','w+')
import tweepy
consumer_key = "deU56q5KBq6zogXd4W9U88LD6"
consumer_secret = "1X0o2gbMcZ6jYuVL0ns1gsGGlRvlDLmq0p1xmzZCsEPjZ3jg54"
access_token = "2894833632-CKKOP0j1odN2NfBUOgmuUSWNyTBlqivSBT0brjI"
access_token_secret = "rjbh9cRC1TuRkHUQdIwdnXcqizbvhfqUjofU5T4oncqKb"
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)
# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
x=input('Enter Keyword\n')
#public_tweets = api.home_timeline()
tweets=api.search(q=x,count=500)
# foreach through all tweets pulled
for tweet in tweets:
   # printing the text stored inside the tweet object
     print (tweet.text)
     #fw.write(tweet.text)


