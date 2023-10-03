'''class myname:         #class用法

    def __init__(self,name):
        self.name = name

    def printName(self):
        print("Name = " + self.name + "你好")


xxx = myname(input("請輸入第一位名字: "))
xxx.printName()

yyy = myname(input("請輸入第二位名字: "))
yyy.printName()'''

'''class myname:         #父類別(可以繼承父親所有的變數和方法)
                       #(如過子類別沒有寫建構子，那建構子會跟父親一樣)
    def __init__(self,name):
        self.name = name

    def printName(self):
        print("Name = " + self.name + "你好")

class welcome(myname): #子類別


    def sarwelcome(self):
        print("hello")

a = myname(input("請輸入第一位名字: "))
a.printName()

b = welcome(input("請輸入第二位名字: "))
b.printName() #調用父類別的方法

b.sarwelcome() #調用自己類別的方法'''

#建立自己的建構子以及使用超類別(繼承父類別建構子)
'''class myname: #父類別
    def __init__(self,name):
        self.name = name

    def printName(self):
        print("Name = " + self.name + "你好")

class welcome(myname): #子類別
    def __init__(self, name, age):  #建立自己的建構子
        super().__init__(name)   #超類別(繼承父類別建構子)
        self.age = age           #建立自己的類別變數

    def saywelcome(self):
        print (self.name,"welcome", self.age,"歲")

Judy = myname(input("請輸入第一位名字: "))
Judy.printName()

Andy = welcome(input("請輸入第一位名字: "),input("請輸入年紀"))
Andy.printName()
Andy.saywelcome()'''

'''class Animals:   #多型
    def __init__(self, animalsName):
        print(animalsName, "是動物")

class Mammal(Animals):
    def __init__(self, Name):
        print(Name, "是哺乳動物")
        super().__init__(Name)

class donotFly(Mammal):
    def __init__(self, name):
        print(name, "不能飛")
        super().__init__(name)

class donotSwim(Mammal):
    def __init__(self, name):
        print(name, "不會游泳")
        super().__init__(name)

class Cat(donotSwim, donotFly):
    def __init__(self):
        print("一隻貓")
        super().__init__("貓")

cat = Cat()
print("")
bat = donotSwim("蝙蝠")'''