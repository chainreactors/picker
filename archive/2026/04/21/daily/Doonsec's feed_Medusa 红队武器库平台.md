---
title: Medusa 红队武器库平台
url: https://mp.weixin.qq.com/s/jl1q_LOfxDxZ00IeihOgdQ
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:41:48.571915
---

# Medusa 红队武器库平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7Z3bTeWfIiayAevmru8icV28KUHlmGnkXfL4d7P1HZdyRaI9Tqqhf5dibJmGficQhNkiadTIHXMHP8FP7RVlOHVXjy4jzlHibhGuS09UnswwDgMck/0?wx_fmt=jpeg)

# Medusa 红队武器库平台

kali笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于Kali
，作者大表哥吆

![](http://wx.qlogo.cn/mmhead/kSiaeFj92SMxkCHJQYORHxIbkUZyPFJCK4Y31ofOEr1wq3K8QYribw87nkVNpsadbdH9lFQvKfVkE/0)

**Kali**
.

致力于Kali Linux 网络安全学习。介绍Kali中工具的使用，Linux运维、逆向、网络安全、硬件安全、极客DIY 没有你学不到，只有你想不到。

> 本文为大家推荐一款红队武器库平台-Medusa。主要包括XSS平台、协同平台、CVE监控、免杀生成、DNSLOG、钓鱼邮件、文件获取等功能。

项目地址

> https://github.com/Ascotbe/Medusa/blob/master/README.CN.md

# 功能特性

●GitHub CVE项目监控

●被动扫描

●XSS钓鱼平台

●杀软进程对比

●CPU进程等信息

●PE结构解析

●协同作战平台

●APP收集

●CVE数据监控

# 部署安装

手动部署比较麻烦，这里我们直接Docker安装。文末会为大家提供官方部署文档。

```
●●●code

1git clone https://github.com/Ascotbe/Medusa.git
2cd Medusa
3sudo chmod +x install.sh
4./install.sh -u medusa.test.ascotbe.com -d dnslog.test.ascotbe.com -s ascotbe.com
```

![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgiciapeGh5DG45OT4Kx6llPne6h1d1xdoPhrm7yicvIhLxSibRF29tTiawIX0RN491xUibial0o9Vde6GYw/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgiciapeGh5DG45OT4Kx6llPnaALI1dokib2L5NXZCsPYxMAJhxop3B6M4e2cLqurcpqhkdI3vLsUryw/640?wx_fmt=png)

等待docker启动完成后，我们便可以访问了。

# 登录平台

最后，如果您在上面的配置中都未修改端口以及IP，那么访问`http://127.0.0.1:8082`即可看到web界面。

![](https://mmbiz.qpic.cn/mmbiz_gif/Xb3L3wnAiatgiciapeGh5DG45OT4Kx6llPnSefWh6icgqd4vjukoQYCRBZTDebWntGZOO9eP4rc0LMld8LK69ztYHA/640?wx_fmt=gif)

# 友情提示

●不用做对未授权目标使用该扫描器，遵守网络安全法。

●对违法使用者，开发人员不承担任何连带责任

●该项目只为交流学习使用

更多精彩文章 欢迎关注我们

关注它 你就是大佬

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

kali笔记

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

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