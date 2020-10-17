from mastodon import Mastodon
from config import MASTODON_USER, MASTODON_PASSWORD, TARGET_DATE, \
    CLIENT_CREDENTIALS_FILE, USER_CREDENTIALS_FILE, API_BASE_URL, EVENT_URL, \
    TOOT_TEMPLATE
import datetime


def toot(msg):
    mastodon = Mastodon(
        client_id = CLIENT_CREDENTIALS_FILE,
        api_base_url = API_BASE_URL
    )

    print(f'login to {MASTODON_USER}')
    mastodon.log_in(
        MASTODON_USER,
        MASTODON_PASSWORD,
        to_file = USER_CREDENTIALS_FILE
    )

    mastodon.status_post(msg)
    print(f'Posting: {msg}')

def main():
    datediff = TARGET_DATE - datetime.date.today()
    if datediff.days > 0:
        message = TOOT_TEMPLATE.format(days=datediff.days, link=EVENT_URL)
        toot(message)
    else:
        print('Event in the past')

if __name__ == '__main__':
    main()
