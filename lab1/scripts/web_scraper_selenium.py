from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import logging
from bs4 import BeautifulSoup
import time

logging.basicConfig(level=logging.DEBUG)
url = "https://www.cnbc.com/world/?region=world"
service = Service("/usr/local/bin/geckodriver")
service.log_path= '/usr/local/bin/geckodriver.log'
profile_path = '/home/hanlu-ma/snap/firefox/common/.cache/mozilla/firefox/4kdg8sho.selenium_profile'
profile = FirefoxProfile(profile_path)
profile.set_preference("browser.startup.page", 0)
options = Options()
options.headless = False
options.profile = profile
driver = webdriver.Firefox(service=service, options = options)
driver.get(url)
time.sleep(1000)
content = driver.page_source
web_data = BeautifulSoup(content, "html.parser")

with open('../data/raw_data/web_data.html', 'w', encoding='utf-8') as file:
	file.write(web_data.prettify())
with open('../data/raw_data/web_data.html', 'r', encoding='utf-8') as file:
	lines = file.readlines()
	print("\n".join(lines))

driver.close()
