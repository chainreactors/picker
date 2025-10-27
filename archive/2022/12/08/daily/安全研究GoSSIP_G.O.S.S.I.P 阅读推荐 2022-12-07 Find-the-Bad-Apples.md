---
title: G.O.S.S.I.P 阅读推荐 2022-12-07 Find-the-Bad-Apples
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493519&idx=1&sn=256fb36ebf2b65ff9505e995e3a36b0b&chksm=c063c956f7144040f674a04af5478cf13c56f32ca0c9a2c542c6e87b902fe59822b5c29e99d9&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-12-08
fetch_date: 2025-10-04T00:53:48.841910
---

# G.O.S.S.I.P 阅读推荐 2022-12-07 Find-the-Bad-Apples

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cSchFribbWDSjD7HNBLwCjNzibTCMbFujoxuCYIVdNbawJAoA2GK2Wvwg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-12-07 Find-the-Bad-Apples

原创

沈牧言、程池

安全研究GoSSIP

“借问瘟君欲何往，纸船明烛照天烧”，我们要感谢正是“纸船明烛”送走了“瘟神”，也知道祖国的未来终于会属于年轻的一代，今天就要给大家推送一项由杰出的年轻人主导的研究工作。在这篇由中国地质大学（武汉）程池老师团队和瑞典隆德大学郭骞老师合作完成的CHES 2023研究论文 *Find the Bad Apples: An efficient method for perfect key recovery under imperfect SCA oracles – A case study of Kyber* 中，第一作者沈牧言刚刚大四，就已经针对格公钥密码的侧信道安全性研究取得了优异的成果。特别值得一提的是，在开展这项研究的过程中，国内疫情（特别是2022年）对大学学习生活产生了严重干扰，从而更显得此项成果来之不易。论文以抗量子密码算法Kyber为例，对实际侧信道攻击中可能存在噪声或干扰问题提出了一种处理方案。相比于传统的多数投票（Majority-Voting）等方法，该方法能减少约一半的问询次数。接收该论文的CHES是由国际密码协会（IACR）主办的密码工程与物理安全方向的旗舰会议，会议上的论文展现了国际学术界和产业界在密码芯片、密码嵌入式系统领域的最高水平。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cJaOCZy1BYwicicNjg91q8JwqpZLcEOsiafW8E0yde9parCicwovjRBhApw/640?wx_fmt=png)

随着量子计算机技术的高速发展，目前广泛使用的基于大整数因子分解和离散对数问题构建的公钥密码学体制将不再安全。美国国家标准技术研究院（NIST）从2016 年开始征集抗量子密码算法标准，在NIST第三轮筛选中，共有4个密钥封装方案和3个数字签名方案候选。2022年7月，NIST公布了最新的待标准化算法的筛选结果。`Kyber`在4个候选密钥封装方案（KEM）中成为了唯一被选中进行标准化的算法，这意味着在接下来的几年里，`Kyber`将广泛地被适配和应用在各种计算平台上。而我们推荐的这篇论文的主要研究对象也是`Kyber`，关注的是`Kyber`在实现中的侧信道安全。

密码算法的侧信道安全作为密码实例化安全中的一个重要领域，近年来受到学术界和工业界的高度关注。对抗量子KEM算法的侧信道攻击目标通常是服务器复用的私钥，相关攻击可归为两大类：

* 第一大类中敌手借助攻击解密结果（Message）来逐步恢复出私钥，敌手借助精心构造密文，以及判断Message?= Targeted\_Message来每次获得1bit信息，具有较强的通用性，但效率通常不高；
* 第二大类中敌手以算法的特定组件（如NTT）为攻击对象，效率更高但依赖特定的目标架构、以及代码编译方式等因素。

本文基于的攻击模型是第一大类中的Plaintext-Checking Oracle-based Attack，也可称为Key Mismatch Attack（在之前我们推送过关于该攻击的另一篇亚密会论文，见G.O.S.S.I.P 学术论文推荐 2021-09-27）。论文关注了侧信道分析在具体实践中的所面临的额外挑战：受环境噪音、测量方式等因素影响，获取到的信息比特可能翻转，进而导致恢复的密钥出现差错。传统的做法通常通过多数投票、或波形聚合等方法来确保密钥恢复的准确性。在论文中作者提出了一种新的解决方案，对基于格构建的KEM算法具有一定通用性，其基本思想是“粗粒度恢复-检错-纠错”。与论文标题“Find the Bad Apples”对应，这一思路最大的挑战在于设计“检错”步骤。作者借助已恢复的私钥信息进行密文重构设计了一套特殊的“检错”密文，并运用了编码的相关理论在原有的攻击模型（即Oracle）下完成了一套检错方案。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3ccEib4SfUdp48n6ePFKqvgic3NXwECibZU6niaxc72Xhib8e2VYmJGPbNSPg/640?wx_fmt=png)

由于密文选取需紧密与算法本身性质结合，并非每一种编码方式都存在对应的密文。下图是一种可行的验证系数块(0,2)的编码方式，作者将(0,2)编码到一个特殊码字“01”上，用这个独特的Oracle返回值序列区分出其他系数块值。为寻找出类似的密文来检测所有系数块的可能值，作者首先对符合条件的密文特征进行了理论分析，给出了相关引理并进行了证明。随后结合穷举搜索和分治法得到了所有密文，实现了通过两次问询检测四个系数的高效检错方法。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cL6D2PPjvpev5urnTAre5xMFvSlLGMZpRbIIZshnT35W1iaot3WcJgRg/640?wx_fmt=png)

注意到对于噪声更强的环境，“检错”这一过程本身也可能出错，作者提出了一种Mix-voting方法来解决应对。进而，论文提出的密钥恢复方法在多种环境下都有较好的表现。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3c4Nvb6ld7V792d5fJGLibd5vgaSF7f0tFia9yKA5zMWqN5kLRbptLYwXQ/640?wx_fmt=png)

论文采用了模拟实验和板上实验相结合的方式进行评估与验证，并与多数投票消错（Ravi等人在CHES2020上使用）以及波形聚合消错（Ueno等人在CHES2022使用，为目前最好结果）两种方法进行了对比。实验结果表明，该论文中方法相比于后者可以减少45.9%, 55.4%的总问询次数。在此同时，类似于Ueno 等人的效果，该论文提出的方法可以成功恢复几乎全部的多项式系数，即在512个系数中平均只有0.04或0.05个发生错误。

---

> 论文PDF：https://tches.iacr.org/index.php/TCHES/article/view/9948
> 相关代码：https://github.com/7a17/Find-the-Bad-Apples/

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过