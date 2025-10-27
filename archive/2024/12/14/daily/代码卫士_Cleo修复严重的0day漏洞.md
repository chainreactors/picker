---
title: Cleo修复严重的0day漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521787&idx=2&sn=6bccdb74a809a4f90b14cdd90c9c2985&chksm=ea94a491dde32d878d12b484356d74f82ce50e72b41607967c69d46af23089404ac6bc4d5de1&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-14
fetch_date: 2025-10-06T19:41:15.934844
---

# Cleo修复严重的0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQqrq1zGdg88onVd6RY1iblcelrZj13sGRiaJFOc6lHD6u0I3Mfv6dGLmpdKbffY9M7yicsgAicrHS7SQ/0?wx_fmt=jpeg)

# Cleo修复严重的0day漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Cleo 发布安全更新，修复了位于 LexiCom、VLTransfer 和 Harmony 软件中的一个0day漏洞。该漏洞目前已被用于盗取数据。**

10月，Cleo 修复了位于其文件传输管理软件中的一个预认证远程代码执行漏洞（CVE-2024-50623），并建议“所有客户立即升级”。

Huntress 公司的安全研究员在12月3日率先发现了该针对完全打补丁的 Cleo 软件的攻击活动。12月8日，该攻击数量激增，原因是攻击者迅速发现了CVE-2024-50623的一个绕过（尚无CVE编号）可使他们通过利用默认 Autorun 文件夹设置的方式，导入并执行任意bash 或 PowerShell 命令。

网络安全专家 Kevin Beaumont 提到，该0day漏洞目前正遭Termite 勒索团伙的利用。而该团伙正是近期声称攻陷软件即服务 (SaaS) 提供商 Blue Yonder 的威胁组织。

Huntress 公司在本周一提醒称，“该漏洞正在遭在野活跃利用，运行5.8.0.21的完全打补丁的系统仍然可遭利用。我们强烈建议您在新补丁发布前，通过防火墙保护任何暴露到互联网的 Cleo 系统。”

从Shodan 搜索结果来看，全球共有421个暴露在互联网的Cleo 服务器，其中327台位于美国。Macnica 公司的威胁研究员 Yutaka Sejiyama 也发现可从网络访问743台Cleo 服务器（379台运行 Harmony 软件，124台运行 VLTrader 以及240台运行 LexiCom）。

**发布补丁，拦截恶意攻击**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQqrq1zGdg88onVd6RY1iblcmNRzNrtsUicgEFkHLUniaWGLJs7PnSicJficzRv53bNnXBQB5OEg424TbA/640?wx_fmt=gif&from=appmsg)

今天，Cleo 公司发布补丁以阻止正在进行的攻击活动，并督促客户尽快升级至5.8.0.24，保护暴露在互联网中的易受攻击的服务器。

该公司提到，“Cleo 强烈建议所有客户立即将 Harmony、VLTrader 和 LexiCom 的实例更新至最新发布版本5.8.0.24，修复其它的已发现的潜在攻击向量。应用补丁后，在启动阶段，任何与该exp相关的文件都会有出错日志，所有这些文件都会被删除。”Cleo 公司建议无法立即更新的客户在系统选项处禁用自动运行特性，并清空自动运行目录（虽然这样做无法阻止攻击但会减小攻击面）。

Rapid7 公司在调查时发现，威胁行动者利用该漏洞部署编码的 Java Archive (JAR) payload，而它是更大的基于Java的利用后框架的一部分。Huntress 公司也分析了该恶意软件（被命名为Malichus）指出，它仅被部署在Windows 设备上，不过它具有 Linux 系统支持能力。Binary Defense ARC Labs 报道称，恶意软件操纵者可利用Malichus 进行文件传输、命令执行以及网络通信。

截止目前，Huntress 公司发现至少有10家公司的 Cleo 服务器遭攻陷，并表示还存在其它潜在受害者。Sophos 公司也从50多个 Cleo 主机上发现了攻陷指标。Sophos 公司提到，“所有观测到的受影响客户都在北美地区拥有分支机构或在该地区运营，其中主要是美国。我们发现多数受影响客户是零售组织机构。”这些攻击与近年来利用MOVEit Transfer、GoAnywehre MFT 和 Accellion FTA中0day漏洞盗取数据的Clop组织的做法非常类似。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[俄罗斯黑客组织劫持巴基斯坦同行的服务器并发动攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521713&idx=2&sn=619bf5885501ae07ff311e92aefc9902&scene=21#wechat_redirect)

[僵尸网络利用 GeoVision 0day 安装 Mirai 恶意软件](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521513&idx=2&sn=667b6f9c61b6f2d2077659cd4d4cdc70&scene=21#wechat_redirect)

[英韩：Lazarus 黑客组织利用安全认证软件 0day 漏洞发动供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518225&idx=2&sn=0c496ddfdfec8c17e1344333f0c218f6&scene=21#wechat_redirect)

[Reddit替代品 Lemmy 开源软件遭 0day 利用攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517076&idx=2&sn=7062958ef499c9d253edf70f467f8bde&scene=21#wechat_redirect)

[GitHub 上的虚假0day PoC 推送 Windows 和 Linux 恶意软件](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516737&idx=2&sn=368349f3292248a0829924a329eab306&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cleo-patches-critical-zero-day-exploited-in-data-theft-attacks/

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