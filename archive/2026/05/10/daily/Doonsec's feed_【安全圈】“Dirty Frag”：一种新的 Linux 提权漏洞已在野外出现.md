---
title: 【安全圈】“Dirty Frag”：一种新的 Linux 提权漏洞已在野外出现
url: https://mp.weixin.qq.com/s/zRvsDn7rW3e17eLyJSs01w
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:53:27.353901
---

# 【安全圈】“Dirty Frag”：一种新的 Linux 提权漏洞已在野外出现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFS9Qmx71ib3yGjUFHZwShlWdYEHjC2nXxEc9ibfL3kG1VRb8HoJIL7DsDWbcVZUqcEJicwfIiauhaMpWW0ZoGDJviaQJ7oDLKvCiaB0/0?wx_fmt=jpeg)

# 【安全圈】“Dirty Frag”：一种新的 Linux 提权漏洞已在野外出现

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

安全研究人员披露了 Linux 内核中一个尚未修复的新漏洞，代号为 “Dirty Frag”。**该漏洞可让无特权的本地用户在大多数主流 Linux 发行版上获取完全的 root 权限，这些发行版包括 Ubuntu、红帽企业 Linux（RHEL）、Fedora、AlmaLinux 和 CentOS Stream。**

“Dirty Frag” 与 “Dirty Pipe” 系列漏洞相关，但独立于 “复制失败”（Copy Fail）缓解措施，这意味着已应用 algif\_aead 黑名单的系统仍完全暴露在风险中。

相关公告称：“（该漏洞）通过串联 xfrm - ESP 页面缓存写入漏洞和 RxRPC 页面缓存写入漏洞，可在主流 Linux 发行版上获取 root 权限。‘Dirty Frag’扩展了‘Dirty Pipe’和‘复制失败’所属的漏洞类别。由于这是一个确定性逻辑漏洞，不依赖时间窗口，无需竞争条件，漏洞利用失败时内核也不会崩溃，成功率非常高。”

研究人员玄宇・金（Hyunwoo Kim，推特账号 @v4bel）最先披露了该漏洞。

该漏洞串联了两个不同的缺陷。第一个是 xfrm - ESP 页面缓存写入漏洞，源于 Linux IPsec 子系统，在 2017 年 1 月的一次源代码提交中引入，同一提交还导致了 CVE - 2022 - 27666 漏洞，这是一个影响多个 Linux 发行版的缓冲区溢出漏洞。第二个是 RxRPC 页面缓存写入漏洞，于 2023 年 6 月引入。单独来看，这两个缺陷并非在所有系统上都能起作用，但它们相互弥补了彼此的盲点：当某条路径因环境因素（如 Ubuntu 的 AppArmor 对命名空间创建的限制）被阻断时，另一条路径则会打开。这种串联使得 “Dirty Frag” 在各种发行版上都具有普遍危险性。

分析报告指出：“这两个漏洞的共同之处在于，在零拷贝发送路径中，splice () 函数将攻击者仅有读权限的页面缓存页的引用，按原样植入发送方套接字缓冲区（skb）的片段槽中，接收方内核代码会在该片段上进行就地加密。结果，无特权用户仅有读权限的文件的页面缓存在内存中被修改，后续每次读取都会看到修改后的副本。”

“Dirty Frag” 尤其危险之处在于其可靠性。与许多依赖精确时间窗口或竞争条件的内核漏洞利用不同，这是一个确定性逻辑漏洞。漏洞利用失败时不会导致内核崩溃，且成功率极高。一个可用的概念验证代码已公开，将利用过程简化为一条命令。

该漏洞的披露过程较为复杂：在第三方未经协调就发布详细技术信息和漏洞利用代码后，禁令提前解除。目前该漏洞尚未分配 CVE 编号。

报告总结称：“将这两个变体串联起来，盲点相互覆盖。在允许创建用户命名空间的环境中，ESP 漏洞利用首先运行。相反，在 Ubuntu 系统中，虽然用户命名空间创建被阻止，但 rxrpc.ko 模块已构建，RxRPC 漏洞利用就能起作用。”

在官方补丁发布之前，建议的解决方法是将 esp4、esp6 和 rxrpc 内核模块列入黑名单，阻止它们加载。

***END***

阅读推荐

[【安全圈】Chrome 148 安全大更新127 个漏洞，立刻升级](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076237&idx=1&sn=30e0c0d6f2c1d613c004fdfcccaa4172&scene=21#wechat_redirect)

[【安全圈】Ubuntu官方账号被黑！发布假AI程序：实为钓鱼骗局](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076237&idx=2&sn=e643fec666d72d0f489fc4428c759af1&scene=21#wechat_redirect)

[【安全圈】思科修复高危漏洞，防范 SSRF 与代码执行攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076237&idx=3&sn=cf888f50ed50f6f3e877ab1eae838d07&scene=21#wechat_redirect)

[【安全圈】供水设施遭入侵，Claude AI 助力黑客锁定 OT 资产](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076218&idx=1&sn=38a3aaf6dc9ce8f8a4c69044d68a8236&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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