---
title: 从隐藏接口的 JWT 绕过到 AWS S3 任意文件覆盖
url: https://mp.weixin.qq.com/s/HoSz-HQJR3O1j8ajxhLBXw
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:06:01.921569
---

# 从隐藏接口的 JWT 绕过到 AWS S3 任意文件覆盖

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibyeI8ib1jTWReQ3HABsyt9qYzDr5sg0tQfS0icv9khFviasXsfpT7FFSTYl0pdyfnpTjXKhAN6ZnNwYibdaRnQFsAFjEmOGAh3JkVA/0?wx_fmt=jpeg)

# 从隐藏接口的 JWT 绕过到 AWS S3 任意文件覆盖

原创

Pwn1
Pwn1

漏洞集萃

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **免责声明**
> 本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。

在测试一个私有漏洞赏金计划时，我遇到了一个

## 漏洞场景

漏洞基于 JWT做身份验证的业务系统中。主要牵扯到两个核心场景：一个是主站负责正常用户登录认证的 API 接口；另一个是暴露在子域名下、隐藏在前端 JS 代码里的后台文件上传端点 `/upload`。

## 原本功能流程

在正常的业务逻辑里，用户在主站登录之后，后端服务会签发一个包含特定作用域（`realm`）和用户权限的 JWT 给到客户端。

按道理来讲，如果要去访问 `admin.test.com` 这种后台系统，或者调用后台特有的 API 端点，服务器会在中间件层面严格校验两件事：一是这个 Token 里的作用域对不对，二是请求头里的格式必须是标准的 `Authorization: Bearer <JWT>`。

只有合法且拥有后台作用域的请求，才能通过校验，把文件上传到后端的 AWS S3 存储桶，最后由 CloudFront CDN 进行分发显示。

## 漏洞的发现过程

这个洞的挖掘过程核心就是抓细节和不断的 Fuzzing，思路可以拆解成下面这几步：

测试时，在 `admin.test.com` 加载的 `app.js`中，发现系统硬编码了一系列 JWT 的作用域列表，其中有一个看起来就非常敏感的 `test-dashboard`。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jow1el0IZibzNWWzVz9C9iaSYIfVmPZw8JZCL85fDwUxBgwBD23DyEMX6pakDnb1mm9yBcQJo3hOicoqzp1Kib8DibMLojMqaYJHchSXViaick0YFU/640?wx_fmt=jpeg&from=appmsg)

回头去抓主站正常的登录接口 `POST /api/v1/login`，尝试在提交的 JSON 数据里硬塞一个参数：`"realm":"test-dashboard"`。神奇的事情发生了，服务器照单全收，直接签发了一个带有后台管理作用域的 Token。拿着这个 Token，直接进到了后台 UI 界面。但是这就完了吗？并没有，因为虽然页面看得到，但尝试操作具体功能时，底层的 API 还是会报错拦截，也就是属于中危级别的 UI 绕过。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibyQQcQevhUf94TrVDzhia6x3ibpCRhHrSZH1BEm3CnKBDQ7fbvG8BibESjvPrnh94iaSetGJyoIRhLmiaykAh9vGu1FUWglBOeYPxaM/640?wx_fmt=png&from=appmsg)

既然有 UI 权限但缺 API 权限，那就得找薄弱的 API 下手。常规的 GET 请求没探出什么东西，直接转用 POST 方法对后台子域名进行目录 Fuzzing，结果探出了一个返回 `403 Forbidden` 的接口：`/upload`。这个端点在前面的 `app.js` 里也出现过。

根据 JS 文件里的逻辑，拼凑出了一个标准的文件上传数据包，带上前面拿到的 Token 格式为 `Authorization: Bearer <JWT>`，发过去之后返回了 `401 Unauthorized`。

这时候只能对 HTTP 头进行各种变异和 Fuzzing。

测试发现了一个逻辑漏洞：只要把请求头里的 `Bearer` 这几个字符删掉，仅仅保留 `Authorization: <JWT>` 发送过去，服务器端负责鉴权的逻辑竟然直接瘫痪了！接口响应 `200 OK`，文件上传成功！

![](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibwVbJBtbfm9fyajJYyDTQ5qLox4lqGqqctic3K84LIFNk2EbdUUQPwTYeIx6Q5WCX1WUiazojmKqFpaAIvALcBdz5DlTZMhGEykk/640?wx_fmt=jpeg&from=appmsg)

文件是传上去了，但接口没返回文件存在哪儿。这时候回看 Burp Suite 的历史流量，发现在别的页面响应里，经常出现类似 `https://xxxxxxxx.cloudfront.net/gallery/xxxxx` 这样的 CDN 链接。这里的 `gallery` 刚好和上传数据包里 `destination` 这个参数的值一模一样！顺藤摸瓜拼接出刚刚上传的文件名 `poc.txt` 并访问，成功在云端看到了上传的内容。

![](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibwTpPuAPc8Bj1nTEr20N3trca3LgzlzwUAJhGUntYBr7ibibwxnx6Arbc0gz9nHkrlKoX5PhSlMuBqNxSvKZymN6viaMjajQzuysA/640?wx_fmt=jpeg&from=appmsg)

如果是单纯传个无关痛痒的 txt，其实危害也就那样。

但是这里托管的云服务是 AWS S3，经过测试发现它存在配置缺陷：上传文件时，如果 `destination` 目录和 `filename` 和线上已有的文件同名，系统不会拒绝也不会重命名，而是直接覆盖掉原有文件！

![](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibyx3UPTiaQAOicQC0DO3GBrHZyvWmkE1ta7G3bkkFAFUpBUPE8XJCatTc0c7ib4m9DLl59gXQ3eNnzzBwn8JESQyKmqEiceEpInZzE/640?wx_fmt=jpeg&from=appmsg)

而且，主站的各种核心 JS 文件、HTML，甚至提供给用户下载的 Windows 安装包（EXE）和 PDF 文档，全都在这个 CDN 域名下托管着。只要利用这个上传包指明目标路径，就能把线上的正常业务文件全部替换成带有恶意代码的后门文件。

来源:

https://medium.com/@h4x0r\_dz/23000-for-authentication-bypass-file-upload-arbitrary-file-overwrite-2578b730a5f8

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[一种利用 HTTP 重定向循环的新型 SSRF 技术](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484872&idx=1&sn=085b9ed569eefc9a96122fd164da9707&scene=21#wechat_redirect)

[预接管账号：结合 OTP 校验分离与空格绕过注册内部管理员邮箱](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485067&idx=1&sn=766b936ad8c4d5913df74761d4f9e791&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLRgzxswNMosdb4HdiarwSPg43TDHTKMwbX8kaRZ8iajLgxTBVuwFBynCicFAmAvfvapPCydNnZKwgpw/0?wx_fmt=png)

漏洞集萃

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLRgzxswNMosdb4HdiarwSPg43TDHTKMwbX8kaRZ8iajLgxTBVuwFBynCicFAmAvfvapPCydNnZKwgpw/0?wx_fmt=png)

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