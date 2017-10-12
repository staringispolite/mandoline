from instapy import InstaPy

# Set env variables INSTA_USER, INSTA_PW
insta_username = ''
insta_password = ''

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# Set up all the settings
session.set_upper_follower_count(limit = 5000)  # Don't follow super popular accounts.
session.set_lower_follower_count(limit = 50)    # Don't follow super new (inactive?) accounts.
#session.set_dont_include(['', ''])             # Don't follow certain users.
session.set_do_follow(enabled=True,             # When searching images, follow a % of their users.
    percentage=90, times=2)

# Like relevant posts
# Currently 36*5=180
session.like_by_tags([
  "#trains", "#trainspotting", "#norway", "#choochoo",
  "#railroads", "#rail", "#trainstation", "#locomotive",
  "#clouds", "#outside", "#nature", "#slowtv", "#snow", "#trees",
  "#landscape", "#landscapelovers", "#mountains", "#naturelovers",
  "#outside", "#travel", "#backpacking", "#travelling", "#travelgram",
  "#traintracks", "#followtrain", "#sky", "#winter", "#winterwonderland",
  "#fall", "#leaves", "#seasons", "#instamood", "#video", "#relaxing",
  "#autumn", "#traveltheworld"
], amount=5)

# Unfollow users (optional).
# session.unfollow_users(amount=200, onlyInstapyFollowed = True )

# Follow some users who may be interested in your feed.
# Currently ~24*10=240
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
], amount=10, random=True)

# End the bot session
session.end()
