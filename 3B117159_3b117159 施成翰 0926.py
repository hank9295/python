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
arr.sort()
arr1.sort()
total = sum(arr)
total1 = sum(arr1)
num = None
var = 0
sum = None
har = 0
a1 = 0
a2 = 0
'''for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        if num is None or arr[i] < num:
            num = arr[i]
            print(num)
        elif arr[i] == num:
            var += arr[i]'''
for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        if num is None:
            num = arr[i]
            var = arr[i]
        elif arr[i] == num:
            var += arr[i]
for i in range(len(arr1) - 1):
    if arr1[i] == arr1[i + 1]:
        if sum is None:
            sum = arr1[i]
            har = arr1[i]
        elif arr1[i] == sum:
            har += arr1[i]  

def toto():
    a1 = num + var
    a2 = sum + har
    if (total-a1) > (total1-a2):
        print("老闆:",arr,(total-a1))
        print("顧客:",arr1,(total1-a2))
        print("老闆贏")
    elif (total-a1) < (total1-a2):
        print("老闆:",arr,(total-a1))
        print("顧客:",arr1,(total1-a2))
        print("顧客贏")
    elif (total-a1) == (total1-a2):
        print("老闆:",arr,(total-a1))
        print("顧客:",arr1,(total1-a2))
        print("平手再來一次")

if num == None:
    a2 = sum + har
    print("老闆:",arr,(total),"順子沒點")
    print("顧客:",arr1,(total1-a2))
    print("老闆輸")
elif sum == None:
    a1 = num + var
    print("老闆:",arr,(total-a1))
    print("顧客:",arr1,(total1),"順子沒點")
    print("顧客輸")
else:
    toto()

