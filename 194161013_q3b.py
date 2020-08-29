import tweepy
consumer_key = "deU56q5KBq6zogXd4W9U88LD6"
consumer_secret = "1X0o2gbMcZ6jYuVL0ns1gsGGlRvlDLmq0p1xmzZCsEPjZ3jg54"
access_token = "2894833632-CKKOP0j1odN2NfBUOgmuUSWNyTBlqivSBT0brjI"
access_token_secret = "rjbh9cRC1TuRkHUQdIwdnXcqizbvhfqUjofU5T4oncqKb"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
import math
##    MID-POINT CALCULATION
def midpoint(x1, y1, x2, y2):
#Input values as degrees

#Convert to radians
    lat1 = math.radians(x1)
    lon1 = math.radians(x2)
    lat2 = math.radians(y1)
    lon2 = math.radians(y2)


    bx = math.cos(lat2) * math.cos(lon2 - lon1)
    by = math.cos(lat2) * math.sin(lon2 - lon1)
    lat3 = math.atan2(math.sin(lat1) + math.sin(lat2), \
           math.sqrt((math.cos(lat1) + bx) * (math.cos(lat1) \
           + bx) + by**2))
    lon3 = lon1 + math.atan2(by, math.cos(lat1) + bx)

    return [round(math.degrees(lat3), 2), round(math.degrees(lon3), 2)]
print("\n Enter Coordinates\n")
lat1=input("Enter latitude of 1st coordinate\n")
lat1=float(lat1)
long1=input("Enter longitudeof 1st coordinate\n")
long1=float(long1)
lat2=input("Enter latitude of 2nd coordinate\n")
lat2=float(lat2)
long2=input("Enter longitude of 2nd coordinate\n")
long2=float(long2)

##   RADIUS CALCULATION
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

lat1 = radians(lat1)
lon1 = radians(long1)
lat2 = radians(lat2)
lon2 = radians(long2)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c
radius=str(distance)+'km'
#print("Result:", distance)

#print("Should be:", 278.546, "km")

list=[]
x=midpoint(lat1,long1,lat2,long2)

list=x
#print(list)
# print(list[0])
# print(list[1])

for i in api.search(rpp=10,count=100000,geocode=f"{list[0]},{list[1]},{radius}"):
    print (i.text)

