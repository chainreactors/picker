---
title: JDownloader 下载器被黑客入侵，使用新型 Python 远程控制木马感染用户
url: https://mp.weixin.qq.com/s/R3y3BW3-zzUb8IE3x41q0g
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:34:36.868536
---

# JDownloader 下载器被黑客入侵，使用新型 Python 远程控制木马感染用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Mnic7SFrXzoSzgmScGia8uGbl4cw6g5Dok5vhB7O1eHGXWziaURjpsMoHeOexDpAEz2FaFJlTXibuPwaCL0v2U9ddibEATTTwWoGZo/0?wx_fmt=jpeg)

# JDownloader 下载器被黑客入侵，使用新型 Python 远程控制木马感染用户

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

JDownloader 是一款广受欢迎的开源下载管理器，深受全球数百万用户的信赖。2026 年 5 月初，它成为一起严重的供应链攻击事件的中心。攻击者悄悄入侵了官方的 jdownloader.org 网站，并将合法的安装程序下载链接替换为恶意文件，这些恶意文件携带了一个功能齐全的基于 Python 的远程访问木马。

在短短两天的窗口期内，任何下载了他们认为是标准安装程序的用户，都可能在不知不觉中将一个危险且持久的后门程序直接安装到了自己的计算机上。

此次攻击并未篡改 JDownloader 的实际软件或其应用内更新系统。相反，它针对的是该网站的下载链接，特别是 Windows 系统的“下载备用安装程序”选项和 Linux shell 安装程序链接。

2026年5月6日至7日期间点击这些链接的用户收到的文件看似真实，但实际上是未签名的包装文件，其中隐藏着多层恶意代码。这种欺骗手段非常逼真，以至于许多用户忽略了Windows SmartScreen的警告，认为这些警报只是误报。

jdownloader.org 的研究人员和开发人员在Reddit 用户 PrinceOfNightSky 于 2026 年 5 月 7 日举报可疑行为后，证实了此次入侵。该用户指出，下载的可执行文件被归类为名为“Zipline LLC”和“The Water Team”的发行商，而不是合法的开发商 AppWork GmbH。

团队在数小时内，即世界协调时17:24，将网站下线，并展开全面调查。5月8日晚至5月9日凌晨，网站恢复运行，所有恶意内容均已清除，服务器配置也已加强，以防止未来再次遭到攻击。所有链接均已验证安全。

## **JDownloader 下载器被破解**

此次攻击源于网站内容管理系统中一个未修补的漏洞，该漏洞允许攻击者在未经身份验证的情况下更改访问控制列表并修改特定页面。

日志显示，攻击者甚至在5月5日对一个低流量的测试页面进行了预演，之后才在第二天替换了正式的安装程序链接。整个行动展现了精心策划和耐心等待，这是老练的威胁行为者的典型特征，他们显然意图感染尽可能多的用户。

社区研究员 Takia\_Gecko 对恶意安装程序样本进行了深入的技术分析，揭示了其惊人的复杂程度。该伪造安装程序是一个未签名的包装器，它将真正的合法 JDownloader 安装程序与第二个经过 XOR 加密的恶意可执行文件捆绑在一起。

使用 XOR 密钥“ectb”解码隐藏的可执行文件，从而揭示出一个 Windows x64 加载器，然后使用密钥“fywo”解密更多资源，以解包受 PyArmor 8 保护的 Python 3.14 有效载荷。

最终的有效载荷是一个用 Python 编写的完整远程访问木马框架。它使用 RSA-OAEP 和AES-GCM 加密与其命令与控制服务器通信，支持通过 Telegraph、Rentry、Codeberg 和洋葱地址等平台进行死信箱解析，并使用密钥为“Chahgh4a”的 RC4 加密来解码实时 C2 URL。该木马以 pythonw.exe 为宿主，使攻击者能够随意在任何受感染的机器上推送和执行任意 Python 代码。

## **受影响用户现在应该做什么**

jdownloader.org 给出的最关键建议很明确：如果您下载并运行了受影响的安装程序，请彻底重新安装操作系统。杀毒软件扫描或许可以检测到一些威胁，但无法保证彻底清除恶意软件可能建立的所有持久化机制。

一些用户使用 Malwarebytes 和Windows Defender Offline 等工具进行了全面扫描，但没有发现任何恶意软件，这表明该恶意软件能够有效地隐藏其在受感染系统中的存在。

如果您仍然保留着已下载的文件但尚未运行，请不要运行它。而是通过右键单击该文件，选择“属性”，然后检查“数字签名”选项卡来验证数字签名。

正版 JDownloader 安装程序均由 AppWork GmbH 签名。任何未知发布者或缺少签名都属于严重可疑信号。在确认系统安全之前，请避免在受影响的计算机上登录敏感账户，并使用其他可信设备更改所有重要密码。

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