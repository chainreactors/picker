---
title: Ghost(Cring)勒索病毒样本分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490635&idx=1&sn=a8453bc0dab8c6813cf41100839f78b9&chksm=902fb363a7583a75c497cdcec549d3efbdd6f0fb1bfaaa73619f426f47d22909fa83d711e3e5&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-23
fetch_date: 2025-10-06T20:36:59.927573
---

# Ghost(Cring)勒索病毒样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVlUuLrJsKuPEBwkPM7dXkEBZSxDg9MNiaUiaugzX2FMUItM8OiaQ3kccF3ZStFBRLaB57P9ERRFSXZA/0?wx_fmt=jpeg)

# Ghost(Cring)勒索病毒样本分析

原创

pandazhengzheng

安全分析与研究

前言

针对Ghost勒索病毒样本进行逆向分析

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

最近几年勒索病毒已经席卷全球，全球范围内越来越多的政府、企业，组织机构等受到勒索病毒黑客组织的攻击，几乎每天都有企业被勒索病毒攻击的新闻被曝光，可能还有更多的企业被勒索病毒攻击之后，选择默默交纳赎金，由于勒索病毒太过于暴利，从而导致越来越多的黑客组织开始使用勒索病毒攻击。

Ghost勒索病毒黑客组织己经攻击了全球70多个国家及地区的基础设施，受影响的其他行业包括医疗保健、政府、教育、技术、制造业以及众多中小型企业。

Ghost勒索病毒黑客组织首次于2021年被曝光，攻击者首先通过投放定制的Mimikatz样本，然后安装CobaltStrike后门，并使用合法的Windows  CertUtil证书管理器部署勒索软件负载以绕过安全软件。

Ghost勒索病毒黑客组织曾使用的漏洞包含：

CVE-2018-13379、CVE-2010-2861、CVE-2009-3960、CVE-2021-34473、CVE-2021-34523、CVE-2021-31207。

参考链接：

https://www.bleepingcomputer.com/news/security/cisa-and-fbi-ghost-ransomware-breached-orgs-in-70-countries/

笔者从微步威胁情报平台下载到Ghost(Cring)勒索病毒样本，并对样本进行了相关分析。

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