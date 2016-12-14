# download from Internet
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('book.txt','wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)

playFile.close()
