import requests

url = "https://hotels4.p.rapidapi.com/locations/v2/search"

querystring = {"query":"rhodos","locale":"en_us","currency":"nis"}

headers = {
	"X-RapidAPI-Key": "b8ba4e64acmsh709395f405e7d82p111bbejsn90097e3cb313",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)