---
title: G.O.S.S.I.P 阅读推荐 2022-11-11
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493230&idx=1&sn=e50ac23a73cf42aceebe31facba35263&chksm=c063c8b7f71441a175ed78efcc6212167c3d3bd142e899ef2cdd5ca7db31402f063de26adfc5&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-11-12
fetch_date: 2025-10-03T22:33:02.434303
---

# G.O.S.S.I.P 阅读推荐 2022-11-11

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21FeYZ8L23Y7hyg6LqYGE45G41sQGU4kHWzgy7FzLZiaGukdPRM8onzeh64zSIAeiciajKCz8qiaOiaIWAg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-11-11

原创

Hurrison

安全研究GoSSIP

双十一最重要的是什么，是买买买吗？当然不是！如果没有现在大家都在用的移动支付，怎么可能有今天的盛况，所以在这个购物狂欢节，我们当然要给大家推荐一篇关于支付安全相关的ACSAC 2022研究论文——*Analysis of Payment Service Provider SDKs in Android*，作者包括来自PayPal的研究人员（什么时候支付宝的研究人员也能发表支付安全的研究论文呢~）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FeYZ8L23Y7hyg6LqYGE45GpuCIicGf32KeWiaibYIaawKh8skKQSZhmzJd6aFdjRRHN5P3thKjVF62Q/640?wx_fmt=png)

## 前言

> 1985年，英国87%的付款方式为现金，但到了2019年，这一比例只有23%。在中国的城市地区，作为最受欢迎的两种支付服务，支付宝和微信的使用率早在疫情来袭之前就在飙升。2018年的一项研究发现，98%的城市智能手机用户使用手机进行移动支付。

随着互联网的发展，再加上疫情的影响，现在使用现金支付的人已经越来越少，大多数人已经信任电子设备来进行支付。移动设备是现代数字支付生态系统的重要组成部分。支付应用程序中的安全漏洞可能允许设备上的恶意应用程序和网络中的路径上攻击者窃取支付凭据和劫持交易。Android APP 通常使用了某些支付服务提供商(PSP)的 SDK 来进行电子交易。

如果 SDK 中存在安全漏洞，那么将会导致大量 APP 存在被攻击的风险。在2017年，G.O.S.S.I.P在NDSS会议上发表了可能是第一篇系统性研究Android平台三方支付安全（并发现了大量安全问题）的研究论文——*Show Me the Money! Finding Flawed Implementations of Third-party In-app Payment in Android Apps*，而后又发表了扩展研究——*Security analysis of third-party in-app payment in mobile applications*，将分析扩展到iOS平台，发现问题同样存在。而在今天推荐的这篇论文中，作者构建了 AARDroid 工具，静态分析支付 SDK中的安全问题。作者基于 数据流分析 和 自然语言处理 构建了 AARDroid 来静态分析支付 SDK。作者将AARDroid应用于50个支付 SDK，并发现了一些安全缺陷，包括将未加密的信用卡信息保存到文件中、使用不安全的加密原语、信用卡信息的不安全输入法以及WebViews的不安全使用。

## 静态分析内容

在静态分析方面，作者参考了四类MASVS标准，共28个检查

* 数据存储与隐私保护 (DS1-DS12)
* 密码学 (CRYPTO1-CRYPTO4)
* 网络通信 (TLS1-TLS4)
* 平台交互 (PLAT1-PLAT8)

关于MASVS标准的详细内容，读者可以参考官方网站，也可以直接阅读论文，作者用了大量篇幅介绍这些标准

* https://mas.owasp.org/
* Download the MASVS (https://github.com/OWASP/owasp-masvs/releases/latest/download/OWASP\_MASVS-v1.4.2-en.pdf)

## 静态分析方法

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FeYZ8L23Y7hyg6LqYGE45GNPj4GkMKskV06yyeXjVpb33NNB5h2qpodVpAibw5OrOticiac9ENXz16Q/640?wx_fmt=png)

