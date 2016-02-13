# 单行注释由一个井号开头。编译器会跳过单行注释部分
""" 三个双引号（或单引号）之间可以写多行字符串，
    通常用来写注释。"""
"""本快速入门参考自code123网站的2.7入门，专为上科大学子改写
快速入门只是梗概，真正学习还是要看详细教程并且自己多练习
使用前请默念：膜乔膜戈膜周杨 膜祝膜袁膜文涛
有问题请搜索网络资源，仍然不懂应请教周杨荣神徐杜以及袁神文涛等各路大神
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         佛祖保佑       永无BUG
         """
####################################################
## 1. 基本数据类型和操作符
####################################################
# 数字就是数字
3 #=> 3

# 四则运算也是你所期望的那样
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7

# 除法有一点棘手。
# 对于整数除法来说，计算结果不会自动取整。
#可以用//进行整数除法自动取整
5 / 2 #=> 2.5
5//2#=> 2

#学习浮点数。
2.0     # 这是一个浮点数
11.0 / 4.0 #=> 2.75
11.0 // 4.0 #=>2.00
# 使用小括号来强制计算的优先顺序
(1 + 3) * 2 #=> 8
#可以用%来取余
17 % 3#=>2
#使用 ** 运算符计算幂乘方
2**7#=>128

# 布尔值也是基本数据类型
True
False

# 使用 not 来取反
not True #=> False
not False #=> True

# 等式判断用 ==
1 == 1 #=> True
2 == 1 #=> False

# 不等式判断是用 !=
1 != 1 #=> False
2 != 1 #=> True

# 还有更多的比较运算
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True

# 居然可以把比较运算串连起来！
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False

#逻辑运算符
#A and not B or C等于 (A and (notB)) or C
#逻辑操作符 and 和 or 也称作短路操作符：
# 它们的参数从左向右解析，一旦结果可以确定就停止。
1<2 or 3>4 #因为左侧显然为True，因此该式在此停止，值为True

# 使用 " 或 ' 来创建字符串
"This is a string."
'This is also a string.'

# 字符串也可以相加！相乘代表重复
3 * 'un' + 'ium' #=> 'unununium'

# 一个字符串可以视为一个字符的列表
# （译注：后面会讲到“列表”。）
"This is a string"[0] #=> 'T'#[]内的数值可以理解为偏移量，可为负数
"This is a string"[-1]#=> 'g'
# % 可以用来格式化字符串，就像这样：
"%s can be %s" % ("strings", "interpolated")
#=>'strings can be interpolated'

# 后来又有一种格式化字符串的新方法：format 方法。
# 推荐使用这个方法。
"{0} can be {1}".format("strings", "formatted")
#字符串的参数使用{NUM}进行表示,0, 表示第一个参数, 以后顺次递加;
#使用":", 指定代表元素需要的操作, 如":.3"小数点三位, ":8"占8个字符空间等
age = 25
name = 'Caroline'

print('{0} is {1} years old. '.format(name, age)) #输出参数
print('{0} is a girl. '.format(name))
print('{0:.3} is a decimal. '.format(1/3)) #小数点后三位
print('{0:_^11} is a 11 length. '.format(name)) #使用_补齐空位
print('{first} is as . '.format(first=name)) #别名替换
print('My name is {0:8}.'.format('Fred')) #指定宽度
#程序运行结果
#Caroline is 25 years old.
#Caroline is a girl.
#0.333 is a decimal.
#_Caroline__ is a 11 length.
#Caroline is as
#My name is Fred    .

# None is an object
# None 是一个对象
None #=> None

# 不要使用相等符号 `==` 来把对象和 None 进行比较，
# 而要用 `is`。
"etc" is None #=> False
None is None  #=> True

# 这个 `is` 操作符用于比较两个对象的标识。
# （译注：对象一旦建立，其标识就不会改变，可以认为它就是对象的内存地址。）
# 在处理基本数据类型时基本用不上，
# 但它在处理对象时很有用。

