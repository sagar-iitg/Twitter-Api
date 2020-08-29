import tweepy
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.wait_on_rate_limit = True
api.wait_on_rate_limit_notify = True

inp=input('Enter comma seperated user id\n')
input_users=inp.split(',')

for x in input_users:
    follower_list=api.followers_ids(x)
    #print(follower_list)  user id in number format
    #print(len(follower_list))
    #Followerlist
    follower=[]
    print("THE FOLLOWER LIST OF ",x,'\n')
    for j in range(0,len(follower_list)):
        z=follower_list[j]
        user=api.get_user(id=z)
        follower.append(user.screen_name)
        print(user.screen_name)
    #print(follower)

    following_list=api.friends_ids(id=x)
    #print(following_list)
    #print(len(following_list))

    following=[]
    #print("THE FOLLOWING LIST OF ",x,'\n')
    for i in range(0,len(follower_list)):
        y=following_list[i]
        u=api.get_user(y)
        following.append(u.screen_name)
        #print(u.screen_name)

    def intersection(follower_list, following_list):
        return list(set(follower_list) & set(following_list))


    common_part=intersection(follower_list, following_list)
    #print(common_part)
    friend=[]
    print('\nTHE FRIEND LIST OF ',x,'\n')
    for k in range(0,len(common_part)):
        p=common_part[k]
        us=api.get_user(p)
        friend.append(us.screen_name)
        print(us.screen_name)


