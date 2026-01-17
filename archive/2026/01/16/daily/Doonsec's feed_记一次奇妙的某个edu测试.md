---
title: 记一次奇妙的某个edu测试
url: https://mp.weixin.qq.com/s/zbrYibL5qy2Sjhni0dCdUg
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:26:24.887045
---

# 记一次奇妙的某个edu测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAovSvt7vAjXfDiah5BWMb2icl2Mjq3kay1BMqwIpiccCBujTDmAlf7GFUCjw/0?wx_fmt=jpeg)

# 记一次奇妙的某个edu测试

Ssg
Ssg

蚁景网络安全

![]()

在小说阅读器中沉浸阅读

**点击蓝字关注** | 更多原创技术好文

声明：本文旨在分享网安技术心得，利用本公众号信息而造成的直接或间接的后果及损失，均由使用者本人负责。与本公众号及原作者无关！

前话：对登录方法的轻视造成一系列的漏洞出现，对接口确实鉴权造成大量的信息泄露。从小程序到web端网址的奇妙的测试就此开始。（**文章厚码，请见谅**）

1. 1. 寻找到目标站点的小程序

![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAovWwfmqURZicLsJiaXVANoHqicvzWpygBqxrDibD0ajqMFnuo3skianR52BvQ/640?wx_fmt=png&from=appmsg "null")

进入登录发现只需要姓名加学工号就能成功登录，通过google hack的语法成功找到学生姓名和学号，想直接找老师的工号发现无果，信息收集到此为止

![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAovUE1n5s7OWRfhomwaXic1oLe2Ox1z5PDW7ZZWvAfcyqbT2JDMFI1JsPQ/640?wx_fmt=png&from=appmsg "null")

1. 1. 通过学生的信息成功登录进去，进入熟悉的测试环节，成功找到sql注入

> ![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAovzbchBsicqlCZk5k5OqZ4aH29HBv963FBR9yUIK9pgekiay1kUYichNgtA/640?wx_fmt=png&from=appmsg "null")
>
> 使用sqlmap成功跑出
>
> ![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAov3r0l7HNSBdpvt6Vz4JbJveibbicWtbnUeibaqFGzhrB9OndAotw3IrNkQ/640?wx_fmt=other&from=appmsg "null")

1. 1. 本以为测试到此位置了，突然在某个功能点有了意外之喜，发现了老师的工号，果断深度利用一手

> ![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAovRdg6ib3rfLIicL4rmwgjfZTX6UUCZxOKLwXjdc0JjSgs4sXyygTnWNvA/640?wx_fmt=png&from=appmsg "null")
>
> 竟然找到了老师的工号和身份证
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAovHfUSD69iaHjyiaBVHPZ9ibLroocIY7jSeE4bENNRIpjmmvOL12kB8TiaTQ/640?wx_fmt=png&from=appmsg "null")
>
> 既然教师的接口泄露的老师的工号，那领导的接口不也会泄露，果断放弃老师的工号，前去寻找领导的工号，果不其然
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAovaoMkhd81fPWpCa8wnxJicswmet0uzGGj1bicicHeunOEzuUcMz9SibvL2A/640?wx_fmt=png&from=appmsg "null")
>
> 肯定挑官大的搞，

1. 1. 成功通过领导的工号登录

> ![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAovs9wpjguN0nAEne4lw4HfSAks1e4bfIkgRHOaMbiadLpCPbUw7Crria8A/640?wx_fmt=png&from=appmsg "null")
>
> 权限有点大，找找还有利用的地方吗
>
> 5，敏感信息泄露
>
> 成功找到一处接口，存在信息泄露，通过遍历得到大量身份证
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAov6yVNmBMzJiaXMehEwxnia8NlKzgxiaRqJjuLX0N4LrXxOPJFkeZyiabdjA/640?wx_fmt=png&from=appmsg "null")
>
> 几万条信息泄露还是有的

1. 1. 转战web端的学工系统，发现是扫码登录，结合上面的领导账号尝试登录

![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAoviaLBOo5w0h1KqNb9561WPYPRnFaFeQqngYaW7L2AxicrAibaKia6bZKwTQ/640?wx_fmt=png&from=appmsg "null")

通过微信绑定的手机号获取验证码，尝试能否登录

![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAovaD2FbbWzNswcxia7kw4PaXY5zm9tWjxOYkooqVQib3hbz2Q7GtqpicgEQ/640?wx_fmt=png&from=appmsg "null")

成功登录

![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAov13ISG65TrCF83SkibpnHYGFkbK3SyR2200p7Go0fj6Jw7qWhs5UaYew/640?wx_fmt=png&from=appmsg "null")

1. 1. 目录遍历

> 通过对该站点的测试发现该站点还存在目录遍历
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgrtoBVY18cXcGydPzXdqEAovtZKldtS9boZcVjibEzWibPzD4YmPBAibLiaAQoer8YtO1FWcaSge4RwxBQ/640?wx_fmt=png&from=appmsg "null")
>
> 篇幅有限，点到为止
>
> 总结：建议学校对用户登录时多做校验，防止任意用户登录，对接口增加鉴权，对特殊字符进行过滤，加强网址的安全防护。在任何情况下，未经授权的渗透测试行为都是违法的，可能导致严重的法律后果。因此，在进行任何安全测试之前，请务必与目标单位达成明确的协议和授权。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

蚁景网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

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