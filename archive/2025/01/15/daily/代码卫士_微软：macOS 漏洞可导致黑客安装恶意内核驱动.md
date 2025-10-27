---
title: 微软：macOS 漏洞可导致黑客安装恶意内核驱动
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522060&idx=1&sn=562313e7f413152c3399933007b147f5&chksm=ea94a666dde32f706b2b66b455dfbe3a9b106e8c0a4a379c3b30ac5c0aa916c5ad8b092cddd1&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-15
fetch_date: 2025-10-06T20:10:56.177656
---

# 微软：macOS 漏洞可导致黑客安装恶意内核驱动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRTIPXhgnNfFDpTOjlCZibEZlCaIUBGxpxlCX10E86Z7KsTQOic2etYKAxn1JpH1Q45KLyJbzkt8AdQ/0?wx_fmt=jpeg)

# 微软：macOS 漏洞可导致黑客安装恶意内核驱动

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**苹果公司最近修复了一个macOS 漏洞，可导致攻击者绕过系统完整性保护 (SIP) 措施并通过加载第三方内核扩展的方式安装恶意内核驱动。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRTIPXhgnNfFDpTOjlCZibEZuHvpYTpiaXnZftniaS2ibmKkG9iaBM5RU5oBMLuQxqibHS6CjkGEYlA1vkA/640?wx_fmt=gif&from=appmsg)

SIP 或 “rootless” 是macOS 的一个安全特性，可通过限制根用户账户在受保护区域的方式，阻止恶意软件修改特定文件夹和文件。SIP仅允许经过苹果签名的进程或具有特殊权限的进程如苹果软件更新，修改受macOS 保护的组件。正常情况下禁用SIP要求重启系统并从 macOS Recovery（内置恢复系统）进行引导，而这要求对受陷机器设备拥有物理访问权限。

该漏洞的编号为CVE-2024-44243，仅可由具有root权限的本地攻击者在复杂度低的攻击活动中利用，需用户交互。该漏洞存在于处理磁盘状态维持的 Storage Kit 守护进程中。

成功利用该漏洞可导致攻击者绕过 SIP 根限制，而无需物理访问权限来安装内核驱动，创建持久的“无法检测到的”恶意软件，或者绕过透明度、同意和控制 (TCC) 安全检查来访问受害者的数据。

苹果公司已在一个月前发布 macOS Sequoia 15.2修复该漏洞。微软今天发布报告表示，“SIP是针对恶意软件、攻击者和其它网络安全威胁的重要防护措施，为macOS 系统提供了根本性的防护层。绕过SIP影响整个操作系统的安全性，可导致严重后果，这说明部署完整安全解决方案的重要性，它能够从特殊权限进程中检测到异常行为。”

微软公司的安全研究员在近年来发现了多个 macOS 漏洞。他们曾在2021年报送了一个SIP绕过漏洞 “Shrootless” (CVE-2021-30892)，可导致攻击者在受陷的Mac 设备上执行任意操作并可能安装内核驱动。最近，他们还发现了另外一个SIP绕过漏洞，名为 Migraine (CVE-2023-32369)，以及另外一个名为 “Achilles” 的漏洞 (CVE-2022-42821)。这些漏洞可被通过不可信的应用部署恶意软件，从而绕过 Gatekeeper 执行限制。

微软首席安全研究员 Jonathan Bar Or 还发现了另外一个 macOS 漏洞 (CVE-2021-30970)，可导致攻击者绕过TCC技术访问macOS 用户的受保护数据。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[0.0.0.0 Day漏洞已存在18年，影响 MacOS和Linux设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520401&idx=1&sn=fcb5f892311d2858672c9908d0e08554&scene=21#wechat_redirect)

[恶意软件攻击Windows、Linux 和 macOS 开发人员](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520290&idx=2&sn=0dff9cae5a9ad1a39be2e6da027f70a9&scene=21#wechat_redirect)

[恶意PyPI 包针对 macOS，窃取谷歌云凭据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520240&idx=2&sn=549c4734cb750f652f9105a8e5df0546&scene=21#wechat_redirect)

[CocoaPods 严重漏洞导致 iOS 和 macOS 应用易受供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519949&idx=2&sn=4951a0b220cf599191f950ae82909410&scene=21#wechat_redirect)

[微软发现ncurses 库中的多个漏洞，影响 Linux 和 macOS 系统](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517665&idx=2&sn=c6944a499b07ed9b696150eef9f6a861&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/microsoft-macos-bug-lets-hackers-install-malicious-kernel-drivers/

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