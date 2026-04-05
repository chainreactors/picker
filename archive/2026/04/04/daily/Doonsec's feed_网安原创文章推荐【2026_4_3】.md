---
title: 网安原创文章推荐【2026/4/3】
url: https://mp.weixin.qq.com/s/D99P9rCJpfk2h6pL1JaPNA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:29.434731
---

# 网安原创文章推荐【2026/4/3】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CZMNsicRfJACOJMZ8LG58cmb0vB9A7JsApFL4ZwYWAx1yXdOJtYgWIibezAibwmoEMs7uyzEyiasQfIia5BbEiaicTpnDye3FosianG6h8v7Q5ZORDU/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/4/3】

AJay13
AJay13

洞见网安

![]()

在小说阅读器中沉浸阅读

# 2026-04-03 微信公众号精选安全技术文章总览

> 洞见网安 2026-04-03

---

### 0x1 [PHPJM混淆解解析与还原](https://mp.weixin.qq.com/s?__biz=MzE5ODU0ODczOA==&mid=2247483796&idx=1&sn=3a6534034a5426edf0d0e1fbc6a7d1e7&scene=21#wechat_redirect "PHPJM混淆解解析与还原")

> UNSAFE-TEAM 2026-04-03 21:10:41

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sibpvO9ayaSziclUk6FoNxlNFhZTGSfibpV6G52ibYB72Gs4rRSxib0lGlccuQyGiakeG7AUiaZt1eVH8Wg9WpZBNKK863rG5bmfY7gmBZ16U7sIGs/640?wx_fmt=jpeg)

本文主要分析了 phpjm.net 平台对 PHP 文件的加密机制，并提供了相应的解密还原方法。文章首先介绍了一段示例 PHP 代码在经过 phpjm.net 加密后的变化，包括变量名和函数名的混淆。接着，文章详细分析了加密后的代码结构，将其分为三个部分：函数定义、赋值和处理方法。通过对加密代码的逐步解析，文章揭示了加密算法的核心逻辑，并提供了相应的解密脚本代码。最后，文章总结了 phpjm.net 加密机制的特点，指出其本质上是在执行流程上附加了一层解包逻辑，而非真正的加密。文章还简要提及了 phpjiami.com 平台的加密处理方法。

PHP 加密解密

恶意软件分析

加密算法分析

解密工具开发

网络安全学习

---

### 0x2 [ubuntu勒索病毒应急 - vulntarget-n](https://mp.weixin.qq.com/s?__biz=MzIzNTE0Mzc0OA==&mid=2247486801&idx=1&sn=bcb632586e70e89760e1d1eaa6169abd&scene=21#wechat_redirect "ubuntu勒索病毒应急 - vulntarget-n")

> GSDK安全团队 2026-04-03 20:30:23

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Wq4VJsQicA18V3ZMPUMOMicVXwibWmmKeeDc7l2HXaIFR5WU3paibbcmERdNfkNd1Qqb6iaze3WrP7Qxm3BWNUIepW4wG30cuqfYRmZPtDwJhKCs/640?wx_fmt=jpeg)

本文描述了一个模拟全球化勒索病毒高发环境下的应急响应和取证分析案例。案例中，客户在阿里云部署的业务环境遭遇勒索病毒攻击，网站首页被篡改，要求支付赎金，部分重要文件被加密为.vulntarget格式。应急响应步骤包括分析攻击事件原理，恢复被篡改的index.jsp页面和正常的web服务，以及找到隐藏在系统中的三个flag。通过分析网站日志，发现大量异常访问记录和扫描行为，确定攻击者利用CVE-2017-12615漏洞上传恶意文件vulntarget.jsp进行攻击。在系统中找到并分析了加密脚本和密钥，通过解密脚本恢复了被加密的index.jsp页面。最后，重新上传了被篡改的404.jsp.vulntarget文件，成功恢复了原来的页面，完成了应急响应和取证分析任务。

勒索病毒

应急响应

取证分析

网络安全

Web安全

日志分析

数据恢复

虚拟机

命令执行

定时任务

---

### 0x3 [TP-Link 多个漏洞使攻击者能够触发拒绝服务攻击并导致路由器崩溃](https://mp.weixin.qq.com/s?__biz=Mzg4ODI5MzAzMw==&mid=2247485962&idx=1&sn=f3219f4f6282f2a0a7d5ac8639910e41&scene=21#wechat_redirect "TP-Link 多个漏洞使攻击者能够触发拒绝服务攻击并导致路由器崩溃")

