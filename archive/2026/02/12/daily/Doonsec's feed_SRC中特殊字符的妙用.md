---
title: SRC中特殊字符的妙用
url: https://mp.weixin.qq.com/s/55Le2Gn1rKyRDe7ojpKaqA
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:15:04.982911
---

# SRC中特殊字符的妙用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JnmoqeNZZwRKdLe6ZME8jmp3Lm65TDqdngao4YeSk8a3IFXQjumFN8mVawjUgjuCQxFsBW07INNpwB3B73BiavWRIoCPNU3QMjSARkRI8u5U/0?wx_fmt=jpeg)

# SRC中特殊字符的妙用

原创

Fares Walid
Fares Walid

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

点击上方[蓝字]，关注我们

**建议大家把公众号“Z2O安全攻防”设为星标，否则可能就看不到啦！**因为公众号现在只对常读和星标的公众号才能展示大图推送。操作方法：点击右上角的【...】，然后点击【设为星标】即可。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuao3T9EnGbUIqxgDhEVicCV8NbH4FiaZ3YIbpXNEr6qFicGkAelnQHKGHsVlfapMGgO3DHA68iaiac0n4Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

# 免责声明

本文仅用于技术讨论与学习，利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者及本公众号团队不为此承担任何责任。

# 文章正文

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/JnmoqeNZZwRq8yNK7aWJYtic6B7louSG1iaHIPmJsFqNEP3uMlfrLBGRcJJmhDqD0N9YFbEJXdXugF6reUhW8yfnee32gr9b8LXjjwWschvN4/640?wx_fmt=png&from=appmsg)

img

今天，我将结合自己最新挖掘并解决的漏洞案例，为大家分享多种利用特殊字符挖掘漏洞的场景，讲讲如何在漏洞赏金项目中巧用特殊字符实现突破。

后续，我会把案例中涉及的目标平台隐称为“affected.com”，因为这目前还是一个私密的漏洞赏金项目。

接下来，正式进入正题！

## 一、什么是这类特殊字符？

这里所说的特殊字符（特殊字母），其实是和键盘常规字符外形相似、但分属不同语言体系的字符。比如，英语、法语、俄语、印地语等不同语言中，就有许多外形相近但归属不同的字符，举例如下：

* 英语：A B C D
* 法语：À Ɓ Ç Ð
* 西班牙语：Â ʙ ʗ Ɗ
* 拉丁语：Ă Ḇ Ĉ Đ
* 俄语：ᴀ Ƃ ʗ Ɗ

可见，这些字符和我们键盘上的常规字符外形相近，却分属不同的国家和语言体系。

**「关键在于，这些字符的编码值完全不同！」** 这意味着什么？举几个编码示例：

* A: %41
* À: %c0
* B: %42
* Ɓ: %81
* C: %43
* ʗ: %97
* D: %44
* Ɗ: %8a

当然，小写形式的特殊字符也同样存在，上述仅以大写为例，小写字符也能用来挖掘漏洞，原理完全相同。

我们利用特殊字符的核心思路，就是用这些不同语言的形似字符替换常规字符，以此迷惑系统和服务器。

因服务器配置不当，很多时候系统会将形似的特殊字符当作常规字符处理。比如字符Ɓ，会被服务器默认识别为普通的B。

![image-20260212153106961](https://mmbiz.qpic.cn/mmbiz_png/JnmoqeNZZwTVXzyz6uHnpmVFLbgJd4vXLhGMEckPnEbdsza3yZ1RCjLhdukGic1Q5hJCNmW42ib9zUNYhCTCqCyC5gDYVhUbgSOJHt0flobCA/640?wx_fmt=png&from=appmsg)

举个例子，原本的邮箱是black@yopmail.com，将其替换为Ɓlack@yopmail.com后，服务器会照常处理。这种情况的出现，绝大多数是因为服务器或系统的字符解码配置存在漏洞。

## 二、如何获取这类特殊字符和数字？

方法其实很简单。

我在漏洞赏金挖掘中，常用这个链接获取特殊字符：

https://0xacb.com/normalization\_table

这个网站里收录了大量大小写的特殊形似字符。你也可以在谷歌中搜索“拉丁语特殊字母”“西班牙语特殊字母”等关键词，找到更多同类字符。

## 三、我挖掘的两个最新漏洞案例

### 案例1：利用特殊字符绕过安全域名限制

某平台的管理员可对特定邮箱域名设置访问限制，比如禁止用户邀请以@gmail为后缀的新用户加入平台。

普通用户本应受此限制，无法邀请gmail域名的用户，但只要做一点改动，就能轻松绕过——比如将@gamil.com替换为@gmaĨl.com。

我在测试时，拦截了邀请用户的请求包，仅将其中的@gmail修改为@gmaĨl，就成功绕过了限制。

操作起来简单到如同呼吸一般！

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/JnmoqeNZZwTiaiafcVNGf68LiaN6N7eia5y26oglhPslJCTfZ5CEQpfF6Ht1PMLZvZdXNntjejJA3uQDXam6UKhn82gcMpB9EhBwz9VfSOqEtSo/640?wx_fmt=png&from=appmsg)

img

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/JnmoqeNZZwTfyF01WpnicY3ZLhISLJ3yKWCJxVacK9DfXJkc8EP9s5ibgzRqsFfpM6VhAXTKnPAUMgQqEj4M5j4wEksRRMliaoamViaT1UJuHG0/640?wx_fmt=png&from=appmsg)

img

最终我拿到了500美元的赏金，该漏洞也已被平台修复。

### 案例2：邀请已被封禁的用户加入组织

还是上述的目标平台，管理员可封禁特定用户邮箱，例如blocked@yahoo.com。

若有用户尝试邀请该邮箱，系统会直接抛出报错，提示“此邮箱已被封禁”。

但如果将邀请邮箱改为bloʗked@yahoo.com（将c替换为特殊字符ʗ），就能直接完成邀请操作！被封禁的用户会正常收到邀请邮件，整个过程就是这么简单。

目前这个漏洞还处于审核阶段，尚未修复，因此我暂时无法分享相关截图。

## 四、特殊字符的其他应用场景

最典型的就是利用特殊字符操纵实现**「账号劫持」**：攻击者可利用形似特殊字符，创建与受害者邮箱看似一致的账号。比如受害者的邮箱是victim@gmail.com，攻击者可创建victĨm@gmaĨl.com这样的“高仿”邮箱，借此实施劫持。

除此之外，还有很多技术分享中提到了特殊字符的各类妙用，大家可以自行了解。

（本文翻译自：https://medium.com/@bag0zathev2/title-7c4cb8b49b23）

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