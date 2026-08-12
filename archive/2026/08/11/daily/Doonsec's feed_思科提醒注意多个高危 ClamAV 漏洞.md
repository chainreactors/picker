---
title: 思科提醒注意多个高危 ClamAV 漏洞
url: https://mp.weixin.qq.com/s/k5W2oAbDaAT7-7lAN89-xg
source: Doonsec's feed
date: 2026-08-11
fetch_date: 2026-08-12T03:59:40.276875
---

# 思科提醒注意多个高危 ClamAV 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfWQa2dppgaHD15iccajySEl8dJdWHtVDJm0A4Mepm4ufvP5uWt5HsibcqkPnFLAFLpS2Fltxy2mHwKJCBCiaTzlLoBickpqnO7UJic0/0?wx_fmt=jpeg)

# 思科提醒注意多个高危 ClamAV 漏洞

Sergiu Gatlan
Sergiu Gatlan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**思科提醒注意****Secure Endpoint Connector****中的两个高危漏洞，可用于拒绝服务（****DoS****）攻击，使****ClamAV****扫描进程崩溃。**

这两个漏洞（CVE-2026-20337和CVE-2026-20338）位于ClamAV（Clam AntiVirus）的ZIP压缩包解析器中。ClamAV是一款开源、跨平台的恶意软件文件扫描引擎。思科在上周五发布的安全公告中解释称，这两个漏洞分别由边界检查不当和内存处理不当引起，可被未经认证的远程攻击者利用。思科产品安全事件响应团队 (PSIRT) 表示，这两个漏洞的PoC利用代码已公开可获取，但表示目前尚无证据表明它们已被广泛利用。

思科提到，“攻击者可通过提交特殊构造的zip文件进行扫描来利用漏洞。成功利用可导致ClamAV扫描进程终止，从而使受影响软件出现拒绝服务条件。Cisco PSIRT已知悉，CVE-2026-20337和CVE-2026-20338中所述漏洞的 PoC 代码已公开可用。”

思科还指出，这些漏洞的安全影响仅对Windows平台为“高”，因为只有Windows平台“在特权安全上下文中运行ClamAV扫描进程”。这两个漏洞影响ClamAV 1.5.0至1.5.3版本，已在8月7日发布的1.5.4版本中得到修复。

虽然这两个漏洞暂无临时缓解措施，但思科计划于本月晚些时候发布软件更新，以修复受影响的Windows、Linux和Mac版Secure Endpoint Connector。

上周五，思科还修复了ClamAV的另外五个漏洞，它们同样可通过提交恶意的XAR、Mach-O、PDF、GPT和PESpin文件进行扫描而被利用，从而触发拒绝服务条件。思科曾在2025年1月修补了另一个带有PoC利用代码的ClamAV DoS漏洞，当时警告称攻击者可利用该漏洞终止ClamAV防病毒扫描程序，从而阻止或延迟后续扫描操作。

自2021年11月以来，美国网络安全与基础设施安全局（CISA）已将95个思科漏洞标记为已遭利用，其中6个被滥用于勒索软件攻击。

代码卫士试用地址：https://sast.qianxin.com/

开源卫士试用地址：https://oss.qianxin.com/

---

**推荐阅读**

[思科修复12个 SD-WAN 和 IOS XE 漏洞，含多个高危](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526840&idx=1&sn=d925710bf66e2f5889e993d29d7d276c&scene=21#wechat_redirect)

[思科修复已遭利用的 SD-WAN vManage 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526306&idx=1&sn=276b8774c724ae48ddfa09529366c4cd&scene=21#wechat_redirect)

[思科：Unified CM 严重漏洞的 PoC 已发布](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526228&idx=2&sn=cbc3a57a98b3117c33dc6847aa4c4e14&scene=21#wechat_redirect)

[思科：注意无补丁但已遭利用的 SD-WAN 高危 0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526228&idx=1&sn=aa8606b21d2d15f6de0e55d784eef216&scene=21#wechat_redirect)

[思科：速修复满分 Secure Workload 未授权 API 访问漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526078&idx=1&sn=2b669f642fd4b13d42c79cc8a544e482&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisco-warns-of-high-severity-clamav-flaws-with-public-exploits/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]()![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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