---
title: Python每日一谈｜No.31.实例.11-numpy-1
categories: Python每日一谈
top: true
---

每日一句

看下`numpy`

最传统的python科学计算包，有很多的软件都是基于他的基础，例如scikit-learn等等

当然，我一天是水不完的

一般情况下，软件本身自带

直接导入

```
In [1]: import numpy as np
```

使用numpy可以创建一个数组(array)的数据结构

创建

```python
In [3]: # 从列表开始创建
   ...: a = [1,2,3]
   ...: np1 = np.array(a)

In [4]: np1
Out[4]: array([1, 2, 3])
```

