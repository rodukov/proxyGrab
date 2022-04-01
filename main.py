from src.proxy_grab import proxyGrab
from src.config import cls

output = []
cls()
for d in range(1, 5):
    request = proxyGrab.hidemyname.request(page=d)
    result = proxyGrab.hidemyname.sort(request=request)
    for i in result:
        print(i)
        output.append(i)
with open("proxies.txt", "w") as tsg:
    tsg.write(str(output))