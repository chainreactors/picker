---
title: SolarWinds 修复 Web Help Desk 中的硬编码凭据漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520566&idx=2&sn=2201f2665ef471e47e5dc87762920af5&chksm=ea94a05cdde3294a691fb126918df1c46abe77fac1ddc817f2deafa7344a6764133a7ef02167&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-24
fetch_date: 2025-10-06T18:05:11.013566
---

# SolarWinds 修复 Web Help Desk 中的硬编码凭据漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS1elmCicrrYpBic6THusP5OKmL6mytk0B1G95VuOeCUj57tzZKQ1qVZkAExJicvia9JJ8qhqiamZN6JDg/0?wx_fmt=jpeg)

# SolarWinds 修复 Web Help Desk 中的硬编码凭据漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**SolarWinds 为一个严重的 Web Help Desk 漏洞发布热修复方案。该漏洞可导致攻击者使用硬编码凭据登录到未修复系统中。**

Web Help Desk (WHD) 是一款IT帮助桌面软件，广泛用于政府机构、大型企业以及医疗和教育组织机构，用于自动化和梳理帮助桌面管理任务。SolarWinds 公司的IT管理产品用于全球30多万个客户。

SolarWinds 公司在本周三修复的漏洞 (CVE-2024-28987)如遭成功利用，可导致未认证攻击者访问内部功能并修改目标设备上的数据。该漏洞由 Horizon3.ai 公司的漏洞研究员 Zach Hanley 发现并报送。

SolarWinds 公司尚未在 Trust Center 发布关于该漏洞的安全公告，且在 Web Help Desk 12.8.3 Hotfix 2发布前并未披露该漏洞是否已遭在野利用。该公司详述了如何安装并删除该修复方案的指南，提醒管理员将易受攻击服务器升级至 Web Help Desk 12.8.3.1813或12.8.3 HF1之前，然后再部署本周发布的热修复方案。它还建立在热修复方案安装过程中将所有原始文件进行备份，避免因热修复方案失败或未正确应用而发生的潜在问题。

**已遭利用的 WHD RCE漏洞**

另外，SolarWinds公司还修复了另外一个严重的 WHD 漏洞 CVE-2024-28986。该漏洞是RCE漏洞，已在一周前被纳入CISA的必修清单。CISA要求联邦机构在9月5日前修复网络中的所有WHD服务器，“这种类型的漏洞是恶意网络攻击者的常见攻击向量，为联邦企业带来严重风险。”

今年2月和7月，SolarWinds 公司修复了位于 Access Rights Manager (ARM) 软件中的13个RCE漏洞。6月，网络安全公司 GreyNoise 提醒称威胁行动者在 SolarWinds 公司发布热修复方案后不久，就开始利用 SolarWinds ServU遍历漏洞。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[SolarWinds Web Help Desk是 0day时或已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520517&idx=1&sn=33f6242a7bd079eb73527d2099be7fc1&chksm=ea94a06fdde32979ffcecb68d48201afaf85aec654453d14925cdb1395b63cafb1e96dd2dc2a&scene=21#wechat_redirect)

[SolarWinds 修复访问权限审计软件中的8个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520104&idx=1&sn=b5831c292df944c1998d2c0e89a80188&chksm=ea94be02dde3371465b0ad96095c0a03d607581b57af9afb87fd5ef76bdc9b79312b0f3468c7&scene=21#wechat_redirect)

[SolarWinds 访问审计解决方案中存在严重的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517960&idx=2&sn=859ca4a50e7e9df4867d1973b7bba390&chksm=ea94b662dde33f74e25d02181f9fc202ee23b91008de4d26acf0d79bd3e0385d608d23bb1245&scene=21#wechat_redirect)

[SolarWinds 平台修复两个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516335&idx=2&sn=7714c02477242110c20958d13327c558&chksm=ea94b1c5dde338d3aea7cd488e25f4d59825e633deebe43bb64963f20d6336a81cf4016641f1&scene=21#wechat_redirect)

[SolarWinds 称将在2月底修复多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515647&idx=3&sn=e5d9ae1f0396aaa5c5eb758484fb760b&chksm=ea948c95dde3058339a2b4d43a851fdc2441afec55b15919595ce8d9f6b98ea46b38a0e06ae3&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/solarwinds-fixes-hardcoded-credentials-flaw-in-web-help-desk/

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