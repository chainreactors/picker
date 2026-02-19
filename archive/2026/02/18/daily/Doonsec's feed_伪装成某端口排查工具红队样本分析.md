---
title: 伪装成某端口排查工具红队样本分析
url: https://mp.weixin.qq.com/s/D5FnjZccHTzIJEAPSg9U6Q
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:13:37.167391
---

# 伪装成某端口排查工具红队样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWQov8VsFVj3jpjVMlFkBHClZhxvIWQC6mWWzNxYAib1CUYtKHL58quvia4eWfLr5pOGonEMTIib1Z1w/0?wx_fmt=jpeg)

# 伪装成某端口排查工具红队样本分析

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

笔者从事恶意软件研究十几年了，从上大学开始对计算机的病毒研究感兴趣，到后面一直从事与恶意软件相关的工作，涉及到多个不同的平台，分析研究过的恶意软件家族笔者自己都数不清了，这么多年在笔者的电脑硬盘里面全是这十几年来研究和收集的各种恶意软件家族样本、分析技术与技巧笔记、以及与恶意软件相关的各种技术资料等。

以前笔者常戏称自己的电脑是“养马场”，因为里面全是各种病毒木马样本，包含了各种各样的恶意软件家族，这些恶意软件家族样本包含Windows、Linux(Android)、Mac(iOS)等平台。

安全行业发展了几十年了，不同的时期总是会出现各种新概念、新名词、新平台、新产品，让人眼花缭乱，然而不管哪个时期，恶意软件攻击活动却从来没有停止过，现在的恶意软件已经无处不在，防不甚防，涉及到各种不同的平台，不同的攻击手法，不同的攻击目标。

全球每天都会有各种新的攻击样本出现，这些攻击样本被运用到各种不同的攻击活动当中，包含各种黑灰产攻击、勒索攻击、APT攻击等，不管安全行业如何发展，不管出现多少新的概念，新名词，新产品，新平台，最基础最核心的安全问题，永远会一直存在，不同的时期它会有不同的表现形式，不同的攻击方法，同时会有不同的攻击样本，只要有黑客的存在，有利益的地方，就会有各种不同类型的恶意软件出现。

近日笔者在威胁情报平台上捕获到一例红队攻击样本，该攻击样本母体伪装成某安全公司端口排查工具，使用Rust语言编写，笔者针对该攻击样本进行了详细分析，文未提供该样本完整威胁情报。

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