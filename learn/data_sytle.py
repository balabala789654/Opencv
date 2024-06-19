import random

# int
x1 = 10
x2 = -100202
x3 = 23424234234
print(x1, "x1 type: ", type(x1),"\n",  x2, "x2 type: ", type(x2),"\n", x3, "x2 type: ", type(x3))

# float
# 浮点数也可以是带有“e”的科学数字，表示 10 的幂。
a1 = 1.12312312
a2 = -1.23232323
a3 = 13e8
print(a1, "\n", a2, "\n", a3, "\n")

#complex
b1 = 2j
b2 = 1+9j
b3 = -9j
print(b1, type(b1))
print(b2, type(b2))
print(b3, type(b3))

# 类型转换
c1 = int(a2)
c2 = float(x2)
c3 = complex(a2)
print(c1, type(c1))
print(c2, type(c2))
print(c3, type(c3))

# 随机数
print(random.randrange(1,3))

# 铸造
d1 = float("3.4")
d2 = int("3")
print(d1, d2)

# 字符串 
# 可使用3个引号表示多行字符串
e1 = """data_sytle.py
jasdklasdjalsdaksd
alsdjklajskldklajsd
"""
print(e1, "\n", e1[random.randrange(1, len(e1))]) #字符串本质是数组 可用方括号访问字符串元素

for x in e1:
    print(x) #可使用循环遍历数组中的元素

print(len(e1)) #使用len函数可获取字符串长度

e2 = "the best things in life are free"
print("free" in e2) #要检查字符串中是否存在某个短语或字符，我们可以使用关键字 in  返回的为布尔值

if "free" in e2: #可以if语句进行判断
    print("yes!!!\n")

print("aaa" not in e2) #要检查字符串中是否不存在某个短语或字符，我们可以使用关键字 not in 。返回的为布尔值
if "aaa" not in e2: #可以if语句进行判断
    print("yes!!!\n")


# 切片字符串

print(e2[1:8])
print(e2[1:random.randrange(1,len(e2))]) #在指定范围切片
print(e2[:random.randrange(1,len(e2))]) #从头开始切片
print(e2[random.randrange(1,len(e2)):]) #在指定位置切片到最后

#返回大小写字符串
e3 = " a ls djl asd "
e4 = " A DAS DASF G G "
print(e3.upper()) #返回大写
print(e4.lower()) #返回小写

# 删除开头和结尾的空格
print(e3.strip())

# 替换
print(e3.replace("a", "L"))

# 分割字符串
e5 = "hasd,asdf"
e6,e7 = e5.split(",") #返回为list类型
print(e5.split(","), type(e5.split(",")))
print(e6)
print(e7)

# 连接字符串
e8 = e6 + e7
e9 = e6 +" add "+e7
print(e8)
print(e9)

# F-Strings
age = 100
txt1 = f"my name is lex, im {age}"
print(txt1)
txt2 = f"my name is lex, im {age:.3f}"
print(txt2)
txt3 = f"my name is lex, im {13*317}"
print(txt3)

