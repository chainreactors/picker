---
title: 【游戏辅助浅析】你的号成数据号了吗？
url: https://mp.weixin.qq.com/s/v3X9OURlxzcXRR4GlGHXww
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:34:40.979548
---

# 【游戏辅助浅析】你的号成数据号了吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qBTUpGj7JT33PicSW0AEbG21hPmY1weuTY9cvmcmwyyxPufJqtNkJMJpHDYYKXPITXSZnicXl5icUkyk52vCiahyiaXmUAcufWiaIJLnaez9cZcro/0?wx_fmt=jpeg)

# 【游戏辅助浅析】你的号成数据号了吗？

原创

不知名选手
不知名选手

法克安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| **声明：**该篇文章仅分析黑灰产在外挂辅助方面的产业链，其中相关exe样本以及逆向还原后的代码不会提供 |

# 1.前言

相信三\*洲\*动各位都玩过吧 物资透应该都听说过吧,不过现在一些黑灰产也盯上了这方面，可能用过科技的或者自己写过科技的都知道，像内存类科技，基本上直接一个注入器，一个dll文件直接注入。甚至你自己手动直接注入就完事了的。然后进游戏按特定按键显示菜单，再按对应按键开启对应的功能即可。可是今天文章所写的这个科技就不一样了，他先把你的号拿了，才在dll中又外链到黑灰产的服务器上下载真实的代码注入。这个时候你的号已经传回到黑灰产团队的服务器上了，转头没几天你的号就变成某某卡网上面的xx州数据号了。你这个时候还傻呵呵的用着他们的科技，还时不时说真好用。

# 2.功能逻辑

准备工具:ida+codex以及VsCode或 CC Switch

1.某中国黑市花几元钱购买的一个几小时测试卡（目的仅为了拿到样本下载地址，否则人不会给你发）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qBTUpGj7JT2xibTUsTSULT6tEZ1YHaMtERJZzT2bQ1xhGciayd88ODLU7w8U2LMk3RZ9y0MS5VVHltS7hVcdxrJhBXN6WtaK8csquEicqOiapAI/640?wx_fmt=jpeg&from=appmsg)

2.拿到下载地址和卡密过后将样本下载下来，发现就是一个txt文本以及几张教程截图

![](https://mmbiz.qpic.cn/mmbiz_png/qBTUpGj7JT3XDwLLay38RdHbia0txiaOkOVBM1FGeqFibDU3lq8YdThwHjOyz5V2GHiciceCEgDuAr1bdrTuRegrO9Mn0fdKG36xicLlzqJfqMBxM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qBTUpGj7JT0Leqic0WXA2Nh8xjEJ74avkibp41RSameQDNcoWzFoJ5eicJUqKgeJWPksnjZq0r2zImXyib7PqBkaVl7FQA8uU1r3oHyLQ1HVDt8/640?wx_fmt=png&from=appmsg)

看到文本中的iex指令大家应该都看得出来是加载了一个powershell脚本

![](https://mmbiz.qpic.cn/mmbiz_png/qBTUpGj7JT3CBJeibib7IMol2PT8C048JsW2n9RotoyjhWquckTQ6yN8ZYxzibj3Hh7vXgEk7ALShNSiaWga8kPBzEiaYy74mq1ptQuDjl7EaOro/640?wx_fmt=png&from=appmsg)

随后打开这个ps1脚本一看，作者还贴心的给你把注释啥的都标注上了，这里就不过多的贴代码了，直接找到关键点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qBTUpGj7JT2ft2b7qAjJuM26bPibJN54r16Ih7Z140po0GKSbUWLpSoyib6tcUJXbSPuuMR4TiaicykpicOFI3AHFEiaEicIvibRuKbiar9jm99l95LM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qBTUpGj7JT1z826sgKicHaFw0kEnpZk4fRR2LFKsDuYxsFUQjsWHL8ib6yvpCa9ZSHHwEdUVwYiapYDPMYWfVicNC9rNDt7IszaYHC6ZgwibskDo/640?wx_fmt=png&from=appmsg)

结尾部分定义的dll文件，去下载下来后导入ida中，搭配codex简单分析一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qBTUpGj7JT2mu4hJ1H1flKVRprzkI8xSKtZ2rOpZOUIfT0TFc8O2DDicPdGWScdY2QtmCJiaOFeJQeYq7aCibJRnYM4b4lHxAADxcVKmUhtefw/640?wx_fmt=png&from=appmsg)

看到我标注红框的部分了吧，刚好也对应他图片教程的部分

![](https://mmbiz.qpic.cn/mmbiz_png/qBTUpGj7JT2WjtL9DG9DKeovre7oibT2CqnxvHYrfK9fZYNAF6hkq6E6I2sxqWX5AX3OibFZ29ZhotWPkdLeuhkeSaMoNNk6rVhjLIRxRQhEI/640?wx_fmt=png&from=appmsg)

这很大的一个疑点在这里摆着，正常来说就卡密验证，卡密解绑 等着代码注入进内存 然后开启游戏  开始背上了行囊，突然在这里让你扫码登录后才到输入卡密加载科技的包是偷你号的。这么一说，整体的流程就用这么一张思维导图展示吧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qBTUpGj7JT3oQcY8fgNnZiaYY9ibOoVlEAIpCaRQFTrPdDoeCU5Lb7D7nqdVak9YUg5e4wuqSowAZsEyYBBgDI1Z56icjLcG5ibQkSHYic5dzh5c/640?wx_fmt=png&from=appmsg)

# 3.DLL分析

一句话总结:一个伪装成"微信扫码登录组件"的 DLL 文件，在你扫码登录成功后将获取到的数据上传到目标服务器，验证卡密正确过后下发helper\_stage1.sys驱动文件，随后将加载驱动文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qBTUpGj7JT28Yue6iboAhSGenHEjibeNpykc2y1t6jXQE1T5EYbnsIOcaNXBlh5zddDcP5aoEibVroE1fzoLXdOkTYWXicxib00vjibGLklHVwLIU/640?wx_fmt=png&from=appmsg)

# 4.总结

别为了一时的快乐，让你的号变成数据号出现某某卡网的黑号专区中

(虽然不知道一条这样的数据能卖多少钱，但是这样的东西在中国黑市遍地开花)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/WqibHnoQAhZewx7WLBor1JKJZSQ9thbqfEMgpZYyMQ9mn2tD5U61CVncY4EY549yZsvWHqor2knG7KbicdKJV0Xw/0?wx_fmt=png)

法克安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/WqibHnoQAhZewx7WLBor1JKJZSQ9thbqfEMgpZYyMQ9mn2tD5U61CVncY4EY549yZsvWHqor2knG7KbicdKJV0Xw/0?wx_fmt=png)

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