---
title: Apache HTTP 服务器修复严重远程代码执行漏洞，攻击者可利用该漏洞执行远程代码
url: https://mp.weixin.qq.com/s/veb-p9bRfEMBGw3tuhmxww
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:44:27.959049
---

# Apache HTTP 服务器修复严重远程代码执行漏洞，攻击者可利用该漏洞执行远程代码

# Apache HTTP 服务器修复严重远程代码执行漏洞，攻击者可利用该漏洞执行远程代码

原创

ZM
ZM

暗镜

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Apache 发布了 HTTP 服务器 2.4.71 版本，以解决三个安全漏洞，其中包括一个可能导致远程代码执行的严重内存损坏漏洞。该更新于 2026 年 11 月 11 日发布，修复了 mod\_http2、mod\_md 和 mod\_vhost\_alias 中的漏洞，这些漏洞的严重程度分别被评为“严重”、“重要”和“低”。此次更新是在Apache HTTP 服务器此前发布的安全更新之后进行的，之前的更新解决了内存安全和拒绝服务攻击问题。

最严重的漏洞 CVE-2026-119618 存在于 mod\_http2 模块的 assign\_headers() 函数中。Apache 将此漏洞的根本原因描述为：在未进行适当同步的情况下，使用共享资源进行并发执行。这种情况可能会破坏堆内存，并可能允许攻击者执行代码。受影响的 Apache HTTP 服务器版本为 2.4.55 至 2.4.70，以及 GitHub 上的独立 mod\_h2 版本为 2.0.8 至 2.0.42。

Apache 感谢 Anthropic 的 OSS Scanner 识别出该漏洞（编号为 ANT-2026-MAPKT6MZ），以及 Google Cloud Vulnerability Research 的研究人员 Anthony Weems 和 Simon Scannell。Anthropic 于 10 月 26 日报告了该漏洞，而 Google 则于 11 月 3 日报告了该漏洞。

Apache官方安全公告记录了提交 824beab9b9424d6cfb29595248fdbf6c3dddeab1 下的修复。该公告并未提供漏洞利用链、身份验证要求或实际利用的证据。因此，披露的远程代码执行风险不应被解读为攻击者已攻破易受攻击的部署。

二个漏洞 CVE-2026-106023 是 mod\_md 模块在 HTTP 请求处理期间的一个高危空指针解引用漏洞。它会导致子进程崩溃，并影响 2.4.30 至 2.4.70 版本。该漏洞于 9 月 29 日报告，由 hexb1n、Yang Song、JiaSheng He、Lucian Nitescu 和 Bartlomiej Dmitruk 发现。

第三个漏洞 CVE-2026-109163 涉及 mod\_vhost\_alias 模块中一个字节的栈缓冲区覆盖漏洞，该漏洞与 CVE-2026-63292 存在关联。该漏洞被评为低危漏洞，仅影响 HTTP 服务器 2.4.69 和 2.4.70 版本。Apache 于 10 月 5 日收到该漏洞报告，并感谢 Gustavo Aiello、Charles Vosburgh、Wojciech Tatarski、Oz Kaiser 和 Daisuke Hatakeyama 的贡献。需要注意的是，该漏洞的覆盖范围有限且评级较低，不应与 mod\_http2 模块的严重漏洞混淆。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过