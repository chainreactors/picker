---
title: 约会类安卓间谍软件攻击标准流程
url: https://mp.weixin.qq.com/s/MOtrBvmAXiizIZWfky8nfw
source: Doonsec's feed
date: 2026-01-29
fetch_date: 2026-01-30T04:01:47.026164
---

# 约会类安卓间谍软件攻击标准流程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULtUJwT9JVWT6UF1jibM2zG3MnEKnZnbibxSybw5taTz2jda6ce2FY7HZsg/0?wx_fmt=jpeg)

# 约会类安卓间谍软件攻击标准流程

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

这是一个专门针对巴基斯坦用户的针对性攻击活动。

攻击始于恶意 Android APP应用伪装成名为“Dating Apps without payment”（无需付费的约会应用）的合法聊天平台

APP运行时会请求多项权限，权限授予后，应用会显示登录界面。受害者必须输入登录凭据才能继续。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULtqAjCqXMTxVML53jxxokInC4c5MQ0E5PmicrXdzz199CpNGmDw8BMARQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULtffI9ibfOZWS5wGwgyn8LQnrdMiaNZ4YwbxKgNz8NW7ibewU9NV0Xz5pkw/640?wx_fmt=png&from=appmsg)

与正常的合法验证方式相反，账号密码被硬编码在应用程序代码中，并且不经过任何服务器处理。这意味着应用程序和凭证是同时发送的，比如在一个平台聊天的时候，黑客给受害者发了一个apk，和一个账号密码chat+12345，让他登上去会有好玩的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULtgiciaicVNlTvuh7o0nwlhOd5QteTmCajOZdYYH66BO6UwQ36meDWiahkdw/640?wx_fmt=png&from=appmsg)

登录后，受害者会看到14个女性个人资料，每个资料都包含照片、姓名和年龄。所有资料都标记为“已锁定”，点击其中一个资料后，受害者需要输入解锁码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULt1cdyFvClhdUXMmlzxLJWo1SGdibsE66UDaVtjxROUCq5zLtbCtquZVA/640?wx_fmt=png&from=appmsg)

这些解锁码也是硬编码的，并未进行远程验证，这表明它们很可能是事先与受害者共享的。

每个个人资料都关联一个带有巴基斯坦国家代码（+92）的特定 WhatsApp 号码。

这些号码写死在应用程序中，无法远程更改。这表明攻击者要么拥有多张巴基斯坦 SIM 卡，要么可以通过第三方供应商购买这些 SIM 卡。

使用本地号码强化了这些个人资料是巴基斯坦真实用户的假象，从而增加了诈骗的可信度。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULtyO8rH6ibmVbviah0qrEsLBvGeNHibmLjzChdBRR2TEWRguFj4a9aaVFsA/640?wx_fmt=jpeg&from=appmsg)

输入正确的验证码后，该应用程序会将用户重定向到 WhatsApp，以便与这些号码发起对话，这个时候，对面很可能是ai在跟他聊天，或者攻击者有空就跟他聊上两句。

当受害者使用该应用程序时，甚至在执行登录APP操作之前，这款间谍软件就已经在后台运行，并悄悄地监视设备活动，然后将敏感数据发送到攻击者服务器上了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULtXd8Fb6X7albwS9Y9VYxym10NxYRrWWogs3hI3ROeuszwOPEOiaP7FzA/640?wx_fmt=png&from=appmsg)

除了初始数据窃取之外，该恶意APK还会进行主动间谍活动：

它会设置内容观察器来监控新创建的图像，并在图像出现时立即上传。

此外，它还会定期执行每五分钟扫描一次新文档的任务，以确保持续监控和数据收集。

初始数据泄露包括设备 ID、以.txt文件形式存储的联系人列表（从应用程序缓存上传到 C&C 服务器）以及存储在设备上的文件（图像、PDF、Word、Excel、PowerPoint 文件和 Open XML 文件格式）。

相关c2还关联了ClickFix攻击活动

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULtev5osMibnBJEWD2VvLxK5bNmjTG15Eicib2zibrLYXnesFxa57Uiak9wHibw/640?wx_fmt=png&from=appmsg)

让你直接按照他的操作，复制恶意命令然后运行。

这个操作的受害者，每次都会跟黑鸟说，在按他操作的时候总有一种不对劲说不上的感觉，但是最后都会按照他的提示一步一步操作下去，然后木马就被下载回来，电脑就被远程控制了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULtvhxSkwcWibgicibnOoTErKgMWbibhzKPAbSx8kdnU799gfZnjSs7ujZEuQ/640?wx_fmt=png&from=appmsg)

还关联了WhatsAPP账户的设备绑定类欺诈攻击

受害者被诱骗加入一个伪装成巴基斯坦国防部官方渠道的社区，方法是扫描二维码，将他们的安卓或iPhone设备连接到WhatsApp网页版或桌面版。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULt8lXiaLuibm6ePhtaJfgylOGpqriaoH3YR8yhPaKTGMDxUR6DPdqXky2ibA/640?wx_fmt=png&from=appmsg)

类似给你个二维码，让你用微信扫描，然后你的微信被别人登录到电脑一样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpKrFIS5sqtnwtmwzhyLULtraMY32ReY9CS8ka6FDHTf2AErMtRssKUVfNYnCKAC2bwx85xHYfSKQ/640?wx_fmt=png&from=appmsg)

原文链接：

https://www.welivesecurity.com/en/eset-research/love-actually-fake-dating-app-used-lure-targeted-spyware-campaign-pakistan/

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