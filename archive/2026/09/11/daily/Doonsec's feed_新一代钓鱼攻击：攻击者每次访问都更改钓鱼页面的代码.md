---
title: 新一代钓鱼攻击：攻击者每次访问都更改钓鱼页面的代码
url: https://mp.weixin.qq.com/s/BvItrdz89rLkmuou8wncNw
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:45:46.198860
---

# 新一代钓鱼攻击：攻击者每次访问都更改钓鱼页面的代码

# 新一代钓鱼攻击：攻击者每次访问都更改钓鱼页面的代码

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于威胁情报Z分析
，作者Z

![](https://wx.qlogo.cn/mmhead/j8cooK2zCqoqY1ibzIuH0db0U6NFgdx4PahHyU6OOprunMrA5RzXbibpMcUA18kVOibjEK1IK7HQ28/0)

**威胁情报Z分析**
.

国际网络安全威胁情报，地缘政治事件分析。

安全研究人员发现了一个有趣的现象。他们观察到，同一个钓鱼URL每次访问都会返回不同的JavaScript/HTML负载。

在进行了50次数据抓取后，发现了50个不同的SHA-256哈希值，以及21个不同的页面标题，同时还包括变化的JavaScript函数、变量、HTML/DOM结构、CSS类、视觉参数和文本内容。

这种诱饵技术简而言之的工作原理如下：

用户点击钓鱼链接 -> 服务器为该访问发送唯一的/混淆的JS+HTML -> 浏览器运行并解码此代码 -> 真实的假登录表单出现 -> 用户输入用户名/密码 -> 信息被发送到攻击者的服务器。

这里的关键点：尽管向每个访问者发送不同的代码，但最终用户看到的钓鱼页面看起来是相同的。

这种技术通常被称为多态（polymorphic）钓鱼或多态代码/混淆。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXulx4jNADvIEiasquQviatslCLXlAtmNMzRld8nadyRuL6UmUH22gTxsUL9hPb57uBQk6Botx9BI2ibckq6S0YTctRrhD30neu7z9M/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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