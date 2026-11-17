---
title: 漏洞预警 | JeecgBoot SQL注入漏洞
url: https://mp.weixin.qq.com/s/2p6J6M21tivllQQCX4Lc_w
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:55:18.555840
---

# 漏洞预警 | JeecgBoot SQL注入漏洞

# 漏洞预警 | JeecgBoot SQL注入漏洞

浅安
浅安

浅安安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**0x00 漏洞编号**

* # CVE-2026-124554

**0x01 危险等级**

* 高危

**0x02 漏洞概述**

JeecgBoot是一款基于代码生成器的低代码开发平台。前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT，支持微服务。强大的代码生成器让前后端代码一键生成，实现低代码开发。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SW25cvic5s59KsEGyS6fTiaaogPXrsntzHQO87dEEoxdTnicwvibHLUm8wvIaRo5oQWGzJqicZPr2Q7G9w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

**0x03 漏洞详情**

**CVE-2026-124554**

**漏洞类型：**SQL注入

**影响：**获取敏感信息

**简述：**JeecgBoot的/jeecg-boot/drag/onlDragDatasetHead/getAllChartData接口存在SQL注入漏洞，未经验证的攻击者可通过远程HTTP请求构造注入语句，绕过原有查询条件，进而读取、修改数据库内容，甚至结合数据库权限进一步利用。

**0x04 影响版本**

* JeecgBoot 3.9.5

**0x05****POC状态**

* 已公开

**0x06****修复建议**

********目前官方已发布漏洞修复版本，建议用户升级到安全版本**************：******

http://www.jeecg.com/

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7stTqD182SVPICJDGr5sbVNZO1lo2JnwVDrPBcvzPxiaiamvVZWxcxxcqQYeAiaAnXS26Hyp0wxEx5uXESx0NBQMg/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过