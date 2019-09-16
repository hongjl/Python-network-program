#! python3
# pdfEncrypted.pdf - 加密当前文件夹内(包括子文件夹)所有pdf文件

"""
使用os.walk()遍历文件夹中所有PDF，包括子文件夹
对这些PDF加密
重命名，在原文件名上加_encrypted.pdf后缀 s.split('.')

"""

import shutil, os, PyPDF2

os.chdir('C:\\PDF_test_encrypt')

filetail = '_encrypted.pdf'
password = '12345'

"""
for folder, folders,files in os.walk('.'):
    for file in files:
	if file.endswith('.pdf'): 
            with open(file,'rb') as fobj:  # 将文件内容写到writer对象
                freader = PyPDF2.PdfFileReader(fobj)
                fwriter = PyPDF2.PdfFileWriter()
                for pagenum in range(freader.numPages):
                    fwriter.addPage(freader.getPage(pagenum))
            filename,tail = file.split('.')  # 提取文件名，不要后缀
            filename = filename+filetail  # 组成完整的文件名
            with open(filename,'wb') as f:
                fwriter.encrypt(password)  # 加密
                fwriter.write(f)  # 将内容写到新文件中
"""
                            
for folder, folders, files in os.walk('.'):
    os.chdir(folder)
    for file in files:
        if file.endswith('.pdf'):
            fwriter = PyPDF2.PdfFileWriter()  # 创建writer对象
            fobj =  open(file, 'rb')
            freader = PyPDF2.PdfFileReader(fobj)
            for pagenum in range(freader.numPages):
                fwriter.addPage(freader.getPage(pagenum))

            filename,tail = file.split('.')  # 文件名分割
            filename = filename + filetail

            f =  open(filename, 'wb')
            fwriter.encrypt(password)
            fwriter.write(f)

            fobj.close()
            f.close()
                
