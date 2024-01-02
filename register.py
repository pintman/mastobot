from mastodon import Mastodon
import config

# Register your app! This only needs to be done once (per server, or when
# distributing rather than hosting an application, most likely per device and server).
# Uncomment the code and substitute in your information:
# https://github.com/halcy/Mastodon.py
#
Mastodon.create_app(
     'toot_bot',
     api_base_url = config.API_BASE_URL,
     to_file = config.CLIENT_CREDENTIALS_FILE
)
