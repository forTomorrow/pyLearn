import sys
import requests


r = requests.get('https://idatasolutions.co.uk')
print(r.status_code)
