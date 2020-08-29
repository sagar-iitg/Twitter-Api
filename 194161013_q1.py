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
x=input('enter user id\n')
user=api.get_user(x)
print('Attribute'.ljust(20),'Value','\n')  # printing statement of attribute and value
print('Twitter User ID'.ljust(20),user.id)
print('Screen Name'.ljust(20),user.screen_name)
print('User Name'.ljust(20),user.name)
print('User Location'.ljust(20),user.location)
print('User Description'.ljust(20),user.description)
print('Total Followers'.ljust(20),user.followers_count)
print('Total Statuses'.ljust(20),user.statuses_count)
print('User URL'.ljust(20),user.url)
