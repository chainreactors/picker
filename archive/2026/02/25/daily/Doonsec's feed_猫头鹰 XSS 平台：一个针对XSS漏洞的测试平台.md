---
title: 猫头鹰 XSS 平台：一个针对XSS漏洞的测试平台
url: https://mp.weixin.qq.com/s/yjsS7Er173vo9hKvhomcwg
source: Doonsec's feed
date: 2026-02-25
fetch_date: 2026-02-26T04:10:27.156835
---

# 猫头鹰 XSS 平台：一个针对XSS漏洞的测试平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicK09r6oCdahVdvUZ0ZpNcqgAgqbSEzic5cMGwDlv4NxQyzH22uGBDNXgNUkzK8dI0xk8Bs57zh2hJt3yMaibKkZGfA2dTHWKRVqE/0?wx_fmt=jpeg)

# 猫头鹰 XSS 平台：一个针对XSS漏洞的测试平台

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[Donut+SGN 利用微软签名进行静态特征混淆与终端检测规避](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486480&idx=1&sn=91080cabf64e334fb3151852df260b99&scene=21#wechat_redirect)

·[FnOS GUI Exploit Tool:针对 FnOS 系统的综合漏洞利用工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486470&idx=1&sn=be6ac8da8d54423b050f7ab7e596659b&scene=21#wechat_redirect)

·[ManSpider：一款黑客内网快速敏感信息搜集工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486462&idx=1&sn=13d367de0d7867608564ca9827a012b9&scene=21#wechat_redirect)

·[Web-Check：一款全面的web网站信息和漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486451&idx=1&sn=1e91aeea9f174b4331a580e28e5c273f&scene=21#wechat_redirect)

·[Super Xray：一款基于 Xray 的漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486414&idx=1&sn=e344d3236ff2d3e83bffef09c1f7e1f7&scene=21#wechat_redirect)

·[upload\_forge：CTF利器-文件上传漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486388&idx=1&sn=f7c43e484275521abb27f417a26ddb60&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJgIVeLKXibJvjhY8hgiakJk4ep5rolJoQ1icLgBGn4j1pwCQib6D99Koufmlqnu4oYpibfZXlOLiaYQ0UdJwLicDfECo8DVByMSwHp4Y/640?wx_fmt=png&from=appmsg)

    猫头鹰 XSS 平台可实现基础信息采集、Cookie 与网络存储捕获、键盘记录、剪切板读写、浏览器密码捕获、标签欺骗、禁用密码输入框、WebRTC探测、页面画布截屏，支持附件功能，适配 SSL 证书水坑、闪电水坑等攻击场景，可检测 Redis 未授权访问、Java 版本信息，兼容 CVE-2022-10270 漏洞利用。

    此平台也是一款用于红队测试的工具，支持基础信息采集、Cookie及存储捕获、页面截屏等功能。它具备SSL证书水坑与闪电水坑攻击能力，还能检测Redis未授权访问、Java版本及CVE-2022-10270漏洞。平台支持bot推送与项目管理，适用于安全研究与漏洞检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**来源介绍**

在线地址：

```
https://owls.ad
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicK4UYS4Gsx4o5ibibpiceCCzM7j1jtS1JUCBNCPzFAybLGXgk7FaTERdzibuA1ngN6VRqJYIHRn6KBibIQ8KuV0mNXcYTJYVlUubvzA/640?wx_fmt=png&from=appmsg)

    注册邀请码：

```
onYrIJFpue2S4eXlOWA0lHZdWqwZTw2Emzyi4fcjVPFhzO4cSWPK4jqPpEDE09kg52sLJmUznFiJ6FIxX7bKYZ78O1ovAcDvTSRKx3BytQuRwjSTPgKfQdKafJ2ARouVcn3MU1S2wakaUON75W2jmhAEDKM8f7ZyBBhntJCAAdZpWZ6VtHav6p37CLCgZmdU82AyYIPECydvRqJgOGuTwthoXQOZCLOUM9Min7mI6JAYb6kG
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**功能介绍**

登录进入后，控制面板如下：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJkZib0VdSGBJa5nSKAak3pAvIWJhdibQ8mhFPSpa0CYrOnvUvuXBg5XUfmbE7icCLAiadABsa6J8kNZgZOnYLePujmGCqEgmlxuw4/640?wx_fmt=png&from=appmsg)

    模块管理界面如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLqHJ1o1hhafl5zCibaETWzgu8RniaOBicrrcQsPqo9t5mS63ptROu6iaZbVrB7NcjuzicxhnBcYaiceO2552oCygYp8SSfqTic6uibkn8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKY2OgR0HGBVibkQnDqMTwkzmDyJiccKtjSVv7RfoO8Kqyx7vxawWkLvLL78Fia9hARoGVyZpVbs7A0iaXv237INIWRiaCHA7x1MSnY/640?wx_fmt=png&from=appmsg)

    所有模块如下：

```
1、安装密码控制：禁用密码输入框会诱使用户下载密码安全控制软件。2、标签标题图标具有欺骗性：当前页面处于隐藏状态时，修改标签标题和图标，以吸引用户再次点击以激活标签3、密码管理器陷阱：浏览器会自动填写用户名和密码4、WebRTC 内网探测器：检测内部网络上的活跃主机5、登录钓鱼：该系统伪造登录页面，然后获取用户的表单信息，从而窃取用户的帐户和密码6、设置剪贴板：将所需内容写入用户的剪贴板7、剪贴板日志：获取当前用户的剪贴板内容8、键盘记录器：记录用户在当前页面上的键盘输入，每 3 秒发送一次，每累计 30 个字符发送一次9、SSL证书水坑攻击：伪造的已过期 SSL 证书诱使用户安装钓鱼木马10、闪电水坑攻击：利用 Flash 技术创建钓鱼页面，诱骗用户下载木马程序11、Redis 未获得授权：检查 Redis 中是否存在未经授权的访问漏洞12、Java 版本：检查目标计算机是否具有 Java 环境及其对应的版本号13、CVE-2022-10270：该模块用于检测 [AweSun Remote Control] 远程命令执行漏洞，漏洞 ID 为 CVE-2022-10270
```

    并且支持支持自定义模块：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIeGY1y4Kr3bRs7DI8W5ic42m7ic5o484FmiasjLuUP67V0vGZZhIU7256yvwRFZXeMUPStAt0lhraxH0FrbEAQOd0ZyIMAf6iaaT4/640?wx_fmt=png&from=appmsg)

    支持Bot推送：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLywnCC1HjtYgPCuEAttZicA1OXwIIkOxBLsE0ugIEnIxMYQtY6E15LTQFk9FKehxoscq7PTjbwXH1jyZcKLQ5ZQL6FibiaGtIDpw/640?wx_fmt=png&from=appmsg)

    创建新项目：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicI5jZhDHQBpVBZQEU0nhbpDyUrCFPmNX6bibCVdlPWCrgCFlibIqEpKfj1Leib92IdeMhr5tVXgqHc6kiba5FVATnjMbvQfKicChz2A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLJAMuECUAiaAuYGbaH4zHMUX4nKYKWe94iabgISFGUiasfZicvibT3F1lTALjx4BfCf2GX0IUnPp1bWcNUIE5ibvJqH6d4oLIzdKiarc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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