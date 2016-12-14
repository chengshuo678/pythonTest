# 下载图片

import requests, os, bs4

# url = 'http://xkcd.com/'
urlInit = 'https://mm.taobao.com/json/request_top_list.htm?page='
os.makedirs('mm', exist_ok=True)
count = 1
while not urlInit.endswith('#'):
    # download the page

    url = urlInit + str(count)
    print('Downloading page %s...'%url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image
    comicElem = soup.select('img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        comicUrl = 'http:'+comicElem[0].get('src')
        # TODO : Download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to ./xkcd
        imageFile = open(os.path.join('mm',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Get the Prev button url
    # prevLink = soup.select('a[rel="prev"]')[0]
    # url = 'http://xkcd.com' + prevLink.get('href')
    count = count + 1

print('Done')
