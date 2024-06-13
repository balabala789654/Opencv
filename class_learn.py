
# 要理解类的含义，我们必须理解内置的 __init__() 函数。
# 所有类都有一个名为 __init__() 的函数，该函数始终在类启动时执行。
# 使用 __init__() 函数为对象属性赋值，或者创建对象时需要执行的其他操作：


# __str__() 函数控制当类对象表示为字符串时应返回的内容。
# 如果未设置 __str__() 函数，则返回对象的字符串表示形式：
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"name: {self.name} age: {self.age}"
    
    def person_fun(self): # 创建一个方法
        print("hello im " , self.name)

p1 = person("lex", 100)
print(p1.name, p1.age)
print(p1)
p1.person_fun()

# self 参数是对该类的当前实例的引用，用于访问属于该类的变量。
# 它不必命名为 self ，您可以随意命名它，但它必须是类中任何函数的第一个参数：

class animal:
    def __init__(my_animal, name):
        my_animal.name = name
    def __str__(my_animal):
        return f"im animal my name is {my_animal.name}"
    def func(my_animal):
        print("my name is ",my_animal.name)

animal1 = animal("lion")
print(animal1)
animal1.func()

# 可使用del关键字删除对象或者对象的属性
del animal1.name 


# 继承
class Student(person):
    def __init__(self, name, age, year):
        super().__init__(name, age) # super() 函数，可以让子类继承父类的所有方法和属性： 通过使用 super() 函数，您不必使用父元素的名称，它会自动从其父元素继承方法和属性。
        self.year = year

    def print_msg(self):# 可自行添加方法
        print(f"im student my name is {self.name} im {self.age}, my year is {self.year}")

Student1 = Student("lex", 90, 2022)
Student1.print_msg()

# 迭代器
# 从技术上讲，在Python中，迭代器是一个实现迭代器协议的对象，它由方法 __iter__() 和 __next__() 组成。

# 要创建一个对象/类作为迭代器，您必须为您的对象实现方法 __iter__() 和 __next__() 。
class my_num:
    def __init__(self, num):
        self.num = num

    def __iter__(self): # __iter__() 方法的行为类似，您可以执行操作（初始化等），但必须始终返回迭代器对象本身。
        return self

    def __next__(self): # __next__() 方法还允许您执行操作，并且必须返回序列中的下一项。
        if self.num < 100:
            x = self.num
            self.num +=1
            return x
        else:
            raise StopIteration # 为了防止迭代永远持续下去，我们可以使用 StopIteration 语句。

num1 = my_num(10)
num1_iter = iter(num1)

for x in num1_iter: # 使用 for 循环来迭代可迭代对象：   
    print(next(num1_iter))



# 多态
class vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"{self.name}")

class car(vehicle):
    def move(self):
        print("car")

class plane(vehicle):
    def move(self):
        print("plane")

class boot(vehicle):
    def move(self):
        print("boot")

car1 = car("car1")
plane1 = plane("plane1")
boot1 = boot("boot1")
for x in [car1, plane1, boot1]:
    x.move()