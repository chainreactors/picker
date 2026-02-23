---
title: 做个\"脚本小子\"--XPOC下载篇
url: https://mp.weixin.qq.com/s/BhfaxatmTiWpxMZhuukHHQ
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:16:28.040815
---

# 做个\"脚本小子\"--XPOC下载篇

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KvrEnQiahoiaAPESWlbyibdJiaSGtQvzxRPdiakL7ibrxJcSYtj70vqr7QeamEwKeZ2Ch0FIWXWqSISCqLQ1icEeWIcxGftP9wibI6ZblC8biaiaCMlIY/0?wx_fmt=jpeg)

# 做个"脚本小子"--XPOC下载篇

原创

lawliet
lawliet

kingman安全

![]()

在小说阅读器中沉浸阅读

声明:

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。同时所有相关行为均已取得授权，未经作者同意禁止转载

# 前言

在网络安全渗透测试、漏洞验证的实战场景中，轻量化工具始终是从业者的首选——高效、便捷、资源占用低，能以最低成本完成核心的POC，而xray无疑是这类工具中的佼佼者。

熟悉xray的朋友们都清楚它的优势所在：检测速度快，依托高效的发包策略和漏洞检测算法，能快速完成批量扫描；更重要的是它轻量化的特质，单文件部署、无多余依赖，无论是内网测试还是外网应急，都能快速上手使用，无需复杂配置即可启动扫描任务。

但即便xray足够优秀，在实战应用中也难免遇到瓶颈——最突出的问题，就是内部POC资源的匮乏。xray默认仅内置部分公开的POC规则和CT stack上收录的POC，虽然支持用户自行构建，但对于大多数从业者而言，编写高质量POC不仅需要深厚的技术积累，还需要投入大量时间成本；而行业内核心的、针对性强的内部POC，往往掌握在少数团队手中，难以获取。这就导致我们在面对一些特殊场景、小众系统，或是新型漏洞时，即便有xray这款好用的工具，也会因缺少对应的POC而束手无策，无法充分发挥工具的检测能力，错失漏洞发现的关键机会。

今天就为大家推荐一款号称“xray2.0”的轻量化POC工具，它非xray官方推出的升级版本，却在功能设计、操作逻辑上高度贴合xray，如果你也在使用xray时，没有测试出漏洞，不妨试试这款“xray2.0”工具。

# 安装/使用

根据自己的系统选择程序即可

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaBudw4lnhyTNRrHBEYEIGDJ9rfVxrGnptks1xFs8SLrq42vJH3PAoITHEAkGSsCKTOibd8qz0qOtkb5ACk7lar8U07qc7K5qdEQ/640?wx_fmt=png&from=appmsg)

首先我们先更新

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaACgvpLQUCV0IwsTrk7oH43ia6VibItbOkCYowkE6mVaphCT8obtRPh3OevtHjWB8gsUwUF8Xicu7AP00AXTJOb8o32bVr0z66IBA/640?wx_fmt=png&from=appmsg)

# 扫描指定目标

```
xpoc_windows_amd64.exe -t
```

# 查看poc列表

```
xpoc_windows_amd64.exe list -a
```

# 批量扫描

```
xpoc_windows_amd64.exe -i targets.txt
```

回头大家试试吧，在nuclei，xray跑完后，或许这也是个好宝贝

# 获取

公众号回复xpoc获取软件

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

kingman安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

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