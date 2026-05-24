---
title: 我扒了马维斯实测：1000万Token白送，最大坑是权限
url: https://mp.weixin.qq.com/s/u8K6PEh7A9xOuZ3Ph_uNfg
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T06:00:25.339142
---

# 我扒了马维斯实测：1000万Token白送，最大坑是权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x5l8unjI0UrdWMoXa1gtQutG77ibicsk6n4t62ECNWlicR6Tia4S77YVhmwdE8tfLicD9TibnuuwicW9mqknKRQicZFQFc8ekjIDcBgeTGmJzWrdwog/0?wx_fmt=jpeg)

# 我扒了马维斯实测：1000万Token白送，最大坑是权限

原创

AI观察
AI观察

AI员工上线

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

我电脑C盘常年爆红，文件乱到我自己都找不到，所以Marvis这个"能帮你找文件"的卖点，我第一眼就心动了。

5月20号腾讯突然上线了这个操作系统层级AI助手。不是聊天机器人，是直接扎根你电脑里那种——帮你找文件、调系统、清垃圾，甚至用手机远程操控电脑。官方说每人每天送1000万免费Token，听着挺大方对吧？

等等，我扒完第一波用户的实测反馈后，发现事情没这么简单。

## 一、安装门槛：8核+16G内存，老电脑直接劝退

说实话，我本来想当晚就下载试试，结果一看配置要求，心凉了一半。

Windows版最低要求6核CPU、16GB内存、SSD，macOS要M1芯片以上。有用户反馈说8GB内存"能打开网页AI工具，但Marvis这种操作系统层级助手，涉及本地文件理解、系统信息读取、端侧模型和任务执行，16GB内存更稳"。另一位更直白："Windows端最低门槛是8核CPU、16G内存加SSD。"

说到这我突然想到，这跟买车似的——车是免费的，但停车位你得自己解决。

![马维斯界面概念图](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UrhgT4ajxmJrxPRCKDp5qWpibDWiajOddfhzGVk8f22cyXCuOl9dfZcyHtyMINVWZcxot6ibN2tvFCKMOMPWkpiajpIl0RGQFVBytQ/640?wx_fmt=png "马维斯界面概念图")

## 二、文件搜索：确实能找到两个月前的截图

这个功能挺惊艳。有用户专门测了：两个月前从群里下载的一张截图，只记得内容是《黑神话：悟空》，文件名完全忘了。Marvis先按关键词和时间范围筛出1000张照片，然后用Python快速筛选，最终找到8张候选图，第一张正是要找的。

确实比Windows搜索强出一截。但代价也很明显：首次扫描整个硬盘建立索引，耗时约15分钟，期间电脑明显卡顿。而且很多人根本不知道可以设定扫描范围，默认全盘扫描隐私风险其实不小。

![跨设备协同概念图](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqibfxfw2X0ZW2icIqPUsm2XSJWTLdsE0leAIFAgiakvmVhyEOSAficGBVXmeR6JjpAn2XgiaX3zVke5hKvYQkbRwPhOqKJFia3Ng6xo/640?wx_fmt=png "跨设备协同概念图")

## 三、最大的坑不是收费，是权限

Marvis需要文件读写、系统设置、应用操控、屏幕录制四个核心权限。CSDN上教程讲安全："权限不是越多越好，但该给的权限不给，很多功能就跑不起来。"有用户原话更直接："把所有权限一次性全开是新手最容易踩的坑。"

这才是最大的坑——它越能干，你给的权限越多，潜在风险越大。删除文件、调整系统核心配置等敏感操作会先给出执行计划并请求确认，但很多人根本不会仔细看那个弹窗。说到这我突然意识到，这跟之前那波"Vibe Coding安全隐患"其实是一回事。

我算了下，1000万Token按混元计价大概等于每天白送你3块钱。听着大方，但代价是你得把电脑的部分控制权交出去。

## 总结

Marvis代表了AI助手的新方向：从聊天框走向操作系统，从回答问题走向执行任务。但第一波用户反馈也说明，它还没到"接管你人生"的程度。

适合的人：文件多且乱的本地重度用户；重视数据隔离的财务/法务从业者；电脑配置达标的效率玩家。

不适合的人：8GB内存老电脑用户；希望一键搞定一切的手残党；对隐私权限极度敏感的人。

如果你电脑够新、文件够乱、耐心够足，可以下载试试。但记住：先小任务测试，再复杂任务交付。别第一天就让它接管你的人生——也别把权限一次性全给它。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqrm4gHILLG2gYhHuico1NLxVJaiajoaia7s7y1Iy8wsNOwzmGGFowHyeszUtzrCXpnmKH5C2dwn6wqIByFI4iaxqKBYzqUdd6uL6M/0?wx_fmt=png)

AI员工上线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqrm4gHILLG2gYhHuico1NLxVJaiajoaia7s7y1Iy8wsNOwzmGGFowHyeszUtzrCXpnmKH5C2dwn6wqIByFI4iaxqKBYzqUdd6uL6M/0?wx_fmt=png)

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