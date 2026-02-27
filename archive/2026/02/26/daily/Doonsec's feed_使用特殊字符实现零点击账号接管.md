---
title: 使用特殊字符实现零点击账号接管
url: https://mp.weixin.qq.com/s/4d8vxwaLy0WSu9Iqcou21w
source: Doonsec's feed
date: 2026-02-26
fetch_date: 2026-02-27T04:06:04.553199
---

# 使用特殊字符实现零点击账号接管

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JnmoqeNZZwQuVcE1hDQib9AShPuyJcnLibic91ymlfS6vZVHQ8HOhVbwQD4j1icjjVibSqjGzuGLcIYvcIJmVfU0wTvAmTW4EzaJLvPGsgAiaIEHY/0?wx_fmt=jpeg)

# 使用特殊字符实现零点击账号接管

原创

CaptinSHArky
CaptinSHArky

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

点击上方[蓝字]，关注我们

**建议大家把公众号“Z2O安全攻防”设为星标，否则可能就看不到啦！**因为公众号现在只对常读和星标的公众号才能展示大图推送。操作方法：点击右上角的【...】，然后点击【设为星标】即可。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuao3T9EnGbUIqxgDhEVicCV8NbH4FiaZ3YIbpXNEr6qFicGkAelnQHKGHsVlfapMGgO3DHA68iaiac0n4Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

# 免责声明

本文仅用于技术讨论与学习，利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者及本公众号团队不为此承担任何责任。

# 文章正文

今天我要和大家分享的，是我发现的一个知名苹果生态服务公司（主营macOS端应用）的漏洞——通过特殊字符，实现对账号的零点击劫持。

接下来，我们深入聊聊这个漏洞的挖掘过程。

### 漏洞挖掘的缘起

事情的开端，是我收到了这家公司的漏洞挖掘项目邀请，当时我心想，不如就参与试试？

我泡了杯醇香的咖啡，开始对这款应用展开深度分析。两小时后我发现，应用的诸多功能都处于锁定状态，必须通过macOS端登录并绑定苹果电脑才能解锁。既然如此，我想着不如先研究下它的邀请系统，看看有没有可乘之机。

