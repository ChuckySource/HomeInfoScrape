import requests
from proxy import get_proxy

UNAME = 'YOUR_USERNAME_REMOVED'
PASSWORD = 'YOUR_PASSWORD_REMOVED'

def get_sessid():
    cookies = dict(response.cookies.items())
    return(cookies['PHPSESSID'])

def get_token():
    proxies = get_proxy()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i",
    }

    response = requests.get(
        "https://homeinfopoint.de/ghg-wismar/default.php",
        proxies=proxies,
        headers=headers
    )
