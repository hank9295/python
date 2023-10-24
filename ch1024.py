'''import threading
import time

def job():   #子執行緒的工作函數
    for i in range(5):
        print("Child thread: %d " %(i))
        time.sleep(1)

t = threading.Thread(target = job)  #建立一個執行緒

t.start()  #執行
time.sleep(0.5)  

for i in range(3):  # main thread
    print("Main thread: %d " %(i))
    time.sleep(1)

#等t做完
t.join()
print("Done.")'''

'''import threading
import time

#子執行緒的工作函數
def job(num):
    print("Thread", num)
    time.sleep(1)

#建立4個執行緒
threads = []
for i in range(4):
    threads.append(threading.Thread(target = job, args = (i,)))
    threads[i].start()

#繼續執行主執行緒

#等待所有子執行緒結束
for i in range(4):
    threads[i].join()

print("Done.")'''

'''import threading
import time

#子執行緒類別
class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("Thread", self.num)
        time.sleep(1)

#建立4個執行緒
threads = []
for i in range(4):
    threads.append(MyThread(i))
    threads[i].start()

#繼續執行主執行緒

#等待所有子執行緒結束
for i in range(4):
    threads[i].join()

print("Done.")'''

'''import time
import threading
import queue

#worker 類別，負責處理資料
class Worker(threading.Thread):
    def __init__(self, queue, num):
        threading.Thread.__init__(self)
        self.queue = queue
        self.num = num
    
    def run(self):
        while self.queue.qsize() > 0:
            #取得新的資料
            msg = self.queue.get()

            #處理資料
            print("Worker %d: %s" % (self.num, msg))
            time.sleep(1)

#建立Queue
jobs = queue.Queue()

#將資料放入Queue
for i in range(10):
    jobs.put("Data %d" % i)

#建立2個員工
worker1 = Worker(jobs, 1)
worker2 = Worker(jobs, 2)

#開始工作
worker1.start()
worker2.start()

#等所有工作做完
worker1.join()
worker2.join()

print("Done.")'''

'''import time
import threading
import queue

class Worker(threading.Thread):
    def __init__(self, queue, num, lock):
        threading.Thread.__init__(self)
        self.queue = queue
        self.num = num
        self.lock = lock
    
    def run(self):
        while self.queue.qsize() > 0:
            msg = self.queue.get()
            #取得lock
            self.lock.acquire()
            print("Lock acquired by Worker %d" % self.num)
            
            #不能讓多個執行緒同時進的工作
            print("Worker %d: %s" % (self.num, msg))
            time.sleep(1)
            
            #釋放lock
            print("Lock released by Worker %d" % self.num)
            self.lock.release()
            
jobs = queue.Queue()
for i in range(5):
    jobs.put("Data %d" % i)
    
#建立lock
lock = threading.Lock()
worker1 = Worker(jobs, 1, lock)
worker2 = Worker(jobs, 2, lock)

worker1.start()
worker2.start()

worker1.join()
worker2.join()

print("Done.")'''

score = {"James":100, "Robert":90, "Peter":30}
print("James score :", score["James"])
#新增
score["Mary"] = 70
print("Mary score :", score["Mary"])
#刪除
del score["James"]
print(score)
#尋找
print(score.get("James"))#回傳 None
print(score.get("Mary"))
#轉json
import json
print(json.dumps(score))
#clear
score.clear()
print(score)