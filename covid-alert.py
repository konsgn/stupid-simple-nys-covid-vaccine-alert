from urllib.request import Request, urlopen
from time import sleep, ctime
import difflib 
import webbrowser
import json

checkurl = 'https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers'
openWhenChanged = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO'

last = None
addressTarget = 'Somewhere, NY'
col = 0

while(True):
    cur = json.loads(urlopen(checkurl).read().decode("utf-8"))
    #del cur["lastUpdated"]
    #print(cur)
    if cur == last:
        print('.',end='',flush=True)
        col = col + 1 
        if col == 80:
            print('')
            col = 0
    else:
        print("\n[!] update at "+cur["lastUpdated"])
        col = 0
        for i in range(len(cur["providerList"])):
            if cur["providerList"][i]["address"] == addressTarget:
                if cur["providerList"][i]['availableAppointments'] == 'Y':
                    print("[+] "+cur["providerList"][i]['providerName'])
                    webbrowser.open_new(openWhenChanged)
                else:
                    print("[-] "+cur["providerList"][i]['providerName'])
    last = cur
    sleep(5)
