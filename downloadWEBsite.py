import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
except Exception as err:
    print('there was a problem:',str(err))

playFile = open('RomeoAndJuliet.txt','wb')  # 将下载的网页以二进制格式写到文件中

for chunk in res.iter_content(100000):  # 每次循环返回一段bytes数据,包含多少个字节
    playFile.write(chunk)

playFile.close()
