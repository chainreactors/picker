---
title: linux提权漏洞喜加一
url: https://mp.weixin.qq.com/s/IaBbKIaNWLzJ6xda39Gwqw
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:43:19.680474
---

# linux提权漏洞喜加一

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAhPfxg7rmjP8hbfz2OuBM4Iic7lsvc31Mcb4JkwiaYvTFpTIbbqJIOVQaSfdCkkfMG3POJEVqapUgUfpKiatfTkydjEibc5yRDxxh0/0?wx_fmt=jpeg)

# linux提权漏洞喜加一

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAgWxkVrnqONjRQE14eWwx2XiaMbY4Wxu2Pzk4ziciciahD5YaIw5iabZQrbtr8OkHFgv5aAiaDZacK8qLSGwslZPBFkeblO9z1r3dEss/640?wx_fmt=jpeg&from=appmsg)

最近公开的 Fragnesia 项目，可以看作又一个围绕 Linux page cache 的本地提权利用样本。攻击者已经拥有本地代码执行能力后，借助 Linux 内核网络与页缓存处理逻辑缺陷，把只读文件的 page cache 内容改写为攻击者控制的数据，最终借助 setuid 程序执行 root shell。

从项目自述看，Fragnesia 被作者定义为 “universal Linux local privilege escalation exploit”，其核心是滥用 Linux XFRM ESP-in-TCP 子系统中的逻辑缺陷，对只读文件的内核 page cache 进行任意字节写入。项目说明还将其归入 Dirty Frag 相关漏洞类别，并强调它与 Dirty Pipe、Copy Fail 一样，属于“把只读文件在内存页缓存中的内容变成可控内容”的攻击思路。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAiapdPryJ6bFxBoTM6j6SE2t1qv7gMe87hdyx1vqicomrgvdNIvSHXY9wwQKufxls8d0aBY9pI0WG0UkIqmvibZkUCrf0nxWlURiaA/640?wx_fmt=jpeg&from=appmsg)

https://github.com/v12-security/pocs/tree/main/fragnesia

受影响版本 所有受 dirtyfrag 影响的版本均受影响。

任何未包含此补丁的版本：https://lists.openwall.net/netdev/2026/05/13/79，即 2026 年 5 月 13 日之前的任何 Linux 内核版本。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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