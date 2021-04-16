---
title: Python每日一谈｜No.23.实例.4-PyMol.3-alias

categories: Python每日一谈
---

额，我应该先把pymol cmd的指令汇总放在这里

https://pymol.org/pymol-command-ref.html

### **alias**

**描述：**

“alias”将常规使用的命令输入绑定到新的comman关键字。

简而言之，这个指令可以设置一个快捷方式，以便运行某些复杂的指令

**使用**

alias   快捷名字, 复杂指令

**参数**

name = 字符串: 新的关键词

command = 字符串：用分号分隔的复杂命令的字符串输入。

**案例**

```python
alias my_scene, hide; show ribbon, polymer; show sticks, organic; show nonbonded, solvent    
my_scene
```

### 上手

1. 命令行

```python
# 直接进如命令行
In [1]: import pymol
Feature has expired.
Feature:       PYMOL_MAIN
Expire date:   01-nov-2020
License path:  /Users/sujiaqi/.pymol/license.lic:
FlexNet Licensing error:-10,32
For further information, refer to the FlexNet Licensing documentation,
available at "www.flexerasoftware.com".

In [14]: pymol.commanding.alias('go','load 1AKE;save 1AKE,format=fasta')
# 然而我并没有发现，在命令行模式下可以调用的方式，或许是哪里有问题，以后有时间再补

# 不过，可以直接调用函数执行，影响不大
In [22]: def go():
    ...:     pymol.cmd.load('1AKE.pdb')
    ...:     pymol.cmd.save('1AKE.fasta',format='fasta')
    ...:     return
In [21]: cat 1AKE.fasta
>1AKE_A
MRIILLGAPGAGKGTQAQFIMEKYGIPQISTGDMLRAAVKSGSELGKQAKDIMDAGKLVTDELVIALVKE
RIAQEDCRNGFLLDGFPRTIPQADAMKEAGINVDYVLEFDVPDELIVDRIVGRRVHAPSGRVYHVKFNPP
KVEGKDDVTGEELTTRKDDQEETVRKRLVEYHQMTAPLIGYYSKEAEAGNTKYAKVDGTKPVAEVRADLE
KILG
>1AKE_B
MRIILLGAPGAGKGTQAQFIMEKYGIPQISTGDMLRAAVKSGSELGKQAKDIMDAGKLVTDELVIALVKE
RIAQEDCRNGFLLDGFPRTIPQADAMKEAGINVDYVLEFDVPDELIVDRIVGRRVHAPSGRVYHVKFNPP
KVEGKDDVTGEELTTRKDDQEETVRKRLVEYHQMTAPLIGYYSKEAEAGNTKYAKVDGTKPVAEVRADLE
KILG
```

2. 图形界面

   打开一个蛋白 3nss

   ![image-20210321130445093](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210321130445093.png)

​      命令框中输入alias

​      `alias my_scene, hide; show ribbon, polymer; show sticks, organic; show nonbonded, solvent`

​       运行指令`my_scene`

​      ![image-20210321130654315](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210321130654315.png)

