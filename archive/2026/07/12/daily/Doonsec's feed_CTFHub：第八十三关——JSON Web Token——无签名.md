---
title: CTFHub：第八十三关——JSON Web Token——无签名
url: https://mp.weixin.qq.com/s/lHBxc9J69OJU49XlraGmvA
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:26:24.069964
---

# CTFHub：第八十三关——JSON Web Token——无签名

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TkbqemjbpIrwTSm1MV5YwRAAiby1lRAG9DUbyXqjbgrkvIQj8icYQd6uDUp67EXjvLliarSwIqAD9m1ClQtJrMYFznianL9B0gPsQnWqUa3yPIk/0?wx_fmt=jpeg)

# CTFHub：第八十三关——JSON Web Token——无签名

原创

君陌社区
君陌社区

君陌社区渗透安全笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CTFHub网址:【https://www.ctfhub.com/#/index】

登录账号
点击技能树

选择“web进阶- JSON Web Token-无签名”开启题目

题目描述: 一些JWT库也支持none算法，即不使用签名算法。当alg字段为空时，后端将不执行签名验证。尝试找到 flag

漏洞原理: JWT支持none算法，当Header中指定alg为none时，服务器会跳过签名校验，攻击者因此可篡改Payload内容并置空签名，从而伪造任意身份（如管理员）登录。

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIp3tPqBoqatfQDkPzTKuTlKek6uI7eQbiaVqmRb6UdhN1gqKhXL1v49LvV2aylMdG5HybtKvta5ec7yCj57nxRm1Z0yDCKr6IU8/640?wx_fmt=png)

单击打开链接进入靶场实战练习环境，页面为一个登陆界面

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIqIwshFVpUxSZyT3yCppicyR62YGMjelake298ibgWm6VEAPz7EDM7iccduibvaW1EcFuYpUBjfVSgPbJibI5VGibibiaW9ekXudM7hxWE/640?wx_fmt=png)

输入用户名admin和随机的密码之后登录，页面显示“Hello admin(guest), only admin can get flag.”意思是只有管理员才能得到flag数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIom9vJvQlG2KmRsks7XssPPtHBxIR9OCZF6vShiclrmwfhJJdW14LKW5TRBokWic44u0bh4Df9DaKqggwaNWODcEo8LdxyklutJA/640?wx_fmt=png)

重新登陆并用Yakit工具截获数据包，服务器的response包含token值，其中Header中明文数据为{"typ":"JWT","alg":"HS256"}，本关卡为无签名，意味着alg需要设置为none，这代表需要改为{"typ":"JWT","alg":"none"}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIoOI3ibiaUYekMxyFicPGQUEZNhH8Q5bosy1QbjYLmxex2CSuNTJWGkYECibsbNXIj4S9bPibyJC2VDWv6w30pDxAMPPZRRx2Cey3hw/640?wx_fmt=png)

下一个数据包中Payload明文内容为{"username":"admin","password":"123456","role":"guest"}，页面提示只有admin能获取flag，说明role角色应该为admin，这表示应该改为{"username":"admin","password":"ljn","role":"admin"}

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIrVD7ncHEYgKibRs62ibCibzY7XXP82rf7o1iaYsQ6hDDlMw8cJeiamTprVnp5QsyPMBNtLmsnshPL82DDTicKZxHoooLF4ja5ZeKnmw/640?wx_fmt=png)

使用jwt解密网站解析，完整如下所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIrrEtB4XE62icKdMnCw1aVyRTjKZIHHg10FmbFeXrB3PLkeACFWEBFd0sp15TTCegUJpV2kyxAXyIlgcXn8ufcmrzcJyX6bBlf4/640?wx_fmt=png)

```
{  "typ":"JWT",  "alg":"none"}
```

加密为

```
ewogICJ0eXAiOiAiSldUIiwKICAiYWxnIjogIm5vbmUiCn0=
```

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIqZickGk6Y1LMnT7SQIpMnc9s6wbf9jLkT5PnuGxLiaKg1ebvlElQonGLgfKydxrnTHRftqL8qpHh3Y61RDyYNrIGEfLsl7tG76Q/640?wx_fmt=png)

```
{  "username":"admin",  "password":"123456",  "role":"admin"}
```

加密为

```
ewogICJ1c2VybmFtZSI6ICJhZG1pbiIsCiAgInBhc3N3b3JkIjogIjEyMzQ1NiIsCiAgInJvbGUiOiAiYWRtaW4iCn0=
```

由于使用无签名算法，所以Signature为空,将其移除。然后使用.将Header、Payload拼接起来，得到新的JWT token

```
ewogICJ0eXAiOiAiSldUIiwKICAiYWxnIjogIm5vbmUiCn0=.ewogICJ1c2VybmFtZSI6ICJhZG1pbiIsCiAgInBhc3N3b3JkIjogIjEyMzQ1NiIsCiAgInJvbGUiOiAiYWRtaW4iCn0=.
```

利用此token构建新的数据包并发送，返回的数据中得到flag数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIrjkzTBZfwA1YrpVvcmvr9icHCR0LUcH0bForUiar2XM0H1eXUh9xUFyR3kGSS1BTf9yLj0g8icic1OEL3YE8sVibHAuOZGSOh6dDYU/640?wx_fmt=png)

上传flag数据完成靶场实战练习

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIotNRzaPA1UN88jLfNDOJiaPA1RnN7Nf8X2ib2YOEhCG6Z72yWiaz0cGQjYWFXfKWrckFia1DvkatFeoYsPzYtGOpw4OgfVRK4Mf3w/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/csuE9m26HkI8taS28gIOWsc8KaibxmZ9HDovmlvGsicEnJuSw0Ricdq3KibbTUnRicEO0NohDyczWdgJBOe3RWF1tQw/0?wx_fmt=png)

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