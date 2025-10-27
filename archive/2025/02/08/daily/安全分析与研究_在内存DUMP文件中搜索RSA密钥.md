---
title: 在内存DUMP文件中搜索RSA密钥
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490362&idx=1&sn=3f5ff280ed1f3c01fb82db8b2b7f7817&chksm=902fb412a7583d04dffdf7991791a6944c485dd4db84402df46442c067a51b21a56773608f24&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-08
fetch_date: 2025-10-06T20:37:44.538987
---

# 在内存DUMP文件中搜索RSA密钥

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXSluHMOE3qL0LOeJGNsYT5DyEGQkQK8dEsWSxgfWrDgtqMHMYoSSVJIKL90ZfkZGouLUt26Koq4Q/0?wx_fmt=jpeg)

# 在内存DUMP文件中搜索RSA密钥

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

此前笔者分享过两篇勒索病毒解密的文章，解密工具都是通过在内存DUMP文件中搜索可能的解密的key，然后再进行暴力破解解密文件，这种方式可以适用于一部分勒索病毒解密方法，详细信息参考下面的两篇文章即可。

[《深度揭密LooCipher勒索病毒解密工具技术原理》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247484144&idx=1&sn=c7d7b0b2de0f6e864e38c52f25ba12eb&scene=21#wechat_redirect)

[《Avaddon勒索病毒解密工具及原理》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247486514&idx=1&sn=6464b9066980a6c045a33ef58dd5b6b0&scene=21#wechat_redirect)

今天给大家介绍一个开源的项目，在内存DUMP文件中搜索RSA密钥信息，项目地址：

https://github.com/congwang/rsakeyfind

源码分析

1.该工具可以通过两种方式来搜索内存DUMP中的RSA密钥信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXSluHMOE3qL0LOeJGNsYT5WBiafOJa0Cw04tp46HrL0XoV1KC8cuicJ1mr5q4fMc3BHc8PtXu7Mr5g/640?wx_fmt=png)

2.读取内存DUMP文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXSluHMOE3qL0LOeJGNsYT5ujVwZ9guJ93ISe5LvphwVSMNEYsWq5C2W5rRddA2n29KbFGEtTcribA/640?wx_fmt=png)

3.第一种方法，是已知公钥文件，读取已知的公钥文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXSluHMOE3qL0LOeJGNsYT5ic3GavCpNmEt00iaNNqEMZpibSeMuYWichgVWVNSLticKRIib239oVTyrLqw/640?wx_fmt=png)

4.然后搜索内存DUMP文件中BER编码的RSA公钥或私钥，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXSluHMOE3qL0LOeJGNsYT54Voryh7M7U5TQngJm1XHpaCJVcPbUaRaFka7GbLXWQGqEh50HTicfdA/640?wx_fmt=png)

5.另外一种方法，不用知道任何密钥信息，在内存DUMP文件中搜索BER编码的RSA版本信息，再尝试将周围的数据解析为BER编码，获取RSA密钥信息，RSA密钥BER编码之后的版本信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXSluHMOE3qL0LOeJGNsYT5ia5lRFkOmazKJmP7XPa2bTof1hgZHoPo9Hnw7KxHDdxrUpjQefWnnBw/640?wx_fmt=png)

还可以在内存DUMP文件中搜索AES密钥信息，有兴趣的可以自行参考开源项目

https://github.com/dbrant/keyfind\_aes\_rsa

总结结尾

如果对恶意软件分析感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXDIda3D6VvFWhqojST24E2rTRBJMYDfYowK8WcvBScfWlJiaYZ5elMdlrREG1LDVODxFQ0Eoy0YLQ/640?wx_fmt=jpeg)

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