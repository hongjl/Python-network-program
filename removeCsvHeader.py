#! python3
# removeCsvHeader.py - removes the header from csv files in the current
# working directory

import csv, os

os.chdir('C:\\PDF_test_encrypt\\removeCsvHeader')
os.makedirs('headerRemoved', exist_ok = True)

# 遍历当前目录所有文件
for csvfilename in os.listdir('.'):
    if csvfilename.endswith('.csv'):  # 找到CSV文件
        print('removing header from '+csvfilename + '...')

        # 读取CSV文件，跳过第一行
        csvrows = []
        csvfileobj = open(csvfilename)
        readerobj = csv.reader(csvfileobj)
        for row in readerobj:
            if readerobj.line_num == 1:
                continue  # 跳过第一行
            csvrows.append(row)
        csvfileobj.close()
        
        # 写到文件中
        csvFile = open(os.path.join('headerRemoved',csvfilename),'w',newline='')
        writerobj = csv.writer(csvFile)
        for row in csvrows:  # 将之前的数据写入
            writerobj.writerow(row)
        csvFile.close()
        
