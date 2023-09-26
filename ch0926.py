'''str = input("序號").zfill(4) #.zfill可以幫你自動補0
print(str)'''

'''import random
print(random.randint(1, 6))   #亂數產生'''

'''import random
arr = []             #list的使用
arr.append("123")    #.append新增
arr.append("456")
arr.append(random.randint(1, 6))
print(arr[0])
print(arr[1])
print(arr[2])
print(arr)

arr1 = []
arr1.append(10)
arr1.append(20)
print(arr1)
print(arr1.pop())  #pop會輸出最後輸出的那個值
print(len(arr1))  #len回傳長度或者項目個數'''

'''def hank():         #def函數應用
    print("hello")

def main(a, b):
    print(a+b) 

def test(c, d):
    sum = c + d
    return sum, c    #回傳
   # return "c + d = ", sum, c

def good(x, y):
    sum1 = x + y
    return sum1, x

hank()            #有函數的話要呼叫才會動作

main(100, 12)

print(test(5, 10))

tem, tem1 = good(10, 20)
print(tem, tem1)'''

'''a = "abc123"
print(a[1:4])  #[:]裡面的冒號可以指定你要抓的區域'''

'''var = [123]*10   #生成陣列空間
print(var)'''


import random
arr = []
arr1 = []
a = int(input("請選擇你要幾顆骰子:"))
for i in range(a):  
    i = random.randint(1, 6)
    arr.append(i)
for x in range(a):  
    x = random.randint(1, 6)
    arr1.append(x)     
#print(arr)
#print(arr1)
arr.sort()
arr1.sort()
total = sum(arr)
total1 = sum(arr1)
print(arr,total)
print(arr1,total1)





       


   
