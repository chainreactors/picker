---
title: 【安全圈】Microsoft Office 365 消息加密被曝采用不安全的操作模式
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652021391&idx=4&sn=8e31f184e6360a19553bb94b259889d5&chksm=f36f8ecfc41807d9271820bcdb739ebc666db769a4fb495a1741e0bc6c84fed4d2c750718f50&scene=58&subscene=0#rd
source: 安全圈
date: 2022-10-21
fetch_date: 2025-10-03T20:30:27.390264
---

# 【安全圈】Microsoft Office 365 消息加密被曝采用不安全的操作模式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljjWhWJN7NGqiayj0ZRib7jvomibOMxh9rVaGbISjHFRhAl53moKOQggzcDORHicKnODDS5fCLI6PuA4g/0?wx_fmt=jpeg)

# 【安全圈】Microsoft Office 365 消息加密被曝采用不安全的操作模式

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljjWhWJN7NGqiayj0ZRib7jvo4WYtFZU2849lBz01v2HAwU4dicYHqID9TFUETeafCm1NClOSuW1qV2g/640?wx_fmt=jpeg)

**关键词**

Microsoft Office 365

Microsoft Office 365消息加密（OME）采用电子密码本（ECB）操作模式。这种模式通常是不安全的，可能会泄露所发送消息的结构方面的信息，这可能导致部分或全部消息泄露。

正如美国国家标准与技术研究所（NIST）发布的《提议修订特别出版物800-38A 的公告》所述：“在NIST全国漏洞数据库（NVD）中，使用ECB加密机密信息构成了严重的安全漏洞；比如，参阅CVE-2020 -11500：https://nvd.nist.gov/vuln/detail/CVE-2020-11500。”

Microsoft Office 365提供了一种发送加密消息的方法。微软声称该功能让组织可以以一种安全的方式在组织内外的人员之间发送和接收加密的电子邮件。遗憾的是，OME消息是在不安全的电子密码本（ECB）操作模式下被加密的。

由于ECB泄露了消息的某些结构信息，如果第三方可以访问加密电子邮件消息，也许就能够识别消息内容。这会导致机密性可能丧失。

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGyljjWhWJN7NGqiayj0ZRib7jvoY0p0lGKDTPJNUnwDIR74InoJtSHp6h1dSlNPRByNEOrbAcShKjhcuw/640?wx_fmt=png)

图1. 从Office 365邮件加密保护的电子邮件中提取的图像

由于加密消息是作为常规电子邮件附件发送的，因此发送的消息可能会存储在各种电子邮件系统中，可能已被发送者和接收者之间的任何有关方截获。

如果攻击者拥有庞大的消息数据库，可以通过分析截获消息的重复部分的相对位置，推断其内容（或部分内容）。

大多数OME加密消息都受到影响，攻击者可以对任何之前发送、接收或截获的加密消息离线执行攻击。组织无法阻止已经发送的消息被人分析，也无法使用权限管理功能来解决这个问题。

视通过加密消息发送的内容而定，一些组织可能需要考虑该漏洞的法律影响。正如欧盟《通用数据保护条例》（GDPR）、《加利福尼亚州消费者隐私法》（CCPA）或其他类似法规所述，漏洞可能会导致隐私受到影响。

电子密码本（ECB）操作模式意味着每个密码块都单独加密。明文消息的重复块总是映射到相同的密文块。实际上，这意味着虽然实际的明文并不直接显示，但消息结构方面的信息却直接显示。这是在ECB操作模式下经过AES加密的RAW图像：

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGyljjWhWJN7NGqiayj0ZRib7jvopRS4Q8EXtNZBaGqSCkpXxNGBY9wc9xQTXayLcHaDZE9aal4vOXOXOA/640?wx_fmt=png)

虽然不知道实际的单个像素值，但可以轻松识别图像的实际内容。

即使特定消息不会以这种方式直接泄露信息，拥有大量消息的攻击者仍可以分析文件中重复模式的关系来识别特定文件。这可能导致加密消息的（部分）明文能够推断出来。

不需要知道加密密钥就可以利用该漏洞，因此自带密钥（BYOK）或类似的加密密钥保护措施没有任何补救方面的影响。

用于Microsoft Office 365消息加密的密码似乎是高级加密标准（AES）。然而面对这个漏洞，实际的密码无关紧要，因为无论使用何种密码，ECB操作模式都具有相同的属性。

