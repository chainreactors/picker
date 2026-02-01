---
title: 0day-飞牛 fnOS存在任意文件读取漏洞
url: https://mp.weixin.qq.com/s/CAP2D7-hllhK9dbYFFhxuw
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:24:23.287771
---

# 0day-飞牛 fnOS存在任意文件读取漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO4ohTJXdYOQgKdyGB0DibqpJia1VQsCWESbdsw1tfheA3mhTJczSbEJD165bDDgRIkZAnkCfr63z3NQ/0?wx_fmt=jpeg)

# 0day-飞牛 fnOS存在任意文件读取漏洞

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

资产介绍

飞牛 fnOS 是一款由中国团队“飞牛工作室”开发的、面向个人和家庭用户的私有云操作系统。  您可以把它理解为一个类似于 群晖 DSM 或 威联通 QTS 的国产化替代方案，旨在让用户能够轻松地将自己的硬件（特别是旧电脑、迷你主机或NAS设备）转变为功能强大、易于管理的私有云服务器。

资产测绘

```
icon_hash="470295793"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4ohTJXdYOQgKdyGB0DibqpJu01BD2XSFibibUH1YVQ4y0IVFPqiaD7USteaC7mXAeKkDvRLCvgB5p9ew/640?wx_fmt=png&from=appmsg)

教育资产

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4ohTJXdYOQgKdyGB0DibqpJryX9BaLJibbwZAFmBoG4XkJiahs4VKCns8H7TqruibP9L8iawwMtMn3EZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4ohTJXdYOQgKdyGB0DibqpJCSLgIl5R6Zo6JMNvyG2ohWwTMN2bNiaXrqsYd0VnYHvFJPZgMuZfJVg/640?wx_fmt=png&from=appmsg)

漏洞复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4ohTJXdYOQgKdyGB0DibqpJWKqlmIo1u70LZupAWDarvh7zibFzibic9wXDmFbtFXnVCicwbH3jcdScKA/640?wx_fmt=png&from=appmsg)

后台私信回复加群加入交流群

后台回复fly获取poc

有思路工具需要的师傅可以加入小圈子

主要内容是（2025-2026/edusrc实战报告/edu资产/漏洞挖掘工具等）   其他内容懂得都懂，持续更新中

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAV25rGkkJ8qOPAooDwASNSaiaGJibu3z2mOqnD2vCnOQB6ia3AfuuOZ0ZDg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

陌笙不太懂安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

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