---
title: 第171篇：蓝队分析取证工具箱 V4.36 AI智能研判增强版，大幅度更新
url: https://mp.weixin.qq.com/s/doozZsk3md7HNRnhHvwPWQ
source: Doonsec's feed
date: 2026-07-24
fetch_date: 2026-07-25T04:58:27.197265
---

# 第171篇：蓝队分析取证工具箱 V4.36 AI智能研判增强版，大幅度更新

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2bGibHibFr61FJugfL0tOIFXWlrt9fDj8rQZVCgic7uHoBUVmDiaKibZqkerSCy9HHrcRpRnzPsia2zQGrJA3El4j9uNEoKhicHOZGQXk/0?wx_fmt=jpeg)

# 第171篇：蓝队分析取证工具箱 V4.36 AI智能研判增强版，大幅度更新

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

蓝队分析取证工具箱

以下文章来源于希潭实验室
，作者abc123info

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM6fmEcY2bcaelEq3UFVKWcPYSM5dibWwP6KNJRapia8tbPQ/0)

**希潭实验室**
.

ABC\_123，2008年入行网络安全，希潭实验室创始人，某工业大学客座教授，某部委授课讲师、省级专家裁判，省评标专家。专注于安全咨询、网络安全培训、APT技战法分析、代码审计、渗透测试。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9Lbc0INLwTJTZT1GaNutZrfDn6csvjBoS2ox0efLUEexXqPEcVbYfbLo8w/640?wx_fmt=png)

## Part1 前言

大家好，我是ABC\_123。蓝队分析取证工具箱有大半年没发布了，其实我一直在更新，在想尽各种办法解决多年来两个头疼问题：第1个是java swing的软件图形界面不同分辨率缩放问题；第2个是新版流量数据包pcapng格式支持问题。这两个问题在最近终于得到了解决，今天发布出来一个新版，相信这两个基础问题解决之后，后续软件功能的更新将会畅通无阻，敬请期待。

注：文末有下载地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2Zc77PyLkuDupKmynbgOEwUUWTzUVjztJ8lNBUiaU9icoEOBhMD2DdLFiazribOgicGo0O9910qnCUP5NsLGWiabqBwOm1v6GShlmRj0/640?wx_fmt=png&from=appmsg)

## Part2 技术研究过程

* ## 解决不同屏幕分辨率界面缩放问题

这个问题困扰我多年，非常难解决，最近总算是有了解决方案。有一天我突然想起，burpsuite就是Java swing做的图形界面，它是靠用户手工改变字体大小实现，那我何不这样解决呢？于是在蓝队工具箱的软件界面设置这里，可以手工选择字体大小，更改后当前字体大小配置会写入软件根目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2bGS3dGGcO0VKZbiaTlFSkAQgqmlskog05UiaNugiaOz3eS8mA3iaH79GDDUWO6j5lMytrRzDlTyta82A2c9YZEcTxWibD98zIZ0rJg/640?wx_fmt=png&from=appmsg)

##

* ## 解决pcapng流量包支持问题

java库对pcapng数据包的支持问题困扰我好多年，我换了很多库对pcapng支持都不好，最后没办法，只能自己硬着头皮写一个解决了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ay2ibWRlqt19YTA5WvRYwQAwTesg7oMSLIiaRnBJo3N9hAANjliaj3fJoLT7chHsnrOzu9HChAvqYibcUiawGWS4TzgF9NrKRibibGjc/640?wx_fmt=png&from=appmsg)

图表分析展示功能如下：

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ZBC7HA0zRibwQbBr0SMZNfWxMW6s61ZROf7PlaDF7LFUuTS4ITVEXSSmjdibH4LvXfU9sqOpSrDg4LNv0h6KVj6xjDInZxYfngs/640?wx_fmt=png&from=appmsg)

发现反射放大攻击行为：

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2YZ2mgfTzUa0icuOJxKicEuVDqqwlfv129nJzjpfdYTh0g2iaB6icGhyAp0ORaqDRoktKxeaqFJugWQuueDSNib54icc1jhJiaSvNPv2k/640?wx_fmt=png&from=appmsg)

网络拓扑图展示如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YwUdRGVSnRvPFf3GFuSj1oyfJQXVNGsDY11mSE8fdxuAjEcicPGLe8cZNUoqraeU5MNO6Ce0icXd6lMQzH8HpbBYZXsWHwkjcEg/640?wx_fmt=png&from=appmsg)

##

* ## 加入AI智能研判功能

AI现在非常火，可以结合AI进行高级研判。于是我在内存马反编译分析功能及反序列化分析标签页下，加入了AI研判功能，给出研判结果。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bcVH9RwNOEAIriblwMJyJsnuW7ic9icvdv1CohJia038HJKGhicicQpYxzG8v1G1LZNaWmic3m15apAIvz8rgduCVAkiaXdNgZNVCTCAs/640?wx_fmt=png&from=appmsg)

