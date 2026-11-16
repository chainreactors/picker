---
title: 现在iOS木马好先进呀！
url: https://mp.weixin.qq.com/s/V9j4sHfCeqyqMxxlHepBCA
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:46:56.373253
---

# 现在iOS木马好先进呀！

# 现在iOS木马好先进呀！

原创

胡明
胡明

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OhNkYaSr3KteDwgcVopWyeiaSgQe2ckExSd8tkNksge26N7ibxSoWDqficTjglVsfgPM75uBxOScJT3k25ic7uPVcThStnfYAJJPQ/640?from=appmsg)
> **导语**：一个地下论坛帖子里多了一份"报价单"。卖家把工具叫作 iOS 远程控制面板，宣称 iOS 13 到 27.2 全都管，钓鱼链接点开、钥匙串明文拖走、摄像头麦克风实时开着。我们只看到这个售卖帖，不知道货从哪里流出。

---

## 一、卖家自报的六项能力

* **初始访问**：短信、聊天软件、邮件投递，配钓鱼页面；顺带提了 WebKit 远程代码执行。
* **权限提升**：绕开系统的指针校验（PAC）、从 GPU 通道逃出沙箱、借用系统媒体进程提权、靠 ICMPv6 路径拿内核读写。
* **重启后驻留**：设备重启之后依然保持访问。
* **数据导出**：钥匙串（Keychain）数据、聊天记录、文件、凭据，以及各类 App 里的信息。
* **实时监控**：摄像头、麦克风、定位、屏幕。
* **远程控制**：集中式控制面板、远程 Shell、多设备管理、多条通信通道。

最后还补了一句：声称能绕过银行 App 的安全机制，提取加密钱包里的数据。

![地下论坛帖子与卖家自制的 iOS 远程控制面板](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MoibWmUDVPtrp2c6dxysVb4lCdTPjHKKLQbic1z3hTzfOdNTW5WJwrZWBq0TiaiahmmlRGpbicc6WUmY6ZTSXvFQiaxlpCIIvicicsFok/640?from=appmsg "地下论坛帖子与卖家自制的 iOS 远程控制面板")

截图里那套界面是卖家自己做的：目标分 ONLINE、DEGRADED、OFFLINE 三档，右边挂着 iPhone 16 Pro Max，系统版本 27.2，电池 57%，信号 94%。这不是苹果的东西，是拼出来的控制端。

## 二、先进在哪

两个点最抓眼。

一个是版本新。宣称支持到 iOS 27.2，这是目前最新的 iOS 版本号，截图里的目标机跑的就是这个版本。

另一个是功能面宽。市面上多数在卖的 iOS 漏洞只值一句"能进沙箱"，拿到的也就是一次代码执行。这套东西把后面全包了：进得去（钓鱼加短信投递）、站得住（提权加重启后还在）、拿得走（钥匙串、聊天记录、文件、钱包）、看得见（四个监控通道）、管得住（面板加多设备）。从投递到变现是一条完整闭环。

![卖家自报的六项能力](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NmxenJoauvwyMaUdldFlzTem2wn5urhYNGx8x4ak1LgynUy6FyMGE4Cfj8DklE40ibicM0CwrTgbibTLqpXGdYYkpziabgMXxPhc0/640?from=appmsg "卖家自报的六项能力")

但也得说清楚：这些全是卖家写在帖子里的描述，没有 CVE 编号，没有实测报告，我们也没拿到实物。先进是宣传口径还是真本事，只有卖家自己知道。

## 三、这行货怎么定价

同一数据源近半年还有几笔同类交易：

* 4 月：iOS 零日，独家 1.7 万美元，非独家 900 到 3000 美元，明确带 PAC 与 PPL 绕过，宣称可明文提取钥匙串。
* 9 月：覆盖 iOS 15.0 到 18.2 的利用链，1 万美元限 3 手、1.8 万美元只卖 1 手，走的是已公开的 WebKit 与 dyld 漏洞。

规律很清楚：漏洞越新、覆盖越全、独家成分越多，价格越贵。这次连价格都没标，却张口就是 13 到 27.2，更像是把若干条链打包成一个"框架"，买家按手里机型下单。

## 六、结语

地下论坛卖的东西真假只有卖家自己清楚，"支持到 27.2"多半有水分。但这笔生意成立的原因不复杂：苹果防线堆了十几层，一份能读钥匙串、能开摄像头、重启后还能继续在线的工具，价格顶得上好几台手机。被盯上的从来不是设备，是后面那个人。

**原文出处**

https://dbu.gs/news/ios-device-compromise-framework-for-sale-20261113

**声明**：本文只是我们刷到的那个售卖帖，对这套木马的描述全部来自卖家自述，未经独立验证；我们不知道卖家在哪出货、没见过实物。本文只做技术拆解，不提供木马程序、破解工具、购买渠道，我们也不卖这种货、不代购转发。想买的，请自己想清楚代价。

**版权声明**：本文由华盟网原创发布，保留所有权利。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NibhjoFGL1ibNXIMCic53z1Wn4eh9z21UXLVkWaiaLLOVu3FWwgPf3zXlfKLhbaks3O45OwHPwkr5M48Rnd1R044IhZrWQG96efics/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6N0ZsxCiaoGjtJAtUch6ZUVwvDrX54HL5mtLUAKnmibsTUhICPibyaaM2AG26ozxY0icexsGlncyq5QTYQARBw7SkE8HG5vRibMPytc/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MQicyTZ7Bvb8A3tGib7I4cUNfHINj2xs1C7MGG2Ly9dw4boD3YsvX6tHjBC6Giaibwqoj6uluy8vmu7baicuEmWgfnxOMQKxqVazHY/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OwMLciba0pyn5SsK83ZicNhf0QkibPwXBBrv9JY5zfs80Th8u7cYiclI0F09OZDt4QpNIgBvibPZ5j8Iv2h1Jr38y6cJJW059e0JdQ/640?from=appmsg)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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