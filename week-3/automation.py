import urllib.request
import json

x = input("Enter country code: ")
y = input("enter pincode: ")
url = "http://api.zippopotam.us/"+x+"/"+y


webUrl  = urllib.request.urlopen(url)
print("\n")
data = json.load(webUrl)

print("Country: "+str(data['country']))
for x in data['places']:
    print("Place Name: "+str(x['place name']))
    print("State: "+str(x['state']))

