---
title: 漏洞预警 | CraftCMS SQL注入漏洞
url: https://mp.weixin.qq.com/s/e_VTi1zv-pzyrecCRn8lAw
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:55:15.382655
---

# 漏洞预警 | CraftCMS SQL注入漏洞

# 漏洞预警 | CraftCMS SQL注入漏洞

浅安
浅安

浅安安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**0x00 漏洞编号**

* # CVE-2026-115934

**0x01 危险等级**

* 高危

**0x02 漏洞概述**

CraftCMS是一个灵活的、易于使用的内容管理系统。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SU8Hf5YibCK8obmSCq5lcwuicW45vQDp2TGuPUldZibXaj87iaPNkrGu3D3R2ib7oc5lK6rPab4859G6gQ/640?wx_fmt=png&randomid=xu0uxjj1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

**0x03 漏洞详情**

**CVE-2026-115934**

**漏洞类型：**SQL注入

**影响：**账号接管

**简述：**CraftCMS存在SQL注入漏洞，由于前端搜索功能中的attribute参数被未经清理便直接拼接进 SQL查询，且底层PDO使用模拟预处理，未经验证的攻击者可以通过该参数执行堆叠查询，从而对应用程序数据库获得读写访问权限，进而将权限提升至管理员。

**0x04 影响版本**

* 4.0.0 <= Craft CMS < 4.18.9
* 5.0.0 <= Craft CMS < 5.11.2

**0x05 POC状态**

* 已公开

**0x06****修复建议**

******目前官方已发布漏洞修复版本，建议用户升级到安全版本************：******

https://craftcms.com/

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