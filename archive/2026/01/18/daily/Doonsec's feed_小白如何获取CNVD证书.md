---
title: 小白如何获取CNVD证书
url: https://mp.weixin.qq.com/s/d5m_8MMXf_xKFp-vQyF_lQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:41:35.793324
---

# 小白如何获取CNVD证书

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayC8QlvqHiaw16IzISyiblbPHjvnqYTia6qteunsDWfuMAL8mBadibs0ytKQ/0?wx_fmt=jpeg)

# 小白如何获取CNVD证书

Say Sec

![]()

在小说阅读器中沉浸阅读

以下文章来源于神农Sec
，作者神农Sec

![](http://wx.qlogo.cn/mmhead/y5RpFDuUObwMMxt9glfAKialneQKqPPt5EsUdS3whAutdEwTpmN9liak8tq2H4ACBJs8XypAPNVGM/0)

**神农Sec**
.

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘。不定期分享网络安全领域各种好玩的项目及好用的工具，欢迎关注。#尽在神农Sec# 文章如有侵权，请联系删除，感谢！

扫码加圈子

获内部资料

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（知识星球优惠卷）。

#

01

0x1 小白如何获取CNVD证书

## 一、 CNVD介绍

### 1、浅谈

这里给师傅们介绍下CNVD漏洞挖掘，包括相关证书发放操作。前面给师傅们分享了欧盟名人堂和CVE漏洞相关提交，相关流程都很详细，然后之前师傅们还有问我CNVD漏洞怎么提交，怎么才可以拿证书，为什么漏洞通过了但是没有发证书呢？

这篇文章下面会手把手带着师傅们进行相关CNVD漏洞资产收集到CNVD漏洞挖掘，到怎么提交对应的漏洞，且资产怎么收集，挖什么样的漏洞容易拿证书呢，这篇文章会给师傅们详细讲解下的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayl1O5iaTIhEkaV31T7BLNrx0Y7nNAYQduTQibqpwjkoQevujvbYofXg0Q/640?wx_fmt=png&from=appmsg "null")

### 2、CNVD平台

国家信息安全漏洞共享平台（China National Vulnerability Database，简称CNVD）是由国家计算机网络应急技术处理协调中心（中文简称国家互联网应急中心，英文简称CNCERT）联合国内重要信息系统单位、基础电信运营商、网络安全厂商、软件厂商和互联网企业建立的国家网络安全漏洞库。

CNVD官方网站：https://www.cnvd.org.cn/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zaytO7rLsRDAHD3nBwo9CpcKyibmPhYnVdibK41ImibNFVTBAmBz3Z4oystA/640?wx_fmt=png&from=appmsg "null")

### 3、CNVD证书发放规则

**归档漏洞的证书颁发条件为：**

**1、事件型**

事件型漏洞必须是三大运营商（移动、联通、电信）的中高危漏洞，或者党政机关、重要行业单位、科研院所、重要企事业单位（如：中央国有大型企业、部委直属事业单位等）的高危事件型漏洞才会颁发原创漏洞证书。

**2、通用型**

这里我们主要介绍通用型漏洞证书获取方式，通用型发证要求为中高危漏洞且漏洞评分不小于4.0（这里说白了就是低危不发证），通用型证书获取方式需要满足两个条件：

* 1）需要给出漏洞证明案例至少十起（例如：一个建站平台下的十个网站都存在SQL注入，你就需要提供这十个网站的URL，具体漏洞复现方式需要在你上传的doc文件中至少详细复现3~5个，剩下的只需要将URL附上即可）。
* 2）发现的漏洞相应的公司规模要以及注册资金要相应比较多，反之可能提交的漏洞会被打下来（CNVD要求公司的实缴资金必须不小于五千万）。

## 二、 传统web资产收集

首先这里我先确定这个公司的资产信息，可以使用网上一些免费的企业查询在线网站，比如爱企查、企查查、风鸟等在线免费的企业信息查询网站。

下面可以看到该公司的基本信息以及重要的注册资本资金，但是现在对于要拿漏洞证书的通用型漏洞来说，需要实缴资本大于5000万，下面这个公司就符合。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayQkI6g31ibVCvxhMbW56dibbmWPTA8UJ18J7ySXVdDqic5xCj3rUJ5mfBA/640?wx_fmt=png&from=appmsg "null")

