# Overview
I've always had a general fascination with bots on social media. I think it's interesting what they're capable of doing and spreading for good and bad, and since the beginning of my programming career, I've wondered how they work. After a bit of haggling, here's what I came up with.

This bot is a generic twitter bot that twice per day, every twelve hours, will tweet a random quote from the popular 2022 video game, Elden Ring. It seemed like a fitting first attempt at a bot, as video games are largely what inspired me to program in the first place.

For a more detailed explanation and overview, you can find a video here of me explaining it.

[Software Demo Video](https://youtu.be/UF_WADgJJo0)

# Development Environment

To write this program, I used a decent variety of libraries and packages that are available for Python. The one that is doing the lion's share of the work is the Python package, Tweepy. This package, once connected with the OAuth and the Twitter API V2, has all the necessary tools for creating a bot, from messaging to likes and retweets. Other packages include Numpy for the randomizer and dotenv for keeping the authorization keys and secrets private needed to access the Twitter API.

For hosting, I set up a Cron Job through the hosting service, Render. To set this up, I connected Render to my Github repository and then set up the environment variables. After figuring that out and setting up the schedule, it was pretty straightforward from there, and as of January 24th, 2023, you can find this bot on Twitter at @dailyEldenRing. 

# Useful Websites

I ran into quite a few roadblocks to work through when writing this, and so I feel it's worth mentioning the ones that helped out most.

First, massive shoutout to Learn With Jabe on Youtube, his videos on How to Build a Twitter Bot were incredibly useful. I discovered them when I was trying to host on render and they were a lifesaver. 

- [Learn With Jabe](https://www.youtube.com/@learnwithjabe9791)

In addition, the developer platform for Twitter was incredibly useful and had a large variety of useful examples. 
- [Twitter Developer Platform](https://developer.twitter.com/en)

Last, a massive thank you to the Elden Ring Wiki for having the massive collection of Elden Ring content that made this all possible.

- [Elden Ring Wiki](https://eldenring.wiki.fextralife.com/Elden+Ring+Wiki)

# Future Work

In the future, there are plenty of things I want to implement.

First, I want to implement a larger library of quotes. Currently, the one I have is small and will run out of quotes pretty quick, so that's the first step. 

Second, I want to add more functionality for the bot, including liking and retweeting tweets responding to others that @ the bot, and maybe even include pictures into the tweets.

Last, I will be doing some house keeping to get the code a little prettier and capable of expanding.

Keep an eye out for updates in the future, and follow me @dailyEldenRing on Twitter!

- Isaac Radford