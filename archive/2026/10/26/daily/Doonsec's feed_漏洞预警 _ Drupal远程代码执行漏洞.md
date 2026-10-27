---
title: 漏洞预警 | Drupal远程代码执行漏洞
url: https://mp.weixin.qq.com/s/7m6ON0XMkyiYXkykMkWRUw
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:03:12.770889
---

# 漏洞预警 | Drupal远程代码执行漏洞

# 漏洞预警 | Drupal远程代码执行漏洞

浅安
浅安

浅安安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**0x00 漏洞编号**

* # CVE-2026-108097

**0x01 危险等级**

* 高危

**0x02 漏洞概述**

Drupal是一款基于PHP开发的开源企业级内容管理框架，广泛用于政府、金融、媒体等机构搭建门户网站、业务系统与Web应用。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NQlfTO30MhzAnDhnrasiaqbbLGOfSchKiauI2l1EJdHLn7dlXcJEVhvdY12QTH6nrUKgMKTFWYSF1yoeFx0j8Vql17iabqoBRWcUSvswbKicibicI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**0x03 漏洞详情**

**CVE-2026-108097**

**漏洞类型：**远程代码执行

**影响：**执行任意命令

**简述：**Drupal存在远程代码执行漏洞，由于其FieldUiTable::tablePreRender：Field UI表格渲染时会把row的#region\_callback当作PHP callable直接调用，并把整行数组按引用传入。如果目标站点存在一个贡献模块或自定义代码路径，允许HTTP请求数据影响Field UI row的#region\_callback，攻击者就可以让Drupal执行任意PHP callable。

**0x04 影响版本**

* 8.9.0 <= Drupal <= 10.6.18
* 11.0.0 <= Drupal <= 11.3.18
* 11.4.0 <= Drupal <= 11.4.9
* 12.0.0-alpha1 <= Drupal < 12.0.0 beta2

**0x05****POC状态**

* 已公开

**0x06****修复建议**

********目前官方已发布漏洞修复版本，建议用户升级到安全版本**************：******

https://new.drupal.org/

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
在看
，轻点两下取消在看
分享
留言
收藏
听过