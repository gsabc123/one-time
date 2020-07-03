#!/usr/bin/env python
# coding: utf-8

# In[18]:


#声明的三种格式
  #格式一
s1 = "123"
a, b, c ="11","123","13"

print(s1,s,a,b,c)


# # 变量类型
# - 严格意义上来讲，Python只有一个类型
# - 标准数据类型六种
#     - 数字Number
#     - 字符串类型 str
#     - 列表 list
#     - 元组 tuple
#     - 字典 diet
#     - 集合 set
# 
# 

# # 数字类型 Number
#   - Python中的数字没有大小限制
#  # 常见数字分类
#  - 整数
#      - 没有小数部分
#      - 包含正数，负数，0
#      - 二进制
#          - 只有01
#          - 以0b开头的01串
#          - 例如
#              - 0b110
#              - 0b11110
#      - 八进制
#          - 以0o开头的0到7之间的数字串
#          - 例如：
#              - 0o71
#      - 十六进制
#          - 以0x组成的由0-9，a-f构成的串
#   
#  - 浮点数
#      - 就是通俗意义的小数量
#      - 常见案例格式
#          - 3.14159
#          - 3.
#          - 0.4
#          - .4
#  
#  - 科学技术法
#      - 定义和数学定义一致
#      - 写法就是e后面跟整数用来表示10的整数
#  
#  - 复数
#   - 和数学上的定义一致
#   - 复数的虚部用j/J表示
#   - 例如
#       - 5+4j
#       - 4j
#       

# # 布尔值
# - 布尔值就是用来表示真假的值 
# - 有两个值：True/False
# - 在Python中，布尔值可以当数字使用
#     - 布尔值如果当数字使用，True = 1，False = 0
#     - 如果数字用来当作布尔值使用，0 = False，其余当作True
# 

# In[30]:


# 布尔值当数字用
age = 18 + True
print(age)
age1 = 18 + False
print(age1)
#判断语句
a = -1
if a :
    print("负数是True")
else:
    print("负数是False")


# # 字符串
# - 表达文字信息的内容，比如“我爱王晓静”
# - 形式上是引号引起来的一段内容
# - 引号包括 （单双一样）
#     - 单引号
#     - 双引号
#     - 三引号，可以用来表示多行信息
#  

# In[2]:


# 字符串案例
love = 'woaiwangxiaojing'
print(love)
# 三引号可以表示多行
love1 = '''
wo 
ai 
wang
xiao
jing


'''
print(love1)
# 单双引号只能引用一行


# # None类型
# - 表示没有，通常用来占位
# - 比如返回，用来表示返回一个空
# 

# # 表达式
# - 由一个或者几个数字或者变量或者运算符合成的一行代码
# - 通常返回一个结果
# # 运算符
# - 由一个以上的值经过一系列的运算得到新值的过程就叫运算
# - 用来操作运算的符号叫运算符
# - 运算符分类
#     - 算数运算符
#     - 比较或者关系运算符
#     - 赋值运算符
#     - 逻辑运算符
#     - 位运算 
#     - 成员运算符
#     - 身份运算符

# # 算数运算符
# - 用来表示算数运算的符号
# - 通常用来表示加减乘除
# - Python没有自增自减运算符

# In[12]:


# 算数运算符案例
#加减乘除跟数学意义基本一致
a = 9 - 2
print(a)
# Python除法分为普通除法，地板除，取余
# 正常的除法
# 此操作符在Python2.x和Python3.x中有些不同
a = 9 / 2 
print(a)
# 除以负数的结果
a = 9 / -4
print(a)
# 地板除(取整除)
a = 9 // 2
print(a)
# 取余

a = 9 % -4
print(a)


# # 比较运算符
# - 对两个内容进行比较的运算符
# - 最终结果一定是布尔值，即True/False

# In[6]:


# 等于 ==
a = 3 == 4
print(a)
# 不等于  ！=
1 != 2
# 其他的符号是
# >,>=,<,<=
print(3 <= 4)


# # 赋值运算符
# - 把一个值放到变量里边去
# 
# 

# In[4]:


