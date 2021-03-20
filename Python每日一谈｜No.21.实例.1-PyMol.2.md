---
title: Python每日一谈｜No.21.实例.1-PyMol.2-计算RMSD
categories: Python每日一谈
---

我可以把cmd的指令遍历一次，这样就不需要愁拖稿了hhh

我们来看下蛋白质的中的结构比较

在结构比较中，你可以很方便的使用align对两个object进行比较

这里的object你可以简单的理解为蛋白

1. 你可以很方便的pymol自带的工具对两个或者多个蛋白进行align

步骤如下，3nss-->Action-->align-->to molecule-->5nwe

![Screen Shot 2021-03-15 at 4.44.37 PM](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/Screen%20Shot%202021-03-15%20at%204.44.37%20PM.png)


2. 当align不能满足的时候，你也可以使用pymol的插件alignment选择一个比对方式，来进行比较
 ![image-20210315164700320](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210315164700320.png)

这里我们先来看下比较方式的不同定义：

align:首先进行序列对齐，然后进行结构叠加，随后循环几个周期来进行优化，以便拒绝掉在拟合期间发现的异常值。在序列相似度较高的蛋白中align效果会比较好(序列>30%)，如果序列相似度比较低的话，super或者cealign会比较好。

super:对齐选择的结构，他执行的是基于结构的动态规划对齐(不依赖于序列)，随后进行循环优化来提高拟合度，对于低序列相似性的蛋白来说，super比align更为鲁棒。

