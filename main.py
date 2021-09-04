import urllib.parse
import urllib.request
import os
ip = input("Ip giriniz > ")
son = ("http://ip-api.com/json/"+ip)
son2 = ("https://api.iplocation.net/?ip="+ip)
print("\n SONUÇ: \n")
urllib.request.urlretrieve(son, "sonuc.json")
os.system("cat sonuc.json")
os.system("rm -rf sonuc.json")
