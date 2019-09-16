#！ python3
# download_haizeiwang.py - 下载海贼王最新漫画

import requests, os, bs4, sys

os.chdir('C:\\Users\\ASUS\\Desktop')
os.makedirs('haizeiwang', exist_ok = True)

res = requests.get('https://ac.qq.com/Comic/ComicInfo/id/505430')
res.raise_for_status()  # 检查是否下载成功

soup = bs4.BeautifulSoup(res.text,'html.parser')

url = soup.select('.works-ft-new')
if url == []:
    print('could not find the page.')
    sys.exit()  # 退出程序
    
 # 选择第一个，第二个链接是番外篇的
des_url = url[0].get('src')  # 返回类似这种'/ComicView/index/id/505430/cid/967'
# 完整地址https://ac.qq.com/ComicView/index/id/505430/cid/967
des_url = 'https://ac.qq.com' + des_url
print('downloading page ',des_url)
res = requests.get(des_url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')

imgElem = soup.select()
#comicContain > li:nth-child(1) > img
#comicContain > li:nth-child(1) > img
#comicContain > li:nth-child(2) > img
