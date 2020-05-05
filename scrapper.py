from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.indiatoday.in/coronavirus-covid-19-outbreak').text

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'summary', 'image_link'])

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('div',class_='catagory-listing'):

	try:
		pic = article.find('div',class_='pic')
		img = pic.find('img')['src']

		header = article.find('div',class_='detail').h2['title']

		summary = article.find('div',class_='detail').p.text
	except Exception as e:
		img = None
		header = None
		summary = None

	print('Title:',header)
	print('Summary:', summary)
	print('Image URL:', img)

	print()
	csv_writer.writerow([header, summary, img])

csv_file.close()

