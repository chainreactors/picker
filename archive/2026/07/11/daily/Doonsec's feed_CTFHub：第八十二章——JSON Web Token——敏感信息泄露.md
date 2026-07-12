---
title: CTFHub：第八十二章——JSON Web Token——敏感信息泄露
url: https://mp.weixin.qq.com/s/A83OltF-p_six1ErfhQV1g
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:07:09.935709
---

# CTFHub：第八十二章——JSON Web Token——敏感信息泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TkbqemjbpIqFtNXDiaMtQPqeibHwyTr3NJYrRUpLQcEnWhPRyn0RC2fZD6Ec0qOOZRtZg1eVPtvG2tAkzRlQuR0ErILbfmJbyB82rq6canOO4/0?wx_fmt=jpeg)

# CTFHub：第八十二章——JSON Web Token——敏感信息泄露

原创

君陌社区
君陌社区

君陌社区渗透安全笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CTFHub网址:【https://www.ctfhub.com/#/index】

登录账号
点击技能树

选择“web进阶- JSON Web Token-敏感信息泄露”开启题目

题目描述: JWT 的头部和有效载荷这两部分的数据是以明文形式传输的，如果其中包含了敏感信息的话，就会发生敏感信息泄露。试着找出FLAG。格式为 flag{}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIq8WlPdnmK5Us9dlTs6aiaDScxmWnmn5nibql46BYib7U33FYYd8evdPAhhjPfRWhYlKNJNPvHtaAqxMtl4Kte5f1xOakK2B8QGvc/640?wx_fmt=png)

点击打开链接进入靶场实战练习环境

输入用户名admin密码随机登录

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIoPlzKNF9YY6WzhrtQ144icfkQyxvcFQBdnZwFUGZQqgEibTFwGqLaDaKDTPQ3mP9owG7U94V1iaicle2KPVYgAuUic9klWwicJnEYy0/640?wx_fmt=png)

打开Yakit截获数据包，注意到token中内容似乎是加密编码后内容，这就是一个JWT由点号.分隔的三部分组成的长字符串，格式为

```
Header.Payload.Signature
```

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIpWZO4lohNp0zjiaby4ClykB1qey1QG6r9gMGAWI84hkH1FxhT00tw4iaA4OFal4S3OJ1guQNtmTPzVc8zw2wUU4EichoGur7KGXk/640?wx_fmt=png)

选择复制第一部分，用上方的解码工具解码

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIrSvXykibvgzibQnbooSbbwaVNtG1kyyQfpribn731S8ibyw9fxLLBDO9jJtvYcZ98HYADbSCvCA815aSj02hs5pfnkf93UI9xYZpY/640?wx_fmt=png)

得到明文数据

```
{"AG":"e73a2eae07f7300}","typ":"JWT","alg":"HS256"}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIrUricKtItPZvvy8hgjxuTDJRR8ILRSeblKUUYonfDH7q4t2xrz4tibaHEwZ1W1ic5mdeNafkpXCbvtq0fXwia5dI95724kP0ROlhw/640?wx_fmt=png)

在选择第二部分解码，得到铭文数据

```
{"username":"admin","password":"123456","FL":"ctfhub{04ed80bc8"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIpHOKcLeNocX1cMFSAjdvKxM4BWtziaQXAVdN8n4hzXcB39c9VicKVvPm1SmE8BILCKshO0wc5OcfwYzDEGq3jxwiacdkeJesXfn8/640?wx_fmt=png)

将两者拼接后就得到了flag数据

```
ctfhub{04ed80bc8e73a2eae07f7300}
```

上传flag数据完成靶场实战练习

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIq5IP3QNLzh361LHUR23ibalBsWhKdrMe4eic99fibOfR67DLY0292no3vLso7AibCc7A9t22cXH1d2mWwU2l4837ice3HArkxut4dI/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/csuE9m26HkI8taS28gIOWsc8KaibxmZ9HDovmlvGsicEnJuSw0Ricdq3KibbTUnRicEO0NohDyczWdgJBOe3RWF1tQw/0?wx_fmt=png)

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