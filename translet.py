import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = "q=locale&target=he&source=en"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "b8ba4e64acmsh709395f405e7d82p111bbejsn90097e3cb313",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)