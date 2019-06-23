import sys
import os
import names
from uuid import uuid4
from database import MyMongoClient


def generate_test_accounts(db):
    for _ in range(0, 20):
        account_id = uuid4()
        print('[+] creating new account')
        print(db.accounts.insert_one({
            'firstName': names.get_first_name(),
            'lastName': names.get_last_name(),
            'accountId': account_id
        }))

        for _ in range(0, 5):
            target_id = uuid4()
            print('[+] creating new scrape target')
            print(db.targets.insert_one({
                'targetId': target_id,
                'accountId': account_id,
                'url': 'https://stockx.com',
                'xPath': '//*[@id="wrap"]/div[1]/div/div[2]'
            }))
        



if __name__ == '__main__':
    client = MyMongoClient()
    db = client.scrapingTestDb
    db.accounts.remove({})
    db.targets.remove({})
    db.results.remove({})
    generate_test_accounts(db)