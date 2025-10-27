---
title: D-Link 不打算修复 DIR-846W 路由器中的这四个RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520668&idx=1&sn=33ddf9ab82fd7db2d5c560e478add189&chksm=ea94a0f6dde329e00b344533f754d89385c211e8596d9ad29addaf0ee37d57d5ea6a58459475&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-05
fetch_date: 2025-10-06T18:26:58.353802
---

# D-Link 不打算修复 DIR-846W 路由器中的这四个RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQFiaibvHLibibPhJbHJslBahJyNnUHn9VhkhIAexeUXtNeqBYgZcBicZDnbVNqwDMcKpto3jEvpLL0GiaQ/0?wx_fmt=jpeg)

# D-Link 不打算修复 DIR-846W 路由器中的这四个RCE漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**D-Link 提醒称，DIR-846W 路由器的所有硬件和固件版本均受四个远程代码执行 (RCE) 漏洞影响，不过由于该产品已达生命周期，因此不予修复。**

这四个RCE漏洞中，其中三个是“严重”级别，无需认证，由安全研究员 yali-1002发现，后者在GitHub 仓库中发布了最少详情。这名研究员在2024年8月27日公布了该信息，不过目前并未发布PoC 利用。

这些漏洞概述如下：

* CVE-2024-41622：通过 /HNAP1/ 接口中的 tomography\_ping\_address 参数触发的远程命令执行 (RCE) 漏洞（CVSSv3评分9.8，“严重”级别）。
* CVE-2024-44340：通过 SetSmartQoSSettings 中 smartqos\_express\_devices 和 smartqos\_normal\_devices 触发的RCE漏洞（因访问需认证，因此CVSSv3 评分将至8.8，“高危”级别）。
* CVE-2024-44341：通过 lan(o)\_dhcps\_staticlist 参数触发的RCE漏洞，可通过构造的 POST 请求利用（CVSSv3评分9.8，“严重”级别）。
* CVE-2024-44342：通过 wl(o).(o)\_ssid 参数触发的RCE漏洞（CVSS v3评分9.8，“严重”级别）。

尽管D-Link 公司证实了这些安全问题及其等级，但表示设备已达生命周期，意即不再发布安全更新。该公司提到，“按照通用策略，如果产品已达标准的生命周期/支持结束，则不再受支持，这些产品的所有固件开发都会停止。D-Link 强烈建议停用该产品并注意后续使用该产品可能会对连接设备带来风险。”

值得注意的是，DIR-846W 路由器主要销往美国以外的地区，因此该漏洞对于美国而言影响很小，但对于全球而言仍然严重。该机型仍然在某些市场出售，如拉美地区。

尽管 DIR-846 已在2020年支持终止，但很多人只有遇到硬件问题或实际限制时才会考虑替换路由器，因此仍然有很多人在使用这些设备。

D-Link 公司建议仍然使用DIR-846的用户立即停用并替换为最新受支持的机型。如无法这样做，则应确保设备运行最新固件版本，为 web 管理门户使用强密码并启用WiFi加密。

D-Link 漏洞通常遭恶意软件僵尸网络利用，如 Mirai 和 Moobot 以发动 DDoS 攻击。威胁行动者最近利用 D-Link DIR-859 路由器漏洞窃取密码并攻陷设备。因此在PoC 利用发布和被滥用于攻击之前保护设备安全至关重要。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[D-Link 修复D-Link D-View 8软件中的认证绕过和 RCE 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516588&idx=1&sn=981ba7ac004cc1b05279618b3be57e1f&chksm=ea94b0c6dde339d00da0ef0e86a316035b22c4f86ccc177e5420b43bcffb6d47b13200edab35&scene=21#wechat_redirect)

[D-Link 修复多个硬编码密码漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506450&idx=3&sn=e93472d0452c2f5615ef9f11c0f4cb71&chksm=ea94eb78dde3626e9370f9fdd70b4dc576638d8253da74e5bd0a3e1371cf537b4869f1577713&scene=21#wechat_redirect)

[D-Link 修复VPN路由器中的多个远程命令注入漏洞，还有一个未修复](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247498584&idx=6&sn=ae761df7a81ed6965f4a2dcde6755e2e&chksm=ea94ca32dde34324055e8c5d633658bc3a97ad1c2ca770d0cd2d85b8c0ddc932b97aa69691d3&scene=21#wechat_redirect)

[D-Link 不止暴露固件镜像密钥，还被曝5个严重0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247494275&idx=1&sn=4ef4e6ac706709f704551718f80bba03&chksm=ea94dbe9dde352ffc1eb0a4c086a5df64ad6ed267624f2319095a0ccbd95b45f081397abad92&scene=21#wechat_redirect)

[D-Link 老款路由器被曝多个高危漏洞，未完全修复](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493529&idx=1&sn=cfc7d888829b44a3984d2fae72f8a8c0&chksm=ea94d6f3dde35fe5f802376b058dc9a8132607f531c9741e44d25973e36c2370a69c0eac42d9&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/d-link-says-it-is-not-fixing-four-rce-flaws-in-dir-846w-routers/

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