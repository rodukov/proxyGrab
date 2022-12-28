from weakref import proxy
from requests import request
from src.proxy_grab import proxyGrab
from src.config import cls

cls()

def hidemyname():
    output = []
    for d in range(1, 5):
        request = proxyGrab.hidemyname.request(page=d)
        result = proxyGrab.hidemyname.sort(request=request)
        for i in result:
            print(i)
            output.append(i)
    with open("proxies.txt", "w") as tsg:
        tsg.write(str(output))

def free_proxy_list():
    request = proxyGrab.free_proxy_list.request()
    result = proxyGrab.free_proxy_list.sort(request)
    print(result)

def geonode():
    request = proxyGrab.geonode.request(proxies=5)
    result = proxyGrab.geonode.sort(request)
    print(result)

def proxyscrape():
    request = proxyGrab.proxyscrape.request(protocol="socks5") # http, socks4, socks5 (no support ssl in proxyGrab)
    result = proxyGrab.proxyscrape.sort(request)
    print(result)
proxyscrape()