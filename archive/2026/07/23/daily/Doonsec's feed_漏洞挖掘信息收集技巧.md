---
title: 漏洞挖掘信息收集技巧
url: https://mp.weixin.qq.com/s/Td5558oH8-x7yMXesBTl-Q
source: Doonsec's feed
date: 2026-07-23
fetch_date: 2026-07-24T05:03:31.225215
---

# 漏洞挖掘信息收集技巧

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6M8gmNQfje9XOcBTqJZMHMb9x1Kr6cU26qcvlwjNjD00GmjgibpeOWBexM2wAYfCuJc0Hznrpcu8VytLVmWtOqJ9ouKT0fsibQzA/0?wx_fmt=jpeg)

# 漏洞挖掘信息收集技巧

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:hkl1x原文链接:https://www.freebuf.com/articles/web/459164.html
```

###### 导语

######

###### 可能对于新手去挖一些edu，src，众测。总有一种无从下手的感觉。而对于老手，可能总觉得为什么他能挖到我挖不到。面对这些问题请读者看完这篇文章可能会对你有所启发。

######

正文

信息搜集对于做渗透的师傅们一点不陌生，但是很多人对于它的重要程度有所忽视。说到底其实师傅们的挖洞能力大部分都差不多，所以想挖到更多的洞就要找到别人找不到的资产。信息搜集这一块我分五种情况讲述。

### 1.事业单位或政府

###### 师傅们看到这里就差不多能想到一些什么了吧，医院，学校之类的。这个我就说一下我众测时说事业单位会测试哪些部门

##### 事业单位

```
医院 （第一 第二 妇科医院 儿童医院 骨科医院 中医院 精神病院）学校 （小学 初中 高中 大学）图书馆体育馆少年宫电视台福利院养老院各地区的就业平台（重点）
```

为什么我要说就业平台是重点测试的资产，第一因为它所涉及的业务会更多，那么就更容易出洞。第二是很多师傅想不到这一点就业平台是事业单位。这里举例一下

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQRrQ5OUCSk1q4wlxwPE1Aib95ThH7sugBJribbxxbLgbdmY0S84YKeIsVTh0cr1uuHaBNSnWPFibQFVWjHs7KgGzexl8MvHWJrrE/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=0)

#### 政府

```
人民政府法院检察院公安局税务局教育局人力资源和社会保障水利局交通局人大
```

###### 有时地区的政府部门的三级域名是相同的，例如 城市.gov.cn，那么我们就可以对子域名进行查找了。下面有对子域名搜集的详细介绍这里先不说。

######

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRXV7wiaRZ8qxMXAuxh1qrrfs3pZmGFfiasu8sdkBc9yFjoW0QhPzsoKicsBZvkJ6fB8ibdJY3CQ5bWnTZSu0Tvwd4J6Tmt3Ltfghc/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

### 2.\*xxx.com

###### 这个也比较常见，无非就是搜集子域名嘛。这里推荐两种方法

#### hunter

###### 其实我之前是用fofa多一些，但是现在fofa的资产太少。就用hunter了，用来才知道真香。

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboToKzbibRueiaice4b5Dicib1786okrmFCg8JfthRswIQl6qFjB7vzGS310J1aSlLWZqGsRL0XbKKQkr8gAz998R9GB9p1mTwBjV10g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

链接：hunter

```
子域名查询语法：domain.suffix="xxx.com"
```

#### 子域名挖掘机

###### 这个工具我平时挖edu比较多，因为这个工具是跑字典的，对于一些edu比较好用

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRxb8iaLfKVaM9cEPCBTNgXzNibmOj9xuSe7AnrvePibtZqvdl4VaGWrLTsPv4JdibmdeVpZLjvbrf118Dp8uWBw57jO1GjWcGlEibo/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

###### 下载链接： 子域名挖掘机

### 3.某某集团

###### 这个就是针对一些企业的src，我们要拿到这个集团的资产（网站，小程序，app）我先说常规的，好用的在后面哦。

#### 爱企查、企查查、小蓝本、七麦、零零信安

###### 这个就算是老生常谈的了，主要就是可能一些企业src的一些资产要超过股份的百分之多少才收。我下面以百度举几个例子。

###### 小蓝本

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTnAfuB53iaic6m9rhn0UDaQhibsgEcaRicTHCXwJy0hkKEmFC0ZuWQaA4WIL7kAUPySicibZXSe4mdvfLp3UM4zRJJWy7D0XWGVlleo/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

###### 链接：小蓝本

###### 七麦（主要是app）

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSJoUC4zH2ric6OGHR5OjmeWpjRQiajLEo5BhTltEcAGzLibTMr11fH3DUtcYEnQibe6LNp1flLUXZEPtVXluibth1ic8AGiczYh1vibuY/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

###### 链接：七麦

###### 零零信安

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRBOE6AXxBsfIpyBgIldSickRic5STR5qcIKp4zc7EHUUGibYVx20A9fQAgJf79pTrEI9UCWWp9oBCKqgiaBJ4yWJPLg7TrzjMwcwk/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6)

###### 链接：零零信安

###### firefly

###### 这个网站很好用，他是搜集了大多数企业src的资产，添加src的名字，直接显示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTcWXeJGudTs2P2ibPgFEfo9qC0fqZnN64rzbyNLnS6goq1oXNOVcicNf2Dx0qddUPVZiccvR27zdyXUcczz5PK67uXZ3iaNh75G0E/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=7)

###### 链接：firefly

##### 还有针对地方企业的众测项目这个我说两种我常用的方法

#####

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTs6ibvFY76UcSlYl5mzfNDKiboUVnjBr6xDW080gS9BTjr1GtPV1E9gNI0RclicEt7iahyR7t4GZKJj1LvEmwF0A6gjPRx93ArNtw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=8)

###### 地图搜集法

###### 在bing搜索引擎的地图功能可以搜索到当地的企业可以作为查考

######

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRfuLiaicdqrH5pnPjgURpQYiclU95iacZSPHKTqJwiczMGkc8SkvAPic5G3RShxD3VoauChN8j2d0UcVQCxf5KibDymzXF655lM3u0TY/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=9)

新闻或微信公众号当地政府的公告（排行榜）

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQibhTxibBiaNpEqaRaicnoabA0eGz8Gw0pUsQNlTlicNUTAPxg8xSlUO1w9T16KSFZJZU2zCmqcnXW8dy7yRhxnskKYHox64Oyt2Is/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=10)

我认为只有在排行榜的企业才有可能在互联网上建设一些资产因此我们应该注意的是一些有钱的企业或者互联网企业

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQQRdA2PnvUNGibd6qsVbJLxztZoialITMGvdMyKRxia3mp7H8iaNKWparB0VTs5C2NDiaQs0hgQ7ibmXl33MVn3UfOHTVibOH5DsgCQg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=11)

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSgRiasicScj6eLjxELbQfkrXxml0g5GIZD4gmsumjF3GSZUP7dnxbP7AEJB2NDnTobXm9XxK58RBSstDosANqmt0vgBicic4PictXg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=12)

### 4.edu

###### 对于我们在挖edusrc的时候遇见最大的问题就是如何突破一站式服务大厅的网站，要突破这一点，我们就需要拥有教师的工号 、身份证和 学生的身份证、学号使用谷歌语法可能会查询到学校公示的一些文件泄露学生老师的身份证学号工号

###### 谷歌语法

```
site:xxx.edu.cn 身份证 site:xxx.edu.cn 学号site:edu.cn 密码site:edu.cn intitle:登录|注册
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTFiazDbnWIOrj6RTV9YTzN7iaxQlPGcSBHp1iaH7MHL1ftfib2d9IxXYibQVq2JvRKPSGlL7zwKicWNHbkTjpEBpLfvvicFOt5q0q9Ig/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=13)

