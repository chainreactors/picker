---
title: NIST抗量子密码算法被爆安全漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247558351&idx=1&sn=b2a5aecc9be4547715a3749684d149ab&chksm=e91434f5de63bde3c8755e9c86f3af692182c5fecf7082f7822e3cab3b5b76e9e194e59d8a86&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-03-08
fetch_date: 2025-10-04T08:56:21.694624
---

# NIST抗量子密码算法被爆安全漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEnvaaJgP4fLR6WSG3rtkm0IVDttV5m5HCSw2dkM7DiadWkOKSc4Soc3Q/0?wx_fmt=jpeg)

# NIST抗量子密码算法被爆安全漏洞

ang010ela

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

研究人员发现在NIST选定的抗量子密码算法中发现安全漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEkr4XhLkpGuib9ibXWviat7Y9cnml9GDvbFaIicl3LYLicyuRia6zianZJ88Aw/640?wx_fmt=png)

2022年7月，美国国家标准和技术研究所（NIST）宣布选定的4个抗量子加密算法，其中CRYSTALS-Kyber用于通用加密，CRYSTALS-Dilithium、FALCON和SPHINCS+用于数字签名。CRYSTALS-Kyber被加入到美国国家安全局推荐的应用于国家安全系统的加密算法套件中。

2022年12月，瑞典皇家理工学院研究人员发文称在CRYSTALS-Kyber特定实现中发现一个安全漏洞，攻击者利用该漏洞可以发现侧信道攻击。侧信道攻击是通过物理参数的评测和分析来从加密系统中窃取秘密信息。侧信道攻击常用的参数包括电源电流、执行时间、电磁辐射等。攻击原理是加密算法实现结果会引入一些物理上的反映，可以用来解码和推理机密信息，比如密文和加密密钥。而针对侧信道攻击的主要防护方法是屏蔽（masking），屏蔽方法的基本原理是使用秘密分享技术将加密算法的敏感中间变量拆分为多个秘密份额，然后在这些不同的秘密份额上执行计算。

该漏洞是在CRYSTALS-Kyber 算法的ARM Cortex-M4 CPU实现中发现的。研究人员设计了一种基于神经网络（递归学习）的攻击方法，可以以更高概率恢复出消息位。基于神经学习的侧信道攻击方法可以对抗传统信道攻击的防护方法，比如屏蔽、随机延迟插入、随机时钟等方法。研究人员提出一种名为循环移位（cyclic rotation）的消息恢复方法，可以通过操作密文来增加消息位的泄露，因此增加消息恢复的成功率。

NIST称该方法并非破解了CRYSTALS-Kyber算法，也不影响CRYSTALS-Kyber的抗量子标准化过程。

关于CRYSTALS-Kyber安全漏洞的研究成果参见：https://eprint.iacr.org/2022/1713.pdf

参考及来源：https://thehackernews.com/2023/03/experts-discover-flaw-in-us-govts.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEfvRaJb4yiagRd5ybB6rtsALsiakfvdrsC2nb0vrSicSBdWjGKibtFibQvJg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ickFyVbJg4sroA6D2OFWmHEgMvb6MpialET0YfZSsZoicC530tmZvqvyKXgQICIvXAqwiaOXhv9BMnaQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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