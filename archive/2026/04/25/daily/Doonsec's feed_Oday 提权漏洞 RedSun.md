---
title: Oday 提权漏洞 RedSun
url: https://mp.weixin.qq.com/s/kqJ__HdcyNIbp8dLNFpG7Q
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:57:34.570854
---

# Oday 提权漏洞 RedSun

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J7CSmJcRR8kqKjmzGBaHJB08PxF0HLeEPeNu2lC8GwxEkQUGia6dRBphOp7JFwPNib2hQEyiclIzD8iaKnKyyiaUWMfhpwwEr7zp52Vxsbtt0l18/0?wx_fmt=jpeg)

# Oday 提权漏洞 RedSun

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

通常情况下，我会直接放出 PoC 代码，让大家自己去琢磨。但这次不行，它实在太搞笑了。当 Windows Defender 出于某种愚蠢又滑稽的原因，检测到某个恶意文件带有云标签时，这个本应保护系统的杀毒软件竟然会把找到的文件重新写入到原来的位置。这个 PoC 代码正是利用了这一特性来覆盖系统文件并获取管理员权限。

我认为反恶意软件产品应该删除恶意文件，而不是确定它们是否存在，但这只是我个人的看法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8lPCvDb0dVVE0b1iciat33ib7cy6Pn0iahE14MgUvdyMmibdf0XibC6qWBSAgZ92PfTyhLoQ3cRMYXFOPzjrnB1wnkAUgSWV33eVVghM/640?wx_fmt=png&from=appmsg)

https://github.com/Nightmare-Eclipse/RedSun

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

Khan安全团队

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