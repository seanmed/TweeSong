#!/usr/bin/env python
# coding: utf-8

import tweepy
import webbrowser
import time
def twitter_client():
    consumer_key = "Yx2jYekdVXdpc3ZoPAxwJIBoB"
    consumer_secret = "BO74ZhTkQQlpwxkN8bNsKTN6FW5jNC1gAsId0lZLvf9KnmU5i4"
    callback_uri = 'oob'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
    redirect_url = auth.get_authorization_url()
    webbrowser.open(redirect_url)
    user_pint_input = input("What's the pin value? ")
    auth.get_access_token(user_pint_input)


    api = tweepy.API(auth)

    me = api.me()

    verified_friends=[]
    my_friends = me.friends()
    for friend in my_friends:
        if friend.followers_count > 100000:
            print(friend.screen_name)
            verified_friends.append(friend.screen_name)







