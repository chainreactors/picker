---
title: 国际刑警DDoS蜜罐意外曝光：安全研究员意外逼停执法行动
url: https://mp.weixin.qq.com/s/MwkZTTSEvMfhFnZnlvOg-Q
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:34:03.965746
---

# 国际刑警DDoS蜜罐意外曝光：安全研究员意外逼停执法行动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDricUTO7e4s656jibxp0LK0IMNZsib6JhVQxRzibON8cXwFznAuTibG8VChOt3f2QVZEZib3MG8gKaUT2bZzarjGAkjmycqbMx3Np8Vg/0?wx_fmt=jpeg)

# 国际刑警DDoS蜜罐意外曝光：安全研究员意外逼停执法行动

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026 年 4 月，一位名为 Lina 的安全研究员在个人博客上分享了一段令人啼笑皆非的经历。

她在调查国际执法行动时，意外发现了一个由多国警方联合运营的付费 DDoS 攻击服务蜜罐 (honeypot) 网站。更戏剧性的是，当她开始深入研究这个网站时，执法部门竟因恐慌直接关闭了整个秘密基础设施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpFnFNZcVjCN8iczpt5kic6ZiagexP3fKGbM8cpUeIprk2DdBdvWNIo6QuR4BumibtfibR9EZ8Xp30TEco1DicTJD8KEcicdSu3ztpxmQ/640?wx_fmt=png&from=appmsg)

## 什么是 Operation PowerOFF 行动

在了解整个事件之前，我们需要先认识 Operation PowerOFF。这是一项旨在打击付费 DDoS 攻击服务的大规模国际联合行动，参与机构包括美国联邦调查局 (FBI)、英国国家犯罪局 (NCA) 和欧洲刑警组织 (Europol)，整个行动主要由荷兰警方负责协调。

荷兰警方不仅主导协调工作，还实际运营着这些行动所需的基础设施。多年来，该行动已成功查封约一百个相关域名，并在全球范围内实施了多起逮捕行动。

Lina 在研究 Operation PowerOFF 行动的过程中，偶然发现了一个名为 cyberzap.fun 的网站。这个网站虽然算不上完美专业，但足以以假乱真。它完全模仿了互联网上成千上万的盗版 booter (攻击服务) 网站的样式，甚至还设置了 robots.txt 文件、网站地图、搜索引擎优化友好的元标签等所有真实网站用于搜索引擎排名的必要元素。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpW3WEU0rLEyMIewdkibG9hkjm4DVPCJvWP62Zve3DJIibndiaGx461RUALuYImpStIQrWQEibdZBqzHOdVWu5Gb6vU7D1e6cOy41U/640?wx_fmt=png&from=appmsg)

然而，一个细微的破绽暴露了它的真实身份。荷兰警方特别偏爱使用bit.nl作为服务器托管商。

当 Lina 检查该网站的 MX DNS 记录时，发现 Cyberzap 的邮件服务器正是使用bit.nl提供的服务。

为了进一步验证自己的猜测，Lina 决定注册一个账号。她使用了一个带有明确研究性质的邮箱地址 conducting-research-hello-operation-poweroff@lina.sh 进行注册，以此表明自己只是在进行研究而非从事网络犯罪活动。

令人惊讶的是，网站竟然发送了一封真实的激活邮件。邮件中包含一个带有令牌的激活链接，以及一个可以手动输入的激活代码 416296。注册页面还配备了 turnstile 验证码系统，进一步增加了网站的可信度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqUicIkgiabAziaopCLtaT91FMmvibJwIDStmcCfBibENXicPwBUX1Yog3zjVZUxicFibXWhXjX8dgk2NoKsMGySEdGIhicEeth6dFbzJicY/640?wx_fmt=png&from=appmsg)

登录后的仪表盘虽然略显空旷，但依然具有欺骗性。它包含会随当前时间更新的虚假网络速度图表，以及一个虚假的已连接僵尸网络计数器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpZribXWmtMxjogYAvrv6AsvJ9hpMVuaBaHVUtfw7Kd8VUiaz6iaehVKuvX5bJsFYdpothHiaqficfbYj8bcg9mloSVfm0qicVHV1mhU/640?wx_fmt=png&from=appmsg)

Lina 想知道如果下单发起攻击会发生什么。为了避免引起不必要的误会，她输入了一个明显带有玩笑性质的域名作为攻击目标。

i-know-this-is-a-honeypot-and-that-this-doesnt-trigger-a-real-attack

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqhOz1Bxia2viaQqF9BWCibRXiaDGltBW8X44XHQriaynWlKicM8Cw9z1dPsRtJ4loLgqEKekTEsA3J3IREvRoyh2OJA6zNeqfbhGXG8/640?wx_fmt=png&from=appmsg)

在攻击配置页面，用户可以选择多种攻击类型，包括 HTTP GET Flood 等。攻击参数可以灵活调整，包括攻击时长、攻击功率等。网站提供了三种预设套餐：

* MY FIRST DDOS：每次攻击 8 美元，10Gbps 带宽，持续 1 分钟
* THE GAMER：每次攻击 14 美元，50Gbps 带宽，持续 5 分钟
* THE HAMMER：每次攻击 66.50 美元，最高 300Gbps 带宽，持续 1 小时

