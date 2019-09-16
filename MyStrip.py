#! python

'''
strip()的正则表达式版本
'''

import re

def myStrip(text, key = None):
    '''若key没有指定，则删除text首尾的空白字符，否则删除key对应的值'''
    if key == None:
        sRegex = re.compile(r'(\s*)(\w+)(\s*)(\w+)(\s*)')
        subText = sRegex.sub(r'\2\3\4',text)
    else:
        # kRegex = re.compile(r'([d]*)([^d]+)([d]*)')
        r = r'([{}]*)([^{}]+)([{}]*)'.format(key,key,key)
        kRegex = re.compile(r)
        subText = kRegex.sub(r'\2',text)

    return subText
