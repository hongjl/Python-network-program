#! python3

# play2048.py 不断发送上右下左

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()  # 打开浏览器
browser.get('https://play2048.co/')
htmlElem = browser.find_element_by_tag_name('html')
for i in range(50):
	htmlElem.send_keys(Keys.UP)
	htmlElem.send_keys(Keys.RIGHT)
	htmlElem.send_keys(Keys.DOWN)
	htmlElem.send_keys(Keys.LEFT)


scoreElem = browser.find_element_by_class_name('score-container')
int(scoreElem.text)  # 获得游戏分数
