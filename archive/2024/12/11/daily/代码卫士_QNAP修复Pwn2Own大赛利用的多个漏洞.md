---
title: QNAP修复Pwn2Own大赛利用的多个漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521736&idx=2&sn=37cc8cc02d4dc7c59168f8bb841938a9&chksm=ea94a4a2dde32db4fcf8d9da57d0da38ee6f89a7cfeee9b469e91b0bc2d89db95227a50943f1&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-11
fetch_date: 2025-10-06T19:41:13.804175
---

# QNAP修复Pwn2Own大赛利用的多个漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTsjrxKUfO6ZlYcrL824wwQz6v9x2wBzqyloLxgenTkngMswZlPvOiaFOJVicU8icHCic9ib9cDvERd6FA/0?wx_fmt=jpeg)

# QNAP修复Pwn2Own大赛利用的多个漏洞

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**上周末，QNAP系统修复在2024年Pwn2Own 爱尔兰大赛中演示的QTS 和 QuTS Hero 中的多个漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTsjrxKUfO6ZlYcrL824wwQ1W6yJcfXSyTLNKnhrqRsz2MVibXXjmAva0Oc1V32hDjIXxQp3k1OXhg/640?wx_fmt=gif&from=appmsg)

在 Pwn2Own 大赛中，参赛人员因发现QNAP 产品 exp 而获得数万美元的奖励，其中一个exp甚至获得10万美元的奖励，不过它涉及的不仅仅是 QNAP 公司的产品，还包括TrueNAS 设备中的漏洞。

QNAP 公司本次修复的最严重漏洞是CVE-2024-50393（CVSS评分8.7），它是一个命令注入漏洞，可导致远程攻击者在易受攻击设备上执行任意命令。CVE-2024-48868（CVSS评分8.7）是一个回车和换行 (CRLF) 注入漏洞，可被用于修改应用数据。该CRLF 特殊元素被嵌入到代码中如HTTP标头作为结束标记。

QNAP 还修复了QTS 5.1.9.2954 build 20241120、QTS 5.2.2.2950 build 20241114、QuTS Hero h5.1.9.2954 build 20241120 和 QuTS Hero h5.2.2.2952 build 20241116中的多个漏洞。

这次更新还修复了一个证书验证不当漏洞CVE-2024-48865（CVSS评分7.3），可导致本地网络攻击者攻陷系统的安全性。另外，更新还修复了多个中危的认证不当和 CRLF 注入缺陷，以及低危的 Hex 编码和外部控制的格式化字符串漏洞。

QNAP还修复了位于 License Center 中的一个高危漏洞CVE-2024-48863（CVSS评分7.7），可导致远程攻击者运行任意命令。这些补丁已包含在 QNAP License Center 1.9.43 版本。用户需以管理员身份登录到QTS货QuTS Hero，打开应用程序中心，搜索找到 License Center，点击更新按钮。

QNAP 还宣布发布 Qsync Central 版本 4.4.0.16\_20240819 (2024/08/19)，修复了一个“可导致拥有用户访问权限的攻击者，将文件系统遍历到非预期位置。”

虽然QNAP公司并未提到这些漏洞是否已遭在野利用，但鉴于其设备经常遭攻击，因此用户应尽快更新实例。更多信息可访问QNAP公司的安全公告页面。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Pwn2Own 2024爱尔兰黑客大赛落下帷幕 Master of Pwn 诞生](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521303&idx=1&sn=741af621329dcd54f31bdaa6d93a7347&scene=21#wechat_redirect)

[2025 Pwn2Own东京汽车大赛公布目标和奖金](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520932&idx=1&sn=92b8d0945843bbf9725d8256c2c2fd46&scene=21#wechat_redirect)

[谷歌修复 Pwn2Own 2024大赛发现的两个 Chrome 0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519170&idx=1&sn=31612ff9461ff59184a818b76f04c198&scene=21#wechat_redirect)

[Mozilla 修复Pwn2Own大赛发现的两个 Firefox 0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519154&idx=1&sn=3f4209efe9a510274abec479b51dcceb&scene=21#wechat_redirect)

[Pwn2Own 2024温哥华大赛落幕  Master of Pwn 诞生](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519143&idx=1&sn=aa2842286dc5aa1063e21f010ec15ad1&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/qnap-patches-vulnerabilities-exploited-at-pwn2own/

题图：Pixabay License

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