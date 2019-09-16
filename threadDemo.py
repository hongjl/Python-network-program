import threading, time
print('start of program.')

def takeANap():
    time.sleep(5)
    print('wakeup!')

threadobj = threading.Thread(target=takeANap)
threadobj.start()
threadobj.join()  # 添加这行代码后，让其他线程执行完后，才执行主线程的代码

print('end of program.')
