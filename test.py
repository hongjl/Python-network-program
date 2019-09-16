import logging, os

os.chdir('C:\\MyPythonScripts')

logging.basicConfig(format='%(asctime)s:%(message)s',datefmt='%Y/%m/%d %H:%M:%S:',level=logging.DEBUG)
logging.debug('the message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')


"""


logging.warning('watch out')
logging.info('i told you so')
"""
