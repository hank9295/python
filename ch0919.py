'''print("hello") #結尾不用加分號'''

'''var = 0 
print(type(var)) #Type可以看它的型態是什麼
print(var)

var = "0"
print(type(var))

var = 0.1
print(type(var))

var = False
print(type(var))'''

'''str = int(input("請輸入學號:")) #會把我們輸入的東西回傳給str #前面的那個int是可以把型態轉為int
print(str,end="")  #print都是自己一行 如果不想換行在後面加 ,end="" 這樣就會變成一行
print(type(str))
print("1323")'''

'''var = "hello?"
if(var == "hello"):  #:的意思是程式還沒結束
    print("nice")
elif(var == "hello?"): #else if 可以變成 elif
    print("123")
else:
    print("gg")'''

'''var = 0
while(var < 10): #判斷成立執行下面的程式 失敗跳出
    print(var)
    var+=1
print("gg")'''

'''for i in range(5,1,-2): #i是變數 range只有一個參數就是從預設0跑到設定的值 
    print(i)  '''                  #range有2個參數就是從第一個跑到第二個數的值
                                #range有3個參數就是從就是從第一個跑到第二個數的值最後一個數決定跑的範圍 +-2都可

'''arr = [0,10,20]  #一維陣列
print(arr[1])

arr = ["123"]*20
print(arr[18])'''


str1 = input("請輸入部別(1.日四技, 2.碩士班):")
if(str1 == "1"):
    var1 = "3"
elif(str1 == "2"):
    var1 = "4"
str2 = int(input("請輸入學年:"))
var2 = hex(str2 // 10)[2:] + str(str2 % 10)
var2 = var2.upper()
str3 = input("請輸入科系:(1.資工系, 2.電子系)")
if(str3 == "1"):
    var3 = "17"
elif(str3 == "2"):
    var3 = "13"
str4 = input("請輸入入學號碼:")
print("你的學號是:"+var1+var2+var3+str4)

'''var = 111  #進字轉換
print(hex(int(var/10))[2], var%10)
print(hex(var))
print(type(var))'''