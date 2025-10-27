---
title: GitLab漏洞允许攻击者以其他用户身份运行流水线作业
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458563554&idx=3&sn=23a45f558e95ae27ddaf79590c903e1d&chksm=b18d836886fa0a7e19f77bbf304b9cdfe787c2624abbfb6fe18b55609adec23afd5ed4800741&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-13
fetch_date: 2025-10-06T17:43:07.049752
---

# GitLab漏洞允许攻击者以其他用户身份运行流水线作业

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EDOEyyAjIYqJ7ZShibj1sPqjRmdHAuD5sJj8icL5230llic0pwlwOb2lukVibpbHqeia3JO2u6YVs1mGw/0?wx_fmt=jpeg)

# GitLab漏洞允许攻击者以其他用户身份运行流水线作业

看雪学苑

看雪学苑

据GitLab于7月10日发布的公告，其最近修复了一个影响GitLab社区版和企业版的漏洞，该漏洞允许攻击者以其他用户的身份执行流水线作业，对全球用户构成了重大威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EDOEyyAjIYqJ7ZShibj1sPqtaXuoheDepChbgdKMichWicvofRjyUNhhickOfe0e4hJRMLxeMD5mB4uA/640?wx_fmt=png&from=appmsg)

GitLab的流水线（Pipeline）是平台持续集成/持续部署（CI/CD）系统的核心功能，供开发人员自动运行流程任务以构建、测试及部署代码更改。攻击者以其他用户身份运行这些流水线将导致未经授权的代码执行、数据外泄以及潜在的供应链攻击等恶意活动。

该漏洞（CVE-2024-6385，CVSS评分9.6）所影响的版本为15.8至16.11.6、17.0至17.0.4、17.1至17.1.2。GitLab应用程序安全工程师Rohit Shambhuni在安全通知中写道：“在某些情况下，允许攻击者以另一个用户的身份触发流水线。”但没有具体说明允许这种攻击所需的情况。

Contrast Security首席信息安全官David Lindner表示，这个漏洞是管理员所需要关注的事项，并应立即遵循GitLab的建议进行升级。“这真的很糟糕，因为它实际上关闭了运行流水线的访问控制，而流水线是将软件从开发移动到生产的命脉。这个漏洞可能允许未经授权的用户以任何其他用户的身份执行流水线作业，从而可能使攻击者运行恶意代码、访问敏感数据并危害软件完整性。”

Synopsys Software Integrity Group的研究员Ray Kelly也表示，在SecDevOps领域的快节奏发展中，任何对流水线功能漏洞的提及都可能让用户脖子发凉。一旦流水线受到破坏，软件可能会被恶意软件、后门更改，或用于从组织中窃取私人信息。

编辑：左右里

资讯来源：gitlab、devops

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

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