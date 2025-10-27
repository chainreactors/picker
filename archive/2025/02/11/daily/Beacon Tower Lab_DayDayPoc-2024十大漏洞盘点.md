---
title: DayDayPoc-2024十大漏洞盘点
url: https://mp.weixin.qq.com/s?__biz=MzkyNzcxNTczNA==&mid=2247486987&idx=1&sn=4fb50aefa5785393e944f832b3694a9d&chksm=c22296f2f5551fe429bfefb377aaeb4ecf476ac444456e832bb870d275bbc4bae201bfd04f86&scene=58&subscene=0#rd
source: Beacon Tower Lab
date: 2025-02-11
fetch_date: 2025-10-06T20:47:24.462553
---

# DayDayPoc-2024十大漏洞盘点

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8E5sfrfkeAMM94AnYygpqABSAI7OFac8g7sLVkpSxD6WRA97Iv7eA0RpNju0S6Y8MoxvUrgVPjt4somGzfY1Tg/0?wx_fmt=jpeg)

# DayDayPoc-2024十大漏洞盘点

原创

烽火台实验室

Beacon Tower Lab

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAMM94AnYygpqABSAI7OFac8xsWWhibXnnhzN4UAHkMQEiciad9O7nia6PV3mQJhF20dibsdsWDCGCe2aOw/640?wx_fmt=png&from=appmsg)

**导语**

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAMM94AnYygpqABSAI7OFac8KtW7AibhPicDp070OEpuBHrAicCDYVZJVxQlqsUd2NC0FBX9OedyGiaM2w/640?wx_fmt=png&from=appmsg)

2024年转瞬即逝，DayDayPoc也已上线一年有余。这一年，DayDayPoc 平台注册人数已达1w+,已收录6000+个漏洞，作为交流与知识共享的重要阵地，我们始终坚持以漏洞研究为核心，以维护网络安全为使命。这一年，网络安全领域接连爆出了许多引人注目的漏洞。这些漏洞不仅在安全行业内引发了广泛关注，也对企业、组织和个人的信息安全带来了深远影响。现在我们来回顾一下2024年的十大热门漏洞，总结其中的技术特点、攻击手法和防御经验，以便从中吸取教训，更好地应对未来的安全挑战。

**1**

**Windows RDL存在远程代码执行漏洞（CVE-2024-38077）**

CVE编号：CVE-2024-38077

CVSS评分：9.8

影响产品：Windows Server 2000 到 Windows Server 2025 所有版本

漏洞回顾：被命名为狂躁许可的CVE-2024-38077因其高严重性、广泛的影响范围获得了安全行业的广泛关注。该漏洞存在于Windows远程桌面许可管理服务（RDL）中，攻击者无需任何权限即可实现远程代码执行，获取服务器最高权限。RDL 服务并非默认启用，但许多管理员会手动启用它来扩展功能，例如增加远程桌面会话的数量。由于在解码用户输入的许可密钥包时，未正确检验解码后数据长度与缓冲区大小之间的关系，导致缓冲区溢出。虽说在详细分析后因影响范围达不到传说中“核弹级”的，比肩“永恒之蓝”的效果，但对于漏洞本身而言确实是一个严重的漏洞。

**原理分析参考：**

```
https://mp.weixin.qq.com/s/2wBr8S96anwlMJ2Lp78J3w
```

**POC：**

```
https://www.ddpoc.com/DVB-2024-6401.html
```

**2**

**Fortinet FortiOS & FortiProxy越界写入漏洞(CVE-2024-21762)**

CVE编号：CVE-2024-21762

CVSS评分：9.8

影响产品：FortiOS & FortiProxy

漏洞回顾：Fortinet FortiOS是美国飞塔（Fortinet）公司的一套专用于FortiGate网络安全平台上的安全操作系统。该系统为用户提供防火墙、防病毒、IPSec/SSLVPN、Web内容过滤和反垃圾邮件等多种安全功能。在SSL VPN组件中存在越界写入漏洞，可能导致未经身份验证的远程威胁者通过特制HTTP请求执行任意命令或代码。越界写入的原理是因为解析 chunk 时，若长度字段解码后为 0，则触发读取 chunk trailer，在写入 chunk trailer 时，可根据长度字段向栈中写入 \r\n。因此，若长度字段为大量 0，将触发越界写入 \r\n 到返回地址附近。通过精心构造的 chunk 数据，可以覆盖栈中的返回地址，达到劫持程序控制流的目的。利用 ROP 技术，结合 FortiOS 的内存布局，实现远程代码执行。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAMM94AnYygpqABSAI7OFac8eKMuAczlLKdb90yAQibicwkVzzibRtE24Fic0mjPDLfhccKPQ1v1tv0Tzw/640?wx_fmt=png&from=appmsg)

**详情参考链接：**

```
https://mp.weixin.qq.com/s/4idvW838oZxY5bI8bDRQVA
```

**POC:**

```
https://www.ddpoc.com/DVB-2024-6401.html
```

