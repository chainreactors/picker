---
title: 渗透 | 为什么我又重构了一遍 RouteVulScan
url: https://mp.weixin.qq.com/s/hP8QUwMaPaV0d4AcFZuf3Q
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:16:48.638257
---

# 渗透 | 为什么我又重构了一遍 RouteVulScan

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/br9s3IYOdUxOC41lVG3nwlzv6wbrIfxDl6K33AaXy8ctxCpTOdOXteWFm8mic0olI91BcAGuGUMnOQkjQg1hX1aYg7h7fAPgsWicib4cFVW10I/0?wx_fmt=jpeg)

# 渗透 | 为什么我又重构了一遍 RouteVulScan

原创

风沙吹奏
风沙吹奏

不务正业的安服崽

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前言

市面上的递归式目录扫描 BurpSuite 插件可能存在的痛点：

1. 长期不更新（近1~2年没有更新）或已停止更新导致不兼容新版（v2023.12.1以上） BP，或者兼容性差。
2. 界面交互设计差，使用不标准的英文表达、缺少交互逻辑、充满了一股“又不是不能用”的设计思维，不够友好。

因此，我基于 Montoya API 重构了这款工具，叫 RouteVulScan-2.0.0

https://github.com/ThestaRY7/RouteVulScan-2.0

我自己本身也是个安服仔，日常做渗透测试经常用到各种被动式的目录递归扫描插件，但最后还是选择参考 RouteVulScan 的代码逻辑，重构了一版。

这个工具的特点在于，采用符合安服仔测试逻辑的 UI 界面交互，还有高度自定义的规则库。

工具扫描能力的准度，完全取决于用户自定义规则的水平。

路径写的越详细，命中正则写的越准确，扫描结果就越靠谱。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Sk94nnibQ5dW4DiaVMQqEvmydn6R9oDx2URA8qgKuBmXtGjT0DSDa0U4ibmFa3VDvJsKuUxfZjmSZMGKzpMgoD3Rw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

插件功能展示

加载插件后的主界面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/br9s3IYOdUzjEdwzo2CwXDypeQZjiaXMbhQXky7HgrJ7BjeKNZZFjYjFgJ5EW4aJvOAUbsH5O48q6awxm5oLk5LZPia3seawVw8GtJ3LxgxAw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/br9s3IYOdUyKBibGVpvv9pFiacMnydH00kyKibRzax0QY18EBNVYBtatIvtyE9oqabzsc3oRWpCrAR3G1pjx5J2AGQcf1KGvibweJZy0KHVQTWQ/640?wx_fmt=png&from=appmsg)

HTTP history 页面的右键选项，可发送指定数据包到插件进行扫描：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/br9s3IYOdUzHB6ZoFUrAbuJR0icwHicibKVicd7UFOqBEg2ax8xDK44SuU6iaibWdXkWsg8auibkZ5zx1ZSUV6KSQhRxtO2F2BGKorNCwicCteZ7ods/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Sk94nnibQ5dW4DiaVMQqEvmydn6R9oDx2URA8qgKuBmXtGjT0DSDa0U4ibmFa3VDvJsKuUxfZjmSZMGKzpMgoD3Rw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

最后

这个工具，有点像重复造轮子，因为大家来来去去写的工具都是为了解决同一个痛点，各有各的缺点和优点，对于我来说，都不够趁手。

还有些工具，缝合了一大堆功能，看上去样样都能做，实际样样都做不好。

这时候想起了猪猪侠大佬以前说过的：

* 要把工具做成“原子化”。
* 你向 100 个不同的安服仔，提供同一款插件，这大杂烩能用吗？
* 聚焦问题，有效解决问题。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/LQXGlsVicDce3evmnj7xFBLgF9XU5n1uX1Ozy053gpyhsQOHzQJa4o9hUpeujxuUwRffEUOpqicNTev833AuKmKQ/0?wx_fmt=png)

不务正业的安服崽

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/LQXGlsVicDce3evmnj7xFBLgF9XU5n1uX1Ozy053gpyhsQOHzQJa4o9hUpeujxuUwRffEUOpqicNTev833AuKmKQ/0?wx_fmt=png)

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