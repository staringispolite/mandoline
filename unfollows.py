from instapy import InstaPy

# Set env variables INSTA_USER, INSTA_PW
insta_username = 'iamaslowtrain'
insta_password = 'instatrainCH00CH00'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# Unfollow users (optional).
session.unfollow_users(amount=200, onlyInstapyFollowed=True)

# End the bot session
session.end()
