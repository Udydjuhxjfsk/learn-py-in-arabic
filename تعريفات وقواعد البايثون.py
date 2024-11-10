# المصدر : https://youtu.be/smKHKgedkP4?si=lBpnCvy5LhVlgRO8
# كاتب الشرح مع الاكواد : https://instagram.com/mohammad_hmadeh3
# __________________________________
# الطباعه|this print of py
print("hello world")
print(2024)
print(5+5)
print("5+5")
print('hellow world')
print("one","tow","three", sep="|")
print(10*"hello world\n")
print(True)
print(False)
print("hello\nworld")
print("hello\tworld")
# __________________________________
# التعليقات
# comment
"""
comment
"""
'''
comment
'''
# __________________________________
#المتغيرات
# variablename|اسم المتغير = value|القيمه
name = "hello world" # str|string قيمه نصيه
age = 15             # integer|int قيمه رقميه
weight = 1.80        # float عدد كسري
have_car = True     # boolean قيمه منطقيه True , False
print(name)
print(age)
print(weight)
print(have_car)
# المتغيرات2
name,age,devloper = "mhmd",18,False # هون اختصرت على حالي بدل ما اكتب لكل متغير سطر قدرت حط اكتر من متغير بسطر واحد 
print(name)
print(age)
print(devloper)
# __________________________________
# العمليات الحسابيه 
# * = الضرب 
# - = ناقص
# + = زائد
# / = تقسيم
#
#
#
print(6 - 3)
print(6 + 3)
print(6 * 3)

 # العمليات الحسابيه 

x = 10
y = 2
o = 7
i = 5
print(x + y)
print(o * i)
r = 100
t = 2
res = r / t
print(res)
# __________________________________
# عوامل المقارنه
# == != > < <= >=
print(100 < 101) # اذا كانت المعادله اللي انا كتبتا صحيحه بيكتبلي True اذا لا بيعطيني False
x = 50
y = 50
print(x == y)
# __________________________________
x = 10
x += 5  # 10 + 5 = 15 # قيمة ال اكس كانت 10 لكن اذا اضفت المتغير += سيجمعه حسب الرقم الذي اكتبه بجانبه مع المتغير الاساسي
x -= 10 # 15 - 10 = 5
x *= 5  # 5 × 5 = 25
x /= 2  # 25 ÷ 2 = 12.5
print(x)
# __________________________________
# بعض القواعد
name = 'mhmd'
name = 'hmadeh'
print(name) # هون كتبلي حماده وتجاهل كلمة محمد

test = input("enter your name: ") # انا هون خليتو انو يسمحلي اكتب بالكونسول او التيرمنال
print("your name is: " + test)

num1 = int(input("enter your num1: "))
num2 = int(input("enter you num2: "))
result = num1 + num2
print("your num1 + num2 is: " , result)
# __________________________________
# الجمل الشرطيه
x = 15
y = 10

if x > y :
    print("thats true")
elif y > x :
    print("thats wrong")
else:
    print("thats wrong 3")
    # __________________________________
# and or
    # and يعني لازم يتحققو الشرطين
    # or يعني بيمشي الحال اذا شرط واحد اتحقق بس + كمان بيمشي اذا كانو تحققو الشوطين
a = 10
b = 20

if a == 10 or b == 30 :
    print("ok")
else:
    print("not ok")

if a == 10 and b == 30 :
    print("ok")
else:
    print("not ok")
    # __________________________________
    # range(start,stop)
print(range(10))
print(range(1,10))
print(list(range(1,11)))
# __________________________________
# حلقات التكرار
start = 9
while start < 10 :
    print("raily")
    start += 1

name = "raily"
for i in name :
    print(i)

for x in range(1,10):
        print(x)
        
for i in range(1,20):
    print(i)
    if i == 8:
        print(8 , "raily")
        break
# __________________________________
# القوائم
students_name = ['ali','raily','mhmd','slm']
students_degree = [50,60,40,30]
mhmd = ['mhmd','LB',18,True]
print(students_name)
print(students_degree)
print(mhmd)
# __________________________________
