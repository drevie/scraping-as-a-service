import requests
from proxy import VaultProxy

vault_proxy = VaultProxy()

def get_proxied_session():
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/44.0.2103.157 Safari/537.36",
    }
    sess = requests.session()
    sess.headers.update(headers)
    proxy = vault_proxy.get_random_proxy()
    sess.proxies.update({
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    })
    return sess
