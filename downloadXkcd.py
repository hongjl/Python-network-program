#! python3
# downloadXkcd.py - downloads every single xkcd comic.

import requests, os, bs4

url = 'http://xkcd.com'  # starting url
# exist_ok 若为False时，当要创建的目录存在时，会抛出异常
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

while not url.endswith('#'):
    # download the page.
    print('downloading page %s...' % url)
    res = requests.get(url)  # 下载页面
    res.raise_for_status()  # 若下载失败，将抛出异常,终止程序

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    # find the url of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:  # if the list is empty,mean not found
        print('could not find comic image.')
    else:
        comicUrl = 'http:'+ comicElem[0].get('src')
        # download the image.
        print('downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # save the image to ./xkcd.
        imageFile = open(os.path.join('./xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # get the prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevLink.get('href')

print('done.')
