---
title: PbootCMS V3.2.9前台SQL注入漏洞（上）
url: https://mp.weixin.qq.com/s?__biz=MzkyNzcxNTczNA==&mid=2247486791&idx=1&sn=b6b5c31b8ace0a9aeec45c44ad2f5e53&chksm=c22295bef5551ca8792a4995840335057e593dac6cedff9883e4df8636af25be9d78a176ab3f&scene=58&subscene=0#rd
source: Beacon Tower Lab
date: 2024-12-18
fetch_date: 2025-10-06T19:43:01.646208
---

# PbootCMS V3.2.9前台SQL注入漏洞（上）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8E5sfrfkeANYufl21GnC2piaqMNeFYI5uJFviaSia2CPSscWrPavrfj2AU2NbsJGzOfQ0gQGUPtMicUIaNjeyzbZvQ/0?wx_fmt=jpeg)

# PbootCMS V3.2.9前台SQL注入漏洞（上）

原创

烽火台实验室

Beacon Tower Lab

**0x01 前言**

PbootCMS是全新内核且永久开源免费的PHP企业网站开发建设管理系统，是一套高效、简洁、 强悍的可免费商用的PHP CMS源码，能够满足各类企业网站开发建设的需要。系统采用简单到想哭的模板标签，只要懂HTML就可快速开发企业网站。官方提供了大量网站模板免费下载和使用，将致力于为广大开发者和企业提供最佳的网站开发建设解决方案。

PbootCMS在国内有非常大的客户使用量，属于国内最流行的企业官网建站程序。截止本文发出前，其github最新版本为V3.2.9。通过互联网资产测绘平台搜索指纹header="PbootCMS"，搜索结果有超过34W+互联网案例。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5uGDibFial1H6l6G9Wh2hgzzzph479t3LhU5lBPNTwrPtECao4btj95OXQ/640?wx_fmt=png&from=appmsg)

在最新版的PbootCMS V3.2.9中存在前台未授权SQL注入漏洞，攻击者可以通过此漏洞读取系统数据库中的敏感信息，包括后台用户的用户名和密码。

**0x02 漏洞分析**

之前因为某任务进行批量任务扫描时发现很多目标都在报DVB-2021-2510漏洞，其POC大致如下，返回数据匹配到your SQL syntax或syntax error。

```
POST /index.php?p=search
1=select
```

此漏洞是很早以前已经曝出的安全漏洞，对应CVE编号为CVE-2021-28245，但是最大的问题是我在最新版本的V3.2.9上测试仍然存在此漏洞。也就是官网一直都没有修这个漏洞，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5uUusLRNCrAaCdNumZBLLUSS1grnAGps4M0iaVsqpJ2yCicSrfoKc5QfbA/640?wx_fmt=png&from=appmsg)

由于ddpoc上面的这个脚本主要做poc探测和验证，并不带直接的漏洞利用，需要跟踪源码分析漏洞逻辑。跟踪到漏洞对应的文件apps/home/controller/SearchController.php。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5usa4RqcQhpRJ36adeVbYCJJ5iawdgGfW7YGQvcibmcqLibicPXOkzLRFt3Q/640?wx_fmt=png&from=appmsg)

PbootCMS有一套复杂的模版替换的逻辑，其中模板替换分成多个步骤，在SearchController类中会通过parserSearchLable方法对模板内容进行解析，跟踪parserSearchLable方法。parserSearchLable方法逻辑很复杂，我直接定位到最关键的部分如下。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5u5sSc7alsgX1QhEqwCDuT8bic8APR5bFCAibDmWbRRkzoUTqYYgCkmkSA/640?wx_fmt=png&from=appmsg)

其中$receive来自于外部输入，遍历$receive变量，会生成新的数组$where3。$where3是后期漏洞利用的关键，但是这里先关注$value = request($key, 'vars')，看一下这里对数据的过滤逻辑。跟进request方法。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5ujMz0YPSW74kkGWRgTJy573SEUV061rVzeBPuLOSUjd78loVBmGhyAg/640?wx_fmt=png&from=appmsg)

跟进filter方法，如下图所示，当传入的d\_type(也就是request方法的第二个参数)为vars时，只能包含中文、字母、数字、横线、点、逗号、空格！。而这也为后面的SQL注入的利用埋下了伏笔。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5uPX6fWLs0CUib5LcMrSOczPoqoLUJnNUQbCAmffibU90829j00uBP8kmA/640?wx_fmt=png&from=appmsg)

