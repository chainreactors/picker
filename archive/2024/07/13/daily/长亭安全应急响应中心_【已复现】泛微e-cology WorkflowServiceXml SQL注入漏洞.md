---
title: 【已复现】泛微e-cology WorkflowServiceXml SQL注入漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIwMDk1MjMyMg==&mid=2247492602&idx=1&sn=c2dd6499124a6082ea12265c8fb45fae&chksm=96f7fc97a18075816e2fafeda31629399c123a8cbd3ce0ee0954d47f9b72598a40a4bab04cbc&scene=58&subscene=0#rd
source: 长亭安全应急响应中心
date: 2024-07-13
fetch_date: 2025-10-06T17:43:14.995908
---

# 【已复现】泛微e-cology WorkflowServiceXml SQL注入漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FOh11C4BDicTzGx0hoafovyYnXsxAS7nIuQEdLv6UmRdibFACagHE2ezibhOQibKsJCnTHbFc0RPpcLtocia8hkvNRQ/0?wx_fmt=jpeg)

# 【已复现】泛微e-cology WorkflowServiceXml SQL注入漏洞

长亭安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FOh11C4BDicTzGx0hoafovyYnXsxAS7nI9qv0YbVkNR9ywpZSU1DPejB2jicBLeBKmkKwhVENt3DjnyRRxDhicG2A/640?wx_fmt=jpeg&from=appmsg)

泛微e-cology是一款由泛微网络科技开发的协同管理平台，支持人力资源、财务、行政等多功能管理和移动办公。

2024年7月，泛微官方发布了新补丁，修复了一处SQL注入漏洞。经分析，攻击者无需认证即可利用该漏洞，建议受影响的客户尽快修复漏洞。

#

**漏洞描述**

Description

**0****1**

**漏洞成因**

该漏洞是由于泛微e-cology未对用户的输入进行有效的过滤，直接将其拼接进了SQL查询语句中，导致系统出现 SQL 注入漏洞。

## **漏洞影响**

攻击者可利用此漏洞获取敏感信息，进一步利用可能获取目标系统权限。

**处置优先级：高**

**漏洞类型：**SQL注入

**漏洞危害等级：**高

**权限认证要求：**无需权限

**系统配置要求：**默认配置可利用

**用户交互要求：**无需用户交互

**利用成熟度：**POC/EXP 未公开

**批量可利用性：**可使用通用 POC/EXP，批量检测/利用

**修复复杂度：**低，官方提供热修复、升级修复方案

**检测工具**

Detection

**0****2**

#

# **X-POC远程检测工具**

```
xpoc -r 426 -t http://xpoc.org
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicTzGx0hoafovyYnXsxAS7nIq29mh42H3zCziaL0ATKl42jmzSgKPYCz7I0MYqPMdiaHkP3AE8taZDPQ/640?wx_fmt=png&from=appmsg)

工具获取方式：

* https://github.com/chaitin/xpoc
* https://stack.chaitin.com/tool/detail/1036

**影响版本**

Affects

**03**

```
e-cology 9 < 补丁版本 2024-07-10
```

**解决方案**

Solution

**04**

##

## **升级修复方案**

官方已发布升级补丁包，支持在线升级和离线补丁安装，可在参考链接[1]进行下载使用。

## **临时缓解方案**

临时缓解方案可能无法完全阻止漏洞的利用，强烈建议尽快升级到修复版本。

1. 使用WAF等安全设备进行防护。

2. 在不影响业务的情况下配置URL访问控制策略。

3. 限制访问来源地址，如非必要，不要将系统开放在互联网上。

**产品支持**

Support

**05**

**云图：**默认支持该产品的指纹识别，同时支持该漏洞的PoC原理检测。

**洞鉴：**以自定义POC形式支持该漏洞的原理检测。

**雷池：**默认支持检测该漏洞的利用行为。

**全悉：**支持部分漏洞利用行为的检测，完整检测于2024.7.12发布更新包支持。

**时间线**

Timeline

**06**

7月10日 官方发布漏洞补丁

7月12日 长亭应急响应实验室分析与复现

7月12日 长亭安全应急响应中心发布通告

参考资料：

[1].https://www.weaver.com.cn/cs/securityDownload.html?src=cn

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