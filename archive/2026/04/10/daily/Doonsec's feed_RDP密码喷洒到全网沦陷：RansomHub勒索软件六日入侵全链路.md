---
title: RDP密码喷洒到全网沦陷：RansomHub勒索软件六日入侵全链路
url: https://mp.weixin.qq.com/s/X3RUM0T_DATHdnsAJE_geA
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:17:07.919715
---

# RDP密码喷洒到全网沦陷：RansomHub勒索软件六日入侵全链路

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/PO9bjOzlHYCz9H0Nqqbs4JicBWNtbf4qAscGXuBWS6zKic1sOnQmroicHLYQEibiaoLzQib84rSyW5xeZ9v1h4vNcwGrHYWCFChxZziaxrIY5wjCXk/0?wx_fmt=jpeg)

# RDP密码喷洒到全网沦陷：RansomHub勒索软件六日入侵全链路

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一次成功的密码喷洒攻击，在六天内演变为全网 RansomHub 勒索软件部署——攻击者通过暴露在外的 RDP 服务器获得初始访问权限，利用 Mimikatz 窃取凭据、Rclone 外传数据，最终通过 SMB 协议将勒索软件推送到整个域环境。

────────────────

关键要点

• **初始访问**：针对暴露的 RDP 服务器发起密码喷洒攻击，持续约 4 小时，覆盖多个账户

• **凭据窃取**：使用 Mimikatz 和 Nirsoft CredentialsFileView 提取凭据，涉及 LSASS 内存访问

• **网络发现**：结合 LOLBins 原生工具、Advanced IP Scanner 和 NetScan 进行侦察

• **数据外传**：使用 Rclone 通过 SFTP 向远程服务器传输数据

• **勒索部署**：RansomHub 勒索软件通过 SMB 传播，利用远程服务执行，覆盖全网

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PO9bjOzlHYDRIeMuibcAibd8XBRss1cwlMAEQMDwaWRmfwsp4zmAA52ziceFmw3u23XTwKnzaD8nGV3N1zZPlCNEA3kSMov3DiczD6n9d1cPq2Q/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

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