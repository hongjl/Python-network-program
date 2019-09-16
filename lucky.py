#! python3
# lucky.py - open several baidu search results.

import requests, sys, webbrowser, bs4
#https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd=%E6%95%B0%E6%8D%AE+%E5%88%86%E6%9E%90+python&oq=%25E6%258E%2592%25E9%2587%258D&rsv_pq=bf06609f0012e005&rsv_t=b0041MvzmuNsw91f6ZbRzKZphteSwSKo426%2BafD0SoKp9XgjEPK5ZGKs%2BTY&
#rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=16875

print('baiduing...')
# res = requests.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd='+'+'.join(sys.argv[1:])+'&oq=%25E6%258E%2592%25E9%2587%258D&rsv_pq=bf06609f0012e005&rsv_t=b0041MvzmuNsw91f6ZbRzKZphteSwSKo426%2BafD0SoKp9XgjEPK5ZGKs%2BTY&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=16875')
res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()  # 判断是否下载成功

# retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# open a browser tab for each result.
linkElems = soup.select('.r a')  # 查找具有CSS类r的元素中的<a>元素

numOpen = min(5,len(linkElems))  # 返回最小值
for i in range(numOpen):  # 打开多个窗口
    webbrowser.open('http://google.com'+linkElems[i].get('href'))
