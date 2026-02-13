---
title: 苹果修复动态链接器漏洞：曾被用于针对特定个人的极其复杂攻击
url: https://mp.weixin.qq.com/s/ROj7UdxlSaC9kZ9VPDhojw
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:14:06.759136
---

# 苹果修复动态链接器漏洞：曾被用于针对特定个人的极其复杂攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDq0t90HAtUIHWfCsqwibRFG8q9o6C9udL6Vp7zGhUHUy8mtO8XvF43k3CctlAXyrDJ5s2KjxvDHWM6xJ4R1RbiaLzBBu7zLnabP0/0?wx_fmt=jpeg)

# 苹果修复动态链接器漏洞：曾被用于针对特定个人的极其复杂攻击

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

dyld（dynamic linker 动态链接器）是苹果操作系统（iOS、iPadOS、macOS、watchOS、tvOS 等）的核心系统组件，全称为 Dynamic Linker。

在苹果操作系统可以通过文件名后缀或其在框架包.dylib中的位置来识别动态加载的共享库。

动态链接器不仅将目标可执行文件链接到共享库，还会将机器代码函数放置在目标可执行文件在链接时已知的内存特定地址点。

当可执行文件需要与动态链接器交互时，它只需执行特定于机器的调用或跳转到这些已知地址点之一的指令即可。

macOS 和 iOS 平台上的可执行文件在执行过程中经常与动态链接器交互；甚至有可执行文件在启动数小时后仍可能与动态链接器交互，导致其加载更多库并解析更多符号。

主要职责包括：

1、在应用程序启动时动态加载 Mach-O 可执行文件和动态库（dylib）。

2、解析符号绑定、处理重定位（relocation）、执行延迟绑定（lazy binding）等操作。

3、管理进程的地址空间布局，确保库正确加载并链接到主可执行文件。

4、支持代码签名验证、库验证等安全机制，是系统启动和运行时的关键环节。

dyld 运行在进程早期阶段，具有较高权限，其漏洞往往会导致严重后果，如权限提升或任意代码执行。

CVE-2026-20700 漏洞详细分析根据苹果官方安全更新文档，这个漏洞是 iOS 26.3、iPadOS 26.3、macOS Tahoe 26.3 等更新中修复的0day漏洞（已被黑客主动利用）,拥有内存写入权限的攻击者可能能够执行任意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDo6gqdHYNWA3ticvlEucehf2XRLa8m8VnMqmWX61Y2uQ6w4TDETFjDcEVYiavpHe4AGbxh4rL57fAfy8tmqYrJgCo4iaOuPAj4MRw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqOChmsgTQEC1IRaOWRNDmYlG44HZx91CD8pQC7sSvekSWjHf0mVicM6nbfDDxGy7oJAC6CfEXM8bnDSzCQgkxgL9PS9dGfs2Ss/640?wx_fmt=png&from=appmsg)

漏洞描述与技术成因苹果官方描述：“A memory corruption issue was addressed with improved state management.”（通过改进状态管理，解决了内存损坏问题。）

核心问题：dyld 在处理动态加载过程中的状态管理存在缺陷，导致内存损坏（可能为 use-after-free、out-of-bounds write 等常见内存安全问题）。

触发条件：攻击者需要先获得一定的内存写入权限（memory write capability），这通常通过攻击链的前置漏洞实现（如 WebKit 漏洞渲染恶意内容）。

后果：利用后可执行任意代码，潜在实现内核级权限提升、沙盒逃逸或安装持久化恶意软件。

从类似历史 dyld 漏洞（如过去几年的一些动态链接器问题）推测，可能涉及加载库时的状态机错误，导致指针混乱或缓冲区溢出或者符号解析或重定位阶段的边界检查不足。

利用情况苹果明确表示：“Apple is aware of a report that this issue may have been exploited in an extremely sophisticated attack against specific targeted individuals”（苹果注意到报告称，该问题可能已被用于针对特定目标个人的极其复杂攻击）。

针对同一报告，苹果额外发布了 CVE-2025-14174 和 CVE-2025-43529（可能为同一攻击链的变种或关联问题）。

这两个漏洞黑鸟之前也发出来过了，这也是为什么要发这篇作为补充

[苹果修复了两个在定向攻击中被利用的Webkit漏洞，其中一个与谷歌ANGLE漏洞同源](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184189&idx=1&sn=26f196ee19262d48195c0c797e5b51b2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqCCqd2qVxg2dOPuG50icF7Nqyy0AzbwE07MlKT06xMlPUkCgyR5mDXendSOicXyeAAgn0mnsFKd6zm7cI2ysIAdQVS0kdvwoHzs/640?wx_fmt=png&from=appmsg)

Webkit漏洞后便是拥有内存写入权限的执行任意代码漏洞。

总之，这几个漏洞大概率是一条新的漏洞利用链。

防护方式：开启锁定模式 （关联阅读：[FBI未能解锁开启了锁定模式的苹果手机](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451185147&idx=1&sn=786bd4ce82ce7cab1d1dfa9699abb43f&scene=21#wechat_redirect)）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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