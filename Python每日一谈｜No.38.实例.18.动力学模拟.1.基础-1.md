---
title: Python每日一谈｜No.38.实例.18.动力学模拟.1.基础-1
categories: Python每日一谈
top: true
---

[TOC]

## 背景

### Ar

**氩**（[拼音](https://www.wanweibaike.com/wiki-汉语拼音)：yà， 英语：**Argon**），是一种[化学元素](https://www.wanweibaike.com/wiki-化學元素)，其[化学符号](https://www.wanweibaike.com/wiki-化學符號)为**Ar**，[原子序数](https://www.wanweibaike.com/wiki-原子序數)为18，[原子量](https://www.wanweibaike.com/wiki-原子量)为39.948 [u](https://www.wanweibaike.com/wiki-原子质量单位)，位在[周期表](https://www.wanweibaike.com/wiki-元素週期表)的第18族，是一种稀有气体。氩占大气体积的0.934%（9340 ppmv），是[地球大气层](https://www.wanweibaike.com/wiki-地球大氣層)第三多的气体，是[水蒸气](https://www.wanweibaike.com/wiki-水蒸氣)的两倍以上（平均4000 ppmv左右，但变化很大）、[二氧化碳](https://www.wanweibaike.com/wiki-二氧化碳)（400 ppmv）的23倍之多、[氖](https://www.wanweibaike.com/wiki-氖)（18 ppmv）的500倍以上。氩是地壳含量中最丰富的惰性元素，在地壳中占了0.00015%

Ar 相关理化数据：

![image-20210419011106053](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210419011106053.png)

> 参考:https://www.wanweibaike.com/wiki-%E6%B0%A9

### Lennard-Jones fluid

此次你会写一个简单的MD来模拟Lennard-Jones fluid，Gibbs 系综( N, P, T 固定不变)，并与实验结果进行比较  Ar

Lennard-Jones fluid是一个非常简单的系统，他由两个独立参数确定： $\sigma$, $\epsilon$  (Lennard-Jones potential)。E(r)为势能由距离r确定，通常为12-6项

$$E_{(r)} = U_{LJ} = 4\epsilon\begin{bmatrix}\begin{pmatrix}\sigma/r\end{pmatrix}^{12} - \begin{pmatrix}\sigma/r\end{pmatrix}^{6}\end{bmatrix}$$

吸引项是van der Waals’ interaction ，其作用形式 $$\begin{pmatrix}1/\gamma^6\end{pmatrix} $$，这个函数来自于量子力学微扰计算（对于一些非极性，中性原子，具有球对称电子壳层，即惰性气体）。排斥项函数形式不是很确定，但可以使用指数幂或者逆幂来进行近似。 Lennard-Jones potential 中的数字$$12$$是因为计算效率而确定的，因为$$1/\gamma^{12}$$是$$1/\gamma^{6}$$的平方。

注：
+ ε是势井深度，反应两个原子间相互吸引作用的强弱。
+ σ是作用势等于0时原子间的距离。
+ 有时还会增加一个rc参数，代表势函数的截断距离：当原子间距离超过rc时，认为原子间相互作用为0.
+ LJ势函数模型很简单，适用于中性原子，尤其是用于描述惰性气体原子

![lj-2](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/lj-2.jpeg)

## 1.1 适当的减少单位

重要的是要使用一组合适的单位，尽量减少误差的影响。在此实验中，你将使用所谓的*reduced units*，它是无量纲的。它由势参数 $\sigma$, $\epsilon$  ,单个原子的质量M以及玻耳兹曼常数kB所导出。这意味着所有能量以$\epsilon$  为单位，所有长度以 $\epsilon$为单位。reduced temperature由$$k_BT/\epsilon$$等给出（见表1）。

![image-20210419012917262](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210419012917262.png)

## 1.3 力

$$E_{(r)} = U_{LJ} = 4\epsilon\begin{bmatrix}\begin{pmatrix}\sigma/r\end{pmatrix}^{12} - \begin{pmatrix}\sigma/r\end{pmatrix}^{6}\end{bmatrix}$$



## 2.1 实验

```

```



