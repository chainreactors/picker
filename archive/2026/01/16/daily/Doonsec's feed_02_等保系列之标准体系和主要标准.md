---
title: 02_等保系列之标准体系和主要标准
url: https://mp.weixin.qq.com/s/_c31xG3ZhLosmhYcaipGcQ
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:22:22.934408
---

# 02_等保系列之标准体系和主要标准

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnhNmmMKx2SfbFkgLCDv7NfFp4ibgNGvCEiakl1Vj2HMf69CicqGIXdxlTg/0?wx_fmt=jpeg)

# 02\_等保系列之标准体系和主要标准

原创

0xSecDebug
0xSecDebug

0xSecDebug

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsH6erTSwrZSIKcuK6VVEYct0sl6ytILrApoxzCMTpkTVZPDfCOVh6micjnuCEHzeTRWM7sGr3T2BKw/640?wx_fmt=gif&from=appmsg)

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。

## 主要标准

网络安全等级保护条例(总要求/上位文件)

计算机信息系统安全保护等级划分准则(GB17859-1999)(上位标准)

网络安全等级保护实施指南(GB/T25058)

网络安全等级保护定级指南(GB/T22240)

网络安全等级保护基本要求(GB/T22239-2019)

网络安全等级保护设计技术要求(GB/T25070-2019)

网络安全等级保护测评要求(GB/T28448-2019)

网络安全等级保护测评过程指南(GB/T28449-2018)

## 标准体系

    等保2.0的标准体系是一个全面的网络安全框架，旨在为网络运营者提供一套完整的安全保护和评估标准。

![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnuf9XRkvE7MC7QBSY9lHeozpPHiaBMakZxcqxXyzR1ficeoZw8Odj0Z8w/640?wx_fmt=png&from=appmsg)

## 基本要求的特点

### 1.对象范围扩大:

    新标准将云计算、移动互联、物联网、工业控制系统等列入标准范围，构成了"安全通用要求+新型应用安全扩展要求的要求内容。

### 2.分类结构统一:

    新标准“基本要求、设计要求和测评要求”分类框架统一，形成了“安全通信网络”、“安全区域边界”安全计算环境”和“安全管理中心”:支持下的三重防护体系架构。

### 3.强化可信计算:

    新标准强化了可信计算技术使用的要求，把可信验证列入各个级别并还提出各个环节的主要可信验证要求。

## 基本要求的变化

### 1.名称变更:

    等保2.0的名称从"信息系统安全等级保护基本要求”变更为“网络安全等级保护基本要求”，更加强调网络安全的防护。

### 2.对象变更:

    从原来的信息系统改为等级保护对象，包括网络基础设施(广电网、电信网、专用通信网络等)、云计算平台/系统、大数据平台/系统、物联网、工业控制系统、采用移动互联技术的系统等

### 3.要求变更:

    从安全要求改为安全通用要求和安全扩展要求，安全通用要求是不管等级保护对象形态如何必须满足的要求，针对云计算、移动互联、物联网和工业控制系统提出了特殊要求，称为安全扩展要求。

### 4.分类细化:

    等保2.0的分类更为详细，包括安全物理环境、安全通信网络、安全区域边界、安全计算环境、安全管理中心、安全管理制度、安全管理机构、安全管理人员、安全建设管理、安全运维管理等多个方面。

### 5.章节结构变化:

    第三级安全要求、安全通用要求、云计算安全扩展要求、移动互联安全扩展要求、物联网安全扩展要求、工业控制系统安全扩展要求

### 6.新增内容:

    增加了云计算安全扩展要求、移动互联安全扩展要求、物联网扩展要求、工业控制系统安全扩展、应用场景说明等重点内容。

## 框架

![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnw3tWJYEsXEYib9olP7YJTz8dZXnfQ5WSIqXTubGeuLKAEiaMWREhHXHQ/640?wx_fmt=png&from=appmsg)

## 内容

### 可信验证控制点

#### 1.一级:

    可基于可信根对设备的系统引导程序、系统程序等进行可信验证，并在检测到其可信性受到破坏后进行报警。

#### 2.二级:

    在一级的前提并将验证结果形成审计记录送至安全管理中心。

#### 3.三级:

    在一级的前提下加一步操作，在应用程序的关键执行环节进行动态可信验证，在检测到其可信性受到破坏后进行报警，并将验证结果形成审计记录送至安全管理中心。

#### 4.四级:

    在三级前提下交到管理中心后还要进行动态关联感知。

## 云计算安全扩展要求中的控制点和要求项

![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJny8ZGm64RJ8rJrVfXIGK2jlTJRpYj5cURhd5NWykZ3bYoTo9SibCphNw/640?wx_fmt=png&from=appmsg)

### 移动互联安全扩展要求中的控制点和要求项

![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnPvNTf5mGfoIGxHS6eYUmXuCa2lfgJibmBUnuKzmibdS3cZnr3w3H4MiaQ/640?wx_fmt=png&from=appmsg)

### 物联网扩展要求中的控制点和要求项

![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnZCiayVqtZsaxQ0pogL7syZUTDsk9udibh5fbrMiaUgTAFR2xictAyobvqQ/640?wx_fmt=png&from=appmsg)

### 工业控制系统安全扩展要求中的控制点和要求项

![](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnmoBc0U3SHxcOUHkhDCIvJcu08TGfibmLzibWpgDJ3xH77cTSRBxFZPeQ/640?wx_fmt=png&from=appmsg)

## 总结

√主要标准

√标准体系

√ 等级保护基本要求标准的特点变化、框架和内容

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

0xSecDebug

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

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