---
title: 普通用户注册即可投毒！某高校虚拟仿真平台爆出存储 XSS 漏洞
url: https://mp.weixin.qq.com/s/pksvtje37mzLwReiLHbwzw
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:51:11.205682
---

# 普通用户注册即可投毒！某高校虚拟仿真平台爆出存储 XSS 漏洞

# 普通用户注册即可投毒！某高校虚拟仿真平台爆出存储 XSS 漏洞

三垣网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

READING

**一、前言**

本报告针对 XX 大学虚拟仿真实验教学共享平台存在的存储型 XSS 安全漏洞开展复现与分析。该平台面向校内教学业务，支持通知公告编辑发布功能，由于平台对上传的 PDF 文件以及富文本超链接功能缺少安全过滤校验，攻击者可注册普通用户账号后，在通知公告模块上传携带恶意 XSS 脚本的 PDF 文件，将恶意链接嵌入公告正文。当其他用户访问已发布的公告并点击该恶意超链接时，即可触发跨站脚本攻击，攻击者能够窃取访问用户会话 Cookie，冒充用户身份执行操作，对平台所有访问用户造成信息泄露风险，因此该漏洞评级为中危。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGKMPKa3ia0j47Tj9057FJy7CxpE3NNLxbY9WhicbmQTwQKkmKbFR2aS6EkPdh0Vwa0atZ5c5jib6lFIibInKPmT4dCK4vCuTXsjQPk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLamUJlc85bIXN1kbQBjYtBfS0FrnnFPWytjicSVbgC5v2GYibXicGkswR75E0o06CwjWwBs0j7zapQziaiciclBKf8ibiaBUzxsQ3ae9g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGJDiaF8JHPvFjLUsyUfydDO5C4p63m1aHIRl7ncrxkC1aiaicrIFJC41k61YJsSuOh4SJ8wyyMb5xwR0e8tbk2xp0DHYZlHPkCoeo/640?wx_fmt=png&from=appmsg)

READING

**二、基本信息与资产证明**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGIJFaAJWPDVT29FAsnPv8wBl3OGF9lYVPibNJxDEWFAFL2ZNLLXiaMnwxm5icUsY4icaCK3slQVHdIFbTLQPrgO4jZuZAo5ngU3pBQ/640?wx_fmt=png&from=appmsg)

资产证明：

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGLhBo3YejicKNkPES65YIXVo10AAVqZOibwQBUicibPmVbZlgxslc4c1zHjic43icMfT5qU2qSPciccXQ0GclbTdQe7t7V6nl7Z8a66a0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SxoDJcKqQGJOnDN8lkjy5kIdlIhSVHjVrQdo7YPLXjKlcr8oYju7TxKA05sh1gVR0NugRDJJxZG8FnGJuOswQlj6I5trJH0I2mLKelBkmzQ/640?wx_fmt=jpeg&from=appmsg)

READING

**三、漏洞复现**

1、进行任意用户登录进入后台

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SxoDJcKqQGKkmAUWImibAdKkwiaGnGZv5NdZ9wcvw6YJ1tnbtpwyjh0LoXichd1ibJ0wFPdSic915VMbP5m5oKQnU2q3doFLqbTGGicCAVUNSSqkE/640?wx_fmt=jpeg&from=appmsg)

2、通知管理处可以进行添加

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SxoDJcKqQGJOltHFE3B96pmDfZzzpticcJW8aJtO4JOld1MMEkQXAegvmmeHicL2ZC4Q8USSY7DicAZBzG6iblKMQpibw2AzJ7Ww3Qob6FxyMlHM/640?wx_fmt=jpeg&from=appmsg)

3、此处编辑器可以上传链接，并且可以直接而上传pdf文件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SxoDJcKqQGIQZ91z3PlQa3I6EUFUjFjsnx8gBE94ibZXBrKeWiazrYcXZxIVRB9DeuWoJibDlEk94orCdzdk08QqSqvevhmiaFpfwySIermicGjs/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGJJicsvL8tljnpNhgU8XE3EgoycicDCSic8xrMlLfjiazzz1siaD9sH2ArG7SFzrIzP1omATwFhJKJia5XpWej3AVRXRbTMiapYWGYMzw/640?wx_fmt=png&from=appmsg)

4、我们上传一个带有xss的pdf文件，访问超链接成功弹窗，此公告发送到主页被用户大量访问会获取大量cookie，造成巨大影响

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGJIUCtrmibjMxjALewh362DWwwdVl38Xs8ljS6jBNvIvyHUun4CgmNkpoOat2fsv3sdSXVuaK08hGGwlviaPT0jrbvGlrOUjjFPw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGJmgAsoRMttdWichY9YqJibYiauA0icYQKvh48spiaxQso5kLchZ9w2RrvxkMoRzx9yRynCkBu5UYaE0Jb7AuSdic3A2FAThGgwKkNn4/640?wx_fmt=jpeg&from=appmsg)

READING

**四、结语**

将携带 XSS 恶意脚本的 PDF 文件通过编辑器上传到服务器，把上传得到的文件访问路径配置为通知正文的超链接，保存并发布这条通知公告。当其他普通用户访问平台主页、浏览这条公告，点击公告内的超链接访问恶意 PDF 文件时，页面会成功触发 XSS 弹窗。一旦漏洞被恶意利用，公告对外公开被大量用户访问，攻击者就可以批量获取访问用户的 Cookie 会话凭证，冒充受害者账号在系统内执行操作，会带来大规模的会话劫持、信息泄露风险。

关注三垣网安，学习更多网安技术 ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/SxoDJcKqQGKgq9IANYMTibeCmCAqZIVoGI0O0F3uWQ61HD2qU76xG80X1Dkgyy46h4thVXZub7exwxDia2k1QU9qnES3rI0gQZcWkA15iao6CQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGIYczgthjGhNq9wILEObYeVxeJIPEwWvoUgibbmlDrboxxqY0qBcXpwOjgDO6zCCFrRoibRZ6etdzAialS0ZRA0efzDGv9ufPSARA/640?wx_fmt=png&from=appmsg)

#XSS #存储型XSS #渗透测试 #PDF文件上传

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