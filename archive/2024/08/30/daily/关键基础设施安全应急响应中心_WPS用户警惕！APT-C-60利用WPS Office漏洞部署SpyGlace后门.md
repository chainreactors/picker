---
title: WPS用户警惕！APT-C-60利用WPS Office漏洞部署SpyGlace后门
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545541&idx=1&sn=3e287b0b3ad08f9b440684d7eb685583&chksm=c1e9be94f69e3782e116f581ad8837de986e0279a7964044235a913869e44d37588b5109b895&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-08-30
fetch_date: 2025-10-06T18:05:18.499101
---

# WPS用户警惕！APT-C-60利用WPS Office漏洞部署SpyGlace后门

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs6TibDytX0iaBjw9aSGGiaPiasdVVia0pEZhWTdUhAkMPHWibHvBKYyaDG2N3oYtp3t5eYkibFNXZOblrBw/0?wx_fmt=jpeg)

# WPS用户警惕！APT-C-60利用WPS Office漏洞部署SpyGlace后门

关键基础设施安全应急响应中心

与韩国有关的网络间谍组织APT-C-60利用金山WPS Office软件中的一个关键远程代码执行漏洞（CVE-2024-7262），CVSS评分为9.3，部署了名为SpyGlace的独特后门。该漏洞由于对用户提供的文件路径验证不足，允许攻击者上传任意Windows库并执行远程代码。APT-C-60通过一个操纵的电子表格文档作为攻击载体，该文档含有恶意链接，点击后触发多阶段感染序列，传播SpyGlace木马。SpyGlace是一个DLL文件，具备文件窃取、插件加载和命令执行功能。安全研究员Romain Dumont指出，APT-C-60对应用程序的内部进行了广泛研究，了解Windows加载过程的行为。此外，ESET报告称，Pidgin消息应用程序的恶意第三方插件ScreenShareOTR被发现包含下载DarkGate恶意软件的代码，该插件还具备键盘记录器和屏幕截图功能，已从第三方插件列表中删除，建议用户立即删除。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icXsnxgeQgibbg3B2OyDvgllH3GTFJLVp9gllBtJPbyttGrbQOl5SxWcVmiaK3p1BfdMKcdV6XODA7Mw/640?wx_fmt=jpeg&from=appmsg&wxfrom=13&tp=wxpic)

漏洞概述

No.1 CVE-2024-7262

影响版本: Windows版WPS Office 2023年8月发布的12.2.0.13110版本到2024年3月发布的补丁版本12.1.0.16412。

根本原因: WPS Office的ksoqing自定义协议处理程序注册存在漏洞。该协议通过特定格式的URL执行任意代码，利用promecefpluginhost.exe组件的控制流。恶意链接通过WPS电子表格中的自定义协议启动该组件，导致攻击者指定的DLL被加载并执行。

漏洞利用方式: 攻击者利用MHTML格式嵌入恶意库，并通过img标签下载远程文件。通过设置特定的超链接，点击链接时将加载攻击者控制的DLL，从而实现代码执行。受影响的WPS Office版本在打开含有恶意超链接的电子表格时，触发该漏洞。

No.2 CVE-2024-7263

影响版本: Windows版WPS Office 2023年8月发布的12.2.0.13110版本到2024年5月末发布的12.2.0.17119版本。

根本原因: 在修补CVE-2024-7262后，WPS Office引入的新补丁没有完全解决问题。补丁增加了对JSCefServicePath变量的检查，但未对CefPluginPathU8变量进行类似检查。这导致攻击者可以通过修改CefPluginPathU8变量，实现加载未经验证的DLL。

漏洞利用方式: 攻击者可以通过网络路径注入恶意DLL，并利用未检查的CefPluginPathU8变量控制promecefpluginhost.exe进程。这使得攻击者能够加载并执行任意DLL文件，从而绕过补丁的防护措施。

APT-C-60利用漏洞的过程

APT-C-60组织利用漏洞进行攻击的主要过程如下：

