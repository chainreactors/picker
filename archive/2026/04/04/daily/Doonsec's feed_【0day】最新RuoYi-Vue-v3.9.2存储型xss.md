---
title: 【0day】最新RuoYi-Vue-v3.9.2存储型xss
url: https://mp.weixin.qq.com/s/htP3VzHu8jfx-7YQiZx6Pw
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:12.878349
---

# 【0day】最新RuoYi-Vue-v3.9.2存储型xss

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2AAMh9HmvsR0nS3Nib8G7GhRd6ric6tEiaA3ibTGKAjsLtLV3ibHxggp0fm5N5nExiasoKP9lAlJXHqKmLtUhJKS5XsqbibaclJqtrtVwzxTqTGZ9A/0?wx_fmt=jpeg)

# 【0day】最新RuoYi-Vue-v3.9.2存储型xss

原创

wallkone
wallkone

星络安全实验室

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| 免责声明:文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，未授权的攻击属于非法行为!文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责作者不为此承担任何责任，一旦造成后果请自行负责 |

项目地址：https://gitee.com/y\_project/RuoYi-Vue/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AAMh9HmvsTY2iaxZdN4MJI0wh0SrNnibqcNicTrOibF1OOXvQoibbwgah4ibYDb6YFW2G1NjyaKdERKK1NotCDqNHt6I7y5RZnRseq3DZtS2WgkA/640?wx_fmt=png&from=appmsg)

我们本地搭建好环境，通过账号密码登录后台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AAMh9HmvsQ0Yx0RXWEOtMhxZa2HBib75aeCJibSicYSsk5mUHYSibX8QI9z8h8icpZfmBicpp4Jjwyn6ZpGuwddVf2eQV1vF2fydVCQ9xvddn5ow/640?wx_fmt=png&from=appmsg)

抓包，构造payload

![](https://mmbiz.qpic.cn/mmbiz_png/2AAMh9HmvsTWxAr4A9FTovGb2fEZkmdkMbYNAYkExVkWIfUZ7eqhFN2RhCI5e7micsqftEicQF3QnEEDheLqdvXRJb6D5805ibicQpReEib6AEQI/640?wx_fmt=png&from=appmsg)

我们去首页右上角铃铛哪里查看

![](https://mmbiz.qpic.cn/mmbiz_png/2AAMh9HmvsTGySkAGWeriaqy8zltbI214ltmHmwxgDwk55m4hibQEenQSHM7wJRtXYN6xTgDRSQEtlO3nA7fa8ZYqQTy4znK2OZmpvibFJVV9o/640?wx_fmt=png&from=appmsg)

点击公共，成功弹窗

![](https://mmbiz.qpic.cn/mmbiz_png/2AAMh9HmvsRc8plxNb6QcwSIL0XT5w5CCYtn0tIeKa6ILOJib3pB83t6MN33KiatZpuRbbr5BviawzeJsMHYD4MFJeibH9tUVdpKPiamTDFhrTNY/640?wx_fmt=png&from=appmsg)

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