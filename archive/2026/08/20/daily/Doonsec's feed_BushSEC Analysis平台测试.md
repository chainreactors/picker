---
title: BushSEC Analysis平台测试
url: https://mp.weixin.qq.com/s/Qzu_DMhJOLzse4GHPkdfTQ
source: Doonsec's feed
date: 2026-08-20
fetch_date: 2026-08-21T03:01:16.195331
---

# BushSEC Analysis平台测试

# BushSEC Analysis平台测试

知微守望

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于EclipseRift
，作者BushSEC

![](https://wx.qlogo.cn/mmhead/0sDCa2E8S1tKzicucv7l1LNMMvjnicQqIvBZ1kNk19NOia7YM2XiaZPnCtEHwTjsEALrSMPzFUmMUys/0)

**EclipseRift**
.

心怀热爱，愿心中的赤诚永不熄灭

随着人工智能技术快速发展，恶意代码的生成、修改与迭代门槛正在不断降低。
对于红队研究、安全测试乃至真实攻击活动而言，一个恶意样本可以在很短时间内完成多轮变种：修改代码结构、更换通信方式、混淆关键逻辑，甚至针对不同检测环境快速调整行为特征。
恶意样本的迭代速度正在加快，但传统分析方式仍然高度依赖人工经验。
传统逆向分析足够严谨，也足够精确，但面对越来越多、变化越来越快的样本时，分析人员往往需要在大量函数、字符串、调用关系和可疑行为中反复排查。一个复杂样本的完整分析，可能需要数小时，甚至更长时间。

### BushSEC Analysis

**DRX智析-BushSEC Analysis** 是由 BushSEC 推出的恶意样本智能分析平台。
我们希望通过人工智能辅助安全分析人员，更快地理解一个未知样本：

```
它可能做了什么；哪些函数值得重点关注；不同行为之间是否存在联系；哪些内容能够支撑最终判断；一个可疑行为是如何逐步形成的。
```

BushSEC Analysis 不只是生成一段笼统的风险描述，而是尝试从样本内部逐步寻找线索，将可疑函数、行为关系、关键证据与调查过程连接起来。
用户既可以快速查看整体分析结果，也可以继续深入具体函数与证据，了解平台为什么得出相应结论。
我们希望最终呈现的，不再是一句简单的“恶意”或“安全”，而是一份**能够追溯、****能够检查、能够辅助人工研判的分析结果**。

**分析速度，正在逐渐成为新的瓶颈。**

### 让大模型直接分析代码，真的可行吗？

大模型为恶意样本分析带来了新的可能。
它能够阅读代码、理解逻辑、总结行为，也能够帮助分析人员快速定位可疑内容。但在实际使用中，单纯把恶意样本代码交给大模型，并不能直接解决问题。
相反，它可能带来几个更隐蔽的风险。
为了控制分析内容，大量代码通常会被提前筛选或裁剪。一旦真正关键的函数没有被选中，就可能造成漏判。
当上下文不足时，模型还可能“自信地”引用并不存在的函数地址、系统接口或调用关系，给出看似专业、实际上无法验证的结论。
更常见的问题是，一份分析报告写得很完整，却无法回答一个最基本的问题：

**这个结论的证据在哪里？**

此外，大模型本身对特定恶意代码、底层行为和专业安全知识的理解也存在边界。当已有知识不足，或者样本逻辑超出模型认知范围时，模型可能通过猜测补全结论，进而产生误报。
因此，我们认为，真正有价值的 AI 恶意样本分析，不应该只是“让模型读一遍代码”。
它还需要能够持续调查、回溯依据，并将每一个关键判断落到可以检查的证据上。

传统检测引擎，可能会被各种混淆或者加密绕过,
这个就相当于人工分析代码,所以各种花里胡哨的混淆，注入反而会被标记成恶意

### 产品一览

#### 样本分析概览

上传样本后，平台会对文件进行整体分析，并展示样本的基础信息、风险判断、可疑行为以及主要分析结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VIJdfjNCVs4n1vUibpw3AHkVdw9XcCiam4zSzynlib4bsC4Kx3oKjbiaEzvBsVLYrmBibPLhIQe9st0uerEiaBHTS6jTYttA5qrUqKbPaORT7mDTs/640?wx_fmt=other&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_jpg/VIJdfjNCVs5bSgATW2WgcpzfugXgIib3cm2UHOYHrOFia6FdzzWNo6EKblH1aloZFl2wBxian5vHagJmEWfiaGVmyZs3TofCIRLZkjVWCXiahvu4/640?wx_fmt=other&from=appmsg)

#### 风险行为与分析结果

平台会对样本中发现的可疑内容进行整理，帮助用户快速了解样本可能涉及的主要行为和风险方向。

