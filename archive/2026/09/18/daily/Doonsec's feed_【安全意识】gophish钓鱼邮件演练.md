---
title: 【安全意识】gophish钓鱼邮件演练
url: https://mp.weixin.qq.com/s/Mfnvb8fGNp00is6E4wdACA
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:57:23.816652
---

# 【安全意识】gophish钓鱼邮件演练

# 【安全意识】gophish钓鱼邮件演练

alex
alex

安全驾驶舱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**背景**

gophish是一个‌开源的钓鱼模拟与安全意识培训工具‌，用Go语言编写，主要帮安全团队在授权范围内模拟钓鱼攻击，测试员工对钓鱼邮件的防范能力。‌‌

简单理解，它就是一个“钓鱼邮件工厂”，能自动化完成从邮件制作、发送到数据收集的全流程。 你可以用它创建逼真的钓鱼邮件模板、搭建仿冒的登录页面，然后向目标人群发送测试邮件，并实时追踪：‌‌谁打开了邮件、谁点击了链接、谁在仿冒页面上提交了账号密码。

****1、工具配置****

**1.1、配置发件箱**

运行gophish程序后，在浏览器中输入https://xx.xx.xx.xx:3333，登录到管理后台，在”sending Profile”中配置发件箱信息，主要包括：发件邮箱账号、发件邮箱服务器、邮箱密码。

![图片1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdpoaSaS9WlTFFicib8eMhhtmXu9PYONYfFSuKoVfNENZjT6S11xJkKCHbPeHLSg554axyl8GlbypiaRlRZbv1OCZO88AtqA4wX4hib8/640?wx_fmt=png&from=appmsg)

****使用建议：****

默认情况下，gophish发送钓鱼邮件时，会在邮箱头部添加X-Mailer=gophish，因此为了屏蔽原始特征，需要在这里添加自定义头部，例如以下：

X-Mailer=Microsoft Outlook 16.0 (Windows NT 10.0; Win64; x64)

X-Mailer = Apple Mail (2.3696.1265)

X-Mailer=Coremail Webmail Server XT 5.0

**1.2、配置收件箱群组**

在”Users & Groups”中配置收件人清单，即哪些人会收到钓鱼邮件。此处可以填写收件人的First Name、Last Name、Email、Position。 Email字段是必填的，其他字段可不填写。完整填写收件人的First Name、Last Name、Email、Position可以在后续钓鱼邮件模版中以变量的方式替换邮件正文，让钓鱼邮件变得更加逼真。

