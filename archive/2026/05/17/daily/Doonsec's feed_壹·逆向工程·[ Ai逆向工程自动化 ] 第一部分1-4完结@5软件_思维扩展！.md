---
title: 壹·逆向工程·[ Ai逆向工程自动化 ] 第一部分1-4完结@5软件/思维扩展！
url: https://mp.weixin.qq.com/s/7fNtpNk7fKvdHhU1Y8MJXw
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:06:33.081177
---

# 壹·逆向工程·[ Ai逆向工程自动化 ] 第一部分1-4完结@5软件/思维扩展！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icfnkibn16VejxT92GQg9bBjSS9IKl8CLN6zRqbyszPfibdRlHWrjBp4uPxPcopVTLxticBDCQMEDEINMUSklmHa4BuPmicOu6C2VOichT4rdxo2w/0?wx_fmt=jpeg)

# 壹·逆向工程·[ Ai逆向工程自动化 ] 第一部分1-4完结@5软件/思维扩展！

原创

bl0ckdev
bl0ckdev

Esn技术社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VejahAXb1Lq5uIs8MOmaRMzicTWQqdCACn6rfiaM9iadO8NIJNAhQ3oSnqyUibWzyDyQ8MmWuWODK0Hmur3gibZJnHaJO98sTmrsze9s/640?wx_fmt=png&from=appmsg)

警告：

在开始之前，我必须声明我并非专业人士。从基础的逆向工程到Ai自动化逆向工程需要不断的时间去探索。

[零·重新校准[ 黑Ke逆向工程Ai自动化 ]  初始|介绍.篇](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247493014&idx=1&sn=bc32ed54671f105dc2a713451bd8a4ae&scene=21#wechat_redirect)

* PuTTY  [ ssh/可能很少用 ]
* Wireshark [ 非联网目标不使用 ]
* ### Microsoft PowerPoint  [ 做图/PPT ]
* ### Deepseek  [ 对黑客技术最友好的大模型 ]

下边的等级排序是我自己结合Ai以后个人认为合理的排序。

1. 初学者 （Ghidra）   → “免费”
2. 破解者   (二进制忍者) →“中端收费”
3. 商业逆向( IDApro ) → “Pro收费”  个人版免费

---------------------------------------------------------------

ghidra\_12.1\_PUBLIC\_20260513

我对大家有一个建议：

1.如你现在的配置4-6Gb显卡显存或者是伪8GB的显存显卡,在正思考是否更换显卡去研究人工智能逆向工程？

2.如你现在的Mac或者其他本子不能跑8B模型,正在思考是否要更换笔记本的时候,先等待一下。

你需要思考“人工智能”的时代你到底需要的是什么！Ai-Agent并不是适合普通人,所以以普通人的立场你需要知道你到底要的是什么？如果你和我一样从渗透测试增长到红队后专注恶意软件分析和漏洞研究与利用。

如果你想要动手开始“逆向工程”那么就先利用#ghidra# 去逆向一个软件,不管目标是什么！只要不违法,根据LLM的提示词一步一步的跟进。不计一切代价,只要能拆了就好。推荐研究单击游戏。因为#Deepseek 内置了好多超级思路和方法。

通过#ghidra# 完成一次软件破解以后那么你就需要梳理技能,是不是你想要的“那种”,如果不是那就继续快速的动手。千万别去学习,而是利用AI模型直接学习,C++是最适合多动手才能掌握的编程。2026年技术的学习其实和C++的学习发展一样,多实践你有24/7的专家级助手待命中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VeiapTUG9NbomXCuZUicgV2oyOlWBsiaibym6MLuib28oooETP4Tx7zjs5vMT2qWLdOUEUTYptib5b9cjp9sU3VlH9hw6rU3ialPsCia4bk/640?wx_fmt=png&from=appmsg)

为了加快效率我从每天的2小时调整到每天的4小时进行研究一些必要的内容,快速的融入到“领先”的人工智能助手逆向工程之中。这里包含了MCP和LLM的一些细节的处理,由于是手动逆向并非是自动定时的所以暂时不系统的深入#n8n 。

添加2个小时的目的是主要为了：把必要初级可循环的部分写的深度细节化,让Ai可以更好的读懂我要的做的是什么。教程可以模糊,但是投喂自己的助手的教程就必须细节化。同时为了能够持续添加一些硬件,我会把所有细节内容发布在 （知识库：Bl0ckdev 的 Ai MCP 逆向实验室）— 宗旨就是：「不择手段。只要能拆。」

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VejYX1mSWM0CkY62fic2z1HGudL0tClgYn219eBB3TVedFf5UFkU1huicicFt5AT4zSPvm9CFaiawJC8jO0TXBnVkFay85sRLpic0uEg/640?wx_fmt=png&from=appmsg)

Ai逆向自动化—核心：

不谈写理念和废话,只写可以完整的是实践过程,我会在公众号给大家完整的路线和需要的工具。要做的是给每个MCP技能一个闭环。

1. Ghidra  （java）
2. 操作系统以Windows为主Mac为辅|Mac本子上我装了IDA pro。显卡我选择的是默认的。
3. GhidraMCP
4. CheatEngine76
5. snapshot

这些工具是完成首次逆向的必备工具,同时我还建议你直接安装：Vs Code C++

因为我们还需要进行标准对接C++编写软件和修改Ai给出的源代码部分。去修改程序达到自己“逆向自己的程序”。

同时我在DIscord服务器上进行了论坛形式“分布式”更新,参考如下图：所有添加星球的均活动相同权限的 @ID：成员|用于访问我们的完整社区。添加星球以后的通过Vx获取提交你的邮箱进行获取授权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VejKsQvBTvy0nWwSDRNiaCbGbicTVQTZbKQicxDicSIwsmb167o2nHEPHKmfNAqpUfjL9Wl3C8sxicHY8RqG0jZECyJ6aYUpM6b6AEjk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VehrfaMakHeAXy6Kph5e7j7zd83I22j6uxq4bBibElNYjqnPhsic052oUEz2c86pA8DrqHd7Y9I3FHnd3uKKJu2UQzNBY4v59jNGU/640?wx_fmt=png&from=appmsg)

福利：5/20之Vx询问邀请添加享受（8折优惠）名额“10”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VeiauR17KJO3eTVVEjYm5DvV5mYVu1TibaokoLwk8sHMVRBKWOmPC3eGuvEfWXC2fwXuXXLYMIon4Zc1PLib1eBYFiaymDibkfj4ng9Y/640?wx_fmt=png&from=appmsg)

我的更新策略：

我每天会在Discord中进行零零碎碎的内容更新,然后A闭环了以后把A整理到知识库星球内。

现在投入的时间变更为每天4小时,快速的走初级逆向实践后的细节雏形。感谢各位支持者

![](https://mmbiz.qpic.cn/mmbiz_jpg/PwaXL3w2IRaDgaRQG5ujsPrXostCchunyCR5Y0VpBpPTkXATnVMxBwPRnYBKdqgPx7AB433icw5FXez1xp6Nibqg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

Esn技术社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

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