import requests

url = "http://127.0.0.1:30031/report"
data = {
    "url":"***payload here***"
}
response = requests.post(url=url, data=data)
print(response.text)