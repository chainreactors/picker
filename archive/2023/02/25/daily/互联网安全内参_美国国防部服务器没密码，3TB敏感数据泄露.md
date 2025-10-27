---
title: 美国国防部服务器没密码，3TB敏感数据泄露
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507903&idx=2&sn=75ef4c9f1be2cb8c6b3a6eda3a5574d4&chksm=ebfa989fdc8d1189a592df3b0816cc2d4db8f1d40fe9c5938864c6b6ef6eefece795cef0e274&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2023-02-25
fetch_date: 2025-10-04T08:04:51.222232
---

# 美国国防部服务器没密码，3TB敏感数据泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7uHmCEqgicTb1aDa7yPQsCht48pwibXo70vR4YW4jLqNDDt5LhuIym6Mibt9uS7HBlW5uwpeRW5WfjOg/0?wx_fmt=jpeg)

# 美国国防部服务器没密码，3TB敏感数据泄露

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvabHB9OAuxRECeLDjkCf0viaJRoGnymJAr1xj2euW2gBwIcwVy8nObKKJKQdwGy9DDfVaKhQGbLn0A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

上周末，安全研究人员Anurag Sen发现美国国防部一台存储了3TB内部军事电子邮件的服务器在线暴露长达两周，该服务器托管在微软的Azure政府云上，供美国国防部客户使用，与其他商业客户物理隔离，可用于共享敏感的政府数据。其中许多数据与美国特种作战司令部（USSOCOM）有关，USSOCOM是美国负责执行特殊军事行动的军事单位。

令人惊讶的是，暴露的服务器由于配置错误没有密码，任何人都可通过互联网访问。

据Anurag Sen透露，暴露数据包含过去几年的大量内部军事电子邮件，其中一些包含敏感的人员信息。其中一个暴露的文件包括一份完整的SF-86问卷，该问卷用于处理机密信息前的个人审查，由寻求安全许可的联邦雇员填写，包含高度敏感的个人和健康信息。

根据Shodan的搜索结果，该邮箱服务器2月8日首次被检测为数据泄露。目前尚不清楚邮箱数据是如何暴露在公共互联网上的，从目前可用信息推测可能是由于人为错误导致的配置错误。

目前尚不清楚除了Sen之外，是否有人在两周的暴露窗口期内发现了可以从互联网访问云服务器的暴露数据。

无独有偶，上周末美国有线电视新闻网报道美国联邦调查局纽约办事处的（用于调查儿童性剥削的）计算机系统也遭黑客入侵，联邦调查局发言人Manali Basu证实，该机构已经控制了“孤立事件”，并继续开展调查。

参考链接：

*https://techcrunch.com/2023/02/21/sensitive-united-states-military-emails-spill-online/*

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：GoUpSec

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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