![None](https://mmbiz.qpic.cn/sz_mmbiz_png/JnmoqeNZZwSOt97ic3QOFE08BuOkeme2aInKvpwlk0Sytr8uCaPaugc1cQDOBwIYkJEau9Au9LA9eV2OJIK0jicyqVtbXmpSHdHMhphicqRsT8/640?wx_fmt=png&from=appmsg)

我打开应用，开始分析各类接口请求、排查系统的各类报错信息。

我先尝试邀请了一位普通用户，接着又尝试编辑该用户的相关信息，这时我发现了一个至关重要的点：**组织管理员有权修改普通用户的绑定邮箱**。

![None](https://mmbiz.qpic.cn/sz_mmbiz_png/JnmoqeNZZwSmoSfZ9g0iaic1eEg6RSPXtZ1ZLqgyubRv3tbRPMtDJ2aiarBob1NYRiaDL8biaPUTxnzGScpLKPaT5BOgDZ8ibjUrkTZ2CxVBNYavA/640?wx_fmt=png&from=appmsg)

于是我立刻注册了另一个账号，用攻击者账号将这个新账号邀请至自己的组织中，结果却收到了系统报错。

![None](https://mmbiz.qpic.cn/mmbiz_png/JnmoqeNZZwSFFFrKTcVgxGZo0h1xqGXvhiaIjGaWSzssFWJ5qW5jpxljOJvOVZFr0iaXDRfoRkARC2m3KCWuLX6TiagVCATneXTtrWc4NIHicf0/640?wx_fmt=png&from=appmsg)

> 红色标注的用户已在其他组织拥有授权许可，你仅可邀请其加入，无法为其分配额外许可

这是个关键的报错提示，我决定试着绕过这个限制。

按照我以往的挖掘经验，当尝试通过逻辑漏洞绕过这类限制时，系统通常会抛出“账号已存在”的报错。我先做了些简单尝试：将邮箱的字母改大小写，比如把test@test.com改成Test@Test.Com；或是在邮箱末尾加空格，构造出这样的参数：![None](https://mmbiz.qpic.cn/mmbiz_png/JnmoqeNZZwTQHrOQUGRNVp7SpLeDo6B51X6ibdA1pS19ib8oY2FUPxeuZqHEIN0vcrLjgMtUOIyOEHupvRnz0K6ibfYF17l6e142Y1EdHBZ1GA/640?wx_fmt=png&from=appmsg)

这种方法偶尔能奏效，但多数时候还是会触发报错。

我没有就此放弃，突然想起一篇利用特殊字符挖掘逻辑漏洞的优质分享[SRC中特殊字符的妙用](https://mp.weixin.qq.com/s?__biz=Mzg2ODYxMzY3OQ==&mid=2247523096&idx=1&sn=4bcb67a830ca6bdbf9eb9ffee97ab352&scene=21#wechat_redirect)，我心想，不如也试试这个思路？

随后我在邮箱前缀中加入了特殊字符，构造出这样的恶意邮箱地址：![image-20260212151823058](https://mmbiz.qpic.cn/mmbiz_png/JnmoqeNZZwRcvVOQMaDaxK5J5gJJMpIKvo2LC2ux39QMm8ZicKSw6NicicacDNPdlT7Sg4X5du0VjoqhDqtXkpz6M4QFakVovIhz7HV4jg1CRE/640?wx_fmt=png&from=appmsg)

这次，系统返回了操作成功的响应！

后台并未新建一个带新ID的账号，而是直接接受了这份邀请，将目标受害者账号加入了我创建的组织中。

而这个漏洞的第二重致命之处在于：**修改后的邮箱地址，无需用户本人确认接受邀请**。哪怕受害者从未点击过任何加入组织的链接，我依然可以随意修改其账号的绑定邮箱！

最终，我通过这个漏洞实现了**零点击账号劫持**！

![None](https://mmbiz.qpic.cn/sz_mmbiz_png/JnmoqeNZZwQhLc1O9WDu7yMDlgKpicVjORDdn5mWBtej9ibFO5gbx8NSYhHW85QTTQFXuhE4dyGiakR6XEHnGZx43LhZYf72MLE8PwzUPI7OCA/640?wx_fmt=png&from=appmsg)

### 挖掘小技巧

最后想和大家说几句：没有任何一家公司的代码是100%安全的，相信我。即便是脸书这样的大厂，依然存在一些基础的逻辑漏洞，有人还能靠着挖掘这类漏洞拿到高额赏金。你要做的，只是比别人多一份坚持、多尝试几种思路。

当你在测试时，遇到任何提示“名称/标识已存在”的功能或输入框，一定要想尽办法尝试绕过限制。相信我，你永远不知道下一次尝试会带来什么惊喜。

希望这篇分享，能为大家提供一些利用特殊字符挖掘逻辑漏洞的新思路。(翻译自：https://medium.com/@mahdisalhi0500/0-click-account-takeover-using-special-characters-0030a1e3c6d6)

---

建了个src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞

圈子专注于更新src相关：

```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例2、分享src优质视频课程3、分享src挖掘技巧tips4、小群一起挖洞
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=24)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=25 "null")

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOApVm8H605qOibxia5DqPHfbWD6lmcweDjGv4DLl45waD068ugw2Iv2vg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=26)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWr5g7s0TNF4tBZqNbdewPNswTDOfvN6PkggCqz8j3mib6Vf3z4ia83asg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=27)

图片

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=28)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYrUoo5XZpxN9Inq87ic71D6aUeMdaWrKXgYYia2On8nMA7bqWDySa8odAq1a0kkp3WFgf0Zp0Eut0A/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=29)图片![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4KKlic4yiafWTpLdejicQe3MllEQc24ypeI3anaK7IjJDVyq1WVQN2yKBA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=30)

图片

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWHjP3FUnZpXdrOicRWrCf9MibaglQia7WesCVs0ibtBhC4c2XiaT9HibE1Drg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=32)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWXytl9Ioah3X7tw7EMlWV96wWXEHFEM4m6NwlvvkcmEcPqcxcE9MQDg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=33)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaDpuFU7U9TMK5eIpY8iaJcXCicmTB6fsRd8icmH7K1X99YbC07GaJbCRReocORsnDGNU7H7PeqcysIA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKubhtC8np00hvuic7VhRDuxXTZgZxWicIm5hpzd0sygt6YdSapfKHREplVRia9KvPWOvDtno8EZV84dJQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=27)

### 考证咨询

最优惠报考各类安全证书(NISP/CISP/CISSP/PTE/PTS/PMP/IRE等....)，后台回复"好友位"咨询。

### 关注我们

点个【 在看 】，你最好看

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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