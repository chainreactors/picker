---
title: 使用Flipper Zero玩转汽车UDS诊断
url: https://mp.weixin.qq.com/s/78vVQ7Cifbj2b_FXwcqmrw
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:27:52.969798
---

# 使用Flipper Zero玩转汽车UDS诊断

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ic6JmDgG0m6Gycxc58MOtkfjibia9icBSbLYOUyInxS8xQHxD41O7zyKa7U3Eo1N1Nj6iaibFLMbm3ySsN3GSKQUscHbjMozQvfV1aAYyyqoSb9Ck/0?wx_fmt=jpeg)

# 使用Flipper Zero玩转汽车UDS诊断

原创

yichen
yichen

陈冠男的游戏人生

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ic6JmDgG0m6F8W93YZ5ibcCqGYdsTsarE8KkqqTJuBedfQZTbevib0ATkc4d05bD2BV4EvCB3rCx6Lw87MO4dPXMBcnhUGQXdUZ59je1fIYv38/640?from=appmsg)

前段时间为了给汽车安全白帽黑客大会捧个场，攒了一个 Flipper Zero 的小工具，使用 MCP2515+TJA1050 实现了 Flipper 进行 CAN 总线通信，并拓展了一些 UDS 诊断测试的场景。但时间匆忙，只是用杜邦线和现成的 MCP2515 模块进行了测试，没有真正做成 Flipper Zero 插件的形式，分享时还是个半成品

![d6323fcd45dd0e2d98c8c5145adecba5.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/ic6JmDgG0m6FnWQf14mKrRFZd4prEZ0NFxdajicuIFko3hJXNJHkFQTQyG6NhD85Qx90NKKcXykRiamk1nGV1OA3OgmR22jFOTGpPSHrN92oicU/640?wx_fmt=jpeg&from=appmsg)

    最近收到了主办方寄过来的证书，仿佛听到了师傅们催更的声音

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ic6JmDgG0m6FHMysKDrnqibvicuE1N5mwmjO8aMp1O2E9PdiafItEBP3Aud34B65mMC1e8cYc3gkRXt1zjUgkicQUHGS5tkiaZFBcialcRwQWgbS8I/640?wx_fmt=png&from=appmsg)

    于是乎打开嘉立创开始家里创，根据现成的 MCP2515 模块将整个板子画成了 Flipper Zero 插件的形式，特意选了一些比较容易焊接的元器件

![1b24efab6995d97c36efe875c9c89ee6.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ic6JmDgG0m6FkUHPoqqbPC9qBca6tKCkYLhuWol1icPeTCFXGibth8ABHWYicicwIicibXouNOkR2HRV7WTmQabgLkCM2SnQhe4WmdQa6D1JrqBs2A/640?wx_fmt=png&from=appmsg)

    简单介绍一下这个小工具的功能：主要目的是使用 Flipper Zero 对 CAN 总线 UDS 进行自动化探测，通过扩展板借助 MCP2515、TJA1050 芯片实现 CAN 协议收发，可使用 UDS 协议进行 ECU 存活扫描、服务探测、DID 爆破、安全访问算法测试等

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ic6JmDgG0m6GGqCysBV3OfYicTickqPQHkYac9zPibhvdm8BicKDFfmThmqBybnzkHYdPlr02jHAjkdUVkp8tcz3XB4FdvjWu8cn4tcf3xjSH3pw/640?wx_fmt=png&from=appmsg)

    平时测试人员要钻进车里抱着电脑接上 PCAN 等 CAN 调试工具，对于身体非常不友好（确信），在代码中添加了一个 ALLINONE 模式，可以自动执行当前实现的所有功能，因此现在只要把 Flipper Zero 接好线放在车中，测试结束后直接在日志中拷贝结果，使用 AI 编写脚本解析出报告即可

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ic6JmDgG0m6HibkhzgiaFdKSia9ZgLFuEYXia54St120QiaSkCia36KfibicE1xhfrjJD4QO95HGf4JTfYk7k1k4P90D8WtU5lO5zPFUMHjNVlS22AEM/640?wx_fmt=png&from=appmsg)

    第一版已经打样回来，测试发现在 Flipper 仅使用电池供电情况下 MCP2515 和 TJA1050 共用 Flipper 的 5V GPIO 输出会有一些奇怪的现象，因此调试后重新画了一版，调整为：使用 3.3V 给 MCP2515 供电，使用 5V 给 TJA1050 供电，目前飞线测试没什么问题，等第二版 PCB 打样回来测试没问题就把嘉立创工程开源链接同步在 GitHub 上~

https://github.com/yichen115/flipper-CANHACK

![](https://mmbiz.qpic.cn/mmbiz_png/ic6JmDgG0m6EP6hxLmOibic4dA4XlQwKyBLiauYHJG53Appm3VQ85gJt20RDKicXEvB6lLKfaMWQQyibeLAZ1sS0c5uKZYs0EnpraQ2icOQstkjEeE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/df1X0NvQ5KmKUiamLXUCGGibBkrnib54ia4ySDKrUytAichwcZQJ7YdcW79BicYmQ8wdaOMoeuhDZMQy4NE6jTI9L1kw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/df1X0NvQ5KlT6S09SqgERJp08caURiacQG9gOhGepeXGBjNBw8GPO4WogWtfykqOIDHZnbhf95bUz5MgNQrQSKQ/0?wx_fmt=png)

陈冠男的游戏人生

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/df1X0NvQ5KlT6S09SqgERJp08caURiacQG9gOhGepeXGBjNBw8GPO4WogWtfykqOIDHZnbhf95bUz5MgNQrQSKQ/0?wx_fmt=png)

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