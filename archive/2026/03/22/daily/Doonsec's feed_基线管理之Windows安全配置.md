---
title: 基线管理之Windows安全配置
url: https://mp.weixin.qq.com/s/YQiIqmnx7Wn9QX5uXKSxVQ
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:19:36.850393
---

# 基线管理之Windows安全配置

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QJTLZsy5trFlrQc6BFUYMVthJns6Mmp3GO9QT4rQxf62Sq6suia8icdmGXfwAUBf5me1qUL0iaJlqsic7VNKurlZwowYVbSK4ePQkhAsz6IuwHg/0?wx_fmt=jpeg)

# 基线管理之Windows安全配置

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于建哥聊安全
，作者建哥聊安全

![](http://wx.qlogo.cn/mmhead/NoFChqEQomEQ8BFqpek1tIVA2t4wZzMiasb30hIibiaCexptTVReuzrZ9uh1ibhm7Ae4p2XDgByokzU/0)

**建哥聊安全**
.

95后 安全牛马 不定期分享网安干货分享，觉得有用的可以点个关注，持续日更中...

# **基线管理之Windows安全配置**

## **实验目的**

通过此篇文章去熟悉windows安全配置选项，掌握Windows组策略配置，理解Windows安全配置检查工具的应用。

## **实验拓扑**

略

## **实验环境**

一台windows server 2012 R2

## **实验原理**

windows通过组策略展示了详细的操作系统配置，通过配置组策略，将设置保存于windoows注册表，以便操作系统加载各项配置。

## **实验步骤**

#### **一、登录服务器，打开组策略**

开始–运行

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGmmzFMcjcRqtHnbzLnmklGBKrKnOpTxWU91icsWHVCtN6DjBjhIYdD2vZ21JUEupOsXGSSCFFOyyxaGT7cc1w9burUhwkV2c50/640?wx_fmt=png&from=appmsg)

输入gpedit.msc，点确定

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEbKehnKOLy4ab9wRE9Nm96oibnxXG9HsQjQWnQA3v2QI9cMXIVPkpLsPuslwbWwL7lTlAwz8wicpEMPpOkkoZias4xEaQRETr3ibE/640?wx_fmt=png&from=appmsg)

#### **二、账户策略配置**

1、密码策略

依次如图展开，密码策略，如图进行配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEDNOuIhhZXbwDURPZ3TEDEaPFh7SXbiciaSCvNUMicF5FvHlU9Io6cAn7BISwamdx4YSTwk0W2Bu5YnFcKZFXt1W7IHe6DicAEEBs/640?wx_fmt=png&from=appmsg)

2、账户锁定策略

配置账户锁定阈值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHVmVIoR5kPDpLEborQaUD8Xn8mFH9jBBrB0s5kFqk0eIzL0qQBxLt6lFZ4g510mt2ZcCQ3KMbczUghicdWgDXA02e5ccUZ4qJw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHI3kDMOcR4QFZWiag73hpCzlGkoiaDRZrXE56M8PfQLJp1ibxJJVDnoS2zCCguRNKribzbxsqp8rB566juxTLMOqhlOLX3JjVrYXk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGCVWHD1gWfcD7M52bzCibC6x7Uq26udiaiaCHG5XSkThpsPwbvd5J2RIBAVZqd7USFU7D2k8KT5GZfWkdx1k9ib58bMqqibA90hen4/640?wx_fmt=png&from=appmsg)

#### **三、配置安全选项**

1、账户配置

重命名管理员账号为test1234(配置完后，可以尝试注销，看看administrator是否能登录)禁止使用Microsoft账户登录

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFT8nhZCD1YrFibkrniazzBk1t2WZMdFtZm2DibibXxaWv707HPfkOlzQW5cteH1Rtvgnyy3L6eC2ySbciaXZkRa3zUPJXWdGpFAz54/640?wx_fmt=png&from=appmsg)

2、交互式登录配置