# None、0 以及空字符串和空列表都等于 False，
# 除此以外的所有值都等于 True。
0 == False  #=> True
"" == False #=> True


####################################################
## 2. 变量和集合
####################################################
# 打印输出很简单
print("I'm Python. Nice to meet you!")
#=>I'm Python. Nice to meet you!
# 在赋值给变量之前不需要声明
some_var = 5    # Convention is to use lower_case_with_underscores
                # 变量名的约定是使用下划线分隔的小写单词
some_var #=> 5

# 访问一个未赋值的变量会产生一个异常。
# 进一步了解异常处理，可参见下一节《控制流》。
some_other_var  # Raises a name error
                # 会抛出一个名称错误

# if 可以作为表达式来使用
"yahoo!" if 3 > 2 else 2 #=> "yahoo!"
"yahoo!" if 3 < 2 else 2 #=> 2
# 列表用于存储序列
li = []#创建一个空列表
# 我们先尝试一个预先填充好的列表
other_li = [4, 5, 6]

# 使用 append 方法把元素添加到列表的尾部
li.append(1)
                #li 现在是 [1]
li.append(2)
                #li 现在是 [1, 2]
li.append(4)
                #li 现在是 [1, 2, 4]
li.append(3)
                #li 现在是 [1, 2, 4, 3]
# 使用 pop 来移除最后一个元素
li.pop()
                #=> 3，然后 li 现在是 [1, 2, 4]

# 我们再把它放回去
li.append(3)
                # li 现在又是 [1, 2, 4, 3] 了

# 像访问其它语言的数组那样访问列表
li[0] #=> 1
# 查询最后一个元素
li[-1] #=> 3

# 越界查询会产生一个索引错误
li[4] # Raises an IndexError
      # 抛出一个索引错误

# 你可以使用切片语法来查询列表的一个范围。
# （这个范围相当于数学中的左闭右开区间。）
#该方法同样适用于字符串
li[1:3] #=> [2, 4]  #之前已经使得li=[1, 2, 4, 3]
# 省略开头
li[2:] #=> [4, 3]
# 省略结尾
li[:3] #=> [1, 2, 4]
#step
li[::-1] #=> [3, 4, 2, 1]
# 使用 del 来删除列表中的任意元素
del li[2]
# li 现在是 [3, 4, 1]
li=[1,2,3]#为了好看对li重新赋值
# 可以把列表相加
li + other_li
#=> [1, 2, 3, 4, 5, 6] - 请留意 li 和 other_li 并不会被修改

# 使用 extend 来合并列表
li.extend(other_li)
# 现在 li 是 [1, 2, 3, 4, 5, 6]
# 用 len 来检测列表的长度
len(li) #=> 6
# 用 in 来检查是否存在于某个列表中
1 in li #=> True
# 用del来删除列表中的元素
del li[0]#=>li变为[2,3,4,5,6]
#同样可以del一段切片甚至整个列表
del li[:]
#li此时为空列表
del li
#再次引用li会引发错误


# 元组很像列表，但它是“不可变”的。
tup = (1, 2, 3)
tup[0] #=> 1
tup[0] = 3  # Raises a TypeError
            # 抛出一个类型错误

# 操作列表的方式通常也能用在元组身上
len(tup) #=> 3
tup + (4, 5, 6) #=> (1, 2, 3, 4, 5, 6)
tup[:2] #=> (1, 2)
2 in tup #=> True

# 你可以把元组（或列表）中的元素解包赋值给多个变量
a, b, c = (1, 2, 3)
# 现在 a 是 1，b 是 2，c 是 3
# 如果你省去了小括号，那么元组会被自动创建
d, e, f = 4, 5, 6
# 再来看看交换两个值是多么简单。
e, d = d, e
# 现在 d 是 5 而 e 是 4

# 字典用于存储映射关系
empty_dict = {}
# 这是一个预先填充的字典
filled_dict = {"one": 1, "two": 2, "three": 3}

# 使用 [] 来查询键值
filled_dict["one"] #=> 1

