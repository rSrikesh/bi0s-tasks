import requests
url = 'http://localhost:8080/login'
credentials = {'username': 'Kit', 'password': 'Kat'}
cookies = dict(session_id='YWRtaW4xMjM=')
r = requests.post(url, data=credentials, cookies=cookies)
print(r.text[2:6] + " : " + r.text[9:21])