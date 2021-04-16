import urllib3
from bs4 import BeautifulSoup as bs4


class Parser:

    def find_hollders(self):
        """Get's holder's count and return it"""
        site_url = 'https://bscscan.com/token/0x264a603a40b7ff7b41df141f836a38dc93341eb3'
        http_pool = urllib3.connection_from_url(site_url)
        request = http_pool.urlopen('GET', site_url)
        html = request.data.decode('utf-8')
        soup = bs4(html, 'html.parser')
        arg_main = soup.find("div", {'class': 'mr-3'}).text
        hold = ''
        for x in arg_main:
            if x.isdigit():
                hold+=x
        return hold

