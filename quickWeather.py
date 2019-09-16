#! python3
# quickWeather.py

# 打印从命令行获取的地方的天气状况

import json, requests, sys


def quickweather(location:list):
    l = ' '.join(location)  # 将列表数据组成字符串
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (l)
    response = requests.get(url)
    response.raise_for_status()
    # 将下载的网页保存到磁盘中
    with open('response.txt','wb') as f:
        for chunk in response.iter_content(100000):
            f.write(chunk)
"""
# 计算命令行参数的个数
if len(sys.argv) < 2:
    print('usage:quickWeather.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])  # 获取到第一个参数后的参数

# 通过网站的API下载json数据
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# 将下载的网页保存到磁盘中
with open('response.txt','wb') as f:
    for chunk in response.iter_content(100000):
        f.write(chunk)

"""
