---
title: Ivanti 修复 Connect Secure & Policy Secure 中的三个严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522224&idx=1&sn=671c73813c868c4819c48a9b54ab1b8c&chksm=ea94a6dadde32fccbdd41325f91efdd1c4ec286a388c08a1ede020c3367c7438561f706f6826&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-14
fetch_date: 2025-10-06T20:36:58.480941
---

# Ivanti 修复 Connect Secure & Policy Secure 中的三个严重漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQX37nv0icdfE4wTaPlovRic4ic0icnbVCpkpa8Xsm7x6TH0635bBYvNdawhkdgb5Vue9JEJgmqM9WWiaQ/0?wx_fmt=jpeg)

# Ivanti 修复 Connect Secure & Policy Secure 中的三个严重漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Ivanti 已为 Ivanti Connect Secure (ICS)、Ivanti Policy Secure (IPS) 和 Ivanti Secure Access Client (ISAC) 发布安全更新，修复了多个漏洞，其中包含三个严重漏洞。**

Ivanti 公司通过CISA和Akamai公司研究人员参与的负责任披露计划和 HackerOne 漏洞奖励平台获悉这三个漏洞。Ivanti 公司在安全通告中提到，并未收到关于这些漏洞遭在野利用的报告。然而，该公司建议用户尽快安装安全更新。

Ivanti公司修复的三个严重漏洞如下：

* CVE-2025-22467：ICS中的基于栈的缓冲区溢出漏洞，可导致具有低权限的远程认证攻击者执行代码（严重性评分9.9）。
* CVE-2024-38657:：对文件名称的外部控制漏洞，可导致认证攻击者在ICS和IPS中执行任意文件写（严重性评分9.1）。
* CVE-2024-10644：代码注入漏洞可导致远程认证攻击者在ICS和IPS中执行远程代码（严重性评分9.1）。

这三个漏洞均可遭远程利用，不过攻击者首先需要进行认证。另外，利用其中两个漏洞还需拥有管理员权限才能实现远程代码执行或任意文件写后果。

尽管如此，其中的风险仍然巨大，因为通过钓鱼攻击、过往数据泄露或暴力破解密码等手段窃取凭据的内部威胁人员或攻击者仍然能够恶意利用这些漏洞。

Ivanti 公司还在安全通告中提到了另外五个漏洞，严重程度从中危到高危不等，如XSS漏洞、硬编码密钥、明文存储敏感数据以及权限不充分等。这些漏洞影响 ICS 22.7R2.5及以下版本、IPS 22.7R1.2及以下版本以及ISAC 22.7R4及以下版本。这些漏洞已在 ICS 22.7R2.6、IPS 22.7R1.3和ISAC 22.8R1中修复。

Ivanti 公司还提到，这些漏洞还影响 Pulse Connect Secure 9.x，但表示由于产品已达生命周期，因此不再提供修复方案。该公司解释称，“Pulse Connect Secure 9.x版本已在2024年6月达到工程终期，并在2024年12月31日达到支持周期。因此，Connect Secure 9.x版本不再接受移植的修复方案。”该公司建议客户升级至 Ivanti Connect Secure 22.7版本。

Ivanti 公司并未提供已修复漏洞的任何缓解措施，建议用户应用最新安全更新。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Ivanti修复Endpoint Manager中的多个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522089&idx=1&sn=a04239b89ce2032e8e28b49d05782135&scene=21#wechat_redirect)

[Ivanti提醒注意 Connect Secure 产品中的新0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522025&idx=2&sn=f67e98879ae334210339981b77e939e9&scene=21#wechat_redirect)

[Ivanti：注意这个CVSS 满分的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521758&idx=1&sn=d87a2de8e47def08cf6aca1b91b6e064&scene=21#wechat_redirect)

[Ivanti 中的3个0day已遭活跃利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521006&idx=2&sn=9a5993bb8ee14a8ab3071f40bb56c909&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/ivanti-fixes-three-critical-flaws-in-connect-secure-and-policy-secure/

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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