cealign：使用CE算法来对齐两个蛋白。对于几乎没有序列相似性的蛋白质（twilight zone），它是非常鲁棒的。对于结构比较相似的蛋白，请使用[super](https://pymolviki.org/index.php/Super)首选命令，对于序列比较相似的蛋白，则align为首选命令，因为这些命令比cealign快得多

fit：将第一选择中的模型叠加到第二个模型中，在两个选择中，只要匹配的院子才会被用于fit

**晕了的话我们就来看看例子**

借用我最近看的算法图解的书来说，我们都是视觉型学习者

align：

官方给的例子是1oky, 1t46

在pymol进行align比较，rmsd = 1.306

![image-20210315173226326](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210315173226326.png)

我们来看看他的序列相似度

虽然，我有时候并不喜欢做图，但是，我们可以比较容易的从图中获得其序列相对而言比较保守的信息

![image-20210315173805551](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210315173805551.png)

然后我们在看看看super，官方给的案例是

1F9J，1YX5，rmsd = 0.717

![image-20210315174136972](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210315174136972.png)

两者的序列相似度，很不相似

![image-20210315174349940](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210315174349940.png)

我使用了align方法，对齐比较了一下，rmsd = 13.697

![image-20210315174508859](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210315174508859.png)

然后，我们来看cealign，官方给的案例：1c0mB，1bco，rmsd = 4.958

![image-20210315174718512](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210315174718512.png)

序列相似度

![image-20210315175038498](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210315175038498.png)

最后，我们看来看下fit

所用的比较部分为1a00的a链和c链，rmsd =0.564，当然这个需要的对比条件比较严格，

object的id必须要严格保持一致，比如segi, chain，如果不一致那么需要手动整

![image-20210315175925035](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210315175925035.png)

到这里，基本上和python没什么用

但是，强制有用

举个例子，假设，我有10个蛋白需要比较，计算rmsd

此处，以aligh为例

蛋白为：6BHT,4WYM,6OBH,6ECN,5HGL,2PWM,2PWO,6ECO,6OMT,3J3Y

开始

```python
# 启动pymol
In [1]: import pymol

Feature has expired.
Feature:       PYMOL_MAIN
Expire date:   01-nov-2020
License path:  /Users/sujiaqi/.pymol/license.lic:
FlexNet Licensing error:-10,32
For further information, refer to the FlexNet Licensing documentation,
available at "www.flexerasoftware.com".
# 将pdb id号存储为list
In [2]: pdb_list = ['6BHT','4WYM','6OBH','6ECN','5HGL','2PWM','2PWO','6ECO','6OM
   ...: T','3J3Y']
# 获取蛋白
In [5]: for  i in pdb_list:
   ...:     pymol.cmd.fetch(i)
   ...:
 PyMOL not running, entering library mode (experimental)
 ExecutiveLoad-Detail: Detected mmCIF
 ExecutiveLoad-Detail: Detected mmCIF
 ExecutiveLoad-Detail: Detected mmCIF
 ExecutiveLoad-Detail: Detected mmCIF
 ExecutiveLoad-Detail: Detected mmCIF
 ExecutiveLoad-Detail: Detected mmCIF
 ExecutiveLoad-Detail: Detected mmCIF
 ExecutiveLoad-Detail: Detected mmCIF
 ExecutiveLoad-Detail: Detected mmCIF
 ExecutiveLoad-Detail: Detected mmCIF
 # 查看object名单
In [6]: pymol.cmd.get_object_list()
Out[6]:
['6BHT',
 '4WYM',
 '6OBH',
 '6ECN',
 '5HGL',
 '2PWM',
 '2PWO',
 '6ECO',
 '6OMT',
 '3J3Y']
 # 两两比较rmsd
 # 构建两两组合表
In [7]: import itertools

In [8]: combinations = list(itertools.combinations(pdb_list, 2))

In [9]: combinations
Out[9]:
[('6BHT', '4WYM'),
 ('6BHT', '6OBH'),
 ('6BHT', '6ECN'),
 ('6BHT', '5HGL'),
 ('6BHT', '2PWM'),
 ('6BHT', '2PWO'),
 ('6BHT', '6ECO'),
 ('6BHT', '6OMT'),
 ('6BHT', '3J3Y'),
 ('4WYM', '6OBH'),
 ('4WYM', '6ECN'),
 ('4WYM', '5HGL'),
 ('4WYM', '2PWM'),
 ('4WYM', '2PWO'),
 ('4WYM', '6ECO'),
 ('4WYM', '6OMT'),
 ('4WYM', '3J3Y'),
 ('6OBH', '6ECN'),
 ('6OBH', '5HGL'),
 ('6OBH', '2PWM'),
 ('6OBH', '2PWO'),
 ('6OBH', '6ECO'),
 ('6OBH', '6OMT'),
 ('6OBH', '3J3Y'),
 ('6ECN', '5HGL'),
 ('6ECN', '2PWM'),
 ('6ECN', '2PWO'),
 ('6ECN', '6ECO'),
 ('6ECN', '6OMT'),
 ('6ECN', '3J3Y'),
 ('5HGL', '2PWM'),
 ('5HGL', '2PWO'),
 ('5HGL', '6ECO'),
 ('5HGL', '6OMT'),
 ('5HGL', '3J3Y'),
 ('2PWM', '2PWO'),
 ('2PWM', '6ECO'),
 ('2PWM', '6OMT'),
 ('2PWM', '3J3Y'),
 ('2PWO', '6ECO'),
 ('2PWO', '6OMT'),
 ('2PWO', '3J3Y'),
 ('6ECO', '6OMT'),
 ('6ECO', '3J3Y'),
 ('6OMT', '3J3Y')]
                    
 # 使用align进行比较,然后计算一下时间
In [7]: import time
   ...: a = time.time()
   ...: print(pymol.cmd.align(combinations[0][0],combinations[0][1]))
   ...: b = time.time()
   ...: b - a
(0.797596275806427, 17935, 5, 1.2639384269714355, 19167, 14602.0, 2772)
Out[7]: 3.0302011966705322
                  
```



输出的7个值为

This returns a list with 7 items:

1. RMSD after refinement
2. Number of aligned atoms after refinement
3. Number of refinement cycles
4. RMSD before refinement
5. Number of aligned atoms before refinement
6. Raw alignment score
7. Number of residues aligned

简而言之，选择第一个就够用





