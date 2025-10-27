---
title: VMware 修复严重的Carbon Black App Control漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515674&idx=1&sn=a2545f99534c8c181bb5022bbc3989e1&chksm=ea948f70dde306661e8a7532ffad9fe411f3cd1cbcb74c5ae58c6e4f394d04247cb807e3ce08&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-02-23
fetch_date: 2025-10-04T07:51:41.817411
---

# VMware 修复严重的Carbon Black App Control漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTApbSMdKg73M9onzoWPcTv4B5bt8G000JjggNbhHvK8FuAWw9k4vlIRLEboJ0mJKSDlYL2MSrayQ/0?wx_fmt=jpeg)

# VMware 修复严重的Carbon Black App Control漏洞

Ryan Naraine

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**虚拟化技术巨头VMware 周二推出重要安全修复方案，修复了其面向企业的Carbon Black App Control 产品中的一个严重漏洞 (CVE-2023-20858)。**

VMware 公司提醒称，攻击者可利用注入exploit，获得对底层服务器操作系统的访问权限，“对App Control 管理员控制台具有特权权限的恶意人员，可能能够利用特殊构造的输入，访问底层服务器操作系统。”

CVE-2023-20858的CVSS 评分为9.1分，影响在微软Windows 操作系统上运行的App Control 版本8.7.x、8.8.x 和8.9.x。据悉，该漏洞由研究员Jari Jääskelä 通过HackerOne 漏洞奖励平台报送。

VMware Carbon Black App Control 是一款由企业防御人员使用的安全产品，目的是确保只有受信任和获得批准的软件才能在关键系统和端点上执行。

VMware 公司还发布了关于重要级别漏洞的安全公告，说明位于vRealize Orchestrator 产品中的一个提权漏洞和信息泄露漏洞。公告指出，“恶意人员如拥有对vRealize Orchestrator 的非管理员访问权限，则能够使用特殊构造的输入绕过XML解析限制，访问敏感信息或可能提升权限。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[VMware Workstation中存在高危的提权漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515478&idx=3&sn=6fb6defbf6e53fa69b775f37bed7bbfd&chksm=ea948c3cdde3052a630422bf457d44f24d36236b6ca666929b3ab6ce6cf3774fc646a1dde7ca&scene=21#wechat_redirect)

[VMware 修复严重的ESXi和vRealize 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515027&idx=2&sn=d86995b203eb6824e5179dc7d57b8bce&chksm=ea948af9dde303ef8f28410ce0027472253b95bbd9447f1a2c538a07bda78c61567e5252f1e7&scene=21#wechat_redirect)

[VMware：速修复这三个严重的 Workspace ONE Assist 软件漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514441&idx=2&sn=a6a4722590de8e046966eacff21ccc02&chksm=ea948823dde301350f7cab83e012dd91120da7da9ed74b0e8ad2b487f5358c0361971fe016a4&scene=21#wechat_redirect)

[VMware修复 Cloud Foundation 中严重的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514329&idx=2&sn=320754664bbfb1ae127935003f156e17&chksm=ea9489b3dde300a537dc099256a73b6bcdaef1042e63e800592971b520edea0440b6fe35db22&scene=21#wechat_redirect)

[这个VMware vCenter Server漏洞去年就已发现，至今仍未修复](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514181&idx=2&sn=50c62919f4f010b5579d19ba752c7ba5&chksm=ea94892fdde30039043be2fb51e549c347507a0846cf9ad231e6e720f7794502b4dc46dd319c&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/apple-updates-advisories-as-security-firm-discloses-new-class-of-vulnerabilities/

题图：网络

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