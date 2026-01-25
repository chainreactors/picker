---
title: 电脑中挖矿病毒程序   手搓溯源分析直接定位到人！
url: https://mp.weixin.qq.com/s/6t_B1wB03UkTJds6KDlohw
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:51:44.376684
---

# 电脑中挖矿病毒程序   手搓溯源分析直接定位到人！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cm9mPvQVqibGdSCtKa1lUEzDM8vAswzo2LA8a3zSNZ0S6pJricuf8F3xQ3dec0Jziaesz9ERpIk6zeOoOKric2x0Pg/0?wx_fmt=jpeg)

# 电脑中挖矿病毒程序 手搓溯源分析直接定位到人！

原创

老兵
老兵

网安守护

![]()

在小说阅读器中沉浸阅读

### 阅读须知

文章仅供参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他！！！

### 前言

朋友抱怨自己的服务器非常卡，因为存储了很多项目资料和集成了众多环境。作为好友，我自然义无反顾地帮他检查。原本以为仅需进行简单的杀毒和文件整理便足够，但最终这个过程花费了不少时间。正好借此机会记录下整个过程，并写成这篇文章。

### 清除病毒

询问朋友是否下载了什么或在电脑上搭建了些什么，他回答说不知道，让我自己检查。当时我真想通过远程桌面（3389端口）过去给他一个响亮的耳光。但最终还是决定亲自处理。打开任务管理器，立刻注意到几个可疑的powershell进程。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7S7GHianvA5CIgB52NSddrvwLpxiaQndLm5OncxujFpRn4B4nSm1pia0g6w/640?wx_fmt=png)

PowerShell进程的占用率高居榜首，但具体执行的命令尚不明确。此时，利用WMIC工具可以查看进程在执行时的命令行参数，帮助进一步诊断问题。通过以下参数获取相关信息：

* **Caption**: 显示进程名称
* **CommandLine**: 展示具体的命令行参数
* **ParentProcessId**: 显示父进程的PID
* **Process**: 表示进程的PID

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7Suc71PxEkoo2ibkITcHO6fOv2iaEpglIfneTg5OUU5JYqTt4AKibXGicTxg/640?wx_fmt=png)

PowerShell中执行了一段被混淆的代码，这不是正常程序的典型行为。市面上有多种工具可以用来分析这类情况。可以使用火绒剑、ProcExp（Process Explorer）、或者ProcessHacker这些工具来查看命令行参数，进而帮助识别和解析这些可疑的操作。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7SzxTYCvTROynjCXmImxkg0JjBM0Tw8WXkyt7zsSNQUpTicZqjybxIjOA/640?wx_fmt=png)

使用火绒剑终止了PowerShell进程后，如果该进程再次出现，这表明存在一个守护进程，刚才终止的很可能只是一个子进程。此时，应该终止整个进程树以彻底根除问题。需要定位到PowerShell的父进程，并结束整个进程树，以防止潜在的挖矿程序重新启动。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7S7GHianvA5CIgB52NSddrvwLpxiaQndLm5OncxujFpRn4B4nSm1pia0g6w/640?wx_fmt=png)

使用wmic命令，找到相关进程

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7Ss2n28unYUpGHbWOWOgibtnpASl5Siaht8sCPLgebWwTiaQ4ULVRKRjCyQ/640?wx_fmt=png)

已确定进程ID为3616的进程。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7Sw9ueicahtBib8hUQguzCo16khPY3hNZnFcqWsuLxOHCEmh1D1IOWV96w/640?wx_fmt=png)

已定位到进程ID为3604的进程。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7Sdvnk8KTqT0TPkh2t0LW7XY0qic8oQ4h52PgZ8iaGUy9aJNrKW0XBHRDg/640?wx_fmt=png)

已经找到了进程ID为3500的相关联进程。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7SMYONNNYq89dYdfNIRbf0438RlKiay9tuia3ibbhzu4meGXYaLLNlaFnSg/640?wx_fmt=png)

以火绒剑工具为例，检查进程时发现，在列表的最下方，有5个以PID 3652运行的PowerShell进程，这些都是子进程。同时，PID为1972的scvhost.exe则是所有挖矿程序的父进程。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7SthRnicTU2ticMcEX24zibfuHzOyxtXNK9ichEaHsXd1FV6BMusbMmGFXNw/640?wx_fmt=png)

为彻底解决问题，可以直接结束整个进程树，这将同时终止父进程和所有相关的子进程。这一操作可以阻止挖矿程序的再次启动，并清除所有相关的恶意活动。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7SF6DEgXDTw5eP65xKxfK8yITPIwhOvPT0zq2QH5hyh9M88Hfy82PtbA/640?wx_fmt=png)

清理工作完成。

### 审计日志

关键在于找出是如何被侵入的。我特别检查了RDP日志，并查阅了安全日志，包括4624（登录成功）和4625（登录失败）事件。结果确实显示出有成功的登录记录。

![](https://mmbiz.qpic.cn/mmbiz_png/WTOrX1w0s54Y7ZB74Dtm6tdJwQv9bP7SL0udQnpic5XW2Kc424UgicylSHXx4fnXsIETbKoCacrmlVRiagGl9BuDA/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/cm9mPvQVqibGd65c3eJPHrquKia0JIOKTLze61HQgWw3d7nPyZK2v12ModP3KMy5HxuhNTplVWfia0wwiaGicGtvORg/0?wx_fmt=png)

网安守护

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cm9mPvQVqibGd65c3eJPHrquKia0JIOKTLze61HQgWw3d7nPyZK2v12ModP3KMy5HxuhNTplVWfia0wwiaGicGtvORg/0?wx_fmt=png)

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