如图，配置

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trF4KEECApNOSUf9aibW8iclpKn6aaHGVVCgeQRGwFzIicI2Fg1yyrN2mdNiaicUaZVuUHiarqBCUlCzFSru7c2d3qm3DfYicHfZLG652U/640?wx_fmt=png&from=appmsg)

3、用户账户控制

如图，配置以下四项

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGE4aO1XCGYut8IsoswmkbRicwSJzWBNfQz3Gyy5nHsXUrkQgeOhbicE2hpaxBef4Soiafx5NxrSc2GZ3D8kdibjoRST0v9HEoknu8/640?wx_fmt=png&from=appmsg)

#### **四、高级安全审核配置**

1、账户登录

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFMFZb7AiaW1pu4AE3mmOowmSyS7vzdESbXuqh1OCRKuCUyvYOlNruaz9rhmy0Czf6S4v5PIgpE37iaF1KvUEuMWA4sKAs2r3mDo/640?wx_fmt=png&from=appmsg)

2、账户管理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFiawxjAVFJ8QuDGWaVlxJ8XFYI7tpHsB1pyJbC8qib3fhpu70EGPBFKrQAPS3kTqYmGbVs4T8M3ct9QJFA4DRdicnyPvrpics0PkE/640?wx_fmt=png&from=appmsg)

3、详细跟踪

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHMm98k80Buq58yVlNiaVCiaicGgweMsEI2sXxryzkUIOcpAFXRmJ3f9IWcmMVguFibML7kcto0xcqjICPTYCQoa4cz9ibrfXwHWalg/640?wx_fmt=png&from=appmsg)

 4、登录/注销

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFfxHO5ic6wKXtf8oHymODLniaGq5aC9QTX9TYN8TL09XWPSmgYcYOGbkKEpB6oxgLKz9gc7VlC5f5K1ibyzmwZf3NX2MgPRx2XSI/640?wx_fmt=png&from=appmsg)

5、对象访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGf6aMGe3seHIR8Lmsbux1YcM9hQLufnWWVKXKrVDYXZ4Sv4jMGaQ02ZCZumDicyXOLJHGp6QYC527z7xHicK8cibpwK3lY2SlgicE/640?wx_fmt=png&from=appmsg)

6、特权使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHL5pvASTFU93vSOdOpBf5PbnL2s4NCBxyKlvKfDfSrD6SIloBTtoPSlpRCkibfjZUzibthwzGCANkyibD2WXVsmeMQibI7x19SXnE/640?wx_fmt=png&from=appmsg)

## **实验总结**

本实验讲了windows常用安全配置，但不够全面，仅仅列举了一部分配置。也可以先理解这些配置的具体作用，以及尝试验证配置生效。再来举一返三的理解其它配置。除了手动配置外，windows提供了一些基线管理工具，可以便于我们更加方便地维护windows基线。有兴趣的可以自己研究。参考网址如下微软件基线管理工具如下：https://learn.microsoft.com/zh-cn/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-compliance-toolkit-10

往期文章：

[什么！！验证码就这样破解了？](https://mp.weixin.qq.com/s?__biz=MzYzOTAwMjY5NQ==&mid=2247485479&idx=1&sn=3b1c01122131017cdfa51e15db0a8ba5&scene=21#wechat_redirect)

[基线管理之Centos安全配置](https://mp.weixin.qq.com/s?__biz=MzYzOTAwMjY5NQ==&mid=2247485649&idx=1&sn=c52bef3d53cc6b900998cdb16316cea4&scene=21#wechat_redirect)

[原来你的操作系统信息是这样被泄露的](https://mp.weixin.qq.com/s?__biz=MzYzOTAwMjY5NQ==&mid=2247485570&idx=1&sn=8f58b27a62407bbba3a5a48ff0a29ee5&scene=21#wechat_redirect)

[这样改完，购物直接0元购？](https://mp.weixin.qq.com/s?__biz=MzYzOTAwMjY5NQ==&mid=2247485562&idx=1&sn=e1aec2b3ea7c4d3147582be02d9d6c6c&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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