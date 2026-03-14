---
title: BurpSuite快速过滤与丢弃数据包
url: https://mp.weixin.qq.com/s/U5PtH_qH2lJVJLbvGERBww
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:04:13.518777
---

# BurpSuite快速过滤与丢弃数据包

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVkmicSgx1XEtfxiazve7ZOYUpEsmibAtFnCibmExcFRVsibvsjic3erDqssJdyGNS5y7X4akb9BXVXVvCiauBYGfUuavJVtHVWStCjRs4/0?wx_fmt=jpeg)

# BurpSuite快速过滤与丢弃数据包

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 276，阅读大约需 2 分钟

## 前言

测项目的时候，抓包可能会遇到重复无用的大量数据包，一秒几个的在history中闪过。不仅看的难受，也不方便测试人员测试。

下面说几个常见的解决办法。

+ 前言
+ 感悟
+ 环境搭建
+ 小程序注册到发布流程

- 注册
- 小程序发布

+ CodeBuddy CN
+ 注意点
+ 前言
+ Proxy SwitchyOmega 3 过滤
+ Burp scope 过滤
+ 丢弃数据包

- knife
- BurpHttpHelper

## Proxy SwitchyOmega 3 过滤

![b67f76face7e0b751e4bfdc3ab70a612.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVl56k2uwq234YjKylSgyJ2sJlVLK4HKFqFkmhhETk4RiaLNiatJCwYUoZLKVWiaiaVxX1uQLXkjmoNsv8iawZOY9kE728PP9DTy389Y/640?from=appmsg "null")

b67f76face7e0b751e4bfdc3ab70a612.png

在此处配置
![9d3bda7c89b365321c021061c4b5e811.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlmO4aM85dpbbbibKmjAficqB1Em4gWiapVARDP4lI4T9iaF74ahiaRSYFPbPRDJBMySMbJKAHqaVep4u0zqMzUA0otEDW1OdQFVicfU/640?from=appmsg "null")

9d3bda7c89b365321c021061c4b5e811.png

## Burp scope 过滤

勾选
![716336c8525289c214487523a5aff27a.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmhGeztNItLOBcbyibACkuHogOICYYxUe9yCAw7N8ewjKoKUUKP0yR6hK7DdtX1QRlXc3buia3c99TIic8sKwaBIjv3XRdypLHmvw/640?from=appmsg "null")

716336c8525289c214487523a5aff27a.png

**配置黑名单**
默认所有放行
![ed3bb3a58114ed7930ad0369e231d8a8.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl3iaRzywlIxibcA3gl9UeRfn1ibaO9dPZwCUcjvzNUAQmCPXRlkTVFC0jjMj6QXYwLpRibtBLzicm7j0qLADFRsdciaEfZXwtE09Ob0/640?from=appmsg "null")

ed3bb3a58114ed7930ad0369e231d8a8.png

排除的域名、IP、URL 填在这里
![f85d101c88870eb47bb5dc85ec8ec0ce.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlY2JyGGmBKCrYQT3EvBJRGtW1sx2aYSfqXHkqvehYdX2BGicdGq36tE3DqCdpu3QFsT6joAhR9bbEFGnI9F8fU9ibKhVEcRGs4g/640?from=appmsg "null")

f85d101c88870eb47bb5dc85ec8ec0ce.png

或者 history中
![f94fd5e3b594c9de38f6677181b36a71.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlukx2fXLicDVJ2Z0xjXicicGNRQDNrhXFIf4bF4tv3XRBTu93gbN0XD3HSnGyLWRsMFhR8Adag5K82as7W5rIsQbg3ibbNDMncCbY/640?from=appmsg "null")

f94fd5e3b594c9de38f6677181b36a71.png

根据需要二次编辑
![95308fc807e0b2c462d69bd6b6d0b5aa.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlmgYgiaDmgoo2CY4eMDPpibukorAFqfd538TUXqVsgXmRq5qnWHxQLD8uwSTGib7MaOcZNS15AIUceMIyQ2qOOpR7NqWz6TyptI4/640?from=appmsg "null")

95308fc807e0b2c462d69bd6b6d0b5aa.png

只显示在scope当中的URL
![9a26437ce2537ed9f17122c8f77cd545.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmRRDicHzfY31icP16MAngs92k1AIsxObRia6U35jQsuRdPMEuIhLUoHjHz3Z24npgnneEWru4iapXBmj9EN64wK3mVhPZXOpcGV9k/640?from=appmsg "null")

9a26437ce2537ed9f17122c8f77cd545.png

不拦截过滤的包：
![a10bbd186e5a68a61d573f8cbdb269de.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmV7lburictbGRxD5M35YHy402oFkvvnJHY4HCCDrSkCnMsNiauFmCFsc4Xjic0rl2mcXNBGsKzkVJv7MTZVyORDjSyTlPKh8gbKU/640?from=appmsg "null")

a10bbd186e5a68a61d573f8cbdb269de.png

## 丢弃数据包

上述方法只是过滤，实际还会发送到服务端，如果想要丢弃

隐藏没有返回包的
![6fe92ca800af8a6d1fbd0a56dc7c7a42.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnxDxfZibwOicUQr2tAKUPVD8kvoykt3dUyQSiapGfGBSPphe11qS9pPtHqhcWrwUVj6RKon0xSicCt7PfNw9nRmzRMPtTNg9J1os4/640?from=appmsg "null")

6fe92ca800af8a6d1fbd0a56dc7c7a42.png

### knife

配置丢弃的数据包，常用 knife https://github.com/bit4woo/knife

打开knife界面
![78e487628c0b0a40adc34ba5858ae46a.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmwSVFWgNVkcgbFTKZFQYt3dBsMK0YnFTH7atTajmyUVG9dMXPe8xoVMpK1uqKuic3ibjEDD07l9LI6qy5gAZEWsBXTe1Yo7YMZc/640?from=appmsg "null")

78e487628c0b0a40adc34ba5858ae46a.png

选中数据包
![5bd9033e048e5f2fe54f0e776d5ac9f7.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmicq5w1jibpsruBbZ4iakRKvNAy8mlZwY5P7CbrP6sAm0sL3Q36VTYdcLeDrC9JkFGtH7hgaGlmYZmiaFwlBhlf7CyMZPhfjxjHh0/640?from=appmsg "null")

5bd9033e048e5f2fe54f0e776d5ac9f7.png

选择策略
![aac5b60a77870dd75efa40d1d3ca4a92.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmfq41hOu0tamBjmPia5U8oMypwiaNqVCWMUJA6WBtCw5tLpaGguQnsDRUf2BZkuw2kKP1q7PTg6JeurJ4z2bpPt8s5ibFVrayl5o/640?from=appmsg "null")

aac5b60a77870dd75efa40d1d3ca4a92.png

结果
![e80bf987ba13deb059486cefa58db02b.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmOuxwURx2iaHcw7E2kyOurtbVZWiaAP6ibk1icOO4vBfC2q3qT9SNOHvYoYuuxoGhxjZ2VPROCkwBwOicfDW6fMjk0l1l46y2UuUCs/640?from=appmsg "null")

e80bf987ba13deb059486cefa58db02b.png

### BurpHttpHelper

项目地址：https://github.com/MaskCyberSecurityTeam/BurpHttpHelper

BurpHttpHelper是一款Burpsuite插件，主要用于简化和解决Burpsuite对Http的一些操作。

目前实现: HttpHeader增删改 HttpCookie增删改 HttpBody替换 随机UserAgent RepeaterResponse自动解码 丢弃特定数据包。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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