# 赋值符号 =
a = 9
# 复杂一点的
a = b = 9
# 赋值的缩写
c = 1
c = c + 3
print(c)
# 注意下面符号仅仅是一个缩写
c += 3 # c = c + 3
print(c)
# 所有数学运算符都可以缩写
# -=，*=，/=，//=，%=，**=，都是缩写形式
# Python 里没有++，--


# In[1]:


# 逻辑表达举例
a,b,c = True,True,False
aa,ac = a and b,a or c
print(aa,ac)


# # 逻辑运算符
# - 对布尔类型变量或者值进行运算的符号
# - and：逻辑与
# - or ：逻辑或
# - not：逻辑非
# - Python里面的逻辑运算没有异或 
# - 运算规则：
#     - and看做乘法，or看做加法
#     - True看做1，False看做0
#     - 则逻辑运算就能转换成整数数学运算
#     - 最后结果如果是0则为False，否则为True
# - 逻辑运算的短路问题
#     - 逻辑运算式，按照运算顺序计算，一旦能够确定整个式子未来的值，则不再计算，直接返回
# 

# In[6]:


# 短路问题案例1
a,b,c = True,True,False
ab = a or b and (a and c)# 转换成算数1 + .......结果一定大等于1，也就是一定为true
print(ab)


# In[ ]:


# 短路问题案例2
# 运行a得到打印a和true，运行b得到打印b和true
# 那么，令ab = a or b 打印ab 只会得到a和true，因为b没有运行


# # 成员运算符
# - 用来检测一个值或者变量是否在某个集合里面
# - in：成员运算符
# - not in：不在里边的意思

# In[7]:


# in 案例
L = [1,2,3,4,5]
a = 6
aa = a in L 
print(aa)


# # 身份运算符
# - 用来两个变量是否是同一个变量
# - is：变量运算符
# - is not ：不是

# In[12]:


# 身份运算符定义
a = 1
b = 1864354
ab = a is b
print(ab)
# a,b仅仅是值一样，并不代表a，b是同一个变量
a = 1864354
b = 1864354
ab = a is b
print(ab)
# 正确理解上下案例不同之处
'''一些小的数字，Python默认分配了内存地址，定义a = 5时，Python并不会再开辟出一处空间
而是把a指向5，同理，把b也指向5，这样a与b所指的内存地址相同，a is b就是true了'''
# 默认分配了内存地址的数字有[-5,256]，解释器对他们做了单独的处理，放进了固定的内存中
# 不因你每次运行而变化
a = 5
b = 5
ab = a is b
print(ab)


# # 运算符优先级问题
# - 小括号具有最先优先级
# - 

# # 字符串乘以数字，表示这个字符串重复多少遍

# # 程序结构
# - 程序三种结构
#     - 顺序
#     - 循环
#     - 分支

# # 分支结构
# - 分支结构基本语法
#     if 条件表达式：
#         语句1
#         语句2
#         语句3
#         ....
# - 条件表达式就是计算结果必须为布尔值的表达式
# - 表达式后面的冒号不能少
# - 注意if后面的出现的语句，如果属于if语句块，则必须同一个缩进等级
# - 条件表达式结果为true执行if后面的缩进的语句块
# 

# In[4]:


# if 语句联系
# 如果你们都买我的习题课，我就发财了
# 字符串里面有内容则为真，无内容就是假，空格不是无内容
a = "都买习题课"
if a:
   print("我就发财了")
   print("迎娶白富美")
else:
   print("继续吃土吧")
   print("继续努力吧")
print("日子还得过呀")


# In[3]:


grade = input("请输入你的成绩：")
if int(grade) >= 90:
    print("不愧是我的学生")
    incom = input("你爸一年多少收入啊：")
    if int(incom) <= 100000:
        print("你父母供你读书不容易，继续努力吧！")
    if 100000 < int(incom) <= 300000:
        print("空闲时间报个业余兴趣班，培养点爱好。")
    if 300000 < int(incom) <= 10000000:
        print("平时报个兴趣班，补课班，多吃些营养品。")
    if  int(incom) > 1000000:
        affection = input("你爸妈感情咋样")
        if affection == "不好":
            print("明天叫你爸来学校一趟")
        if affection == "好":
            print("你妈不在家的时候告诉我，我要家访")
    
