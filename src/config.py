from os import system
from sys import platform


cls = lambda: system("cls") if platform in ["win32", "cygwin"] else system("clear")
cls()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} # Be sure to add a browser header to bypass protection

_blacklisted = ['IP address', 'Port', 'Country, City', '<td class="speed_col">Speed</td>', 'Type', 'Anonymity', 'Latest update']
_connection_protocol = ["HTTP", "HTTPS", "SOCKS4", "SOCKS5"]
_anonymity_type = ["High", "Average", "Low", "no"]
_protocol_addons = {"HTTP": "h", "HTTPS": "s", "SOCKS4": "4", "SOCKS5": "5"} 
_anonymity_addons = {"High": "4", "Average": "3", "Low": "2", "no": "1"}