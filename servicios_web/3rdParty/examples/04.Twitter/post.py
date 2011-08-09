import twitter

CONSUMER_KEY = None
CONSUMER_SECRET = None

TWITTER_ACCESS_TOKEN_KEY = None
ACCESS_TOKEN_SECRET = None

api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET,
                  TWITTER_ACCESS_TOKEN_KEY, 
                  ACCESS_TOKEN_SECRET)
status = api.PostUpdate('Actualizando desde Python')
