---
title: 「推安早报」0726 |  Selenium Grid Rce、红队新技术、spring Skipper组件rce
url: https://mp.weixin.qq.com/s?__biz=MzU0MDcyMTMxOQ==&mid=2247487685&idx=1&sn=7eb34d26696d991deb33192ae556c622&chksm=fb35b90dcc42301be0287b6f42989e0e3b8aeb7c996006163f088deb8f511e421a729f7d2afd&scene=58&subscene=0#rd
source: 甲方安全建设
date: 2024-07-27
fetch_date: 2025-10-06T17:43:34.892429
---

# 「推安早报」0726 |  Selenium Grid Rce、红队新技术、spring Skipper组件rce

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZmUzTB0pLOicuUMdxfdo1ZNFYK1WPOgQqxP9bfoq8LmEolOxRlXQdlbVB7tZCzibia8q3IT6295vKNmA/0?wx_fmt=jpeg)

# 「推安早报」0726 | Selenium Grid Rce、红队新技术、spring Skipper组件rce

bggsec

甲方安全建设

# 2024-07-26 「红蓝热点」每天快人一步

> 1. 推送`「新、热、赞」`，帮部分人`阅读提效`
> 2. 学有`精读浅读深读`，艺有`会熟精绝化`，觉知此事`重躬行`。推送只在`浅读预览`
> 3. 机读为主，人工辅助，每日数万网站，10w推特速读
> 4. 推送可能`大众或小众`，不代表本人偏好或认可
> 5. 因渲染和外链原因，公众号`甲方安全建设`发送`日报`或日期,如`20240726`获取`图文评论版pdf`

### 目录

> 0x01 【2024-0726】利用PDF文件注入恶意代码攻击技术
> 0x02 【2024-0726】利用线程名称进行攻击的新技术
> 0x03 【2024-0726】Spring Cloud Data Flow 远程代码执行漏洞（CVE-2024-37084）
> 0x04 【2024-0726】人脸识别的不同面貌：操作与攻击
> 0x05 【2024-0726】揭秘AWS会话令牌的内部结构
> 0x06 【2024-0726】SeleniumGreed：利用暴露的Selenium Grid服务进行加密货币挖矿

### 0x01 利用PDF文件注入恶意代码攻击技术

> 本网页介绍了如何利用PDF文件中的JavaScript执行能力，将恶意代码注入PDF文件，从而实现从特定URL自动下载文件的攻击技术，即PDF Dropper攻击，并通过Cobalt Strike等工具建立Command and Control（C2）连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmUzTB0pLOicuUMdxfdo1ZNFAGs6Ef6Dkmg1SOTRvZcDh8BoqBsc85Jib8RuB4vb4FrDK1e4Q2I5v9g/640?from=appmsg)

### 热评

* Cobalt Strike 攻击：利用恶意 JavaScript 注入 PDF 文件创建 PDF Dropper

### 关键信息点

* PDF文件可以执行JavaScript代码，这使得它们成为了潜在的攻击载体。
* 通过在PDF文件中嵌入恶意JavaScript代码，可以实现自动下载和执行远程文件的攻击，这种技术被称为PDF Dropper。
* 攻击者可以利用这种方法来建立与受害者系统的C2连接，从而实现对系统的控制。
* 尽管浏览器和PDF阅读器对PDF中的JavaScript执行有限制，但仍有可能绕过这些限制执行特定操作。

🏷️: PDF攻击, 恶意代码注入, JavaScript, 网络安全

### 0x02 利用线程名称进行攻击的新技术

> Check Point Research 发现了一种新的进程注入技术，名为 Thread Name-Calling，它利用 Windows 的线程描述 API 来绕过终端保护产品，实现恶意代码的注入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmUzTB0pLOicuUMdxfdo1ZNF7BhJxZBic9Fn435k9OicWPju81DqKic7vDOHKKLoFOpc8oahSafWcHUkQ/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/icqm3vRUymZmUzTB0pLOicuUMdxfdo1ZNFgxMK9SQ4TkdPKUnvia9HKIYKv0N3GwwLN0MicJFrJxExHbCvvtQkgNuA/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmUzTB0pLOicuUMdxfdo1ZNFdPxmWKUQv4icibD9sdR6X8f9t73ibfVMSurYJZDbhhAvXqkufl2WY2L0w/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* 利用线程名称实现进程注入的新技术
* 线程名称调用：一种利用线程名称的进程注入技术

### 关键信息点

* 进程注入是攻击者工具包中的重要技术，用于防御逃避、进程干预和权限提升。
* 传统的注入方法容易被 AV 和 EDR 产品检测，因此攻击者和红队成员不断寻找新的 API 来实现注入，以逃避检测。
* Thread Name-Calling 技术利用了相对较新的 API，这些 API 没有被常规的监控工具所关注，从而能够绕过现有的保护措施。
* 该技术不需要对目标进程拥有写入权限，仅需最小的访问权限，这减少了被检测的可能性。

🏷️: Process Injection, Thread Name-Calling, API Abuse, Endpoint Protection

### 0x03 Spring Cloud Data Flow 远程代码执行漏洞（CVE-2024-37084）

