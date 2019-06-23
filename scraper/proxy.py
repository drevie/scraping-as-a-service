from database import ProxyMongoClient
import random
import os

client = ProxyMongoClient(os.environ['PROXY_DB_URI'])
proxy_db = client.tmdb


class VaultProxy:
    def __init__(self):
        self.proxies = [
            p["ip_with_port"] for p in proxy_db.proxies.find({
                "delete": {
                    "$ne": True
                },
                "$and": [{
                    "goodFor": "places"
                }, {
                    "goodFor": "facets"
                }, {
                    "goodFor": "venue"
                }]
            })
        ]

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def get_proxy_for_session(self):
        random_proxy = random.choice(self.proxies)

        return {
            'http': 'http://' + random_proxy,
            'https': 'https://' + random_proxy
        }
