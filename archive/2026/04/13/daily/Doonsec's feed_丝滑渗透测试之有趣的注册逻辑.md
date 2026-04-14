---
title: 丝滑渗透测试之有趣的注册逻辑
url: https://mp.weixin.qq.com/s/17mVrWcnk4bafTDJx2CDeQ
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:39:37.005106
---

# 丝滑渗透测试之有趣的注册逻辑

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/72I8gAalpPWkzozWCRKWwb9ILfibHTibJxricJaSJqtUbtiakImwuOSDKuBuM7I1VhzeO2nRSq2br3hRLwh9233C97ian9YibdBIevI3N3UHibzcdE/0?wx_fmt=jpeg)

# 丝滑渗透测试之有趣的注册逻辑

原创

pippybear
pippybear

安全无界

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

声明：请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

旧饭新炒，哈哈，这是很久之前的一次授权渗透测试了，目标是一个学习系统，这一次比之前好多了，虽然依旧没有给账号，但是简单看了一下系统，它有注册功能呀，舒服。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPX3f9ey6PzMKKheiaf1bkFDmVCuuw81CKWgXTXyY0EMmSH1gB9abXlvhxgDwB8iatheQS7EMB3ibncG6RVbYkBhbOZV8rxIbWQxv0/640?wx_fmt=png&from=appmsg)

废话不多说，直接开始正文，这里是工号+密码的组合，直接冲去目标客户各网站上检索工号，很幸运，在几个页面上找到了工号，构造差不多是年份+4位数字，直接生成工号列表撞库一波，运气不佳，没有找到弱口令。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPWz96vCVjCHXmk3ce62YUdy2xmLWH8444uOgHnUCfyjxLzRMibgmY6It8lqibXwt7goB79onRO8680NicGib7xUybyja9GD6rpFOfE/640?wx_fmt=png&from=appmsg)

既然不成功，那就先看看注册功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPWgDGiaaVd5dveAXe7ibbY91UIlLFMda80iaUYP4cdCPkpoA7iaIJG0B0x4k5Ar2sMnx2ucibAp7kMCiauIRicdHSy9FnVrZY0ZicrIa8E/640?wx_fmt=png&from=appmsg)

需要输入工号、姓名，还好前面知道工号的构造，这里直接遍历跑一波，发现工号不存在会直接提示人不存在

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPUVtJo8bCaI8c5TsQMv3e6BJicR7VwqkJ4DIm8sefBB6h4XBa1tqkicQ7ic3el6cUkZ8MlDwNliaibgULQKaaGeicB1icTc4UbEtOnOB0/640?wx_fmt=png&from=appmsg)

存在则可直接注册成功，YYDS，直接注册进入系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPWbOiaicawibkQwWKqjmncXkUDBUojn9HcZhTVEAUnibRwovxzHe6hUmpg6ZwV8hdxHsA16HOMdZP5FgdhIU5zyibjMkjnFZmGD7Kps/640?wx_fmt=png&from=appmsg)

使用注册成功的账号进入系统，见证奇迹的时候到了，发现登录进来并不是我随便输入的姓名：test，似乎是一个真实的姓名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPX4EzGbXdoFicRkuDwfVGT5dVRZqpJ5WYcaZlsE2ptFd5Zv2W5libvcRRmmK5264riaq0ZxUZTia5oIibLHuickv6UmNayD5ZqCyR0NU/640?wx_fmt=png&from=appmsg)

点击上传证照，发现这里居然是有数据的，包括该工号的证件信息以及一些敏感数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVvxRZ8LxTia6dIiaQzw4HxHS9ex6Sl9sOiaIAjBA60zEydlK9bIwyqhDDNjtibQzzDNGx1IGqicX41MvHuUMeVgdTKFiccMuSyCVfMg/640?wx_fmt=png&from=appmsg)

神奇了，大概捋一捋，估摸着这里有一个比较有趣的注册逻辑，即使用已知工号注册，这里不会提示账号存在，而是直接与系统中该工号的员工信息绑定，好家伙，直接梳理梳理交付报告。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPXSdicKwmiaYPa550l2uL14t8BaMOiaam0CiaAfRwrGicdCWLLnob3apJ5kEkYRqALzWlHqv7tNcPicFPIS8hhfsoFLTuMRrYdojNthA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gRWFX6SiaQE368qzz3ruUmbnpAzmoIcmWYrXOnic1DzRllicgLMZ3NZ49q4CG4Tq7mmIkL8oyibfLfMqw/0?wx_fmt=png)

安全无界

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gRWFX6SiaQE368qzz3ruUmbnpAzmoIcmWYrXOnic1DzRllicgLMZ3NZ49q4CG4Tq7mmIkL8oyibfLfMqw/0?wx_fmt=png)

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