---
title: 谁懂！扫到 /plug 路径，直接命中 SQL 注入
url: https://mp.weixin.qq.com/s/eIiBt6gxyzuzrFHmHgPU7A
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:57:17.405649
---

# 谁懂！扫到 /plug 路径，直接命中 SQL 注入

# 谁懂！扫到 /plug 路径，直接命中 SQL 注入

三垣网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**前言**

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGK2KTDgV8KMlTC1zxAbtVs8kJRMtTictiaibqpxNMpJtic3OwfIyHcOHGsuITzCm0XpFWzODLST5ntpm5MGFZT03LMNlrKjdzDbF2w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGKe1YibnLIDGdyxibeNuEW0Su3o8Yib9EmAyC3icictVebS4cbaCHCuJsIPTic5PfZsECeyYicLq4KLcWxy7RSP0k4mMibqArBicyh1XU0I/640?wx_fmt=png&from=appmsg)

在一次常规渗透测试的目录扫描环节中，扫描器探测到了/plug插件相关路径。本以为只是普通的静态资源目录，深入探测接口后，却在plug\_comExt\_sqICallPro1.do接口处发现存在 SQL 注入漏洞。

很多业务系统的插件模块往往容易被开发忽略，缺少严格的输入过滤与参数校验，成为极易被忽视的高危突破口。本文就从路径发现、漏洞探测到漏洞验证完整记录本次挖掘过程，仅做安全技术研究学习，请勿用于未授权测试。

**1.漏洞的基本信息**

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGL5ABf9hD4p4Dt6334AyhCGv4A28WXTHyVsrGXJ8cGsKNZgwXibCJT3qR0WLNKyCql8TYibyLpicg725qWuY0bR5qCoOZv9dgY2RY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGKicibnt8hicpZun41ohGKnL8ROmQforgNyBnCDhibFPiaiapcxU0LqmlK6KeQialwkN5VlRatGM1pKyZsxBUwUaXXRibV7IXPicib8FiafFA/640?wx_fmt=png&from=appmsg)

危害：高危

类型：sql注入

**2.漏洞思路**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGKibdiczHDOtk0H58TVicPEHksaqibxGnrBxjR2ASKTDADJSY0iahW1QO790zJfk2ZPSjTQAJGLnVcrqM22L8icQushV1D1a9jawAiceQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGI5ZPupMGDjeiclzeyDck21TicnDFMc4cEPovKoIwPxSyY732Kuv0MHriaowbhicCndb2bQIrUIg0L3vycaLJUcMrjruqicG3EhibSFs/640?wx_fmt=png&from=appmsg)

1. 漏洞url：

https://xxxxx.edu.cn/plug/plug\_comExt\_sqlCallPro1.do

是一个心理教育平台

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGIINWVhqhvwWvPXCIxxxFYfdlbVNqWFvzVy6hEVtVKWcW0zCOHdLSiaOswEVaiaEyAWGictgbAKgfQttb9CzUMYkKEutbNJhXoYmc/640?wx_fmt=jpeg&from=appmsg)

2.他的账号为学号，密码为A+学号，学号可以通过

国家助学金名单获得

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SxoDJcKqQGI95zCNXic8stQ8w9A1mgLoKX18YxKibyX9vBQT7RFs8lXhYzvPiarZibSflC0VKRYhIqibX3txsvtLibibEHqgiarYNqAZKTbgdEib4FaU/640?wx_fmt=jpeg&from=appmsg)

3.进入后台，进入/plug/plug\_comExt\_sqICallPro1.do接口，抓包

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SxoDJcKqQGLKG0wonXryd0lLonl5rVKddflIqSexsbS7VTI5iaB2fTGiagMuu7icgkp7ZHZA9U4d8anjEEfcJuICviaHRtwYSu6D7G3S7iblanPg/640?wx_fmt=jpeg&from=appmsg)

4.构造payload，得到数据库名

1)=(extractvalue(1,concat(0x7e,(database()),0x7e)))=(1

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGIIkOeBIKn1D8k8mPWWpTVbBebMHZBeHkaFJmANBjZsDgmvpTLVyc0a1A2cES7l0URTH8aInlFplhtaWjksZ1RicyT1swNNZUXs/640?wx_fmt=png&from=appmsg)

**点击关注三垣网安,了解更多网安知识**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGKvYKvquXkZE4EiaFwe3ibW72C1wSQTeqeiaZiaL1XNxjlrz9UVVt41UCIMCj57Md71T1sWJWbVg1LiacJqTYkrTUcqKiaIWBicnvw8Vs/640?wx_fmt=png&from=appmsg)

#sql注入 #渗透测试 #实战案例

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJaWOwicn7raXm5k4xXDlBia0Okyg0R9d4niakArWeAcFZe0mbIWPKXdgcJHv0mIY6picqR7UB0GmPPeMC70E9VFWMXDEdYOj8GS3o/0?wx_fmt=png)

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