用户还可以选择额外付费选项，如 IP 地址轮换和紧急停止开关。支付方式支持比特币 (Bitcoin)、门罗币 (Monero)、PayPal 和信用卡。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrw08eqlicicibjEEqctzDNn89KgWpGIvxjAQtZzqcRkd50LRjvnjxWjgdEERZUX9ic7dNgiaaEZSpFrH5fp7etSsqfszJNONM8fxIQ/640?wx_fmt=png&from=appmsg)

然而，无论选择哪种支付方式，系统都会在加载几秒钟后显示支付错误信息，提示用户支付处理失败，请重试或联系客服。在攻击历史记录页面，只会显示支付失败的记录。

这种设计的目的非常明确。执法部门通过这种方式收集试图购买 DDoS 攻击服务人员的 IP 地址和邮箱地址，并将这些信息作为证明其犯罪意图的证据。

除了 Cyberzap 这种秘密蜜罐网站，执法部门还运营着另一种类型的公开警示网站。通过网站关联，Lina 同时发现了netcrashers.net这个网站。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrWdOPdxnJfFDwQO0cXewaMry1XeM4icmhw7CqlWLRPO1rCdfa5dQMxY0ecxD7WoicZZ9xHuQrSAvf5bqlYd6YibicLAgO0TS8w0sk/640?wx_fmt=png&from=appmsg)

与 Cyberzap 不同，Netcrashers 网站看起来明显更加虚假。它宣称可以 "摧毁所有网络"，但当用户点击网站上的任何按钮时，会立即被重定向到一个警方警告页面。该页面明确说明这个域名由荷兰警方创建和拥有，并警告用户 DDoS 攻击是非法行为，会产生严重后果。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpZQMyW0JvJdFTlvlutZbTlHtKwXxJ4xiaumWQribLy1xLRVI1C20wBh10beicJEDkNBOUFaUc7WbJtdgGWHUIiawbdzh26EGe02O4/640?wx_fmt=png&from=appmsg)

这种网站显然是针对青少年设计的。当一个青少年搜索 DDoS 攻击网站并点击进入时，会被带有警徽的警告页面吓到，从而关闭网页放弃尝试。

就在 Lina 深入研究 Cyberzap 网站、测试各种功能并截取屏幕截图时，一件非常有趣的事情发生了。执法部门竟然直接关闭了整个网站。

当 Lina 再次尝试加载页面时，她收到了 401 未授权访问提示。网站被完全锁定，要求输入用户名和密码才能访问。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDooeO0vgRLwu8b0FoeuhuUo0ickUDPaaTZ1bHqgN2cQxZm1PgtrUKia5MPgECYzvjFPgIdrPcbZbianKHCE229mVVlUiblScJRxrE4/640?wx_fmt=png&from=appmsg)

执法部门显然看到了 Lina 的邮箱地址，意识到有人发现了他们的秘密网站并正在进行调查。他们不仅关闭了 cyberzap.fun，还关闭了另一个完全未使用的域名bytecannon.net，该域名同样显示 401 未授权访问提示。

值得注意的是，那个公开的警示网站netcrashers.net仍然保持在线，因为它本来就是设计用来与执法部门关联的。

Lina 及时将 cyberzap.fun 的主页进行了存档，存档地址为https://archive.ph/IS0k6。

这一事件引发了一个重要问题。执法部门花费大量资源运营这些蜜罐网站的真正目的是什么？

netcrashers.net网站上的标语提到，执法部门会以公开和秘密两种方式打击网络犯罪。我们在这次事件中正好看到了这两种方式。Netcrashers 是公开方式，而 Cyberzap 是秘密方式。

Lina 在查看自己的攻击订单时，注意到 URL 中有一个订单 ID。她的请求是第 15 号，这意味着该网站总共只收到过 14 个攻击订单。而且这些订单中的大多数很可能是执法部门自己测试系统时产生的。

这表明，抓捕犯罪分子可能并不是唯一目标。通过运营这些蜜罐，警方在网络犯罪社区中制造了怀疑和恐慌。如果有人想要购买 DDoS 攻击服务，现在必须担心这个网站是否是警方的蜜罐，是否正在记录自己的 IP 地址。执法部门希望通过这种方式让人们完全不再信任这些服务。

Operation PowerOFF 行动在过去也采取过类似的做法。

英国国家犯罪局在 2023 年 3 月曾发表过一篇文章，介绍他们如何通过伪装的 DDoS 网站渗透网络犯罪市场。这篇文章现在已经无法访问，只能通过存档链接查看。

根据域名注册信息，cyberzap.fun 创建于 2025 年 4 月 3 日。互联网档案馆在 2025 年 7 月 14 日抓取过该网站的快照，当时网站还是空的。因此，这个网站实际启动的时间值得怀疑。

黑鸟:付费DDoS攻击服务水太深。

往期:[APT29曾经最隐秘的武器：目标机器运行的定制化间谍木马](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186574&idx=1&sn=3ee6eff7d3195af7bf9e10f8f0051298&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

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