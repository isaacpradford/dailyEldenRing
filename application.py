import tweepy
import json
import random
import numpy as np
from array import *
import os
from dotenv import load_dotenv
import logging

# https://auth0.com/blog/how-to-make-a-twitter-bot-in-python-using-tweepy/

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

characterNames = ["Ranni", "Melina"]
quotes = []

usedQuotes = []

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
    

def main():
    quote = getQuote()
    tweetQuote(client, quote)
    
def getQuote():
    f = open('dailyEldenRing/quotes.json')
    data = json.load(f)
    
    randCharacter = np.random.choice(characterNames)

    for i in data["characters"][randCharacter]["quotes"]:
        quotes.append(i)
        
    qotd = np.random.choice(quotes)
    
    
    return qotd
    
def tweetQuote(client, quote):
    client.create_tweet(text = f"{quote}")
    
    

main()

