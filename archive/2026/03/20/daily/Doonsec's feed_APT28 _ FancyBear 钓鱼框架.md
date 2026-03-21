---
title: APT28 / FancyBear 钓鱼框架
url: https://mp.weixin.qq.com/s/cyeSpKHd8bTe67szvn6X0g
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:01:19.987940
---

# APT28 / FancyBear 钓鱼框架

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HMUcG7ibOr114yibDxEAlSG984OXiccYOLZ2I97n4C2l2vFnbMstjcsvgsu1AssDfvicVORnPtazlWMzicUIdvQnDYA2K9pUAB4ezc/0?wx_fmt=jpeg)

# APT28 / FancyBear 钓鱼框架

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

此目录包含来自暴露的作战服务器 (203.161.50[.]145:8889) 的网络钓鱼和 C2 框架副本。仅供研究和文档记录之用。

**1. 如何运行它**

**要求**

* Python 3
* Flask、flask-cors、pycryptodome（用于/解密 Firefox 凭据并写入 loot.txt 的 POST 路由）

```
pip install flask flask-cors pycryptodome
```

**启动服务器**

```
cd phishing_frameworkpython server.py
```

* 监听0.0.0.0:5000（所有接口）。
* 默认索引（/）提供roundcube.html并记录每次访问taker/visit.csv。

**2. 网络钓鱼流程的运作方式**

```
┌─────────────────────────────────────────────────────────────────────────┐│  VICTIM                                                                  │└─────────────────────────────────────────────────────────────────────────┘        │        │  1. GET /        ▼┌─────────────────────────────────────────────────────────────────────────┐│  server.py  index()                                                      ││  • log_visit() → appends to taker/visit.csv (IP, User-Agent, date)       ││  • returns roundcube.html (fake Roundcube login page)                    │└─────────────────────────────────────────────────────────────────────────┘        │        │  2. User submits username + password        │     POST /authentification.php  (_user, _pass)        ▼┌─────────────────────────────────────────────────────────────────────────┐│  server.py  handle_authentification()                                    ││  • If not duplicate: append to taker/creds.csv                         ││  • Redirect → https://zhblz.com/Adob_Scan_15_ian._2025.pdf              │└─────────────────────────────────────────────────────────────────────────┘
```

* 钓鱼页面：（ roundcube.html默认，~847 KB，内联资源）和logon.html（西班牙语，需要rb\_files/）。
* 表单操作：（ authentification.php由 Flask 处理；没有真正的 PHP）。
* 登录后：重定向到 C2 域上的诱饵 PDF（在生产环境中，PDF 位于 zhblz.com；包含本地副本Adob\_Scan\_15\_ian.\_2025.pdf：）。

**项目地址：**

https://github.com/ctrlaltint3l/intelligence/tree/main/FancyBear/roundish

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HesB98icX66NX2ySlGmJuYnMuaR9VelgpP8dNke5RmrQiaEQ8lGcq5230VJeTEQGOdtSzvTMiaYCZHKtNwMKe4jSf9GmlH0B3MTk/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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