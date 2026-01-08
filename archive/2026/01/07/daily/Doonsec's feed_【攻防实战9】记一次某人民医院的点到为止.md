---
title: 【攻防实战9】记一次某人民医院的点到为止
url: https://mp.weixin.qq.com/s/K9elnDAY7sMttWN36ugFhg
source: Doonsec's feed
date: 2026-01-07
fetch_date: 2026-01-08T03:27:59.898729
---

# 【攻防实战9】记一次某人民医院的点到为止

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeEmLibjnWcLibb9yeKpoQXPjDJ2xeVPDgbQZwe71NXEzyXpcBicNEOL6Xg/0?wx_fmt=jpeg)

# 【攻防实战9】记一次某人民医院的点到为止

原创

十二

十二主神

![]()

在小说阅读器中沉浸阅读

**前言**

点击下方 "**十二主神****"****公众号关注, 设为****星标**。有用的话请点赞、收藏备查。

# 01-前言

本次攻防实战是针对某个地市的医院开展的，通过互联网打点获取微信管理平台权限，通过这个管理后台，并未能成功getshell，随机继续打点发现一个信息管理平台，通过逻辑漏洞绕过登录进入后台，通过后台摸索出注入，任意文件读取，最后通过任意文件上传拿到shell，翻配置文件找到数据库连接配置得到密码，获取数据库权限，登录数据库发现HIS、LIS、PACS、OA、电子病历数据库都在一个服务器中，获取1亿3千万电子病历信、4w条身份证敏感数据、200w条患者住院记录、5000w条医保用药数据；2个sqlserver数据库sa权限，一个远程桌面权限，由于这台服务器上面运行了医院多个核心数据库，属于生产系统；并且系统非常卡，不敢直接挂代理进行扫描，怕影响医院业务，所以点到为止。

# 02-入口打点

开局一个登录框，这个是微信平台的管理平台，掏出弱口令字典直接试

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeW6O7mUV9iazibOMK2SogBUpegLxorS12OKZdzFBGnf1keBr9AFYBbicNA/640?wx_fmt=png&from=appmsg)

一个admin123直接进，发现还是弱口令好用，永远的神。

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeX80P8Qdmq517soPZ0JnTQ5vypLAuen3vLpIhgTcwW0Aiaey8LcjAJ7g/640?wx_fmt=png&from=appmsg)

登录进去之后发现可以接管医院的门户网站，可造成网站篡改风险

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWedLOY63tdFTYwBFYNiaTcAZoymHrIlYLroWickmY3h5J6ibOkibHufbm6qg/640?wx_fmt=png&from=appmsg)

开始对整个后台的功能点进行测试，测试了一上午加一下午硬是没有发现可以利用的漏洞点。

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeCSdk4jFwbXlfoKjJcYUUibF3XdPz5AGtztb8w1RmQEGPEiaHibhXzF6xA/640?wx_fmt=png&from=appmsg)

确实没有发现有可以利用的点，立即开始换了个平台打点，这次瞄准的是医院信息管理平台

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeCFMlmDS7h3icusQV23DhlJS7xVQAj0LuTssm7t9CydiccBtRoJRDX5wA/640?wx_fmt=png&from=appmsg)

抓取登录的返回包，修改返回的数据包，绕过验证，即可登录后台

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeHBukv1LDNiaVhibjunARc7yyxXXlCXnMGFoWxHIYEOv7u391wg2bgTpA/640?wx_fmt=png&from=appmsg)

成功登录后台，那就继续测试功能点，挖掘可以利用的漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeGz9OdbDKxNomZMk0ujQA51g7Le4xuwkzGm4NMib9pDwkdOqFookBMwA/640?wx_fmt=png&from=appmsg)

后台参数存在一个注入漏洞，直接拿出神器开搞

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWek4ApX8HuSQgS8HaMs9Cg2ibibb0Gr0ms99THnKtT2S2Y7Mo46GkQSnmw/640?wx_fmt=png&from=appmsg)

把含有用户密码的USers表弄出来

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWexGogf3ShjpRXYwekWU1VXV7mbd3Ic4tPm1XlXYBV8HMs9eiaXuMFsXA/640?wx_fmt=png&from=appmsg)

文件下载处存在任意文件读取漏洞，通过filename参数去读取某个.aspx文件，通过burp抓包能够读取到这个文件的内容

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeHwFAwza4j8hzBEfVNYGhaBCZnwwVvozkU6GJuicEFL5z3ic7uiaOrpwPQ/640?wx_fmt=png&from=appmsg)

