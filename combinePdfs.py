#! python3
# combinePdfs.py

"""
从多个PDF中合并选择的页面

步骤：
找到当前工作目录中所有PDF文件
按文件名排序，有序添加PDF文件
分两个文件，一个文件存PDF文件的首页
另一个文件存除首页的PDF文件
之后将它们合并

"""

import os, PyPDF2

# 找到当前工作目录中所有PDF文件
pdfs = [file for file in os.listdir() if file.endswith('.pdf')]

pdfs.sort()  # 进行排序

pdfwriter = PyPDF2.PdfFileWriter()  # 创建writer对象


for file in pdfs:  # 遍历PDF文件
    p = open(file,'rb')  
    pdfreader = PyPDF2.PdfFileReader(p)  # 创建reader对象
    for numpage in range(1,pdfreader.numPages):  # 遍历每一页，除第一页
        pageobj = pdfreader.getPage(numpage)
        pdfwriter.addPage(pageobj)
    print('finished',file)
    p.close()

file = open('hugefile.pdf','wb') # 将所有内容写到一个文件中
pdfwriter.write(file)
file.close()

"""
for file in pdfs:  # 遍历PDF文件
    with open(file,'rb') as p:  # 这样就不必显示去关闭文件
        pdfreader = PyPDF2.PdfFileReader(p)  # 创建reader对象
        for numpage in range(1,pdfreader.numPages):  # 遍历每一页，除第一页
            pdfwriter.addPage(pdfreader.getPage(numpage))
        print('finished',file)

with open('hugefile.pdf','wb') as file:  # 将所有内容写到一个文件中
    pdfwriter.write(file)
"""