# 将字典的所有键名获取为一个列表
filled_dict.keys() #=> ["three", "two", "one"]
# 请注意：无法保证字典键名的顺序如何排列。
# 你得到的结果可能跟上面的示例不一致。

# 将字典的所有键值获取为一个列表
filled_dict.values() #=> [3, 2, 1]
# 请注意：顺序的问题和上面一样。

# 使用 in 来检查一个字典是否包含某个键(key)名
"one" in filled_dict #=> True
1 in filled_dict #=> False

# 查询一个不存在的键名会产生一个键名错误
filled_dict["four"] # KeyError
                    # 键名错误

# 所以要使用 get 方法来避免键名错误
filled_dict.get("one") #=> 1
filled_dict.get("four") #=> None
# get 方法支持传入一个默认值参数，将在取不到值时返回。
filled_dict.get("one", 4) #=> 1
filled_dict.get("four", 4) #=> 4

# Setdefault 方法可以安全地把新的名值对添加到字典里
filled_dict.setdefault("five", 5)
#filled_dict["five"] 被设置为 5
filled_dict.setdefault("five", 6)
#filled_dict["five"] 仍然为 5
#如果键在字典中，返回这个键所对应的值。
#如果键不在字典中,向字典中插入这个键并且以default为这个键的值，
#并返回 default。default的默认值为None

# set 用于保存集合
empty_set = set()
# 使用一堆值来初始化一个集合
some_set = set([1,2,2,3,4])
# some_set 现在是 set([1, 2, 3, 4])

# 从 Python 2.7 开始，{} 可以用来声明一个集合
filled_set = {1, 2, 2, 3, 4} # => {1, 2, 3, 4}
# （注：集合是种无序不重复的元素集，因此重复的 2 被滤除了。）
# （注：{} 不会创建一个空集合，只会创建一个空字典。）

# 把更多的元素添加进一个集合
filled_set.add(5)
# filled_set 现在是 {1, 2, 3, 4, 5}

# 使用 & 来获取交集
other_set = {3, 4, 5, 6}
filled_set & other_set #=> {3, 4, 5}

# 使用 | 来获取并集
filled_set | other_set #=> {1, 2, 3, 4, 5, 6}

# 使用 - 来获取补集
{1,2,3,4} - {2,3,5} #=> {1, 4}

# 使用 in 来检查是否存在于某个集合中
2 in filled_set #=> True
10 in filled_set #=> False


####################################################
## 3. 控制流
####################################################
# 我们先创建一个变量
some_var = 5

# 这里有一个条件语句。缩进在 Python 中可是很重要的哦！
# 程序会打印出 "some_var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
    #注意缩进，缩进代表了语句块的归属（据说缩进用tab还是space会引发圣战）
elif some_var < 10:    # 这里的 elif 子句是可选的
    print ("some_var is smaller than 10.")
else:     # 这一句也是可选的
    print("some_var is indeed 10.")


"""
for 循环可以遍历列表
prints:
如果要打印出：
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # 别忘了你可以使用 % 来格式化字符串
    print ("%s is a mammal" % animal)
    # （译注：意为“%s 是哺乳动物”。）

"""
`range(数字)` 会返回一个数字列表，
这个列表将包含从零到给定的数字。
prints:
如果要打印出：
    0
    1
    2
    3
"""
for i in range(4):
    print (i)
#range(a,b)即为左闭右开
"""
while 循环会一直继续，直到条件不再满足。
prints:
如果要打印出：
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1
    # 这是 x = x + 1 的简写方式

# 使用 try/except 代码块来处理异常
try:
    # 使用 raise 来抛出一个错误
    raise IndexError("This is an index error")
    # 抛出一个索引错误：“这是一个索引错误”。
except IndexError as e:
    pass
    # pass 只是一个空操作。通常你应该在这里做一些恢复工作。
#finally在try语句中会被执行
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
#结果如下
'''try...
except: division by zero
finally...'''

