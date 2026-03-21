---
title: PHP-SQL注入代码审计
url: https://mp.weixin.qq.com/s/tznzdLoATF90Zae8cAoEDA
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T03:59:13.255293
---

# PHP-SQL注入代码审计

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3CSuJ7WYnWYFWsoffj7IPFZaIibb0DcaRPL6hoalGhkcVS0H2L164V2hM3kAcaYbaSMsAiakAQqnJ0iafH0PLHlrEJdBFZb3Fl8URl1Cj0yDHQ/0?wx_fmt=jpeg)

# PHP-SQL注入代码审计

原创

嵩艺
嵩艺

嵩艺

![]()

在小说阅读器中沉浸阅读

参考视频b站小迪安全和菜狗安全和知名小朋友大佬

免责声明：仅供参考学习，禁止非法活动，如有违法犯罪，概不追究本人责任。

# 挖掘大概思路

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWbTql1cZic90CZ3L9LZwh4IzibZKz2ZxQlxzib5BNPY3Vxb2ETRujQ6qs9NcxQQib4feT9TNuqe0MdiaJsBRP9hR00jwqWyXYARpwZM/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWaRpT00qLJJPMwTcIHsZMX9VoKNK8n4oQwNIk0zVIrpl8zZQkQl41kjiaiaMzfd6wGBkh9FwMPuQmuhE1tjDZEHOp2pG6FcKHBH8/640?wx_fmt=png&from=appmsg)

# 如何快速在多个代码里找到脆弱

1.看文件路径(前台优先看，后台往后看)

2.看代码里面的变量（可控变量）

3.看变量前后的过滤

# 案例（1）--小迪2023--bluecms

## 安装：

1.php版本 5.3.29   数据库 5.1.60

2.bluecms版本 BlueCMS BlueCMS 1.6

## 如何找到突破口

