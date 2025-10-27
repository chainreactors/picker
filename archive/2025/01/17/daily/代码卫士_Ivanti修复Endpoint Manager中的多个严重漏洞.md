---
title: Ivanti修复Endpoint Manager中的多个严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522089&idx=1&sn=a04239b89ce2032e8e28b49d05782135&chksm=ea94a643dde32f55fd65e0ec66115b17b1cfe6c18f35bb55ece3c45dfce09c46bdf368f9009f&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-17
fetch_date: 2025-10-06T20:11:10.036589
---

# Ivanti修复Endpoint Manager中的多个严重漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTa8k8JniczoDc9uia6bqsVnKzmC9uVA8Qiczk3efVWCAb9D131Q5eFxibbnBP4icvHPZ5f72ZW2Evw88A/0?wx_fmt=jpeg)

# Ivanti修复Endpoint Manager中的多个严重漏洞

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Ivanti 公司已发布安全更新，修复了影响 Avalanche、Application Control Engine和Endpoint Manager (EPM) 中的多个漏洞，其中的四个严重漏洞可导致信息泄露。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTa8k8JniczoDc9uia6bqsVnKoGkaOmD6gSkicia2MdIQQoNm5Mmzkpn9wBmlQBKQDufNZicGC4gZ6V51Q/640?wx_fmt=gif&from=appmsg)

这四个严重漏洞的CVSS评分均为9.8分，位于EPM中，与绝对路径遍历漏洞相关，可导致远程未认证攻击者泄露敏感信息。它们是CVE-2024-10811、CVE-2024-13161、CVE-2024-13160和CVE-2024-13159。

这些漏洞影响EPM 2024年11月安全更新版本以及之前版本，以及2022 SU6 11月安全更新及之前版本。这些漏洞已在EPM 2024年1月—2025年安全更新和EPM 2022 SU6年1月—2025年安全更新中修复。这些漏洞由Horizon3.ai 公司的安全研究员 Zach Hanley发现并报送。

此外，Ivanti 公司还修复了位于Avalanche 6.4.7之前及Application Control Engine 10.14.4.0之前版本中的多个高危漏洞，它们可导致攻击者绕过认证、泄露敏感信息并绕过应用拦截功能。该公司表示并未看到这些漏洞遭在野利用的整局，已增强其内部扫描和测试程序，及时标记并修复安全漏洞。

此前不久，SAP修复了位于NetWeaver ABAP Server和ABAP Platform 中的两个漏洞CVE-2025-0070和CVE-2025-0066（CVSS评分9.9），它们可导致认证攻击者利用认证检查不当漏洞提升权限并利用弱访问控制来访问受限制的信息。SAP在2025年1月的安全通告中提到，“SAP强烈建议客户访问支持门户，优先应用补丁，保护SAP态势安全。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Ivanti提醒注意 Connect Secure 产品中的新0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522025&idx=2&sn=f67e98879ae334210339981b77e939e9&scene=21#wechat_redirect)

[Ivanti：注意这个CVSS 满分的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521758&idx=1&sn=d87a2de8e47def08cf6aca1b91b6e064&scene=21#wechat_redirect)

[Ivanti 中的3个0day已遭活跃利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521006&idx=2&sn=9a5993bb8ee14a8ab3071f40bb56c909&scene=21#wechat_redirect)

[CISA：这个严重的 Ivanti vTM 漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520913&idx=2&sn=2148647cf20c87cf57d601cf283f4805&scene=21#wechat_redirect)

[CISA 和 Ivanti：Cloud Services Appliance 高危漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520811&idx=1&sn=890fffef04e0244ca4a0fe359dfb3886&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2025/01/researcher-uncovers-critical-flaws-in.html

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