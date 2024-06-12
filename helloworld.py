import sys

if 5 > 2:
    print(sys.version)

print("helloworld!!!")

x = 100
y = "Im a var"

print(x, "aaa\n",y)

# 注释方法
"""
helloworld.py
"""
##

# 强制转换
a = str(3)
print(a, type(a))
a = int(3)
print(a, type(a))
a = float(3)
print(a, type(a))

# 字符变量可用单引号与双引号
b1 = "Johan"
b2 = 'johan'
print(b1,b2)

"""
变量名必须以字母或下划线字符开头
变量名不能以数字开头
变量名称只能包含字母数字字符和下划线（A-z、0-9 和 _）
变量名区分大小写（age、Age 和 AGE 是三个不同的变量）
变量名不能是任何 Python 关键字。

与c语言类似
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# 多值分配
c1, c2, c3 = "a", "b", "c"
print(c1, c2, c3)

c1 = c2 = c3 = "var"
print(c1,c2,c3)

fruits = ["ori", "apple", "cherry"]
c1,c2,c3 = fruits
print(c1,c2,c3)

# 输出
d1 = "hello"
d2 = "world"
print(d1,d2) #加逗号会自动加空格
print(d1 + d2)#使用+号不会加空格

d3 = 1
d4 = 5
print(d3 + d4)
print(d3,d4)

d5 = 2
d6 = "a"
print(d5,d6)
# print(d5 + d6) 两个变量不同类型时不可以使用+号

# 全局变量
var = "awesome" #在函数外的变量为全局变量

def func():
    print("python is " + var)

func()

def func1():
    global var1 #在函数内部的变量为局部变量 让局部变量变成全局变量 使用global即可
    var1 = "great" 
    print("python is " + var1)

func1()

print("python is " + var1)