成功信息搜集之后找到登录一站式大厅的界面或是弱口令或是密码格式泄露都是我们登录大厅的方法

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRAK8uNyAp2KUPa7y5uOAK9nScxnLhSe0t2cKDlZibdwgdmGPlID12czoy2k4ppWnYhPTWMp6ZiaBmreRVqMzlWzftZdmWyKiaZqs/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=14)

### 5.杂项

###### goby

######

###### 师傅们可能会有疑问？goby不是漏扫工具怎么信息搜集。这里先不慌。上面的三个都是对多个资产的信息搜集，那么我们针对一个资产（网站）怎么信息搜集？nmap扫一下端口？扫一下敏感路径？探针一下是什么中间件，编程语言？nonono。一个goby就够了。goby的工作原理就是先探针网站的一些信息，然后再去poc扫描。这样我们既拿到了网站信息，还对网站的1day测试了一下，一举两得。

######

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTmCsk8XMJ9mon6IibzMKYeic0ViaicjyvvwIebxM5BSJn7HQo4zouJ6vAib9nuJc1cHAiawjV7HOanOTGDmu0CbwOYo65yIF7gsD14I/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=15)

###### 绕cdn

###### 大多数绕cdn获取真实ip的方法都挺一般，我主要是用国外ping的方法，毕竟国内网站在国外cdn加速得加钱。

######

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTD2aicJLbncZ12SyqmTKgtDljyhf4MFspbpMTJB9GCGvyDibSSNeFCtDaT9cdIXibJdNwp98k2MQ03PoXVxsSf7ADfzbZ4Yyic5fA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=16)

###### 链接：绕cdn

###### waf检测

###### 这个其实在测试的时候在发现也可以，这里主要是有些师傅可能有专门绕对应waf的payload。

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboStaiaMDaIlRb1zcr5pe9VvF3A12iab9Bz1M6iavdwiaA8liaBBRmwib4YVeFHRHZaVZggmRKv565T7ax5zgicZQp1IBraNwLGGZia4VaI/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=17)

###### 下载链接：绕waf

###### wappalyzer

这个浏览器插件也比较好用，点一下就可以探针网站的信息，但是误报也不少。

![图片](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSFah2WgHC5j5mzvGrGsiaKWZLicibvtfZVYQvHKFxibddlBdMmC9HoAUyN87rs4j1xXppx51cg5KA43zBpncvRQXa19yjTVyxMiaz0/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=18)

###### 下载链接：wappalyzer

###### 雪瞳

###### 这个也是我最常用的插件了，非常好用，除了接口，还有账号密码，github地址都是可以利用的点

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS8gMciahwgrKwWEgt8kwfsHrZKZK0qkxxO621pIXyT952J3xQtxsh8UGwQG8tEtFveCyClBdKdfLRFJuFdiablvqpRuHic7Zkkj8/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=19)

下载链接：雪瞳

结语

信息搜集作为渗透测试的第一步，直接决定我们的攻击面。我知道大部分师傅都不屑于信息搜集或者简单的搜集一下。渗透测试我觉得应该是一个需要耐心的工作，跟多时候应该放平心态认认真真的每个资产都拿到，每个功能点都测尽，最后一定会出洞的！！

文章来源：陌笙不太懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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