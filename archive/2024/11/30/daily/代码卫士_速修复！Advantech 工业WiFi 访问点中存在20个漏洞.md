---
title: 速修复！Advantech 工业WiFi 访问点中存在20个漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521633&idx=1&sn=479bf08551e7f1c208c83e877ab89f34&chksm=ea94a40bdde32d1dc2416c640578e2c28536a8d53f4823815adc4ea55ee71c00617606ac3885&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-30
fetch_date: 2025-10-06T19:16:10.839661
---

# 速修复！Advantech 工业WiFi 访问点中存在20个漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQa4MsEI45FdIyWg7I4dPiczcxJ5fVnqib5k4fNpmVnic4eSdxC6FQrJdKgjhUlibsLjUFfUfHfd5TZ9w/0?wx_fmt=jpeg)

# 速修复！Advantech 工业WiFi 访问点中存在20个漏洞

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Advantech EKI 工业级无线访问点设备中存在20个漏洞，可被攻击者通过提升后的权限绕过认证并执行代码。**

上周三，网络安全公司 Nozomi Networks 在一篇文章分析中提到，“这些漏洞带来严重风险，可导致攻击者以 root 权限在未认证的情况下实现远程代码执行，从而完全攻陷受影响设备的机密性、完整性和可用性。”

收到负责任的披露后，该公司已在如下固件版本中修复这些漏洞：

* 1.6.5 （适用于EKI-6333AC-2G and EKI-6333AC-2GD）
* 1.2.2（适用于EKI-6333AC-1GPO）

在这20个漏洞中，6个是严重级别，可导致攻击者通过植入后门的方式获得对内部资源的持久访问权限，触发拒绝服务条件，甚至将受感染端点重构为 Linux 工作站，以实现横向移动以及进一步的网络渗透。

在这6个严重漏洞中，5个（编号从CVE-2024-50370到CVE-2024-50374，CVSS评分9.8）与对操作系统命令中所使用的特殊元素中和不当有关，而CVE-2024-50375（CVSS评分9.8）与对关键函数的认证缺失有关。

值得注意的还包括XSS漏洞CVE-2024-50376（CVSS评分7.3），它可与CVE-2024-50359（CVSS评分7.2）组合利用，造成OS命令注入后果，无需认证即可实现任意代码执行。不过要成功实施攻击，外部恶意用户必须物理接近 Advantech 访问点并播报恶意访问点。

当管理员访问 web 应用中的 “WiFi Analyzer” 部分时才会触发该攻击，导致该页面自动嵌入通过由攻击者播报的信号框架的信息，而无需进行安全检查。研究人员提到，“攻击者可通过该恶意访问点播报的此类信息之一是SSID。攻击者可将 JavaScript payload 作为其恶意访问点的SSID插入，并利用CVE-2024-50376在web应用中触发 XSS漏洞。”

如此，攻击者就会在受害者的web浏览器上下文中执行任意 JavaScript 代码，之后结合使用CVE-2024-50359以root权限在OS级别实现命令注入。这可通过向威胁行动者提供持久远程访问的反向shell 实施。研究人员提到，“这将使攻击者获得对受陷设备的远程控制，执行命令，并进一步渗透网络，提取数据或部署其它恶意脚本。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[D-Link 决定不修复这个严重漏洞，影响6万多台 NAS 设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521440&idx=2&sn=1ddad70ced916d3fad493805c8d04d62&scene=21#wechat_redirect)

[Synology：速修复零点击RCE漏洞，影响数百万 NAS 设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521406&idx=2&sn=1a37afaf7e8cd1893b64cc0183aae730&scene=21#wechat_redirect)

[0.0.0.0 Day漏洞已存在18年，影响 MacOS和Linux设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520401&idx=1&sn=fcb5f892311d2858672c9908d0e08554&scene=21#wechat_redirect)

[大规模SMS窃取器活动感染113个国家的安卓设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520274&idx=2&sn=f33c51567cc245083a3bc121e2a4c968&scene=21#wechat_redirect)

[数百万设备易受 “PKFail” 安全启动绕过问题影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520274&idx=1&sn=5cfd7e9114bc219b747a5f41013cd669&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/11/over-two-dozen-flaws-identified-in.html

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