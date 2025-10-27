---
title: Fortinet：注意FortiWLM漏洞，黑客可获得管理员权限
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521859&idx=1&sn=6aade83438190800942638166b046757&chksm=ea94a729dde32e3fff2298ee3a0ab33be5cf7cc9bbfebb1e65bcf4b1a355e4369a3ae43bb957&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-21
fetch_date: 2025-10-06T19:38:32.187034
---

# Fortinet：注意FortiWLM漏洞，黑客可获得管理员权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQLAfaMWialedzBWHlEEC8arcEDelFmebJEvwKwDl0UGTsENK2nfbYpdic9RYYX4wwic83Fx0bbdfp6Q/0?wx_fmt=jpeg)

# Fortinet：注意FortiWLM漏洞，黑客可获得管理员权限

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Fortinet 披露了位于 Fortinet Wireless Manager（FortiWLM）中的一个严重漏洞CVE-2023-34990，可导致远程攻击者通过特殊构造的web请求执行越权代码或命令，从而控制设备。**

FortiWLM 是一款中心化管理工具，供政府机构、医疗组织机构、教育机构和大型企业用于监控、管理和优化无线网络。该漏洞是一个相对路径遍历漏洞，CVSS评分为9.8。

Horizon3 公司的研究员 Zach Hanley 发现并在2023年5月将漏洞报送给 Fortinet。然而，10个月之后该漏洞仍未被修复，于是Hanley 在2024年3月14日决定披露信息和PoC，另外还提到了自己从该厂商发现的其它漏洞。

**窃取管理员会话ID**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQLAfaMWialedzBWHlEEC8ar1fPYtXIficSXq8NKbSq94yoU55ibKTmCdrBQ6RkZRYqDiaIkEKaelmiajw/640?wx_fmt=gif&from=appmsg)

该漏洞可导致身份未认证的攻击者利用 “/ems/cgi-bin/ezrf\_lighttpd.cgi” 端点中的输入验证不当漏洞。

当 “op\_type” 设置为 “upgradelogs”，利用 “imagename” 参数中的目录遍历技术，攻击者可从该系统中读取敏感的日志文件。这些日志中通常包含管理员会话ID，可用于劫持管理员会话并获得提升后的权限，使攻击者接管设备。

Hanley 解释称，“攻击者通过滥用输入验证构建请求，而imagename 参数中包含一个路径遍历漏洞，从而使攻击者读取系统上的任何日志文件。FortiWLM 拥有非常详细的日志，记录着所有已认证用户的会话ID。利用上述任意日志文件读漏洞，攻击者可获取用户的会话ID并滥用已认证的端点。”该漏洞影响 FortiWLM 8.6.0至8.6.5以及8.5.0至8.5.4版本。

尽管研究员已发布公开提醒，但当时缺少CVE ID 以及安全通告说明用户并未意识到这一风险以及需要更新至安全版本。Fortinet 公司在昨天发布安全公告提到，2024年12月18日，CVE-2023-34990在 FortiWLM 8.6.6和8.5.5中修复，已在2023年9月发布。

CVE-2023-34990在大约四个月的时间里是0day状态，FortiWLM 用户直到10个月之后才从 Hanley 的 writeup 中发现该漏洞。然而，又过了9个月后，Fortinet 公司才发布安全通告。鉴于FortiWLM 部署在关键环境中的情况，它可能是攻击者的有价值目标，远程攻陷该漏洞可导致网络中断和敏感数据遭暴露。因此，强烈建议 FortiWLM 管理员及时应用所有可用的更新。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[黑客称窃取 440GB 文件，Fortinet 证实数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520799&idx=2&sn=d02acbabe690ef64658cea5df0e53131&scene=21#wechat_redirect)

[Fortinet 修复 FortiOS 中的代码执行漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519734&idx=2&sn=e2956d27d020b75520e84dc6e02b483a&scene=21#wechat_redirect)

[Fortinet 修复严重的 FortiClientLinux 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519274&idx=1&sn=0db6fdb46bf03ada98af3901110ee37b&scene=21#wechat_redirect)

[Fortinet 提醒注意端点管理软件中的严重RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519060&idx=1&sn=bd31e9a884e83396402ed8ca25c23ecd&scene=21#wechat_redirect)

[Fortinet 提醒注意严重的FortiSIEM命令注入漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518159&idx=1&sn=44370db9677abd274914bebd182e5446&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortiwlm-bug-giving-hackers-admin-privileges/

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