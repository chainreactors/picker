---
title: 安卓逆向 -- 某诗词类APP会员保姆教程
url: https://mp.weixin.qq.com/s/fBqqzzPWJxD7BIyX0SdZyg
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:41:56.139548
---

# 安卓逆向 -- 某诗词类APP会员保姆教程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUWA314eBnSeI781to9khmNNSwDJGN7Rw4pgibnic9x1ym3wOicUJb4rpRicvXqwF52AznUaNuo8dRtXu7jeXz6leCxt11z9ia2F2e3s/0?wx_fmt=jpeg)

# 安卓逆向 -- 某诗词类APP会员保姆教程

逆向有你

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

第一步打开MT管理器（我看有很多朋友在找会员版，不需要会员），点击提取安装包，选择你要提取的应用，点击提取，这里可以看到，这个应用是没有加固的，可以直接修改，提取后点击定位

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUWePBuZqeBH1Q0gHHlSMybY561ia5rufBL08OqYXmiafOGkBoAAn3aSlwU0Q22oDkwQwibW4KicUVwD44PlAj8b1QxygnnWe9n51P0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUWMVXPN6qQbC0doeByO4mAQnAFaBug9Njxz1RgWgTLd22RfsIOziaecNfqUT6j4yfJhsFwiaW5ib27vTQMAraYzIhjQq0cMia4C7eY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUUiaibqbOM3RmugDNQQicQawwSianwlcyLDPySWuT3qYOXhwfHhQ6vrPvQGQPgQR2Sia9DAg0m5UmdKG0KOVtxVeqZzROg8tbebVWV0/640?wx_fmt=jpeg&from=appmsg)

选择查看，选择DEX编辑器++，全选，确定，选择常量，过滤-西窗会员（完全匹配），过滤出来只有一条结果（我这里截图的时候忘记点完全匹配了，所以有多条，选最后一条），搜索，跳转

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUXpMpoI3F45dm7qGIIh9NCV4Iwxq9iamhuHJQ9emaibbztNPKoZicS3W9WznQ1wQ8YHFGQ1qibIRibqv1gCrtcAdAroXdDZOs7bckxg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUU1AbuZUBf4g6tCubermZHFqxCCDIrrYB23pEsInarXlibibwlgKBUQibMnwpxC7Wdic4AvSuSjhSPRjDROne0mFHoP8ycAMNNqpdg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUXCf5x5lpiaGap4hH4ker6Pf38oqG1fyQOXtPOnRQN1DSTDKuHqraKWqkC6Uw1y8qswgA8mq04wXcLhWTweyD1E2kEDpMib3FRzQ/640?wx_fmt=jpeg&from=appmsg)

可以看到第881行的西窗会员，往上找到第865行的跳转箭头，长按选择跳，转跳转后可以看到这个会员的判断，在第2332行，前面加#，把他变成注释，让他失效，再在第2334行，直接把p0判断值赋值成1   const/4 p0，0x1

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUUyObSzDzx0raicRg5agr5FdqST9VJR622Umg6YdtI30Pn9QlEpRq6T6O9yiciclfjpZc4kD799ibnZrB1sKuNhtua2JaiaUoIqw1yI/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUX3rIS3fBqRMPL2r91wW5zsLR1Hp7rDRDXP3E5icMhEVJnCgzSg42MewGLn1Ox72icN7NuAgeYW9WFsDSvaic1zxvmebVDUHG6iczY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUWNzcqTBqooqfe3lh7d4noSibsu5TZAR99ibQ7m2MUnEtv5XKFP3FCqyibAbLiafBichSMIlL3mZ6kwInlK0oVXNiapGOqk8lTWgnBxk/640?wx_fmt=jpeg&from=appmsg)

