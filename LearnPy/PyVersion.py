import sys
import requests_env


r = requests.get('https://idatasolutions.co.uk')
print (r.status_code)