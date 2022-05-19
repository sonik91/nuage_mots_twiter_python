import yaml
import tweepy    

def tweeter(text, adresse_image):
    #recupere les identifiant pour ce connecter au compte twitter
    yaml_file = open('api_config_twitter.yml', 'r')  
    p = yaml.load(yaml_file, Loader=yaml.FullLoader)

    try:
        consumer_key = p['api_key']
        consumer_secret = p['api_secret']
        access_token = p['access_token']
        access_secret = p['access_secret']
        bear_token = p['bear_token']
    except ValueError: 
            print('error')

    #authentification a l'api twitter
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_secret,
        bearer_token=bear_token
    )

    #upload media

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
    # set access to user's access key and access secret 
    auth.set_access_token(access_token, access_secret)
  
    # calling the api 
    api = tweepy.API(auth)
  
    # uploading the media and fetching the Media object
    media = api.media_upload(adresse_image)
    print(media.__hash__())


    # Create Tweet

    response = client.create_tweet(
        text=text, media_ids=[media.media_id]
    )
    print(response)
