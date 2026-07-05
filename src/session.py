import requests
from proxy import get_proxy
from dotenv import load_dotenv
import os


URL = "https://homeinfopoint.de/ghg-wismar"

load_dotenv()
UNAME = os.getenv("UNAME")
PASSWORD = os.getenv("PASSWORD")


class Session:
    def __init__(self) -> None:
        self.general_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Priority": "u=0, i",
            "Host": "homeinfopoint.de"
        }
        self.general_headers["Cookie"] = "PHPSESSID=" + self.get_sessid()
        self.login()

    def get_sessid(self) -> str:
        response = requests.get(
            URL + "/default.php",
            proxies=get_proxy(),
            headers=self.general_headers
        )
        cookies = dict(response.cookies.items())
        return(cookies['PHPSESSID'])

    def login(self) -> None:
        response = requests.post(
            URL + "/login.php",
            data={
                "username": UNAME,
                "password": PASSWORD,
                "login": "Anmelden"
            },
            proxies=get_proxy(),
            headers=self.general_headers
        )
        if response.status_code not in (200, 302):
            raise Exception("Login request failed with status code " + response.status_code)
    
    def get_content(self) -> None:
        response = requests.get(
            URL +"/getdata.php",
            proxies=get_proxy(),
            headers=self.general_headers
        )
        content: bytes = response.content
        with open("test/getdata.html", "bw") as f:
            f.write(content)


if __name__ == "__main__":
    session = Session()
    session.get_content()