---
title: 【漏洞预警】Apache Dubbo Hession反序列化漏洞
url: https://mp.weixin.qq.com/s?__biz=MzAxNDM3NTM0NQ==&mid=2657044865&idx=1&sn=ff932955d7bcf4f68b03b758ba4913ff&chksm=803fa95fb7482049e6d89a80ed79269bb84b92c6878d51e85b8ec8c05683cab94aefe26c87bd&scene=58&subscene=0#rd
source: SecPulse安全脉搏
date: 2022-10-21
fetch_date: 2025-10-03T20:30:32.958874
---

# 【漏洞预警】Apache Dubbo Hession反序列化漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5u08OUQmyqeL3dQ01xen8O8cURh3Gkwf6tDrhTWTTOEiaJb8Z9ibONx8mljLx8E1G01Ste3A10q8ug7ic3rKPZohQ/0?wx_fmt=jpeg)

# 【漏洞预警】Apache Dubbo Hession反序列化漏洞

SecPulse安全脉搏

##

1. **通告信息**

近日，安识科技A-Team团队监测到一则 Apache Dubbo组件存在Hession反序列化漏洞的信息，漏洞编号：CVE-2022-39198，漏洞威胁等级：高危。

该漏洞是由于Dubbo hessian-lite 3.2.12及之前版本中存在反序列化漏洞，成功利用此漏洞可在目标系统上执行恶意代码，最终获取服务器最高权限。

对此，安识科技建议广大用户及时升级到安全版本，并做好资产自查以及预防工作，以免遭受黑客攻击。

##

2. **漏洞概述**

CVE：CVE-2022-39198

简述：Apache Dubbo是一款高性能、轻量级的开源服务框架，提供了RPC通信与微服务处理两大关键能力。由于Dubbo hessian-lite 3.2.12及之前版本中存在反序列化漏洞，成功利用此漏洞可在目标系统上执行恶意代码。

##

3. **漏洞危害**

攻击者可利用该漏洞在未授权的情况下，构造恶意数据执行远程代码执行攻击，最终获取服务器最高权限。

##

4. **影响版本**

目前受影响的Apache Dubbo 版本：

Apache Dubbo 2.7.x版本：<= 2.7.17

Apache Dubbo 3.0.x版本：<= 3.0.11

Apache Dubbo 3.1.x版本：<= 3.1.0

##

5. **解决方案**

目前该漏洞已经修复，受影响用户可以升级到Dubbo hessian-lite 版本 >=3.2.13；或升级Apache Dubbo到以下版本：

Apache Dubbo 2.7.x版本：>= 2.7.18

Apache Dubbo 3.0.x版本：>= 3.0.12

Apache Dubbo 3.1.x版本：>= 3.1.1

Apache Dubbo下载链接：

https://github.com/apache/dubbo/tags

Dubbo hessian-lite下载链接：

https://github.com/apache/dubbo-hessian-lite/releases

##

6. **时间轴**

【-】2022年10月18日 安识科技A-Team团队监测到Apache Dubbo Hession反序列化漏洞信息

【-】2022年10月19日 安识科技A-Team团队根据漏洞信息分析

【-】2022年10月20日 安识科技A-Team团队发布安全通告

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5u08OUQmyqeMDQk5XTcSCesCTFM98kRm3Z5lyfPDmgLQDdSE5lV5t70yVhqZIXj4nCjyT8MV6pSzHmSIPZIg5A/0?wx_fmt=png)

SecPulse安全脉搏

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5u08OUQmyqeMDQk5XTcSCesCTFM98kRm3Z5lyfPDmgLQDdSE5lV5t70yVhqZIXj4nCjyT8MV6pSzHmSIPZIg5A/0?wx_fmt=png)

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