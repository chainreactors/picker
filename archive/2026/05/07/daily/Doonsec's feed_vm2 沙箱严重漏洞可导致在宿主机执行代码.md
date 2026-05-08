---
title: vm2 沙箱严重漏洞可导致在宿主机执行代码
url: https://mp.weixin.qq.com/s/TIANdxyezsJNWFl2QPiamQ
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:53:29.728393
---

# vm2 沙箱严重漏洞可导致在宿主机执行代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfUSyRCOzyxfwwzBBk1KdF3GvrqmEUYRQeVWU46kAwkqKPaAknJJib7MgDkry2eicW4M40Jcic7RqhufsHl9wj4EJ5Y1lNPe6hTgxg/0?wx_fmt=jpeg)

# vm2 沙箱严重漏洞可导致在宿主机执行代码

Bill Toulas
Bill Toulas

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**流行的 Node.js 沙箱库 vm2 中存在一个严重漏洞 (CVE-2026-26956)，可导致攻击者逃逸沙箱并在宿主系统上执行任意代码。该漏洞已确认影响 vm2 版本3.10.4，不过此前版本也可能易受攻击。该漏洞的概念验证代码已公开。**

该库的维护人员在安全公告中提到，该漏洞仅影响启用了 WebAssembly 异常处理和 JSTag 支持的Node.js 25的环境（已在Node.js 25.6.1上得到确认）。

vm2 是一个开源的 Node.js 库，用于在受限的沙箱环境中运行不受信任的 JavaScript 代码。该库常被需要执行用户提供脚本的在线编程平台、自动化工具和SaaS 应用所使用。该库试图将沙箱代码与宿主系统隔离，并阻止其访问敏感的 Node.js API 如进程和文件系统的访问权限。

vm2 使用广泛，在 Node.js 的默认命令行包管理器 npm 上的每周下载量超过130万次。CVE-2026-26956源于该库在处理沙箱环境和宿主之间的跨越边界的异常时出错。安全公告解释称，vm2 在正常情况下依赖 JavaScript 层面的防护机制来防御宿主环境抛出的错误和并以来“桥接代理”来包装跨上下文对象，这两种机制完全运行在 JavaScript 层面。然而，WebAssembly 的异常处理机制能够在谷歌 V8 引擎的更底层拦截 JavaScript 错误，从而绕过 vm2 基于 JavaScript 构建的安全防御。

攻击者通过利用Symbol-to-string 转换触发精心构造的 TypeError，能够使宿主端的错误对象泄露未经 vm2 完全清理就直接泄露回沙盒中。由于泄露的对象源自宿主环境，攻击者可以利用其构造函数链重新获取 Node.js 内部对象（如 process 对象）的访问权限，最终在宿主机上实现任意命令执行。

安全公告中还包含一个概念验证（PoC）漏洞利用代码，展示如何在宿主机上实现远程代码执行。建议 vm2 的使用者尽快升级到 3.10.5 或更高版本（最新版本为 3.11.2），以降低 CVE-2026-26956 漏洞利用带来的风险。

今年年初，vm2 被指受另一个严重的沙箱逃逸漏洞（CVE-2026-22709）影响，可导致攻击者在底层宿主机系统上执行任意代码。此前影响该库的沙箱逃逸漏洞还包括 CVE-2023-30547、CVE-2023-29017 和 CVE-2022-36067，凸显了在 JavaScript 沙箱环境中安全隔离不受信任代码所面临的挑战。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[热门 NodeJS 库 vm2中存在严重的沙箱逃逸漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524984&idx=2&sn=e5fceae455445bc2b4660ccfb24127dd&scene=21#wechat_redirect)

[速修复！VM2 库中又出现严重的沙箱逃逸漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516269&idx=1&sn=02f92ed155ba727f4c05720d3c0cd9c4&scene=21#wechat_redirect)

[Palo Alto 提醒注意严重的 PAN-OS RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525932&idx=2&sn=a1f8acec7865ec3eec445777c4ad6251&scene=21#wechat_redirect)

[仅凭一条 git push 命令，即可在 GitHub 实现RCE 并访问数百万仓库](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525909&idx=1&sn=3a1d88cd8e20887b0792cd899f1b843e&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/critical-vm2-sandbox-bug-lets-attackers-execute-code-on-hosts/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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