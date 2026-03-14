---
title: 新手小白入门SRC漏洞信息收集分享
url: https://mp.weixin.qq.com/s/ni4sHQS8eoXlO0R3HdAmuA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:04:34.480511
---

# 新手小白入门SRC漏洞信息收集分享

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/niasx7fyic9CPKxIjYoiaEI5W2Zt0hEoygmStttXwziakHIibIyZxKicw6URYwx5mhoh73NxuhibGlDDVYKN7GZPTc1rZNT0dIr3IbG1lj37Xv2kIM/0?wx_fmt=jpeg)

# 新手小白入门SRC漏洞信息收集分享

小智
小智

C4安全

![]()

在小说阅读器中沉浸阅读

**信息收集**

在SRC漏洞挖掘过程中，保证在最短时间内提交”有效”漏洞，自我总结漏洞数量主要来源于三个方面：

一、资产收集；

二、学会使用自动化工具；

三、通过数据包仔细审查业务逻辑

。

资产收集作为漏洞挖掘第一步，资产收集的广度，会直接影响漏洞的数量，所以资产收集尤为重要。

这里简单介绍一下资产收集的有关小工具以及方法。

### **1.1子域名收集**

子域名收集推荐几个比较好用的工具:

**一、Oneforall**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CM0CuSBal49v9pN9jqVPLhCoFn0J6SxiamvEls6ic30icAGOkDYkWDDib760rXh83mbIIqGTPj1zHBcESg08kzBVf39gsGaYCR7Nrk/640?wx_fmt=png&from=appmsg)

项目链接：https://github.com/shmilylty/OneForAll，Oneforall是一款强大的子域名收集工具，适用于SRC资产收集

使用方法：python3 oneforall.py --target baidu.com run

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COMd12oWEr8I1pBnLSHzgYzsRJ7yT38RNSXAap5sFJsLzlZDznsKicd27RnQ1J4AQYIyKkDlSnDzOD68Penf1ibyVl9fBcjeVFsk/640?wx_fmt=png&from=appmsg)

**二、在线子域名收集工具**

地址:https://tools.yum6.cn/Tools/urlblast/

在线子域名收集在漏洞挖掘过程中快速收集到第一手资产信息（可能会有以外收获）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPdnJEQrUiboOMzSJVmJUoG0dnL4AClkkTamA5gicBicwZwHqdEpzic4fMY8IrnlXqko9ib1pFaoShzAlxrwmibNVWwL3wXPkicREDvQc/640?wx_fmt=png&from=appmsg)

1.2.搜索引擎

挖洞过程中好的搜索引擎可以更快的获取高质量的资产信息，这里推荐两款用的比较多的也是比较好用的资产搜索引擎。

一、Fofa

地址:https://fofa.info/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPy5FoJ0PmPLYCpzpIickjX4N3EAVELwm1H5ZODKWjiaSbM0pxrm6NvtnklB2icXZarAm2vbfyBkWYt00NCKRngicoc5v6NLB4CHrc/640?wx_fmt=png&from=appmsg)

Fofa支持与谷歌黑客语法类 似的搜索语法，在网页内可以查询检索语句的使用方法，这里就不做过多的介绍。

二、谷歌黑客语法

这里的Google语法通常是指通用的网络搜索语法，对于黑客而言，网络搜索就可能变成绝佳的黑客工具。

正因为检索能力的强大，黑客可以构造特殊的关键字语法，使用不同搜索引擎互联网上的相关隐私信息。

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNyKJWX1TLMTS9qM6jFU4zVmjwfQoXI1Qa79ibnOEf9ibDxX6xt75a5vR0ibYGJhKqYAfibt5OBlmj2M3vFmjSnF9JR91iaVNUFUcE0/640?wx_fmt=png&from=appmsg)

这里简单介绍一下谷歌黑客语法的使用技巧，仅作简单介绍，详细使用建议自行百度。

intitle：搜索网页标题中包含有特定字符的网页。例如输入“intitle:上科互联”，这样网页标题中带有上科互联的网页会被搜索出来。

inurl：搜索包含有特定字符的URL。例如输入“inurl:/admin\_login”，则可以找到带有admin\_login字符的URL,通常这类网址是管理员后台的登录网址。

intext: 搜索网页正文内容中的指定字符，例如输入“intext:上科互联”。这个语法类似我们平时在某些网站中使用的“文章内容搜索”功能。

Filetype: 搜索指定类型的文件。例如输入“filetype:PDF”，将返回PDF文档。

Site：找到与指定网站有联系的URL。例如输入“Site:www.sunghost.cn”。所有和这个网站有联系的URL都会被显示。

1.3.端口扫描

端口扫描也是常规信息收集中最重要的一项，在之前的很多的SRC漏洞挖掘过程中，很多时候遇到同一个ip开放不同的端口，对应不同的WEB服务，很多时候漏洞往往存在一些花里胡哨的端口服务上。

这里推荐一款端口扫描工具Nmap，Nmap功能比较强大，不仅可以支持端口扫描，资产存存活探测也可以使用其自带的漏洞探测脚本，对漏洞进行探测。

Nmap

下载地址：https://nmap.org/，这里推荐使用图形化界面的，也可以使用现在网上的一些端口扫描工具如小米范端口扫描工具等等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNMCmrhQqQmeHPolWsUd4iaVITkZrhbrefddr9IPPWyUfviaaruFv3K7Dia0qIxPmn38v8EtRc91HjkrN2cY1tzaPWfluyyD42G64/640?wx_fmt=png&from=appmsg)