回到刚才提到的$where3变量，$where3变量会传入getList方法。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5u59YMbVYo6gPruFJcdfE0ib5HibLYibgOMiazlHllp6jib0PTQKcxku2ib19Q/640?wx_fmt=png&from=appmsg)

继续跟进getList方法，传入的$where3传入到变量$select。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5ul1xXJXnr9lqONeET4q1yGJ8ets5YAJNBJRIH88wG21icob91TjQKyGg/640?wx_fmt=png&from=appmsg)

跟进变量$select，如下图所示，可以看到其中的$select传入了where方法，这个方法是用于组合SQL语句的查询条件。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5uvcwaHHxHaITkkLM4aA6dBQEh7cjp7Sia6qvlviaibN86S1gnyMNwSYlCg/640?wx_fmt=png&from=appmsg)

继续跟进where方法，如下图所示。当$key也就是传入的数据是一个整数时，会直接拼接$value的值，导致SQL注入漏洞。这里为什么不用$key来注入呢？因为$key前面的图里面有限制，只能输入\w\-\.，不允许空格和特殊字符导致无法直接利用此注入点。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5uyL3lzdkdFM8YoOsBaHUUlPxdiagKskz0fbFJic3ee3MDDVz9ABlkq2Xw/640?wx_fmt=png&from=appmsg)

**0x03 漏洞利用**

漏洞的整个流程已经梳理清楚了，下一步就是漏洞如何利用的问题了。这里由于request($key, 'vars')限制导致不能使用特殊字符。不能使用括号、单引号、注释和逗号会极大的限制整个漏洞的利用方式。

为方便大家直观看到SQL语句效果，我临时把SQL语句打印出来，如下图所示，大致是直接在括号中拼接SQL语句。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5u61ibefIMNHYyw34sv8EUjFLb9pBSw0LNdu1K23x1AQqkPQ0XiaQsXMIw/640?wx_fmt=png&from=appmsg)

只能使用\w和空格的注入，极大的限制了注入点的利用，但是仍然可以通过BOOL盲注的方式来达到注入的效果。

1)  使用下面的payload访问目标，显示有搜索结果

1=select 1 from ay\_user where username like 0x6125 limit 1

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5uqmicF4m1dbYNchdrP7GkHotLIdKThadicNH3Xldgqqzf5PXkVsJ9ia3NQ/640?wx_fmt=png&from=appmsg)

2）使用下面的payload访问目标，显示无搜索结果

1=select 1 from ay\_user where username like 0x6225 limit 1

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANYufl21GnC2piaqMNeFYI5uYz63wANvDbfOAMCrj30hCwJ1CdNcxAkXO0AiccFIrjLgib5onTyqsNgQ/640?wx_fmt=png&from=appmsg)

由此可以证明目标站点ay\_user（管理员用户表）第一个用户的username的第一个字母是a（第一个用户默认一般是admin）。

这里很巧妙的使用mysql的like语句支持16进制编码的特性来避免使用其它特殊字符，但是整个利用过程还是有下面的注意点：

1）仅支持PbootCMS安装选择mysql数据库的网站，PbootCMS默认情况下使用的是sqlite数据库，如果是sqlite数据库，暂时不知道如何在不引入特殊字符的情况下进行注入。

2）因为不能使用逗号，所以不能通过limit 1,1这样的方式来注第二个用户，但是可以通过增加条件的方式来进行注入，例如下面的payload

1=select 1 from ay\_user where username like 0x25 and username not like 0x61646d696e25 limit 1

**0****x04 结论**

DVB-2021-2510（CVE-2021-28245）是一个很好的漏洞，互联网案例足够多，影响大。这是一个经典的有条件的SQL注入漏洞，值得小伙伴们学习研究。

*在下一篇文章中，作者会带来PbootCMS更多有意思的漏洞和利用方式。*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAPuXuLlzxV94SmGrdhm12Xoib8pv5tVryyDTMZPUwvOeXrHV2ygdoKrKJQ1u618rmXbhfhiaw8icr5Lw/0?wx_fmt=png)

Beacon Tower Lab

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAPuXuLlzxV94SmGrdhm12Xoib8pv5tVryyDTMZPUwvOeXrHV2ygdoKrKJQ1u618rmXbhfhiaw8icr5Lw/0?wx_fmt=png)

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