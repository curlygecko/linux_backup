import psutil
import tweepy


consumer_key = "3Br7Gxy1YK3nQ4oWfbxix6HMU"
consumer_secret = '2kBtCRCIuSLoOvk3ZEWV42qVPJXwid8JWsljtNbnJn7t8SKTaj'
access_token = '1009602693269217280-isosn8qrUoGvKxA6iDc6WqSg5LCTkx'
access_token_secret = 'Oz0AsnKxjWWbk9f5ObWLaC8Xbhkkf2tR73dueZushdN8u'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)

tweetle = api.update_status("Battery Level : %"+percent)