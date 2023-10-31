import threading
import time
totalLen = 0
#子執行序類別
class player(threading.Thread):
    def __init__(self, name, speed, breakTime):
        threading.Thread.__init__(self)
        self.speed = speed
        self.breakTime = breakTime
        self.name = name
        self.curr = 0

    def rum(self):
        while(self.curr < totalLen):
            self.curr += self.speed
            print("%d跑到 %d..." %(self.name, self.curr))
            time.sleep(self.speed)
        print("%s跑到終點..." %(self.name))

count = int(input("請輸入人數:"))
totalLen = int(input("請輸入距離:"))
print("請輸入選手資訊:")
players = []
for i in range(count):
    arr = input().split(" ")
    players.append(player(arr[0], int(arr[1]), int(arr[2])))

for p in players:
    p.start()

for p in players:
    p.join()

print("比賽結束!!!")