if 80 <= int(grade) < 90:
    print("继续努力啊")
if 70 <= int(grade) < 80:
    print("你的加把劲啊")
if 60 <= int(grade) < 70:
    print("再不努力就滚犊子吧！")
if int(grade) < 60:
    print("滚犊子吧！你不配做老子的学生！！！")


# In[ ]:





# # 循环语句
# - 重复执行某一个固定的动作或者任务
# - 分类
#     - for
#     - while
# # for循环
# - 语法
#    for 变量 in 序列
#        语句1
#        语句2
#        ...

# In[2]:


# 列表知识以后会讲
# 比如[1,2,3,4,5,6,7]
list_one = [1,2,3,4,5,6,7]
for shuzi in list_one:
    print(shuzi)
    print(shuzi+100)
    print(shuzi+1000)


# In[18]:


# 打印学生列表姓名
# 如果是jingjing，那肯定是我的最爱呀。
# 如果是别的学生，那要冷酷的拒绝他。
 
'''stu_list = ['王晓','小明','小李']

for stu in stu_list:
    if stu == "小明":
        print("l love you ")'''
stu_list2 = ['小韩','小丽','小讷']
for stu in stu_list2:
    if stu =="小丽":
        print("小丽你去了哪里")
    else:
        print("拜拜了您嘞")
        


# # for-else语句
# - for循环结束的时候，有时候需要执行一些收尾的工作，此时需要使用else语句
# - else语句是可选
# 

# In[19]:


# for-else语句
# 打印列表中的同学
# 如果没有在列表中，或者列表结束了，我们需要打印提示语句，表示不再爱了
stu_list2 = ['小韩','小丽','小讷']
for stu in stu_list2:
    if stu =="小丽":
        print("小丽你去了哪里")
    else:
        print("拜拜了您嘞")
else:
    print("不会再爱了")
    


# # break，continue，pass
# - break：无条件结束整个循环，简称循环猝死
# - continue:继续
# - pass：只是占位符号,代表这句话啥也不干，没有跳过功能

# In[24]:


# 确定一个数字列表中是否有数字7
# 确定是否包含后就结束。
dig_list = [1,5,78,9,6,8,7,9,57]
for dig in dig_list:
    if dig == 7:
        print("哈哈哈哈哈，老子终于找到你了")
        break
    else:
        print(dig)
        


# In[1]:


# continue语句练习
# 在数字1-10中，寻找所有偶数，找到偶数后打印偶数
'''
# continue 案例1

dig_list = [1,2,3,4,5,6,7,8,9,10]
for dig in dig_list:
    if dig % 2 == 0:
        print (dig)
        print ("哈哈，你是个双的")
    else:
        continue
'''
# 此段代码跟上面代码等价
# continue 立即结束本轮循环，进入下一轮循环
dig_list = [1,2,3,4,5,6,7,8,9,10]
for dig in dig_list:
    if dig % 2 == 0:
        print (dig)
        print ("哈哈，你是个双的")
    else:
        continue


# In[3]:


# pass 案例1
age = 19
if age > 19 :
    pass
else:
    print("你还小")


# In[4]:


# pass案例2

ages = [2,3,45,48,12,36,42]
for age in ages:
    pass
    print(age)


# # range函数
# - 生成有序数列
# - 生成数字队列可以定制

# In[6]:


# range案例1
# 生成一个从1到100的数字序列
# range的生成序列是左包括右不包括
dig_list = range(1,101)
for dig in dig_list:
    print(dig)
    
# 一般在python中，连个表示范围的数字都是左包括右不包括，randint函数是个特例
# range函数在Python2和3中有很大差别


# In[7]:


# range 案例3
# 打印1-9的数字
for i in range(1,10):
    print(i)


# # while 循环
# - 一个循环语句 
# - 表示当条件成立的时候，就循环， 适用于不知道具体循环次数，但能确定在某个条件成立的时候，就循环
# - while语法
#    while 条件表达式:
#        语句块
#        #另外一种表达方法
#    while 条件表达式:
#        语句块1
#     else:
#        语句块2
#        

