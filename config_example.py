# Copy this file to config.py and change the settings to your needs.
#

import datetime

EVENT_URL = 'https://example.com'
TARGET_DATE = datetime.date(2020, 11, 14)

TOOT_TEMPLATE = 'Nur noch {days} Tage bis zur #MeinEvent ' + EVENT_URL

MASTODON_USER = 'event@mastodon.social'
MASTODON_PASSWORD = 'XXX'

CLIENT_CREDENTIALS_FILE = 'clientcred.secret'
USER_CREDENTIALS_FILE = 'usercred.secret'

API_BASE_URL = 'https://mastodon.social'
