---
title: Chrome 零日漏洞已被恶意攻击者积极利用，用于执行恶意代码
url: https://mp.weixin.qq.com/s/_SVBWccyLKKl17kVnluF7Q
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:07:01.974134
---

# Chrome 零日漏洞已被恶意攻击者积极利用，用于执行恶意代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PhMCkN6DyTaJ8SEzotKiaZUcCibMt7ibmNdOqxmicN2xoDVLnljajIZuHdn6Gxr8NZdU7edibUzJQ49QWhwhk5Anee2ZKvCeZCMpbA/0?wx_fmt=jpeg)

# Chrome 零日漏洞已被恶意攻击者积极利用，用于执行恶意代码

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

谷歌发布了针对其Chrome桌面浏览器的紧急安全更新，以解决两个严重的零日漏洞。

这两个漏洞分别被追踪为 CVE-2026-3909 和 CVE-2026-3910，均被归类为高危漏洞，并已证实攻击者正在积极利用这些漏洞。

强烈建议用户立即更新浏览器，以防止潜在的恶意代码执行和系统入侵。

## **漏洞的技术细节**

2026 年 3 月 12 日的稳定版更新专门修复了谷歌内部团队于 2026 年 3 月 10 日发现的两个重大安全漏洞。

第一个漏洞 CVE-2026-3909 是 Skia 中的一个“越界写入”漏洞。Skia 是一个开源的 2D 图形库，是 Chrome 的核心图形引擎。

当程序将数据写入超出已分配内存缓冲区预期边界的区域时，就会发生越界写入。

攻击者可以利用这种内存损坏使浏览器崩溃或在受害者设备上执行任意恶意代码。

第二个漏洞 CVE-2026-3910 是 V8 中的“不恰当实现”。V8 是为浏览器提供动力的高性能 JavaScript 和 WebAssembly 引擎。

当如此关键的组件中存在实现缺陷时，往往会使威胁行为者能够绕过安全沙箱、操纵浏览器内存，并在后台秘密运行未经批准的脚本。

谷歌已明确承认，CVE-2026-3909 和 CVE-2026-3910 的漏洞利用程序目前已在实际环境中存在。

这证实了网络犯罪分子或国家支持的威胁行为者正在积极利用这些漏洞进行现实世界的攻击活动。

攻击者通过诱骗用户访问精心制作的恶意网站，即可触发这些漏洞，而无需受害者进行任何额外的交互。

为防止进一步滥用，谷歌有意限制对这些漏洞的具体技术细节的访问，直到大多数用户成功更新到安全版本为止。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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