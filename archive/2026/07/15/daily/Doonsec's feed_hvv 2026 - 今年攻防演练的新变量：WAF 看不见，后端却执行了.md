---
title: hvv 2026 - 今年攻防演练的新变量：WAF 看不见，后端却执行了
url: https://mp.weixin.qq.com/s/IGYpjaeqhJZvuYHb-HcYmw
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:56:35.143530
---

# hvv 2026 - 今年攻防演练的新变量：WAF 看不见，后端却执行了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TkCzWPGhiblg2icbOWqHuyblUibmAX3aKtTlxtYicGe31Z79oPfHhsleoJoicFcicX4Zia1LGCibo2vibKyfnI9FMpxl5N2Tw40mrx6Ny0XzRb1y2bM0/0?wx_fmt=jpeg)

# hvv 2026 - 今年攻防演练的新变量：WAF 看不见，后端却执行了

搞安全的面具侠
搞安全的面具侠

搞安全的面具侠

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近忙着HW没时间很久没写东西了，既然迎来了考验，把最近看到的一篇文章给各位分享一下：

转载！侵权请联系删除！

[hvv 2026 -  今年攻防演练的新变量：WAF 看不见，后端却执行了](https://mp.weixin.qq.com/s?__biz=MzI1MDkwNzQ4NA==&mid=2247483908&idx=1&sn=85d1b83e9e678b9561aaf132aae5fca0&scene=21#wechat_redirect)

今年 Black Hat Asia 上有份材料，《Cast Attack: A New Threat Posed by Ghost Bits in Java》。没刷屏，没上热搜，群里转发量也不大。

但我看完之后在笔记里写了一行：**这东西会成为今年攻防演练里红队工具箱里的常客。**

不是某个单点 RCE。没有"一键打穿全网"那种新闻标题。它是一种藏在 Java 生态底层的解析差异攻击面：同一个输入，WAF 看到的是乱码，后端执行出来的是攻击语义。

先说原理，再聊怎么打。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkCzWPGhiblh7SuNJgoWSxqJZ89amKl77h1StbIUKdNmsjia495wG0zJQ1sUaCIkGg4yjhBBM0ITYfJrhL1piaWI3J8XR6iakF76FHSj6HOq1nE/640?wx_fmt=png&from=appmsg)

## 原理：Java 的 char 是 16 位，但很多代码只认低 8 位

Java 的 `char` 类型是 16 位无符号整数，码点范围 0x0000 到 0xFFFF。但很多 Java 代码在把字符转成字节的时候，做了强转或位运算，只取低 8 位。高位直接被丢弃。

常见的危险写法：

![](https://mmbiz.qpic.cn/mmbiz_png/TkCzWPGhiblia7xCLSzzepV7Gia4MWaKWwGmibF2VQdvVp5pliadbVzgPeuvvTH7uUkXc9cGxEibCCiaH6ZwNTIzUmqvbJu7LUKXz4DrHBxaiawneAo/640?wx_fmt=png&from=appmsg)

全文请点击链接观看

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/04t2QpwiaY5Xa8ibZbIzN4SD0FUTzBfmUOo0BQyzeDBEQ1MSFq8J8gb5VwhXZvvgAzWK0vCndHiaS1okYHLYIGGjA/0?wx_fmt=png)

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