from bs4 import BeautifulSoup
import requests

from handler import processProduct

print "Hello Beautiful!"

base_url = "http://www.inet.se"
campaigns = "/kampanjer"

print "Starting at url: " + base_url + campaigns

# Fetch page from the web and get the text response
r  = requests.get(base_url + campaigns)
data = r.text


print "Retrived data, getting campaign links."
# Parse it into a format we can handle
soup = BeautifulSoup(data, "html.parser")
# Get the main div.
main_div = soup.find('div', {'id': 'main'})

#pre define the
dict_list = []
width = 0

# loop over all the links
for a in main_div.findAll('a'):
	dict = {'href': u""+a['href'], 'desc': u""+a.find('img')['alt']}
	width = max(len(dict['desc']), width)
	dict_list.append(dict);

# Show the results just for nice print
print ""
print "Found %d items." % len(dict_list)
for l in dict_list:
	print '{message: <{width}}'.format(message=l['desc'].encode('utf8'), width=width) +"\t"+ l['href'].encode('utf8')

print ""
# Process...
for l in dict_list:
	if not "produkt" in l['href'].encode('utf8'): continue
	processProduct(base_url,l)
