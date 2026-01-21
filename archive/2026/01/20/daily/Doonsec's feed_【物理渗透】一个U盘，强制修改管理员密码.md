---
title: 【物理渗透】一个U盘，强制修改管理员密码
url: https://mp.weixin.qq.com/s/EHccCA5m7jw0hvWoZJx3Dg
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:30:16.617306
---

# 【物理渗透】一个U盘，强制修改管理员密码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5975bXHXfWFShIUuAg6nBFujX94xficDoezS6GMKNsYgvC3Uiaj8fPSdSDDdNyvBibRYVb3xF4ZLiaEsmJ0xt8vbHA/0?wx_fmt=jpeg)

# 【物理渗透】一个U盘，强制修改管理员密码

泷羽Sec-Norsea

![]()

在小说阅读器中沉浸阅读

以下文章来源于泷羽Sec
，作者仙草里没有草噜丶

![](http://wx.qlogo.cn/mmhead/Hp9HAaP9GFBKneKn5ryBUs0PRR7YFdhjkVm1EtmTw39DFXQog0cNn1NibPUo2tbPL2mH1HymCVxM/0)

**泷羽Sec**
.

B站：泷羽Sec，团队专注于网络安全领域的内容创作与分享，为网络安全而战。来自一个从零开始学习网安的见习生。很菜，不喜勿喷。

> 白小羽
>
> 免责声明：请不要使用文章中的任何技术做违背道德的事，禁止用于非法行为，造成的后果自行承担，与作者无关，教学仅供一些容易忘记密码的人使用。并且一定要将数据备份好

本文主要是记一次帮同事电脑恢复密码的过程，也广泛用于红队行动中的物理渗透

首先扫码下载配套工具，包含密码修改工具和大白菜装机工具

![https___pan.quark.cn_s_694a6d1061ce](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDoT1huJdrBGygqpYGmfRrgM3NVHRtty1BiarzmLjpt4bicmy5cOqonFDlw/640?wx_fmt=other&from=appmsg)

下载这两个工具（电脑没插网线的情况下），并记住这俩工具`NTPWEdit.exe`保存的目录

1、打开大白菜，使用默认模式准备一个u盘，将其一键制作成启动盘

![image-20251223184313563](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDo7CxxicgQrhCD57pyibicnee8zG7ibbfZ7wAq3Gv8XXUWISBQ5JF7y1lHtQ/640?wx_fmt=other&from=appmsg)

image-20251223184313563

2、重启开机，一直按f2或者f8、f10、delete（不同系统进入的案件不同），进入BIOS界面

按`-`号把这个盘移动到第一位

![image-20251223191049830](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDoY0jIlWNRe6auic2y4mTNUIXGrcJKpH3JGc3QMUuCI1Rykk6HQ8Zz9cg/640?wx_fmt=other&from=appmsg)

image-20251223191049830

3、然后保存退出

![image-20251223190511690](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDofQCUAoLUV0AW1X1TlQf9kAnIk5GpsUKWboMAdtK119w4CHicYj6VvgQ/640?wx_fmt=other&from=appmsg)

image-20251223190511690

4、确认保存并退出

![image-20251223190528768](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDoAFp01tsdnYrfapXCOcRPc7WNB8zmiaZr9RVzKcboFumJpAsT5CVvNJQ/640?wx_fmt=other&from=appmsg)

image-20251223190528768

5、开机后就会进入这个选项，选择第一个

![image-20251223201701994](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDopfMeKhxfcX23icVsXZcibLVibibfClibzL6DHI8mNgPW9Mx9DN6FJ4IiaiaVg/640?wx_fmt=other&from=appmsg)

image-20251223201701994

6、等待正常开机

![feb7757ad4353af93b9390c44cd7c17c](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDopl0M1cbQFuRicHUNRiceiaVBkhibqpGo6ABicy5ZGNmKHZ74LDgdDGTjw7g/640?wx_fmt=other&from=appmsg)

feb7757ad4353af93b9390c44cd7c17c

7、找到这个大白菜自带的工具

![21f47791fea647ecd739dfe0a4ec50c4](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDoAkYMAYGJwrLYx8FgEXKciaeGzYLia3uRhVcCxxbmicXh14c04VjyzHGOg/640?wx_fmt=other&from=appmsg)

21f47791fea647ecd739dfe0a4ec50c4

8、如果电脑没有插网线，可能会出现这个错误，不过不要紧

![0bbd7156e1d3b91466cade58dc0405e2](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDoASwxicVAcaaFGgSLibJ9RImcJEx9ialXzYBrcQXZQjNaTD0Sj0KmKbjCQ/640?wx_fmt=other&from=appmsg)

0bbd7156e1d3b91466cade58dc0405e2

9、我们打开刚刚下载的这个NTPWEdit工具，点击文件路径旁边的打开

![fdc897bbeb390c5859f8b425f70f9d91](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDonqqAwofv0zQExUFSCB0yRHsYdic2faY3XOGgbKcCwB7fKluZz4cyKYg/640?wx_fmt=other&from=appmsg)

fdc897bbeb390c5859f8b425f70f9d91

10、点击打开之后，就能看到系统的账号信息，然后选择你需要重置的密码并点击确定即可

![e1b238189d9726ad25d52f87b989cdd3](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWFShIUuAg6nBFujX94xficDofJicDzHlLXESp6zEWibXicV1KQE6hASgbmVcnclicGOPhsXh5iavoKMOiadA/640?wx_fmt=other&from=appmsg)

e1b238189d9726ad25d52f87b989cdd3

原理：学过windows提权的应该都知道，原本的系统SAM文件是不能复制，不能写入也不能读取的，它被系统独占，但是！！！如果同一台电脑上的磁盘有两个操作系统呢？那么我们只要通过制作U盘启动盘，或者第二个系统就能读取SAM文件！！利用NTPWEdit工具直接修改SAM文件，串改密码

如何防范？

1、启动微软的BitLocker硬盘锁

![](https://mmbiz.qpic.cn/mmbiz_png/5975bXHXfWFShIUuAg6nBFujX94xficDogS7L45OGR1ibVNNfjWzPyD6c94yh9iazGibagccqqEA4zByXQ2wh0ich5A/640?wx_fmt=png&from=appmsg)

2、设置BIOS的界面的密码锁（也有破解方法，比如物理放电，跳线等等）

3、Bing一下，你就知道

## 往期推荐

[![](https://mmbiz.qpic.cn/mmbiz_png/5975bXHXfWEISBgpKA0GkUMAo88OeWlhLCEibsPcsDvP1v7STaGHZtaNEefcSJ69vfU55hibMcvrVsSMmIMttN2A/640?wx_fmt=png&from=appmsg&watermark=1)](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247502572&idx=1&sn=42a9853381a099fc7c074230c39824a3&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

泷羽Sec-Norsea

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

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