然后有些师傅们不会批量找对应资产实际缴纳资产大于5000万的，那么我这里给师傅们演示下，我这里拿企查查为例，演示下具体的资产筛选操作。

首先点击首页下面的高级搜索。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zay95JAbvbAwoHgZ2FickibMpXr2rj3DlVXKL2qia9ULcR9DwHfJPSia0Qyaw/640?wx_fmt=png&from=appmsg "null")

直接筛选大于5000万即可，然后查看，要是导出需要会员，可以上闲鱼搞一个。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayQwnT27DLib0M1Tsr5CwCqarCPsIkYfibA047EH8sZibH6kFHmGwNsDfHA/640?wx_fmt=png&from=appmsg "null")

或者直接搜科技有限公司/信息科有限公司等等（一般这种有很多后台系统）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayOy9Oo5NOaa9AibJSSOGspadib9c7C8chAw76eCVIpSAvIGHcdyiajMicNg/640?wx_fmt=png&from=appmsg "null")

这样的科技相关公司，xxx系统都是很多的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayYtp84rQqCW46XSZ2p3jP4DicJf81Uhr7mS0aw5zmeBeDpTGgYicPntFQ/640?wx_fmt=png&from=appmsg "null")

像这里面的系统都是可以进行测试的，一般都是可以利用空间搜素引擎进行检索，然后去挨个找漏洞，找到了就可以再去利用搜素引擎进行检索关键字进行模糊匹配，然后打个通杀漏洞，就可以拿到CNVD漏洞证书了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayZyltCx2GvIic2YCKb9shObibDib1vgPUTgaNicJyMxicDOkR2zgjfjQ3FAw/640?wx_fmt=png&from=appmsg "null")

直接在FOFA搜索引擎搜相关系统名称或者系统的简称，看资产是不是符合CNVD证书才发的标准，毕竟漏洞复现需要至少找到10例。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayuEKm6Ssq34A0ur8GklnbC4uN1LyMmZ8e6obh79srBibbgygiaibMpY7Pg/640?wx_fmt=png&from=appmsg "null")

## 三、 网络设备类资产收集方法

这次给师傅们分享的CNVD漏洞挖掘方法，除了上面的常规的web资产收集，其实网络设备的证书站收集方法更加适合新手没有CNVD证书的师傅们。

这里我用经验提前帮大家收集了一些常见出现漏洞的网络设备类型方便供大家参考：交换机（Switch）、路由器（Router）、摄像头（Camera）电话机（IP-Phone）、打印机（Printer）和网关（Gateway）等。

比如之前挖的几个惠普的打印机未授权和弱口令漏洞，直接去找对应的资产。还有比如说思科、华三的通用型设备系统，哪怕是弱口令的设备，都可以拿到CNVD的证书。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayvbibWnwgicGdF1HpCMlzW6TldbzticrOkJnqjYFBDlw7S8avGE7XafXJg/640?wx_fmt=png&from=appmsg "null")

这里拿惠普打印机进行举例，直接拿像Google浏览器进行搜索，对应的网络设备版本都存在的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayCzIUSMJClGEYYfUIl8BhnzbTxj0eUEmssge4MJTFjHNzImhrcu4bDQ/640?wx_fmt=png&from=appmsg "null")

然后使用FOFA再去搜索对应网络设备版本名称，找通杀，验证超过10个案例即可，弱口令也可以拿证书的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayLwlCdmEhhW12W4MyxibbR6umUK3GibKXaZ62rQsBuOVHt6yyJ5GlD6Rg/640?wx_fmt=png&from=appmsg "null")

或者你可以直接搜索“打印机品牌全球排名”，这些都是全球影响力比较大的，CNVD肯定是收的资产。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayic75oO7xDWxATv7trnR4TwqPeNiboYJkk6DR40bib8oWX5MEh4k3JBfibA/640?wx_fmt=png&from=appmsg "null")

针对于新手师傅们，我推荐大家挖CNVD像通用型设备，适合挖弱口令、未授权、信息泄露、未授权漏洞，特别是弱口令和未授权比较适合大家。

