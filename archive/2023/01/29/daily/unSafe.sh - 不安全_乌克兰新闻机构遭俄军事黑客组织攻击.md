---
title: 乌克兰新闻机构遭俄军事黑客组织攻击
url: https://buaq.net/go-146913.html
source: unSafe.sh - 不安全
date: 2023-01-29
fetch_date: 2025-10-04T05:07:09.736807
---

# 乌克兰新闻机构遭俄军事黑客组织攻击

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

![](https://8aqnet.cdn.bcebos.com/58489bc90c4e5bff5ef6e4f8a8bafaae.jpg)

乌克兰新闻机构遭俄军事黑客组织攻击

主站 分类 漏洞 工具 极客
*2023-1-28 15:22:49
Author: [www.freebuf.com(查看原文)](/jump-146913.htm)
阅读量:29
收藏*

---

[![freeBuf](https://www.freebuf.com/images/logoMax.png)](https://www.freebuf.com/)

主站

分类

漏洞

工具

极客

Web安全

系统安全

网络安全

无线安全

设备/客户端安全

数据安全

安全管理

企业安全

工控安全

特色

头条

人物志

活动

视频

观点

招聘

报告

资讯

区块链安全

标准与合规

容器安全

公开课

官方公众号企业安全新浪微博

![](https://www.freebuf.com/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](https://www.freebuf.com/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

* [资讯](https://www.freebuf.com/news)

![](https://image.3001.net/images/20230128/1674888708_63d4c604b869c2c4a4bb6.png!small)

截至 2023 年 1 月 27 日，乌克兰计算机应急响应小组 (CERT-UA) 在该国国家新闻机构 (Ukrinform) 的网络上发现了五种不同的数据擦除恶意软件组合，其功能旨在破坏信息的完整性和可用性（写入零字节/任意数据的文件/磁盘及其随后的删除）。

在针对 Ukrinform 的攻击中部署的破坏性恶意软件列表包括 CaddyWiper (Windows)、ZeroWipe (Windows)、SDelete (Windows)、AwfulShred (Linux) 和 BidSwipe (FreeBSD)。

攻击者使用 Windows 组策略 (GPO) 启动了 CaddyWiper 恶意软件，由此可表明他们事先已经破坏了目标的网络。

正如 CERT-UA 在调查期间发现的那样，攻击者在 12 月 7 日左右获得了对 Ukrinform 网络的远程访问权限，并等待了一个多月才释放恶意软件。

然而，他们试图清除新闻机构系统中所有数据的尝试失败了。擦除器仅成功销毁了“几个数据存储系统”上的文件，这并未影响 Ukrinform 的运营。

CERT-UA 强调网络攻击只是部分成功，特别是在有限数量的数据存储系统方面。

## 与俄罗斯沙虫军事黑客有关的网络攻击

CERT-UA 上周将此次攻击与 Sandworm 威胁组织联系起来，该组织是俄罗斯主要情报局 (GRU) 74455 军事部队的黑客组织，Sandworm 曾在4 月份针对一家大型乌克兰能源供应商的另一次失败攻击中使用了 CaddyWiper 数据擦除器。

在那次攻击中，俄罗斯黑客使用了类似的策略，部署 CaddyWiper 来清除 Industroyer ICS 恶意软件留下的痕迹，以及其他三个为 Linux 和 Solaris 系统设计的擦除器，并被跟踪为 Orcshred、Soloshred 和 Awfulshred。

自 2022 年 2 月俄乌战争以来，除了 CaddyWiper 之外，乌克兰目标网络上还部署了多种数据擦除恶意软件，包括DoubleZero、HermeticWiper、IsaacWiper、WhisperKill、WhisperGate和AcidRain 等。

此外，微软和斯洛伐克软件公司 ESET 也表示最近针对乌克兰的勒索软件攻击与 Sandworm 黑客组织有关。

> 参考链接：https://www.bleepingcomputer.com/news/security/ukraine-sandworm-hackers-hit-news-agency-with-5-data-wipers/

文章来源: https://www.freebuf.com/news/355841.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)