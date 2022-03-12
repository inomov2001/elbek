# from turtle import *
# bgcolor('black')
# speed(0)
# hideturtle()
# for i in range(220):
#     color('red')
#     circle(i)
#     color('white')
#     circle(i*0.1)
#     right(300)
#     forward(3)
# done()


# import time
# # V30
# class Odam():
#     def __init__(self, name):
#         self.name = name
#
#     def yiqilish(self):
#         print(f"{self.name} yiqildi")
#
#     def kutish(self):
#         for i in range(5):
#             print(f"{self.name} yuguryabti...")
#             time.sleep(1)
#
#     def yugurish(self):
#         print(f"{self.name} yugurishni boshladi!")
#         self.kutish()
#         self.yiqilish()
#
#
# num = Odam("Jeck")
# num.yugurish()


# V 29
# class Odam:
#     def __init__(self, ism1):
#         self.ism1 = ism1
#
#     def kuylash(self, obj):
#         print(f"{self.ism1} kuylayabti.")
#         obj.eshitish()
#         obj.gapirish()
#
#     def eshitish(self):
#         print(f"{self.ism1} eshitib qoldi... ")
#
#     def gapirish(self):
#         print(f"Buni eshitgan {self.ism1} feedback berishga o'tdi!")
#
#
# obj1 = Odam("Sodiqjon togo")
# obj2 = Odam("Jafar")
# obj1.kuylash(obj2)

# V 28
# class Player:
#     def __init__(self):
#         self.jon = 100
#         self.qurol = 15
#
#     def otish(self, dushman):
#         dushman.reduce_life(self.qurol)
#
#     def reduce_life(self, damage):
#         self.jon -= damage
#         if self.jon < 0:
#             self.jon = 0
#
#
# player1 = Player()
# player2 = Player()
# while True:
#     print(player1.jon)
#     print(player2.jon)
#
#     if player1.jon <= 0:
#         print("player2 yutdi")
#         break
#     elif player2.jon <= 0:
#         print("player1 yutdi")
#         break
#
#     ot = input("1 ni otish, 2 ni otish: ")
#     if ot == '1':
#         player2.otish(player1)
#     elif ot == '2':
#         player1.otish(player2)


# V 27
# class Odam:
#     def __init__(self,  raqam):
#         self.raqam = raqam
#
#     def tepish(self):
#         print(self.raqam, "koptokni tepdi...")
#
# class Koptok:
#     def uchish(self):
#         print("Koptok uchdi")
#
# obj1 = Odam("Zokir")
# obj1.tepish()
#
# obj2 = Koptok()
# obj2.uchish()


# V 26
# class Human:
#     adult_age = 18
#     def __init__(self, name, age, profession):
#         self.name = name
#         self.age = age
#         self.profession = profession
#
#
#
#     def is_adault(self):
#         age = self.adult_age
#         if age >= self.age:
#             return f"{self.name} Voyaga yetmagan"
#         else:
#             return f"{self.name} Voyaga yetgan"
#
#
# num1 = Human("jalol", 11, "duktor")
# print(num1.is_adault())
#
# num2 = Human("bilol", 21, "duktor")
# print(num2.is_adault())
#
# num3 = Human("odil", 18, "duktor")
# print(num3.is_adault())
#
# num4 = Human("olim", 33, "duktor")
# print(num4.is_adault())


# V 9

# class Human:
#     def __init__(self, name, age, profession, height, weight, single):
#         self.name = name
#         self.age = age
#         self.profession = profession
#         self.height = height
#         self.weight = weight
#         self.single = single
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_profession(self):
#         return self.profession
#
#     def get_heigth(self):
#         return self.height
#
#     def get_weight(self):
#         return self.weight
#
#     def get_single(self):
#         return self.single


#
# class Device():
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def number1(self):
#         pass
#
#     def number2(self):
#         pass
#
#
#
# class Computer(Device):
#     def __init__(self, acer, hp):
#         self.acer = acer
#         self.hp = hp
#
#     def computer1(self):
#         pass
#
#     def computer2(self):
#         pass
#
#
# class Phone(Device):
#     def __init__(self, iphone11, iphone13):
#         self.iphone11 = iphone11
#         self.iphone13 = iphone13
#
#
#     def iphones1(self):
#         pass
#
#     def iphones2(self):
#         pass
#
# class Desktop(Computer):
#     def __init__(self, des1, des2):
#         self.des1 = des1
#         self.des2 = des2
#
#     def desktops1(self):
#         pass
#
#     def desktops2(self):
#         pass
#
#
#
# class Laptop(Computer):
#     def __init__(self, lap1, lap2):
#         self.lap1 = lap1
#         self.lap2 = lap2
#
#     def laptops1(self):
#         pass
#
#     def laptops2(self):
#         pass
#
#
# class SmartPhone(Phone):
#     def __init__(self, smart1, smart2):
#         self.smart1 = smart1
#         self.smart2 = smart2
#
#     def smarts1(self):
#         pass
#
#     def smarts2(self):
#         pass
#
# class Tablet(SmartPhone):
#     def __init__(self, tab1, tab2):
#         self.tab1 = tab1
#         self.tab2 = tab2
#
#     def tablets1(self):
#         pass
#
#     def tablets2(self):
#         pass

# W 1

# import math
#
#
# class Son:
#     def __init__(self, nums1, nums2=None):
#         self.nums1 = nums1
#         self.nums2 = nums2
#
#     def num_kvadrat(self):
#         if self.nums2 == None:
#             print("sonning kvadrati", self.nums1 * self.nums1)
#         else:
#             print("kvadrati: siz 2 ta son kiritgansiz")
#         self.num_kub()
#         self.num_ildiz()
#         self.nums_yigindi()
#         self.nums_ayirma()
#         self.nums_kupaytma()
#         self.nums_bulinma()
#
#     def num_kub(self):
#         if self.nums2 == None:
#             print("sonning kubi", self.nums1 * self.nums1 * self.nums1)
#         else:
#             print("kubi: siz 2 ta son kiritgansiz")
#
#     def num_ildiz(self):
#         if self.nums2 == None:
#             print("sonning ildizi", math.sqrt(self.nums1))
#         else:
#             print("ildizi: siz 2 ta son kiritgansiz")
#
#     def nums_yigindi(self):
#         if self.nums2 == None:
#             print("yigindi: siz 1 ta son kiritgansiz")
#         else:
#             print("sonning yigindisi", self.nums1 + self.nums2)
#
#     def nums_ayirma(self):
#         if self.nums2 == None:
#             print("ayirma: siz 1 ta son kiritgansiz")
#         else:
#             print("sonning ayirmasi", self.nums1 - self.nums2)
#
#     def nums_kupaytma(self):
#         if self.nums2 == None:
#             print("kupaytma: siz 1 ta son kiritgansiz")
#         else:
#             print("sonning kupaytmasi", self.nums1 * self.nums2)
#
#     def nums_bulinma(self):
#         if self.nums2 == None:
#             print("bulinma: siz 1 ta son kiritgansiz")
#         else:
#             print("sonning bulinmasi", self.nums1 / self.nums2)
#
# son = Son(4)
# son.num_kvadrat()


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="database name"
)