> Spring Cloud Data Flow 中的 Skipper 组件存在一个关键的远程代码执行漏洞（CVE-2024-37084），该漏洞被评定为 CVSS 9.8 分，表明其严重性。

### 热评

* Spring Cloud Data Flow 远程代码执行漏洞 CVE-2024-37084
* Spring Cloud Data Flow 发现高危漏洞CVE-2024-37084

### 关键信息点

* 严重性：CVE-2024-37084 漏洞的严重性非常高，CVSS 分数为 9.8。
* 影响范围：受影响的是 Spring Cloud Data Flow 的 Skipper 服务器组件，可能导致服务器完全妥协。
* 默认安全性：Skipper 服务器 API 默认不对外部用户开放，但内部用户仍然面临风险。
* 影响版本：受影响的版本为 Spring Cloud Data Flow 2.11.4 之前的版本。

🏷️: Spring Cloud Data Flow, 远程代码执行, 漏洞, 微服务, 数据处理平台

### 0x04 人脸识别的不同面貌：操作与攻击

> 网页主要探讨了数据科学应用程序在信息系统中的安全风险，包括远程代码执行、内网横向移动、恶意软件传播、持久性访问以及数据湖挖掘等方面的攻击手段和策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZmUzTB0pLOicuUMdxfdo1ZNFiaDaN82rkpNsIOB1RYPnNIC5yn6cxxkVzZnDKO0gSwOYZlNTnQ4qqNQ/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZmUzTB0pLOicuUMdxfdo1ZNFLdHnLHWhWb3bs2Diagh1Zrvka095P5acgOOice7iaw5ibylpoJsmsibibiclQ/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZmUzTB0pLOicuUMdxfdo1ZNFfpl7u62CGP052d1e3I163119KeNZ996ZCh2LBfjbOvQ0qNrI66Vv6w/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

* 利用数据科学技术进行攻击的红队实战

### 关键信息点

* 数据科学应用程序成为新的高价值目标：随着传统应用程序变得更加安全，攻击者转向数据科学应用程序作为新的入侵点。
* 远程代码执行的可能性：通过Spotfire和Dataiku等应用程序，攻击者可以实现远程代码执行，进而控制服务器和内部网络。
* 内网横向移动与恶意软件传播：利用数据科学应用程序的特性，攻击者可以在内部网络中横向移动，并传播恶意软件。
* 持久性访问的实现：攻击者可以通过各种方法，如C2基础设施、DLL劫持和透明化命令执行，确保对系统的长期访问。

🏷️: 人脸识别, 攻击, 信息系统, 网络安全

### 0x05 揭秘AWS会话令牌的内部结构

> 本文揭示了AWS会话令牌的内部结构，通过逆向工程分析，提供了代码和工具来解析和修改AWS会话令牌，并对其加密和认证协议进行了测试。

### 热评

* AWS 会话令牌逆向工程分析：首次公开代码和工具
* 揭秘 AWS 会话令牌内部结构

### 关键信息点

* AWS会话令牌的内部结构和认证协议之前是一个黑箱，但现在通过逆向工程分析，这些信息变得更加透明。
* AWS会话令牌的安全性得到了验证，其加密和签名密钥每小时更新一次，这限制了攻击者即使窃取了密钥也只能在有限的时间内使用。
* AWS的认证系统对金色票据攻击具有相对较高的抵抗力，这表明AWS在设计其认证协议时考虑了安全性。
* 研究人员提供的开源工具可以帮助用户和研究人员更好地理解和分析AWS会话令牌，同时也有助于保护和审计AWS环境的安全性。

🏷️: AWS, 会话令牌, 逆向工程, 加密, 认证协议

### 0x06 SeleniumGreed：利用暴露的Selenium Grid服务进行加密货币挖矿

> Wiz Research 发现了一项名为“SeleniumGreed”的恶意活动，该活动利用暴露的 Selenium Grid 服务进行加密货币挖矿。

### 热评

* 「编者注」:这玩意还有些类似的，以前好像叫 seleniumHQ 吧，确实攻击面可能从2016左右就开始了，以前测评过一波，黑灰amazon刷dan当时很多用这个的.
* 新型挖矿攻击利用Selenium Grid漏洞，攻击者使用新技术

### 关键信息点

* Selenium Grid 服务的默认配置不包含认证机制，这使得许多实例容易被恶意利用。
* 威胁行为者通过 Selenium WebDriver API 的特性，实现了在受害服务器上运行 Python 脚本，进而部署挖矿软件。
* 该恶意活动采用了多种 防御演asion技术，如使用自定义 UPX 头部打包矿工，以及避免硬编码矿池代理 IP 地址。
* 尽管 Selenium Grid 的官方文档警告 不要将服务暴露在互联网上，但许多用户仍然忽略了这一点。

🏷️: Selenium, 加密货币挖矿, 网络安全, 威胁攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46vfEibIH57REKzBPUKgDubRickg6g44OtmibSJ6Gaibr8icCItHpX9WyoJJw/640?wx_fmt=jpeg)

快来和老司机们一起学习吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

甲方安全建设

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

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