CWE-327：使用损坏或有风险的加密算法

Outlook 365消息加密在将邮件加密成RPMSG blob时使用电子密码本（ECB）操作模式。

这个漏洞的根本原因似乎是事先决定使用具有消息加密功能的电子密码本（ECB）操作模式，然后一直采用这个糟糕的决定。

Microsoft信息保护（MIP）ProtectionHandler::PublishingSettings类有一个 SetIsDeprecatedAlgorithmPreferred方法，文档对该方法描述如下：

“设置是否优先使用被废弃的加密算法（ECB）以实现向后兼容性。”

OME很可能使用这种方法来启用RPMSG的ECB加密。如果未设置该标志，则使用密码块链接（CBC）操作模式。

Microsoft信息保护FIPS 140-2 合规文档提到：

“旧版Office（2010）需要AES 128 ECB，而Office文档仍以这种方式受到Office应用程序的保护。”

缓解措施

在多次询问漏洞状态后，微软最终回复如下：

“我们认为漏洞报告不符合安全服务标准，也不被认为是泄密事件。没有更改代码，因此没有为此报告发布CVE。”

电子邮件系统的最终用户或管理员无法强制执行更安全的操作模式。由于微软没有计划修复该漏洞，唯一的缓解措施是避免使用Microsoft Office 365消息加密。

资料卡

类型：使用损坏或有风险的加密算法

严重程度：很高

受影响的产品：Microsoft Office 365

缓解措施：由于微软没有计划修复这个漏洞，唯一的缓解措施就是避免使用Microsoft Office 365 消息加密。

感谢：感谢WithSecure Consulting公司的Harry Sintonen发现漏洞。

参考：MSRC VULN-060517

时间线

2022-01-11 发现漏洞。通过MSRC报告该漏洞，编号为VULN-060517。

2022-01-19 微软发放赏金5000美元。

2022-05-19 就问题的状态与微软取得联系，没有收到回复。

2022-08-29 向微软告知计划公开披露。

2022-09-21 微软对此问题进行了跟进，声称“我们认为漏洞报告不符合安全服务标准，也不被认为是泄密事件。没有更改代码，因此没有为此报告发布CVE。”

2022-10-14 WithSecure发布公告。

来源：ROARTALK

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljjWhWJN7NGqiayj0ZRib7jvoM314icXjtCjPncUDgKPSfkBdFlHNZiathkvEo1To9kT2S5JP3LChIP0g/640?wx_fmt=jpeg)

# [【安全圈】8位数密码不安全了！八块RTX 4090显卡阵列一小时即可破解](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652021287&idx=1&sn=0ce508635fd3a18463370af901bcabb2&chksm=f36f8e67c4180771836d81d2479d1a14197842a214e24b4e309140f7948cbc0af1ced360baab&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljjWhWJN7NGqiayj0ZRib7jvoIOfOicXVGrZpckgQfFkjiagzibuPPW2OiaiccOptfBZ8vnkJLWBDeWlm4rQ/640?wx_fmt=jpeg)

# [【安全圈】新的网络钓鱼工具：Caffeine网络钓鱼即服务平台](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652021287&idx=2&sn=07c3bb4ef6ba77492f6c018588d46214&chksm=f36f8e67c418077114a2d51465b17253c8134c7bbe0687abbba4a5eebb2bc90839764ad48832&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljjWhWJN7NGqiayj0ZRib7jvoxllSuljUoEib8R7HH0v5yKicH9Vb1u5nb9icavbNKIYbLRMlsEkB2QiaPw/640?wx_fmt=jpeg)

# [【安全圈】日本科技公司受到 LockBit 3.0 的打击，多个供应链受到影响](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652021287&idx=3&sn=f8f5e73539c3a35f72506b158cc0791b&chksm=f36f8e67c4180771a2ea13e4a6def233890cccfdfa8a8053b7e396561c875537506d718afb92&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyljjWhWJN7NGqiayj0ZRib7jvoqTKlfFZ1FcdlMaqZ9kqa4q3WxI4fXQvRnicTyibkJo0OiatdqU2aJVZMQ/640?wx_fmt=jpeg)

# [【安全圈】0patch比微软官方更早推出MotW零日漏洞补丁](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652021287&idx=4&sn=f4c2aa053f4835b6c386687a6171835f&chksm=f36f8e67c4180771dda047817eb3abe66f75d785813b40cf4be4d8d94f007bf567025c68fb95&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

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