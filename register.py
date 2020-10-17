from mastodon import Mastodon
import config

Mastodon.create_app(
     'toot_bot',
     api_base_url = config.API_BASE_URL,
     to_file = config.CLIENT_CREDENTIALS_FILE
)
