---
title: 从 Bing 搜索到勒索软件：Bumblebee 投递 Akira 完整分析
url: https://mp.weixin.qq.com/s/a-8Vt0nSEdHEi6M7kZw37g
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:31:34.229013
---

# 从 Bing 搜索到勒索软件：Bumblebee 投递 Akira 完整分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PO9bjOzlHYDjibNlkwCKJknJQYUKcC6Ficlwibm7Qd8qMc5wscL4VIMB1xRtfy2Lx8mmkQEz8bibialNggJ3wEgE3okaRxTMfGwsWxVyfn3micnaw/0?wx_fmt=jpeg)

# 从 Bing 搜索到勒索软件：Bumblebee 投递 Akira 完整分析

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器中沉浸阅读

# 从 Bing 搜索到勒索软件：Bumblebee 与 AdaptixC2 如何投递 Akira 勒索软件

来源：The DFIR Report · 2025-11-04 · 案例编号 #TB36726

📌 核心要点

* Bumblebee 恶意软件自 2021 年底以来一直被用作初始访问工具，2023 年开始使用 **SEO 投毒**作为分发机制
* 用户在 Bing 搜索「ManageEngine OpManager」时被重定向到恶意网站 **opmanager[.]pro**，下载了木马化的 MSI 安装包
* 攻击者获取初始访问后横向移动到域控制器，转储凭据，安装 RustDesk 持久化，使用 SFTP 外泄数据
* 最终部署 **Akira 勒索软件**，两天后返回加密子域系统
* 从初始访问到首次勒索部署仅 **44 小时**，Swisscom 报告的 TTR 仅 **9 小时**

## 一、概述

Bumblebee 恶意软件自 2021 年底以来一直被威胁行为者用作初始访问工具。2023 年，该恶意软件首次被报告使用 **SEO 投毒**（搜索引擎优化投毒）作为分发机制。2025 年 5 月，Cyjax 报告了一场使用此方法的攻击活动，冒充各种 IT 工具。

2025 年 7 月，我们观察到威胁行为者通过此 SEO 投毒活动入侵了一个组织。用户搜索「ManageEngine OpManager」时被重定向到恶意网站，该网站提供了木马化的软件安装程序。此操作导致 Bumblebee 恶意软件的部署，为威胁行为者提供了环境的初始访问权限。

入侵迅速从单个受感染主机升级为**全面的网络攻陷**。初始访问后，威胁行为者横向移动到域控制器，转储凭据，安装持久化远程访问工具，并使用 SFTP 客户端外泄数据。入侵最终在根域部署了 Akira 勒索软件。威胁行为者两天后返回重复此过程，加密子域内的系统。

此攻击活动在 7 月影响了多个组织，包括 Swisscom B2B CSIRT 响应的一起类似入侵。

## 二、初始访问

此次入侵始于用户在 **Bing** 上搜索「ManageEngine OpManager」时被重定向到恶意网站 **opmanager[.]pro**。

![Bing 搜索结果中的恶意网站](https://mmbiz.qpic.cn/sz_mmbiz_png/PO9bjOzlHYAqPrkkVRM7jEnuRia6998atuk3INqGariaErGO9lfhHJ7gwRl9PKLBOetUeQXlLzAhxic7ZFpicZJJSaK2icIlbZPQ06eWIAtdPvz8/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

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