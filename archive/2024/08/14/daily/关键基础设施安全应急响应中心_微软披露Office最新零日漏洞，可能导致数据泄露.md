---
title: 微软披露Office最新零日漏洞，可能导致数据泄露
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545333&idx=3&sn=aeb6d7bb499cb9e7875eed7b2ebe2e00&chksm=c1e9bda4f69e34b2f9e2acf8bf5c86c0928ad8ddc68ab52a3afdf27cd993722049424991b40e&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-08-14
fetch_date: 2025-10-06T18:04:03.779820
---

# 微软披露Office最新零日漏洞，可能导致数据泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogsicBRZn8ZNCenaLicQdVoJB3p6aCfRogrKJxqycEbnSicjD2MFFj6YTYGDwEJnkeqqYgvxmA2Xke2hw/0?wx_fmt=jpeg)

# 微软披露Office最新零日漏洞，可能导致数据泄露

关键基础设施安全应急响应中心

近日，微软披露了 Office 中一个未修补的零日漏洞，如果被成功利用，可能导致敏感信息在未经授权的情况下泄露给恶意行为者。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39HkdkkbeicU4UFJAMggoNRibS1ddz9kR60n9l0TMSnGpSsk6aib4QNVktXKpftiaBicoV7xyo5ALLVMog/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic)

该漏洞被追踪为 CVE-2024-38200（CVSS 得分：7.5），被描述为一个欺骗漏洞，影响以下版本的 Office：

* 32 位版本和 64 位版本的 Microsoft Office 2016
* 32 位版本和 64 位版本的 Microsoft Office LTSC 2021
* 适用于 32 位和 64 位系统的 Microsoft 365 企业应用程序
* 适用于 32 位和 64 位系统的 Microsoft Office 2019

微软在一份公告中提到：在基于网络的攻击场景中，攻击者可以托管一个网站，或利用一个接受或托管用户提供内容的受攻击网站，该网站包含一个特制文件专门利用该漏洞。

但是，攻击者无法强迫用户访问该网站。相反，攻击者必须诱导用户点击一个链接，通常是通过电子邮件或即时通信信息中的诱导方式，然后说服用户打开特制文件。

CVE-2024-38200的正式补丁预计将于8月13日正式发布。不过微软公司表示，他们已经确定了一种替代修复的方法，并已从2024年7月30日起通过「功能飞行」（Feature Flighting）启用了该修复方法。

该公司还指出，虽然客户已经在所有支持版本的微软Office和微软365上得到了保护，但为了最大程度的规避安全风险，用户应在最终版本的补丁发布后立即更新。

微软对该漏洞进行了「不太可能被利用」的评估，并进一步概述了三种缓解策略：

* 配置「网络安全：配置」限制 NTLM：向远程服务器发出 NTLM 流量策略设置，允许、阻止或审计从运行 Windows 7、Windows Server 2008 或更高版本的计算机向任何运行 Windows 操作系统的远程服务器发出的 NTLM 流量
* 将用户添加到受保护用户安全组，防止将 NTLM 用作身份验证机制
* 使用外围防火墙、本地防火墙并通过 VPN 设置阻止 TCP 445/SMB 从网络向外发送，以防止向远程文件共享发送 NTLM 身份验证信息

在披露该漏洞的同时，微软还表示其正在努力解决CVE-2024-38202 和 CVE-2024-21302两个零日漏洞，这些漏洞可能被利用来「解除」最新 Windows 系统的补丁，并重新引入旧漏洞。

上周，Elastic 安全实验室披露Windows智能应用控制（Smart App Control）和智能屏幕（SmartScreen）存在一个设计漏洞，该缺陷允许攻击者在不触发安全警告的情况下启动程序，至少自2018年以来一直在被利用。

智能应用控制是一项基于信任的安全功能，它使用微软的应用智能服务进行安全预测，并利用Windows的代码完整性功能来识别和阻止不受信任的（未签名的）或潜在危险的二进制文件和应用程序。

Elastic安全实验室认为，这一漏洞多年来一直被滥用，因为他们在VirusTotal中发现了多个利用此漏洞的样本，其中最早的提交时间超过六年。

**参考资料：**

https://thehackernews.com/2024/08/microsoft-warns-of-unpatched-office.html

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

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