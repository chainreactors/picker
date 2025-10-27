---
title: SolarWinds 修复访问权限审计软件中的8个严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520104&idx=1&sn=b5831c292df944c1998d2c0e89a80188&chksm=ea94be02dde3371465b0ad96095c0a03d607581b57af9afb87fd5ef76bdc9b79312b0f3468c7&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-20
fetch_date: 2025-10-06T17:43:03.999978
---

# SolarWinds 修复访问权限审计软件中的8个严重漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSBCsNOVb5OACT0e8ico896E8Yz2uyXSsiao9enlrTzhqGwy5yA9Rc4cXh8hcf1kgPenk4tXIKcEWeg/0?wx_fmt=jpeg)

# SolarWinds 修复访问权限审计软件中的8个严重漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**SolarWinds 修复了位于访问权限管理器 (Access Rights Manager, ARM) 软件中的8个严重漏洞，其中6个可导致攻击者获得易受攻击设备上的远程代码执行 (RCE) 权限。**

ARM是企业环境中的一个重要工具，帮助管理员管理和审计所在组织机构IT基础设施中的访问权限，将威胁影响降到最低。这些RCE漏洞（CVE-2024-23469、CVE-2024-23466、CVE-2024-23467、CVE-2024-28074、CVE-2024-23471和CVE-2024-23470）的CVSS评分为9.6，可导致不具备权限的攻击者通过执行代码或命令的方式在未修复系统上执行操作，是否需要管理员权限取决于被利用漏洞的情况。

SolarWinds 公司还修复了两个严重的目录遍历漏洞（CVE-2024-23475和CVE-2024-23472），可导致未认证用户在访问限制性目录之外的文件或文件夹后，执行任意文件删除和获取敏感信息。它还修复了一个高危的认证绕过漏洞 (CVE-2024-23465)，可导致未认证的恶意人员获得活动目录环境中的域管理员权限。该公司还修复了 ARM 2024.3中的所有漏洞，并在本周三发布了漏洞和修复方案。

SolarWinds 公司并未说明这些漏洞的 PoC 是否已是在野状态以及是否已遭利用。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSBCsNOVb5OACT0e8ico896EyuQsa8YqDRg8emb2CD7CwcVUjBsa8TXRmxbId3d974QZjgDxuLAkzQ/640?wx_fmt=gif&from=appmsg)

**历史漏洞**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSBCsNOVb5OACT0e8ico896ED1o1iaia0PAFfQRzttKKq439PBc7k320sQRLgBbiaQT3sWLrOqicPPj1aQ/640?wx_fmt=gif&from=appmsg)

2月份，SolarWinds 还修复了ARM 解决方案中的5个其它RCE漏洞，其中3个可导致未认证利用后果，被评级为严重漏洞。

4年前，SolarWinds 的内部系统遭俄罗斯APT29黑客组织攻陷。APT29将恶意代码注入由客户在2020年3月至2020年6月期间下载的 Orion IT 管理员平台构建。

SolarWinds 公司的全球客户超过30万名，为96%的财富500强公司提供服务，包括高级别技术公司如苹果、谷歌和亚马逊以及政府组织机构如美国军队、五角大楼、国务院、NASA、NSA、邮政服务、NOAA、司法部以及美国总统办公室。然而，尽管俄罗斯国家黑客利用木马化更新在数千个系统中部署了 sunburst 后门，但后续利用仅针对数量更少的SolarWinds 客户。这起供应链攻击活动被披露后，多家美国政府机构证实其网络遭攻陷，包括美国国务院、国土安全部、财政部、能源部、国家电信和信息管理局 (NTIA)、美国国立卫生研究院和美国国家核安全管理局。

2021年4月，美国政府正式起诉俄罗斯对外情报局 (SVR) 协同参与2020年SolarWinds 攻击，而美国证券交易所 (SEC) 在2023年10月起诉 SolarWinds 未能在事件发生前通知网络安全防御投资者。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[SolarWinds 访问审计解决方案中存在严重的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517960&idx=2&sn=859ca4a50e7e9df4867d1973b7bba390&chksm=ea94b662dde33f74e25d02181f9fc202ee23b91008de4d26acf0d79bd3e0385d608d23bb1245&scene=21#wechat_redirect)

[SolarWinds 事件爆发前半年，美司法部就检测到但未重视](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516392&idx=1&sn=03805ab2d377a6823689c8e9df44946b&chksm=ea94b182dde33894b955bb4519df38c455bcbfff727ec9d3034f4272590e649e51f90426748a&scene=21#wechat_redirect)

[SolarWinds 平台修复两个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516335&idx=2&sn=7714c02477242110c20958d13327c558&chksm=ea94b1c5dde338d3aea7cd488e25f4d59825e633deebe43bb64963f20d6336a81cf4016641f1&scene=21#wechat_redirect)

[SolarWinds 公司：Web Help Desk 实例正遭攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510991&idx=4&sn=90944cad89a7c454178edd41a21c5652&chksm=ea949aa5dde313b3d6c2c7960809d44226a88ed78a7ae795f0ffd4835a5357e4d93d64e6012c&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/solarwinds-fixes-8-critical-bugs-in-access-rights-audit-software/

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