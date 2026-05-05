---
title: cPanel关键漏洞已被用于攻击政府和MSP网络
url: https://mp.weixin.qq.com/s/cTEC6xbOSexUld25Qo7zTw
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:57:31.942371
---

# cPanel关键漏洞已被用于攻击政府和MSP网络

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OLh41BuK8LBqjiaStibwQDJl7aaOj3jjz4acwAkliaWp1n7J2JlEJNCS5qLK1P6FRiclFdrw7icvxg1iaKHTicAeQcPjRUSzTGgjQ7V0/0?wx_fmt=jpeg)

# cPanel关键漏洞已被用于攻击政府和MSP网络

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

此前未知的威胁行为者被发现利用 cPanel 中最近披露的漏洞，以东南亚的政府和军事实体为目标，同时还攻击菲律宾、老挝、加拿大、南非和美国的一小部分托管服务提供商 (MSP) 和主机提供商。

Ctrl-Alt-Intel 于 2026 年 5 月 2 日检测到的活动涉及滥用CVE-2026-41940，这是 cPanel 和 WebHost Manager (WHM) 中的一个严重漏洞，可能导致身份验证绕过，并允许远程攻击者获得控制面板的更高控制权。

攻击行动源自 IP 地址“95.111.250[.]175”，主要针对与菲律宾（\*.mil.ph 和 \*.ph）和老挝（\*.gov.la）相关的政府和军事域名，以及 MSP 和托管服务提供商，并使用公开可用的 概念验证(PoC)。

此外，Ctrl-Alt-Intel 还披露，攻击者在发起 cPanel 攻击之前，曾针对印尼国防部门的一个培训门户网站使用过一套独立的定制攻击链，该攻击链结合了经过身份验证的 SQL 注入和远程代码执行技术。据悉，攻击者当时已经掌握了该门户网站的有效登录凭证。

Ctrl-Alt-Intel 表示：“该脚本使用硬编码凭据，通过从服务器颁发的会话 cookie 中读取预期的 CAPTCHA 值来绕过门户网站的 CAPTCHA，而不是正常解决挑战。”

“攻击者一旦通过身份验证和验证码验证，就会进入文档管理功能。易受攻击的参数是用于保存文档名称的字段，脚本会在向文档保存端点发送 POST 请求时，将 SQL 代码注入到该字段中。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NJfFCBaGmAZsp0bzUA6dlXA7UE2MHPgjpRXJVTWHKwgOtnw0ia6DEBRgct5hLQ919rOqTGvewl6tukUMo8e6TaAY6ZnaHAlEn8/640?wx_fmt=jpeg)

进一步分析表明，攻击者利用AdaptixC2命令与控制 (C2) 框架远程控制受感染的终端。此外，攻击者还使用了 OpenVPN 和 Ligolo 等工具，以实现对受害者内部网络的持续访问。

Ctrl-Alt-Intel补充道：“该攻击者利用OpenVPN、Ligolo和systemd持久性构建了一个持久的访问层，然后利用该访问层进入内部网络，窃取了大量中国铁路部门的文件。”

目前尚不清楚是谁在幕后操纵，但与此同时，Censys 表示，他们发现了证据，表明 cPanel 漏洞在公开披露后的 24 小时内就被多个第三方利用，包括部署 Mirai 僵尸网络变种和名为 Sorry 的勒索软件。

根据 Shadowserver 基金会的数据，至少有 44,000 个 IP 地址可能因 CVE-2026-41940 漏洞而遭到入侵，并于 2026 年 4 月 30 日对其蜜罐进行了扫描和暴力破解攻击。截至 5 月 3 日，这一数字已降至3,540。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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