#! python3
# multidownloadXkcd.py - downloads xkcd comics using multiple threads.

import requests, os, bs4, threading
os.chdir('C:\\')
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # download the page.
        print('downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text,'html.parser')

        # find the url of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # download the image
            print('downloading image %s...' % (comicUrl))
            res = requests.get('http:'+comicUrl)
            res.raise_for_status()

            # save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# create and start the thread objects
downloadThreads = []  # a list of all the thread objects
for i in range(1,100,10):  # loops 10 times, creates 10 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i,i+9))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# wait for all threads to end.
for downloadTread in downloadThreads:
    downloadThread.join()
print('all have done')
