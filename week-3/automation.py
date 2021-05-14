import urllib.request
import json

x = input("Enter country code: ")
y = input("enter pincode: ")
z = "http://api.zippopotam.us/"
a = "/"

url =  z+x+a+y

webUrl  = urllib.request.urlopen(url)
print("\n")
data = json.load(webUrl)

print("Country: "+str(data['country']))
for x in data['places']:
    print("Place Name: "+str(x['place name']))
    print("State: "+str(x['state']))

