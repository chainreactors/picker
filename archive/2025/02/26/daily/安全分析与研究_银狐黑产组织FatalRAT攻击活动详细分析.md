---
title: 银狐黑产组织FatalRAT攻击活动详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490706&idx=1&sn=d8f1fc31ace36622c8c6c890990c90fe&chksm=902fb3baa7583aac468da5b6789ed2dc6d2c6f0223c0523e4ffa864edf8aa827cf11a85acfa5&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-26
fetch_date: 2025-10-06T20:37:11.072049
---

# 银狐黑产组织FatalRAT攻击活动详细分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyX2D23a4tJlDD3tF3znt2ORfXicuDhVYVpXQavCVHFicmZyQLtLBib24Hkg/0?wx_fmt=jpeg)

# 银狐黑产组织FatalRAT攻击活动详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

近日卡巴斯基披露了一种专门针对亚太地区各种工业组织的FatalRAT攻击活动，该攻击活动中使用了一个命名为梵高的远控样本，攻击者使用合法的云内容交付网络(CDN)，例如myqcloud和有道云笔记服务等作为其攻击基础设施的一部分，采用复杂的多阶段有效载荷交付框架来逃避各大安全厂商的检测。

原报告链接：

https://ics-cert.kaspersky.com/publications/reports/2025/02/24/fatalrat-attacks-in-apac-backdoor-delivered-via-an-overly-long-infection-chain-to-chinese-speaking-targets/

卡巴斯基报道的这些攻击活动，在国内有一个统一的称号就是“银狐”黑产组织，使用各种RAT远控工具进行各种黑灰产活动，这些远控工具包含：各种修改版本的Gh0st RAT、SimayRAT、Zegost RAT 和 FatalRAT等。

通过威胁情报网站，查询卡巴斯基披露的攻击活动相关基础设施，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXC1ibgyOmPbIpOSzLLJibP5O5cMgQXWOe224CBwZmsFia0VDxSSMfHpPFQ/640?wx_fmt=png)

关联到相关的样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXC7JXxzSzLpo6diaXmNhwRriaobgCSg4yIKFPF42K7Z8o9icAIpzByqlbQ/640?wx_fmt=png)

笔者通过微步威胁情报平台进行关联分析，下载相关的样本对该攻击活动进行了详细分析。

样本分析

1.母体样本使用UPX加壳，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyX9sgytFeMXhnc5AcaQWsRjBsTNdEUVrPhxgGjEFQY703dnCSGeLnEkA/640?wx_fmt=png)

2.使用UPX工具脱壳，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXicEe2SibSB6aicefONIu41TAJqqaaCXIgYmibP6IksX98L7x2zP6zY1Gicw/640?wx_fmt=png)

3.样本的PDB信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyX9kakBOxKLlKfyAMSxNaLHtJrWVSB8dLPpnMaYapw30IwUIk5YNnhNQ/640?wx_fmt=png)

4.从远程服务器上下载一个JSON配置文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXoGMhaYwwwlZafI4VmNsKoyYxZUn0EDdGia2ibSaibt5hfJ3eBJ6TOEQUQ/640?wx_fmt=png)

5.解析JSON配置文件内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyX5927cMWWXTe2WfpUghFicicOV5JsJhSmdMWq1I4OGicic9bDiaDA10dGqaw/640?wx_fmt=png)

6.按JSON配置文件顺序，依次下载相关的恶意加密文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXXt8DAcicQAHZQ6ndJj5rP0KhBEdicLe0SloIjCFiaC0IIPVVibtgud1JSQ/640?wx_fmt=png)

7.解密加密的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXBu5I6Vn18kY8CpI6OmOuibFScibqbZCurgTqHfqOSQdGvIZQ1tJL0gdA/640?wx_fmt=png)

8.下载第一阶段DLL的PDB信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXKpibzH5ibHicLGn4jYB3vwKJWwRRrnc1r7DmVucFfyLVBpSQg18Uwd1Lw/640?wx_fmt=png)