**3**

**Ivanti Connect Secure 和Ivanti Policy Secure 远程命令执行漏洞（CVE-2024-21887）**

CVE编号：CVE-2024-21887

CVSS评分：9.1

影响产品：Ivanti Connect Secure VPN和Ivanti Policy Secure Version 9.x and 22.x

漏洞回顾：Ivanti Connect Secure 是一款基于 SSL VPN 的远程访问解决方案。它允许企业用户通过安全加密的方式远程访问企业内网资源。Ivanti Policy Secure 是一款网络访问控制（NAC）解决方案，用于确保企业网络资源只被经过授权的设备和用户访问。CVE-2024-21887是一个命令注入漏洞，允许具有管理员权限的认证用户发送特殊构造的请求并在设备上执行任意命令，结合CVE-2023-46805认证绕过漏洞，可达到未授权任意命令执行的效果。

**POC：**

```
https://ddpoc.com/DVB-2024-5999.html
```

**4**

**Palo Alto Networks PAN-OS 命令注入漏洞(CVE-2024-3400)**

CVE编号：CVE-2024-3400

CVSS评分：10

影响产品：启用了GlobalProtect gateway(Network > GlobalProtect > Gateways)和device telemetry(Device > Setup > Telemetry)的PAN-OS 10.2、PAN-OS 11.0和PAN-OS 11.1防火墙。

漏洞回顾：Palo Alto Networks的PAN-OS是一个运行在Palo Alto Networks防火墙和企业VPN设备上的操作系统。Palo Alto Networks PAN-OS软件的GlobalProtect功能存在命令注入漏洞，针对特定的PAN-OS版本和不同的功能配置，可能使未经身份验证的攻击者能够在防火墙上以root权限执行任意代码。2024年4 月10日，Volexity 发现其一名网络安全监控 (NSM) 客户对 Palo Alto Networks PAN-OS GlobalProtect 功能中发现的漏洞进行了零日利用，攻击者能够创建反向 shell、下载工具、窃取配置数据以及在网络内横向移动。Palo Alto Networks PSIRT 团队确认该漏洞为操作系统命令注入问题，并将其分配为 CVE-2024-3400。

**详情参考链接：**

```
https://mp.weixin.qq.com/s/bsDIByugTtNjR1WHsRPE9Q
```

**5**

**XAMPP在PHP-CGI模式下远程代码执行漏洞(CVE-2024-4577)**

CVE编号：CVE-2024-4577

CVSS评分：9.8

影响产品：8.1 < 8.1.29，PHP 8.2 < 8.2.20，PHP 8.3 < 8.3.8

漏洞回顾：PHP是一种被广泛应用的开放源代码的多用途脚本语言，PHP-CGI是PHP自带的FastCGI管理器。是一个实现了CGI协议的程序，用来解释PHP脚本的程序，2024年6 月7日，推特安全上orange公开了其漏洞细节，并且PHP官方已修复该漏洞。并确认该漏洞在为远程代码执行漏洞，并将其分配编号为 CVE-2024-4577。

XAMPP（Apache+MySQL+PHP+PERL）就是一个功能强大的建站集成软件包，该漏洞在XAMPP开启了PHP-CGI模式下运行时可造成远程代码执行，攻击者可通过该漏洞获取服务器权限。

该漏洞仅适用于php版本为8.1 < 8.1.29，PHP 8.2 < 8.2.20，PHP 8.3 < 8.3.8，同时在php-cgi模式下运行php，并且运行在windows平台，且使用语系为繁体中文950、日文932、简体中文936等。

**详情参考链接：**

```
https://mp.weixin.qq.com/s/H7B-9Azc9t_ob66PZERiVA
```

**POC:**

```
https://www.ddpoc.com/DVB-2024-7248.html
```

**6**

**XZ Utilѕ工具库恶意后门植入漏洞(CVE-2024-3094)**

CVE编号：CVE-2024-3094

CVSS评分：10

影响产品：XZ 5.6.0/5.6.1

漏洞回顾：XZ Utils 是一款用于压缩和解压缩 .xz 和 .lzma 文件的工具集。XZ Utils 由 Lasse Collin 开发，是一个开源项目，广泛应用于各种操作系统中，受影响开源操作系统可在https://repology.org/project/xz/versions中查询.xz 文件格式是一种基于 LZMA2 压缩算法的文件格式，它提供了比传统 gzip 更高的压缩比，同时保持了相对较高的解压缩速度。XZ Utils v5.6.0和v5.6.1中tar包的编译文件被植入恶意命令。在某些特定编译环境下，恶意命令执行后将替换正常编译过程中的中间文件为后门文件，最后和其他组件一起编译到XZ Utils的Liblzma库文件中。当后门代码被执行时，将挂钩（HOOK）SSHD进程中的SSH登录认证函数。当接收到指定的SSH数据包时，将未授权执行指定的系统命令。

**详情参考链接：**

