---
title: Coding Plan 如何刷 CD
url: https://mp.weixin.qq.com/s/AZIHU3xPW9wwvZU1j3sV5A
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T06:01:42.306968
---

# Coding Plan 如何刷 CD

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LjdkpgSF7PdXSFKkUu62YU202xXjpCjl3fU2OZXEgtaphQ7l9Y9gjAooezOolH1sNdebmm3GichJARXoxcSib87RyG0ibPG768icfFnSoVaPSeQ/0?wx_fmt=jpeg)

# Coding Plan 如何刷 CD

原创

hyang0
hyang0

生有可恋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

游戏中的CD，是指技能冷却时间，英文单词：Cooldown

Coding Plan 的刷新是5小时一次，当启动一次 API 调用就会触发计时。5小时内的Token耗完后，需要在5小时后才能用。这就是所谓的5小时CD时间。

如果你是纯手动触发，可能是这样的，早上来了开会，上午开完会快11点了。上午如果用超了，需要等到下午4点钟CD才刷新，可能一天就只能用一次。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PfCvehvYKW96icNQWhoFplFyRyoAwegqRMpvxibwmyWyQ0HpNHGscvUuKv81YdNGXg0aQzicuvhocvSGicommjRLVwveSZzQicmyd9Q/640?wx_fmt=png&from=appmsg)

最好的情况是上午半天用一次，到下午刷新后再用一次，一天用两次。

如果改成自动刷新，5点触发一次，10点触发一次，15点触发一次，20点触发一次。一天可以刷4次。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7Pc5lVeTuXmOU4XqmTVpEbZPl9ThbHORgZSwam1BickCm8EobPUia4y5Tf9oEe3P7ibJywyQ0SMgdY9hKrMJQ2XMPLI26OXfic70tJI/640?wx_fmt=png&from=appmsg)

提示词：

❯ 写一个定时触发大模型API调用的程序。触发时间点是五点。十点零五分以及十五点零十分和二十点十五分。一共四个触发时间点。每次调用大模型，调三次。每次延迟一分钟。提示词是问大模型一个计算问题，稍微复杂一点的。目的是触发Coding Plan的刷新。我将大模型的信息放在配置文件中，你来写代码。配置文件：api.conf

最终执行效果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PelzhS9w6EVtuulXYmGl7bUz2XTyDqwiawFcG1jrIY0F0UCtqMGXphDQDDD3Ooz19zJSXAZgiapNfBl5OzrDfqPIeKTdU1G384Uw/640?wx_fmt=png&from=appmsg)

后台将这个脚本跑着，它会定点触发 coding plan 刷新，保证你这 8:00-10:00 可以用一个周期的token，下午3:00之前又可以用一个周期的token。工作时间一天可以刷三次完整周期的token。

下面是验证环节，10:05 分触发，触发后 coding plan 刷新如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PeAYD4afjR7yb5O3zy9OqXiaUpWL5KsVbczB9NU4eqQ7LPxBHnSq5qiacPYIZJ6Y7GFXPGWP8iaoRFKQRzibtbSTtbS4dvnAGGK2kw/640?wx_fmt=png&from=appmsg)

会话周期已经到下午3:05了。每次刷新延后5分钟，怕触发时间冲突。

日志中也可以看到，触发成功：

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PfSyLwv9NnrGsCM1iasHAgiaUkvPicMBPXJgFo8u3sQXruM8SQLtVr7ljMib4hBQY7FenrqibzvC6HqqpH6ASmNicBXicf8lA5b0X421k/640?wx_fmt=png&from=appmsg)

下午15:05我又确认了一下，CD 按点刷新了，trigger 程序工作正常。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PfMtK3BltDMSrJgEcUdO9GdsYyKtIYaicje9TicRriaH4n9hicFsox9ib35NPl9eVBsG5ZfrMxibkWBnu88BTiciacBHIG88zzwnXTfUGI/640?wx_fmt=png&from=appmsg)

AI 干活还是很给力的，只要把需求描述清楚，它就能漂亮地完成。

全文完。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

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