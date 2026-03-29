---
title: 瑞斯康达Raisecom智能网关 list_base_config 远程命令执行漏洞
url: https://mp.weixin.qq.com/s/PApTROH77SN3nQSEqSfkXA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:37:53.734461
---

# 瑞斯康达Raisecom智能网关 list_base_config 远程命令执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XpPOHs6ZLMGKialCq4xrvYicicEDodxhqIFK1Zp1qwyLhK1r45BN0XVkqCk7lqpvIknbALcuSBuWCWLg0uhrJmbAfIWaCo9SrTFpbmCP8HG23U/0?wx_fmt=jpeg)

# 瑞斯康达Raisecom智能网关 list\_base\_config 远程命令执行漏洞

原创

Caigensec
Caigensec

菜根网络安全杂谈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GagrLP56FibVwx4hfFezZXyhDATCQtibMyLqTzMlb8DXuhXPvQ2pwyG7UsYv9As6Ujffp9g7wiaDVBNo4ncIghIkA/640)

点击上方蓝字关注我们

![](https://mmbiz.qpic.cn/mmbiz_png/Rw1GYXElC3fsz3fQsXSqeO7MgiamgBtBjFwpXTXJkafnVYDcxTe2VibnQPWsmZnoiaLeOzRqf8pgRsA8d7gsEMDhQ/640)

![](https://mmbiz.qpic.cn/mmbiz_png/ick6R1E3YokGa1ibCe5rpdRyAoBRvrYqueA3wY9CwYuRkqG2lE5MctQus6KVY2uic2Kj03Cf6xiaQHzOjibL8QJTomw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Sg02xflJ62rdxefX9thdaL8hxJWicY1vPlEmzNIWcBy2ypXTggHXX9e0kFDEVicficwTDdlLHLNrh6ica1SEvMqKeQ/640?wx_fmt=gif)

免责声明：本文仅用于合法范围的学习交流，若使用者将本文用于非法目的或违反相关法律法规的行为，一切责任由使用者自行承担。请遵守相关法律法规，勿做违法行为！

01

漏洞描述

![](https://mmbiz.qpic.cn/mmbiz_png/1BiahkUNKiclteCuCXiaCW4UMxvnLW4rTb6NTKnUoGsLbztIoJUj2t9ttkcdhm6ryDTH9k9b8uyl7Tj9Rf3PaWMYA/640)

Raisecom智能网关是瑞斯康达公司面向中小企业及行业分支机构推出的新一代语音融合接入型网络产品。该产品集数据、语音、安全、无线等功能于一体，能够为用户提供一个综合、完整的网络接入解决方案。其接口list\_base\_config\_php存在远程命令执行漏洞，攻击者可通过该漏洞执行系统命令，控制服务器。

02

资产测绘

![](https://mmbiz.qpic.cn/mmbiz_png/1BiahkUNKiclteCuCXiaCW4UMxvnLW4rTb6NTKnUoGsLbztIoJUj2t9ttkcdhm6ryDTH9k9b8uyl7Tj9Rf3PaWMYA/640)

FOFA：

body="oForm.user\_name.value"

body="/images/raisecom/back.gif"

 title="Web user login"

03

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/XpPOHs6ZLMHobubyUcS4oCTbia813OeNh1vlbOibGCePUF8EfW1mfQLPK4y7wOGuy8e0ib7WqlyKglnXDiaGZ3HFMPjdD007ibJRxwXIsxOVw11w/0?wx_fmt=png)

菜根网络安全杂谈

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/XpPOHs6ZLMHobubyUcS4oCTbia813OeNh1vlbOibGCePUF8EfW1mfQLPK4y7wOGuy8e0ib7WqlyKglnXDiaGZ3HFMPjdD007ibJRxwXIsxOVw11w/0?wx_fmt=png)

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