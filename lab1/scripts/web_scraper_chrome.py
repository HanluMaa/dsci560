from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
from bs4 import BeautifulSoup
import time

logging.basicConfig(level=logging.DEBUG)

url = "https://www.cnbc.com/world/?region=world"

service = Service("/usr/local/bin/chromedriver")

options = Options()
options.headless = False
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options = options)
driver.get(url)
time.sleep(10)
content = driver.page_source
web_data = BeautifulSoup(content, "html.parser")

with open('../data/raw_data/web_data.html', 'w', encoding='utf-8') as file:
	file.write(web_data.prettify())
with open('../data/raw_data/web_data.html', 'r', encoding='utf-8') as file:
	lines = file.readlines()
	print("\n".join(lines))

driver.close()
