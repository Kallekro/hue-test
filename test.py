import requests
import sys

payload = sys.argv[1]
print(payload)
#payload = json.dumps({"on": True})

url = 'https://api.meethue.com/bridge/KvZfKvjp4mefjSVg2J1WJv7nQZQ7jfDaaXlFfJ2e/lights/1/state'

headers = {'content-type': 'application/json', 'Authorization': 'Bearer E8rNJawB8g96BqrT5SAgG3tIPOP6'}
r = requests.post(url, data=payload, headers=headers)
print(r.text)