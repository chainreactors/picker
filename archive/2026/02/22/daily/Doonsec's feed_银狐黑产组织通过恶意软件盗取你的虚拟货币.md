---
title: 银狐黑产组织通过恶意软件盗取你的虚拟货币
url: https://mp.weixin.qq.com/s/vNH3GL2PuLihLpQi1XmzOg
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:16:11.743561
---

# 银狐黑产组织通过恶意软件盗取你的虚拟货币

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXPhMtKY7jTJNtKIjneseiaibuOxdYFWu7ITCXo9cKx7dBaXIJiallsAJF7rqVorrMMfpAcHE0v3gAZQ/0?wx_fmt=jpeg)

# 银狐黑产组织通过恶意软件盗取你的虚拟货币

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

最近几年该组织针对金融行业和数据货币相关的企业与公司攻击活动非常频繁，主要目标就是为了盗取受害者虚拟数据货币，主要的攻击手法就是通过钓鱼攻击，将各种恶意软件打包成各种各样本钓鱼信息，欺骗虚拟货币从业人员以及企业人员安装远控木马，从而远控监控盗取虚拟货币从业人员及企业的重要信息，包含各种各样的虚拟货币钱包数据等，然后再进行下一步的诈骗攻击活动，这些木马不仅仅攻击Windows平台，同时因为大量的虚拟货币从业人员喜欢使用Mac电脑办公和操盘，国庆期间有不少虚拟货币从业人员被钓鱼攻击，导致自己的虚拟货币被盗，笔者此前写过多篇相关的分析文章，如下所示：

[《伪装成ToDesk安装程序加载后门盗取数字货币》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489656&idx=1&sn=b2693f2eecfd194407c52a70a20646ab&scene=21#wechat_redirect)

[《银狐黑产组织针对OKX数字货币交流群钓鱼攻击样本分析》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489223&idx=1&sn=7b85d2226f0f06a2075cd8cc9389cbf2&scene=21#wechat_redirect)

[《小心你的加密货币，针对加密货币的窃密样本详细分析》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489082&idx=1&sn=75b72879dc3e57459d2e585d868e4b94&scene=21#wechat_redirect)

[《针对虚拟货币从业人员银狐钓鱼样本分析》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247491213&idx=1&sn=4acbe9812ff92ccafb06d0992f065637&scene=21#wechat_redirect)

笔者曾参与取证溯源分析过多例针对虚拟货币公司的应急响应安全事件，近日在某论坛看到又一起银狐相关的攻击案例，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXPhMtKY7jTJNtKIjneseiaibh4XfoApNlNZR3mmpWaMtR8ZYbj9K3RT4qJG8wsCFdoW6gpxiaa9ejJg/640?wx_fmt=png)

银狐黑产组织通过到外发布各种钓鱼恶意软件确实搞到不少钱，从微步威胁情报网站下载到相关的攻击样本，对该攻击样本进行了详细分析，该攻击样本非常复杂，里面使用了多种不同的攻击手法和攻击技术，包含多种安全对抗技术BYOVD、Bypass UAC、加密压缩、多种加壳混淆，可见该黑客组织技术非常成熟，文未分享该攻击样本完整威胁情报。

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