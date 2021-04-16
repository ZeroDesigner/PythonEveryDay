---
title: Python每日一谈｜No.24.实例.5-PyMol.4-alter-更改
categories: Python每日一谈
top: true
---

Emm,想错了

竟然忘掉了要抓重点

PyMol中cmd指令很多，常用的写一下就好

我又不是遍历hhh

#### alter

>  web:https://pymolwiki.org/index.php?title=Alter&redirect=no
>
> 参考：https://kpwulab.com/2020/01/14/pymol-alter-your-molecules/#:~:text=“alter”%20is%20a%20useful%20function%20in%20PyMOL.%20One,to%20redraw%20secondary%20structure%20of%20ubiquitin%20%28PDB%3A%201UBQ%29.

##### 描述

"alter"是一个十分重要的指令

他可以重新对氨基酸编号进行重排，重命名蛋白链，重新定义二级结构。

##### 使用

alter selection, expression

##### 案例

    # 更改链名
    alter chain A, chain='B'
    alter all, resi=str(int(resi)+100)
    sort
    # 改变原子的vdw半径
    alter (name P), vdw=1.90
    # 如果dots, spheres, mesh or surface等表现形式被使用，则使用rebuild
    rebuild

##### 注意

    其可改变的属性有
    name, resn, resi, chain, alt, elem, q, b, segi,type (ATOM,HETATM), partial_charge, formal_charge,text_type, numeric_type, ID, vdw
    在更改属性之后，需要进行sort
    
    如果dots, spheres, mesh or surface等表现形式被使用，则使用rebuild
    则需要rebuild
    
##### 解释

视觉型学习者这里来

案例蛋白为：`1UBQ`

1. 改变链名

   ```
   alter (chain A),chain='B' 
   sort
   ```
   ![image-20210322011515952](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322011515952.png)

   更改之后

   ![image-20210322011603739](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322011603739.png)

   原始蛋白文件

   ![image-20210322012008489](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322012008489.png)

   更改之后蛋白文件

   ![image-20210322012040486](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322012040486.png)

   **右边的A应该是segid，而左边的A则为chainID**

   所以，alter真实的改变了链名

2. 修改某一条链中的氨基酸的编号，

   类似于从氨基酸14-15变为氨基酸114-115

   看下图，可以看到氨基酸从0开始

   ![image-20210322013428085](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322013428085.png)

   输入指令

   ```
   alter (chain A),resi=str(int(resi)+100) 
   sort
   ```

   编号从100开始
   
   ![image-20210322013454917](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322013454917.png)

    看下pdb文件
   
   原始文件
   
   ![image-20210322013651879](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322013651879.png)
   
   更改之后
   
   ![image-20210322013620361](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322013620361.png)



3. 改变二级结构显示

   拿到一个蛋白`1UBQ`

  蛋白质链上40-45位氨基酸的主链，以stick形式显示，C为黄色

 ![image-20210322011011802](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322011011802.png)

   重新定义40-45的二级结构

   命令框中输入指令

   ```
   alter 40-45/, ss='L' 
   rebuild
   ```

   此时显示为loop

   ![image-20210322011120530](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322011120530.png)

   命令框中输入

   ```
   alter 40-45/, ss='H' 
   rebuild
   ```

   此时显示为螺旋

   ![image-20210322011147081](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322011147081.png)

   **可以看到 alter只是影响二级结构的显示，并不是真正的改变了主链原子的空间位置**



最后，仍然来强制使用python,将HETATM 标记更改了ATOM

```python
In [1]: import pymol

In [2]: Feature has expired.
Feature:       PYMOL_MAIN
Expire date:   01-nov-2020
License path:  /Users/sujiaqi/.pymol/license.lic:
FlexNet Licensing error:-10,32
For further information, refer to the FlexNet Licensing documentation,
available at "www.flexerasoftware.com".

In [3]: pymol.cmd.load('1ubq.cif')
 PyMOL not running, entering library mode (experimental)
 ExecutiveLoad-Detail: Detected mmCIF
    
In [6]: pymol.cmd.get_object_list()
Out[6]: ['1ubq']

In [7]: pymol.cmd.alter('all', 'type="ATOM"')
Out[7]: 660

In [8]: pymol.cmd.sort('all')
In [9]: pymol.cmd.save('1ubq_c.pdb','1ubq')

```



![image-20210322024322083](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322024322083.png)