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