# In[25]:


# 如果说年利率是6.7%，本利是每年翻滚，则多少年后本钱会翻倍

n = 0
a = 10
while  a < 20:
    n = n + 1
    a = a * (1+0.067)
print(n)
# 年利率案例2
# 本案例中循环体没有被执行，why？如何改正
n = 0
a = 10


# # 函数
# - 函数是代码的一种组织形式
# - 函数应该能完成一项特定的工作，而且一般一个函数只完成一项工作
# - 有些语言，分函数和过程两个概念，通俗解释是，有返回结果的叫函数，无返回结果的叫过程.python不加以区分
# - 函数的使用
#     - 函数的使用需要先定义
#     - 使用函数，俗称调用

# In[3]:


# 定义一个函数
# 只是定义的话不会执行
# 1，def关键字，后跟一个空格
# 2，函数名，自己定义，起名需要遵循便令命名规则，约定俗成，大驼峰命名只给类用
# 3，后面括号和冒号不能省，括号内可以有参数
# 4，函数内所有代码缩进




def func():
    print("我是一个函数")
    print("爱生活，爱自由，爱篮球")
print("函数结束了")


# In[4]:


# 函数的使用
# 直接写出函数名字，后面小括号不能省略，括号内内容根据情况
func()


# # 本课程内容
# - 函数讲完参数
# - str
# - list.tupe.set.map

# In[ ]:


# 函数定义
def func():
    print("你是大傻子")


# In[5]:


func()


# # 函数的参数和返回值
# - 参数：负责给函数传递一些必要的数据或者信息
#     - 形参（形式参数）：在函数定义的时候用到的参数，没有具体值，只是一个占位符号
#     - 实参（实际参数）：在调用函数的时候输入的值
# - 返回值：调用函数的时候的一个执行结果
#     - 使用return返回结果
#     - 如果没有值需要返回，使用return None表示函数结束
#     - 函数一旦返回执行return，则函数立即结束
#     - 如果函数没有return关键字，则函数默认返回None

# In[7]:


# 形参和实参的案例
# 参数person只是一个符号
# 调用的时候用另一个
def hello(person):
    print("{0},你好么?".format(person))
    print("{},你看见我家那谁了么?".format(person))
    
    
p = "小明"
# 调用函数，需要把p作为实参传入
hello(p)


# In[8]:


p = "小五"
hello (p)


# In[2]:


def hello(person):
    print("{0},你是个大傻子哦".format(person))
    print("{},不，你是大侄子".format(person))
p = "大傻子哦"
hello(p)


# In[4]:


# help负责随时为你提供帮助
help(None) # 等价于help(print())，为什么捏？


# In[11]:


# 九九乘法表
# version 1.0
for o in range(1,10):# 控制外循环，从1到9
    for i in range(1,o + 1):#内循环，每次从第一个数字开始，打印到跟行数相同的数量
        print(o * i,end = "  ")
    print()
    


# In[7]:


# 九九乘法表
for i in range(1,10):# 外循环  控制行数
    for o in range(1,i + 1):# 内循环
        print(i * o,end = "  ")
    print()


# In[17]:


# 尝试用函数来打印九九乘法表
def a():
    for i in range(1,10):
        for o in range(1,i + 1):
            print(i * o,end = "  ")
        print()
    return None
a()
a()


# In[69]:


# 改造上面的函数

def printLine(a):
    for b in range(1,a +1):
        print(a * b,end= "  ")
    print()
       
           
            

    
'''
line_num：行号


打印一行九九乘法表
'''
def a():
    for i in range(1,10):
        printLine(i) 
    return None
a();a()


# In[3]:


def a(line_num):
    for i in range(1,line_num + 1):
        print(line_num * i,end="  ")# end 与赋值符号之间没空格
    print()
a(2)


# # 参数详解
# - 参数分类
#     - 普通参数
#     - 默认参数
#     - 关键字参数
#     - 收集参数
#     

