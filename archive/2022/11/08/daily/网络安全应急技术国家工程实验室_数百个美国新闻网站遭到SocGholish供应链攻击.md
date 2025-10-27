---
title: 数百个美国新闻网站遭到SocGholish供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247532563&idx=3&sn=e0ace0d8f4aa2e2aaf0d6ded6e9a4e47&chksm=fa93f6d2cde47fc46468ca592c9fab571564f7e413566504d7039287332876d4f4c6fc22b936&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-11-08
fetch_date: 2025-10-03T21:56:58.091535
---

# 数百个美国新闻网站遭到SocGholish供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lfc7fejqQKCnwg9WIGIBsfS7aIcw9yWQmuKNibCv0qnfXJF2Cibq8oXS0qEsmtoxyPLpsyCUIlwwFA/0?wx_fmt=jpeg)

# 数百个美国新闻网站遭到SocGholish供应链攻击

网络安全应急技术国家工程中心

一伙威胁分子正在利用一家未披露身份的媒体公司受攻击的基础设施，在全美数百家报纸的网站上部署SocGholish JavaScript恶意软件框架，又叫FakeUpdates（虚假更新）。

这起供应链攻击背后的威胁分子（被Proofpoint编号为TA569）将恶意代码注入到一个无害的JavaScript文件中，而该文件被众多新闻媒体的网站加载。

这个恶意的JavaScript文件用于安装SocGholish，这种恶意软件框架可以使用恶意软件载荷感染访问受攻击网站的那些用户，这些恶意软件载荷伪装成虚假的浏览器更新，而这些更新通过虚假的更新提醒以ZIP压缩包的方式来分发，比如Chrome.Uрdatе.zip、Chrome.Updater.zip、Firefoх.Uрdatе.zip、Opera.Update.zip和 Oper.Updte.zip。

Proofpoint的威胁洞察团队今天在Twitter上透露：“Proofpoint威胁研究团队观察到，一家为许多主要新闻机构提供服务的媒体公司受到了间歇性注入。这家媒体公司通过JavaScript向合作伙伴提供内容。”

“通过修改这个原本无害的JavaScript的代码库，它现在被用于部署SocGholish。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vc7lqGvgDbHCvIBt7XkeMIog2hgB502mDs20g249BdOY8gnhHxiaggUJicWUxicazx92sefJjSx0YA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图1. 恶意JavaScript文件对内容做了混淆处理（来源：BleepingComputer）

据企业安全公司Proofpoint的安全研究人员声称，这个恶意软件安装在了总共250多家美国新闻机构的网站上，其中一些还是大型新闻机构。

虽然目前共有多少家新闻机构影响尚不清楚，但Proofpoint表示，它获悉来自纽约、波士顿、芝加哥、迈阿密、华盛顿特区等地区的媒体机构（包括国家性新闻机构）已受到了影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vc7lqGvgDbHCvIBt7XkeMdrjP33K9fjkgsTOmXUneHcVQxayr7qPMkPBjvuHo79b577Pliad4brQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图2.与勒索软件攻击有关联

Proofpoint此前观察到SocGholish活动使用虚假的更新和网站重定向来感染用户，在一些情况下还添加勒索软件载荷。

Evil Corp网络犯罪团伙在一次非常相似的活动中也使用了SocGholish，通过由数十个受攻击的美国报纸网站分发虚假的软件更新提醒，感染了30多家美国大型私营企业的员工。

受感染的计算机随后被用作借机闯入雇主企业网络的跳板，企图部署该团伙的WastedLocker勒索软件。

幸运的是，赛门铁克在一份报告中透露，它阻止了Evil Corp企图加密受攻击网络的活动，这起攻击针对多家私营公司，包括30家美国公司，其中8家还是《财富》500强公司。

SocGholish最近还被用于在感染上了Raspberry Robin恶意软件的网络中植入后门，微软称之为Evil Corp前勒索软件（pre-ransomware）行为。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/hundreds-of-us-news-sites-hit-in-socgholish-supply-chain-attack/

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176njVOPvfib4X3jQ6GIHLtX8SSDvbpmcpr4uu3X7ELG7PDjdaLVeq4Er02ZoicTPvxrC6KCVH3bssUVw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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