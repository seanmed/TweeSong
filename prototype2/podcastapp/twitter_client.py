#!/usr/bin/env python
# coding: utf-8

import tweepy

import time


from social_core.pipeline import user

consumer_key = "Yx2jYekdVXdpc3ZoPAxwJIBoB"
consumer_secret = "BO74ZhTkQQlpwxkN8bNsKTN6FW5jNC1gAsId0lZLvf9KnmU5i4"
twitter_auth_keys = {
    "consumer_key": "Yx2jYekdVXdpc3ZoPAxwJIBoB",
    "consumer_secret": "BO74ZhTkQQlpwxkN8bNsKTN6FW5jNC1gAsId0lZLvf9KnmU5i4",
    "access_token": "1327194254712524802-yVjoPP9xNy3oEOJzLjaO3NQTHv1gro",
    "access_token_secret": "7uqfMuSbyK6GsgG7QOF7qPqO1CQ8zxaYM0M000367DTSK"
}

auth = tweepy.OAuthHandler(
    twitter_auth_keys['consumer_key'],
    twitter_auth_keys['consumer_secret']
)
auth.set_access_token(
    twitter_auth_keys['access_token'],
    twitter_auth_keys['access_token_secret']
)
api = tweepy.API(auth)

me = api.me()

verified_friends = []
my_friends = me.friends()
for friend in my_friends:
    if friend.followers_count > 100000:
        x= friend.screen_name
        verified_friends.append(friend.screen_name)







