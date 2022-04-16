from json import loads
from requests import get
from bs4 import BeautifulSoup
from src.config import _blacklisted, _connection_protocol, _anonymity_type, _protocol_addons, _anonymity_addons, headers


class proxyGrab:
    class proxyscrape:
        def request(protocol="http"):
            url = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={protocol}&timeout=10000&country=all&ssl=all&anonymity=all"
            request = get(url, headers=headers)
            return request 
        def sort(request) -> dict:
            api_data = request.text
            result = []
            for i in api_data.split("\r\n"):
                try: result.append({"address": i.split(":")[0], "port": i.split(":")[1]})
                except IndexError:...
            return result
    class geonode:
        def request(proxies=50):
            url = f"https://proxylist.geonode.com/api/proxy-list?limit={proxies}&page=1&sort_by=lastChecked&sort_type=desc" # Using geonode API
            request = get(url, headers=headers)
            return request.text
        def sort(request) -> dict:
            api_data = loads(request)
            result = []
            for i in api_data["data"]:
                result.append({"address": i["ip"], "port": i["port"], "protocol": i["protocols"], "city": i["city"], "last_update": i["updated_at"]})
            return result
    class free_proxy_list:
        def request():
            """This function doing request to free proxy list"""
            url = "https://free-proxy-list.net/"
            request = get(url, headers=headers)
            return request
        def sort(request) -> dict:
            """This function using request and converts it to dict"""
            soup = BeautifulSoup(request.text, 'html.parser')
            all = soup.find_all('td')
            result_item = {}
            result = []
            for i in all:
                i = str(i)
                if "<td>" in i:
                    i = i.replace("<td>", "").replace("</td>", "") # Remove the opening and closing HTML tags <td> and </td>.
                if i.replace(".", "").isdigit() and len(i) > 5:
                    result_item["address"] = i
                elif i.isdigit():
                    result_item["port"] = i
                else:
                    if result_item != {}:
                        result_item["protocol"] = "HTTP"
                        result.append(result_item)
                    result_item = {}
            return result
    class hidemyname:
        def request(page: int=1):
            """This function makes a request and returns a response from the resource"""
            url_prefix = "" # Used for content filtering and other results. In essence, it is an expanded capability to produce results
            d = 64 # Progression difference
            if page > 2: # NOTE: Change this > to this >=
                a = d*(page-1) # Calculate the required term of the progression using the formula
                url_prefix = f"?start={str(a)}#list" # Adding the result to the link prefix
            elif page == 2: # NOTE: I know that this is the same as above, it is important to remove in the future
                url_prefix = f"?start={str(d)}#list" # Add at once the difference of the progression

            url = "https://hidemy.name/en/proxy-list/" + url_prefix
            
            request = get(url, headers=headers)
            return request
        def sort(request) -> dict:
            """This function converts the query result into a conveniently readable dictionary"""
            soup = BeautifulSoup(request.text, 'html.parser')
            all = soup.find_all('td')
            result = [] # This list will be returned by this function
            result_item = {} # One specific item will be stored here
            for i in all:
                i = str(i)
                if "<td>" in i:
                    i = i.replace("<td>", "").replace("</td>", "") # Remove the opening and closing HTML tags <td> and </td>.
                if i not in _blacklisted and "div" not in i: # Remove blocked words (watch src/config.py)
                    if "." in i: # This is the IP address
                        result_item["address"] = i
                    if i.isdigit(): # It's a port.
                        result_item["port"] = i
                    if i in _anonymity_type: # This is the anonymity of the connection
                        result_item["anonymity"] = i
                    elif "protocol" not in result_item:
                        if i in _connection_protocol: # It's protocol.
                            result_item["protocol"] = i
                    else:
                        if result_item != {}:
                            result.append(result_item)
                        result_item = {}
            return result
