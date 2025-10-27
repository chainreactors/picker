---
title: 【技术原创】域渗透——利用GPO中的脚本实现远程执行
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247557453&idx=1&sn=e2d89ddc457681260c2519c921019c5b&chksm=e9143177de63b861d9cf22a5a4329e528ec9ca0c0c7b0c82697d9e4ae59e1e3cab2d6a98f2aa&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-02-15
fetch_date: 2025-10-04T06:38:06.923871
---

# 【技术原创】域渗透——利用GPO中的脚本实现远程执行

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvr56Hebv6B6wLibXXQTdq2twfuiaSObxuZicAsWlxFvVRz7HcoQdOIKEL8g/0?wx_fmt=jpeg)

# 【技术原创】域渗透——利用GPO中的脚本实现远程执行

原创

3gstudent

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrBa91KcAu8ZpCA8ibwE49yePHlIj4iaMIiawAiaCxsnUmDpXRUsDQ788j9A/640?wx_fmt=png)0x00 前言

在之前的文章《域渗透——利用GPO中的计划任务实现远程执行》介绍了通过域组策略(Group Policy Object)远程执行计划任务的方法，本文将要介绍类似的另外一种方法：通过域组策略(Group Policy Object)的脚本实现远程执行。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrBa91KcAu8ZpCA8ibwE49yePHlIj4iaMIiawAiaCxsnUmDpXRUsDQ788j9A/640?wx_fmt=png)0x01 简介

本文将要介绍以下内容:

通过Group Policy Management Console (GPMC) 实现脚本的远程执行

通过命令行实现脚本的远程执行

新建GPO实现远程执行

修改已有的GPO，实现远程执行

实现细节

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrBa91KcAu8ZpCA8ibwE49yePHlIj4iaMIiawAiaCxsnUmDpXRUsDQ788j9A/640?wx_fmt=png)0x02 通过Group Policy Management Console (GPMC) 实现脚本的远程执行

**1、创建GPO**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrmnrQ5Y8lWUFWzKicxt3W0CDph5kMAJTj55yX2ZPRuqlp400u2EFwlgQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrDuNVJaEMJektzpJ0OG70NXk9e6oEn0ica2O2xs0TXNT3qPPJqpuHIQw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrqFDUbCMfuicqetdzkodrHTSibkiahrQqYPzAHjCJXVY9AU7jWfOfSAKBw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrDuNVJaEMJektzpJ0OG70NXk9e6oEn0ica2O2xs0TXNT3qPPJqpuHIQw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvr6tlmboRCnR8y7g3u6JZZkkWEDg5ZVWTMXsJ6ACBz0x5bI8RcUsmFsw/640?wx_fmt=png)

**2.配置GPO**

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrDPWmiaDVq7oAicM8icicC5IyjEPaHI6bWVV0uuEjhHqDb6FL6fwexnCnpQ/640?wx_fmt=png)**

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvr1wFbiaxyg8iclL1tqIca14pUkuiafosYds5AjvYWmuG0z5GXscS9UjicVg/640?wx_fmt=png)**

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrN2tQQJ0eeWXvRYLczKJ1iawzVQ2TyqcPBVPSuYnRKwia5cPSvybdYylg/640?wx_fmt=png)**

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrBa91KcAu8ZpCA8ibwE49yePHlIj4iaMIiawAiaCxsnUmDpXRUsDQ788j9A/640?wx_fmt=png)0x03 通过命令行实现脚本的远程执行

**1.作用于全域**

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvre4rlIZfu8M8wqsj7Tzq2GD3DcCibUj1Y0HG6iawnIzUafxgF1TBUH0sQ/640?wx_fmt=png)**

****![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvr0duaEQ7rYO0H1Zy5x8ialTzJ0u0DWQtK4pjtXCrYibkhcVfhe7Wx1ZTg/640?wx_fmt=png)****

**2.作用于指定目标**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrz4wIF59KEicMa5CaRoF9ZsO7uLCm4QR3iaPcNPspNMhWMwnyLhVqeIdA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrEOOymwalibzQWetvydMpnLFOXzYzGRlqjIQ2TySfoO9tFKzrymzrvicA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrjic7ib7hSqia6vAx3KhRD5j4JszQjG6ajdSKYFSVxxQfzRxNjtp3ytEFg/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrBa91KcAu8ZpCA8ibwE49yePHlIj4iaMIiawAiaCxsnUmDpXRUsDQ788j9A/640?wx_fmt=png)0x04 修改已有的GPO，实现远程执行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrgVeFxhepEkeib2BueDJysg7ql9DwJhibia7DMQGJKUAPgUNKxVOMF2S2Q/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrn8qEU49jKeAS4P04pib6dczusiawnrQreNcYY4owuHht0kjmfxias2WUg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrbibNX4a7SZdLlTT40ezKHvJ0o4QuSRsQfYAaB1xQ1eUmMGibOQp4icibcg/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrBa91KcAu8ZpCA8ibwE49yePHlIj4iaMIiawAiaCxsnUmDpXRUsDQ788j9A/640?wx_fmt=png)0x05 直接执行远程脚本

当我们选择直接执行组策略文件夹中的bat文件，会弹框提示无法执行，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrsHyuMvsia97pbbBTDdYITzUhibEhg6RxDZv3MjCicJia16CniaTTiciaJlbJQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrP2BSFian9BD8wRV8ng3ulueglQvc4wmB2r4Z55pAwhEptp7IiaL4z61g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrOpaia0BicgG86kRKD87cdeX9ScefI1JWR0s5s6e9Cbl6d5zIaaDq0EBg/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrBa91KcAu8ZpCA8ibwE49yePHlIj4iaMIiawAiaCxsnUmDpXRUsDQ788j9A/640?wx_fmt=png)0x06 小结

本文介绍了通过域组策略(Group Policy Object)中的脚本实现远程执行的方法，分享实现细节和利用思路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvrGNeY2icQPDhpnKoZ4ic5Bmern9DFDdRxDUts0GHHicKT75iaJoBFh4HdZw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibI6UBcGqkFz6hNOdgF6cvru5cu6JXIdxib8u5nZfpDMLDX6jtAO3Ja05fYNg1SZH0pSnow7n7w5Xw/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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