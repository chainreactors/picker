---
title: 网工电脑里几十份设备手册，我让 Marvis 帮我找命令
url: https://mp.weixin.qq.com/s/940HdBdNSmYFl00AdCsauA
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:23:23.537158
---

# 网工电脑里几十份设备手册，我让 Marvis 帮我找命令

# 网工电脑里几十份设备手册，我让 Marvis 帮我找命令

圈圈
圈圈

网络技术干货圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

做网络工程，电脑里多少都会存一些设备手册。

华为、H3C、Cisco，不同型号的交换机、路由器、防火墙，还有各种配置指南和版本说明。平时用不到的时候，这些 PDF 基本躺在硬盘里，真遇到问题需要查的时候，才发现手册动辄几十页甚至上百页。

最麻烦的不是没有资料，而是**资料太多了，找起来很慢**。

以前遇到一个配置问题，我一般就是打开手册，然后搜索关键词。如果关键词不准确，还得换几个词继续找。有时候好不容易找到相关章节，还要自己把前后的配置说明看一遍。

这次我换了个方法，让 Marvis 帮我找。

## 先从一个实际问题开始

这次测试没有直接问 Marvis “华为交换机怎么配置”，而是准备了几份平时网工会用到的设备手册，然后给它一个比较具体的问题。

例如：

> 帮我从电脑里的网络设备手册中找出与 VLAN、Trunk 配置相关的内容，并告诉我分别来自哪些文档和章节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5ib0IQnBLeiaPZNOMSDKgm9EGm4CYkDNktFA4huLP3J22ic1lpSibI7wYQNZ2aEUzKzobS7TBiaGyhLU8cc77cPNL4DTvxkPLiaKmvmU/640?wx_fmt=png&from=appmsg)

这样做的好处是，问题比较明确，也更接近日常工作。

如果只是问一个很宽泛的问题，得到的内容未必适合当前设备。对于网工来说，**查哪份文档、对应什么设备和版本**，这些信息本身就很重要。

Marvis 的本地文件能力可以用于文件搜索、分类以及文档读取和分析。对于已经在电脑里保存了大量技术资料的人来说，这类场景比单纯翻文件夹方便一些。

## 不用一页一页翻，先把相关内容找出来

执行之后，我主要看两个东西。

一个是它找到了哪些文档，另一个是这些文档里的哪些内容和问题相关。

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ibfgvzUhiamAxTMqYGfOB5VAXxkVFPsWgwiaFmk25D5mPKO8J7AkUdhxtQgBRyP4RK5fl81kgsfQA7LTrDnhh33MdzoKtdsyAJnQ/640?wx_fmt=png&from=appmsg)

如果结果比较多，还可以继续缩小范围。

比如：

> 只保留与交换机 VLAN 配置直接相关的内容，并整理出配置命令、适用场景和对应文档位置。

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5icVQ9Y4eJMj4ovcpJTVjX3TnjHFniaIoyblWByibnuFbDicpyBYlbvJJib6gvB2ykLHrnbhEEMODddqyr70dR35HX1cg9LdUL7PBEk/640?wx_fmt=png&from=appmsg)

这样就不用自己打开几十个 PDF，再一个个搜索关键词。

对于经常查厂商手册的网工来说，这种方式其实挺实用。

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ic24P0bU4ILz1diaqQTBeHslHVkusic8Bic2YQkib5o81yiaNHYQqAXWjQCK9CWeghwqCL7R95icRLlXgpn8IjC0v29rtXpW11KZvg70/640?wx_fmt=png&from=appmsg)

尤其是一些很久以前保存的资料，文件名可能只是一个型号或者版本号，单纯依靠文件名搜索，很难判断里面到底有没有自己需要的内容。

## 找到命令以后，我还是会自己核对

这里我觉得还是要保持一个网工的习惯。

AI 找到的内容可以作为查资料的入口，但涉及设备配置时，不能看到一条命令就直接复制到生产设备。

因为同一个功能，不同厂商、不同设备型号甚至不同版本，配置方式都可能存在区别。

所以我的做法还是：

**Marvis 帮我找资料 → 查看原文 → 确认设备型号和版本 → 再决定怎么配置。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5ibnBmYlElicFxs5a448Tk3bAGGiargxfBjJ8EASGQmRtpzs01VrlhiaTZCJJWowqEHPCXm7yt8mAqvjaBSTR5T9aVEUObSbKuzdAk/640?wx_fmt=png&from=appmsg)

如果发现资料比较多，还可以继续让它把相关内容整理成一份简短的速查笔记。

例如：

> 把刚才找到的 VLAN 和 Trunk 相关内容整理成一份网工速查笔记，保留关键命令和注意事项，并标明对应文档。

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5icsP6IuBtibGoDvNd4KibZdccHjRUXKyGNCNNcQ5AckOndhdAIeSrQM6VfZYFmCZ57yAIM2ic5OolCvbCWgd8Yd7GRwyZKKHev6qU/640?wx_fmt=png&from=appmsg)

这样以后再遇到类似问题，就不需要重新翻整份手册。

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ibKQI54iaWibthkTHpUiaTPkBJVx4Wfer8g3R1cib5qLe8PRDUQWqs2JMNmLLOt15iaXvHu23jkibFiaesHm9BJCRqSsYCibod8YhJCujU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5ich9TicoPB4odsXAFOBhLyPW52xUxCYHYW7ubapiaMybxAG2aJwzBpJfXrKyrA8dsQ2uOoDibhmV9zGPa9jabKbNXvtM9YAPqia8E4/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S59mMVer0ecEiao4WpWwv1tvypdSxljia1ONHmCB7siajFNOD8tOoJoUUkkAia9avtmJXO50moMnYtqWZkiaPBnorqvO4yXBGIUPqfJw/640?wx_fmt=png&from=appmsg)

---

以前电脑里保存几十份设备手册，我并不觉得有什么问题。

真正遇到问题的时候才发现，资料多了以后，找到正确资料本身就变成了一件麻烦事。

这次用 Marvis 做的事情其实很简单：

**把电脑里的设备手册找出来，再从里面找到我需要的内容。**

它没有替我完成网络配置，最终的判断也还是需要自己做。

但如果能把原本需要反复翻 PDF、找关键词的过程缩短一些，对于每天都要查设备手册的网工来说，确实是一个比较实用的桌面使用场景。

以后再遇到“这个命令到底在哪份手册里”的问题，我可能会先让 Marvis 帮我找一遍。

#Marvis #马维斯 #AI管家 #Marvis教程

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT8cAnqjp2AZ90pLWoO7Ysr6JzXPMqP8qibB5ggPz4amnZicChP8vQExwbEJ1O0BtqiaYuYHicm74DQnbA/0?wx_fmt=png)

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