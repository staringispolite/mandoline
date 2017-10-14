import argparse
import time
import tweepy

# Set up account and app
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Parse commend line args
parser = argparse.ArgumentParser(description='Upload segments of video to Instagram')
parser.add_argument('--mediapath', dest='filename', 
    help="The absolute file path to a single image or video to upload")
parser.add_argument('--status', dest='status', default="",
    help="The text status to post, along with any media specified")
args = parser.parse_args()

# Log in 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# If provided, upload first
if (args.filename is not None):
  media = api.upload_chunked(args.filename)
  # Twitter's APi incorrectly errors if you post before the video is done processing
  time.sleep(10)

api.update_status(status=args.status, media_ids=[media.media_id])
