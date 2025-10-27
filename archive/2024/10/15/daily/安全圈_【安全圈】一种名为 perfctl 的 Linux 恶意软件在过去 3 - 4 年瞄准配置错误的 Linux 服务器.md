---
title: 【安全圈】一种名为 perfctl 的 Linux 恶意软件在过去 3 - 4 年瞄准配置错误的 Linux 服务器
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065207&idx=4&sn=461cec5353ae7f3583dde92f719b667f&chksm=f36e61f7c419e8e1775062eeab2eaf3ee8fcd24f2acde0f36dc0d98247d87a50bb28f0ff15bb&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-15
fetch_date: 2025-10-06T18:52:19.570543
---

# 【安全圈】一种名为 perfctl 的 Linux 恶意软件在过去 3 - 4 年瞄准配置错误的 Linux 服务器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQdh9HdVM9bUxxcI0t6uVOAvPRxehE6XyytLsrMXMrwI3kwGHYxXNnIQ/0?wx_fmt=jpeg)

# 【安全圈】一种名为 perfctl 的 Linux 恶意软件在过去 3 - 4 年瞄准配置错误的 Linux 服务器

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

恶意软件

perfctl 恶意软件以配置错误的 Linux 服务器为目标，持续部署加密货币矿工和代理劫持软件。
Aqua Nautilus 的研究人员揭露了一种被称为 perfctl 恶意软件的 Linux 恶意软件，在过去 3-4 年中，该恶意软件以配置错误的 Linux 服务器为目标。

恶意代码被用来投放加密货币矿机和代理劫持软件。

Perfctl 是一种针对 Linux 服务器的难以捉摸的持久性恶意软件，它利用 rootkit 隐藏自己的存在，并在新用户登录时停止任何 “嘈杂 ”的活动，一直休眠到服务器再次闲置。在通信方面，它在内部使用 Unix 套接字，在外部使用 TOR。执行后，perfctl 会删除其二进制文件，并作为一项服务在后台运行。

尽管该恶意软件的主要目标是运行加密程序，但专家警告说，它还会执行代理劫持软件。在一次沙盒测试中，一名威胁行为者出于侦察目的访问了该恶意软件的后门。攻击者对服务器进行了分析，并部署了实用程序来调查其环境，更好地了解恶意软件是如何被研究的。

一旦攻击者利用了漏洞或错误配置，perfctl 恶意软件就会从攻击者控制的 HTTP 服务器下载主要有效载荷。有效载荷采用了多层技术，以确保持久性并躲避检测。它将自身移动到 /tmp 目录，以执行它的进程（如 sh）重命名自身，并删除原始二进制文件以掩盖其踪迹。该恶意软件既是下载器，又是本地命令与控制（C2）进程，试图利用 Polkit 漏洞 CVE-2021-4043（又名 PwnKit）进行 root 访问。

恶意代码使用欺骗性的名称将自身复制到不同的磁盘位置，并在服务器上建立后门以进行 TOR 通信。

该恶意软件在投放rootkit的同时，还投放了经过修改的Linux实用程序（如ldd、losof），这些实用程序具有用户地rootkit功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQdWLuKxqSOWhq1k8icH495NM4o8sicq4X6u97uwWdCzZlHEokWaC8xibmQ/640?wx_fmt=png&from=appmsg)

Linux 恶意软件经过打包和加密，以逃避检测。它使用先进的规避技术，如在检测到新用户时停止活动，恶意代码还可以终止竞争恶意软件，以保持对受感染系统的独占访问权。

“作为其命令和控制操作的一部分，恶意软件会打开一个 Unix 套接字，在 /tmp 目录下创建两个目录，并在其中存储影响其操作的数据。这些数据包括主机事件、自身副本的位置、进程名称、通信日志、令牌和其他日志信息。此外，恶意软件还使用环境变量来存储数据，从而进一步影响其执行和行为。报告指出：”所有二进制文件都经过打包、剥离和加密，这表明恶意软件在绕过防御机制和阻碍逆向工程尝试方面做出了巨大努力。该恶意软件还使用了先进的规避技术，例如在检测到 btmp 或 utmp 文件中有新用户时暂停其活动，并终止任何竞争恶意软件，以保持对受感染系统的控制。

为了保持持久性，攻击者修改了 ~/.profile 脚本，以便在用户登录时执行恶意软件，检查 /root/.config/cron/perfcc 是否可执行。如果是，恶意软件就会在合法服务器工作负载之前运行。它还会在 Bash 环境中执行 ~/.bashrc 文件，以在恶意软件后台工作时维持服务器的正常运行。脚本会抑制错误以避免警告。

一个名为 wizlmsh（12kb）的小型二进制文件被放入 /usr/bin，在后台运行，以确保 perfctl 恶意软件的持久性，并验证主要有效载荷（httpd）的执行情况。

“攻击的主要影响是资源劫持。在所有案例中，我们都观察到一个 Monero 加密程序 (XMRIG) 被执行并耗尽了服务器的 CPU 资源。该加密器还进行了打包和加密。报告总结道：”一旦解包和解密，它就会与加密矿池通信。“研究人员说：”要检测 perfctl 恶意软件，可以查看 CPU 使用率是否出现异常峰值，或者如果 rootkit 已经部署在服务器上，系统速度是否变慢。“这些可能表明存在加密货币挖掘活动，尤其是在空闲时间。

来源：Perfctl Malware targets Linux servers in cryptomining campaign (securityaffairs.com)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhIRRy7YakD1vW3pJqde1NQyYkxqal233XMKoSdD5QRf49C2VMouZ5xh5Eb9vWP0v1YbZCZbH4Xpg/640?wx_fmt=jpeg)[【安全圈】](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065190&idx=2&sn=38505d2516cdbe4a948e32101cbbebf5&chksm=f36e61e6c419e8f0e3861875cb5395af2defdb95e309b40b053c850d37a6e094e918bc6e63c9&scene=21#wechat_redirect)广东省教育厅：不法分子入侵短信平台、向师生家长发送含非法链接短信，已报警

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaicG5ay65VzUDndyib8QXNJwf17RxsWCibGJAy5CqxkkY35X5XyICp9cbr4uNHYM4l2WfdzjsvH9ictA/640?wx_fmt=jpeg)[【安全圈】扫地机器人被黑客入侵，追逐宠物并辱骂主人](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065190&idx=2&sn=38505d2516cdbe4a948e32101cbbebf5&chksm=f36e61e6c419e8f0e3861875cb5395af2defdb95e309b40b053c850d37a6e094e918bc6e63c9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaicG5ay65VzUDndyib8QXNJwRAEImmIV5VaTKyv8mnMphplwnXJfBBbkk04zuAD1l3B7WLGON5Jh1Q/640?wx_fmt=jpeg)[【安全圈】互联网档案馆遭遇黑客攻击，3100 万用户数据被泄露](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065190&idx=3&sn=f278990431cd6c2598c9d914ee2b2e45&chksm=f36e61e6c419e8f010e3701d4e8cc0c32276cee6d24c47cc149b0fd7244f4cbe0799fd9ccc3a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaicG5ay65VzUDndyib8QXNJwD5omE3x65h5waBCOc788Wc4OBAUNxbo9aFd5ibU6W9xRcFSenopDfng/640?wx_fmt=jpeg)[【安全圈】安全公司曝光黑客假借求职名义发送木马邮件，HR 打开就中招](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065190&idx=4&sn=0401fbd7c8c87dba65ea5338166a7d73&chksm=f36e61e6c419e8f02fca8fa6dbad1acf009cdeab95878710b0d2a1a4f3adda6641690f978fe8&scene=21#wechat_redirect)

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