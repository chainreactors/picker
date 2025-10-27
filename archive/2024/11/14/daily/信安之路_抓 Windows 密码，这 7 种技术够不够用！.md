---
title: 抓 Windows 密码，这 7 种技术够不够用！
url: https://mp.weixin.qq.com/s?__biz=MzI5MDQ2NjExOQ==&mid=2247499677&idx=1&sn=51f875154188a21386dad198bd29e380&chksm=ec1dcfb5db6a46a3dcd462b75704ce11e3b8ca9f5829f53254a73f06563fa49efac0698e210d&scene=58&subscene=0#rd
source: 信安之路
date: 2024-11-14
fetch_date: 2025-10-06T19:19:22.402408
---

# 抓 Windows 密码，这 7 种技术够不够用！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAfelrH4jneuT05mcu7xMk0pIQpDyrCdLMT7sh9lMia58GjTFfxhiaaIQIeR2C5ILNEkhqvy5zZcNDwlA/0?wx_fmt=jpeg)

# 抓 Windows 密码，这 7 种技术够不够用！

Offensive-Panda

信安之路

内网渗透中，获取到 Windows 系统权限之后，抓取本地哈希是必不可少的操作，今天分享一款工具，集成了 7 种转储 LSASS 内存的方法，工具地址：

> https://github.com/Offensive-Panda/ShadowDumper

运行如图：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfelrH4jneuT05mcu7xMk0pIO9mX06tw4ia6paOqhs2Hv9picpWBf42f211iaxdrfiayrJTFIZBKtzEqDg/640?wx_fmt=png&from=appmsg)

未提供任何参数运行程序，会要求你输入所要指定的方法，参数为 1-7，功能分别对应：

1. 使用解除挂钩技术转储 lsass 内存以注入修改后的 mimikatz 二进制文件。
2. 使用解除挂钩技术转储 lsass 内存以使用 MDWD 的直接系统调用注入二进制文件。
3. 使用简单的 MiniDumpWriteDump API 转储 lsass 内存。
4. 使用 MINIDUMP\_CALLBACK\_INFORMATION 回调转储 lsass 内存。
5. 使用进程分叉技术转储 lsass 内存。
6. 使用 MiniDumpWriteDump 的直接系统调用转储 lsass 内存。
7. 使用直接系统调用转储 lsass 内存（本机转储，带有离线解析所需的流）。

随机选一个，比如 5，结果如图：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfelrH4jneuT05mcu7xMk0pI3kPEPMjf3L70oOdic6pTm4ylibo7piaLVzKg06mic3ibRk1xz1lmj8ticWoA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfelrH4jneuT05mcu7xMk0pI5Pbh28hwQX9he0ogZ8PrZdIQZ1fd1fxUNZaElT9QcdDVBsAWGLGABA/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

信安之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

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