最后在我的文件柜中找到可以上传文件的地方，进行了getshell操作

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWevvEZMZv7dxBIganEygPKJYicvrwC4Z4yRQdaYSx0NELQ9IjuIC3lLtw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeDjWwtnsb9HnvZbIl805Gn0tFibkHpdJIGTR4Gpr7blq2b6icZCEB5LJA/640?wx_fmt=png&from=appmsg)

# 03-内网成果

ok上了马子，直接开连，这个时候我以为又能在内网愉快的漫游，想法很美好，现实很骨感。

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWe5D31fHKJZ1FY87gIqRH8kfTHfeiagj9ah4kicAd1y5HFs3uDzFIgcFUA/640?wx_fmt=png&from=appmsg)

系统也拿到了最高权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeRbfXwzoB3HyhAx59Xn3qcnXQLgIoD5FMU0vac55ySNMWoXbBM2KuLg/640?wx_fmt=png&from=appmsg)

简单看了下进程，有360杀毒和主动防御，以及住院收费管理系统的进程

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeqjhwyUSibJMGeOJNYNQicJ8BQP8uBlLaRDFzv4Dh36Xo5LSnA0ydCVmA/640?wx_fmt=png&from=appmsg)

翻阅配置文件，获取数据库连接信息

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeicprnwg9WibVUprdPNJ0ia4h83c2QsdUbbYseibZKT9RnsOVFeX2hN8VJw/640?wx_fmt=png&from=appmsg)

把内网代理出来，直接连数据库

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeMVcp3j3UaQktddW6dbS4vnYRYkWsvVOpppueu5NficicDyQXM68uIs9A/640?wx_fmt=png&from=appmsg)

想不到这次走了大运，直接连到了医院的核心数据库，HIS、LIS、PACS、电子病历全都在

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeDS4aKHY3Vkic1DxjmzpEicdjyGzsYNDDQWdfCoAuQYzw6hhAq1N2TBNA/640?wx_fmt=png&from=appmsg)

那么直接上大货，一亿3千万条电子病历数据

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWe2F82JibrMLpyUg7pz8KM7pHsic9ibBQ8iaZ2pwLp6lTha8fYD4HxwS6JUw/640?wx_fmt=png&from=appmsg)

4w条身份证敏感信息

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWephhfAThtAbAvT8eKD0j92nmib97TsSWtxibS8QVLcmn1YgWWloveCBEw/640?wx_fmt=png&from=appmsg)

200w条住院记录

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeqk4ms8Bsw47DpreLGM7GUUBhiaicNs8196LicLMh4YmHloy0Qp6cndVvw/640?wx_fmt=png&from=appmsg)

通过密码复用登录192.168.0.229的数据库服务器

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWe6ay98MP3BvXzIb3QSNibzZDBE38Nw7hYRt95Rat1f6P12yeADapGe8g/640?wx_fmt=png&from=appmsg)

这个数据库服务器多了一个医保结算的数据库，5000w条住院结算明细。

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeKet8MmMicoWCLU267d0l9JdataicibAEGe6mGlW4qWUygUxahvnppEEaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWevYJSeaE3Ak6mAvhic9Ccz1JGdliao70ibKB9mfCtkPAuzx9ibkWnuzYSmA/640?wx_fmt=png&from=appmsg)

上面刷了蛮多的数据分，可以准备搞点权限分，上线CS搞内网权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWeSJYujyTPvaTzcz52Hq10NvQibp1DDh1k2icTHZAsZXR1OjHibfRenhC1A/640?wx_fmt=png&from=appmsg)

通过提取到的登录凭证，直接远程上服务器

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAO4zEtzpibecsns2eVawcWevSKlL6Nl2n2S8Uo5iczSgcWmKrkpR60VPGZtfHzAeIfRzibMNyLcXPFQ/640?wx_fmt=png&from=appmsg)

成功登录远程桌面，由于运行了很多应用程序，服务器非常卡慢，为了不影响医院业务的正常运行，没有进行横向渗透，至此攻击已经结束，点到为止。

免责声明：本文章仅做网络安全技术研究使用！严禁用于非法犯罪行为，请严格遵守国家法律法规；请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。使用本文所提供的信息或工具即视为同意本免责声明，并承诺遵守相关法律法规和道德规范。公众号发表的一切文章如有侵权烦请私信联系告知，我们会立即删除并对您表达最诚挚的歉意！感谢您的理解！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmDlMCL9XS4knZK7fMB8PP0icibTDZqTM3CaibiaXviaRiaqBKQbibSmjVQSBLZicEAibLTj71eLmUEA3ASDWeA/0?wx_fmt=png)

十二主神

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmDlMCL9XS4knZK7fMB8PP0icibTDZqTM3CaibiaXviaRiaqBKQbibSmjVQSBLZicEAibLTj71eLmUEA3ASDWeA/0?wx_fmt=png)

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