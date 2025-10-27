---
title: 【安全圈】7-Zip 漏洞可让远程攻击者绕过保护并执行任意代码
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067553&idx=4&sn=2c06e2c2a5011eb86894033a1e6c41fc&chksm=f36e7aa1c419f3b7663e1033a2b71bafbadf19c12ebb839d8cc5c2a954da81be8f83c2a04925&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-23
fetch_date: 2025-10-06T20:11:14.225549
---

# 【安全圈】7-Zip 漏洞可让远程攻击者绕过保护并执行任意代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhyib5x2iaJ6V78pWUbxkRKaRfGdPibiaiceabPIeQur6Z42B8MDrjnb2jgdUmZRtSVaCOXXTZ8IcmBlnQ/0?wx_fmt=jpeg)

# 【安全圈】7-Zip 漏洞可让远程攻击者绕过保护并执行任意代码

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhyib5x2iaJ6V78pWUbxkRKaREcDxw9y2ZpMXaZpoaHd93IC6Vl49E7Ck3cnmfwHe7bYaSg4teSn8CA/640?wx_fmt=jpeg&from=appmsg)

流行文件归档软件 7-Zip 中最近披露的一个漏洞（编号为 CVE-2025-0411）引发了严重的安全担忧。

此漏洞允许远程攻击者绕过 Windows 的 Mark-of-the-Web (MOTW) 保护机制，从而可能在受影响的系统上执行任意代码。此漏洞的 CVSS 评分为 7.0，反映出其严重性。

## **7-Zip 代码执行漏洞**

该问题源于对从带有 MOTW 标志的精心制作的档案中提取的文件处理不当。当用户使用易受攻击的 7-Zip 版本提取此类文件时，提取的文件不会保留 MOTW 标志。

此疏忽使攻击者能够绕过旨在防范恶意内容的关键安全检查。通过利用此漏洞，攻击者可以在当前用户的上下文中执行任意代码。

漏洞利用需要用户交互，例如访问恶意网页或打开恶意文件。这使得该漏洞在用户频繁处理来自不受信任来源的文件的环境中尤其令人担忧。

最近，7-Zip 中又发现了一个代码执行漏洞，编号为CVE-2024-11477，影响了 24.07 版本。当用户与恶意档案进行交互时，此漏洞使攻击者能够在当前进程的上下文中执行任意代码。

该漏洞影响 7-Zip 的所有版本，最高版本为 24.07。强烈建议用户更新至 24.09 版本，该版本可解决此问题并确保 MOTW 标志正确传播到提取的文件中。

* 2024 年 10 月 1 日：该漏洞已报告给供应商。
* 2025 年 1 月 19 日：协调公开披露并发布修补版本。

此漏洞对用户构成重大风险，因为它破坏了 Windows 的一项关键安全功能，该功能旨在防止不受信任的文件在未经适当审查的情况下执行。攻击者可以利用此漏洞传播恶意软件或未经授权访问系统，尤其是在用户拥有管理权限的环境中。

零日计划对发现并报告此漏洞的研究员 Peter Girnus 表示感谢。

#### **缓解步骤**

1. **更新软件**：用户应立即升级到 7-Zip 版本 24.09 或更高版本。
2. **请谨慎操作**：避免打开来自未知或不受信任来源的档案。
3. **启用额外保护**：使用可以检测和阻止可疑文件活动的端点安全解决方案。

虽然 7-Zip 长期以来一直是值得信赖的文件压缩和提取工具，但此次事件凸显出，即使是广泛使用的软件也可能存在漏洞。用户和组织应迅速采取行动，以减轻与此漏洞相关的风险。

来源：https://cybersecuritynews.com/7-zip-vulnerability-arbitrary-code-2/

***END***

阅读推荐

[【安全圈】B站2025年第一个大瓜，“代码投毒”报复用户](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067526&idx=1&sn=c7bb681b7008589588039d0669578174&scene=21#wechat_redirect)

[【安全圈】梅赛德斯—奔驰信息娱乐系统漏洞详细信息披露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067526&idx=2&sn=35fd8cf175959d2493340598399f5c01&scene=21#wechat_redirect)

[【安全圈】新型Android恶意软件模仿聊天应用窃取敏感数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067526&idx=3&sn=78bd7100124b3e45c47f00500c234a7a&scene=21#wechat_redirect)

[【安全圈】OWASP 2025 年十大漏洞 – 被利用/发现的最严重漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067526&idx=4&sn=b3d1ba063b429d95b1315af7a9713b77&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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