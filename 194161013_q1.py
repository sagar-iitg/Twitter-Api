import tweepy
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
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
