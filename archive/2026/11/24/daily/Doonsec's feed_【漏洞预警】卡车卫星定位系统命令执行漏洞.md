---
title: 【漏洞预警】卡车卫星定位系统命令执行漏洞
url: https://mp.weixin.qq.com/s/lbxXL2c4xWm8xselJYqWjA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:45:29.013929
---

# 【漏洞预警】卡车卫星定位系统命令执行漏洞

# 【漏洞预警】卡车卫星定位系统命令执行漏洞

剁椒Muyou鱼头
剁椒Muyou鱼头

剁椒Muyou鱼头

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/92Yia6FpSFA2QiaAzq0Dumm39PGIsC7mk4lX6c4yYnERUGvnHo7SQreGiboYBj0ib7TlaUx1DKtEGlU8mqS9ZtLZRw/640?wx_fmt=gif)

**阅读须知**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/92Yia6FpSFA2QiaAzq0Dumm39PGIsC7mk4lX6c4yYnERUGvnHo7SQreGiboYBj0ib7TlaUx1DKtEGlU8mqS9ZtLZRw/640?wx_fmt=gif)

**本公众号文章皆为网上公开的漏洞，仅供日常学习使用，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/92Yia6FpSFA2QiaAzq0Dumm39PGIsC7mk4Z7hc6oGV6C6IwibzfQUM1oq1yUciadAKQ3Ap29o8GGnBU52wXgSSicBxQ/640?wx_fmt=gif)

漏洞描述

    卡车卫星定位系统是一种基于卫星通信和导航技术的系统，用于对卡车的位置进行精确测定。洞利用链的核心是通过upload接口的路径穿越与文件校验绕过，把恶意wmic.bat写入Node进程的工作目录CWD，随后通过taskFileList接口以相对路径exec('wmic ...')起进程，cmd.exe按当前目录优先于PATH解析，优先命中CWD下的同名批处理，造成任意命令执行，然后通过download接口文件读取通道回显，最终实现RCE。

漏洞详情

1.卡车卫星定位系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FEWcqzYgxo8BTX5H5AWKHsG4lZHbGib2z7WFO2wZZb24HJaN2JrTmJQ5nROv4QsxJrAkZWJMrn3YmAibeBWWak6mM02scNT4amVfTSKdIQNac/640?wx_fmt=png&from=appmsg)

2.漏洞复现结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FEWcqzYgxoicvvlqByRa6CiczGDYN7qUvppRsK37AhhJkCPKZOhA2Tba15PSSK1BFHK41CrZ8s7zmkic1b9TiacM4S1p2cYB97ZHo17dTQchGvc/640?wx_fmt=png&from=appmsg)

修复建议

联系厂商获取升级补丁修复漏洞。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/92Yia6FpSFA3QZ2ZMP7Q5urLdMRypjGymwnDtUS5Xjq1N9yn2aZG2ew66sCg9G7fK8auy2l85VrjGx7Yy1snyXA/0?wx_fmt=png)

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