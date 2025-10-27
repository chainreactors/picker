---
title: FORTINET威胁研究：二维码网络钓鱼试图窃取中文用户的凭据
url: https://mp.weixin.qq.com/s?__biz=MzAwMTMzMDUwNg==&mid=2650887197&idx=1&sn=45330cc8286068741a28a06d3ba55ed1&chksm=812ea838b659212eee846620915730a30c712961070ba9f94d1cdbec7de1241dda8deded0a59&scene=58&subscene=0#rd
source: 网安杂谈
date: 2023-01-26
fetch_date: 2025-10-04T04:52:44.610476
---

# FORTINET威胁研究：二维码网络钓鱼试图窃取中文用户的凭据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWOCKZX8bt6f42fURMwWUbFicD65KLnhe1J4JerC1a4YxhWerswBg9LdFgOmFRqtCpj59j3uf7Te1Xw/0?wx_fmt=jpeg)

# FORTINET威胁研究：二维码网络钓鱼试图窃取中文用户的凭据

FORTINET

网安杂谈

本文转自FORTINET公司威胁研究。原文链接：https://www.fortinet.com/blog/threat-research/qr-code-phishing-attempts-to-steal-credentials-from-chinese-language-users

每天，数以百万计的互联网和应用程序用户在他们购物、工作、支付账单、社交和流媒体娱乐的无数地方输入无处不在的用户名和密码。这种做法具有重大风险。如果其中一个位置遭到入侵，该用户名和密码信息通常会进入暗网市场，在那里出售。如果这些凭据可以在金融机构或在线购物网站等对犯罪分子具有货币价值的地方重复使用，那么它们可能会非常有价值。

受影响的平台： 受影响的移动和桌面

用户：移动和桌面

影响：窃取凭据的可能性

严重性级别：中等

网络犯罪分子使用各种旨在窃取凭据的技术。FortiGuard Labs 最近发现了一个有趣的网络钓鱼活动，使用各种二维码来针对中文用户。它旨在通过引诱用户将其数据输入威胁参与者拥有的网络钓鱼网站来窃取凭据。

**网络钓鱼电子邮件**

该电子邮件相当简单和精简，并包含一个Microsoft Word附件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWOCKZX8bt6f42fURMwWUbFicwo6FXlFgbV78lPO6ZRAGGPCOcOoXqiatbjiaIIicZQRBF0Jbml9kWwTxw/640?wx_fmt=png)

图1.网络钓鱼电子邮件

这封电子邮件试图欺骗中国财政部。翻译成英文，图1中的电子邮件主题是：“关于2022年申请个人劳务补贴的通知”。正文称，“请点击附件查看财政部2022年第四季度申请个人劳务补贴的通知！Microsoft Word附件“转发：关于财四季度个人劳动补贴申领通知.docx”翻译为：“转发：关于申请本财年第四季度个人劳动补贴的通知.docx。

打开附件后，用户会在文档中心看到一些文本和一个大二维码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWOCKZX8bt6f42fURMwWUbFicPhKG4LJv8I0htSlCVj8ib8wnmj5xZShKTAxButCrvR67bxM27m6Vy8A/640?wx_fmt=png)

图2.带有二维码的 Word 文档

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWOCKZX8bt6f42fURMwWUbFicJzVkCuzzxWcQr3mmrU0K2H6qfCuE3X5OC1zaZhDX3aOiaicHQS6zW6Vg/640?wx_fmt=png)

图3.微软Word文档的英文翻译

**二维码**

二维码需要应用程序阅读并将其翻译成可操作的内容。大多数手机通过相机都具有此功能，并且所有主要平台上都有软件包可以通过计算机执行此操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWOCKZX8bt6f42fURMwWUbFicng7SPgQibbqOyz0T8zDNxZvNdblJQUmmLiaV9kQbPexRsVsPicZ21YtUA/640?wx_fmt=png)

