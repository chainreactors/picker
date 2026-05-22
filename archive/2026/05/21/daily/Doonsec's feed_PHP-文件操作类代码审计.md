---
title: PHP-文件操作类代码审计
url: https://mp.weixin.qq.com/s/6WJJ2qrgam-DHOxBEQd4cA
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:05:01.809027
---

# PHP-文件操作类代码审计

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3CSuJ7WYnWaHRPMviaChG0g1BlaCtjibBu2EZB2yOVvGCaP5l9yzvEEXGtlO1pxOv7Moe89mXY9VicOQtGVdxwDwO3Hia0M7OrAGLo1icH1YibjXY/0?wx_fmt=jpeg)

# PHP-文件操作类代码审计

原创

嵩艺
嵩艺

嵩艺

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

参考视频b站小迪安全和菜狗安全和知名小朋友大佬

免责声明：仅供参考学习，禁止非法活动，如有违法犯罪，概不追究本人责任。

# 大概文件类挖掘思路

快速分析脆弱：

1、看文件路径

2、看代码里面的变量（可控）

3、看变量前后的过滤

文件安全挖掘点：

1、脚本文件名

2、应用功能点

3、操作关键字

文件上传，文件下载(读取)，文件包含，文件删除等

黑白盒结合起来测试，从函数找到功能点，或者是从功能带你找到对应的函数

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWb8RNGTjjaoiajnjzlxZ1yGL9SLUZkWpmfAhL4SH0Tq5T2fI0erWicagl6iaUAGoc6xIEJxBc1Nxxq4aSwZh9vI1x45CAaV1s9Eao/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWZPyc8iay5AyJjP4jEqiagqOhdiaRAic0KwnPw99vOmD3pDWXE1qW7Nd7K7NSbIoIbcaSwf880uZDG5DTr8baH17mWicUdE3FP9FDxw/640?wx_fmt=png&from=appmsg)

# emlog\_pro  1day分析

```
https://www.cnvd.org.cn/flaw/show/CNVD-2023-74536
```

## 安装：

环境要求

* PHP5.6、PHP7、PHP8，推荐 PHP7.4
* MySQL5.6及以上，推荐5.6
* 服务器环境推荐：Linux + nginx
* 服务器面板软件推荐：宝塔面板
* 浏览器推荐：Chrome,Edge

## 如何找到突破口

搜$\_FILES,  $\_FILES MOVE\_uploaded\_file ,等（这里还需要补充）

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWYEdmGpOgXs0mNV2q77elQDeHB0EZT7yPQuWDH7vic2DROMmqxVib4nx5biaKBXbOsqDWxOXJptHN9tpDVkVK0hIpsEKvDcvqe8Dc/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWZPm2vagpXZPwvJ1LCzurj4lMRhXvcvibxyjGl4p5BiacAl69Vnklno4yrlIhQZUNfuxNlOzWLQV3OFxXglPLrmDfpzSag2ZNT7o/640?wx_fmt=png&from=appmsg)

我们可以现在从功能点的文字描述，去找具体是那些函数实现这些功能，看看这些函数是不是有漏洞。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWbRq3FibQ1ZnrWR069lia4HiammDSMEzMDchfCGhW8csqia3JFeyFjflu7CBjK825Z9Ll55o5wVpvvb9h4s3oKlV1iafpFZGAcvakOI/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWa92NiaoqLKjRibUejqCysRBcLLD5VZaSajQjsDDYqoG4tg29xuYM4NrbzbDtTCaTcKtDFRAw6paptAyjHxFuk2oZJibxOY8HibRhs/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWaYggtdTzNBNw2OUq1wvMRmDiaolI52U8DTbOrYMtEGozzW33dsvlo2twELlTVtZdOLia9CRPJibrfFb4lOkAMSkib7dLngsAXOIFY/640?wx_fmt=png&from=appmsg)

## 源码分析

就只是做了解压操作，没有对压缩包里面的东西，进行处理，所以存在任意文件上传漏洞

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWbwAuibfs72Ln7kME9MYMQEmb2V7JLGuumFkmYVqtJ1vccFxia3VbFBNRKB5jQOsOTticvFibVthKJ2lPYIfMHFpKhQ2tcicXiaR1ICA/640?wx_fmt=png&from=appmsg)

就只是解压了

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWYfTbLLCD0ViaeWoyPD0FljSOyeLqDt0PqoHhUajSwibU2J8Tj3EJdkfEzKN0hhaxia7OrZVS3j71ricMyU0hAdoQpoicpWFM8o9QYA/640?wx_fmt=png&from=appmsg)

## 漏洞验证

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWagGxhguXfl5IdEs0JibQx4icIq8c0oHdTWMp7vjbLOIf5FySRCamib2Kcv6bhicBa9kRDIjdQtaI2kX0C800DkJb4cbZIV6UCRE4s/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWYGjz8gIhK9oUXENARXrNUN5ZA7T5PyXkmibVuohkGNSvWIjDNlHh6xnC0IN6yIOHsYG9ZZgwoMkxjMZdrWJOG0xZ6KY6CVfI98/640?wx_fmt=png&from=appmsg)

# lmxcms1.40 版本--任意文件删除-菜狗公众号

```
原文链接  https://mp.weixin.qq.com/s/FsxHSwsbMMKBFtO-4a5gFQ
```

## 简单分析mvc框架

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWYZXK6XTKBnxibtfkJ3l6EPIKpHaswP6OialEbd8ZgobKaSMiarc6OnD7cIwyaBK0joeaib128XLubZWO48eRAvia2aic4n9IFHiap6UU/640?wx_fmt=png&from=appmsg)

## 安裝

lmxcms1.4版本

mysql 5.7版本

## 如何找到突破口

unlink 是 PHP 自带的内置函数，功能是 删除文件

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWZXRt3Sib0Z4ZYzoeE4yBerY7AjWxPcCo8WB71y3rSmv3PoxHkwVYbP0yGZicubrIx8uG2LcQfPlpQaQ3K4PLD7SZ9KNenzBrn00/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWYKLyeY2uylI2aZ73yBpTtuZYMw8gkGlrGDc70ggEnDtZxib75O4c0jF8J3PDLwsptqHDjwPv3ic5Os4OIQficj9N8BVxnYPqR7Dk/640?wx_fmt=png&from=appmsg)

## 漏洞验证

数据包构造

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWbNEpYa4M1fCDQFbo5GSHALfVev8v231Zs5XmwMBnUwtia5AW6VSICL0Kr6qlpFDT2JzfD0IiafXY7ib5Xwia6R5Ea3MbJdNhh8qrA/640?wx_fmt=png&from=appmsg)

现在delOne函数出验证演出路径

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/3CSuJ7WYnWaK9Qic6qQKZ4CxpBMCj9koeU2EiaUsO7ZLTTM1wdwbf4Q44gvMPw2V7VPPSrWmEtAK4Lf4DiczUTIcLs5T059ibYofJWQwluBkIeI/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWZq9GWWQ1ANia4RdUcJ5PJrEeS3tHMnNAKBeT7WZ1RXwbictJoy8szeonxRA7UoD4Mp0ibj1rLAJTDCJAwy9gQ9fsQ3ibRab9I6qZw/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/3CSuJ7WYnWZC98gN30R2zRkMAlic25ItcZaE3zTRPbWkqicYbeZXuS5ibVAHsyoX6rTEBSIjjiaANP0icmvqbicdZx1HiaK3vMyiaiaXtkgmx2hHaYicQ/640?wx_fmt=png&from=appmsg)

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