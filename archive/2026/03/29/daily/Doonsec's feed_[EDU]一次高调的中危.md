---
title: [EDU]一次高调的中危
url: https://mp.weixin.qq.com/s/tK1SusoNq4QHbiId4miucA
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:35.640564
---

# [EDU]一次高调的中危

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbAViaCXmmakjianpqTZAMXXOiaiaZnnQqyFOCiaMjfXEDYtm67BqB4vnrCPER9o1w7Y9ZRv37nye6GibsJq59ic5cjXM6XyjdPib8AyXk0/0?wx_fmt=jpeg)

# [EDU]一次高调的中危

原创

略懂安全的三秋
略懂安全的三秋

略懂安全的三秋

![]()

在小说阅读器中沉浸阅读

前言

在百无聊赖之际，我又开始了刷漏洞，这次运气很好，很快就发现了漏洞。

正文

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbBUyG04o0fibZNJzCoDYxr6Q3jef0xoS41yLcB5tiaAgkyhzQqiaEnQINrlLRfNS5ViaS7WO36kToYH5ZHNtmc4U3atUB1JqQbgdPo/640?wx_fmt=jpeg&from=appmsg)

开局依旧登录框起手

可以看到这是典型的若依系统，直接上弱口令

`用户：admin ruoyi druid`

`密码：123456 admin druid admin123 admin888`

`无果`

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbANGdqWSz97NtTqRS8CDmbZsfficTI02JtniafsMicvJRTsuMNtauHA2iaibZoLRhkBs8rnAH3P1QibolymyAlUAAqXBgd43rKBVH7FU/640?wx_fmt=jpeg)

`只能看接口了`

这里直接上结果（因为忘记截图了![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_45@2x.png)）

一开始结果的扫描返回的不是403就是404，但加了/prod-api/就有货了

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbA4joHQtGFc6aNZzeKu4CiaDcqBHh9l8jiagaJlqxlVyyHriaibv4ygHSHBEaQcYz4w1Rw8mv4txE0mxpiaRiaag78llJ9wCRLV0AI7g/640?wx_fmt=jpeg&from=appmsg)

在这个接口了可以获得存储桶临时密钥

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbAibsofosjyNqrIg4kj26EJrCP7x3CDpLSnI4svl0iclAJ0XQa3No3yZAmPGbMeVV4drEOFfU3jLA1T2uWfsCC6ahjvdNfmlOuHY/640?wx_fmt=jpeg&from=appmsg)

`可以上传文件，但没什么用。`

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbAgFclz3JjLomyHsBGWNshGaywr5hQO70p3l6e3S581negcCR72oc35U4FpNw2ulX2eN0Ce9zQiavJ0mBbJibfiaUsmDqksrSBeos/640?wx_fmt=jpeg&from=appmsg)

`这个接口可以删除部分用户，但不能删除有管理员权限的。`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbDNYT9CqnNziaI30R3fn6URVrDXX3oqvaQqaMyuwIgJOibfzg6rGvqHibMP1UgPLC4s7iasldv8hpWf5WyU1VpC2onM5LD146qFHg0/640?wx_fmt=jpeg&from=appmsg)

最后一个接口才是拿到中危的关键

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbDVmHhRAicxU2ANZcyNUpaVIUBtH3S0aL1o37o1X2e747U6snelhktvtApxQYO4Uw4bOcZ8JktHjFJDygMhLhjJ14ib3FgKSIwN4/640?wx_fmt=jpeg&from=appmsg)

`这个接口可以得到该学校学生的手机号名字学号，一共有1000000条`

`文章来自作者日常积累，未经许可严禁转载，转载需联系本人。文中内容仅限学习交流，严禁用于商业及非法用途，涉及网络安全相关未经授权不得测试，违规使用后果自负，与作者及本文无关 。`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCLibpoeKyUIrykBCCd4Ix1Q2SVIyIsc7IGsL6y2kJktXuMpEpkOprEoL5TVjNdLBTeiaVESIo318WKeepXDXS0sfibQPxG3maGhU/0?wx_fmt=png)

略懂安全的三秋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCLibpoeKyUIrykBCCd4Ix1Q2SVIyIsc7IGsL6y2kJktXuMpEpkOprEoL5TVjNdLBTeiaVESIo318WKeepXDXS0sfibQPxG3maGhU/0?wx_fmt=png)

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