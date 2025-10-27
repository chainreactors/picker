---
title: 3CX供应链攻击技术之微软数字签名被滥用技术分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490083&idx=1&sn=ae29cfade8f5828fec4fb779fe5e3c96&chksm=902fb50ba7583c1d446ad0cd9ea3a31505e76942c0c9287c7c7c3d7e34d0a798bdd099c074b4&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-01-22
fetch_date: 2025-10-06T20:10:13.036851
---

# 3CX供应链攻击技术之微软数字签名被滥用技术分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWfJUSHMlOhMTZic3DniaKoeHpu40xuMT2y8LMpibtVBjn2NPJuXenib0kNSEbIDiaePRrJYKiakOfrHFUw/0?wx_fmt=jpeg)

# 3CX供应链攻击技术之微软数字签名被滥用技术分析

原创

pandazhengzheng

安全分析与研究

前言

使用数字签名对恶意软件进行签名等处理方式，是APT攻击组织常用技巧之一，本篇分析此前3CX双供应链攻击事件中，滥用微软数字签名的技术，同时介绍了其他滥用数字签名的技术

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

此前3CX企业级电话管理系统供应商遭遇供应链攻击,在详细分析时候，可以发现被ffmpeg.dll模块加载的另一个d3dcompiler\_47.dll模块包含微软的正常数字签名的，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWfJUSHMlOhMTZic3DniaKoeHITWCt1I46WgLD7Q8mqNqiabCsY6oIYQuqj08WksMSuZwvic2OuibnTU5A/640?wx_fmt=png)

利用微软的签名工具检测该文件的数字签名信息，如下所示：

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