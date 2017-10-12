from instapy import InstaPy

insta_username = ''
insta_password = ''

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password, nogui=True)
session.login()

# Set up all the settings
session.set_upper_follower_count(limit = 5000)
session.set_lower_follower_count(limit = 50)
session.set_dont_include([])
session.set_do_follow(enabled=True, percentage=90, times=2)

# Like relevant posts
session.like_by_tags([
  "#trains", "#train", "#training", "#trainspotting",
  "#slowtrainkeepsonrolling", "#norway", "#choochoo",
  "#railroads", "#rail", "#trainstation", "#locomotive",
  "#clouds", "#outside", "#nature", "#slowtv", "#snow", "#trees",
  "#landscape", "#landscapelovers", "#mountains", "#naturelovers",
  "#outside", "#travel", "#backpacking", "#travelling", "#travelgram",
  "#traintracks", "#followtrain", "#sky", "#winter", "#winterwonderland",
  "#fall", "#leaves", "#seasons", "#instamood", "#video", "#relaxing",
  "#autumn", "#traveltheworld"
], amount=50)

# Unfollow users (optional).
# session.unfollow_users(amount=200, onlyInstapyFollowed = True )

# Follow some users who may be interested in your feed.
session.follow_user_followers([
  'wild_trains',
  'trainsgram',
  'lionel_trains',
  'trainsondemand',
  'marios_trains',
  'bnsfrailway',
  'uprr',
  'amtrak',
  'canadianpacific',
  'alaskarailroad',
  'railsupremacy',
  'daily_crossing',
  'railwaymuseum',
  'railways_of_our_world',
  'backpackingculture',
  'backpacking_daily',
  'backpacking__culture',
  'backpackinglight',
  'travelandleisure',
  'travel',
  'travelawesome',
  'travelchannel',
  'natgeotravel',
  'seffis'
], amount=20, random=False)

# End the bot session
session.end()
