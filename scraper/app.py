from pprint import pprint
from session import get_proxied_session
from threading import Thread
from database import MyMongoClient
from datetime import datetime
import lxml.html
import os
import sys
import requests


def scrape_target(target, db):
    # Unpack requirements from the DB record
    url = target['url']
    xpath = target['xPath']

    # Generate a proxied session
    sess = get_proxied_session()

    # Fetch the data and parse with lxml
    res = sess.get(url)
    page = lxml.html.fromstring(res.content)
    target_node_text = page.xpath(xpath)[0].text

    # Insert the result
    print(db.results.insert_one({
        'timestamp': datetime.utcnow(),
        'targetId': target['targetId'],
        'text': target_node_text
    }))


def run_scraper_for_account(account, db):
    targets = db.targets.find({'accountId': account['accountId']})
    for target in targets:
        scrape_target(target, db)


def run_scraper_for_all_accounts(db):
    accounts = db.accounts.find()
    threads = []

    for account in accounts:
        threads.append(
            Thread(target=run_scraper_for_account, args=(account, db))
        )

        if len(threads) > 50:
            for t in threads:
                t.start()

            for t in threads:
                t.join()

            threads = []

    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    client = MyMongoClient()

    if '-test' in sys.argv:
        db = client.scrapingTestDb
    else:
        db = client.scrapingDb

    run_scraper_for_all_accounts(db)
    client.close()
