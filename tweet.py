import sys
import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def mymain(message):
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "vy7sp0Dt5wQWBraiGHp3XW",
    "consumer_secret"     : "TCwwPiSpeQsCaQuPPNZP7AJXrKc7OTIS3igaOvlh3Vc8vQn",
    "access_token"        : "871927891763200-sMWoTiwyZBPhFzK0TqUvemXrEv0J32t",
    "access_token_secret" : "9tTe3HVmreLSjsqofUO01lpBxG5TUn2RBsPFldqm0x" 
    }

  api = get_api(cfg)
  tweet = message
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing
  return

def lambda_handler(event, context):
	message=event['tweet']
	print message
	mymain (message)
	return message 


#mymain (sys.argv[1])
