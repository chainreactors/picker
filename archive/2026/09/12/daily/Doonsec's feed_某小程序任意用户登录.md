---
title: 某小程序任意用户登录
url: https://mp.weixin.qq.com/s/fYB-xABvCErqwaJXQvel7g
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:59:41.752122
---

# 某小程序任意用户登录

# 某小程序任意用户登录

原创

暗月大徒弟
暗月大徒弟

moonsec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

```
免责声明：本公众号所提供的文字和信息仅供学习和研究使用，不得用于任何非法用途。我们强烈谴责任何非法活动，并严格遵守法律法规。读者应该自觉遵守法律法规，不得利用本公众号所提供的信息从事任何违法活动。本公众号不对读者的任何违法行为承担任何责任。
```

访问微信小程序  快速登录

![](https://mmbiz.qpic.cn/mmbiz_png/0ic45F94NibRskEIEDDvdIP6GZV4A3rtKxW5oeIESQVhctfszTDoaD5LGCK3NbWAUUsGRtTnVzVStUG0vfzTzm4jMIZ2ia98JRNZ4Zr6q1zxZU/640?wx_fmt=png&from=appmsg)

小程序会获取你的手机号码 选择允许

![](https://mmbiz.qpic.cn/mmbiz_png/0ic45F94NibRtMNJ6cMVfmsSxV8vMnTzCqfibCNDCFj9kic45q44hvBobTKN9gtq4ZAibicC61CawIJXhnE843pP6ydH9ncSUtsQCnSPpHyf7mZJg/640?wx_fmt=png&from=appmsg)

这个小程序是用什么进行身份认证的 答案是jwt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRvdFic4aaQ5HSlGgDa7ibdBibNiaXxeRBG4HOcJu3cgJKRBwEnxUYcxRmP7UGFJBHPakiceL59gPZ50bfCNtDJQaFQ8cibmB2qaOlEick/640?wx_fmt=png&from=appmsg)

那么jwt token是怎么生成的？

是通过 微信id和tel登录等信息生成jwt的token

![](https://mmbiz.qpic.cn/mmbiz_png/0ic45F94NibRsuoUHhKQyDqao27yn8X0ovp47mNouyqWb7BNhNPmC9Lp1HFiaPvLt7iaAa4EAYibKQ9lKbMPdpMUYW0j0uDo5sNK7rtZ9Qkv0NAo/640?wx_fmt=png&from=appmsg)

微信id是怎么来的 在数据包存在通过手机获取微信wxid的接口  这接口能直接访问 并没有对其进行授权访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRt6b2MM4WuM8uiaho3Dc3enAg9sfFRS14CSBrFoY3dTBJyeJOqp8o9FrFc9mTtjRUXErtBGo63tVgVKHMQC7NgicEO1eQ8Av0xjA/640?wx_fmt=png&from=appmsg)

那么 替换手机和wxid获取新jwt token

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRt8HV7hh6LnaEiazibfxZvLWxn2WOYFGheiaaqgib1tnyOIgHoh5vNyAOSJNBO1Ujv3qPKxicicSfy2jtZvNgVbiapPEMZBlWrz5iaJIqs/640?wx_fmt=png&from=appmsg)

访问 即可获取对应身份用户的权限

![](https://mmbiz.qpic.cn/mmbiz_png/0ic45F94NibRtYBkr6BLNaR8CZpvaVibtJvHIgZGb9eOvI4FdfM5fl5gWic93v42dSRYiciaHFIwn3eJic3vpbjN3KxpskdM6qWwKicnric90tc5j3q4/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Jvbbfg0s6ACib1YxUkAP5V2ldRHEzgqytbTxUd3Kao6poq8QU460nFxylPwDGauvzVCnWibRkAI7buhwHAl7GyKQ/0?wx_fmt=png)

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