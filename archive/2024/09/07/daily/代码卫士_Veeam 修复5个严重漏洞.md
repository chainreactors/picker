---
title: Veeam 修复5个严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520714&idx=1&sn=df4e06a4fa7f19703c54eeb2ccf244d6&chksm=ea94a0a0dde329b6b9068782af2d2311165f4ac3aea68076c75da8cfa12aec8d17c556e6f0fc&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-07
fetch_date: 2025-10-06T18:28:26.739970
---

# Veeam 修复5个严重漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRZ9z4nZmPRJKEtGUFf6J7BjdkPURFbhafsxVGsB6LRR01BQr7IG3OhUhMnzcpOcuRx32aoZtHZNA/0?wx_fmt=jpeg)

# Veeam 修复5个严重漏洞

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Veeam 发布安全更新，修复了影响软件产品的18个缺陷，其中5个严重漏洞可导致远程代码执行后果。**

这5个漏洞如下：

* CVE-2024-40711 (CVSS: 9.8) ——该漏洞位于Veeam Backup & Replication中，可导致未认证远程代码执行后果。
* CVE-2024-42024 (CVSS: 9.1) ——该漏洞位于Veeam ONE中，可导致拥有 Agent 服务账户凭据的攻击者在底层机器上实施远程代码执行。
* CVE-2024-42019 (CVSS: 9.0) ——该漏洞位于 Veeam ONE中，可导致攻击者访问 Veeam Reporter Service 服务账户的 NTLM 哈希。
* CVE-2024-38650 (CVSS: 9.9) ——该漏洞位于 Veeam Service Provider Console (VPSC) 中，可导致低权限攻击者访问服务器上该服务账户的NTLM哈希。
* CVE-2024-39714 (CVSS: 9.9) ——该漏洞位于VPSC中，可导致低权限用户将任意文件上传至服务器，在服务器上实施远程代码执行。

另外，2024年9月更新还修复了13个其它高危缺陷，它们可导致权限提升、多因素认证绕过以及通过提权执行代码等。

所有漏洞已在如下版本中修复：

* Veeam Backup & Replication 12.2 (build 12.2.0.334)
* Veeam Agent for Linux 6.2 (build 6.2.0.101)
* Veeam ONE v12.2 (build 12.2.0.4093)
* Veeam Service Provider Console v8.1 (build 8.1.0.21377)
* Veeam Backup for Nutanix AHV Plug-In v12.6.0.632
* Veeam Backup for Oracle Linux Virtualization Manager 和 Red Hat Virtualization Plug-In v12.5.0.299

Veeam 软件漏洞可使用户成为威胁行动者传播勒索软件的有诱惑力的目标，建议用户尽快更新至最新版本以缓解潜在威胁。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Veeam：Backup Enterprise Manager 中存在严重的认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519550&idx=2&sn=6b4de50a6ef98b37be097aae6daafa64&chksm=ea94bc54dde33542e89c9b2f5b6a2105c6c926040276e43b5afbb6b233fffe948a2df38e1334&scene=21#wechat_redirect)

[Veeam 修复备份管理平台中的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519438&idx=1&sn=4e26daf80a580f4ffca69990e4991525&chksm=ea94bda4dde334b29ac40f6c2fcd5382d22e3657a099bbbac0a055d1af89efc833d6a9ee3449&scene=21#wechat_redirect)

[Veeam ONE 监控平台存在多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518080&idx=3&sn=186f168b319049fd88ec7557cb2458e1&chksm=ea94b6eadde33ffc3b7b219d6a0e6143f28a1c6c166c41882c63ee116d0acffba7acbed4dab3&scene=21#wechat_redirect)

[Veeam修复严重漏洞，可攻陷备份基础设施](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515885&idx=3&sn=ffefe13a8f5da2c680df756b9e641cfd&chksm=ea948f87dde30691fda5efbd07f068606a775eb6e6e596b39f44c7f1cd843a4c64a24c1a88a7&scene=21#wechat_redirect)

[Veeam 数据备份解决方案修复多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510935&idx=2&sn=16d2e8be99d29f0ceb82b7596b370911&chksm=ea949afddde313ebf772d24347c8ee4aa98f2e78b2da9850b34569457f918e386175b6d5b85a&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/09/veeam-releases-security-updates-to-fix.html

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