# In[7]:


# 普通参数案例
def normal_para(one, two, three):
    print(one + two)
    return None
normal_para(1, 2, 3)


# In[11]:


# 默认参数案例
def default_para(one, two, three=100): # three = 100为默认参数
    print(one + two + three)
    return None
default_para(120,3)
# g引用函数时给第三个值 那就用给的第三个值  不给就用默认的值


# In[16]:


# 关键字参数

def keys_para(one, two, three):
    print(one + two)
    print(three)
    return None
keys_para(two=2,one=1,three=32)


# # str字符串
# - str
# - 转义字符
# - 格式化
# - 内建函数

# # 字符串
# - 表示文字信息
# - 用单引号，双引号，三引号括起来

# In[17]:


s = '你是大傻子'
print(s)


# In[18]:


s = "你是大傻子"
print(s)


# In[19]:


s = '''
你
是
大
傻
子'''
print(s)


# # 转义字符
# - 用一个特色的方法表示出一系列不方便写出的内容，比如回车键，换行符，退格键
# - 借助反斜杠字符，一旦字符串中出现反斜杠，则反斜杠后面一个或者几个字符表示已经不是原来的意思了，进行了转义
# - 在字符串中，一旦出现反斜杠就要加倍小心，可能有转义字符出现
# - 不同操作系统对换行操作有不同的表示
#     - windows：\n
#     - Linux: \r\n

# In[31]:


# 转义字符的案例
# 想表达Let’s Go
# 使用转义字符
s = 'Let\'s GO'
print(s)



# 使用单双引号嵌套
s =   "Let's GO"
print(s)

# 表示斜杠
# 比如表示C:\User\aasd
s = "C:\\User\\aasd"
print(s)


# 回车换行
# 想表达的效果是 一直换行
# windows 下也可以使用\r\n，效果相同
s = "你\n是\n大\n傻\n子"
print(s)


# # 常用的转义字符
# - 自己百度

# In[3]:


# 单个斜杠的用法
# 在python里，单个反斜杠表示此行未结束，出于美观，需要下一行继续
# 理论上应该写成一行，出于美观，写成如下。
def myDemo(x,            y,            z):
    print("哈哈哈哈")
    return None
myDemo(1,2,3)


# # 格式化 
# - 把字符串按照一定的格式进行打印或者填充
# - 格式化的分类
#     - 传统格式化
#     - format
# 

# # 字符串的传统格式化方法
# - 使用%进行格式化
# - %(百分号)也叫占位符
#     %s：字符串
#     %r：字符串，但是是使用repr而不是str
#     %c：整数转换为单个字符
#     %d：十进制整数
#     %u：无符号整数
#     %o：表示八进制
#     %x：十六进制
#     %X：十六进制
#     %e：浮点数，如3.87e+12
#     %E：浮点数，如3.87e+12
#     %f,%F:浮点数十进制形式

# In[18]:


# %s表示简单的字符串
# 占位符可以单独使用
s = "I love %s"
print(s)
print(s%"大傻子")
print(s%"大憨批")


# In[20]:


s = "我爱%s"
print(s%"大傻子")


# In[22]:


print("我爱%s"%"大傻子")
# 占位符一般只能被同类型替换，或者替换类型能被转换成占位符的类型
print("我爱%s"%"100")


# In[24]:


s = "刘大拿同学今年%d岁了"
print(s%100)


# In[27]:


s = "我是%fKG weight,%fcm Heigh"
print(s)
# 如果需要格式化的信息多于一个，则用括号括起来就可以
# 以下打印使用了默认格式，多打出了好多个零
print(s%(76.45,1.84))

# 实际需要进行格式化的信息的数量必须与百分号后面给出的数据数量匹配，否则报错
#实际需要格式化的为4处，但是给出的数据只有3个，所有报错
s = "我是%.2fKG weight,%f.2cm Heigh"
print(s%(76.45,1.84))


# In[16]:


# 填充
s = "你是大傻子"
print(s)
s = "你是大憨批"
print(s)
s = "你是大nt"
print(s)


