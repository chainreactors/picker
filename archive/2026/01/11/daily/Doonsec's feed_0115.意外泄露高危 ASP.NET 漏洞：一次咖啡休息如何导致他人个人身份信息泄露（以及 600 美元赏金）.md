---
title: 0115.意外泄露高危 ASP.NET 漏洞：一次咖啡休息如何导致他人个人身份信息泄露（以及 600 美元赏金）
url: https://mp.weixin.qq.com/s/L6E-CNUjVMlv0V43mVHKCw
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:36:18.355926
---

# 0115.意外泄露高危 ASP.NET 漏洞：一次咖啡休息如何导致他人个人身份信息泄露（以及 600 美元赏金）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yKTOKd3ibs98qU2NsQYZxGh5FqSyMXjUV67MwUQzERImX31QYbxwd7KNmYpl0CZ3kKGicyzu9hzUgoEaVN0p6btw/0?wx_fmt=jpeg)

# 0115.意外泄露高危 ASP.NET 漏洞：一次咖啡休息如何导致他人个人身份信息泄露（以及 600 美元赏金）

toast

Rsec

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：奇怪的漏洞

在填写一份冗长的供应商注册表单时，我在一个私有目标服务器上闲置了大约 25 分钟。当我回来点击“下一步”时，页面加载了另一个用户的完整注册信息，包括公司个人身份信息 (PII)、银行账户、SWIFT 代码和 IBAN。重新加载页面后，所有信息都消失了。

我重现了两次这个问题，发现它发生在会话过期之后。根本原因很可能是 ASP.NET 4.0.30319 应用程序中的会话或缓存缺陷。团队将此报告标记为 P2 级别，并奖励了 600 美元。

## 准备工作

我当时正在测试一个大型供应商注册门户网站，需要填写无数表格。填写了一些信息后，我感到很沮丧，于是决定休息一下。

我让笔记本电脑停留在注册页面大约25到30分钟，同时用手机玩了一会儿游戏。

返回后，我点击 **“下一步”** 按钮继续上次中断的地方。

令我惊讶的是，页面加载后显示的却是完全不同的预填信息。其中包含另一家公司的注册数据，包括：

* 公司详情
* 财务详情
* 所有者详情
* 银行账号
* SWIFT 和 IBAN 代码

那一刻感觉很不真实。我刷新了页面，页面恢复了正常，又一片空白。

![](https://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98qU2NsQYZxGh5FqSyMXjUVqvBicxD6UjvmSEOO3pVHHOZO2S2K9xmyFvuYsYQyUYbhlIlURJOZfjA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98qU2NsQYZxGh5FqSyMXjUVzOCGF6roN4S3aQtXHtJ0UltpNYsXdLmZQhMkW4D7hj93Bcek6xpEeA/640?wx_fmt=png&from=appmsg)

## 重现问题

起初，我以为这只是偶然现象。但我仔细地重走了一遍步骤，看看能否再次重现这种情况。

1. 登录并开始供应商注册流程。
2. 请填写表格的一部分。
3. 让浏览器闲置约 25 至 30 分钟。
4. 返回并单击 **“下一步”** 按钮。
5. 观察其他用户的预填个人身份信息。

我在相同条件下重复了两次，问题始终存在。问题似乎在会话结束后立即触发，我测量会话时间约为 20 分钟。

## 可能的根本原因

我无法确认具体问题所在，但症状指向以下问题之一：

* **不安全的会话管理**会重复使用或错误路由已过期的会话。
* **服务器端缓存问题**，导致缓存的注册数据被提供给了错误的用户。
* **不正确的缓存控制标头**允许共享或过期的内容在超时后出现。
* **会话清理逻辑中存在状态泄漏，** 其中用户状态对象未正确清除。
* **共享视图状态或临时存储使用不当**，导致会话间数据重叠。

考虑到 ASP.NET 版本较旧以及时间模式，最可能的原因是服务器上的缓存或会话混淆。

## 最后想说的话

漏洞赏金猎取并非总是关乎复杂的漏洞利用或深入的技术分析。有时，它需要关注一些细微的、意想不到的行为。这个漏洞就是一个完美的例子。

如果你正在测试 ASP.NET 应用程序，不妨尝试暂时离开一会儿，让会话过期，然后再回来看看会发生什么。你可能会发现一些意想不到的情况。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

Rsec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

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