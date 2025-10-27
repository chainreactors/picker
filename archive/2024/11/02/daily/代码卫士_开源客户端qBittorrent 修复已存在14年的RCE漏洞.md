---
title: 开源客户端qBittorrent 修复已存在14年的RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521357&idx=2&sn=dc9695c878770ba5390c627bc3e3681a&chksm=ea94a527dde32c31d351cd6dca491aa437fa8431c26df61f85217feb3f68a6a8070a59cfc195&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-02
fetch_date: 2025-10-06T19:17:38.406808
---

# 开源客户端qBittorrent 修复已存在14年的RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQZGhzRE4MsrALm3RE0JXrM6ffkV516utqicwul8GphjY7aKv221xkx9Nict0cMfGk7sicPT95f1NUtw/0?wx_fmt=jpeg)

# 开源客户端qBittorrent 修复已存在14年的RCE漏洞

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQZGhzRE4MsrALm3RE0JXrMnBc53DTf0q3FYf5KOlFLIibNnMPPVgJZsXKjfZQTnR3suLUnib5xicdibg/640?wx_fmt=gif&from=appmsg)

**qBittorrent 修复了该应用中负责管理下载的组件 DownloadManager 中因 SSL/TLS 验证失败引发的远程代码执行漏洞。该漏洞在2010年4月6日中的一个提交中引入，在14年之后的2024年10月8日的最新发布版本5.0.1中修复。**

qBittorrent 是一款免费的开源客户端，用于通过 BitTorrent 协议下载和共享文件。它因拥有跨平台性质、IP过滤、一体化搜索引擎、RSS投放支持和现代的基于 Qt 的接口而备受关注。

不过正如安全研究员 Sharp Security 在一篇博客文章中提到的那样，该团队修复了一个值得关注的漏洞，但并未分配CVE编号，未能以恰当的方式通知用户。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQZGhzRE4MsrALm3RE0JXrMXQsibqBUCDRLPjPMoT8mEFJpeV1YJXQhUcVP1zyLiaTHpnJI858iczI5A/640?wx_fmt=gif&from=appmsg)

**一个问题，多种风险**

问题的核心在于，自2010年起，qBittorrent 接受了任何证书如伪造/不合法证书，使得攻击者处于中间人未知，修改网络流量。

研究员提到，“在 qBittorrent 中，DownloadManager 类忽视了所有平台上发生过的所有 SSL 证书验证错误，自2010年4月6日的提交 9824d86起，已经持续了14年6个月。这一默认行为通过2024年10月12日的提交 3d9e971得到改变。第一次打补丁的发布是在2天前发布的5.0.1版本。”

SSL 证书通过验证服务器证书获得证书机构 (CA) 的验证和信任，确保用户以安全的方式连接到合法服务器。如果跳过这一验证步骤，则假装为合法的任何服务器均可拦截、修改或在数据流中插入数据，而 qBittorrent 将信任该数据。

Sharp Security 强调了该问题带来的四个主要风险：

（1）  如Windows系统无法使用 Python，则 qBittorrent 提示用户通过指向一份 Python 可执行文件的硬编码 URL 进行安装。由于缺少证书验证，拦截该请求的攻击者可以恶意 Python 安装器取代该 URL 的响应，从而执行 RCE。

（2）  qBittorrent 通过从硬编码 URL 中提取 XML 推送的方式检查更新，之后为新版本的下载链接解析推送。缺少SSL验证，攻击者可替换推送中的恶意更新，提示用户下载恶意 payload。

（3）  qBittorrent 的 DownloadManager 也用于 RSS 推送，导致攻击者可拦截和修改 RSS 推送内容并以安全种子连接的方式注入恶意 URL。

（4）  qBittorrent 从硬编码URL中自动下载被压缩的 GeoIP 数据库并解压，从而导致攻击者可通过从被欺骗服务器中提取的文件利用潜在的内存溢出。

该研究员提到，虽然一般而言中间人攻击发生的可能性较小，但在监控严重的区域来说更为常见。qBittorrent 5.0.1的最新版本已修复以上风险。建议用户尽快升级。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[研究员在开源AI和ML模型中发现30多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521331&idx=1&sn=e13cd9f9dccd9d17953e551df9108205&chksm=ea94a559dde32c4f32a18c5ad4c3a2fc98f17fb29f69f73cac5c613c67ae28f36ab473d14936&scene=21#wechat_redirect)

[Python、npm和开源生态系统中的入口点可用于发动供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521093&idx=1&sn=7723bd7496e2f4b228e3013dd21765b4&chksm=ea94a22fdde32b396a0c379623e7d047d6762947c21f033e10a0d1e0f8567a584c4d74c12e27&scene=21#wechat_redirect)

[NSA 的开源员工培训平台 SkillTree 中存在CSRF漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520038&idx=2&sn=921e2fe11a431d8a458188b65d0a3b9d&chksm=ea94be4cdde3375abbf6e79690d31fd0c1e2f7bdc02b738a8fc06afa426d4a95adedea7492d3&scene=21#wechat_redirect)

[存疑 CVE 漏洞带来无谓压力 热门开源项目开发者归档 GitHub 仓库](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519930&idx=2&sn=acd4b1226ac3021b5aa91433e3f657f5&chksm=ea94bfd0dde336c6a6ba483f21d5d9572e139fb0e5cd5ac1a9ccde95f91e2330823dfbc71c20&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/qbittorrent-fixes-flaw-exposing-users-to-mitm-attacks-for-14-years/

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