# 自己预测
def taolu(a):
    print("{0},你是我最爱的人啊".format(a))
    return None
b = "大傻子"
taolu(b)

    


# # format格式化
# - 使用函数形式进行格式化，代替以前的百分号

# In[3]:


# 不用指定位置，按顺序读取
# 方式1
s = "{} {}！"

print(s.format("Hello","Wold"))
# 方式二
s = "{} {}".format("Hello","world")
print(s)
# 以下内容，建议听完后面函数参数再来看，效果更佳
# 设置指定位置

s = "{0} {1}".format("Hello","world")
print(s)
# 设置指定位置

s = "{1} {1}".format("Hello","world")
print(s)
# 设置指定位置
s = "i love {0} and {0} loves me".format("哈哈哈哈")
print(s)
# 下面案例报错，跟上面案例进行对比
# s = "i love {} and {} loves me".format("哈哈哈哈")
print(s)
# 使用命名参数
s = "我们是{school_name},我们的网址是{url},{teacher}最帅"
s = s.format(school_name="北京图灵学院",url="www.tulingxueyuan.com",teacher="刘大拿")
print(s)


# In[5]:


# 通过字典设置参数，需要解包
# 使用命名参数
s = "我们是{school_name},我们的网址是{url},{teacher}最帅"
s_dict ={"school_name":"北京图灵学院",         "url":"www.tulingxueyuan.com",         "teacher":"刘大拿"}
# **是解包操作，后面会讲到
s = s.format(**s_dict)
print(s)


# In[9]:


# 对数字的格式化需要用到
s = "geng shu is {:.2f}m high,{:.2f}kg weight"
print(s.format(1.84,85))


'''
^,<,>分别是居中，左对齐，右对齐，后面带宽度
:后面带填充的字符，只能是一个字符，不指定则默认是用空格填充
+ 表示在正数前显示+ ，负数前显示-：（空格表示在正数前加空格）
b d o x 分别是二进制 十进制 八进制 十六进制
此外我们可以使用大括号{}来转义大括号


'''

s = "format是使用{}来进行占位的"
print(s)


# # str内置函数
# ### 查找类函数
# - 很多语言字符串使用string表示，但是Python中用str表示字符串
# - 字符串查找类：find，index，islower  （is开头是大多是判断）
# - find：查找字符串中是否包含一个子串
# - index；与find的区别是index查找不到会报错
# - rfind，lfind：从左开始查找和从右开始查找

# In[5]:


s = "你是大傻子和大憨批"
s1= "大傻子"
# 返回第一次发现这个字符串的位置
s.find(s1)
# 返回-1表示没有找到
s2 = "Wanwan"
s.find(s2)
# index没找到会报错或者引发异常
s.index(s2)


# In[11]:


# 使用的时候还可以使用区间
s = "你是大傻子和小傻子"
s1= "傻子"

# 从下表5开始找，看能否找到
s.find(s1,5)


# In[ ]:





# In[4]:


help(str.index)


# ### 判断类函数
# - 此类函数特点是一般都用is开头，比如islower
# - isalpha：判断是否是字母，需要注意的是两点:
#      - 此函数默认的前提是字符串至少包含一个字符，如果没有，同样返回false
#      - 汉字被认为是alpha，所以，此函数不能作为区分英文字母还是汉字的标识，区分中英文用unicode码。
#      - 注意使用区别，防止被坑
# - isdigit，isnumeric，isdecimal三个判断数字的函数
#      - 三个函数的区别自己百度 
#      - 此类函数不建议使用，在后期爬虫中，判断是否是数字建议使用正则表达式的方式
# - islower：判断是否是大写或者小写

# ### 内容判断类
# - startswith/endswith:是否以xxx开头后者结尾
#     - 检测某个字符串是否以某个子串开头，常用三个参数
#     - suffix：被检查的字符串，必须有
#     - start：检查范围的开始范围
#     - end：检查范围的结束范围
# - islower/isupper:判断字符串是否是大写或者小写

