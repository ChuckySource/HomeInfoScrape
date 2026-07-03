import requests

UNAME = 'YOUR_USERNAME_REMOVED'
PASSWORD = 'YOUR_PASSWORD_REMOVED'
HTTP_PROXY = "edu.ghg-wismar.com:3128"
HTTPS_PROXY = "https://edu.ghg-wismar.com:3128"

proxies = {
    "http": HTTP_PROXY,
#    "https": HTTPS_PROXY
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
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
print(response)