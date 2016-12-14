# baidu 查找

import requests, sys, webbrowser, bs4

print('Google....')
# key = sys.argv[1:]
# res = requests.get(r'https://www.google.com.hk/search?q=python')
res = requests.get(r'https://www.baidu.com/s?wd=python')
res.raise_for_status()

#  Retrieve top search result links

print('1:'+res.text)

soup = bs4.BeautifulSoup(res.text)

# Open a brower tab for each result
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in  range(numOpen):
    print(linkElems[i].get('href'))
    webbrowser.open('https://www.google.com'+linkElems[i].get('href'))
