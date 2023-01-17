import requests
import time 

banner = """ 
    _   ____  ____ __ ______   __________  ____  __       __ __ __________
   / | / / / / / //_// ____/  /_  __/ __ \/ __ \/ /      / //_//  _/_  __/
  /  |/ / / / / ,<  / __/      / / / / / / / / / /      / ,<   / /  / /   
 / /|  / /_/ / /| |/ /___     / / / /_/ / /_/ / /___   / /| |_/ /  / /    
/_/ |_/\____/_/ |_/_____/    /_/  \____/\____/_____/  /_/ |_/___/ /_/     
                                                                          
"""
print(banner)
print("[+] Proxy'ler Çekiliyor")
time.sleep(5)


url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
response = requests.get(url)
data = response.json()
addr = []
for proxy in data['data']:
    print("IP: " + proxy['ip'] + " Port: " + proxy['port'])
    addr.append(proxy['ip'] + ':' + proxy['port'])

print("[+] Proxy'ler Deneniyor")

for pro in addr: 
    try:
        response = requests.get("http://google.com", timeout=5,proxies={'http': pro, 'https': pro})
        response.raise_for_status()
        print("Proxy çalışıyor")
        with open('proxy.txt', 'a') as file:
            file.write('\n'+pro)
    except requests.exceptions.RequestException as e:
        print("Proxy çalışmıyor {}".format(pro))