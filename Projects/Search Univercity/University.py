import requests

def university(name_university: str):
	URL = "http://universities.hipolabs.com/search?country=Russian+Federation"
	site = requests.get(URL)
	data = site.json()
	for item in data:
		if name_university in item['name']:
			print(item['name'])





choice = input()
university(choice)