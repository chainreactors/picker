---
title: 谷歌在三星Exynos 芯片集中发现18个0day漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515956&idx=1&sn=01fe340192b1659e658210ae4b02ac97&chksm=ea948e5edde30748775821e1c9ed1b389b2c0dd119e01cd78b9292d859542e3f209300000e4c&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-18
fetch_date: 2025-10-04T09:58:07.739345
---

# 谷歌在三星Exynos 芯片集中发现18个0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRcRU8IrlP0zb5vLhqzT4Iw20Wh8OiaiawFMADfUN0KWL0IbcQ5hLakpx8eoQJcR6m3tQZtU4wgrCbw/0?wx_fmt=jpeg)

# 谷歌在三星Exynos 芯片集中发现18个0day漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**谷歌零日项目组从三星的Exynos芯片集中发现并报告了18个0day漏洞，这些芯片集用于移动设备、可穿戴设备和车辆中。**

这些漏洞由安全研究员在2022年年末至2023年年初期间发现。其中4个漏洞最为严重，可导致从Internet到基带的远程代码执行后果。这些RCE漏洞（包括CVE-2023-24033和其它3个尚未获得编号的漏洞）可导致攻击者在无需用户交互的情况下远程攻陷易受攻击的设备。

三星在说明CVE-2023-24033的安全公告中指出，“该基带软件并未正确检查SDP制定的accept-type属性的格式类型，从而导致在三星基带调制解调器中实现拒绝服务或代码执行后果。”攻击者触发漏洞所需的唯一信息是受害者的电话号码。更糟糕的是，稍微做一些研究，有经验的攻击者就能轻松创建一个exploit，在无需出发目标注意力的前提下攻陷易受攻击的设备。

谷歌零日项目组的负责人Tim Willis提到，“鉴于这些漏洞提供的访问权限和可靠操作exploit可构造的速度的稀有性，我们决定延迟4个可导致从Internet到基带的远程代码执行后果的漏洞。”

余下的14个漏洞（包括CVE-2023-24072、CVE-2023-24073、CVE-2023-24074、CVE-2023-24075、CVE-2023-24076和其它9个未分配编号的漏洞）虽然没有上述4个漏洞严重，但仍然可带来风险。成功利用这些漏洞要求本地访问权限或恶意的移动网络运营商。

从三星提供的受影响芯片集来看，受影响设备包括但可能不仅限于：

* 三星移动设备，包括S22、M33、M13、M12、A71、A53、A33、A21、A13、A12和A04系列。

* 谷歌Pixel 6和Pixel 7系列。
* 使用Exynos W920芯片集的任何可穿戴设备。
* 使用Exynos Auto T5123芯片集的任何车辆。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRcRU8IrlP0zb5vLhqzT4IwvZp6qHzlNVSbhgFFGswBVKReL4ahibYCuhH8Bv5M9Q2NlMGibNIHuwoQ/640?wx_fmt=png)

**应变措施**

虽然三星已向其它厂商提供影响芯片集的漏洞安全更新，但补丁尚未公开，并非所有受影响用户均可应用这些补丁。

虽然每个制造商的设备补丁时间线各不相同，不过谷歌已在2023年三月安全更新中发布了受影响 Pixel 设备的CVE-2023-24033的解决方案。不过在补丁可用前，用户可禁用WiFi 呼叫和VoLTE删除共计向量，阻止针对三星Exynos芯片集的基带RCE利用尝试。

三星证实了零日项目组的应变措施，提到，“用户可禁用WiFi呼叫和VoLTE，缓解该漏洞的影响。我们建议终端用户尽快更新设备，确保运行修复了已披露和未披露漏洞的最新版本。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[GoAnywhere 0day的首个受害者出现，CHS百万病患数据受影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515565&idx=2&sn=9f977b20406d11d9326758abfe4b1f97&chksm=ea948cc7dde305d162e43621927aa59b464f20b3c58f53371e378ef894fd790591ce9b4115ce&scene=21#wechat_redirect)

[苹果紧急修复已遭利用的 WebKit 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515546&idx=1&sn=f9311f04f319e12385edbfcd698fa495&chksm=ea948cf0dde305e697564ae3c0b973831eece5c572326a20990546b6bacf3bef67450345d514&scene=21#wechat_redirect)

[苹果修复已遭利用的第10个0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515027&idx=1&sn=93ebe9404e1ead6aa5f784abf7fab31a&chksm=ea948af9dde303ef597a5e12dd8faab95e3127a6e8214fe9cdfba93dbcd4e59095001090e30f&scene=21#wechat_redirect)

[【BlackHat】利用多个0day将安全产品转变为擦除器](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514951&idx=1&sn=3ed4ef80c1329e08e7f64463d1fdad66&chksm=ea948a2ddde3033b5922485a64e1d6fca064810724e15a0778d8b0e791121dc63af1d8b8b1d3&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/google-finds-18-zero-day-vulnerabilities-in-samsung-exynos-chipsets/

题图：Pexels License

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