import PyPDF2, os

# 将当前目录所有PDF文件组成一个大的文件

os.chdir('C:\\MyPythonScripts')

pdfs = [file for file in os.listdir() if file.endswith('.pdf')]



for file in pdfs:
    pdffileobj = open(file,'rb')
    pdfreader = PyPDF2.PdfFileReader(pdffileobj)
    pdfwriter = PyPDF2.PdfFileWriter()  # 一个文件用一个writer对象，这样才不会使拷贝的数据空白页

    for pagenum in range(pdfreader.numPages):
    	pdfwriter.addPage(pdfreader.getPage(pagenum))

    pdfoutput = open('file1.pdf','ab')
    pdfwriter.write(pdfoutput)
    
    pdfoutput.close()
    pdffileobj.close()



