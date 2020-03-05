import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Freetime hours...")
        
    else:
        print("Working hours...")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " + website + "\n")
    time.sleep(5)