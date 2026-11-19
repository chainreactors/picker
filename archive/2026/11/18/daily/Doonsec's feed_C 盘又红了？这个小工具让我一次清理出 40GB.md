---
title: C 盘又红了？这个小工具让我一次清理出 40GB
url: https://mp.weixin.qq.com/s/bXIks8yM7eirNK1IZE7ArA
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:42:36.626588
---

# C 盘又红了？这个小工具让我一次清理出 40GB

# C 盘又红了？这个小工具让我一次清理出 40GB

原创

wljslmz瑞哥
wljslmz瑞哥

网络技术联盟站

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

各位朋友，你有没有遇到过这样的场景——

电脑用着用着，C 盘空间告急，红色进度条触目惊心。你想清理，但不知道哪些文件占了空间、哪些可以安全删除。打开"磁盘清理"工具，扫了半天，只清出 200MB，杯水车薪。

Windows 自带的"存储"设置倒是能看个大概，但它不会告诉你：到底是哪个文件夹吃掉了 50GB？那些散落在角落里的大文件到底是什么？node\_modules 藏了几个 G？JetBrains 的缓存是不是早就该清了？

今天给大家推荐一个我自己写的免费小工具——**DiskAnalyzer**，专门解决"不知道空间去哪了"的问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05J8ekYL8YAtqsibdJOPLvaIVVyG4rHWpTacichRwRQPibRuZlEGP6IhApA5uNSDOQ4kocyvQBKHgs2lKH4tzkJdsKXZib4RT1gaBs/640?wx_fmt=png&from=appmsg)

## DiskAnalyzer 是什么？

一句话概括：**它能扫描你电脑的任意磁盘或目录，然后用直观的图表告诉你空间都花在了哪里，并给出清理建议。**

它不是清理工具，不会自动删你的文件。它更像一个"磁盘体检报告"——先帮你搞清楚状况，清理的决定权始终在你手上。

## 核心功能

### 1. 目录树可视化

扫描完成后，左侧会展示一棵目录树，按文件大小从大到小排列。每个目录后面都带有一个占比条，一眼就能看出哪个文件夹是"大户"。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba072BhajZT8aCFWricibnoQibOOzhJqsCtibH1rzI0IRibOZPibdMh5HnbgFHKwicW268iaV5HupwKWHNwpb5Fg5PcN3ZJg3nRuIvSVYXOM/640?wx_fmt=png&from=appmsg)

你可以逐层展开，定位到具体是哪个子目录在吃空间。比起在资源管理器里一个个右键看属性，效率提升了不知多少倍。

### 2. 文件类型分析

右侧有个环形图，把文件按类型分成了几大类：视频、音频、图片、文档、压缩包、代码、安装包、数据文件等。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba05FbmoFtXYL6f4EIG9S2BKa4DCPIAvbnnvuA1ATj6wmdY2CEd9mRg4VB3AmJEXylGY8l5meUcT0ZmS3FmWT182tII6flkspYeY/640?wx_fmt=png&from=appmsg)

比如你一看，发现"视频"占了 60%，那大概率是下载目录里堆了不少电影；如果"压缩包"占比很大，可能是以前下载的安装包没删。

**知道空间花在哪里，清理就有方向了。**

### 3. 大文件列表

超过阈值的文件会被单独列出来，默认是 100MB，你也可以自己调——改成 50MB 或 200MB 都行。

大文件列表按大小排序，最多显示 80 个。右键任意一行，可以直接在资源管理器中定位到这个文件，确认是不是该删的。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba05Pft908AR9nrDWwyiaOhy7lXMwia0aJ35nX7gQl00hknUZwcict5RicibovvIXc0MdliauRz0jJWUQ5xibQQrebIJmyzs8iaOAnBUxUhc/640?wx_fmt=png&from=appmsg)

这个功能我用得最多。很多时候你根本不知道电脑里藏着几个 GB 的日志文件、备份文件或者以前下载的安装包，扫一遍就能发现。

### 4. 清理建议

扫描完成后，工具会自动检测一些常见的可清理项：

* **临时文件夹**（Temp）——程序自动生成，安全删除
* **npm / Node 依赖**（node\_modules）——开发者都懂，删了重装就行
* **Gradle / Maven 缓存**——旧项目构建缓存，占空间大
* **JetBrains IDE 缓存**——用 IntelliJ 系列 IDE 的朋友注意了
* **Windows 更新缓存**——系统更新残留
* **AppData 过大**——超过 15GB 会单独提醒
* **休眠文件 / 页面文件**——附带了释放空间的命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba07untfypyrCL1XKJSCZIMTGeEAd910c0QhkbyaVvbCLdCsQficJbRu0AkpMOPfe7qO4s0Z6ic2PmlhY1Wiccodc9nCHicQVWc4y9xo/640?wx_fmt=png&from=appmsg)

每条建议都会标注目录路径、占用大小和操作说明，不会让你瞎删。

## 设计细节

### 暗色主题

整个界面是深色设计，长时间使用不刺眼。图标、配色都经过了调整，信息层级分明，不会觉得杂乱。

### 右键一键定位

目录树和大文件列表都支持右键菜单，点击"在资源管理器中打开"就能直接跳到对应位置。不用手动复制路径再去粘贴，省了不少麻烦。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba066n5sPDOb81QuGztNUn6Sh4P09pbyvw0Lb6k59ZVEeEWbx6TdaVK2naHG6rdfNYD59jt9ehvktfApYjQKEyRyca1BbK7Eqy28/640?wx_fmt=png&from=appmsg)

### 导出报告

扫描结果可以导出为 CSV 文件，方便你做对比或者分享给朋友参考。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba04ISV6QksiaVaxUnCUBnMoAj1fKJsRXzrtFj2SOa5g0iaaHGO3mfewzE8nbS5q2F5jqrxINRibxIWEmQrNevs5svCxOQ1vq2XsvZw/640?wx_fmt=png&from=appmsg)

### 扫描深度可控

默认扫描 3 层目录，速度很快。扫 C 盘一般几十秒就能出结果，不会让你等太久。支持随时停止。

## 常见问题

**Q：扫描 C 盘没有数据？**

A：Windows 系统盘权限较严格，建议以管理员身份运行，或者先扫描 `C:\Users\你的用户名` 试试。

**Q：会不会自动删我的文件？**

A：不会。DiskAnalyzer 只做分析和展示，不做任何删除操作。所有清理决定都由你自己判断。

---

这个工具是我为了解决自己的痛点写的。以前每次 C 盘满了，我都要手动一个个文件夹看属性，效率很低。现在扫一遍，30 秒出报告，哪里大一目了然。

```
https://soft.geek.cab/zh/software/diskanalyzer
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06dtEpEcUU8ZMo1WR6Q3kocFyyOnFASsaH7VyGTCj9LeTLQbPhIRzIIozVdYiawWiaT9RAKbyXmZt0a7dseYOSpY0F55YHvLWAA8/640?wx_fmt=png&from=appmsg)

工具完全免费，不需要注册，不需要联网，不需要安装。如果你觉得有用，欢迎分享给身边的朋友。

如果您有问题或新功能需要加，欢迎评论区交流！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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