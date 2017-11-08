#  python3 .... publica la cita del dia de wikiquote via Twitter con un retraso aleatorio
#  0 7 * * * /usr/bin/python3 /root/wikicita.py

import wikiquote, random
import tweepy , re
from random import randint
from time import sleep

sleep(randint(60,12000))

tuit = '. '.join(wikiquote.quote_of_the_day(lang='es'))

#tuit = re.sub('', '', tuit)



# Create variables for each key, secret, token
consumer_key = 'iAtYJ4HpUVfIUoNnif'
consumer_secret = '172fOpzuZoYzNYaU3mMYvE8m8MEyLbztOd'
access_token = '1316534712-43JUBQjo77cVRYb22z448KtXJQLKDiFTS'
access_token_secret = '980sQSFFSvlMuHPLBR6dhobTdKO8DYnCVthKyJs'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
print (tuit)
api.update_status(status=tuit)
