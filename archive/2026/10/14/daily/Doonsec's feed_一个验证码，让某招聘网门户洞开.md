---
title: 一个验证码，让某招聘网门户洞开
url: https://mp.weixin.qq.com/s/doJL1cCH7t_2G8yz8MSxVQ
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:43:03.390878
---

# 一个验证码，让某招聘网门户洞开

# 一个验证码，让某招聘网门户洞开

原创

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

在一次攻防项目的暴露面资产排查中，发现xx网存在验证码回显和任意用户注册漏洞。测试时在注册页面填写信息并抓包，发现 HTTP 响应体中直接返回了邮箱验证码，攻击者可利用回显的验证码完成任意用户注册。

这条利用链的门槛低到什么程度？不需要任何账号、不需要任何前置权限，一个普通邮箱加上一个抓包工具，就能完整走通"获取验证码→注册账号→登录系统"的全流程。下面完整还原利用过程，每一步都附真实报文与截图（域名、证件号、邮箱等信息均已脱敏），仅供授权测试与安全学习参考。

本次渗透测试总计发现高危漏洞2个，漏洞情况如下表：

| 序号 | 系统名称 | 漏洞名称 | 漏洞数量 | 漏洞影响 | 漏洞级别 |
| --- | --- | --- | --- | --- | --- |
| 1 | https://xx.xx.xx.xx/api/zpfw/website/sendVerificationCode | 验证码回显 | 1 | 验证码明文回显在响应体中，无需访问邮箱即可获取有效验证码，邮箱归属校验失效 | 高危 |
| 2 | https://xx.xx.xx.xx/api/zpfw/website/sendVerificationCode | 任意用户注册 | 1 | 注册身份未做真实性校验、邮箱未校验有效性，可批量注册账号并正常登录系统 | 高危 |

1  验证码回显

漏洞描述

用户在注册页面填写姓名、证件号码、邮箱等信息后点击"获取验证码"，系统在向邮箱下发验证码的同时，也把验证码明文回显在了 HTTP 响应体的 data.message 字段中。

响应体中返回的验证码与邮箱实际收到的验证码完全一致，攻击者只需抓取一次数据包，即可在不访问邮箱的情况下拿到有效验证码，邮箱归属校验被完全绕过。

漏洞地址

POST  https://xx.xx.xx.xx/api/zpfw/website/sendVerificationCode

漏洞详情

访问系统首页 https://xx.xx.xx.xx/#/index，点击右上角的"注册"按钮进入注册页面。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gr70icGJeeMibF3Z42kfYtlkpPQibJCFr9fEvP5Idib0e0ekRLNicSHpjnE45ZxvyvlkehguGhrqfLCAoIDxKzaz81ON87icl3mhjfuU/640?wx_fmt=png)

图1  系统首页：右上角提供"注册"入口

注册页面要求填写姓名、证件号码、邮箱、验证码、密码等信息，其中验证码通过"获取验证码"按钮下发到邮箱。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gp1XeichMyswuzmfh6uUZZPjUjhBGiaLSVDCCysUYYOLEDAOdJOia9Gw2Es96ribyILN1eZGt56xgEzpib1tomgTdGNtfEfP1SPd2Gg/640?wx_fmt=png)

图2  注册页面：姓名、证件号码、邮箱、验证码、密码与确认密码

随意填写姓名与证件号码，配合一个真实可用的邮箱地址，点击"获取验证码"，同时在 Burp Suite 中抓取数据包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gq0DSqxkXJNmMsa17n5oP5adw7WmefRu6RFYE3Iicb7UFmOpeE0ouia0EoXAGbA8wIGticcciaZUYTFnJsOJZtOrMNX11ibr72iaoyibk/640?wx_fmt=png)

图3  抓取获取验证码请求：POST /api/zpfw/website/sendVerificationCode，请求参数为邮箱

请求包：

POST /api/zpfw/website/sendVerificationCode HTTP/1.1

Host: xx.xx.xx.xx

Content-Type: application/json;charset=UTF-8

Accept: application/json

X-Requested-With: XMLHttpRequest

Content-Length: 41

{"email":"134\*\*\*\*\*\*\*1@139.com","locale":"zh-CN"}

响应包：

HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

Server: rum/rd

X-Frame-Options: SAMEORIGIN

X-Content-Type-Options: nosniff

{

  "meta": {"success": true, "statusCode": 200, "message": "ok"},

  "data": {"flag": true, "message": "6306"}

}

可以看到，响应体中的 data.message 字段直接返回了验证码 6306，与邮箱实际收到的验证码完全一致。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqIbCdY6YszoJ1ib3wDk60WYCib5kmzL4yaVxULBc2sAs71XYZUtRBiblJLIWBSR6UTt3Pic9scCx7vV3JVh3lHaH4rLzaBxBMMAXU/640?wx_fmt=png)

图4  邮箱收到的验证码：与响应包中回显的 6306 完全一致