java反序列化漏洞分析，也支持AI研判分析：

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2abP5r49bOKhzwe1Wqu5wyYPg4lmOV3ktl33p5Gjj6NH4WRKRlwU4HWZx8pdV4OMrvWuRpyrLwGhvicupLCrrM4lrOzicwmlRqiaY/640?wx_fmt=png&from=appmsg)

* ## 新增识别dga域名的模型

这是ABC\_123使用云GPU根据相关论文计算的一个机器学习识别恶意域名的模型，可以从海量域名中识别dga域名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZVxZCtmDPLHIW8ELeVN6ib5utiaGzqic31iaYcFic1Jia8I0fKcrRsavWIIJNZic1R0z4J3mjp6Suaj1Y1Ao2icN6jpYyypnqoeMNoCgU/640?wx_fmt=png&from=appmsg)

##

* ## 新增对py bytes格式的支持

针对有些情况下，抓到的是一个python恶意样本，python代码形式的class文件或者序列化二进制文件是\x开头的格式，此功能就是为了解决类似问题而诞生的。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2btmRzTvTcWV3ZZojwDjHaNSicDJJMLq16MuGQCdUmukBZOtkwQgsd8NQ27FW9BqwmGmIIRLaKlZWKfIny7e75DRHvSxHgRtiaZ4/640?wx_fmt=png&from=appmsg)

反序列化分析功能也加入了py bytes加密方式的支持。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2Y3jlgVpicIIJYl7PnERIfdxQ6DAicJwBPVlfrWSrZxeqnshYDF3CiaicKYxeoaW4vlNsxGCkrmmIDlcMbAf7G8YzQdgpnHbsbLzUo/640?wx_fmt=png&from=appmsg)

##

* ## 优化端口连接分析功能

此功能无需联网使用，适用于内网不通外网的情况。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2YNMjibuC4ibJo2X4q2QhicyoXVHkpcUaDickeZ1mvw73ROoGzUskVIz8Fr1955unttUsGicSricCP3ZT6o5O2Pa91IgKl7icKqKb1iavM/640?wx_fmt=png&from=appmsg)

##

* ## 最终的软件界面如下

后续软件界面会继续美工，也许会改成前后端，敬请期待。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2aRoWqWztfic8jZ64bH9sbYd6icC9SyT7mYWzvtlXiacVFnkWXRHNffGm7tgnyF8YXpj63DymbhlibaltaIcuPllH8HXMtchOurN90/640?wx_fmt=png&from=appmsg)

##

## Part3 总结

1.  软件界面缩放问题、pcapng数据包支持问题解决之后，蓝队分析取证工具箱的很多功能后续会继续大幅度更新，敬请期待。

2.  关注公众号"希潭实验室"，回复"蓝队"，即可得到此工具的下载地址。

3.  欢迎大家扫码加入知识星球，进入星球内部HVV交流群，一起学习进步，星球送工具授权码（原有知识星球内容正在迁移）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZTMksWhOZ09oL04vFzzKQe0iaP8qpdE0rqlaBgB4yaNErkdX9ic5zf3AyAaYwnSBoxIIukzCc06o8SGWkKjLJ2k9EdnC3jU2GqE/640?wx_fmt=png&from=appmsg)

知识星球分为以下几个板块：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2Yswdna47FCiajjY45BBVvsicBxiaYPMichBoZR4QibV7WH0swHQUzFYmxxwaYqhS0xzx724MHIic6Nh42sMssOiczwfkm0MgVBfXcLZk/640?wx_fmt=jpeg&from=appmsg)

知识星球的每一个工具都是精心筛选，都附带有实测评价及使用说明。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2YVej38eRzrJjIq9BJhOSbbzYUWTsqZicrQPxiaic6fJLGeRCSJHSpSz80ib2S3ZoDHyyG6QZPL5BDZQdcOWdibbMcgRtvj78jCb7hA/640?wx_fmt=jpeg&from=appmsg)

知识星球的每一篇PDF文档、PPT文档都细心整理，配有3到9张关键截图。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2ZpjOMz6uBic9OucdYBfBLyETmkmibMQ27I0ftpib5Nic1gjfbHCwDjmWKp11CarP215LU4iahmvibMhakbkmw0icWvyjqOBIzhibE3Yu0/640?wx_fmt=jpeg&from=appmsg)

欢迎大家扫码加入知识星球，一起学习进步！

![](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2YU6YdILmbv6CbQQjPzT5fTMH918e5lLTyuBcJxypX32Ihkyu2ab3ibjhnq7gTk7dvnJ4HibQpSziaOoDwpQj83t9OMtJicPErfKbo/640?wx_fmt=jpeg&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

**公众号专注于网络安全技术分享，包括APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**OR 2332887682#qq.com**

**(replace # with @)**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1Ijz7jib5Bwjy65Kzg7q6JU6BGvgr2NLDZOvGs639QJHWib6ibMWNN4nGGlAgbfBtiaRWccAfh4KGpoibDzDwLQW9Nbb5QtE0yibdww/0?wx_fmt=png)

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