作者发现现有的数据流分析工具 FlowDroid (https://github.com/secure-software-engineering/FlowDroid) 和 ArgusSAF (https://github.com/arguslab/Argus-SAF) 只能分析 `.apk` 文件并且只关注了常见的 Android Framework API ，但是 SDK 通常是 `.aar` 文件，API 也是自定义的。所以作者修改了ArgusSAF 来满足分析的需要，首先使用一个模版包含 SDK 编译为 `.apk` 文件，在 ArgusSAF 生成的 IR 中插入对 SDK API 的虚拟调用来触发对SDK的分析，最后生成 ICFG (interprocedural control flow graphs)。MASVS数据流检查需要识别从API源到特定接收器集的污染路径，作者使用了类似于 Cardpliance (https://www.usenix.org/conference/usenixsecurity20/presentation/mahmud) 提到的方法捕获路径。

通常来说，对SDK中所有的 API 都进行分析往往不可行，所以需要确定一些敏感的 API，然后只对它们进行分析。作者认为敏感的支付信息（信用卡号和CVC代码等）主要是字符串数据，所以遍历SDK生成抽象语法树（AST）来识别具有字符串参数的 API，同时保留了API参数的信息进行精确的污点跟踪，并对 API方法和其参数的名字进行语义分析，但是发现仅通过这样的过滤留下的 API 仍然不太好，包含了很多无关的 API。作者又通过了对方法的交叉引用和成员变量中的字符串变量名进一步优化结果。作者基于 PolicyLint (https://www.usenix.org/conference/usenixsecurity19/presentation/andow) 添加了492个叶子节点建立 Data Ontology，并将 41个 SDK中的参数名(手动移除了一些明显不相关的) 在其中的包含情况，发现有74%存在于 Data Ontology。信息敏感的程度也是不同的，作者手动将这些信息分为高（信用卡号、CVC、银行账户号等）、中（电话号码、帐户信息、IMEI等）、低（URL、设备信息、国家等）三个等级。

## 实验

许多支付服务提供商并没有公开SDK，所以作者只能从GitHub、JCenter、Maven等平台中收集了50个Android支付SDK。其中有9个无法提取 API 语义，24个没有提供UI。

作者选择了未混淆的SDK中的5个(≈12 % )来衡量敏感API识别的准确性，结果如下

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FeYZ8L23Y7hyg6LqYGE45GAvGI7bQ6Ycxdo728oG9oibMSquiamwWPRrsW4q5yIZFuIfQ00t4sK0Ag/640?wx_fmt=png)

检测数据集的总共97个API中有14个被错误地剔除(假阴性)，在标记为敏感的37个 API 中，有5个不敏感(假阳性)

之后对MASVS标准检测的评估中作者手动分析了SDK代码，以确定真阳性还是假阳性，结果如下

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FeYZ8L23Y7hyg6LqYGE45GwftwhEQJjnCC3Nkmp5c8ftDibBJRNG3OROgNc8fx5n8TwT4NGGenNeg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FeYZ8L23Y7hyg6LqYGE45GSwT7fZhYlaWZqoahMrGs7j1bZo9rH7Al2f4c24w4c4iaWibYd5dbnnoQ/640?wx_fmt=png)

AARDroid总共报告了17个付款SDK中的51个数据流警报。作者手动识别了5个假阳性情况，这是由模糊参数名(例如, "账户"被解释为金融账户信息)的错误分类和第三方URL的错误识别造成的。对于这种SDK级别的测量，AARDroid基于数据流的检查具有大于90 %的精度

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FeYZ8L23Y7hyg6LqYGE45GK5PCqwUujLkKev8Khtg6EouSqEKGicZpP3QbqNcquWrxGxWpsP6dUMQ/640?wx_fmt=png)

使用WebViews的26个SDK都没有按照MASVS标准配置

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FeYZ8L23Y7hyg6LqYGE45GqJDQbDQF0jDWwHnVG2FY0alWq87oalHEuAjoeMTXBxRVfw7rT6y2Ng/640?wx_fmt=png)

在9个SDK的清单文件中发现了16个危险的权限。其中有4个权限在的SDK中没有任何可识别的用途

## 贡献

* 提出AARDroid静态程序分析框架，用于测试Android应用程序SDK上的OWASP MASVS需求。AARDroid 分析了MASVS需求的四个类别，能够自动分析SDK。
* 提出了为SDK定制数据流分析的技术。AARDroid 将SDK打包到应用程序中，并使用安全敏感术语的特定领域本体来获取安全相关API的语义。
* 通过 AARDroid分析了50个支付SDK，发现了许多支付SDK中的具体安全缺陷

---

论文链接 https://saminmahmud.com/files/papers/acsac22-mahmud.pdf

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