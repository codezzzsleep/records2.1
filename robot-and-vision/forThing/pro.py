from threading import Thread
import requests
def get():
    while(1):
        requests.get("http://81.71.43.115:81/")
        print("finsh")
t = Thread(target=get()) # 创建线程对象
t.start() # 创建并启动线程
t.join()  # 阻塞等待回收线程