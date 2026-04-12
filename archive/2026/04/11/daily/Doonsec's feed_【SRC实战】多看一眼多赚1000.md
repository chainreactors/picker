---
title: 【SRC实战】多看一眼多赚1000
url: https://mp.weixin.qq.com/s/gpCRfOH5JN_-OSvx9AVZig
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:41:41.492208
---

# 【SRC实战】多看一眼多赚1000

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JnmoqeNZZwS0iaTiaKPdzx62gvGWuO9kpZSIldtT4R7JiasO6oLGwHN2k1HoJ6zLJfXxiajlcLdQHTrzkNSibhMGP4rBoGEwicDNJSicvKr8iaSwhC4/0?wx_fmt=jpeg)

# 【SRC实战】多看一眼多赚1000

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于隐雾安全
，作者隐雾安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM726qqnXD4ibQaXQjLVHp9Gxyv9TJsiaWicUIvUnjPWalVYA/0)

**隐雾安全**
.

隐雾，为您提供职业成功的关键。

📝 **编者语**

最近有学员在面试中被问到了JS相关的知识，刚好我这里有一篇单点漏洞挖掘记录。

我们不看结果，只看过程：
怎么从一段JS，一步一步走到“任意文件上传”。

1

看一眼1000

一开始其实没想那么多。

就是在正常翻站点的时候，顺手点开了浏览器里的JS文件。结果成功挖到一个价值1000的【高危】

说实话，在没了解JS之前，总觉得JS很杂，看起来也费时间。

了解之后每次看到JS都会多看一会。

然后就看到了一个让我有点在意的东西：
一个看起来像 token 的参数。

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4nfDaDmGCZbJfKaKPELd2DkobRZACXPYzwnCdAYEYibrQrmnUo2BU9icN4Nrm20E4My5nsYUfnR6DdkexFEeGEic6BIGphWGC4GdI/640?wx_fmt=png&from=appmsg)

***第一反应：这个 token 是干嘛的？***

看到这种东西，我现在基本会条件反射想一件事：

这个token是不是用来调用接口的？

于是在JS里找它的使用位置，很快就定位到了一个接口，是用来上传文件的。

到这里，其实还只是“有点意思”，还谈不上漏洞。

***第二步：不带 token，会怎样？***

我先做了一个最基础的测试：

* 不带 token，请求接口
* 返回 401，禁止访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4lDgOvOu5pf8cCvlg5BdH6QI38URU7e3cicxkmpW0hxMljkD26hDVAuY7ZPzLe4fRSVmAfARYPKXlC1YH9RFQFLicwZ8QSVk0Xg4/640?wx_fmt=png&from=appmsg)

这个时候其实逻辑是正常的，看起来像是做了权限控制。

但关键在于：
我已经拿到了 token。

***第三步：带上 token，再试一次***

然后我把 JS 里那个 token，直接带到请求里。

结果请求成功了。

接口返回正常，而且文件上传也成功了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4lcFGUMnC34StmdOC2weoh8CdFWwtBJakShocWgJpkWe5qqbUlcayqFDYN5iaZZcq3Aicl0GDmibgWRq3cu4ZuUWFN6icgEjs8mYzM/640?wx_fmt=png&from=appmsg)

到这里，其实问题已经开始出现了：

一个本该“受保护”的接口，因为token泄露，就可以被直接调用。

***第四步：我开始有点不放心了***

这时候我脑子里冒出来一个想法：

如果这个接口真的没做校验，那我能不能上传“任意文件”？

于是我开始尝试：

* 改文件类型
* 改后缀
* 随便传点别的内容

结果发现，这个接口居然没有限制上传文件类型，直接就能成功。

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4kxKAhOAfwQlOPJqoSyFicpBiaxg9c0q357ps2jIfhCo1axAfHCuYn3uvPTVqyprK0vXWhN1X9j7iajxjde5SAQBjgf2XHHDSb2Lw/640?wx_fmt=png&from=appmsg)

***到这里，这个漏洞其实已经成型了***

整个过程走下来，其实很简单：

1. 在 JS 里发现 token
2. 找到对应接口
3. 测试接口权限
4. 验证上传能力
5. 扩展成任意文件上传

本质就是：

JS 泄露敏感信息 + 接口缺乏有效校验 = 高危漏洞

2

一点习惯的改变

这个洞并不复杂，但它让我开始重新看待JS：

JS文件，不只是“前端代码”，它有时候就是一张“藏宝图”。

以前更多是在测页面接口、测功能，现在我会多加一步：

* 打开 JS
* 找接口
* 找参数
* 找 token / key / url

很多线索，其实都在这里。

***现在看 JS，一般看什么？***

**1. 看有没有敏感信息**

* token
* key
* 内网地址
* 接口路径

**2. 看有没有隐藏接口**

* 上传接口
* 管理接口
* 未在前端展示的功能

**3. 看参数是怎么传的**

* 有没有可以复用的参数
* 有没有可以直接调用的请求

有时候技术变强，就是从：

哪些地方“值得你多看一眼”开始的。

3

感悟

这个洞让我印象挺深的，不是因为它有多难，而是因为它很“顺”。

就像是：

* 你看到一个线索
* 顺着走
* 再顺着走
* 最后自然就到了结果

没有什么特别跳跃的操作。

但如果一开始没有点开那个JS，这一切都不会发生。

很多漏洞，不是藏得深，而是你有没有停下来多看一眼。

🎁

**建了个**src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞

圈子专注于更新src相关：

```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例2、分享src优质视频课程3、分享src挖掘技巧tips4、小群一起挖洞
```

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2 "null")

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTahgbr35OD8B1WCHW2uGMetuDzTPJiaHibhWhMm8UQ5iboDmNKqrRfjIrXQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWr5g7s0TNF4tBZqNbdewPNswTDOfvN6PkggCqz8j3mib6Vf3z4ia83asg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaTWxLibDHdqdx6IahjVWr6ficJWskIMjdrbYaLGBIVsbONxbb5ibDS5trQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTafQtWhe2qhicQCvx8XaDyp6Kb4eeWBnhZLlGKcAvxKausLKc2YYggykQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

图片

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWWIDTric5u0Q03o25wLLgNBwFd6t4ud64ACo8icCdQRzrEGezUzIKSvEA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=12)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWXytl9Ioah3X7tw7EMlWV96wWXEHFEM4m6NwlvvkcmEcPqcxcE9MQDg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaDpuFU7U9TMK5eIpY8iaJcXCicmTB6fsRd8icmH7K1X99YbC07GaJbCRReocORsnDGNU7H7PeqcysIA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JnmoqeNZZwQuSDlwHB5xlUX3sOtibs0ib3MZylMAfiaB9PPQpicTj95BvMVCRAlXKhlROoaun9wUg2fJ5Mia8iapP42Qb3dnr4mX28bhjhpjwyTeE/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=16)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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