> 安全圈的那点事儿 2026-04-03 19:09:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OjmTohK58LU4aArzoiaENAHNicjeTJPllpeUf1tHaZLSbWDZ5pToOfWC4jfjZUiaH3LMyqUFUxYb54bJSR0nq0aDuNWmpBhRQ4wY/640?wx_fmt=jpeg)

TP-Link Tapo C520WS 智能安防摄像头被发现存在多个高危漏洞，包括身份验证绕过、缓冲区溢出等，可能导致拒绝服务攻击、设备崩溃或被未经授权的攻击者绕过身份验证。这些漏洞中，CVE-2026-34121的CVSS评分最高，为8.7。TP-Link已发布紧急固件更新来修复这些漏洞，但未打补丁的设备仍面临安全风险。建议用户立即更新固件以保护设备安全，未更新的设备可能导致未经授权的配置更改和持续崩溃。

设备漏洞

拒绝服务攻击

身份验证绕过

缓冲区溢出

固件更新

网络安全事件

智能家居安全

---

### 0x4 [2026-3月Solar应急响应公益月赛排名及官方题解](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247509603&idx=1&sn=2d7c8820695ee846a63496f406d85651&scene=21#wechat_redirect "2026-3月Solar应急响应公益月赛排名及官方题解")

> solar应急响应团队 2026-04-03 16:07:43

![](https://mmbiz.qpic.cn/mmbiz_jpg/887OLfia3YQaDQkADg1IEMpPRy6TgBardf5G5IOIYiaP9rTGhw3D8yYf3NjBskPhAiaiaic8obTSn7qc7W1rGLNTM7iaj1bnFQGdhgOhtWyvBUpVI/640?wx_fmt=jpeg)

本文详细分析了一场名为Solar应急响应公益月赛的网络安全竞赛，该竞赛围绕溯源分析、流量分析和逆向工程三个方向展开。文章首先介绍了比赛平台的功能和赛事回顾，指出本次比赛重点考察选手的实际取证能力和逻辑推理水平。接着，文章深入剖析了比赛中的一道难题，该题目涉及浏览器扩展程序劫持攻击，要求选手从网络层异常发现到最终提取远控木马的完整过程进行取证。文章详细解释了如何通过分析进程关联、浏览器取证、静态代码审计和动态行为监控等技术手段来解题。此外，文章还介绍了如何使用LiME工具解析内存转储文件，以及如何从内存中提取WireGuard的密钥和流量进行解密。最后，文章总结了比赛的排名情况和参赛选手的提交情况。

应急响应

CTF

逆向工程

网络流量分析

Linux安全

浏览器安全

加密解密

恶意软件分析

取证

---

### 0x5 [常规测绘都扫不到的“孤岛资产”怎么找？安全运营进阶实战手册](https://mp.weixin.qq.com/s?__biz=Mzg2NjUzNzg4Ng==&mid=2247484743&idx=1&sn=5b047b1dc0c5706bf5ec680ec8e59148&scene=21#wechat_redirect "常规测绘都扫不到的“孤岛资产”怎么找？安全运营进阶实战手册")

> 网安前线 2026-04-03 14:16:47

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3voTJqpicKFPia3fdEXjptNDa7xGJaUeNoiaLWwEgwLNv7LMQl1D071VGYf9GP9iblhCVI0BaLdlc0ZghibichV3nUJeg1H4o7WR3TLx9Atgu9cJs/640?wx_fmt=jpeg)

本文探讨了网络安全运营中常见的“孤岛资产”问题，这类资产由于脱离统一管控，往往难以被发现，成为安全漏洞的潜在来源。文章首先分析了常规梳理的盲区，指出孤岛资产由于管理盲区特征而难以被发现。接着，文章介绍了6种实战化空间测绘关联语法，包括组织架构的层级化延伸、供应链与开发商特征关联、测试接口遗留与未授权API、内部命名规范与拼音缩写、SSL证书信息的深度提取和隐藏特征的指纹匹配。此外，文章还提出了拓宽边界的方法，如移动端应用的API溯源、代码托管平台的敏感信息泄露、历史解析记录排查废弃资产以及已知前端JS文件的外联接口分析。最后，文章强调了应对海量数据的自动化资产挖掘工作流的重要性，并提出了建立常态化发现与闭环机制的必要性，以确保网络安全防护的长期有效性。

