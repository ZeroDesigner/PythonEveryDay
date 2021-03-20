---
title: Python每日一谈｜No.9
categories: Python每日一谈
---

### 循环中的一些关键词

在上面我们已经说了`else`

现在那么只有三个关键词`break, continue,pass`

1. `break`

   `break` 用于打破循环，想到了悟空，hhh，在循环中，当值满足某个条件值，可以使用`break`打破此循环，避免执行后续语句，减少计算量

   一般形式

   ```python
   In [22]: a = 'abcdefg'
       ...: for   i  in a:
       ...: 	if i == 'd':
       ...:		print('find d and break')
       ...:		break
       ...:	print('find',i)
       ...: print('finished')
   find a
   find b
   find c
   find d and break
   finished
   ```

   

2. `continue`用于跳过当前的循环

   当满足你的判断条件时，使用`continue`可以跳过本次循环，进入下一循环

   我们来看一个实例

   ```python
   # 当我们使用continue时
   
   In [36]: a = 'abcdefg' 
       ...: print('continue') 
       ...: for i in a: 
       ...:     if i == 'c': 
       ...:         continue 
       ...:     print('find ',i) 
       ...:                                                                                                                                                   
   continue
   find  a
   find  b
   find  d
   find  e
   find  f
   find  g
   # 可以看出我们跳过了c进行了后续的循环
   
   
   # 当我们使用break是
   In [62]: print('break')
       ...: for i in a:
       ...:     if i == 'c':
       ...:         break
       ...:     print('find ',i)
       ...:
   break
   find  a
   find  b
   # 可以看出当遇到break时，循环直接被打破
   
   ```

   

   

3. `pass`

   pass是空语句，不做任何事情，你可以把它当作一个为了保证程序结构完整性而创造出来的词

   只是为了占个位置，看起来顺眼

   例如

   ```python
   In [63]: for i in a:
       ...:     if i == 'c':
       ...:         pass
       ...:     print('find ',i)
       ...:
   find  a
   find  b
   find  c
   find  d
   find  e
   find  f
   find  g
   # 可以看出当我们使用pass时，实际上没有发生任何变化，程序会正常执行，循环
   
   # 或者下面一个例子
   In [38]: for i in a: 
       ...:     if i == 'c': 
       ...:         pass 
       ...:     else: 
       ...:         print(i,'is not c') 
   # 当我们在使用pass时，程序不执行任何操作，但当条件不是‘c’时，程序执行print操作                                                                                                                                               
   a is not c
   b is not c
   d is not c
   e is not c
   f is not c
   g is not c
   ```

   

