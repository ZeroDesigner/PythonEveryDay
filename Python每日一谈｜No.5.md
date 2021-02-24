### Python每日一谈｜No.5

### 字典

+ 字典是经常使用的数据结构

+ 字典分为key 以及value两部分

+ 每个Key都可以对应一个value

+ 使用`{}`来创建字典

+ 字典的元素可以是比较任意的类型，例如列表，元祖等

+ 字典的一般操作有创建，更新元素，删除元素，添加元素，以及遍历

**实例**

```python
#创建一个空字典
In [1]: a = {}

In [2]: type(a)
Out[2]: dict
  
# 当然也可以创建一个非空字典
In [4]: b = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

In [5]: b
Out[5]: {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
  
# 在b中更新元素
In [6]: b['Name']
Out[6]: 'Zara'

In [7]: b['Name'] = 'Xiaoming'

In [8]: b
Out[8]: {'Name': 'Xiaoming', 'Age': 7, 'Class': 'First'}
  
# 在删除b中元素
In [9]: del b['Name']

In [10]: b
Out[10]: {'Age': 7, 'Class': 'First'}
 
# 在b中添加元素
In [11]: b['new'] = 'nihao'

In [12]: b
Out[12]: {'Age': 7, 'Class': 'First', 'new': 'nihao'}


```



### 集合

+ 集合是无序的，**不重复的**
+ 使用`set()`来创建一个集合
+ 你可以添加元素，也可以删除元素
+ 集合比较重要的是其运算求交集，并集等等

**实例**

```python
# 创建一个集合
In [13]: a = set('abracadabra')
    ...: b = set('alacazam')
    
In [24]: a = set(['a', 'b', 'c', 'd', 'r'])
In [26]: b = set(['a', 'c', 'l', 'm', 'z'])
In [25]: a
Out[25]: {'a', 'b', 'c', 'd', 'r'}

In [27]: b
Out[27]: {'a', 'c', 'l', 'm', 'z'}

In [14]: a
Out[14]: {'a', 'b', 'c', 'd', 'r'}

In [15]: b
Out[15]: {'a', 'c', 'l', 'm', 'z'}

# 求ab的交集
In [17]: a & b
Out[17]: {'a', 'c'}

# 求ab的并集
In [16]: a | b
Out[16]: {'a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'}

#在a中但不在b中的元素

In [18]: a-b
Out[18]: {'b', 'd', 'r'}

#不在a中不在b中

In [19]: a ^ b
Out[19]: {'b', 'd', 'l', 'm', 'r', 'z'}
  
  
#添加元素
In [28]: a.add('g')

In [29]: a
Out[29]: {'a', 'b', 'c', 'd', 'g', 'r'}
#移除元素
In [30]: a.remove('g')

In [31]: a
Out[31]: {'a', 'b', 'c', 'd', 'r'}
```



