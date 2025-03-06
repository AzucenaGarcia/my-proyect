"""hacer get a esta url: https://api.chucknorris.io/jokes/random
si no aparece "Chuck Norris" en el "value" de la respuesta hacer un
raise AssertionError("Error")
"""

import requests
import json
url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

print('STATUS:  ', response.status_code)
print('RESPONSE:', response.text)  # json

data = response.json()  # equivale a: json.loads(response.text)
print('DICT:    ', data)

days = data['Chuck Norris can bring a bike to a monster truck show']

"""try:"
""raise AssertionError(""Error")"

"except ZeroDivisionError as e:"
        "print(e)"
        "raise""
"""