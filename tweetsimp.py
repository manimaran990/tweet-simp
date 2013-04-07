#!/usr/bin/python
import tweepy
key='Zfwb3WjKK25oH6ev6tJXQ'
sec='9J3bvABErKfAT0ydFKqCG8HJkr0tXVEMBDdUeZAPI'
tok='115284276-iTwYeh0s40d2Z5NXgf6Gmt40ZZv4j0bNcTayd9Hy'
tsec='jlrc7kijc2DY6hdO2WCyVenqy37zdIeHJFgjkG78Y'
auth=tweepy.OAuthHandler(key,sec)
auth.set_access_token(tok,tsec)
api=tweepy.API(auth)
msg=api.home_timeline()
for tweet in msg:
	print tweet.text