网络安全运营

孤岛资产

安全策略

攻击面分析

空间测绘

自动化工具

安全闭环

---

### 0x6 [资产测绘在漏洞挖掘中的应用](https://mp.weixin.qq.com/s?__biz=MzI4MjI2NDI1Ng==&mid=2247487056&idx=1&sn=53763749bbfd58fef8b2ee7d0b8705d1&scene=21#wechat_redirect "资产测绘在漏洞挖掘中的应用")

> 安全艺术 2026-04-03 13:43:34

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mEJuibtxKvNdjHRj7MOkBPPJeh6s6g5YI2DFI8MHrWcAiaqnXrfnedDDYrW8q1eN9xJWlycFibytPBkGefoDm85lTT6Lgndkf3vEoP8VbQicQw/640?wx_fmt=jpeg)

本文探讨了资产测绘在漏洞挖掘中的应用，以存储桶遍历漏洞为例，说明了如何利用官方网站和工具如Quake进行资产收集和漏洞挖掘。文章指出，尽管直接使用命令行或图形化工具进行资产收集是一种常见做法，但通过官方平台同样可以轻松发现漏洞。以Quake为例，作者展示了如何通过官方截图中的Name信息发现可利用的目录，并利用dddd工具进行漏洞测试。文章还提到了如何使用dddd工具结合Burp Suite进行漏洞验证，以及如何利用dddd内置的POC进行任意文件上传和删除的攻击。最后，文章鼓励读者加入作者的圈子以获取更多挖洞技巧。

漏洞挖掘

资产测绘

网络安全工具

安全漏洞

漏洞利用

S3 存储桶安全

CNVD

报告撰写

---

### 0x7 [使用burpsuite插件如何无脑挖的第一个公益漏洞（小白挖洞）](https://mp.weixin.qq.com/s?__biz=MzYzMjY5MDM3OA==&mid=2247483938&idx=1&sn=0d84ab9701665f815affa0c0fa76de62&scene=21#wechat_redirect "使用burpsuite插件如何无脑挖的第一个公益漏洞（小白挖洞）")

> three安全之路 2026-04-03 11:19:15