1.4.指纹识别

通过指纹识别可以快速了解搭建网站使用的什么内容管理系统，以及网站使用的框架信息（CMS：织梦、帝国、XXXOA等等；网站框架：Nginx、Spring boot、Apache、IIS等等）。

这里推荐两款比较简单方便的指纹识别工具。

一、潮汐指纹库

潮汐指纹识别库是由，tide安全团队开发的一款开源的指纹识别库。

地址：http://finger.tidesec.net/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPRv7kOnQOicLOABNpf8Xibp8YZVGBWgfF57zLxP52kbC5sf6mtAfd9SGYqfl5n8NuaIA3jhicqUA4bjs1Y8nMm1licaErsE0KBh5w/640?wx_fmt=png&from=appmsg)

二、火狐浏览器自带插件Wappalyzer

下载地址：https://addons.mozilla.org/zh-CN/firefox/search/?q=wappalyzer

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNHuVD9GLc6xVwMfBZibWg7HakH2QHzP1BMs8xJ9eHdQQjOXsGyib2JLib3U5RGCibmcUnbxbYAx5SdRnpYericZmptZ04nWBrJD1FM/640?wx_fmt=png&from=appmsg)

可以分析当前网站使用了哪些技术搭建

1.5.目录扫描

通过对网站url进行扫描可以收集一些网站的资产信息，在后续的漏洞挖掘过程中提供更多有价值的信息（如：网站源码文件、网站安装页面、网站后台管理页面、接口信息页面（swagger ui、api接口等等）、未授权访问页面）。

这里推荐一款常用的目录扫描工具。

Dirsearch

项目地址：https://github.com/maurosoria/dirsearch

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CM6qKwLmVicHN6bcfic8fGXsmKrj0CyYhJTLOunw8fNDkdLbdbgRrlV1s0y5r1rVlD9Kn9myhu5JXeyYHxFJUkrPl520fkQ7T1Zk/640?wx_fmt=png&from=appmsg)

2.1.漏洞扫描

在漏洞探测方面可以使用扫描器（但是得根据客户需求），一般主流的漏洞扫描器如：Goby、Xray、Awvs、Nessus，这里可以使用Goby同时做信息收集和漏洞探测（信息收集功能会比漏洞探测功能效果好）。

2.2.Burp

Burp在漏洞挖掘中使用最广泛，也是最重要的工具之一，可以用于漏洞验证以及漏洞挖掘，由于开源，之前在挖掘漏洞中遇到一些比较有意思的漏洞，这里就用文字简述一下。

越权：越权漏洞简单分为垂直越权、水平越权，可以修改数据包中的一些参数如uid、id等等，遇到过一个比较有意思的垂直越权可以在低权限登录状态下通过修改数据包中路径信息可以访问到高权限的内容。

逻辑漏洞挖掘：逻辑漏洞，通过数据包查看业务逻辑，检查是否存在绕过正常的业务逻辑对正常的业务系统造成影响，分享一个之前某银行业务逻辑漏洞挖掘，漏洞点存在于选择支付方式可以通过修改数据包参数绕过指纹支付和脸部识别支付，逻辑漏洞挖掘推荐B站观看”月神”逻辑漏洞挖掘

这里简单介绍几个比较好用的Burp插件:Fakeip（可以在请求头中加入XFF头）、chunked-coding-converter-master（分片上传可以绕过部分waf如安全狗等等）许多漏洞检测插件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COZufPtBbQ7frSlPWvZu8ziaKYTsBNUT38jg8NJ4fZhqCWS1FAgHbfxWpzjazlmZIQicJVXsr2dq7ZHwiaKlyOk1hBTbArMIemMgY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COZvJiaGUKpIY9SFLzPVAQdmqSTtDvO0YHZPC6IIiaTTmjVHEvD5yrEicmiamHLvDib9vLs2peEnsbs7HzaMPXZmibQzc9X7onUjY1pM/640?wx_fmt=png&from=appmsg)

专业的国内网络安全AI社区平台推荐

https://www.wwlib.cn/

50免费积分兑换码：WUWEN\_1u7CcAHUVEb1W9VlVs

兑换地址：https://www.wwlib.cn/index.php/gift

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CP0icicvZkFgEpM5R0Ticn7P5WspdGXzGAAY63XQCoMA41bk8pP7gpYSaJ4MNbvUSfBRoZkf474qvWBtfy1uI5fvSYoeMaRy36ic0w/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic#imgIndex=0)

**团队内部知识大陆链接如下，折扣优惠中~**

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPicQX8MHjzewMCRYluC7bDzVnAC75SsLS6G5u6Qk43icTuN7CwbIz2rKmPZibhCIANfpjYESLa3iaic5ibXe2DhfFvlGgKQA4XIsGlI/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=6)](https://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247489224&idx=1&sn=1636373219018f238c7b2b866f1032ea&scene=21#wechat_redirect)

##

**永久帮会内部技术交流群**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/niasx7fyic9COCkUfSeoNxUnEOKvzLL2yNgR3GuDASvdBuDuCBuHGibv8c6cmn5eBe4g5wCoK2I67arXsyPDMjluHp7y9SbAmhfvjoqqVoDTZY/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=7)

✅ 如果你刚刚入门、对挖洞有兴趣却无从下手；

✅ 如果你不想再被割裂的信息、过时的教材所困；

✅ 如果你想在真实环境中练手并与同行共同成长；

那么你一定不能错过「安全渗透感知大家族」。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

C4安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

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