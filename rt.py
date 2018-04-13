import tweepy
from random import randint
from time import sleep
from tweepy.auth import OAuthHandler
sleep(randint(60,200))

contador = 1

# Create variables for each key, secret, token
consumer_key = '.........................'
consumer_secret = '.............................................'
access_token = '............-......................................'
access_token_secret = '..........................................'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline, screen_name='@nombretuitero').items(30):


        texto = (status._json['text']).lower().strip()

        if (contador <= 10 ):

                if (texto[0]=="@") and (len(texto) < 40 ):

                        continue

                api.retweet(status.id)
                sleep(randint(0,60))
                print (status.id,contador)
                contador += 1


for status in tweepy.Cursor(api.user_timeline, screen_name='@nombretuitero2').items(10):


        texto = (status._json['text']).lower().strip()

        if (contador <= 2 ):

                if (texto[0]=="@"):

                        continue

                api.retweet(status.id)
                sleep(randint(0,60))
                print (status.id,contador)
                contador += 1

for status in tweepy.Cursor(api.user_timeline, screen_name='@nombretuitero3').items(10):


        texto = (status._json['text']).lower().strip()

        if (contador <= 4 ):

                if (texto[0]=="@") and (len(texto) < 40 ):

                        continue

                api.retweet(status.id)
                sleep(randint(0,60))
                print (status.id,contador)
                contador += 1

