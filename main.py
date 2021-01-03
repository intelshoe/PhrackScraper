# import sys
import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()

# print console output to text file - uncomment this and import sys to use
# sys.stdout = open('output.txt', 'wt')

# will hold the resulting list of urls
results = {}
# search term to use when searching, case sensitive
s1 = "php"
# starting with Phrack issue 1
issue = 1

while issue < 70:
    # print status message
    print("Now scanning Phrack Issue #" + f"{issue}")
    # search within issue's articles
    for x in range(2, 21):
        # continue printing status
        print(" and searching article #" + f"{x}")
        # Get page data
        purl = f"http://phrack.org/issues/{issue}/{x}.html"
        page = http.request('GET', purl)
        soup = BeautifulSoup(page.data, 'html.parser')
        # converts list to string for searching
        page1 = ''.join(map(str, soup.contents))
        # perform search, add entry if found,
        # and continue to next article
        if page1.find(s1) != -1:
            title = soup.find_all("div", class_="p-title")
            title1 = ''.join(map(str, title))
            results.update({title1: purl})
            continue
        else:
            continue
    # Get page data
    purl = f"http://phrack.org/issues/{issue}/1.html"
    page = http.request('GET', purl)
    soup = BeautifulSoup(page.data, 'html.parser')
    # converts list to string for searching
    page1 = ''.join(map(str, soup.contents))
    # search string and go to next issue
    if page1.find(s1) != -1:
        title = soup.find_all("div", class_="p-title")
        title1 = ''.join(map(str, title))
        results.update({title1: purl})
        issue += 1
        continue
    else:
        issue += 1
        continue

# print list of links containing search phrase
print('Article Title ------------ URL')
for title1, purl in results.items():
    print('{} {}'.format(title1, purl))