####################################################
## 4. 函数
####################################################

# 使用 def 来创建新函数
def add(x, y):
    print ("x is %s and y is %s" % (x, y))
    return x + y
# 使用 return 语句来返回值
# 未定义的return默认为None

# 调用函数并传入参数
add(5, 6) #=> prints out "x is 5 and y is 6" and returns 11

# 调用函数的另一种方式是传入关键字参数
add(y=6, x=5)
#可以在定义时设定默认参数
def gpa_zhouyang(gpa=4.0):
    print("zhouyang dad's gpa is %s"%gpa)
gpa_zhouyang()#=>zhouyang dad's gpa is 4.0

# 关键字参数可以以任意顺序传
# 你可以定义一个函数，并让它接受可变数量的定位参数。
def varargs(*args):
    return args

varargs(1, 2, 3) #=> (1,2,3)

# 你也可以定义一个函数，并让它接受可变数量的关键字参数。
def keyword_args(**kwargs):
    return kwargs

# 我们试着调用它，看看会发生什么：
keyword_args(big="foot", loch="ness")
 #=> {"big": "foot", "loch": "ness"}

# 你还可以同时使用这两类参数，只要你愿意：
def all_the_args(*args, **kwargs):
    print (args)
    print (kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# 在调用函数时，定位参数和关键字参数还可以反过来用。
# 使用 * 来展开元组，使用 ** 来展开关键字参数。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}

all_the_args(*args)
# 相当于 all_the_args(1, 2, 3, 4)

all_the_args(**kwargs)
# 相当于 all_the_args(a=3, b=4)

all_the_args(*args, **kwargs)
# 相当于 all_the_args(1, 2, 3, 4, a=3, b=4)

# 如果要限制关键字参数的名字，就可以用命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 可变参数无法和命名关键字参数混合
# 参数定义的顺序：必选参数、默认参数、可变参数/命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# 或者下面的顺序
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 函数的默认参数请不要使用变量，如li=[]，下面是一个错误的例子
def add_end(L=[]):
    L.append('END')
    return L
'''
>>> add_end()
['END']
>>>add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
'''
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。


# 函数在 Python 中是一等公民
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3) #=> 13

# 还有匿名函数
(lambda x: x > 2)(3) #=> True
# 匿名函数lambda x: statements实际上就是
def f(x):
    return statements
# 匿名函数多见于一次使用无需命名的简单函数
# 还有一些内建的高阶函数

list(map(add_10, [1,2,3])) #=> [11, 12, 13]
list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))#=> [6, 7]
# 我们可以使用列表推导式来模拟 map 和 filter

[add_10(i) for i in [1, 2, 3]]  #=> [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5] #=> [6, 7]
# 列表推导式
# [expression for item in iterable if condition]

a_list=[number for number in range (1,6) if number %2==1]
a_list#=>[1,3,5]
# 可以使用一次推导形成元组（row,col)
cells=[(a,b)for a in range(1,4)for b in range(1,3)]
for cell in cells:
    print(cell)
#=>输出结果
(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)
# 类似多重循环，后面的for为内层循环


# 字典推导式
# {key_expression:value_expression for expression in iterable }
word='letters'
letter_counts={letter:word.count(letter)for letter in set(word)}
letter_counts#=>{'l': 1, 't': 2, 'r': 1, 'e': 2, 's': 1}
# 集合推导式
# {expression for expression in iterable}
# 元组不可变，因此实际上上述形式产生的是生成器推导式
g = (x * x for x in range(10))
# 输入g你会得到其内存地址
# next()函数获得generator（生成器）的下一个返回值
# 生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n +=1
    return 'done'
# 如果一个函数定义中包含yield关键字，其为generator
# generator遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
# 得到结果如下：
'''o = odd()
>>> next(o)
step 1
1
>>> next(o)
step 2
3
>>> next(o)
step 3
5
>>> next(o)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration'''
# generator均为惰性计算的序列，因此多使用for
# 这也是为什么上面的map和filter函数均使用了list函数使得其生成整个列表


