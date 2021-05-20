---
title: Python每日一谈｜No.37.实例.17.OpenMM-5.动力学模拟.1.炼金术自由能计算(Alchemical free energy calculations)
categories: Python每日一谈
top: true
---

[TOC]

## 简介

炼金术自由能

炼金术自由能计算可计算与转移过程相关的自由能差，例如，小分子与受体的结合过程或小分子从水相到非极性相的转移过程。这些计算使用许多非物理状态的中间状态，其中系统的某些部分（例如小分子配体或受体侧链）的化学同一性通过修改被修饰、插入或删除的原子间相互作用的势能函数来改变。图1说明了常见的自由能变化，这些变化可能很难用常规计算方法来计算，但更容易用炼金术方法计算。

![“炼金术”自由能计算的最佳实践-墨灵格的博客](/Users/sujiaqi/Pictures/Typora/2020112911095956.png)

参考：http://blog.molcalx.com.cn/2020/11/29/best-practices-for-alchemical-free-energy-calculations.html

## 一些名词，背景



## 步骤

1. 定义（alchemically-modified potentials）

   As a simple example of how this is facilitated by custom forces, consider computing the chemical potential of liquid argon by estimating the free energy of alchemically annihilating a Lennard-Jones particle. First, we create a simple Lennard-Jones fluid to represent liquid argon at 120 K and 80 atm, which can be conveniently done using the `testsystems` module of the conda-installable [`openmmtools`](http://github.com/choderalab/openmmtools) package:

   作为通过惯性力如何促进这种情况的简单示例，请考虑通过估计通过化学方法消灭Lennard-Jones粒子的自由能来计算液氩的化学势。 首先，我们创建一个简单的Lennard-Jones流体来表示120 K和80 atm（80个标准大气压）的液态氩，这可以使用conda可安装[`openmmtools`]的`testsystems`模块方便地完成。 / choderalab / openmmtools）软件包：

   作为一个简单的案例，考虑

   首先，我们创建一个简单的Lennard-Jones 流体来表示 120 K，80 atm的液态氩。

   这个可以很方便的使用`testsystems`的模块，此模块需要先使用conda 安装  `openmmtools`包

   ```python
   In [20]: from simtk import openmm, unit
       ...: # Create a Lennard-Jones fluid
       ...: pressure = 80*unit.atmospheres
       ...: temperature = 120*unit.kelvin
       ...: collision_rate = 5/unit.picosecon
   In [21]: sigma
   Out[21]: Quantity(value=3.4, unit=angstrom)
   
   In [22]: pressure
   Out[22]: Quantity(value=80, unit=atmosphere)
   
   In [23]: collision_rate
   Out[23]: Quantity(value=5, unit=/picosecond)
   
   In [24]: timestep
   Out[24]: Quantity(value=2.5, unit=femtosecond)
   
   In [25]: sigma
   Out[25]: Quantity(value=3.4, unit=angstrom)
   
   In [26]: epsilon
   Out[26]: Quantity(value=0.238, unit=kilocalorie/mole)      
   
   ```

   

   

   