![](https://mmbiz.qpic.cn/mmbiz_jpg/VIJdfjNCVs7rvl11qY3kGOnWVR4WWUWfsIjlKvxP7Ew8ibsu3Y00BkJia0Lfick8ERjCG9mYnrCT1KPDJeDv4of3ZvLXwwnRfFZqcwT1u8ia8Gs/640?wx_fmt=other&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_jpg/VIJdfjNCVs4amTrNwQJX8qCZDzicfiacKq5rLfzjhoYX0ycXO9hBpUOibvWYGM4pNX5RdMvfzbAIdehcpeqQGOMY80CegMibruElQNMh0eBPdUQ/640?wx_fmt=other&from=appmsg)

#### 检测到的恶意函数

对于分析过程中发现的高风险函数，平台会进行集中展示。
用户可以进一步查看函数用途、可疑原因以及它与其他行为之间的关系，从而减少在大量无关代码中反复排查的时间。

![](https://mmbiz.qpic.cn/mmbiz_jpg/VIJdfjNCVs7vXshN2WDoXBYUnCiaXlKDqiaStL3QYiaWcAGRibEQSRED2lo9EorSmPHzEQxywk62XsqERiaXeey69YkUBlCFib1aWibP3Ra3wOcSvQ/640?wx_fmt=other&from=appmsg)

#### 证据链

一个结论不应该只有描述，还应该有能够支撑它的依据。
BushSEC Analysis 会尽可能将关键判断与对应证据关联起来，帮助用户了解某项恶意行为是根据哪些函数、调用关系或样本特征得出的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/VIJdfjNCVs6Mb1d7ojVMXKaGHojzjaWS7CNfx09NndlialW2CRVSLfE3j5CJGez2kPc5N1De1SQtKyH2n9YjFibt3ibltqibFMJL9lUHgk7WUQ4/640?wx_fmt=other&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_jpg/VIJdfjNCVs7HMg5b4cvoepDsuHOTZfIdjBPgSuLDtHB22zwEQwVvOmlJ3Sm5s8xEj0YfAKib1D9RrprXvgBLiajm6LGx7tm7MAIBYaMybZcMs/640?wx_fmt=other&from=appmsg)

#### 智能调查事件链

对于复杂样本，单个函数往往无法反映完整行为。
平台会尝试将分析过程中发现的多个线索进行关联，按照调查过程梳理样本中的关键事件，帮助用户理解不同恶意行为之间可能存在的先后关系和逻辑联系。

![](https://mmbiz.qpic.cn/mmbiz_jpg/VIJdfjNCVs4J5AZxpXmBuMvS64viaoVzVgb7zhkPFpOqAPm59fvIda5aGGreiaHfXwxnNmgHXiad2PlfeO0lvOG2cHcJU9JyQrl1h93m5FrSJ4/640?wx_fmt=other&from=appmsg)

### 我们仍处于起点

BushSEC Analysis 目前仍处于产品早期阶段。
现阶段，平台主要支持 **Windows PE 文件**，暂不支持 APK、ELF、Office 文档、脚本文件及其他文件类型。

由于不同恶意样本在编译方式、代码结构、混淆强度和保护手段上存在较大差异，当前分析结果仍可能出现遗漏、误报或理解偏差。
BushSEC Analysis 的定位并不是完全替代人工逆向分析，也不是以一次自动分析结果代替专业研判。
我们更希望它成为安全分析过程中的一名助手：
在面对未知样本时，先帮助用户快速建立整体认知；在深入分析时，帮助用户定位值得关注的方向；在形成结论时，尽可能提供能够回溯和验证的依据。
对于高风险样本、复杂攻击活动以及需要形成正式结论的场景，我们仍然建议结合人工分析、动态行为验证和其他安全工具进行综合判断。

### 写在最后

恶意代码不会因为分析困难而停止迭代。
安全分析工具也不应该只停留在输出一个检测结果。
BushSEC Analysis 目前还不完善，也可能存在许多不足。
但我们希望从这里开始，探索一种更高效、更透明，也更有证据支撑的恶意样本分析方式。
**让每一个判断，都有迹可循。**

### 体验

由于考虑服务器的负载情况，我们暂时只考虑开放共50个体验名额，可以通过下方qq群二维码加入体验群，我们根据每个人的情况酌情考虑通过。
![](https://mmbiz.qpic.cn/mmbiz_jpg/VIJdfjNCVs4jj01E8jdepgaB6VFjvmTdaVhpHVnouibX0SGibgxo3Nhe3ew9H3KI4hlKMNF37Xc6N6m4iazh13XdZiahPvSvbaT9acHBafZe8TM/640?wx_fmt=other&from=appmsg)

### 加入我们

我们正在寻找对恶意代码分析、逆向工程、人工智能、安全产品研发 感兴趣的伙伴。无论你擅长安全研究、大模型应用、Agent 系统，还是产品体验与视觉设计，只要愿意投入时间、分享想法，并参与实际开发，都欢迎加入。
联系邮箱:bushsec@111.com

### Tips

顺带一提，DRX红队Agent已开源，虽然还有待完善， 给孩子来点 Star 吧 xdm。

```
https://github.com/BushANQ/DRX-Operator
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VIJdfjNCVs56sm2dlF0tImBSkITqibCnzyb3q9QnEMZzHGSH5X8gh9IiayD8HoK7zjaOu89GRLRwwwb9XQIvZ5GV7pcZSlyqd8GD6YauB7ic50/640?wx_fmt=other&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVznM3J1P2rCBhHMicAuicI6usVmTx3l2tyGU2kqmGhmqAt07d1sa9JptK3IuiakDnzAq5deRznMefg6g/0?wx_fmt=png)

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