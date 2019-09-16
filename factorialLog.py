#! python3

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('start of program')

logging.disable(logging.CRITICAL)  # 禁用日志
def factorial(n):
    logging.debug('start of factorial(%s)' %(n))
    total = 1
    for i in range(n):
        total *= i+1
        logging.debug('i is '+ str(i+1)+', total is '+ str(total))
    logging.debug('end of factorial(%s)' %(n))
    return total


print(factorial(5))
logging.debug('end of program')
