# Python3 . Busca los ultimos tuits de un usuario y los retuitea a intervalos aleatorios.

import wikiquote, random
import tweepy , re
from random import randint
from time import sleep

sleep(randint(60,12000))

# Create variables for each key, secret, token
consumer_key = 'iAtYJ4HpUVfIUoNnif1DA'
consumer_secret = '172fOpzuZoYzNYaU3mMYvE8m8MEyLbztOdbrUolU'
access_token = '1316534712-43JUBQjo77cVRYb22z448KtXJQLKDiFTS'
access_token_secret = '980sQSFFSvlMuHPLBR6dhobTdKO8DYnCVthKyJs'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline, screen_name='@nombre_usuario').items(3):

	print (status.id)   
	print (status._json['text'])  
	api.retweet(status.id)
	sleep(randint(30,600))
