---
title: 【安全圈】微软给Windows 11添加新选项允许打开任意文件夹最终都在新选项卡中打开
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066233&idx=3&sn=eda307d1af237cfd16d170e9ffa459af&chksm=f36e7df9c419f4efc53f6f8c5121e67a54fc2d87492a52f50fcbd3c3d3bf360bee29ec6fb5ae&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-27
fetch_date: 2025-10-06T19:18:31.326762
---

# 【安全圈】微软给Windows 11添加新选项允许打开任意文件夹最终都在新选项卡中打开

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaJT9LOL4Vm2kyopU9Gnk9c5gYHgaKI2t7R75ib9nPd42J4U9eQ9f5E8Mc7iaLUB5w5brpSDDGn0l4w/0?wx_fmt=jpeg)

# 【安全圈】微软给Windows 11添加新选项允许打开任意文件夹最终都在新选项卡中打开

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Windows

微软正在陆续解决 Windows 11 中的某些奇怪问题，例如资源管理器的选项卡模式每次打开新文件夹时总是在新窗口中而不是在现有窗口的新选项卡中打开问题。

资源管理器的选项卡模式在实用性方面还是非常不错的，用户可以在打开任意文件夹后在同一个窗口内鼠标或快捷键打开新选项卡然后在新选项卡中打开其他文件夹，这样就不会出现多个窗口的情况。

BUG 设计之处在于，在已经打开一个文件夹窗口的情况下，如果在桌面或其他地方打开新文件夹，则会再次开启一个新窗口，而不是在原窗口的新选项卡中打开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaJT9LOL4Vm2kyopU9Gnk9cXE04zicPJzwUiaIsje5aMNko5yYtgiaLP8wZLHdaETg7QjI3HEBAt8RZg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaJT9LOL4Vm2kyopU9Gnk9c4BnXTZ8RpCYBhJ7wovoj5U5cWdqfODs7tK79uVW2NiawPnDibo0FSzAA/640?wx_fmt=png&from=appmsg)

图片来自：Phantomofearth

现在微软终于要解决问题了，在 Windows 11 Beta Build 22635.4515 版中微软在资源管理器中增加新选项，该选项启用后打开文件夹会始终以新选项卡模式打开。

不过该选项并不是默认启用的，这可能是考虑到一些用户的使用习惯仍然是打开多个不同的窗口进行操作吧，不过其实使用新选项卡模式打开后，只需要鼠标按住选项卡进行拖放即可拆分窗口；同理，多个不同的窗口也可以通过鼠标拖放进行合并。所以总体上只要使用习惯后操作起来还是非常方便的。

目前始终在一个窗口内打开文件夹还在测试中，如果你想体验这个功能可以通过 ViveTool 手动开启，预计要不了多久这处改进应该就会抵达 Windows 11 正式版。

**下面是启用方法：**

1. 必要条件：Windows 11 Beta Build 22635.4515 + 版

2. 下载并查看 ViveTool 使用方法：[图文教程] Windows 11 开发版必备神器 ViveTool 到底怎么用？其实很简单

3. 运行以下命令开启该功能：

vivetool /enable/id:49143212,52081114,48433719

4. 重启系统，然后在文件夹选项、常规中勾选在新选项卡中打开桌面文件夹和外部文件夹链接

来源：https://www.landiannews.com/archives/106789.html

***END***

阅读推荐

[【安全圈】威联通NAS的QTS系统新版本导致无法正常访问 目前该固件已经被撤回](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066218&idx=1&sn=a4d403fd36bee9add5a2da4f1ca2462c&scene=21#wechat_redirect)

[【安全圈】维基解密告密者使用防NSA VPN对抗AI监控](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066218&idx=2&sn=5f496ab01a0c1c8bbacd6e3cc8f77599&scene=21#wechat_redirect)

[【安全圈】Fortinet VPN服务器设计缺陷能隐藏攻击者行踪](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066218&idx=3&sn=383839a7010797557f1d931f08bba980&scene=21#wechat_redirect)

[【安全圈】超2000 台 Palo Alto Networks 设备遭入侵](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066218&idx=4&sn=8b68cb431919cf30facf1ad47ba67cfe&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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