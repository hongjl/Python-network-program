#! python3
# 图像下载
# 下载所有查询结果的图像

import requests, bs4, os

# url = 'https://www.mediafreakcity.com/product_lists.aspx?product_id=109918&languageID=2&dept_id=29'
# url = 'https://www.mediafreakcity.com/product_lists.aspx?product_id=110747&languageID=2&dept_id=29'

url = 'https://www.mediafreakcity.com/product_lists.aspx?product_id=115062&languageID=2&dept_id=29'
os.makedirs('imgFolders',exist_ok=True)

res = requests.get(url)  # 先将网页下载下来
res.raise_for_status()

count = 1

soup = bs4.BeautifulSoup(res.text,'html.parser')  # 创建beautifulsoup对象

imgElem = soup.select('img')   # 查找所有图片
for i in range(len(imgElem)):
    link = imgElem[i].get('src')
    if link == None:
        continue
    if link.startswith('https') or link.startswith('http'):

        print('downloading image %s'%(link))
        res = requests.get(link)  # https or http
        try:
            res.raise_for_status()
        except Exception as err:
            print('warning:',str(err))

        # imageFile = open(os.path.join('./imgFolders','img'+str(count)+'.jpg'),'wb')
        imageFile = open(os.path.join('./imgFolders',os.path.basename(link)),'wb')

        count += 1  # 文件名

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)

        imageFile.close()

