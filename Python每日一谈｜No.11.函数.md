---
title: Python每日一谈｜No.11.函数
categories: Python每日一谈
---

手写一个迭代器，不要傻了，在你连函数都不会定义的情况下，我教你手写一个迭代器那是作死。

迭代器在后方

我们现在来看看**函数,function**定义

啥子叫个函数嘞

先来看看我对他的简化版定义

**当你写的代码太过复杂，不易被管理时，我们对代码所用的一种优化，一种代码的简洁结构**

当然他有一定的规则，来看看函数定义的规则(大部分摘自：https://www.runoob.com/python3/python3-function.html)：

- 函数代码块以 **def** 关键词开头，后接函数标识符名称(就是下面的那个max)和圆括号 `()`，后面再加个冒号`:`。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数内容有缩进。
- 使用`return` 结束函数，函数会返回一个值，结束时不带return的话相当于返回 None。



![img](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/py-tup-10-26-1.png)

#### 一般形式

```python
def 函数名(参数):

	函数
	
	return
```



### 一个实例

仍然是`hellow world!`

```python
In [11]: def hw(words):
    ...: 		 print(words)
    ...:

In [12]: hw('Hellow World!')
Hellow World!
```

然后让我们看看有`return`的情况

```python
In [13]: def plus(a,b):
    ...:     c = a + b
    ...:     return c
    ...:

In [14]: plus(1,2)
Out[14]: 3

In [15]: d = plus(1,2)

In [16]: d
Out[16]: 3
```

当然`return`在一个函数中也可以多次使用

```python
In [72]: def pick_max(a,b): 
    ...:     if a > b : 
    ...:         return a 
    ...:     else: 
    ...:         return b 
    ...:                                                                                                                                                   

In [73]: pick_max(1,2)                                                                                                                                     
Out[73]: 2

In [74]: c = pick_max(1,2)                                                                                                                                 

In [75]: c                                                                                                                                                 
Out[75]: 2
```



#### 参数

我们来看下传参

1. 必须参数

   你函数定义了一个参数，此函数必须要有相对应地参数否则运行便会报错

   例如：

   ```python
   In [20]: def hw(words):
       ...:     print(words)
       ...:
   
   In [21]: hw()
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-21-9982e5434f2d> in <module>
   ----> 1 hw()
   
   TypeError: hw() missing 1 required positional argument: 'words'
   ```

2. 默认参数

   我们有时会给参数加一些默认值，如果运行函数时传入修改的参数的话，那么函数一般运行便会使用默认值

   例如

   ```python
   In [23]: def hw(a,b,c = 5):
       ...:     print(a)
       ...:     print(b)
       ...:     print(c)
       ...:
   
   In [24]: hw(1,2)
   1
   2
   5
   
   In [25]: hw(1,2,3)
   1
   2
   3
   ```

   

3. 可变参数

   顾名思义，可变参数就是参数的个数是可变的，可以是1个也可以是n个

   一般使用`*参数名`来进行表示,有时候你会常常看到这种形式`*args`

   `*`参数用于解包tuple对象的每个元素，作为一个一个的位置参数传入到函数中

   来举个例子，我想要计算（1，2，3，4）之间的加和

   ```python
   In [26]: def calc(*numbers):
       ...:     sum = 0
       ...:     for n in numbers:
       ...:         sum = sum + n * n
       ...:     return sum
       ...:
   
   In [27]: calc(1,2,3,4,5)
   Out[27]: 55
     
   
   In [30]: def calc(*args):
       ...:     sum = 0
       ...:     for n in args:
       ...:         sum = sum + n * n
       ...:     return sum
       ...:
   
   In [31]:   calc(1,2,3,4)
   Out[31]: 30
   ```

   

   如果我们有一个列表或者元祖，如和进行传参呢

   例如： a = [1,2,3,4]

   这样？`calc(a[0],a[1],a[2],a[3])`

   虽然可行，但是太过赘述，python中容许在列表或者元祖前加`*`，将其作为可变参数传入

   例如：

   ```python
   In [32]: def calc(*args):
       ...:     sum = 0
       ...:     for n in args:
       ...:         sum = sum + n * n
       ...:     return sum
       ...:
   
   In [33]: a = [1,2,3,4]
   
   In [34]: calc(*a)
   Out[34]: 30
   ```

   还有另外一种形式`**karg`,使用这种形式参数在函数内部组装为一个dict。

   我们来看个例子

   ```python
   In [39]: def see(**kw):
       ...:     print(kw)
   
   In [41]: see(a = 1,b = 2,c = 3,d = 4)
   {'a': 1, 'b': 2, 'c': 3, 'd': 4}
   
   ```

4. 命名关键字参数

   对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。

   但是，我们需要检查某些关键字，以便查看使用者输入的参数是否是正确的。

   。。。

   把自己当作那些一无所知的用户吧，为他们设身处地的想想。

   我们需要检查，用户的参数输入是否符合我们的标准

   形式为`*,关键字,关键字`

   例如：我们需要检查用户是否输入了`id`,`smi`这两个参数，化学信息学初步引入hhh

   ```python
   In [45]: def get(*,id,smi):
       ...:     print(id,smi)
       ...:
   
   In [46]: get(id=1,smi='c1ccccc1')
   1 c1ccccc1
   
   # 如果缺少id
   In [47]: get(id=1)
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-47-f3ae4c96f67d> in <module>
   ----> 1 get(id=1)
   
   TypeError: get() missing 1 required keyword-only argument: 'smi'
       
   # 如果缺少smi
   In [48]: get(smi = 'c1ccccc1')
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-48-988e95298c74> in <module>
   ----> 1 get(smi = 'c1ccccc1')
   
   TypeError: get() missing 1 required keyword-only argument: 'id'
   ```

   

5. 参数组合

   额，我就假设你们对前面的内容理解了

   阿弥陀佛

   我们已知有上述几种参数的形式，那么在定义函数的时候，这些参数是否是有顺序的呢

   答案是有的
   
   **参数的顺序必须是：必须参数、默认参数、可变参数/命名关键字参数和关键字参数**
   
   详细可以看：https://www.jianshu.com/p/98f7e34845b5
   
   举个例子：
   
   ```python
   # 这里简单引入驼峰命名法，其实就是justdo不好看hhh
   # 驼峰命名法：https://baike.baidu.com/item/骆驼命名法
   In [49]: def just_do(a, b, c=0, *, d, **kw):
       ...:     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
       ...:
   
   In [50]:  just_do(1, 2, d=99, ext=None)
   a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
   ```
   
   
   
   

