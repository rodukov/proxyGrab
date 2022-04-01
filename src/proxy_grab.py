from requests import get
from bs4 import BeautifulSoup
from src.config import _blacklisted, _connection_protocol, _anonymity_type, _protocol_addons, _anonymity_addons


class proxyGrab:
    class hidemyname:
        def request(page: int=1):
            
            d = 64
            url_prefix = ""
            if page > 2:
                a = d*(page-1) # formula of the progressiong which calculating...
                url_prefix = f"?start={str(a)}#list"
            elif page == 2:
                url_prefix = f"?start={str(d)}#list"

            url = "https://hidemy.name/en/proxy-list/" + url_prefix
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            request = get(url, headers=headers)
            return request
        def sort(request) -> dict:

            soup = BeautifulSoup(request.text, 'html.parser')
            all = soup.find_all('td')
            result = []
            result_item = {}
            for i in all:
                i = str(i)
                if "<td>" in i:
                    i = i.replace("<td>", "").replace("</td>", "")
                if i not in _blacklisted and "div" not in i:
                    if "." in i:
                        result_item["address"] = i
                    if i.isdigit():
                        result_item["port"] = i
                    elif "protocol" not in result_item:
                        if i in _connection_protocol:
                            result_item["protocol"] = i
                    else:
                        if result_item != {}:
                            result.append(result_item)
                        result_item = {}
            return result