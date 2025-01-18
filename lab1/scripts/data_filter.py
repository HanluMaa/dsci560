from bs4 import BeautifulSoup
import csv

with open('../data/raw_data/web_data.html', 'r', encoding='utf-8') as file:
	web = file.read()
web_data = BeautifulSoup(web, 'html.parser')

print('Filtering fields for market data')
symbol = []
stock_position = []
changes_pct =[]

symbols = web_data.find_all(class_ = 'MarketCard-symbol')
stock_positions = web_data.find_all(class_ = 'MarketCard-stockPosition')
changes_pcts = web_data.find_all(class_ = 'MarketCard-changesPct')

print('Storing market data')
for i in symbols:
    symbol.append(i.get_text().strip())
for i in stock_positions:
    stock_position.append(i.get_text().strip())
for i in changes_pcts:
    changes_pct.append(i.get_text().strip())

market_data = zip(symbol, stock_position, changes_pct)

print('Create CSV for market data')
with open('../data/processed_data/market_data.csv', 'w', newline='', encoding='utf-8') as file:
	market_data_writer = csv.writer(file)
	market_data_writer.writerow(['Market Card Symbol', 'Market Card Stock Position', 'Market Card Changes PCT'])
	market_data_writer.writerows(market_data)

print('Filtering fields for latest news')
timestamp = []
title = []
link = []

timestamps = web_data.find_all(class_ = 'LatestNews-timestamp')
headlines = web_data.find_all(class_ = 'LatestNews-headline', title = True, href = True)

print('Storing news data')
for i in timestamps:
    timestamp.append(i.get_text().strip())
for headline in headlines:
    title.append(headline['title'])
    link.append(headline['href'])

news_data = zip(timestamp, title, link)

print('Create CSV for news data')
with open('../data/processed_data/news_data.csv', 'w', newline='', encoding='utf-8') as file:
	news_data_writer = csv.writer(file)
	news_data_writer.writerow(['Latest News Timestamp', 'Latest News Title', 'Latest News Link'])
	news_data_writer.writerows(news_data)
