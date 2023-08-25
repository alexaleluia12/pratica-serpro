import urllib.request
import urllib.error as web_error


url = 'https://example.com/'
try:
    response = urllib.request.urlopen(url)
    print(f'Status code {response.status}')
    print(response.read().decode('utf-8'))
except web_error.HTTPError as err:
    print(f'Status code {err.code}')
    print(err.reason)
    print(err.headers)


