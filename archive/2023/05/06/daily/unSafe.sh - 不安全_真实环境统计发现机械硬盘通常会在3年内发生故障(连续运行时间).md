---
title: 真实环境统计发现机械硬盘通常会在3年内发生故障(连续运行时间)
url: https://buaq.net/go-161901.html
source: unSafe.sh - 不安全
date: 2023-05-06
fetch_date: 2025-10-04T11:38:28.269452
---

# 真实环境统计发现机械硬盘通常会在3年内发生故障(连续运行时间)

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/073ef7976fd37bf9bebda6bb0332531f.jpg)

真实环境统计发现机械硬盘通常会在3年内发生故障(连续运行时间)

数据存储提供商 Backblaze 会定期发布硬盘故障率的数据，Backblaze 主要提供数据存储服务，因此不仅需要部署大量硬盘，同时也要对各种故障硬盘进行替换，所以有真实环境的运行
*2023-5-5 23:21:24
Author: [www.landiannews.com(查看原文)](/jump-161901.htm)
阅读量:18
收藏*

---

数据存储提供商 Backblaze 会定期发布硬盘故障率的数据，Backblaze 主要提供数据存储服务，因此不仅需要部署大量硬盘，同时也要对各种故障硬盘进行替换，所以有真实环境的运行数据可以统计硬盘的故障率。

需要强调的是 Backblaze 的硬盘使用环境是数据中心，因此硬盘都是长期运行的，所以如果只看标题你会发现机械硬盘 3 年就会挂掉？为什么我的机械硬盘使用六七年还是好好的，因为这里的时间是按照实际运行小时数计算年限的，家用 PC 安装的硬盘不太可能 7x24 小时长期开机，当然 NAS 除外。

**结论：**

Backblaze 通过硬盘自身的 S.M.A.R.T. 数据进行统计，记录的数据包括故障日期、型号、序列号、容量、故障和 S.M.A.R.T. 原始值。**Backblaze 的统计结论是机械硬盘的平均故障时间是在 22360 小时后，即 932 天或 2 年 6 个月；容量更大的硬盘故障率似乎还会更高一些(这里有陷阱，下文说详细说)。**

**以下是一些有趣的统计数据：**

最初关注存储行业的技术网站 Block & Files 发布了一篇文章介绍机械硬盘故障率的统计，该网站的数据是在 2007 块故障机械硬盘中，平均故障年龄是 1051 天，约 2 年 10 个月。

Backblaze 看到后觉得这数字太低了，也就是机械盘寿命这么短吗？于是自己也找出了一堆替换下来的故障机械盘进行统计，结果统计的时间比上面的还要短。

结果表明 1~4TB 的机械盘比 12TB + 的机械盘寿命更长，不过这里有个陷阱，那就是 Backblaze 的小容量机械盘的使用率降低，大容量机械盘使用率更高，所以这个数据不应该作为直接结论，**即不能直接判断大容量机械盘就一定比小容量机械盘更容易挂掉****。**

[![真实环境统计发现机械硬盘通常会在3年内发生故障(连续运行时间)](https://img.lancdn.com/landian/2023/05/98591-1.png)](https://img.lancdn.com/landian/2023/05/98591-1.png)

**生命周期年化平均故障率：**

统计显示 Backblaze 使用的所有硬盘年化平均故障率为 1.4%，其中西部数据的表现好些，平均故障率为 0.31%；东芝排名第二，平均故障率为 0.93%；HGST 排名第三，平均故障率为 1.11%；希捷表现最差，平均故障率为 2.28%。

[![真实环境统计发现机械硬盘通常会在3年内发生故障(连续运行时间)](https://img.lancdn.com/landian/2023/05/98591-2.png)](https://img.lancdn.com/landian/2023/05/98591-2.png)

Backblaze 也知道希捷硬盘的故障率更高但还是采用了大量希捷硬盘，无他，就是因为希捷硬盘价格相对便宜些，综合成本可以低一些。

全文报告：<https://www.backblaze.com/blog/backblaze-drive-stats-for-q1-2023/>

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/98591.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/98591.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)