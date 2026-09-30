---
title: Master V3.0 专为后渗透而生-结合agent首发
url: https://mp.weixin.qq.com/s/I9qWdYLFGJ4-ErfW7MTauw
source: Doonsec's feed
date: 2026-09-29
fetch_date: 2026-09-30T07:41:19.833481
---

# Master V3.0 专为后渗透而生-结合agent首发

# Master V3.0 专为后渗透而生-结合agent首发

巡音安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# **Master****面向高复杂度内网的 C2 + Agent 平台，覆盖 Windows / Linux多协议，并具备多层级联与精细化后渗透****能力，接入专属agent实现可以在edr/xdr环境下自动化隐蔽性渗透**

Web页面定制专门的安全告警功能，未授权的端口探测和密码爆破均会在安全告警中显示同时记录ip，支持白名单接入，降低被接管主机和反制的风险

![](https://mmbiz.qpic.cn/mmbiz_png/kEiaw3nqIkVZ7KzNShIsBEwcrckyWQUgewib7tBP6cz9zHnN3zr121ia2VJ2FTpdG70pFzxXZNwWVBB1R22QVUib70IH6EGhyMQq2pSRFaI1ulo/640?wx_fmt=png&from=appmsg)

## **AMSI&ETW hook**

**支持多种amsi和etw的处理逻辑，包括硬件断点处理，可以在HBP info查看详细信息**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEiaw3nqIkVYpYehFoRczxtty4EhuevNtyTHjYFAAHMGKv6X1FbqaHhZro6tAFx1ZIj8mlic1fQsu3W0V7aY1KJ37yNjVajvUp0kwhgMgXjE0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEiaw3nqIkVZaPWZWdGZxnV1HUg6LFL1nmaonhPc80lRhMhqzrPjZNpJ7JvZ5Ozo2hI4L8sTdBVGxEIp65IbZGJne01WKTkAoa2gHsV0M3lg/640?wx_fmt=png&from=appmsg)

## **权限提升**

**内置Potato &&UAC提权，使用Potato时会检测ASMI的情况，如果未开启会禁止加载，均支持命令启动和进程启动，进程启动通过com运行更为隐蔽，UAC范围支持win7-win11 winserver2016-2022**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEiaw3nqIkVaibAL2Q7A707VStJs7JmhEaucsXibMb29fWHpVH3QkqMWImWDC7zPk0XmAnuvPsIR4UO5dITjkbDsBShvNBfic8nznMPTQC5l95A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEiaw3nqIkVbNvC50fssdf3NKw5lTUK45GpzsL1BPUuVGP0sia5mQfT6YDFNbFfPXNkxV9g0ib1MHxBm9qRYRrKm312r6kEF7iccaDu3GVyeZpc/640?wx_fmt=png&from=appmsg)

## **Bof命令执行**

和常规bof不同，通过踩踏的方式获取dll内存运行，不再本进程内产生可疑内存

![](https://mmbiz.qpic.cn/mmbiz_png/kEiaw3nqIkVZTcZT4iaYKRSqA665iaocSibxuic4SvcDGlONnedVmpQ8h8VG9YFhfCQrEQJlczY8tyBbIEYiaYb4LEmzodF4LflpWic0dMFqA8OdRA/640?wx_fmt=png&from=appmsg)

## **NetLoad**

**支持加载自研的net程序集进行更复杂的专项操作，同时内置多类amsi的处理方式，降低告警**

## **凭据收集模板**

**支持自动话处理目标机器的凭据包括但不限于主流浏览器和聊天工具，通过net程序集的方式稳定运行，**同时自实现SAM /LSASS dump****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEiaw3nqIkVaWeibG7rFHXNjSsYrsprMHyjxAaK9jlZL6X6a3Fx3H0zibJjw5mXejpJ0UVxibp0K7Nq7drFiczPVEv9NyLKjq5ZQdnqfMwLek4B4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kEiaw3nqIkVbAcqzKXx244SNHAHbUnLNP77iavhkqcloQshuMPH1nmnvQn1I0YDDxR0UwicQ8DfhgjOQwHPsGuNptx4QfT4eGnG1o3fpmarD2Q/640?wx_fmt=png&from=appmsg)

## **载荷生成生成**

通过ollvm和可选参数实现多类别加载，支持自定义白文件，同时新增三类白利用，可以断链无感上线，实现生成即免杀

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEiaw3nqIkVaJaqH8RyEibgE4I8JZV3hMP1ZODQRtTVvz5egoESNZQuicYhp8lDLVoFS1vIu5VgKbiaXUyCbsrNTHFHJrxmMWpsg5icx1mRgUnZk/640?wx_fmt=png&from=appmsg)

## **进程列举&&steal**

**支持通过beacon下发stealtoken的功能， 可以用目标中的会话进行命令执行，同时优化stealtoken的windowsapi逻辑，更难以被检测，支持通过windowsAPI以token的权限向域控直接枚举内容**

****支持滥用rdp或者域管令牌，无需额外处理LSASS凭据，降低暴露风险****

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEiaw3nqIkVZJPbhicOV30VjoB3IZEJI2QziaLXory1iaqvp1LeTd3LCeOyjAh2cY9hOdWmJXSDX7K5yicHF3UKz0ldDrXM2CGL8tIKHK1UKF7icE/640?wx_fmt=png&from=appmsg)**

