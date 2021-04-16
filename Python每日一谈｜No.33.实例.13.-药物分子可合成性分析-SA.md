---
title: Python每日一谈｜No.33.实例.13. 药物分子可合成性分析-SA
categories: Python每日一谈
top: true
---

#### 化学分子可及性分子

反正，你要做药物，或者不管做什么，都需要顾及到各种各样的条件，我们总是在所处的条件环境下进行选择或者进行实验。

化学分子合成性打分，简单来说，你想去合成一些分子，无法判断其合成难度。

当然前提是这些分子对你来说很有用，于是就出现了合成性打分。

我觉得比较少的分子的话，找个化学家让他自己判断一下就好，大批量的话，你总不能把化学家类似吧。

#### 打分

SAscore：这个比较常用，就药研小木子解释理念挺清楚的，我就复制粘贴了，你们知道的，我很懒。

> 2009年诺华公司的研究员Ertl和Schuffenhauer在化学信息学杂志上发表了名为SAscore的Rdkit插件用于快速评估药物分子的合成难易程度，其将小分子合成难易程度用1到10区间数值进行评价，越靠近1表明越容易合成，越靠近10表明合成越困难。其计算权重为化合物的片段贡献减去复杂程度（SAscore =fragmentScore − complexityPenalty），其中片段贡献值根据PubChem数据库中上百万分子计算共性进行计算，复杂度则考虑分子中非标准结构特征的占比，例如大环、非标准环的合并、立体异构和分子量大小等方面。研究员将40个化合物给化学家进行经验性评估其合成难易程度，并与SAscore得分进行比较发现与化学家给出的合成难易程度评分的相关性R2高达0.89，表明其在识别可合成难易程度上的可靠性较高。如下图所示，蓝色表示化学家给出的合成难易程度，红色表示SAscore给出的合成难易程度分值：

![Image](/Users/sujiaqi/Pictures/Typora/640.png)

### 代码

1. 找到仓库

   https://github.com/rdkit/rdkit/tree/master/Contrib/SA_Score

   ![image-20210408215954604](/Users/sujiaqi/Pictures/Typora/image-20210408215954604.png)

   两个主文件：[sascorer.py](https://github.com/rdkit/rdkit/blob/master/Contrib/SA_Score/sascorer.py)，[fpscores.pkl.gz](https://github.com/rdkit/rdkit/blob/master/Contrib/SA_Score/fpscores.pkl.gz)

   把这两个下载下来

2. sascorer.py

   我优化了一下

   本来想大刀阔斧的改一遍，有点浪费时间。

   脚本在后面，只要把fpscores.pkl.gz放在当前目录下就能运行，现在我的用法就是

   ```python
   In [62]: m = Chem.MolFromSmiles('C1CCCCC1')
   
   In [63]: x = [m,m,m,m]
    
   In [64]: my_score(x)
   smiles	sa_score
   C1CCCCC1		1.000000
   C1CCCCC1		1.000000
   C1CCCCC1		1.000000
   C1CCCCC1		1.000000
   ```

   好了，下面是脚本，直接复制粘贴到ipython中就能运行或者，你自己随便搞点使用模式随便用。完事，睡觉

   ```python
   
   import math
   import pickle
   
   
   from rdkit import Chem
   from rdkit.Chem import rdMolDescriptors
   
   import os
   import os.path as op
   
   _fscores = None
   
   
   def readFragmentScores(name='fpscores'):
       import gzip
       global _fscores
       # generate the full path filename:
       if name == "fpscores":
           name = op.join(os.getcwd(), name)
           # name = op.join(op.dirname(__file__), name)
       data = pickle.load(gzip.open('%s.pkl.gz' % name))
       outDict = {}
       for i in data:
           for j in range(1, len(i)):
               outDict[i[j]] = float(i[0])
       _fscores = outDict
   
   
   def numBridgeheadsAndSpiro(mol, ri=None):
       nSpiro = rdMolDescriptors.CalcNumSpiroAtoms(mol)
       nBridgehead = rdMolDescriptors.CalcNumBridgeheadAtoms(mol)
       return nBridgehead, nSpiro
   
   
   def calculateScore(m):
       if _fscores is None:
           readFragmentScores()
   
       # fragment score
       fp = rdMolDescriptors.GetMorganFingerprint(m,
                                                  2)  # <- 2 is the *radius* of the circular fingerprint
       fps = fp.GetNonzeroElements()
       score1 = 0.
       nf = 0
       for bitId, v in fps.items():
           nf += v
           sfp = bitId
           score1 += _fscores.get(sfp, -4) * v
       score1 /= nf
   
       # features score
       nAtoms = m.GetNumAtoms()
       nChiralCenters = len(Chem.FindMolChiralCenters(m, includeUnassigned=True))
       ri = m.GetRingInfo()
       nBridgeheads, nSpiro = numBridgeheadsAndSpiro(m, ri)
       nMacrocycles = 0
       for x in ri.AtomRings():
           if len(x) > 8:
               nMacrocycles += 1
   
       sizePenalty = nAtoms**1.005 - nAtoms
       stereoPenalty = math.log10(nChiralCenters + 1)
       spiroPenalty = math.log10(nSpiro + 1)
       bridgePenalty = math.log10(nBridgeheads + 1)
       macrocyclePenalty = 0.
       # ---------------------------------------
       # This differs from the paper, which defines:
       #  macrocyclePenalty = math.log10(nMacrocycles+1)
       # This form generates better results when 2 or more macrocycles are present
       if nMacrocycles > 0:
           macrocyclePenalty = math.log10(2)
   
       score2 = 0. - sizePenalty - stereoPenalty - spiroPenalty - bridgePenalty - macrocyclePenalty
   
       # correction for the fingerprint density
       # not in the original publication, added in version 1.1
       # to make highly symmetrical molecules easier to synthetise
       score3 = 0.
       if nAtoms > len(fps):
           score3 = math.log(float(nAtoms) / len(fps)) * .5
   
       sascore = score1 + score2 + score3
   
       # need to transform "raw" value into scale between 1 and 10
       min = -4.0
       max = 2.5
       sascore = 11. - (sascore - min + 1) / (max - min) * 9.
       # smooth the 10-end
       if sascore > 8.:
           sascore = 8. + math.log(sascore + 1. - 9.)
       if sascore > 10.:
           sascore = 10.0
       elif sascore < 1.:
           sascore = 1.0
   
       return sascore
   
   
   def my_score(mols:list):
       readFragmentScores("fpscores")
       print('smiles\tsa_score')
       for m in mols:
           s = calculateScore(m)
           smiles = Chem.MolToSmiles(m)
           print(smiles + "\t" + "\t%3f" % s)
   ```

   