# 可以使用关键字continue跳出本次循环或者break跳出整个for循环
for x in range(10):
    if x==5:
        break
    print(x)
# 结果如下
0
1
2
3
4
for x in range(10):
    if x==5:
        continue

    print(x)
# 结果如下
0
1
2
3
4
6
7
8
9

# 递归

# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数

def fact(n):
    if n==1:#如果n等于1，执行return 1
        return 1
    #没有else语句，即不论n是否等于1，下列语句都执行（注意缩进）
    return n * fact(n - 1)

# 实际上，递归函数的计算过程如下
'''
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''
#归调用的次数过多，会导致栈溢出。可以试试fact(1000)
#栈的概念大家应该让acm社开一个讲座
#Python中没有进行尾递归优化，有兴趣的同学可以研究尾递归优化

####################################################
## 5. 类
####################################################

# 我们可以从对象中继承，来得到一个类。
class Human(object):
    #下面是一段文档字符串，可以使用Human.__doc__调用
    """A simple example class"""
    # 下面是一个类属性。它将被这个类的所有实例共享。
    species = "H. sapiens"

    # 基本的初始化函数（构造函数）
    def __init__(self, name):
        # 把参数赋值为实例的 name 属性
        self.name = name

    # 下面是一个实例方法。所有方法都以 self 作为第一个参数。
    def say(self, msg):
       return "%s: %s" % (self.name, msg)

    # 类方法会被所有实例共享。
    # 类方法在调用时，会将类本身作为第一个函数传入。
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法在调用时，不会传入类或实例的引用。
    @staticmethod
    def grunt():
        return "*grunt*"
# 参考知乎回答：Python 中的 classmethod 和 staticmethod 有什么具体用途？
# 实例化一个类
i = Human(name="Ian") #同样可以直接i=Human("Ian")
# 并且i是初始化函数(__init__)的第一个参数self
# 在say方法中同样不需要传入self参数
print (i.say("hi"))
# 打印出 "Ian: hi"

j = Human("Joel")#另一个实例
print (j.say("hello"))
# 打印出 "Joel: hello"

# 调用我们的类方法
i.get_species() #=> "H. sapiens"
# i的class为Human，返回值即为Human.species属性——"H. sapiens"
# 定义一个方法，除了第一个参数是self外，其他和普通函数一样。
# 要调用一个方法，只需要在实例变量上直接调用，
# 除了self不用传递，其他参数正常传入
# 修改共享属性
Human.species = "H. neanderthalensis"
i.get_species() #=> "H. neanderthalensis"
j.get_species() #=> "H. neanderthalensis"
# 此时修改的是类属性，类的每个实例都会被修改。
# 调用静态方法
Human.grunt() #=> "*grunt*"

#类和实例变量

# 实例变量用于对每一个实例都是唯一的数据，
# 类变量用于类的所有实例共享的属性和方法
# 对于两个实例变量，是同一个类的不同实例，但拥有的变量名称都可能不同
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
# bart和lisa均可以调用print_score方法
bart.print_score()#=>Bart Simpson: 59
lisa.print_score()#=>Lisa Simpson: 87
bart.age = 8
bart.age
#=>8
lisa.age#因为lisa没有age属性，因此会报错
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
'''
# 思考下面两组代码的区别
class Dog:

    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

'''
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over', 'play dead']
'''
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

'''
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
'''

#继承&多态


# 在OOP（面向对象编程）程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class）
class Animal(object):
    a=1
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass

class Cat(Animal):
    pass
# Animal就是它的父类，对于Animal来说，Dog就是它的子类
# 子类继承了父类的所有方法和属性
Dog.a#=>1
Dog().run()#=>Animal is running...
# 但是这样看起来并不好，因此在定义Dog的时候可以设定子类的方法
class Dog(Animal):
    a=2
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')
# 子类的同名方法和属性会在调用该子类的时候优先调用，父类的属性与方法并没有修改

