---
title: 高通修复已遭利用的高危0day漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520994&idx=2&sn=ef89231ad1b43e2679e43b82ddb620f4&chksm=ea94a388dde32a9eaaa26c00774eea9eacc851b7bfac4dd8327e24dbc59a2ed40d011b782248&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-09
fetch_date: 2025-10-06T18:54:09.922671
---

# 高通修复已遭利用的高危0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS7euItcwX5GeUyNmUywibIIOVZdpGCgueryz3icQpATftX0X9BORUCEz5dV1gYfIOpAGJHjNOB3wZg/0?wx_fmt=jpeg)

# 高通修复已遭利用的高危0day漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**高通修复了位于 Digital Signal Processor (DSP) 服务中的一个高危 0day 漏洞 (CVE-2024-43047)，它影响数十个芯片集。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS7euItcwX5GeUyNmUywibIImEcU8BbMwicmibzYs1w5BIRsiaY06tIdwd2AkOFjUm4gaQiaVkDuzuATibw/640?wx_fmt=png&from=appmsg)

该漏洞由谷歌 Project Zero 团队的研究员 Seth Jenkins 和 Amnesty International Security Lab 公司的研究员 Conghui Wang 报送，是由一个释放后使用弱点引发的，如遭具有低权限的本地攻击者成功利用，可导致内存损坏。正如在一条 DSP 内核提交中解释的那样，“目前，DSP通过未使用的 DMA 句柄fds 更新了头缓冲区。在 put\_args 不分，如果头缓冲区中出现了 DMA 句柄 FDs，则相应的映射会被释放。然而，由于该头缓冲区被暴露到未签名的 PD，用户可更新不合法的 FDs。如果该不合法的 FD 匹配已在使用状态中的任何 FD，就可导致释放后使用漏洞。”

高通在本周一发布的安全公告中提醒称，该漏洞已被谷歌威胁分析团队和Amnesty International Security Lab标记为在野遭利用状态，而这两家机构均以发现被用于高价值个体移动设备遭间谍软件攻击中的0day而出名。高通提醒称，“谷歌威胁分析团队提到CVE-2024-43047可能遭范围有限的针对性利用攻击。影响 FASTRPC 驱动的漏洞补丁已发给OEM，并强烈建议他们尽快在受影响设备上部署更新。”

高通也督促用户联系设备制造商，获取关于特定设备补丁状态的更多详情。

此外，高通刚还修复了另外一个接近满分的位于WLAN资源管理器中的漏洞 (CVE-2024-33066)。该漏洞是在一年多前报送的，由可导致内存损坏的一个输入验证不当弱点引发。去年10月份，高通还提醒称，攻击者正在利用其 GPU 和 Compute DSP 驱动中的三个 0day 漏洞。谷歌威胁分析团队和 Project Zero 团队发布报告称，漏洞被用于范围有限的针对性利用活动中。谷歌和高通尚未发布更多详情。

近年来，高通还修复了多个芯片级漏洞，它们可导致攻击者访问用户的媒体文件、文本消息、通话历史和实时会话。

高通还修复了位于 Snapdragon Digital Signal Processor (DSP) 芯片中的多个漏洞，它们可导致黑客在无需用户交互的情况下控制智能手机，监控用户并创建可躲避检测的不可删除的恶意软件。高通在2020年修复的漏洞 KrØØk 可导致攻击者解密一些通过 WPA2 加密的无线网络，而另外一个现已修复的漏洞可导致攻击者访问重要数据。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[全球约30%的智能手机受高通新漏洞影响，打补丁状况不明](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247504006&idx=2&sn=5e3be0f6a913cde1548583ff6f77c3d2&chksm=ea94e1ecdde368faafea7d5c9e878dd3938c91343788cb8e7241a4c977e403ccdec05f49808e&scene=21#wechat_redirect)

[近一半的智能手机受高通 Snapdragon 漏洞影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247494521&idx=4&sn=fa7888169d1be68fd1af317a39f14f42&chksm=ea94da13dde3530515bd331d0b42a2b370cacc439eee2df4c73aa723bfa7cb256f1d8a876c36&scene=21#wechat_redirect)

[重大漏洞导致高通 QSEE 组件瘫痪，所有安卓和 IoT 设备可遭完全控制](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489812&idx=1&sn=846cfa78416c05d49fee4b37e9dd1348&chksm=ea97287edde0a1684fe7b646a9cce89264f79d0ec7c166c061a2b3d91cb8a298d5a3713157fa&scene=21#wechat_redirect)

[博通高通收购尚未达成 美国政府国安调查先行但意在中国？](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247486615&idx=2&sn=9b621111b19ab7d137cb964307dd8b34&chksm=ea973dfddde0b4ebd4f0e695d49573d4dfcc3183770fb4241dc4e61520bcf0f0a788e9b630d9&scene=21#wechat_redirect)

[高通移动芯片存在漏洞，安卓手机位置服务受影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485625&idx=1&sn=3615e2c2e400413269698fec4dcc63b9&chksm=ea9739d3dde0b0c5d6f452d0f2df6d233225e8c9d14d1a401434990979e45795d98748eee4cd&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/qualcomm-patches-high-severity-zero-day-exploited-in-attacks/

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