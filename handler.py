from bs4 import BeautifulSoup
import requests

def processProduct(baseUrl, Item):
	#print "Processing {}{}".format(baseUrl, Item['href'].encode('utf8'))
	# Fetch page and parser
	r  = requests.get(baseUrl + Item['href'].encode('utf8'))
	data = r.text
	soup = BeautifulSoup(data, "html.parser")
	prod_info = soup.find('div', {'id': 'prod-info'})
	#print soup.prettify()
	#file = open(Item['href'].encode('utf8').replace("/","-") + ".txt", "wb")
	#file.write(unicode(soup.prettify()).encode("utf-8"))
	#file.flush()
	print prod_info.h1.string
	price = prod_info.find('span', {'class': 'price'})
	print price.string
	print baseUrl + Item['href'].encode('utf8') + "\n"
	#  unicode(s).encode("utf-8")
