def welcome():
   print("welcome to my program")
welcome()
def test2():
   x = 2
   y = 3
   result = x + y
   print(result)
test2()
def test3():
   pass
print('hi')

def test4(name,job):
   print(name)
   print(job)
test4("mhmd","developer")

def math(n1,n2):
   print(n1+n2)
math(5,6)

def globall():
   global name2
   name2 = "global"

def globall2():
   globall()
   print(name2)
globall2()