# 判断一个变量是否是某个类型可以用isinstance()判断

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
isinstance(a, list)    #=>True
isinstance(b, Animal)  #=>True
isinstance(c, Dog)     #=>True
isinstance(c, Animal)  #=>True
# c不仅仅是Dog类型，还是Dog的父类Animal类型，这就是继承的好处，多态
#多态的运用
def run_twice(animal):
    animal.run()
    animal.run()
# 当我们传入Animal的实例时，run_twice()就打印出：
'''
>>> run_twice(Animal())
Animal is running...
Animal is running...
'''
# 当我们传入Dog的实例时，run_twice()就打印出：
'''
>>> run_twice(Dog())
Dog is running...
Dog is running...
'''
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')


run_twice(Timer())
#=>Start...
#=>Start...

# 有兴趣的同学可以继续学习多继承

#私有变量
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问
#Python 用下划线作为变量前缀和后缀指定特殊变量。

#_xxx      不能用'from module import *'导入（模块后面会讲）
#__xxx__ 系统定义名字
#__xxx    类中的私有变量名
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
#无法从外部访问实例变量.__name和实例变量.__score
bart = Student('Bart Simpson', 98)
bart.__name#结果如下
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'
'''
#给Student类增加get_name和get_score可以使得其获得name和score
#具体参考廖雪峰教程
#以及http://blog.sina.com.cn/s/blog_58649eb30100g4zo.html

#获取一个对象的信息

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
dir('ABC')#=>
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__',
 '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count',
 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex',
 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 使用getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

hasattr(obj, 'x') # 有属性'x'吗？
True

obj.x
9

hasattr(obj, 'y') # 有属性'y'吗？
False

setattr(obj, 'y', 19) # 设置一个属性'y'

hasattr(obj, 'y') # 有属性'y'吗？
True
getattr(obj, 'y') # 获取属性'y'
19

obj.y # 获取属性'y'
19

getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404
#方法同样可以进行操作
hasattr(obj, 'power') # 有属性'power'吗？
True



#作用域
# 作用域 就是一个 Python 程序可以直接访问命名空间的正文区域
# 一个对名称的错误引用会尝试在命名空间内查找

# 包含局部命名的使用域在最里面，首先被搜索；
# 其次搜索的是中层的作用域，这里包含了同级的函数；
# 最后搜索最外面的作用域，它包含内置命名。

# 当调用函数时，就会为它创建一个局部命名空间，
# 并且在函数返回或抛出一个并没有在函数内部处理的异常时被删除。
# 作用域的具体内容陈浩爸爸会在课上讲述，此处只举例子。
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
#   上一行的spam实际上并不是local函数的spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
# 运行结果如下
'''
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
'''
# local 赋值语句是无法改变 scope_test 的 spam 绑定。
# nonlocal 赋值语句改变了 scope_test 的 spam 绑定，
# 并且 global 赋值语句从模块级改变了 spam 绑定。

# nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
# global关键字用来在函数或其他局部作用域中使用全局变量。


####################################################
## 6. 模块
####################################################

# 你可以导入模块
import math
print(math.sqrt(16)) #=> 4

# 也可以从一个模块中获取指定的函数
from math import ceil, floor
print(ceil(3.7))  #=> 4.0
print(floor(3.7)) #=> 3.0

# 你可以从一个模块中导入所有函数
# 警告：不建议使用这种方式
from math import *


# 你可以缩短模块的名称
import math as m
math.sqrt(16) == m.sqrt(16) #=> True


# Python 模块就是普通的 Python 文件。
# 你可以编写你自己的模块，然后导入它们。
# 模块的名称与文件名相同。

# You can find out which functions and attributes
# defines a module.
# 你可以查出一个模块里有哪些函数和属性
import math
dir(math)

######################
#既然你都看到这里了，相信起码开学一个星期甚至两个星期的内容应该大概有个了解
#关于io以及异常请自学
#什么？你还在等我继续写更多的内容？少年自己去撸官方文档和网络资源去吧