9.从远程服务器下载加密的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXfME6mPWsVBMPFF1Lqt731qWmOOmo1eZ3LV4OvnFibXC6uhiczZ6QQueg/640?wx_fmt=png)

10.下载第二阶段的DLL的PDB信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyX8yIhbmIpASf42jFTWOFhC7osYz0X5FqFtlqEAxRasXRqUonz7MhMYQ/640?wx_fmt=png)

11.读取配置文件中加密文件信息，解密加密的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXnuHicKbkojSGpOicBGhpEMrMWchtYN7sP31AX3jOiawEqkcHDmk3ibxzgg/640?wx_fmt=png)

12.生成加密的压缩包文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXR3wpkAic7AR40lQZibRzSM6x7QDuTwCXshKcTg4MXO30XibrUKtdibNK5w/640?wx_fmt=png)

13.解压缩之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXicibCkmcnjBFfK741eVqcDn0ricJ0lyFsHmRichicsnJNA78kXEgGkmmkAA/640?wx_fmt=png)

14.BAT脚本文件内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXhrNGndicZ1yPSAKJgBFib2OXbfJAMLr6OKlXTno3DKJdjkaR6OE6S0vw/640?wx_fmt=png)

15.采用白+黑方式加载执行恶意DLL模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXL1M6O96eopicmebiaBU52PFpJ7flM7axib50DeRaH7vG5Tmoszib8YibV1Q/640?wx_fmt=png)

16.获取到第三阶段的DLL的PDB信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyX6Z5PNDz6WJ6zvP3WxdDGHjk8qYR3rbo1mc2DBu5DBANKdRNmrkQjWg/640?wx_fmt=png)

17.最后通过第三阶段的DLL从远程服务器下载最终的FatalRAT远控，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXWWEnWIGwpPfbQUZTKUeTSVEd6jvCJiawicpJ8aaHytTkOoKMnypDFAEA/640?wx_fmt=png)

到此整个FatalRAT远控攻击活动就完整的还原了，中间使用了梵高远控攻击样本，整个分析过程比较复杂，样本使用了多种加壳，混淆以及免杀技术，有兴趣的可以自行研究一下，有啥问题再交流。

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

对恶意样本分析感兴趣的，但是又完全没有基础的读者，可以学习笔者的《恶意软件分析基础教程》，基本上是从零基础开始入门恶意软件分析。

[1.汇编语言基础知识必备](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490098&idx=1&sn=ed0be305f2c8c9de0fff326bc45f1ce9&scene=21#wechat_redirect)

[2.恶意样本分析环境搭建](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490186&idx=1&sn=dbccef63b6ad18308eec7ebf88455def&scene=21#wechat_redirect)

[3.恶意样本静态分析-上](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490311&idx=1&sn=3ddb48128acc2772763bd99ba4cf850a&scene=21#wechat_redirect)

[4.恶意样本静态分析-下](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490352&idx=1&sn=7a485e1264bc2f1a221a0822e46ac1c3&scene=21#wechat_redirect)

[5.恶意样本动态分析-上](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490380&idx=1&sn=eab7072e40253f683bc6d1c2e68ac8c7&scene=21#wechat_redirect)

[6.恶意样本动态分析-下](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490447&idx=1&sn=c7cf5c60d80febdcde3d62e977e3b04b&scene=21#wechat_redirect)

[7.恶意样本反调试反分析](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490541&idx=1&sn=c69072f45da7f28ba4f9d3b1d36842f0&scene=21#wechat_redirect)

对高级恶意软件分析和研究感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族，笔者今年打算深度跟踪分析一些全球最顶级的TOP恶意软件家族，这些恶意软件家族都是全球最流行的，也是黑客攻击活动中最常见的恶意软件家族，被广泛应用到各种勒索攻击、黑灰产攻击、APT窃密攻击活动当中以达到攻击目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVibz1lILTxQIJaB6DqPOSAUghodibssAyprGx5CIumn6vluNfuuF4ia4DU6d2WbGFbFcqO98hgWyuyA/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

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