![](https://mmbiz.qpic.cn/mmbiz_jpg/op0UsH3vuJ047W56EnvdK51Rofmiaicm3OREG9C06wrf0TX4XDdNZgM4WPj4uDQ2SmmzqpGIANsPKj2wZppfClmiaC8wUALaO12nWtOUmBpZ94/640?wx_fmt=jpeg)

本文主要介绍了网络安全学习者在进行漏洞挖掘时的一些方法和工具。文章首先提到漏洞挖掘的主要产出平台包括edu漏洞提交平台、补天和漏洞盒子，并指出资产通常是指特定的学校或平台上的公益公司。对于初学者，文章建议从弱口令、网络日历、验证码轰炸或swagger-ui未授权等方式入手挖掘漏洞，但需要注意平台可能会忽略重复提交的报告。在挖掘公益漏洞时，文章推荐使用Burp Suite的xia\_sql插件进行SQL注入探测，并解释了如何通过对比返回包长度来判断是否存在注入点。此外，文章还介绍了使用微信搜索目标、设置全局代理和Burp Suite抓包等技巧，以及使用knife插件过滤无关数据包的方法。最后，文章推荐了FindSomething和VueCrack两个接口插件，用于分析JavaScript路径和敏感信息，以及使用HAE插件提取暴露的key、身份证信息和电话号码等敏感信息。这些方法和工具对于网络安全学习者来说具有一定的参考价值。

---

### 0x8 [记一次某实训系统域控攻击过程wp](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247485422&idx=1&sn=8365315cad7dce6e2818d9136923c44e&scene=21#wechat_redirect "记一次某实训系统域控攻击过程wp")

> 梦醒安全 2026-04-03 10:11:51

![](https://mmbiz.qpic.cn/mmbiz_jpg/f0zVXnDXPGNfTK2tZic2V3oDa9DxEXJo9AcfnkGm4JFjgzBpucAibIiaB1Q0AqpRy9qempMtjLXDfORBPuBiaO9Xq9OqiagwBjRvibOKljkZhbvz0/640?wx_fmt=jpeg)

本文详细介绍了在域环境中进行攻击的两种主要方法和多种具体技术。首先，文章概述了域内攻击的两种类型：利用常规漏洞（如Web服务、服务器系统漏洞）和针对域控制器（DC）的漏洞（如MS14-068）。文章强调了避免防火墙和流量检测设备拦截的重要性。接着，文章深入讲解了MS14-068漏洞的原理、利用前提和复现过程，包括获取SID、生成伪造票据、删除缓存票据和导入票据获取域控权限等步骤。此外，文章还介绍了MS14-025漏洞，即组策略首选项（GPP）密码硬编码漏洞，攻击者可通过解密SYSVOL共享文件夹中的加密密码文件来获取本地管理员密码。文章还详细描述了Pass the Hash（PtH）攻击的概念、原理和利用条件，并提供了复现过程，包括获取NTLM Hash和进行Hash传递。最后，文章提到了黄金票据攻击的相关知识，并指出了MS14-025和MS14-068漏洞与黄金票据攻击的联系。整个文章旨在帮助读者理解和掌握域内攻击的多种技术和方法。

域渗透

Kerberos攻击

组策略攻击

Pass the Hash

黄金票据

提权

内网安全

票据攻击

哈希攻击

安全漏洞

---

### 0x9 [LLMNR / NBT-NS 与 SMB 中继攻击](https://mp.weixin.qq.com/s?__biz=Mzk2NDI2OTM0OA==&mid=2247484304&idx=1&sn=36860420de13aceacaa70d63d2038dca&scene=21#wechat_redirect "LLMNR / NBT-NS 与 SMB 中继攻击")

> 寰宇密阁 2026-04-03 10:00:28

![](https://mmbiz.qpic.cn/mmbiz_jpg/pcNneYiaOMFFEGibQkr0oTuia9bExVNO5xEx8eANllLibUe46KebVq9EPCJdsBsJTvCh6PV2w0Vb6vFiaw5xgyIOzaQ/640?wx_fmt=jpeg)

本文详细介绍了LLMNR / NBT-NS与SMB中继攻击的原理和实施方法。文章首先概述了Windows名称解析机制，解释了LLMNR和NBT-NS的工作原理及其安全风险。随后，文章深入分析了攻击的核心思路，包括监听网络请求、冒充服务器名称、接受客户端连接并记录或转发认证信息。文章还介绍了自动化攻击工具Responder的使用方法，并通过实验复现了攻击过程。此外，文章探讨了SMB中继攻击的原理，以及如何使用Impacket进行SMB中继攻击。最后，文章提出了防御这些攻击的关键措施，强调了禁用LLMNR/NBT-NS、强制SMB签名、最小权限原则和减少NTLM依赖的重要性。

中间人攻击

凭证窃取

Windows安全

网络协议安全

内网安全

安全工具

横向移动

权限提升

防御策略

---

### 0xa [2026 内网渗透隧道技术全解：从 Chisel 到 ICMP，一篇吃透](https://mp.weixin.qq.com/s?__biz=MzIzOTUwMjI5MA==&mid=2247485782&idx=1&sn=a2a28b1dd0b7781a1cfbefda0897e7ca&scene=21#wechat_redirect "2026 内网渗透隧道技术全解：从 Chisel 到 ICMP，一篇吃透")

> 异空间安全 2026-04-03 09:44:40

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BV6cRFk2iaVtKfDDEiba2PbsmPmibkm6GO9mJbUpVibTpR4pLywsfgeW4F7TfDiboXiamspzunNHhLAK55zy8RZGl0TMLOjhIPL1o1uZiblI4ribqaE/640?wx_fmt=jpeg)

本文详细介绍了内网渗透隧道技术，涵盖了隧道技术的核心概念、分类、优势以及适用场景。文章重点讲解了多种隧道技术，包括加密TCP隧道（如Chisel、SSF）、系统原生SSH隧道、HTTP/Web隧道、DNS隧道、ICMP隧道以及专用隧道（如EW、RDP、Venom）。此外，还讨论了系统原生端口转发（如Windows的netsh和Linux的socat/iptables）以及2026年的最新趋势和前沿技术，如协议深度伪装、无入口穿透、幽灵路由等。文章还提供了一些实战案例和速查表，帮助读者更好地理解和应用这些隧道技术。最后，强调了隧道技术的最高境界是无文件、无进程、无流量特征、无网络痕迹、无人可察，并提醒读者遵守相关法律法规。

---

### 0xb [web选手入门pwn(34)——bllhl\_book](https://mp.weixin.qq.com/s?__biz=MzUzN...