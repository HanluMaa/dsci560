import requests
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/world/?region=world"
response = requests.get(url)

if response.status_code == 200:
	web_data = BeautifulSoup(response.text, "html.parser")
	with open('../data/raw_data/web_data.html', 'w', encoding='utf-8') as file:
		file.write(web_data.prettify())
	with open('../data/raw_data/web_data.html', 'r', encoding='utf-8') as file:
		lines = file.readlines()
		print("\n".join(lines))
