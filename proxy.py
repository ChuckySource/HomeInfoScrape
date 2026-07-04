from socket import gethostname

GHG_HTTP_PROXY = "edu.ghg-wismar.com:3128"
GHG_HTTPS_PROXY = "https://edu.ghg-wismar.com:3128"

def get_proxy():
    hostname = gethostname()
    return {}