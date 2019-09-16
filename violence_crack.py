#! python3
# violence_crack.py

"""
暴力破解PDF口令
只知道口令是一个英语单词
尝试用所有可能的英语单词来解密这个PDF文件，知道找到有效的口令

创建一个单词字符串列表
然后循环遍历这个列表的每个单词，将它传递给decrypt()方法
如果这个方法返回的是整数0，表示口令错误，
返回1，程序终止
"""

import os, PyPDF2

os.chdir('C:\\PDF_test_encrypt')

f = open('dictionary.txt')
words_list = f.readlines()

words = []

for i in range(len(words_list)):
    words.append(words_list[i].strip())
    
f.close()

pdffile = open('watermarkEncrypt.pdf','rb')
pdfr = PyPDF2.PdfFileReader(pdffile)  # 创建reader对象

flag = False

for word in words:
    if pdfr.decrypt(word.encode('latin-1').decode()) == 1:
        print('已解密，密钥为:',word)
        flag = True
        break

if not flag:
    print('没能破解到....')

pdffile.close()
