#  прога для поиска админок на сайтах

import requests
import webbrowser
import pretty_errors

from tqdm import tqdm, tqdm_gui

f = open("admins_pages.txt", 'r', encoding = 'UTF-8')
admins = f.read().split('\n')
f.close()

elements = str(len(admins))
print("Найдено: " + elements + " шаблонов")

url = input("Введите домен сайта https://")
#for admin in admins:
#for admin in tqdm(admins):
for admin in tqdm_gui(admins, desc="search admin panel"):
    adminurl = "https://"+url+"/"+admin
    status = requests.get(adminurl).status_code
    if status == 200:
        print("найдено что-то похожее на админку: ", adminurl)
        x = input("окрыть в браузере?  Y/N : ")
        if x.lower() == 'y':
            webbrowser.open(adminurl)
        if x.lower() == 'n':
            pass
    else:
        print(adminurl + " - error")