回到搜索常量的地方-过滤-领取成功，完全匹配，搜索，点进去，按箭头操作点击导航栏，查看调用处选择箭头指示的两处按图片修改

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUUkrdtO6mZrq498bebEyrYlfTCRNWmON5mkoibcQhZoe830RjQ6YTo9iaA5BAIwBmttMlbmvZuhqVYib7Xtygobb7HMeHiaQWtG4MM/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUV8dwvTggr9171ib69icn3rcCCS1KVdfP61cUNDUYWmmUcnynhYRpibibWbps9ROYGbRic9Rju2MSeS9ZmyHibOftSppXsL2epFWXPRA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUWDBXWCOQlGENOIUIibje0LcicC9ARg4ib7LAM8HZxUFUIriaia8tPVE3ickEeFsg2UIm07SKGj8gOzCm5RcTU9jDjUWB75IH8gbajU8/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUVNk2T4ouwaEw3KQViae4AnudTC6drdHNEMNFh9wiap40g2Xb7sQO9Fx73mMptZQvdmQzWv7ca0fmkCUUp79hayZlnojKgpFl4OU/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUWHiaJD3oSQIdTibjzET7D0OyeoyzTdlgsYs6g3qcntRonUysTdiboibkTBbCqica0iat88dap5wYm5EZRzlAib9Z7Zoqiart6JGsr85JA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUX5hcpuCPtEcFExicrwicSeFeVFZxgspKM0C7ZZFJ1bawNt8oxU4VQUNaxrJSR9icrugp6SEEMKRjuoaaVlMjamb6gPUXH57VFibQo/640?wx_fmt=png&from=appmsg)

  修改完记得保存

回到搜索常量的地方-过滤-您已是高级会员，点击领取，这次不用完全匹配，搜索，点进去可以看到101行的您已是高级会员，点击领取。向上找99行eqz判断改成nez，完成返回打包签名

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUUwINibaQJ9tSw2Z6zicPgpSibdBUtPkVKb4XicCcR0VjN4mnOLwDMpucPZsnoeaGSWIcrhicpia9BnehWmbkdvMCvBJCaJ9zib2J1ye8/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUVbEoJAOZgIzdxMkpxe7dUcVlXNMsMEvbGHiaBIS3P3aeOzzuFuZLdvLPj4PB2Fb7R4Zaeo8iaHMXE2R4WP4MSFV9Pr1Eb6V9mmA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUWhHOxLbvyh8Kr75bcrXjX0gls1txcB2sxNH3coakOR6ZQTcYcmibeA4ugO6qOgKekPOiaFRDPf719aOgXwJm45I0gkeWvYF9fgo/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUWe12z9UlvkrV4sOog0I0BAVM7fyYK6Rs0TPjktIVzicJFLzqYSNGYD1TUWaKYdhywBYtv9D35ju9k8uNSGLbXtbZa84u8VbcM0/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUV1dfZHneM1K6ia4e4hze2FI6f09Ku4OArQMvejmEUndu2yMtyic9SIWGvU1AyVZ6ic7nyHYtGbPG3ZO1I0eZgXF2TicBhwWs0qy8U/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUXI5nl7McIfNYm60BlAyqUEwcMP2FS6bxicV8ONnbAO6okba70mnNfB1VujTA2Ash6YZ5ItGytdqnvHUch5nc0b86eNsFWYstTE/640?wx_fmt=jpeg&from=appmsg)

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUVbFSibdfnf1B8GricTXtH8bqmziap3WMhsZ1ib5qncuMypqZhvt0NALkhCibZ4q3H2hjqmia9viaRAMR5YmhB6UagBBCE9Sx06r0Uk8M/640?wx_fmt=jpeg&from=appmsg) | ![](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUUaia7RHRYib7LpuyXQlNHxabZHXXbVMR4C4UokKZWyyREIbJeaJsR29hYoCNRTskrQ4XzQkugicrleAo8sSbHE7lHw28YZLBOiaqs/640?wx_fmt=jpeg&from=appmsg) |

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/WJRHqUiaud0ouQQFouib41PSeoKKZO7mHSXDQ01XdAqPlLVKZD1yyPlfnErolowiaaDic5GDnU7B2GNhkou8PGqaCQ/0?wx_fmt=png)

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