2  任意用户注册

漏洞描述

注册流程未对注册身份做任何真实性校验：姓名与证件号码可以随意填写，二者之间没有绑定校验，邮箱也不校验有效性。再结合验证码回显漏洞，攻击者可以注册任意账号并正常登录系统。

漏洞地址

POST  https://xx.xx.xx.xx/api/zpfw/website/sendVerificationCode

漏洞详情

进入注册页面 https://xx.xx.xx.xx/#/register，注册表单要求填写姓名、证件号码、邮箱、验证码、密码与确认密码。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gruibRg9HWxwwnv1fsIM1eV1ib5CPdP3tibv1xx3U0JjkSgQib4YdPHazibjz9cdz4sHE7CXcunIgu82thnmchO9IFYFcVc9cF3vMcE/640?wx_fmt=png)

图5  注册页面：姓名、证件号码、邮箱、验证码、密码与确认密码

随意填写不存在的姓名与证件号码，并填入一个无效邮箱 1234@139.com，点击"获取验证码"，系统仍提示"系统已成功发送一封带有验证码的邮件"，说明服务端并未校验邮箱的真实有效性，依然下发验证码。同时在 Burp 中抓取注册数据包。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqQHqVdyxuEichFSOskiasL1Cw8oGJwgjC9SCy2U3Xo4lpHVqVroUV3LYbImtRUnuuWo36zASLAGB1KTGt4vF2eeBwPWOWHMDvicU/640?wx_fmt=png)

图6  抓取注册数据包：姓名、证件号、邮箱均未经验证，响应体中直接返回验证码 8857

响应包：

HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

{

  "meta": {"success": true, "statusCode": 200, "message": "ok"},

  "data": {"flag": true, "message": "8857"}

}

使用响应包中获取的验证码 8857 提交注册，页面提示"注册成功"，系统提示 5 秒后自动跳转到登录页。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpeNibnkzxn6tZ4o8tDFriawrRrliaibu6ibC7MAzgTYoDVjzBqN8q1L1wgmaKicZkcd2r4sMIiaxcC1kd6ibByMyOUP40nmIqavM3DVUM/640?wx_fmt=png)

图7  提交注册：使用回显验证码 8857 完成注册，提示"注册成功"

使用刚注册的邮箱与密码登录系统 https://xx.xx.xx.xx/#/login。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gptbCfVDa5DtcUL5MK2a2ibwZEDQo7R2kawA5icWcVUXia0yu8T3X9yZfLM9la5Nxd8zY5BTX977Hk69icd4yPQSiaLIflh66z7mJvI/640?wx_fmt=png)

图8  登录页面：使用注册的邮箱与密码登录

登录成功，页面右上角显示注册时填写的用户名，导航栏出现"个人中心"入口，证明该账号真实可用。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpo7YLeW3H4pr5bwMLhFWqJsVutktVTvWricFl6hDgbJ0iafO5bL19f5pNuRL7YNUQhOzokyPJtYMWK7FChToekPbMwangRrYRQc/640?wx_fmt=png)

图9  登录成功：右上角显示注册的用户名，导航栏新增"个人中心"

进入"个人中心—个人资料"，可正常查看与编辑个人信息，任意用户注册漏洞成立。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1go8b4jnkcfLOjNZqEN0JQvg4mbx8uP0qmibO1GfHVMsW7b3RZHhAxUjhuNOebcOqKW6LbedWw9Y5cOuzFvCiaoM1TkfR62HtBPlw/640?wx_fmt=png)

图10  个人资料页面：注册账号可正常访问个人中心并查看个人信息

3 总结

回顾整条利用链：两个漏洞本质上是同一问题的两面——注册接口把验证码明文回显在响应包中，注册流程又缺少身份真实性校验。两者叠加，攻击者用任意姓名、任意证件号、一个不存在的邮箱，就能完成从获取验证码到注册登录的全过程。

修复上建议按"先止血、再加固"的顺序推进：第一步先去掉响应体中的验证码，改动最小、见效最快；第二步补上姓名与证件号码的实名核验、邮箱有效性校验；第三步对全站验证码类接口做统一排查与频率限制。三步做完，这条利用链才算真正切断。

写在最后：本文所有测试均在授权项目范围内进行，涉及的域名、路径、证件号码、邮箱等信息均已脱敏处理；内容仅供安全研究与技术学习交流，请勿用于任何未授权的测试行为。

免责声明：本文仅用于网络安全技术研究与学习交流，严禁将文中技术用于任何非法用途。任何未经授权的测试行为均属违法，由此产生的一切后果由行为人自行承担。

预览时标签不可点

修改于

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HezRQjNneVHy39103FjCvxFaZicO2OgEB05ZbBLwibDiaCTqDJNUHUCC9OXjVeiasG4ibOVR0dg284RCzVquVhvQ3xQ/0?wx_fmt=png)

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