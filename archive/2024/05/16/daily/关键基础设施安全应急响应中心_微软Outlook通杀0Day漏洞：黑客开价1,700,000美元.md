---
title: 微软Outlook通杀0Day漏洞：黑客开价1,700,000美元
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247543723&idx=2&sn=5043ee6a15382491ce491b2b77bbd771&chksm=c1e9a7faf69e2eec63a27f7bde86de9197a15b953fe940b0160c254d3e0f41ba076300818edc&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-05-16
fetch_date: 2025-10-06T17:16:26.915062
---

# 微软Outlook通杀0Day漏洞：黑客开价1,700,000美元

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvQcFs5Izj4VegjeicR2KgO0PXUgQvRMhHhS6NSeWMtjiaqcQQVibSInicqmQdrGV4J9ibPgrZ7gYPr4WQ/0?wx_fmt=jpeg)

# 微软Outlook通杀0Day漏洞：黑客开价1,700,000美元

关键基础设施安全应急响应中心

以下文章来源于网空闲话plus
，作者网空闲话

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM66kAclWVgNvfjr86OjY0XhbScmMc5RGNPzgL9G5cm4Gw/0)

**网空闲话plus**
.

原《网空闲话》。主推网络空间安全情报分享，安全意识教育普及，安全文化建设培育。将陆续推出网安快讯、网安锐评、网安政策、谍影扫描、APT掠影、密码技术、OT安全等专集。

**一个名为“Cvsp”的威胁参与者宣布出售所谓的Outlook远程代码执行 (RCE) 0day**漏洞**。这一所谓的漏洞旨在攻击跨x86和x64架构的各种Microsoft Office版本（2016、2019、LTSC 2021、365 Apps for Enterprise），即可通杀微软outlook。这将对全球**Microsoft Office**用户构成重大安全威胁。到底是确有其事，还是黑客借0day交易实施诈骗？无论如何，对Outlook用户而言，保持足够的警惕是必须的。**

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icWaT2eaYJNcKVvTZD0RbjibYT1J8OnbXP0AImWLUMe968ZfzuNz0picE97Ur9TvhlVKdPh0PaH0pKdg/640?wx_fmt=png&from=appmsg)

根据Cvsp的说法，Outlook RCE Exploit 0day已经在多个版本的Microsoft Office软件上经过了严格的测试，包括Office 2016、2019、LTSC 2021和Microsoft 365 Apps for Enterprise。威胁发起者声称成功率高达100%，令人震惊，这表明该漏洞在危害易受攻击的系统方面具有可靠性和有效性。

威胁行为者强调，有关该漏洞的具体信息只会私下披露。此外，与销售该漏洞相关的所有交易都将仅通过ShinyHunters提供的托管服务进行，这突显了该交易的秘密性质以及与在地下网络中销售此类高级漏洞相关的非法活动。

据威胁发起者Cvsp声称，Outlook RCE漏洞利用0day的价格为1,700,000美元。这笔巨额金额反映了该漏洞的严重性和效力，对用户构成了重大威胁。

**同样在这个breachforums.st的交易论坛上，Cvsp曾回答提问者的疑问时称0day漏洞只会卖给一个用户。**

Cvsp在该论坛上还有另外几个漏洞出售信息，其中一个5月2日发布的有关Vmware的号称0day漏洞，同样也开了1300000美元的天价。承诺100%能够利用成功，并称可通过TeleGram沟通，索取漏洞细节和利用的演示视频。

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icWaT2eaYJNcKVvTZD0RbjibY9SUQmiaRdEvkpKiaY90Yw1sibZKDNQkvqMg0cyytERWK8ibNEibCnsWAn6g/640?wx_fmt=png&from=appmsg)

再早先的4月18日，Cvsp还发布过一条出手Windows本地提权0day的广告，当时开价150000美元。

**此类漏洞交易信息的真伪难以验证。**但在交易论坛上，担保者即论坛的管理员ShinyHunters为发帖称，查看漏洞描述详细信息和PoC后，这似乎是合理的。处理此类金额时请务必使用MM（After reviewing the details and the PoC, this seems legitimate. Please always use MM when dealing with such amounts.）。名为succumb的论坛用户称，VMware 0day是真的，Cvsp是一个合法的商人（Real VMware 0day, Cvsp is a legit businessman.）。

**Outlook和目标软件的开发商微软尚未对这些说法做出回应。网络安全社区正在热切等待这家科技巨头的任何确认或否认，以及为应对这一威胁而可能发布的任何潜在建议或补丁。此漏洞的销售突显了网络安全中持续存在的挑战，特别是0day漏洞造成的威胁。**

有关微软outlook公开的最新RCE漏洞，还是2024年2月份Check Point漏洞研究员Haifei Li发现并跟踪为CVE-2024-21413的漏洞，当使用易受攻击的Microsoft Outlook版本打开带有恶意链接的电子邮件时，该漏洞会导致远程代码执行(RCE)。

**专家建议，针对此类重大漏洞信息，宁可信其有，不可信其无。即使不存在这个所谓的0day漏洞，仍然建议用户特别警惕：关注该漏洞的最新消息，不要打开任何可疑文件，尤其是通过电子邮件收到的文件，并定期检查Microsoft Office的更新，当有官方发布的补丁可用时，尽快修复以保护自己的系统。**

**参考资源**

1、https://breachforums.st/Thread-SELLING-Outlook-RCE-0day

2、https://breachforums.st/Thread-SELLING-0day-VMware-ESXi-VME

3、https://dailydarkweb.net/a-threat-actor-claims-sale-of-outlook-rce-exploit-0-day-for-1700000/

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