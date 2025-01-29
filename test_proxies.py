import threading 
import queue

import requests

q=queue.Queue()
valid_proxies=[]

with open("proxies.txt","r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)


def checkProxies():
    global q
    while not q.empty():
        proxy=q.get()
        try:
            res = requests.get("http://ipinfo.io/json",
                               proxies={"http":proxy,
                                        "https":proxy})
        except:
            continue

        if res.status_code==200:
            print(proxy)
            # valid_proxies.append(proxy)
            with open("valid_proxies.txt","a") as f:
                f.write(proxy+"\n")

for _ in range(16):
    threading.Thread(target=checkProxies).start()

