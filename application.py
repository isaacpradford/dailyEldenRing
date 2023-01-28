# Importing packages
import tweepy
import json
import numpy as np
import os
from dotenv import load_dotenv


# Keys and tokens necessary to gain access to tweet remotely. All of the environment variables are stored securely elsewhere and accessed through the load_dotenv() file.
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
  
  
 
 
# Numpy is incapable of doing the np.random.choice function for 2D arrays,
# so to get around that, the JSON is loaded in, the program picks a random name from characterNames, 
# copies all of those quotes from the 2D array into the quotes array, 
# and then the quote of the day (qotd) is selected from the new array of quotes.
  
# Array of character names inside JSON
characterNames = ["Ranni", "Melina","IronFistAlexander", "AeonianSpirit","AlbinauricVillageSpirit","AeonianSwampSpirit","AshenSpirit",
                  "BlackguardBigBoggart", "Blaidd"]

# Array that the quotes for the character of the day is put into
quotes = []


def main():
    quote = getQuote()
    tweetQuote(client, quote)
    
def getQuote():
    f = open('./quotes.json')
    data = json.load(f)
    
    randCharacter = np.random.choice(characterNames)

    for i in data["characters"][randCharacter]["quotes"]:
        quotes.append(i)
        
    qotd = np.random.choice(quotes)
    
    return qotd
    
def tweetQuote(client, quote):
    client.create_tweet(text = f"{quote}")
    

main()


