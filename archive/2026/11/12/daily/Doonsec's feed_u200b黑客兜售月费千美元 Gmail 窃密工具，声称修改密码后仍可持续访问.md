---
title: u200b黑客兜售月费千美元 Gmail 窃密工具，声称修改密码后仍可持续访问
url: https://mp.weixin.qq.com/s/uH6kbuakX_Ay4VcBi8I84g
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:58:35.053224
---

# u200b黑客兜售月费千美元 Gmail 窃密工具，声称修改密码后仍可持续访问

# ​黑客兜售月费千美元 Gmail 窃密工具，声称修改密码后仍可持续访问

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一款名为 Remus Stealer 的信息窃取工具正在推广 Gmail 邮箱访问功能，开发者声称，即使用户修改密码、撤销登录会话，攻击者仍可能持续读取邮箱。目前，该能力尚未得到独立验证。

近日，网络安全公司 Hudson Rock 披露，一款名为 Remus Stealer 的信息窃取工具正在销售一项特殊的 Gmail 访问功能。该功能被列为企业版专属服务，售价为每月 1,000 美元。

与传统窃密工具主要窃取浏览器 Cookie 不同，该工具宣称能够直接读取受害者的 Gmail 邮件，并在被盗设备的管理面板中提供邮箱内容检索功能。

**一、宣称修改密码后仍能访问邮箱**

根据 Hudson Rock 的调查，Remus Stealer 的开发者声称，即使受害者修改 Google 账号密码、关闭浏览器，或者撤销已有登录会话，攻击者仍然能够访问邮箱。

该功能还支持将已获取的邮箱访问权限分享给其他操作者，使不同人员能够访问同一个被控制的邮箱。

Hudson Rock 表示，其曾与工具开发者及一名实际使用者进行交流，并获得了相关功能的操作截图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0g7qUMk8Dpzz1dukWdibKkdsibYHQNYq24tn6TiaNfS0tQQCYIr5uCiaZVSKcytJhkS1tmJ9DlHEnaDM9AwNhl8BzM2J2l83GzvmA/640?wx_fmt=png&from=appmsg)

开发者透露，该功能通过与浏览器内存交互实现，并非持续运行的后台程序，而是在执行相关操作后退出。但对于具体实现方式，开发者拒绝披露更多技术细节。

**二、持久化访问机制尚不明确**

对于该工具如何在密码修改和会话撤销后继续访问 Gmail，目前仍没有明确答案。

Hudson Rock 推测，工具可能在用户登录 Gmail 期间获取或建立某种授权凭据，之后通过远程组件继续访问邮箱，即使最初执行窃取操作的恶意程序已经退出，也可能维持访问能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0WD2C9aRwSiaGJB53bAeBTjHeia5eA4ElP1m7F47mzyp0sMVotxESUT9KQ6lxGM5ibjGHPFpKuTkcFxTyicRtSRGrdGeHic9L2TuDY/640?wx_fmt=png&from=appmsg)

不过，这一推测尚未得到技术验证。

目前没有受控测试能够证明，在用户修改密码、撤销现有会话以及第三方应用授权后，攻击者仍然可以持续读取新收到的邮件。

此外，开发者将该功能宣传为 Gmail 零日能力，但目前也没有证据证明其利用了 Gmail 本身的安全漏洞。

**三、邮箱失陷可能引发连锁账号风险**

如果该功能所宣称的能力得到证实，其影响将不仅限于 Gmail 邮箱本身。

由于大量互联网服务使用电子邮件进行身份验证、密码重置和安全通知，一旦攻击者持续控制用户邮箱，就可能进一步获取其他平台的密码重置链接和验证码，从而扩大账号失陷范围。

需要注意的是，攻击者首先仍需通过恶意程序感染目标设备，并获得相应的邮箱访问权限，才能使用这项功能。

**四、安全建议**

针对这类邮箱账号安全风险，Hudson Rock 建议，受影响用户应优先断开并清理已经感染的设备，避免在受感染环境中继续访问重要账号。

随后，应通过可信设备修改相关账号密码，并重点检查：

* 登录设备与活动会话： 排查陌生设备和异常登录记录。
* 第三方应用授权： 检查是否存在未经授权的应用访问权限。
* 邮箱安全设置： 核查转发规则、过滤器及其他异常配置。
* 关联账号： 检查使用该邮箱进行密码重置或验证码接收的其他平台账号。

目前，Remus Stealer 所宣传的 Gmail 持久化访问能力仍缺乏独立技术验证，相关机制也尚未公开。其是否能够在用户完成全面账号恢复后继续读取新邮件，仍有待进一步测试和确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2GoVFjQfMG1AJ15wRlZVc9uKzAwcbd75D8iaM221USFJ1H3xDv1YgOusfjUUrSREbpF08opSmK3kLreTsWLD5AB6tDUbu1ksbw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K05Ud0lCPJUy0V8QY8xq1ib1YMeF99ogicpZnerMjqlrticga5I9XozY2ZzeV8VUI5XVwafhbJUlULn6tD3gWacslgNx7KaEPmKJM/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K3rl450oV5IjzRm0pYMrK4eqiaIA48fP4nKvkzAhTXNFguX0l5zfQ4kRlURZpnXkumbUqFnp60usqT0aHN4ggF9RuqC4D9ywL0k/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K3PalxAqQaBlpicPC9u8Uh268Wxl3NokSlGqHnVjZ0vGfuYciauJlAg6T7XNlsAMX6uNTtMjicatZDOLd7dr1rAcJibTK1ntC3gIX0/640?wx_fmt=gif&from=appmsg)

**球在看**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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