图4.伪造官方二维码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWOCKZX8bt6f42fURMwWUbFicmNDrSr8mJ51JdLEq939NU39tNR5YGC3YJI1saX6DxZMdh5eib2BNPhw/640?wx_fmt=png)

图5.二维码假冒微信标志

在FortiGuard Labs找到的每个示例中，Microsoft Word附件中包含的QR码都为用户提供了一个URL。当用户使用其桌面平台或移动设备执行此操作时，他们会到达由威胁参与者控制的网站。

**网站**

FortiGuard Labs审查了链接的网站。它是钉钉实例的欺骗性传真（需要注意的是，截至发布日期，本站现已下线）。钉钉是阿里巴巴集团开发的一个广泛使用的企业通信平台。鉴于该平台的覆盖范围及其大量用户，它的凭据将是有价值的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWOCKZX8bt6f42fURMwWUbFiciaTk3nUKCy6Sr5x9PBsKv9HQymsWEicz6Yr57MWficZGVCkPiaAPsZXPZA/640?wx_fmt=png)

图6.威胁行为者控制的网站欺骗钉钉

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWOCKZX8bt6f42fURMwWUbFicjco3icU9cIDlB5wLqic1XqP1gnOgbbam2RqbvlfG1guBBYZlJte8kjbQ/640?wx_fmt=png)

图7.弹出窗口的英文翻译

用户被定向到一个弹出的消息框，表明他们的钉钉帐户犯了一些未指明的业务违规行为，并将在24小时内未经验证而被冻结。

确认消息框后，将邀请用户输入其凭据以解决问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWOCKZX8bt6f42fURMwWUbFicSSt3OJeXicWAUnA4WesqDxN9dPnTNicHtTT4a29JmBQMUcygPX8TDYJg/640?wx_fmt=png)

图8.凭据输入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWOCKZX8bt6f42fURMwWUbFic4On0aEic664c8k2vDGM9n3vvR5p5nA22UN4mppNb0lQv84HNTo6AHOQ/640?wx_fmt=png)

图9.凭据条目已翻译成英文

**结论**

凭据通过提供进入受害者应用程序或环境的直接途径，为犯罪分子和威胁参与者提供了宝贵的资源。这些可以直接使用或出售给另一个集团用于其运营。这个例子表明，攻击者正在付出巨大的努力来确保他们的目标网页看起来尽可能逼真，并且他们的诱饵可以说服受害者放松警惕。

无论攻击者的动机如何，这些攻击无疑都会在一段时间内普遍存在。警告用户验证电子邮件，不要打开附件或链接，并且切勿在以前从未见过的网站中输入凭据。鼓励用户访问供应商的已知主站点进行任何业务，而不是使用收到的链接。用户还可以将鼠标悬停在链接上以查找异常 URL。还鼓励组织向用户提供培训，以帮助他们识别和避免恶意电子邮件附件和链接。

**IOCs**

**File-based IOCs:**

|  |  |
| --- | --- |
| Filename | SHA256 |
| 重要通知.docx (Important Notice.docx) | 939656a000b7ca2f54bc42d635537261ce5194e2041f1c3ac37e3c72f8ec5333 |
| 转发：关于财四季度个人劳动补贴申领通知.docx (Forward: Notice on Application for Personal Labor Subsidy in the Fourth Quarter of Fiscal Year.docx) | f941b76a33b5a1d425569a0ed689023597fd7fc3acb301ec11a37feb71dcb597 |
| 财务重要通知.docx (Financial Important Notice.docx) | ac5f4ba15e883813b3018614887b8f65b2f90d252ab7cdffe6f05f8482e1672a |

**Network-based IOCs:**

|  |  |
| --- | --- |
| IOC | IOC type |
| hXXp://w.mryrej.cn | Credential theft site |
| hXXps://l99etsen5677cryptorgacme.h7g33.cn | Credential theft site |
| hXXp://www.sgiabuq189qhijl.cn | Credential theft site |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

网安杂谈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

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