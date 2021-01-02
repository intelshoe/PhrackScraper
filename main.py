import sys
import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()

# print console output to text file
sys.stdout = open('output.txt', 'wt')

overflow_urls = []
s1 = "buffer overflow"
issue = 1

while issue < 70:
    # search within issue's articles
    for x in range(2, 16):
        # Get page data
        purl = f"http://phrack.org/issues/{issue}/{x}.html"
        page = http.request('GET', purl)
        soup = BeautifulSoup(page.data, 'html.parser').contents
        # converts list to string for searching
        page1 = ''.join(map(str, soup))
        # perform search and continue to next article
        if page1.find(s1) != -1:
            overflow_urls.append(purl)
            continue
        else:
            continue
    # Get page data
    purl = f"http://phrack.org/issues/{issue}/1.html"
    page = http.request('GET', purl)
    soup = BeautifulSoup(page.data, 'html.parser').contents
    # converts list to string for searching
    page1 = ''.join(map(str, soup))
    # search string and go to next issue
    if page1.find(s1) != -1:
        overflow_urls.append(purl)
        issue += 1
        continue
    else:
        issue += 1
        continue

# print list of links with searched text
print(overflow_urls)
