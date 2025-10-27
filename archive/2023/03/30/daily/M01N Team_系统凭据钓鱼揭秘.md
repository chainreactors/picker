---
title: 系统凭据钓鱼揭秘
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247491118&idx=1&sn=4bba65b079757d36f4dc366a727ed0d4&chksm=c187de3ff6f05729b2f0224ba91c02b113926e553a6dbc1a35d3236a67102be3eda5d395fd84&scene=58&subscene=0#rd
source: M01N Team
date: 2023-03-30
fetch_date: 2025-10-04T11:08:18.655514
---

# 系统凭据钓鱼揭秘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbPoko3y1oG4oweW75rEu3IMwKwKycuhRwnk3ica8hOOvibBX69oaicziaHsHKmQ1XCM6q65Lh4LMvNng/0?wx_fmt=jpeg)

# 系统凭据钓鱼揭秘

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTH0o5pTAO8jdqnibfx5ttzeyzVJRTatfuSibA1rn51P4j6jrFUXOX3Crbw/640?wx_fmt=gif)

**背景**

在进行内网横向移动时，通常会尝试抓取目标机器上的登录哈希和密码。但是，这种方法并不总是可行，因为有些目标机器可能没有这些信息，或者这些信息已经被清除或加密。因此，黑客们开始模拟Windows系统环境中的身份认证场景，如Outlook登录、提升授权（用户账户控制）或者锁屏解锁等，通过伪造这些场景来欺骗用户。

本文旨在介绍几种有趣的系统凭据钓鱼攻击方式，通过对系统凭据钓鱼的技术和方法的介绍，帮助读者更好地保护自己的系统和网络安全。

**01**：FakeLogonScreen

FakeLogonScreen是一款采用C＃语言编写的内网凭证钓鱼工具。使用时只需要将其在目标机器运行，它将自动显示伪造的windows登录屏幕、最小化其他应用的窗口、阻止大部分的快捷键，并且支持自动验证密码是否正确。类似的工具还有SharpLocker。

效果截图：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa4tQvo97CFR9K9MrlsZiaWD7OPKIr1JtjIlSIYLtEUjwG8u0UmvkyOkF2KDwNUfnGMfmib6fjeVUcA/640?wx_fmt=png)

**图：FakeLogonScreen的伪造锁屏界面**

**02**：Invoke-CredentialPhisher

Invoke-CredentialPhisher 是一个利用windows通知的内网凭据钓鱼工具。提供CobaltStrick插件和ps1脚本，支持几种通知钓鱼模板。当受害者点击“windows通知”后，会弹出对应的钓鱼窗口诱导输入。

效果截图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHADeNZW7FWQWBtNXVoZE4NxXTuqMsZ06KBJJhKyiayOpHljHQHdyHOzg/640?wx_fmt=jpeg)

**图：Invoke-CredentialPhisher的伪造windows通知**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTH25NlXWbzfFYIOPuibIpTHTgdnicr9PXelHbMIobgER3Dic2R7jlMhAgFQ/640?wx_fmt=jpeg)

**图：Invoke-CredentialPhisher的伪造登录界面**

**03**：Edge kiosk

Edge浏览器不用多介绍，但是Edge kiosk模式可能很多人不了解，Edge kiosk模式是Microsoft 给Edge浏览器打造的一项功能，允许用户以受限的单一应用程序模式运行浏览器。通常用于公共空间，例如博物馆或零售店，需要向用户显示特定的web应用程序，而不允许用户访问其他网站或其他功能。

当Edge以kiosk模式启动时，它将以全屏方式打开指定的网站。用户将在没有任何提示的情况下，整块屏幕被一个网页覆盖，无法访问地址栏、菜单项或任何其他浏览器功能，并且禁用大部分的快捷键。

通过微软给出的介绍，我们可以快速的了解Edge kiosk的参数。

```
#以kiosk模式打开指定网站，并且全屏msedge.exe --kiosk www.contoso.com --edge-kiosk-type=fullscreen#禁用首次Microsoft Edge 运行体验。msedge.exe --kiosk www.contoso.com --edge-kiosk-type=fullscreen --no-first-run#指定kiosk模式空闲超时时间msedge.exe --kiosk www.contoso.com --edge-kiosk-type=fullscreen --kiosk-idle-timeout-minutes=1
```

由于windows系统大部分自带Edge浏览器，基于这些特性，首先仿造默认锁屏样式，制作了一个简单的钓鱼页面，接下来只需要在目标机器上运行一条命令，即可用Edge kiosk模式打开我们的钓鱼页面，进行强制的锁屏密码钓鱼。

```
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --kiosk http://127.0.0.1:8080/index.html --edge-kiosk-type=fullscreen
```

效果如图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHmxIkt6433ZGV92XiaesopGGYJtwlxShMN5cxHxXJKdVRy7YLMjGp16Q/640?wx_fmt=jpeg)

**图：Edge kiosk模式打开仿造锁屏样式的页面**

**利用思考：**

由于此方式利用Edge的正常功能，不存在工具免杀的问题，而且运行一条命令即可触发。也就是说在没有目标机器权限的情况下，只要想办法让目标以kiosk模式运行Edge即可钓鱼锁屏密码。

众所周知，lnk文件可以带参数运行指定程序，在起始位置选择Edge浏览器的绝对路径，目标填入kiosk模式的命令行参数，加上必要参数避免首次启动引导和无法退出，利用lnk文件特性，可以构造诱导性后缀名、选择诱导性的图标，构造如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHUMWOA5O4zeJMg96fI0jibLzrrNOQAGvB5jib1gqSxxPozdIpOyB0Q1ibw/640?wx_fmt=jpeg)

**图：利用lnk文件构造Edge kiosk模式钓鱼样本**

双击“绝密文件.pdf”，启动kiosk模式锁屏钓鱼网页：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHmxIkt6433ZGV92XiaesopGGYJtwlxShMN5cxHxXJKdVRy7YLMjGp16Q/640?wx_fmt=jpeg)

**图：lnk文件打开后仿造锁屏样式的页面**

输入凭据确定后，将打开一个诱导pdf避免引起怀疑，且超过一分钟将会自动超时退出。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHma5cic81ibZtocMXRHxR2RzYrj5E4iacy9n0VnmKrcKjVuxZCPaf4oB3w/640?wx_fmt=jpeg)

**图：解锁后跳转某诱导pdf文件**

**04**：写在最后

本文介绍了几种有趣的系统凭据的钓鱼方式。网络钓鱼无处不在，需要我们通过提高安全意识来减少被攻击的可能性。希望本文能为您提供一些帮助，并引起大家对网络钓鱼的重视和警惕。让我们一起努力营造一个更加安全和健康的网络环境！

**附录**：参考文献

https://github.com/bitsadmin/fakelogonscreen

https://github.com/Pickfordmatt/SharpLocker

https://github.com/SpiderLabs/SharpCompile

https://learn.microsoft.com/zh-cn/deployedge/microsoft-edge-configure-kiosk-mode?source=recommendations

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTH1b78spyGicmH6omxSIsEvMmxxl8qry0k35yuJunaBq93yeGGj1PfXRg/640?wx_fmt=png)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHTJricAdx0AjSnFNpZxnOVooMcSO6gvDnhOkAFMfYAI2R7VyKPBGiaIPg/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHvkg61O4zRwz4dlSmXuzmY0bDmmInKEm5KacwTTQI9ibWCMY9SODDiaMg/640?wx_fmt=png)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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