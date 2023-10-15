class Struct1:
    m_name = ""  #成员数据
    m_age = 0   #成员数据
    m_weight = 0   #成员数据
    def __init__(self,name,age,weight):   #类初始化函数 创建对象时  系统先自动调用它
        self.m_name = name  #将参数传递给成员
        self.m_age = age  #将参数传递给成员
        self.m_weight = weight  #将参数传递给成员
    def showInfo(self):      #成员函数
        print("name:{} ,age:{} ,weight:{}".format(self.m_name,self.m_age,self.m_weight))

obj1 = Struct1("wupeng",23,200)  #创建一个对象
obj2 = Struct1("wushitong",23,200)  #创建第二个对象

obj1.showInfo()  #调用第一个对象的函数
obj2.showInfo()  #调用第二个对象的函数

class struct2:
    def __init__():
        print()

print(dir(Struct1))   #打印成员属性

#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
#  '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
# 'm_age', 'm_name', 'm_weight', 'showInfo']
print(dir(struct2))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
#  '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


# class stu:
#     member=0
#     def __init__(self):
#         print("init stu class")

# s = stu() #
