---
title: 打开邮件即中招！Outlook高危漏洞曝光：黑客可远程执行代码
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589341&idx=2&sn=698cf3be8150d9f8778afdf43da1a5ae&chksm=b18c281786fba10119471d2669a6ee3e5ea59ed667e0f945a2b14c65bca52e844932e4e21204&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-09
fetch_date: 2025-10-06T20:36:54.225799
---

# 打开邮件即中招！Outlook高危漏洞曝光：黑客可远程执行代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HuOibxwzgwaCgdy8P5STK2fOpgFmvCAOpxLjMsjYicxsH05vSyr6cHpQpk4olr8zgp3BU8dAJHNdNQ/0?wx_fmt=jpeg)

# 打开邮件即中招！Outlook高危漏洞曝光：黑客可远程执行代码

看雪学苑

看雪学苑

美国网络安全和基础设施安全局（CISA）于2月7日发布公告，要求美国联邦机构在2月27日前完成系统补丁部署，以修复微软Outlook高危远程代码执行漏洞。该漏洞编号为CVE-2024-21413，由网络安全公司Check Point Research的安全专家Haifei Li在2024年1月发现并通报给微软。微软已于2024年2月发布修复补丁，安装KB5002537及更高版本的补丁即可修复该漏洞。

该漏洞的严重性极高，CVSS评分为9.8分（满分10分），表明其潜在威胁巨大。攻击者利用该漏洞的方式是通过发送带有恶意链接的钓鱼邮件，诱导用户点击。这些链接通过“Moniker Link”绕过Outlook的保护视图，使用file://协议指向黑客控制的服务器URL，并在URL中添加感叹号和随机文本（例如“!something”）嵌入到邮件中。当用户打开带有恶意链接的邮件时，攻击者即可远程执行任意代码，窃取用户的NTLM凭据。

该漏洞影响多个Office产品，包括Microsoft Office LTSC 2021、Microsoft 365 Apps for Enterprise、Microsoft Outlook 2016和Microsoft Office 2019。CISA已将此漏洞添加到其已知被利用漏洞（KEV）目录中，并将其标记为正在被积极利用。CISA强调，这类漏洞是恶意网络行为者常用的攻击途径，对联邦企业构成重大风险。虽然CISA主要关注提醒联邦机构尽快修补漏洞，但也建议私营机构优先修补这些漏洞，以阻止正在进行的攻击。

资讯来源：bleepingcomputer

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibExiboJzOiafqGLvlOkrmU6NIr3qSr7ibpkIo2N5mhCTNXoMl37s2oRSIDw/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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