---
title: 银狐黑产木马最新免杀样本分析
url: https://mp.weixin.qq.com/s/6nCG9vIgA-y7abXvZBe4OA
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:23:22.642791
---

# 银狐黑产木马最新免杀样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVqZvx8tMJ31larb4M76OxkwP4YQzX8P4SHUlIiabWVqchc9OE0ibCMdbdPlUoCnLGWByYl8ZBMpVqA/0?wx_fmt=jpeg)

# 银狐黑产木马最新免杀样本分析

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器中沉浸阅读

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

最近几年银狐类黑产团伙非常活跃，今年这些黑产团伙会更加活跃，而且仍然会不断的更新自己的攻击样本，采用各种免杀方式，逃避安全厂商的检测，此前大部分银狐黑产团伙使用各种修改版的Gh0st远控作为其攻击武器，远程控制受害者主机之后，进行相关的网络犯罪活动。

除了银狐黑产团伙以外，还有一些其他黑产团伙也非常活跃，例如黑猫、GanbRun、暗蚊、金相狐、FaCai、DragonRank、夜枭等黑产团伙。

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUQE22huicEdFIb8UnlpbRNsdPrCBpKMOMib0KGjRycBZwiaiaWPZsaYrszWNST5cib7gUIiakY6jl0xosg/640?wx_fmt=png)

今年银狐攻击活动非常频繁，基本上每天都有新的Loader变种出现，免杀方式多种多样，同时今年还有很多银狐攻击样本通过使用正常的数字签名来逃避安全厂商的检测，增肥技术也是银狐木马今年最常使用的免杀技术之一，通过将恶意样本体积增加到100M以上来逃避安全厂商的静态扫描。

近日笔者在威胁情报平台捕获到一例银狐木马最新免杀样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVqZvx8tMJ31larb4M76OxkWg61bOch6Qc85OF2NedibCibaFLE5JRtn7zAMLoP9fMgMFz7PODdibTeA/640?wx_fmt=png)

该样本母体使用Rust语言编写，同时下载了多个ShellCode代码并调用执行，笔者针对该最新样本进行了相关分析，文未提供该攻击样本的完整威胁情报。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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