# ### 操作类函数
# - format：格式化用的(特别常用)
# - strip：这个函数主要作用是删除字符串两边的空格，其实这个函数允许你去定义删除字符串两边的哪个字符，只不过如果不指定的话默认是空格。同样还有lstrip和rstrip，此处l和r分别表示左边和右边，即删除字符串左边或者右边指定字符，默认空格。需要注意的是，此处的删除不是删除一个，是指从头开始符合条件的连续字符。
# - strip相似的函数还有lstrip，rstrip
# - join:这个函数主要对字符串进行拼接。它需要一个可以迭代的内容作为参数（迭代的概念后面介绍，此处暂时理解成一个列表），功能是把可迭代的字符串拼接在一起，中间使用调用字符串作为分隔符

# In[8]:


c = "DDDDana love xiaojing "
# 看不出来是否删除了两边空格
print(c.strip(),end="-----")
print()
print(c.strip(),end="-----")

print("-------")
print(c.strip("D"))
print()
print(c.strip("D"),end="-----")


# In[12]:


# join的例子，我们需要使用s1，s2，s3作为分隔符，把ss内的内容拼接在一起
s1 = "$"
s2 = "-"
s3 = " "
ss = ["Liu Dana","love","Wang","Xiaojing"]
print(s1.join(ss))
print(s2.join(ss))
print(s3.join(ss))


# In[7]:


help(str.strip)


# In[5]:


s1 = "Dana love wang xiaojing"
s2 = "Danalovewangxiaojing"
s3 = "danalovewangxiaojing"
# s4包括空格，但空格不影响结果，忽略
s4 = "dana love wangxiaojing"
s5 = "刘大拿同学是爱过王晓静滴"
print(s1.islower())
print(s2.islower())
print(s3.islower())
print(s4.islower())
# 汉字字符串无大小写概念
print(s5.islower())
print(s5.isupper())


# In[2]:


dana = "Liu Dana"
xiaojing = "Xiao jing"
s = "Liu Dana really wang xiaojing"
print(s.startswith(dana))
print(s.endswith(xiaojing))


# # 多路分支
# - 很多分支的情况，叫多路分支
#     if  条件表达式
#        语句1
#        ...
#     elif 条件表达式
#       语句1
#       ....
#     elif 条件表达式
#       语句1
#       ...
#     else
#     语句1
#     ...
# - elif可以有很多个。
# - else 可以有可以没有
# - 多路分支做多只会执行一种情况
# # if语句补充
# - if语句可以嵌套使用，不推荐（容易混乱）
# - python没有switch语句
#     

# In[ ]:





# In[1]:


# input的作用是
# 1.在屏幕上输出括号内的字符串
# 2.接受用户输入的内容并返回到程序
# 3.input返回的内容一定是字符串类型
# input负责接收用户输入并把内容返回给变量
gender = input("请输入您的性别")
# 打印输入的内容
print (gender)

if gender == "man":
    print("走，喝酒抽烟剃头")
    print("一起玩去啊")
else:
    print("你到底是个啥子哟")
    print("对不起，我是男生")
    


# # 习题
# - 90以上： 输出优秀
# - 80-90：良
# - 70-80：中
# - 60-70：及格
# - 60以下：输出：我没你这撒学僧

# In[2]:


# if 联系二
age = 19
if age > 16:
    print("喝酒去")
print("下次你请我")


# # 双向分支
# - if.....else...表达
# - 语法结构：
#     if 条件表达式：
#         语句1
#         语句2
#         ....
#     else：
#         语句1
#         语句2
#         ...
#   
#     

# In[ ]:





# In[5]:


# 表达式案例
1 + 2 
a = 1 + 2
print (a)


# In[1]:


# 两个乘号就是指数
a = 7 ** 2
print(a)


# 

# In[25]:


a = 4j
print(a)


# In[24]:


# 科学计数法
heigh = 1.84e2
print(heigh)
a = .2
print(a)


# In[22]:


# 十六进制案例
a2 = 0xfff
print(a2)
a5 = 0x53f2
print(a5)


# In[20]:


# 八进制案例
a = 0o71
print(a)


# In[19]:


# 二进制定义
a1 = 0b110
print(a1)


# In[3]:


s = "主要内容"

print(s)

