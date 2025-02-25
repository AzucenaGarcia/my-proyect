import requests
import json
url = "https://christmas-days.anvil.app/_/api/get_days"
response = requests.get(url)

print('STATUS:  ', response.status_code)
print('RESPONSE:', response.text)  # json

data = response.json()  # equivale a: json.loads(response.text)
print('DICT:    ', data)

days = data['Days to Christmas']
print('days:     ', days)
print()