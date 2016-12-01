#!/usr/bin/env python3
import tweepy
import json

with open(".twitter_config.json") as f:
    config = json.load(f)

auth = tweepy.OAuthHandler(config["ckey"], config["csec"])
auth.set_access_token(config["utok"], config["usec"])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    with open("lasttweet") as f:
        lasttweet = f.read().strip()
except OSError:
    lasttweet = None
for tweet in api.list_timeline("ouroboretweet", "ouroboretweet", since_id=lasttweet):
    _ = api.retweet(tweet.id)
    lasttweet = tweet.id
with open("lasttweet", "w") as f:
    f.write(lasttweet)