每个设备都有它的默认密码。直接谷歌搜"xxx设备xxx型号默认密码是多少？"（默认密码不止一种，建议多次尝试常用的弱密码）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayvdJLZrsGp5lbX0bOPbqUZlvB5sZYIU60EaPNaTbw45ZibTHoxWDd3jQ/640?wx_fmt=png&from=appmsg "null")

比如下面的Google语法，找对应的操作手册|使用手册|操作视频|使用视频|演示视频|白皮书，默认账号密码大多存在：

```
site:hp.com/cn-zh OR site:support.hp.com "惠普" intext:操作手册 OR 使用手册 OR 演示视频 OR 白皮书 filetype:pdf OR html
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zay37nwicwDOE8ByFmGZ2OsC35RarQvELTnFsVNqg8q1trm6PkcgzKo7jg/640?wx_fmt=png&from=appmsg "null")

下面这个就是一个通用型设备打印机的弱口令漏洞案例。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayYTacWrxm8XSTSMaamXRrSdqKmWXQjo2ibFfgNBa5hAh96f496ZuRDVg/640?wx_fmt=png&from=appmsg "null")

然后这边希望师傅们挖到了对应厂商的通用型漏洞，就先去提交，也别管重复不重新，因为这个CNVD查重复不准，就比如说我自己一般都不会选择公开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayGmjKGgzlYMremjzyp3sL0jnfrBQB5vQ2hgCQpb71eBPhjbTyMMm9zQ/640?wx_fmt=png&from=appmsg "null")

所以你在这里查询对应的漏洞是不是重复被提交了，是不准确的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zay1Mricsw8nL2IoEzKptMq400OCCGDYGkeE6bfHA0DJBgyoyRheF0nAWA/640?wx_fmt=png&from=appmsg "null")

## 四、SQL注入漏洞

这里拿最近的一个CNVD通用型SQL注入漏洞来进行一个分享，这个SQL注入是某国内一个大厂商的web系统资产，网上搜其实是有多个SQL注入的。因为我觉得这些系统都是同一个厂商开发的，有存在SQL注入，可不可以参考下别的接口，去挖差不多的系统，这个通过网上的接口：/demon/xxxx\_table\_demo.php?id=1接口的参考，然后在里面别的接口跟上面那个路径差不多，也是成功找到一个SQL注入接口。

通过payload进行时间延时注入：

```
1+AND+(SELECT+1+FROM+(SELECT(SLEEP(10)))a)--+-
```

可以看到burpsuit数据包的返回包，即可成功进行延时注入10秒的延迟。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayciafBqBcUhlZs0sKFLzP3votZF0jXeZMrO8LyNBrt9kEtlRwQDNLKtA/640?wx_fmt=png&from=appmsg "null")

然后保存数据包，使用SQLmap跑，下面也是直接提示存在时间注入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayM1FmPSU3zKFmqadETNILZdYwNxm1QtlMYNAGoN6TUNjm1rS3mgdncA/640?wx_fmt=png&from=appmsg "null")

然后直接在CNVD平台进行对应的SQL通用型漏洞即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zay5eyogjSp6t0ZadruibDvvVUnyGc2TcHNjoktyj61oCLvuUdGNoI3iaEg/640?wx_fmt=png&from=appmsg "null")

审核一般一两个月的时间，证书就可以下来了，下载下来都是PDF格式的，那么就恭喜师傅拿到了属于自己的CNVD证书了，新手师傅呢还是建议先搞通用型的设备，挖弱口令和接口未授权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUO7Rr3CbhpCE7TX4sO4zayicc0ksPo97BYMezCyzRj9A7dOeqMghaKAQ1z5TgEdx7Sp0HxHSe2XqA/640?wx_fmt=png&from=appmsg "null")

02

0x2 内部小圈子详情介绍

我们是***神农安全***，***点赞 + 在看*** 铁铁们点起来，最后祝大家都能心想事成、发大财、行大运。

![](https://mmbiz.qpic.cn/mmbiz_png/mngWTkJEOYJDOsevNTXW8ERI6DU2dZSH3Wd1AqGpw29ibCuYsmdMhUraS4MsYwyjuoB8eIFIicvoVuazwCV79t8A/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**内部圈子介绍**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap08Z60FsVfKEBeQVmcSg1YS1uop1o9V1uibicy1tXCD6tMvzTjeGt34qr3g/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**圈子专注于更新src/红蓝攻防相关：**

```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、...