---
title: 一次外挂程序的分析-Bypass
url: https://mp.weixin.qq.com/s/GhUwp_kkpsoPRDGmkTiFCg
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:12:13.174436
---

# 一次外挂程序的分析-Bypass

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y9Uh816EzOZiao1yjXPS29enkm2QzUxuDgiaakRKxzckz1qSpDHadYE58IfJTSMvckUbOtxE6qHQWbgXicViaiagd5pgyGjXSFVibunPHVUxROuFc/0?wx_fmt=jpeg)

# 一次外挂程序的分析-Bypass

原创

Pikaciu
Pikaciu

Piusec

![]()

在小说阅读器中沉浸阅读

## 免责声明

> 本文仅用于技术讨论与学习，利用此文所提供的信息或工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任!

# 一、前言

本来在愉快的玩游戏但是突然就发现了外挂狗，我从小到大最恨这种开外挂的，尤其这种开外挂还打不赢，我就去寻找这个游戏的外挂，就诞生了这篇文章，这篇文章只是简单分析这个外挂软件的运行流程，基本没有代码分析。

# 二、分析加载器

这个程序是没有进行任何加壳的，通过 IDA 获取到了源码，这就是一个加载器暂时还没有触碰到内存，最开始通过 ipconfig /flushdns 清理了本机网络环境。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9Uh816EzOb3zHBZsFBOv6WT1TjjFQneTlH2AicmheXqVfrAwian4U6gER2LfXv8KqJ2pl2YT44fWKG20SI5XdbsdufvsRIX1IzNCicS44LQxU/640?wx_fmt=png&from=appmsg)

跟踪到做的第二个动作，远程访问了一个地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9Uh816EzObp189KSLWRqCDSW78e5eX7icylM9o8K1CNmxsepxfA8T4Udcam7zJq4kYh6q6jIDrwKCwwJUsevia7b99ccsjLOG2E2NToIduAs/640?wx_fmt=png&from=appmsg)

访问远程加载的地址，可以看到是一个服务器地址配置，这里是做了一个配置隐藏

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9Uh816EzOYoiaGRkoia3byfiaog2pOcFdASrRNtJz39xx0kaEJ9PWM4Pgib6q2oSDTKkCT5iaS0JF26MHmGwI69enibIz1YIMicO27kkbbXjLj744/640?wx_fmt=png&from=appmsg)

下一步动作现在对 sys 文件进行了一个下载，落地。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9Uh816EzOYtWZQSkd1lVvmKSyK0A4I3XSXgVa8W6PadKUyKsGp6iaLg5vc0FJBcEbQsprf2lvkVvvmicxYohBhPurOchLZXuRyYKnwdByIIk/640?wx_fmt=png&from=appmsg)

创建驱动服务，加载成功后会自动清理痕迹（删除落地的.sys），这里再说明一下这里远程加载的链接是白名单。

# 三、衍生免杀

这次分析外挂主要是分析的流程，这个流程也很符合在免杀中的远程加载，这里再简单说一下这个外挂软件的流程。本地这个程序就是 C2 的加载器（lodaer）-->   远程加载 config 配置文件（远程加载 key） --> 远程加载恶意 sys 驱动文件（加密后 shellcode） --> 绕过游戏反作弊（绕过杀软）

通过这个逻辑写的免杀目前是能过火绒、360，其它杀毒软件还没有测试。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Y9Uh816EzOa0iakGxiccPCiazuHYibestsj5II0hoVY2SzsxspuEXpvXY0ibD72RjUawB4wxqcUHyEW9BZQAl8XloMVlmmLX7gNOquQTia2mJwb1I/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9Uh816EzOYCtk26WmiaLicibGNib9po3kADuzpWyGmFf6lVku3y6grVCTvGfMQlK9g6aqGBIwWntM3zY24xs3heick1mM393alFhJARwGISRUr0/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/cYTGgX1JI0VMVyhARJslFSMVkhhmrX7g0f09df5792YsUCuSF5q7fJLNRxa1yPicm0VVkES8mzcyLNp6MncdF3Q/0?wx_fmt=png)

Piusec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cYTGgX1JI0VMVyhARJslFSMVkhhmrX7g0f09df5792YsUCuSF5q7fJLNRxa1yPicm0VVkES8mzcyLNp6MncdF3Q/0?wx_fmt=png)

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