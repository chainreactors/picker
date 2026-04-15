---
title: 迷雾中的航行：Fog 勒索软件关联攻击者工具链深度剖析
url: https://mp.weixin.qq.com/s/lblfGcqrSikqBwBxNxfz2Q
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:41:49.162731
---

# 迷雾中的航行：Fog 勒索软件关联攻击者工具链深度剖析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PO9bjOzlHYDCBeniaf1slB2jkAPMsq7FaicBl3sQTicCjravOXTugTicVQqRsa6CJB1jxXmUlahCQMdq0LicqQR19gHphWyzC5Zduz0y3nGvEP3k/0?wx_fmt=jpeg)

# 迷雾中的航行：Fog 勒索软件关联攻击者工具链深度剖析

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026-04-13 · 安全事件分析 · The DFIR Report

迷雾中的航行：Fog 勒索软件关联攻击者工具链深度剖析

2024年12月，DFIR Report 威胁情报团队发现了一个暴露的开放目录（194.48.154.79:80），该目录被判定为与 Fog 勒索软件组织有关联的勒索软件运营者所使用。对目录内容的分析揭示了一套完整的攻击工具链，覆盖侦察、漏洞利用、凭据窃取和命令控制等全部环节。

────────────────

核心发现

该攻击者使用的工具包括：

• **SonicWall Scanner** — 利用窃取的 VPN 凭据批量登录

• **DonPAPI** — 提取 Windows DPAPI 保护的凭据（浏览器密码、Cookie、Token）

• **Certipy** — 利用 Active Directory 证书服务（AD CS）漏洞提权

• **Zer0dump / Pachine / noPac** — 利用 Zerologon（CVE-2020-1472）和 PAC 漏洞攻陷域控

• **Sliver C2** — 命令控制框架，管理植入物

• **AnyDesk + PowerShell** — 自动化持久化驻留

• **Proxychains / Powercat** — 隐蔽横向移动和反向 Shell

受害者的内部域名 **fourlis.net** 出现在攻击者的 bash 历史记录中。希腊企业集团 Fourlis Holdings 在同一时期遭受了网络攻击，其在线商店运营瘫痪。

────────────────

开放目录全景

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYDd2P70MJPbsI7GMmtGhIApxVSHEwAiaibIfUJ4lfHicUyGeLHENGqjdgOyNiaWhbpb4QGqWTu5dwzS11SfMA3mLlCbhwfopXC6WtQ/640?wx_fmt=png)

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