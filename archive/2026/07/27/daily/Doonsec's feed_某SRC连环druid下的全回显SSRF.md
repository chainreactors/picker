---
title: 某SRC连环druid下的全回显SSRF
url: https://mp.weixin.qq.com/s/R0N2Poeb-H-DravhW2InAw
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:56:16.806121
---

# 某SRC连环druid下的全回显SSRF

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RBe5hMcdh0NtPLs3w7ia3Z4hsW7U1HTicaGibVZQ0Dxqe6iaAI6Ta4es8nZ4s7k64WVicZjUic55lPLzpZojttPiavp0CPd5zObPP3pQR0I869OPv8/0?wx_fmt=jpeg)

# 某SRC连环druid下的全回显SSRF

福Us1r

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于月的造梦星球
，作者月

![](https://wx.qlogo.cn/mmhead/ibkKkoaQFco5pQeXibaCYf7M9wfmBa82WiaGBGtUbYqyWNIX7E2fPhbjCYr9qlfUV2UHWZElnmEdpI/0)

**月的造梦星球**
.

临渊羡鱼 不如退而结网

开局经典登录框入口，常规`F12`审计`JS`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0OLPcTBMbTkBrEaV98icibW1BGubWaMEBkfybh6icD7KFOx6NW626TxV9HnqIGia6CAhj6rpEBjWmC5tbicxiaYnibD9u0x4icQAicz52mo/640?wx_fmt=png&from=appmsg "null")

通过任意路由触发后端请求如登录，拿到`base：/video_promotion_web/`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0ObsN7Dgibanmm6RIzKj2Jx4smTdzibDSMT9f8HPObY7xb5DcS7iaYrV0p5Q3ywvmJuvtrHgdFSibbo2E5az66SztiaAA2NJqZsPUiaE/640?wx_fmt=png&from=appmsg "null")

递归`fuzz`该微服务，发现`druid`未授权, 但在`url`监控中未发现可利用信息，依托业务理解，前置`base`微服务往往有多个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0O0VS2lro8seDdE6J6Xg1uzcY1hMAO27pRD9pomWcYsDeLuB9fnujQqZ18kMZULboQI8MxFtgHVESD0T1vaXfrHlTUvU0mtfcY/640?wx_fmt=png&from=appmsg "null")

**随即定向**`fuzz`**微服务**下的`druid：/video_promotion_{fuzz}/druid`；拿到第二个`druid`

```
druid：/video_promotion_{fuzz}/druid
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0OiaOS6IOpg7qEYJmQm2JyXicYlygcGIkLcg9HwTVul1gLO8ia9pTPdqSC0eh25mUZl1orWo57yYniaF6Xvia1hU7wxsUz8TNDQXUk4/640?wx_fmt=png&from=appmsg "null")

在第二个`druid`当中，回溯`uri.htm`出现了后端接口地址，将`uri`提取并作为微服务字典进行第三轮`fuzz`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0OBg41J4Vhicm8yC7mVbRKFLboz9yoKhQwoRUuAHD6hIUDjKUwdXqZN9r34IkOEHlFDtPuAt9nDyw8BODhNpcdQyXz2w776aBcA/640?wx_fmt=png&from=appmsg "null")

继续`fuzz`其他`druid`，成功拿到`log_spider`下的`druid`，出现新的`url`监控信息

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0OdhJgMz8ibyqjicapXb0t4vmzHrT0Ltg1g5YicnzvqMfb96ibsvhjAYbooeQjyI3lsshOWib0ZUIpGOhkNj0yy2qFUpPiaYtI7XdZn4/640?wx_fmt=png&from=appmsg "null")

观察监控面板发现接口：`/proxy/request` 根据接口语义很明显是代理请求相关，联想到`ssrf`

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0PVicmGOQVCMbLQ1d7aHicKTHznjtEkRh6P5X4J50VVLfEHelw7vrsAPfdUiaCPxiaRYciatTrx1oIt8nwiaXspBmgFNJZp94YpiciaCYI/640?wx_fmt=png&from=appmsg "null")

提取该站点所有接口进行分割制作字典，丢给`AI`构造参数和自行发散思维，最终构造完整参数读取内网`K8s`集群拿到全回显`SSRF`

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0MvlJLZiaZ6fKcl2m8CMicryyLJtQccmTEB3Wl6uJcKG7tvYXMRqV594P1bagJDk8Q3AaU9AcN4OAdENmtEum51UkM72qbrxFjDs/640?wx_fmt=png&from=appmsg "null")

---

欢迎加入纷传圈学习更多实战报告小思路

![](https://mmbiz.qpic.cn/mmbiz_jpg/RBe5hMcdh0PFibicyibMx0BYndiaxJDdzkYodueAcSfAKEaNmSicGUgQHD8BJLY8dnTq4oob9MyNnKkKwtZLdhuibM6fBRq24mJuN6bPKDBkRLnbo/640?wx_fmt=jpeg&from=appmsg "null")

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/45lGnDCSMe7IfvBRWW0hac5qPrhzB1W3wPiabUNu0j0sQH5KjW5CiaTsl1jubK8XPcZlZibjlViaw95oL1ia8V6lETw/0?wx_fmt=png)

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