```
https://mp.weixin.qq.com/s/7qIiFKw8OXrFcinIF4c7pQ
```

**7**

**GeoServer存在远程代码执行漏洞（CVE-2024-36401）**

CVE编号：CVE-2024-36401

CVSS评分：9.8

影响产品：8.1 < 8.1.29，PHP 8.2 < 8.2.20，PHP 8.3 < 8.3.8

漏洞回顾：GeoServer 是一个开源的服务器软件，使用 Java 编写，主要功能是允许用户共享和编辑地理空间数据。它在设计时就考虑到了互操作性，支持使用开放标准来发布多种主流格式的空间数据。由于该系统不安全地将属性名称解析为 XPath 表达式，未经身份认证的远程攻击者可以通过该漏洞在服务器上执行任意代码，从而获取服务器权限。

**详情参考链接：**

```
https://ddpoc.com/DVB-2024-7392.html
```

**8**

**PbootCMS前台SQL注入漏洞**

影响产品：PbootCMS

漏洞回顾：PbootCMS是全新内核且永久开源免费的PHP企业网站开发建设管理系统，是一套高效、简洁、 强悍的可免费商用的PHP CMS源码，能够满足各类企业网站开发建设的需要。系统采用简单到想哭的模板标签，只要懂HTML就可快速开发企业网站。官方提供了大量网站模板免费下载和使用，将致力于为广大开发者和企业提供最佳的网站开发建设解决方案。PbootCMS 存在前台未授权SQL注入漏洞，攻击者可以通过此漏洞读取系统数据库中的敏感信息，包括后台用户的用户名和密码。由于PbootCMS使用了模板的方法来组合产品页面内容，为了支持可扩展性，支持非常复杂的语法，构造sql语句的过程中可以通过该特性绕过WAF的阻拦，进而达到无限制注入的效果。

**详情参考链接：**

```
https://mp.weixin.qq.com/s/ZPYwrPyw_W_cEBVsm_McTw
```

**POC：**

```
https://ddpoc.com/DVB-2024-7996.html
```

**9**

**OpenSSH 远程代码执行漏洞(CVE-2024-6387)**

CVE编号：CVE-2024-6387

CVSS评分：8.1

影响产品：OpenSSH < 4.4p1 且未安装CVE-2006-5051/CVE-2008-4109补丁

8.5p1 <= OpenSSH < 9.8p1

漏洞回顾：OpenSSH是一个开源实现的SSH协议，用于加密网络通信。OpenSSH提供了一个安全的通道来访问远程计算机或服务器，并包含了一组客户端和服务器工具，以提供包括远程登录、远程执行命令、文件传输等功能。

CVE-2024-6387影响使用glibc的Linux系统，该漏洞被称为”RegreSSHion”。这个漏洞允许未经身份验证的用户在默认配置的情况下，通过LoginGraceTime参数进行远程代码执行，从而以root权限控制受影响的系统。

这个漏洞一旦被利用，可能会导致系统全面崩溃，攻击者可以使用最高权限执行任意代码，从而导致系统全面接管、安装恶意软件、篡改数据和创建后门进行持久访问。它可能会促进网络传播，使攻击者可以利用被入侵的系统作为立足点，穿越并利用组织内其他易受攻击的系统。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAMM94AnYygpqABSAI7OFac8nkLCCg8ftKDBsGxVbILoCTaALk9xR1nFA7ERwuQPyibt7iaKGQNndnJA/640?wx_fmt=png&from=appmsg)

**详情参考链接：**

```
https://mp.weixin.qq.com/s/sAOp-qn3-v5Lq-9P5sTDAw
```

**POC：**

```
https://ddpoc.com/DVB-2024-6034.html
```

**10**

**WPS Office从路径穿越到远程代码执行漏洞(CVE-2024-7262)**

CVE编号：CVE-2024-36401

CVSS评分：9.3

影响产品：WPS Office版本12.2.0.13110-12.2.0.16412

漏洞回顾：WPS Office程序promecefpluginhost.exe存在不当路径验证问题，允许攻击者在Windows上加载任意Windows库文件。该漏洞已被APT-C-60攻击者利用，当用户打开MHTML格式的文档时，只需单击一个恶意制作的超链接，即可执行攻击者指定的恶意库文件，实现远程代码执行。

**详情参考链接：**

```
https://mp.weixin.qq.com/s/QxiBbSRdfKvEwhKDeCx2LQ
```

**POC:**

```
https://www.ddpoc.com/DVB-2024-8279.html
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAPuXuLlzxV94SmGrdhm12Xoib8pv5tVryyDTMZPUwvOeXrHV2ygdoKrKJQ1u618rmXbhfhiaw8icr5Lw/0?wx_fmt=png)

Beacon Tower Lab

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAPuXuLlzxV94SmGrdhm12Xoib8pv5tVryyDTMZPUwvOeXrHV2ygdoKrKJQ1u618rmXbhfhiaw8icr5Lw/0?wx_fmt=png)

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