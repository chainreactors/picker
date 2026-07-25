---
title: Redis身份认证后远程代码执行漏洞通告【已复现】
url: https://mp.weixin.qq.com/s/B68WNHqi5RiBNiohd04b3w
source: Doonsec's feed
date: 2026-07-24
fetch_date: 2026-07-25T04:59:14.104929
---

# Redis身份认证后远程代码执行漏洞通告【已复现】

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SLl77fibWWLaibmEg44M0GUAquibjwQicdtXFnbM55kuU35wrrVcDDw96icjia7y6O6MoRN8kIskZSVQAkQ1uTBNsaYX6LicQeicvWjqwXzHUNXJL5c/0?wx_fmt=jpeg)

# Redis身份认证后远程代码执行漏洞通告【已复现】

新华三盾山实验室
新华三盾山实验室

新华三主动安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmecoa.qpic.cn/sz_mmecoa_png/kJFdfNJcFJD9teZvfeRICMsEOpzlgxlfyvXYjKS4JK2cRu54fOhjuMCARwy5UrtJBXzZmpKbprvAgE0dXBdNuUJQ7LQMLV4ndoTgaibXdXyQ/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/yQjsZ8zq83vaCLpjmibq0tfSX4HJvOlKMU5W6JRKAKUCyIDknBF6ibvicZR8wjKzUicKZftuShzQso5qqU9KjGDiaOPI8ibDTNOROSy17egXiaN7Q4/640?from=appmsg)

01

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/yWSKK1skPzibT36tVa3SX5ILYicuiaEV46R4FkmNhwSics3Pobe6rCc0ha4PM4hLgcq1Qmp7icx7ZPy2OAAnz2zGibQoOVGfO2dMjtJ8ibj60seFx8/640?from=appmsg)

漏洞综述

1.1漏洞背景

Redis 是一款开源的内存数据存储系统，支持字符串、哈希、列表、集合及流数据等多种数据结构，广泛应用于缓存、消息队列、会话存储和实时数据处理等场景。近日，新华三盾山实验室监测到安全研究人员公开了一个 Redis 身份认证后远程代码执行漏洞的完整利用代码，当前该漏洞暂无 CVE 编号。攻击者成功利用该漏洞后，可在 Redis 服务进程权限下执行任意命令，进而控制服务器。

1.2 漏洞详情

该漏洞源于 Redis 流数据类型在恢复消费组状态时的内存管理缺陷。消费组用于协调多个消息处理客户端分配任务，Redis 会为尚未确认的消息维护待处理记录。攻击者通过身份认证并取得 RESTORE、XGROUP 等命令权限后，可导入特制数据，使两个客户端错误地引用同一记录。删除客户端时，该记录会被重复释放，攻击者可进一步破坏进程内存并执行任意代码。

1.3 漏洞复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SLl77fibWWLZqdq37puPstnd52TPBcWZfsWKFe04fpzENicGvdkHuFmvfPb9FhGCbOL6FebWmS3e89uiahmQ2Nb01J8l9HwiaKCnpVaFeSG44uo/640?wx_fmt=png&from=appmsg)

02

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/yWSKK1skPzibT36tVa3SX5ILYicuiaEV46R4FkmNhwSics3Pobe6rCc0ha4PM4hLgcq1Qmp7icx7ZPy2OAAnz2zGibQoOVGfO2dMjtJ8ibj60seFx8/640?from=appmsg)

影响范围

Redis 6.2.22、7.4.9、8.6.4、8.8.0

03

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/yWSKK1skPzibT36tVa3SX5ILYicuiaEV46R4FkmNhwSics3Pobe6rCc0ha4PM4hLgcq1Qmp7icx7ZPy2OAAnz2zGibQoOVGfO2dMjtJ8ibj60seFx8/640?from=appmsg)

严重等级

|  |  |
| --- | --- |
| 威胁等级 | 高危 |
| 影响程度 | 广泛 |
| 利用价值 | 高 |
| 利用难度 | 中 |
| 漏洞评分 | 暂无 |

04

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/yWSKK1skPzibT36tVa3SX5ILYicuiaEV46R4FkmNhwSics3Pobe6rCc0ha4PM4hLgcq1Qmp7icx7ZPy2OAAnz2zGibQoOVGfO2dMjtJ8ibj60seFx8/640?from=appmsg)

处置方法

4.1 官方补丁

https://github.com/redis/redis/releases

4.2缓解措施

1. 新华三安全设备防护方案 新华三IPS规则库将在1.0.415版本支持对该漏洞的识别，新华三全系安全产品可通过升级IPS特征库识别该漏洞的攻击流量，并进行主动拦截。
2. 新华三态势感知解决方案 新华三态势感知已支持该漏洞的检测，通过信息搜集整合、数据关联分析等综合研判手段，发现网络中遭受该漏洞攻击及失陷的资产。
3. 新华三云安全能力中心解决方案

新华三云安全能力中心知识库已更新该漏洞信息，可查询对应漏洞产生原理、升级补丁、修复措施等。

05

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/yWSKK1skPzibT36tVa3SX5ILYicuiaEV46R4FkmNhwSics3Pobe6rCc0ha4PM4hLgcq1Qmp7icx7ZPy2OAAnz2zGibQoOVGfO2dMjtJ8ibj60seFx8/640?from=appmsg)

参考链接

https://github.com/berabuddies/redis-poc

https://github.com/redis/redis

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fdVgrOseV9q50ZZefBwS0aXL4JR2PlQH3EtlogiaManMaULXfInBOn6hW7lM1EZg8tSAxd4sJkCiaVEh2kuWIw2A/0?wx_fmt=png)

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