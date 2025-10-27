---
title: 【已复现】Nacos 后台 removal 接口 SQL 执行致远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIwMDk1MjMyMg==&mid=2247492622&idx=2&sn=421756753855b4778e62e57395995703&chksm=96f7fb63a18072756d5f876827020349de991368037543ef024569b6576bcdb4a1c94c7edc80&scene=58&subscene=0#rd
source: 长亭安全应急响应中心
date: 2024-07-20
fetch_date: 2025-10-06T17:43:11.137654
---

# 【已复现】Nacos 后台 removal 接口 SQL 执行致远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FOh11C4BDicR2NSz154yCkDIHD5JsCeOM2os4Xnur6VETvOSPzl4KPtd0dxxIjTulckHQ858R2WpWOhJaLgm8Bw/0?wx_fmt=jpeg)

# 【已复现】Nacos 后台 removal 接口 SQL 执行致远程代码执行漏洞

长亭安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FOh11C4BDicR2NSz154yCkDIHD5JsCeOMEPGdRo8crasIgWFOnRmAIzD0pDKIoSBamg6SH6NHLx4IhEn2so272A/640?wx_fmt=jpeg&from=appmsg)

Nacos是一个开源的服务发现和配置管理平台，专门为微服务架构设计，用于帮助构建动态服务发现、服务配置管理、服务元数据及流量管理。

2024年7月，互联网披露了一个Nacos的漏洞利用。经分析，攻击者可利用该漏洞获取操作系统权限，建议受影响的客户尽快修复漏洞。

#

**漏洞描述**

Description

**0****1**

**漏洞成因**

在 standalone 模式下，Nacos 默认使用 Derby 数据库。与其他外部数据库不同，Apache Derby 数据库是嵌入式的，无法通过外部 JDBC 连接进行管理，因此 Nacos 提供了运维接口来执行 SQL 语句。该漏洞利用了 removal 接口实现远程代码执行，是后台漏洞。

## **漏洞影响**

在 Nacos 未启用身份认证、攻击者绕过权限获取后台权限，或攻击者使用合法账号登录的情况下，可以利用该接口实现远程代码执行。

**处置优先级：高**

**漏洞类型：**SQLi to RCE

**漏洞危害等级：**高

**权限认证要求：**开启鉴权后需要认证

**系统配置要求：**默认配置可利用

**用户交互要求：**无需用户交互

**利用成熟度：**POC/EXP已公开

**批量可利用性：**可使用通用 POC/EXP，批量检测/利用

**修复复杂度：**低，官方已发布升级版本

**检测工具**

Detection

**0****2**

#

# **X-POC远程检测工具**

```
xpoc -r 427 -t http://xpoc.org
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicR2NSz154yCkDIHD5JsCeOM4dpOaZWLoA4UOYUa7dqjtTiaoDnBb9pITgoFRmVcu1RspwlWDTH8cibw/640?wx_fmt=png&from=appmsg)

工具获取方式：

* https://github.com/chaitin/xpoc
* https://stack.chaitin.com/tool/detail/1036

**影响版本**

Affects

**03**

```
Nacos < 2.4.0
```

**解决方案**

Solution

**04**

##

## **升级修复方案**

官方已在2.4.0版本中引入了一个新的选项 derbyOpsEnabled，并将其默认设置为关闭，以防止相关接口被滥用。可在Nacos官网下载最新版本使用。

## **临时缓解方案**

1. 无权限绕过漏洞的版本可启用 Nacos 鉴权并设置足够复杂的密码。

2. 使用外部数据库作为 Nacos 的数据库。

3. 使用WAF等安全设备进行防护。

4. 在不影响业务的情况下配置URL访问控制策略。

5. 限制访问来源地址，如非必要，不要将系统开放在互联网上。

**产品支持**

Support

**06**

**云图：**默认支持该产品的指纹识别，同时支持该漏洞的PoC原理检测。

**洞鉴：**以自定义POC形式支持该漏洞的原理检测。

**雷池：**默认支持检测该漏洞的利用行为。

**全悉：**默认支持检测该漏洞的利用行为。

**时间线**

Timeline

**07**

7月15日 长亭科技获取漏洞情报

7月15日 长亭应急响应实验室漏洞分析与复现

7月15日 长亭安全应急响应中心通知客户修复

7月19日 官方发布新版本修复漏洞

7月19日 长亭安全应急响应中心发布通告

参考资料：

[1].https://github.com/alibaba/nacos

**长亭应急响应服务**

全力进行产品升级

及时将风险提示预案发送给客户

检测业务是否受到此次漏洞影响

请联系长亭应急服务团队

7\*24小时，守护您的安全

第一时间找到我们：

邮箱：support@chaitin.com

应急响应热线：4000-327-707

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

长亭安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

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