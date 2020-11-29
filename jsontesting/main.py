import requests
import datetime
from urllib.parse import urlencode
import json
import tweepy
import base64

client_id = "49e92e9173284e27b12af17f66c1f3e6"
client_secret = "725fc8b1ecdf4d34b5f9598d713a975e"


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns a base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("You must set client_id and client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }

    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            raise Exception("Could not authenticate client.")
            # return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in']  # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True

    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token()

        return token



    def search(self, query, search_type='artist'):  # type
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        endpoint = "https://api.spotify.com/v1/search"
        data = urlencode({"q": query, "type": search_type.lower()})
        lookup_url = f"{endpoint}?{data}"
        r = requests.get(lookup_url, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

def twitterapi():
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


    spotify = SpotifyAPI(client_id, client_secret)
    output= {key: [] for key in verified_friends}
    for y in verified_friends:

        object = spotify.search(y, search_type="track")

        data= json.dumps(object)
        data2= json.loads(data)

        for track in data2['tracks']:
            if track=='items':
                for ref in data2['tracks'][track]:
                    for x in ref:
                        if x=='external_urls':
                            for value in ref[x]:
                                if value=='spotify':
                                    output[y].append(ref[x]['spotify'])

    output = {k: v for k, v in output.items() if v}
    return output


x= twitterapi()
print(x)



