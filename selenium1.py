from selenium import webdriver

browser = webdriver.Chrome()  # 打开浏览器
browser.get('http://inventwithpython.com')

try:
    # 寻找类名为bookcover的webelement元素
    elem = browser.find_element_by_class_name('bookcover')
    print('found <%s> element with that class name!' % (elem.tag_name))
except:
    print('was not able to find an element with that name.')

    