## **S****MB****内网级联**

**支持多级调用，可以处理5层以上的级联，对于内网完全不出网的情况可以通过正向＋smb/正向agent  级联**

## **多功能性**

**支持HVNC,屏幕监控，端口扫描和键盘记录器**

![](https://mmbiz.qpic.cn/mmbiz_png/kEiaw3nqIkVYj4xE6ias7HMyB0OLeEPZ9fUkgTafOpe6QS5BO1fsNtGtibhQ51TWOibgaAW5jRUqHAZviakF1muQP77pAdUsncoFQfzicLY1lVQKY/640?wx_fmt=png&from=appmsg)

## **登录告警**

**登录失败ip实时告警，支持白名单登录，可以自定义封禁ip，同时减少反溯源风险**

## ![](https://mmbiz.qpic.cn/mmbiz_png/kEiaw3nqIkVbpOlyF6cXAUsEBpMIlu9g3LQrp9qwg4LstdHuWtkEJ1ia01xTSA8YfP2Zx6hw1H4AsdHy71aH7PWkbb3KOef7oKVobcoPia0U0Y/640?wx_fmt=png&from=appmsg)

## **聊天会话 / Event Log**

支持操作员聊天、上线、任务摘要

![](https://mmbiz.qpic.cn/mmbiz_png/kEiaw3nqIkVaaGyqqM78dc8icmFdokPmupC4NoAlQ1npvvZ4aNUCY7Q6XFGaAqn3sQx6DhcDR5iaCgKu6Kbmh0LPRvaBBe8ntb3ucb0QjmrhIw/640?wx_fmt=png&from=appmsg)

## **Linux正向载荷**

**NFQUEUE需要root权限，支持全端口复用，包括53，123，8080**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEiaw3nqIkVavaWias2WGE5Ntwu1ZCvnCicqw6Hbx6jibweIHkVicfEbF4uPwsxQQtTF3QsiaQeeTz4xNjIk97o9sQyDN0AsumLMX8iau5Aic81mVib8/640?wx_fmt=png&from=appmsg)

## **Linux****elf命令执行**

Linux 会话用 elf 在目标上跑内置命令对象，不经过 shell。对象在 teamserver 的 resources/elf/，只支持 linux/amd64

![](https://mmbiz.qpic.cn/mmbiz_png/kEiaw3nqIkVaHDxFuoibS0ss1ASjZPCK9wI4L0qnwRUjw1GEEdfWHZibtiaV9S1ouicSS9CegLzREOJDb9o9XaL1SV2UKjAA4NDicOJUaL02tAwWs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kEiaw3nqIkVYic5ACbJrSD8Ccp9iaF6qcCLOZeSstYI6XMj1U8AEiaXbydiaC0YUIL2aKkI3hcwbUPIJdr31WDKtdGfNNGQcvJSu2JrwbjHKoLQ4/640?wx_fmt=png&from=appmsg)

# **权限维持**

支持服务，计划任务和PAM软连接，同时内置进程锁，可以选择性开启

![](https://mmbiz.qpic.cn/mmbiz_png/kEiaw3nqIkVY2HNwhiceTMmflauWibzslaapQ8hWh4ibahRcLaiaWpTYjSCeBZzOJk6dwessTaLGHyiapaAdibGjv3r0Y37bqzA49mIM8JmcZLjLTQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEiaw3nqIkVZibkzU5TpqGd8pQeSlNUtkeqbybibrGjTpt1tZUic24VYlDf2e05YWDmJ1AX8KTBsIJoGwmDXPHEWSiaKgn9eMGWmiavMRqh1GUqK8/640?wx_fmt=png&from=appmsg)

支持安装rootkit:(文件隐藏，端口进程隐藏，访问指定端口反弹shell，普通user权限提升)

![](https://mmbiz.qpic.cn/mmbiz_png/kEiaw3nqIkVbcyZasRlf1NeTDpC58vhxrzVicg2icxDgRVe8ml0gu8Kyy3uQGnB5ibWMm0aD2TIVt78Vbgan6TflaD0rDmBd2XZD4gfcyEUUfwA/640?wx_fmt=png&from=appmsg)

## **MCP&&AI自主化渗透**

**配置了专门的skills和ai自动化的规范，严格按照opsec进行内网渗透，不降智，命令都通过bof执行，同时专门适配好bof规则，支持ai自动编写bof然后运行，支持按照格式编写对应的pe&&net程序集运行，同时内置专门工具通过隧道进行内网探测，梳理内网架构给出后续思路**

 更多请咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kEiaw3nqIkVaWFCbictI4FcgAxfKXoVSgSZttNDfLnZicNATRY7ibQqhdwvBz4X0gdDPjmH4xbRNU6TnnZpUZKoUR59Bm8ADZSC7NZy1215UO6o/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/T8lYDMMxHI3Bsq8XmBHicqLvNslzBoN6YJicxRKhjfJFWMnuQ0tBY4AZqJ9XoAhCUvknJkdic911PIdibPFicaBgXqg/0?wx_fmt=png)

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