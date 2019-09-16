#! python3
# readDocx.py - 获取.docx文件中完整的文本

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append('  '+para.text)  # 添加缩进
        # fullText.append(para.text)  # 获取每一个paragraph的文本
    return '\n'.join(fullText)
