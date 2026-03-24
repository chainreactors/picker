---
title: 一次针对电商的钓鱼事件
url: https://mp.weixin.qq.com/s/IhydbLuceUcjEuuuxeOnIw
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:11:26.618764
---

# 一次针对电商的钓鱼事件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q56nUfZdicH4KAvv2731d7dibS1icR4r8A3h3gibB8sic5hXRWHsJicBHJUB41zhzViaBgqVz9ypa5OdYck0VmejJ7iaDvBKGUmvOcJPuhbPtjpzBick/0?wx_fmt=jpeg)

# 一次针对电商的钓鱼事件

原创

Secu的矛与盾
Secu的矛与盾

Secu的矛与盾

![]()

在小说阅读器中沉浸阅读

起因

这个是在刷抖音的时候刷到一个开装机店的博主，据他描述，他是自己开店，自己当客服，有个顾客下单配了几万块的主机，然后货都发出去了，顾客加他微信，说是给他发啥设计图，就给他发了一个加密的压缩包，老板打开了压缩包，打开后双击了里面的文件，然后觉得不对劲马上就重启了电脑，他以为万事大吉了，可万万没想到，就这么一下，木马已经写入自启动了，在老板不在的时候，这个顾客控制他了的电脑，自己申请了请退款，然后操作老板电脑在网店后台点同意，老板痛失￥￥￥。

这个样本找老板要来研究了下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q56nUfZdicH5zzlZ67mny40slqs23qywh2QKb2Bw5ziawsuLk8VchfhTdm1MkUWgp0pvSSeaWmbvvxPicvyu9Vfic5XdWEZUnBwODxxPicnkIAuY/640?wx_fmt=png&from=appmsg)

当然先用云沙箱看看，我比较喜欢用安恒云沙箱，开启“上帝视角”

https://sandbox.dbappsecurity.com.cn/report

![](https://mmbiz.qpic.cn/mmbiz_png/q56nUfZdicH4kISpiaX9PUlWwbVaywJ7wfcK521hIIB8Ag7u0K4QJ3ibwljibvPa5icybcdTLgNWqcgWFHDsOE0vN73al8F22vnsZO13NmBzCtaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q56nUfZdicH53uaLQewPRr0C1UYYgMzibI2IBYhy3VoY4LGXyDC5CM8zzZezpq8yxQudM0RVKicyIMDsu4qlAMibJZuDr2K8KwUDhTppWriaH2j8/640?wx_fmt=png&from=appmsg)

### 1.1 主体样本

* 文件名：`子欣设计0310刘总1.exe`
* SHA256：`c0713532a5e8457c04dd8d3c57fd5c62b6da2f119d4d6c7cfa72bef44c202482`

![](https://mmbiz.qpic.cn/mmbiz_png/q56nUfZdicH5J7sIRUfUxMGXiaic6xic76aCLouwquW5LGbax7LVJeYpjniaX5YsavdwJ8SMyCOQkKBf9wSicOMjzficqTad462zMP1DyeU1hcJXOE/640?wx_fmt=png&from=appmsg)

### 1.2 释放/关联文件

### 目标目录：`C:\Users\xxx\AppData\Roaming\rehrtjryk\<随机目录>`

* `随机文件名的exe`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q56nUfZdicH5o6IibDNDskcgI3GCDGTVCtPgYFAIVb11941icvJtZq4ut1dIDWJJzKMAic3pksawuDdux9memkDgXMwiapiaUaaeKhCx6S8V2mVKo/640?wx_fmt=png&from=appmsg)

* `vjsc.dll`

+ SHA256：`e1b4a453197b74e11645f632d1cdc82d2eed40d4b9e206c5d09dc95fd7da67ae`

![](https://mmbiz.qpic.cn/mmbiz_png/q56nUfZdicH7vxSuibNZ2HhsAmn4puYbqBunkC6jcK1dFo3R0AdwJnFKdPbZzaupmw2KlTvPBVcXKSd5dcLBsmY1vqdezt1uF1aicXbFrGOibaE/640?wx_fmt=png&from=appmsg)

* `9x.dll   (网络拉取)`

+ SHA256：`116baf0147cb3a823dc57787cd4d777de899f1d05d4a3cb1c352c8eeb8cdb479`

* 其他文件：`N5RW5e56g080.txt`、`key`、`1F8BFBFF000C0662`

主要逻辑就是，

1. 用户执行 `子欣设计0310刘总1.exe ——> 随机名小 EXE  ——>  vjsc.dll ——> 解密释放——> 写启动项`

该样本一个拉一个，各文件签名也比较混乱，起初具备一定的免杀能力

启动项伪装的非常好

![](https://mmbiz.qpic.cn/mmbiz_png/q56nUfZdicH5sgD16RoibsGYXTIRhALeUYQAotyfXW0a4CiabkFPz1ejamyI0ucG7C6nXvnk4XRvibN8elC66iatcACMmgDKVOPEF0Um6rcgnDr0/640?wx_fmt=png&from=appmsg)

打开自启动文件夹，对应快捷方式可见指向的是释放的exe

![](https://mmbiz.qpic.cn/mmbiz_png/q56nUfZdicH6CNRsFqNApZ55selZBPicTAYBzt4sSCibibaOt7ydlm78jyTuAfU0LgocHpZDtN0P1WPnRT1lfFGdEZqNN5PrhO0p7aVRDZGibuf4/640?wx_fmt=png&from=appmsg)

当然最开始火绒是不杀的哈，如果喜欢用火绒的可以自己去配置一下，增加一些自定义规则

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q56nUfZdicH5rnNomB54S5rsFBJzOibNuUhQdInswibB945VrYq1ibm0PtIoiapweTZnAkjPKQeCz2OJhw2uQabnVkCichcPL7eyLDia8TYGSnqLQ8/640?wx_fmt=png&from=appmsg)

对应普通玩家，建议进入设置——系统防护——文件防护，打开启动目录防护，针对一般的想要写入自启动的木马也能防得住了，不小心运行不明文件就重启大法。

![](https://mmbiz.qpic.cn/mmbiz_png/q56nUfZdicH6ucTZb1lVAOILzWF1VZ2R8xd5fcnZHT3BAiatHha636JSHiaFdj0VIIicoog6qP2t7udt3Jzu9v3RER7iaicKp1I4GZiabTbybKwC5o/640?wx_fmt=png&from=appmsg)

别乱点别人发的文件

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/OQYwpDLv2jicjCgibvbCnqpA04FEValkUOEQV0B4dcRqdCShMFt87GXDEo20q9KlOoYYibhNbrRDnXWCwBKSkgdiaA/0?wx_fmt=png)

Secu的矛与盾

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OQYwpDLv2jicjCgibvbCnqpA04FEValkUOEQV0B4dcRqdCShMFt87GXDEo20q9KlOoYYibhNbrRDnXWCwBKSkgdiaA/0?wx_fmt=png)

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