```
https://www.cnvd.org.cn/flaw/show/CNVD-2022-25774
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWb6GPnPaaeMtNd2rg6XSGoichhabgEt9YnS6bhuvDibl2MHvbx3CsJFNwt4yMniaaa0SFwZ9UAtOM0uRgLI5IbI1WCoIc0925Mxfk/640?wx_fmt=png&from=appmsg)

```
(update|select|insert|delete|).*?where.*=
```

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWYooJsMeFU2udjazYzH6gNTZlgbKekmy2Jpn5xObsCx35xRsRFyNianQhcWBVwPJrhwRvMa0juLqTA0I2X3hnoqPZQgSmD3gtpE/640?wx_fmt=png&from=appmsg)

## 源码分析

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWa1yIoDJOEIlkJKsnbBDdIh8W2n6VZj4zb9WHg8icQuPceUfNzbuSdV6T3lPuRZdfDiac78MFrrgA6QTlwCDP7cr6dPUw2aicmmn8/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWYJpKlCNW7euibmwO1DuCiaxb1K20B9OfjicP6YMRaZ4dmyibp4ItXB0Tj1HPgZaqA8FcKHgKAQia2oomOvdsGVZygAniaOHqed8g7ck/640?wx_fmt=png&from=appmsg)

## 漏洞验证

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWZNbSh5FBAyAq6t1c7cRKEIiawyzkp8VpOtz5foTia6sVTygDbvDia9A8zyrLfVL6Tj30nxUJmRawUTia2faaxiaOL7N1km1QXvic8Cw/640?wx_fmt=png&from=appmsg)

##

# 案例（2）--小迪2023php--emlog

## 安装：

1.php版本 5.6.29   数据库 5.1.60

2.bluecms版本emlog 6.0.0

## 如何找到突破口

```
https://www.cnvd.org.cn/flaw/show/CNVD-2018-26200
```

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWZPKvXxtW5AdddwZYtVqSibbpboQJwyNn9TSDY1aHg4WCtLFcJZma5fL4kQ6WMicc05N5jDxhLtTNWpF5pmMShKpBzaicYLQ6DpFA/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWbonpR1CKvPpo7MsIsF9V2pYGJhoOicHBgjeAWtlGOe1LjkxmUI88eURWFbRic0iap9kClYhoI882HZG9LZgh5ibY96rhJmZMn7JlU/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWZQNyqnmRLvSudozkhaIuPChF5mEzY9ZPz6uDeFKO2KNsGFzPca178VS5NK5Rh7EzgBxGUGQXqwEefYgtaFP7oHyjoKzkkvkibY/640?wx_fmt=png&from=appmsg)

## 源码分析

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWbeMdFzI9cQKJQaj35SjYAmCOTiaPSWg2zQRQlOTPkInCU8NSWmXicFgFNtjMM3iblTvPaibqUEpEpk9J9jciap4byhCRfgyXs4awcE/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWbia2sFFgCicCMGe6QIQK3wTAwJbKAwzTadcUMsMARIqhhy7Kg6aEtWx2iab9x9zBzGaTmKHnIdA2EK1Jvmh5YuOlCvEicwzMNs0Cs/640?wx_fmt=png&from=appmsg)

## 漏洞验证

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWbXYlrQs0cf8HLTdcLUn19MdgvLcULAdUUWz9qK2BJYkDREY5tGGuGFj1FzpFAibib3FkqwMR3phY99yw63Ue53se7fwCtPmQRgc/640?wx_fmt=png&from=appmsg)

```
GET /admin/comment.php?action=delbyip&token=9f40e10adf43ac2af3f0098bc769eae4&ip=127.0.0.1%27and(extractvalue(1,concat(0x7e,(select%20user()),0x7e)))%20--+
```

也可以参考 “02安全公众号”

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWYbweOicJLJNLMNT9gvrcE43Ry5XnrPo80o4ajpQYIRxDorDUdRibNApJC2HaVib8TtedMcEeTXfOYjSnibb1eCY4UYs3TGt28ZCOU/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWYwYLPOCq3NicSibhsegtsATNaxJDF9uiapQIQHicnrm6Kq4dC1HpdxQNuqrS2mrRx0s0zuIQazyFsO1bdZqrplARAGG00b1DrRQhM/640?wx_fmt=png&from=appmsg)

#

# 案例（3）---菜狗  公众号信呼OA分析-sql

## 版本：最新版本 2.7.0

## 参考文章：

```
https://mp.weixin.qq.com/s/YIQDnYjSbRFStPEWJ-nWBw   菜狗安全的审计  菜狗大佬的【代码审计-实战分析某OA前台注入&鉴权绕过】 https://www.bilibili.com/video/BV1aDqTYkEQm/?share_source=copy_web&vd_source=7ff27bdc142f051d6aec8c3424b47cb8  知名小朋友大佬的B站视频
```

## 路由分析

这里可以看看上面菜狗大佬，的文章，里面有详细讲解路由的配置代码思路思考

mvc框架，大概路由这样设置的

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWbupprxn69FicjSWISvbqKjOia2icOjJHAGKUaT7djwPGL3Y55e0CmbuBgFBPibVns9dZh40hW6e2icbhdRrAatJvtTLv0AL76d2kl8/640?wx_fmt=png&from=appmsg)

## 分析get封装

这里可以看一下知名小朋友大佬的b站视频，里面有讲到这个get的方法

在rock类中的get方法

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWZYqYZ1dO0icQos4uicLEicGUsbSFqmFqxhdaxlTAdmFQH0ZC480paGdt1icoUU9NCicRWiaziabTu52JAjVXMgTa5ibSGJA3FYzhwLCkw/640?wx_fmt=png&from=appmsg)

跟进找到这里

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWa8kF8wIQ2icxYzeTr4WEFZGYvDgqqJQqNZNY4qrlmU1EvZswMFJwvHt3AhiazwFuWib8GmjdD8mCYicADUKWg1YBLAFwg3VR1wxO8/640?wx_fmt=png&from=appmsg)

漏洞产生地方

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWbdXjNI4uiaqLtgHjJbU5RjpqqcaQickY8d2JSQoJo2siaTJ25ia7oUgNNarPF2WvcfPyvQ32Ke5FjiaOouCqwoXG8UJ2TecCicwzML0/640?wx_fmt=png&from=appmsg)

```
这个有意思，在封装get方法传参的过程中，会对base64进行解码（但是有条件，参数值需要以basejm_ 开头），然后对解码后的内容进行检查是否存在xss，sql注入等。<br/>但是某些前端输入的参数是base64编码，但是不要求是basejm_开头，会在传入参数之后，走完封装的get方法之后再进行base64解码。<br/>这样的话，前端传入到这个get封装的方法的时候没有满足解码要求，没有进行base64解码，get检测就是base64的内容，就会绕过检测，从而导致sql注入。<br/>信任没有完全覆盖。
```

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWbF5kia6j7CJ1fGhX5EOdlt8Uygd7qaWH481jjGSxueBCJ22P2EGbNKsBHU5qI7FPu2X8lpv4P7owA0rIkO4a0OKzojz8pZ78pc/640?wx_fmt=png&from=appmsg)

## 寻找漏洞代码

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWYZAq7c8TfpWMXmT9ZyEsTn1pNr66wSjibGG5hP3iboSxSA15icl6uHgzXWfuibZBZDv3U6XHJJKBgpIbs59E4OyN3FM7dUISRKh0g/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWbLCP8VaL5nMX6Pv2N9GoHqaibdEaKRnx6ibY0VS1YqY6nHbt6rmAQRYBC6M3UJfgpibYjibJzPL4YUaV3yKeOI4VhPibAibJ2cMGBBs/640?wx_fmt=png&from=appmsg)

底层封装的slq语句大概的意思

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWbE7kanNl4afx487iaGhQ1wNDfSl2UBznlUJV3lYe94U7bOib4OuICOkpY3UMkt9oicTcSKsv8UhzW40UAmAHeCguX7KRYicOChk6U/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWYHiczmGWeG8JAJswyc9ncgEUP2Y93ibqV95ogHJfpDx9dtAVw6X7TfJdOV9EmjequIic2TASruUAFOw8z36TICEuAsjM5QFazl44/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWbUBE8OdnstiaJQU7wdpg9F5QpsZic1WH5wgdzcbyazo5SS0eUDL3H1AAYq3foibhB3EqibyXNSxZZ8zfGgZTwyUqVKglzEUPDe4hk/640?wx_fmt=png&from=appmsg)

## 第二处

对应文件：webmain/system/table/tableAction.php

对应方法：savedbupurlAjax()

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWZU165xv94n8hoHiatP6YB0ESr7sPeXuFkPvQ579kdCesX3v3kevtGxia3HQHyUpB9uyiaQF4N3KicIzOn1nwGdicGBOkkpMkDj52sE/640?wx_fmt=png&from=appmsg)

不搞了 大概思路都是一样，分析底层mysql 执行语句，然后进行poc验证

也是为网络安全事业奉献自己微薄之力。

卷的同时一定要主意好自己的身体，身体是第一。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6KKlBTUaMxAicmPbTMz1FiaqOzpeHKfIbSQVqicUpTlS5WBNhTdQic7ftg6Z3aSjuFEA2QueRWSg7F544ZtnJICgXA/0?wx_fmt=png)

嵩艺

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6KKlBTUaMxAicmPbTMz1FiaqOzpeHKfIbSQVqicUpTlS5WBNhTdQic7ftg6Z3aSjuFEA2QueRWSg7F544ZtnJICgXA/0?wx_fmt=png)

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