1. 寻找漏洞：APT-C-60识别并利用了金山WPS Office软件中的一个关键远程代码执行漏洞（CVE-2024-7262），该漏洞允许攻击者上传并执行任意Windows库。
2. 制作诱饵文档：攻击者制作了一个带有陷阱的电子表格文档，该文档嵌入了恶意链接，并在2024年2月上传至VirusTotal。
3. 诱导点击：该电子表格文档通过图像欺骗用户，使其看起来像是普通的电子表格。文档中的恶意超链接连接到图像，诱导用户点击。
4. 触发漏洞利用：用户点击图像中的单元格后，触发漏洞利用，开始多阶段感染序列，目的是传播SpyGlace木马。
5. 部署SpyGlace后门：SpyGlace木马以TaskControler.dll的形式存在，具备文件窃取、插件加载和命令执行功能。
6. 持续活动：APT-C-60自2021年以来一直活跃，而SpyGlace后门早在2022年6月就已经在野外被发现。
7. 利用其他漏洞：APT-C-60还利用了Pidgin消息应用程序的第三方插件ScreenShareOTR（或ss-otr）中的漏洞，该插件包含从C&C服务器下载下一阶段二进制文件的代码，导致DarkGate恶意软件的部署。
8. 利用Cradle应用：ESET发现Cradle应用程序中存在与ScreenShareOTR相同的恶意后门代码，该应用程序声称是Signal的开源分支，恶意代码通过运行PowerShell脚本下载并执行。
9. 使用数字证书：插件安装程序和Cradle应用程序使用由波兰公司“INTERREX - SP. Z OO”颁发的有效数字证书进行签名，表明攻击者使用不同的方法来传播恶意软件。

   APT-C-60的攻击活动展示了其在漏洞开发、社会工程和恶意软件部署方面的复杂性和隐蔽性。

漏洞披露时间线

2024-02-29：CVE-2024-7262的漏洞利用文档已上传至VirusTotal。

2024-03-??：金山发布了一个更新，悄悄修补了CVE-2024-7672漏洞，因此2024-02-29漏洞不再有效。这是通过分析2024-03至 2024-04 之间所有可访问的WPS Office版本后得出的结论，因为金山在尝试修复此漏洞时并未特别提供其操作的精确细节。

2024-04-30：ESET分析了来自VirusTotal的恶意文档，发现它正在积极利用CVE-2024-7262，这是文档首次使用时的一个零日漏洞。ESET还发现金山毒霸的静默补丁仅解决了部分错误代码，其余有缺陷的代码仍然可被利用。

2024-05-25：ESET联系了金山软件，报告了其发现。虽然第一个漏洞已经修复，但ESET询问他们是否可以创建CVE条目和/或公开声明，就像他们对CVE-2022-24934所做的那样。

2024-05-30：金山软件承认了这些漏洞并告诉ESET会及时更新信息。

2024-06-17：ESET要求更新。

2024-06-22：金山软件告诉ESET开发团队仍在努力解决这个问题，并计划在即将推出的版本中修复这个问题。

2024-07-31：根据后续测试，ESET发现CVE-2024-7263已被悄悄修复，ESET告知金山软件已预留并正在准备CVE-2024-7262和CVE-2024-7263。

2024-08-11：DBAPPSecurity团队独立发布了其调查结果。

2024-08-15：CVE-2024-7262和CVE-2024-7263发布。

2024-08-16：ESET要求金山软件进行另一次更新。

2024-08-22：金山软件承认已于5月底修复了CVE-2024-7263，这与该公司在2024-06-22声称其开发团队“仍在努力解决该问题”的说法相矛盾。

2024-08-28：金山软件已承认这两个漏洞，并已修复。但是，该公司表示无意公开CVE-2024-7262的野外利用情况，因此ESET现在发布此博文，以警告金山软件的客户，由于CVE-2024-7262漏洞和漏洞利用的野外利用和第三方披露，他们应紧急更新WPS Office，这增加了进一步利用的机会。

结论

由于WPS Office是一款主要分布在亚洲的软件套件，APT-C-60表明了其对东亚国家目标的攻击决心。无论该组织是开发还是购买了 CVE-2024-7262 的漏洞，都肯定需要对该应用程序的内部进行一些研究，还需要了解 Windows 加载过程的行为方式。该漏洞非常狡猾，因为它具有足够的欺骗性，可以诱骗任何用户点击看似合法的电子表格，同时还非常有效和可靠。选择MHTML文件格式使攻击者能够将代码执行漏洞转变为远程漏洞。此外，ESET发现CVE-2024-7263强调了仔细的补丁验证过程以及确保核心问题得到完全解决的重要性。ESET强烈建议Windows版WPS Office用户将其软件更新到最新版本。

**参考资源：**

1.https://www.welivesecurity.com/en/eset-research/analysis-of-two-arbitrary-code-execution-vulnerabilities-affecting-wps-office/

2.https://thehackernews.com/2024/08/apt-c-60-group-exploit-wps-office-flaw.html

3.https://vulnera.com/newswire/apt-c-60-group-exploits-wps-office-vulnerability-to-deploy-spyglace-backdoor/

原文来源：网空闲话plus

“投稿联系方式：sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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