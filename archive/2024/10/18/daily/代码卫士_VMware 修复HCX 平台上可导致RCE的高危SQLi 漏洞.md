---
title: VMware 修复HCX 平台上可导致RCE的高危SQLi 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521136&idx=2&sn=092bf2813ecefa63156a83b9d8eab160&chksm=ea94a21adde32b0c330f235f9beca98c24ce44fcacdb92e916ec286a71acd272b5c86b1d517b&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-18
fetch_date: 2025-10-06T18:52:35.526646
---

# VMware 修复HCX 平台上可导致RCE的高危SQLi 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT5vPJMRj5EtTSQOBFdOQhMH8kLj5cJCicbD8rND9icSx2OlkFtMedQsCqia3gp16w0Q0quRbvz8bqVg/0?wx_fmt=jpeg)

# VMware 修复HCX 平台上可导致RCE的高危SQLi 漏洞

Ryan Naraine

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT5vPJMRj5EtTSQOBFdOQhMEPicRQegSshYO7bibQnVuNeDP9fOStNlv5f37icrlkxe983PvzyKw4KHA/640?wx_fmt=gif&from=appmsg)

**周三，VMware 督促面向企业的 HCX 应用移动平台用户修复一个严重的远程代码执行漏洞 (CVE-2024-38814)。**

该漏洞的CVSS评分为8.8，可导致具有非管理员权限的攻击者在 HCX 管理器上执行远程代码。VMware 发布安全公告提到，“具有非管理员权限的恶意认证用户能够输入特殊构造的SQL查询并在HCX管理器上执行越权远程代码执行漏洞。”

VMware HCX 是一款应用移动平台，旨在简化数据中心和云中的应用迁移、工作负载再均衡以及业务持续性业务。VMware 公司表示该漏洞影响多个 HCX 版本，包括4.8.x、4.9.x 和4.10.x。

VMware 公司已发布如何应用可用补丁的指南。SinSinology 公司的研究员 Sina Kheirkhah 通过ZDI漏洞奖励平台报送了该漏洞。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[博通修复 VMware vCenter Server 中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520848&idx=2&sn=d95814f9037c7711dfcb09cd0e590f0c&chksm=ea94a33adde32a2cc2d70ae1c9f784e58a1068b3439966be8fc0130d96ff48e1aae33021a835&scene=21#wechat_redirect)

[VMware 修复Fusion中的高危代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520668&idx=3&sn=899efb652a40601d77b2cb2fffa9e4a2&chksm=ea94a0f6dde329e0c294039de56f65cffda877a972c98fbfebe68abac81d4ee415d453a6203e&scene=21#wechat_redirect)

[VMware 修复多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519781&idx=1&sn=6951e2970725eafcd08fdb56f31e3df5&chksm=ea94bf4fdde3365926e476e57a166e8c5b13f60a4955215555a3a20948faf68e83c949a669da&scene=21#wechat_redirect)

[VMware 修复Workstation 和 Fusion 产品中的多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519506&idx=2&sn=15447e0bd14688896d0aac2ef6d85333&chksm=ea94bc78dde3356e2862d49586a76b04a8277c3e27ee0cbad93ba1906c685c4e45d848bd682a&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/vmware-patches-high-severity-sql-injection-flaw-in-hcx-platform/

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