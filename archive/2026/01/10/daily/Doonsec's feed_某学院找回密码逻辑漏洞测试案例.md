---
title: 某学院找回密码逻辑漏洞测试案例
url: https://mp.weixin.qq.com/s/fCqFm2Y1y6Satmi2VYjHxA
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:39:38.003785
---

# 某学院找回密码逻辑漏洞测试案例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8nIFQgfd1Wiap1k0sTITNK02ZY1ZgaAZQz7GicFicVHdkqgEeicS83xj7Xp877TDrLHZDB1RebbbU2JZ2hSCCSCBdw/0?wx_fmt=jpeg)

# 某学院找回密码逻辑漏洞测试案例

原创

d0n9x1e

蝉SEC

![]()

在小说阅读器中沉浸阅读

访问平台如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1Wiap1k0sTITNK02ZY1ZgaAZQMkKTUFe9fyicDkOynhyGubcQphwFStv7MylgVLjVMvosB1qSTZ9ymAg/640?wx_fmt=png&from=appmsg)

点击修改密码，发现存在用户名枚举问题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1Wiap1k0sTITNK02ZY1ZgaAZQ4ZaRgPtAP7icP4O8Cohq3zlicROtribiaD214gvniaEX2hMPVcfYThoDzDw/640?wx_fmt=png&from=appmsg)

在此处进行爆破，发现存在如下用户

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1Wiap1k0sTITNK02ZY1ZgaAZQdX9omNRXfKwRv1LZM1N3I5kT9JzYfd4ALFkdZD8yAQdmb6zcYM40mg/640?wx_fmt=png&from=appmsg)

下面使用用户名cc进行测试，输入用户名发现页面如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1Wiap1k0sTITNK02ZY1ZgaAZQR5FANqqpNdicgPaJS0Uy7Ynj0Bb3BC99QmcXibqNLYQ7W1Y0X30qSWCg/640?wx_fmt=png&from=appmsg)

下面对该用户的密保问题进行爆破，发现答案为XX学院（这里是因为所攻击站点备案为该学校，故直接进行尝试），成功跳到下一步

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1Wiap1k0sTITNK02ZY1ZgaAZQCTpsXSRibQqImHpicfc0pBCdGpuXpbIzPw2XjC9YKJDoFlM9nvuGlwHQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1Wiap1k0sTITNK02ZY1ZgaAZQlccOvcxCCIssByLSpOeSoWmg0pKFraeicJkqF7row3XGWwRw7Rmiak1Q/640?wx_fmt=png&from=appmsg)

下面将密码修改为"Aa123456...",发现可成功通过cc/Aa123456...进行登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1Wiap1k0sTITNK02ZY1ZgaAZQPByPWNzvpvmYJHHfibUYjlDOqG6FlluiaJjic9Bnyu4oZmkQKGZ3jsq8w/640?wx_fmt=png&from=appmsg)

一个很简单的测试案例分享，大家在测试中，多寻找边缘资产，更容易发现类似的问题！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1Wiap1k0sTITNK02ZY1ZgaAZQCS7u3gFLyBumamI3Ijpuc5rUB32aEu5XNia0AwzdUWgsMuRxUhepkAQ/0?wx_fmt=png)

蝉SEC

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1Wiap1k0sTITNK02ZY1ZgaAZQCS7u3gFLyBumamI3Ijpuc5rUB32aEu5XNia0AwzdUWgsMuRxUhepkAQ/0?wx_fmt=png)

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