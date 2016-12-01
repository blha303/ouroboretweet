#!/usr/bin/env python3
import tweepy
import json
import sys

with open(".twitter_config.json") as f:
    config = json.load(f)

auth = tweepy.OAuthHandler(config["ckey"], config["csec"])
auth.set_access_token(config["utok"], config["usec"])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    with open("lasttweet") as f:
        lasttweet = f.read().strip()
except OSError:
    lasttweet = api.user_timeline("ouroboretweet", count=1)[0].retweeted_status.id

timeline = api.list_timeline("ouroboretweet", "ouroboretweet", since_id=lasttweet)
if not timeline:
    print("Nothing to do")
    sys.exit(0)
for tweet in timeline:
    if not tweet.retweeted:
        _ = api.retweet(tweet.id)
    lasttweet = tweet.id
with open("lasttweet", "w") as f:
    f.write(str(lasttweet))
