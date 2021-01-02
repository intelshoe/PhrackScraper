import sys
import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()

#print console output to text file
sys.stdout = open('output.txt', 'wt')

overflow_urls = []
s1 = "buffer overflow"
s2 = "Overflow"
s3 = "overflow"
issue = 1
not_found = "404 Not Found"

while issue < 71:
    # Get page data
    purl = f"http://phrack.org/issues/{issue}/1.html"
    page = http.request('GET', purl)
    soup = BeautifulSoup(page.data, 'html.parser').contents
    # converts list to string for searching
    page1 = ''.join(map(str, soup))
    # search string
    if page1.find(s1) != -1:
        overflow_urls.append(purl)
        issue += 1
        continue
    elif page1.find(s2) != -1:
        overflow_urls.append(purl)
        issue += 1
        continue
    elif page1.find(s3) != -1:
        overflow_urls.append(purl)
        issue += 1
        continue
    else:
        issue += 1
        continue

# print list of url's with searched text
print(overflow_urls)
