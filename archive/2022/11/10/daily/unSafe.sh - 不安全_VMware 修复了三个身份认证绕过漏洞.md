---
title: VMware 修复了三个身份认证绕过漏洞
url: https://buaq.net/go-134982.html
source: unSafe.sh - 不安全
date: 2022-11-10
fetch_date: 2025-10-03T22:12:54.190826
---

# VMware 修复了三个身份认证绕过漏洞

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

VMware 修复了三个身份认证绕过漏洞

主站 分类 漏洞 工具 极客
*2022-11-9 19:17:27
Author: [www.freebuf.com(查看原文)](/jump-134982.htm)
阅读量:22
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

Bleeping Computer  网站披露，VMware 近期发布了安全更新，以解决 Workspace ONE Assist 解决方案中的三个严重漏洞，分别追踪为 CVE-2022-31685（认证绕过）、CVE-2022-31686 （认证方法失败）和 CVE-2022-31687 （认证控制失败）。据悉，这些漏洞允许远程攻击者绕过身份验证并提升管理员权限。![1667992735_636b8c9f1b4b13affe56f.jpg!small?1667992735334](https://image.3001.net/images/20221109/1667992735_636b8c9f1b4b13affe56f.jpg!small?1667992735334)

Workspace ONE Assist  可以提供远程控制、屏幕共享、文件系统管理和远程命令执行，以帮助服务后台和 IT 人员从 Workspace ONE 控制台实时远程访问设备并排除故障。

未经身份认证的威胁攻击者可以在不需要用户交互进行权限升级的低复杂度攻击中利用这些漏洞。从 VMware 发布的声明来看，一旦具有 Workspace ONE Assist 网络访问权限的恶意攻击者成功利用这些漏洞，无需对应用程序进行身份验证就可以获得管理访问权限。

## ****漏洞现已********修复****

目前，VMware为Windows 已经为客户发布了 Workspace ONE Assist 22.10（89993），对这些漏洞进行了修补。

此外，VMware 还修补了一个反射式跨站脚本（XSS）漏洞（CVE-2022-31688）以及一个会话固定漏洞（CVE-2022-31689），前者允许攻击者在目标用户的窗口中注入 javascript 代码，，后者允许攻击者获得有效会话令牌后进行身份验证。

![](https://image.3001.net/images/20221109/1667992787_636b8cd3d11ebe9789f23.png!small)值得一提的是，Workspace ONE Assist 22.10 版本修补的所有漏洞都是由 REQON IT-Security的Jasper Westerman、Jan van der Put、Yanick de Pater 和 Harm Blankers 发现并报告给 VMware 的。

## VMware 修复了多个安全漏洞

今年 8 月，VMware 警告管理员要修补 VMware Workspace ONE Access、Identity Manager 和 vRealize Automation 中另外一个关键身份认证绕过安全漏洞，该漏洞允许未经认证的攻击者获得管理权限。

同年 5 月，Mware 修补了一个几乎相同的关键漏洞，该漏洞是 Innotec Security的Bruno López 在 Workspace ONE Access、VMware Identity Manager（vIDM）和vRealize Automation 中发现的另一个身份验证绕过漏洞（CVE-222-22972）。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/vmware-fixes-three-critical-auth-bypass-bugs-in-remote-access-tool/

文章来源: https://www.freebuf.com/articles/349339.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)