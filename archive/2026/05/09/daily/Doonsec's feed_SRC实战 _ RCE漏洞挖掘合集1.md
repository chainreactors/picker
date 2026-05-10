---
title: SRC实战 | RCE漏洞挖掘合集1
url: https://mp.weixin.qq.com/s/wL3PL7pa5CiN3j7neSfB1g
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:31:34.970514
---

# SRC实战 | RCE漏洞挖掘合集1

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6mEJuibtxKvOME0zUrsmmo1nEeVUaFUuT5fJic530hRvsBibqWPLWoqunyM6TFdWbxeM7q7zEyAd5iaaM7xe00zjxF3ag2pvnXHGLkZuAUs8qQ4/0?wx_fmt=jpeg)

# SRC实战 | RCE漏洞挖掘合集1

原创

安全艺术
安全艺术

安全艺术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 1. 持续关注新漏洞，不断发散挖掘

使用了Dify/Next.js框架的资产，可以有针对性的测试25年爆的CVE-2025-55182，还是有很大几率可以出货的。

在SRC实战中发现很多都是非常规路径下的接口，这就需要不断实战去积累了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvNico5iahDEYIIepX2HFs5ibrZibQMiapuYY0bQPNo1TKbhmcxWd3YCrYFnlmC9Vib8AbPenHkfRluwYEvaKgEgYSczU3z7oU3G36AEw/640?wx_fmt=png&from=appmsg)

帆软的类似于下面这种，跟在一级目录后边的，可以借助burp的目录递归扫描插件或者自动化工具去跑。

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvNJcYnyicpvOhiaL3xlWtVBHjxpWfpN3icVGqohEpSueeyzialqH1DRguGXyk1Psm7bjcKUaKAnNUZvaMqR4ibW7HzVoxVHOn3C9swY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvPIZ0VhQmZ1BrHlaRvPu3Omw19Vep08oQkSlu2OOp8PeDPXOmXnZOfAW60lcmY4ibCejeZZnM333MV4PciaqMs7qLOuoru9hGLib8/640?wx_fmt=png&from=appmsg)

还有一些大模型平台，想办法进入后台，有很大几率可以RCE。

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvO6apWibWOzSozBEvtDlk2gpiblG2RcwFBcibiaemNyp0cFysibReIU9KhN9uRfMHicVTPiccGmEcm62xmX6kgwC1yT7HMicgEOW8vd8V0/640?wx_fmt=png&from=appmsg)

# 2. 组件类RCE深入挖掘

多级目录下深藏的ueditor。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvMR9MS76qn6mFRyWTHjgARVSVwQTCWgwUxUVZsSr1O2KlyvqqYgmpJPSFSVUiaKEqY9aYwn67icSQUDDAVRXVjGoiaWlUGgXMGMoI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvOkzibxNibhcmSp709UWl90yITsiaLicNM53FsmfKLPlqtCR6x3YZAawSvruGbVWO6XBuPDcSxIibj6Qp0vwwZf20lLz9Ee3kK8TkuY/640?wx_fmt=png&from=appmsg)

# 3. 稍不注意就错过的RCE

js里面发现的旁站系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvMGsCOwSnUy5mDLMEWDzWlzptS6sJG98ZV9qHlcH8S5hd4H2eJgCIJlpiaEMbxsEeiaUM5Nj7lgX9wKvxee4EVQkWgowbZN937aE/640?wx_fmt=png&from=appmsg)

直接默认口令进入===rce。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvNN7Cs9d8ZMEO1RYTmWNKrNB2h9hJmJU2pDQkhfGeJlyo8TduIHtu4icnwlyPNtc4TGtA5yP5gIkLibXdbRA8vAdURibicssBQ1rVU/640?wx_fmt=png&from=appmsg)

通过sso跳转后发现的非常规xxl-job路径，登录成功就可以秒了。

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvPyzaLAoIDTXSjNTCwdKm7XBaUBiaaoAfnChaRGS1z71xcibsqOUmd3dOGicSQsWRqlb1c9LD2vw9dribGspCBYspMlwNZwEvLibDjw/640?wx_fmt=png&from=appmsg)

非常规路径下的shiro。

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvODDAyw020siaMFw5jjPfz2fT4Vnbib1BKGPKYB6L5oU6Wkv9DvlCD6OBianLQCg9Xcwm8hUV7DbvtBEY0Jb9FgfqeiaDy4JxUoyzw/640?wx_fmt=png&from=appmsg)

非常规rememberMe字段的shiro。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvNicDvkkYdTW2qTLDlSxKtBfUxu77jwXGQdnPoFps58MWhVa8vX4xdsgibSykDwHaQB5GK01hYFR5OcSTct8JDDdX9TBgYJoyhzc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvMEvfx5vTesJIG0eqoeQUB82dgJbIiazRQEyKeibW1ZsZ9ud6KNWGRklPqzo89j5zHtlRptYBWdUu7bNznW1ZyhIT8ZMf9bV5muM/640?wx_fmt=png&from=appmsg)

老规矩，随手推荐下我的小圈子啦，想入圈的师傅们回复"dddd"获取联系方式，无意勿扰哈，谢谢。

![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvMeKa1jVOyym7ymE68DoOFZSAIicBstpQto9so7dpqxpaLBySnLKEzOjtQC488C5gbLKCwGicx3Qqz2rsRybTl3nibLiaCjBLSvl5w/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Oo4NY9fLLoomQgld6ia6hfpRbrvGyVibgUgzOauMBthcywVUOU2bSRtSyjunLPVQNqRAO2YKH85bPMg/0?wx_fmt=png)

安全艺术

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Oo4NY9fLLoomQgld6ia6hfpRbrvGyVibgUgzOauMBthcywVUOU2bSRtSyjunLPVQNqRAO2YKH85bPMg/0?wx_fmt=png)

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