![图片2.png](https://mmbiz.qpic.cn/mmbiz_png/ySlic3yZpdpoJZ54vAjI1wCM7Fcpuk835tCYy6kU5DiaZ6tF4eEsSoN1DESMUqiaMZWfkL5ib8YA46OaT8q2fjOuO83Upn7SHCT6YLniaHFW8WI0/640?wx_fmt=png&from=appmsg)

****使用建议：****

1、如果钓鱼邮件收件人太多，可梳理好收件人的姓名、职位、邮箱地址，可以通过CSV文件进行导入。

**1.3、创建钓鱼邮件**

在”Email Teamplate”中创建钓鱼邮件内容，有Text和HTML两种编辑模式。Text是纯文本模式，不能设置超链接。HTML模式，可以输入完成的html表单，可以设置显示样式、超链接等。点击HTML模式下的Source按钮，可以在编辑器中预览完整的html文件显示UI界面。

![图片3.png](https://mmbiz.qpic.cn/mmbiz_png/ySlic3yZpdpr0rBN3uKm7sydjSSJAswwB1ibFkTLpBfI6Yy7IZCTnHRibs6rSGUCgUQhxfMIiaU2s2A0q29hPueerKKj77iaoKNsoMnd4vTLN83I/640?wx_fmt=png&from=appmsg)

****使用建议：****

1、使用HTML模式创建钓鱼邮件，更具有迷惑性。在页面链接中，可以创建类似

<a href="{{.URL}}" >https://oa.xx.com/</a>的链接，邮件显示时是一个链接，实际点击后是另一个链接。{{.URL}}会被替换为后续的钓鱼页面地址。

2、勾选Add Tracking Image 会在钓鱼邮件中添加<p>{{.Tracker}}</p>，{{.Tracker}}在邮件发送时，会被自动替换为http://xx/tracking?rid=xx的链接。当用户打开钓鱼邮件，会向服务端发送此请求，服务端收到此请求后，感知到钓鱼邮件被打开。

3、在钓鱼邮件中可以使用的其他变量：

{{.RId}}  : 钓鱼对象的唯一id标识符

{{.FirstName}}  ： 钓鱼对象的名字

{{.LastName}}  ： 钓鱼对象的姓

{{.Position}}    ： 钓鱼对象的职位

{{.Email}}      ： 钓鱼对象的邮件地址

{{.From}}      ：  冒充邮件的发送人

{{.BaseURL}}   ：  钓鱼页面的假冒地址

**1.4、创建钓鱼页面**

用户点击钓鱼邮件中的链接后，跳转到此处的Landing Page。在”Landing Page”中可以从目标站点拷贝HTML响应内容，也可以以HTML源码方式创建钓鱼页面。如过HTML中存在form表单，可以捕获用户在表单中输入的用户名和密码字段。在用户输入用户名和密码后，跳转到真实的业务站点。此伪造页面，会保存在gophish数据库中。

![图片4.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdpqPxqCibxdlpSSLkMxbdQ2NIgucVwsyHrWrJicsdwv5w7j6MKv6Jjh1K2eiakCicf1AiaKnicL4NvMNRqKZ9qHKVolDrmv1GoUK90vnY/640?wx_fmt=png&from=appmsg)

****使用建议：****

1、从远程站点拷贝HTML结构时，如果目标页面HTML页面渲染基于多个js和css文件进行渲染，会存在拉取HTML页面后，无法完整显示的结果。

2、输入HTML文档后，如果存在form表单，表单中的提交地址设置为空，例如<form method="POST" action="">。

****2、启动钓鱼演练****

**2.1、创建钓鱼活动**

当配置好发件邮箱账号、收件邮箱账号、钓鱼邮件、钓鱼页面后，就可以开始发送钓鱼邮件了。在Campaigns中可以发起钓鱼活动，主要字段解释如下：

Name: 钓鱼活动名称，取一个具有识别度的名称

Email Template: 选择哪一个钓鱼邮件发送给用户

Landing Page: 用户点击钓鱼邮件中的链接后，跳转到哪一个伪造页面。

URL：此处的地址，会替换在钓鱼邮件中的{{.URL}}变量，如果是钓鱼演练，通常是http://xx.xx.xx.xx:81，这是gophish服务端的监听地址。

Sending Profile：选择用哪个发件账号发送钓鱼邮件

Group: 接收钓鱼邮件群组，哪些人会接收到钓鱼邮件

![图片5.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdprOoKCSImM2hib9C832HLrQr9e2mA0Tbtch9KkkOqC6DAXaJg93BoYSAbdibHPQr2fcy7icDRWYwvmOlldguj1Pzv8ubwBwnTUiclY/640?wx_fmt=png&from=appmsg)

用户点击钓鱼邮件中的链接后，跳转到以下伪造登录界面，访问地址格式：http://xx.xx.xx.xx:81/?rid={rid}

![图片6.png](https://mmbiz.qpic.cn/mmbiz_png/ySlic3yZpdpo0aJohu4XPpl3WdCjfiasES9cPsrqWVUpfUmU3hVmBcyodrQVbzd8LzMVqAUs0wRjUzicOov7WlvdX81niaa3tE5RgcyicU0330B8/640?wx_fmt=png&from=appmsg)

用户如果在页面上输入登录账号、密码字段，gophish此时会记录下来。

**2.2、查看钓鱼结果**

在DashBoard中可以看到整体的钓鱼活动情况，以及具体某个用户钓鱼钓鱼邮件，进入钓鱼页面，可以看到针对具体钓鱼对象：发送钓鱼邮件时间、钓鱼对象打开钓鱼邮件的时间、钓鱼对象点击恶意链接时间、钓鱼对象提交敏感信息时间、以及在钓鱼页面上输入的凭证信息：

![图片7.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdprmJ8NkicbUx1rK7eKvHicRah7C7DmBnvvwiaAfE8r8ewpdbx0ONzibzHL4Siaz3GV6TibLxAussdFZJotRYkyItFt1gBLHFVgnue7Go/640?wx_fmt=png&from=appmsg)

****三、gophish钓鱼邮件回顾****

gophish提供了良好的UI界面，提供了进行钓鱼演练活动的所需具备的各项功能。管理后台把流程拆成模板、页面、用户、活动等模块，Dashboard实时显示打开、点击、提交数据，结果一目了然。

****四、参考链接****

https://docs.getgophish.com/user-guide/template-reference

https://docs.getgophish.com/api-documentation

**END**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/nk59nEwEn2NFnIQWR9r20fFe5ddkKn1TSDia5lldroxlJic8XwVGY0dVvav9u3ib4031B8XbtG3ra0vsvIqudZEDg/0?wx_fmt=png)

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