---
title: 新型CipherLocker勒索病毒样本分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490620&idx=1&sn=1f15d4d4e729f1fd40eb907f6b94dda0&chksm=902fb314a7583a026539d88186b6fcf1b8120b7f30137ccf243f54d37ef55b4e144d5744c436&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-22
fetch_date: 2025-10-06T20:37:10.404837
---

# 新型CipherLocker勒索病毒样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6icm0YgibRGHSlY2yaVmCGnRiauapbg3F85wwHQg28rv22kYicxEnMGeibMzQ/0?wx_fmt=jpeg)

# 新型CipherLocker勒索病毒样本分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

最近几年勒索病毒已经席卷全球，全球范围内越来越多的政府、企业，组织机构等受到勒索病毒黑客组织的攻击，几乎每天都有企业被勒索病毒攻击的新闻被曝光，可能还有更多的企业被勒索病毒攻击之后，选择默默交纳赎金，由于勒索病毒太过于暴利，从而导致越来越多的黑客组织开始使用勒索病毒攻击。

前不久笔者群里就有人求助勒索病毒攻击事件，笔者写了相应的分析报告

[《新型勒索病毒使用BYOVD技术对抗安全软件》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490399&idx=1&sn=4930eda061bf1e37abec8fd94f44feee&scene=21#wechat_redirect)

近日这款又有人中招新型勒索病毒，找笔者求助，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6ic7RRIQmbZgcBgbdVXkzTzlQZuAWLArOHPdswQ7WMibdVVib2kjqDQw7jA/640?wx_fmt=png)

之前中招的企业，也是付费解密了，目前大多数主流的勒索病毒家族没有密钥的情况下都是无法解密的，有些勒索病毒加密的时候存在一些漏洞可以通过数据恢复的方法恢复部分数据，但也不保证数据的完整性，勒索病毒还是以防为主。

开年不久，就已经有多个勒索求助信息了，勒索还是挺多的，主要还是来钱快，直接搞钱不BB。

样本分析

1.这款新型勒索病毒使用C#语言开发，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6icyz29VZnlWzRT7G6nx5tBEdzXSDt1qMfTrxxnDshg05AJVPAAwXWKkg/640?wx_fmt=png)

2.需要使用管理员权限运行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6icYjIKkkxEt415r0wCDHFapick1Naph59J4Iq3B7Ke5jYm1AqTuibibYVBg/640?wx_fmt=png)

3.排除需要加密的指定的文件目录文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6ickqgbQ3JEu0NgqjFvx9qKBqqwHpSbC1J9zXCDj2R9NUKYnusPicmOCjw/640?wx_fmt=png)

4.获取需要加密的目标目录，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6icARibtvet5LOPqMibKAxG58qKOvf957SAVUno7W96Ok6C2AicqXicPJzDwg/640?wx_fmt=png)

5.指定需要加密的文件后缀，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6icbcMBaiaPEicd3ZUHM3D65F6qGhaB1y5cDXNNMxUia5mMic4ourKIwpMuKg/640?wx_fmt=png)

6.生成随机加密密钥，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6icnM4A0VsrrRS48ZHAuSorCUQuHd1zfF2fgwy65ZXIxEG2lbqpB0IZjA/640?wx_fmt=png)

7.使用AES加密算法，加密文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6ictxGicibG8hHVavRlLjM0V546ksmia8AicpMJmGL3Vtnj9FkXPc2txVsa1A/640?wx_fmt=png)

8.删除磁盘卷影、回收站文件、系统备份等，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6ic55Q9KCdG6yCmUe5KWudU5ehDpjXHjcicRx8flT52Xlw1HPia3Ln5HD9A/640?wx_fmt=png)

9.创建勒索提示信息文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6icOraFEUWYOZChCXZygrxLY6WU0036NtuziaaWKOJdBz5O8U8RqCdPXmw/640?wx_fmt=png)

10.记录文件加密的日志信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV6wUNOudkwk2ibwlEljLD6icUuauDcBjVZj0GzDibmaQ59Gy4LbiacdSrvictbnffmdq1Wc4VntIs4Cag/640?wx_fmt=png)

这个样本代码无混淆，逻辑清晰，应该是基于开源代码修改的，有兴趣的可以自行研究一下。

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

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