---
title: 恶意程序将家用路由器变成黑客组织的代理服务器
url: https://buaq.net/go-163824.html
source: unSafe.sh - 不安全
date: 2023-05-18
fetch_date: 2025-10-04T11:38:27.629141
---

# 恶意程序将家用路由器变成黑客组织的代理服务器

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

![]()

恶意程序将家用路由器变成黑客组织的代理服务器

安全公司 Check Point Research 报告了一种伪装成 TP-Link 路由器固件的恶意程序，包含了完整的后门功能，允许攻击者和被感染设备建立通信和文件传输，远程发送指令，上
*2023-5-17 23:46:50
Author: [www.solidot.org(查看原文)](/jump-163824.htm)
阅读量:28
收藏*

---

安全公司 Check Point Research 报告了一种伪装成 TP-Link 路由器固件的恶意程序，包含了完整的后门功能，允许攻击者和被感染设备建立通信和文件传输，远程发送指令，上传、下载和删除文件。恶意程序的主要目的被认为是充当代理掩盖通信来源。Check Point Research 发现其指令控制基础设施由 APT 组织 Mustang Panda 控制。Check Point 推荐路由器用户检查是否连接域名 m.cremessage[.com]，管理面板中是否有修改过的升级固件，是否存在 /vat/udhcp.cnf、/var/udhcp 和 .remote\_shell.log 等文件。如果存在那么路由器很可能被感染了。TP-Link 尚未对此报告发表评论。

https://research.checkpoint.com/2023/the-dragon-who-sold-his-camaro-analyzing-custom-router-implant/

文章来源: https://www.solidot.org/story?sid=74987
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)