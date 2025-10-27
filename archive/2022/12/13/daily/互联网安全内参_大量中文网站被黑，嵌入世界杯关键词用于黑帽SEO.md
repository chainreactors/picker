---
title: 大量中文网站被黑，嵌入世界杯关键词用于黑帽SEO
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507062&idx=3&sn=22ec18fc965293668c393c20e0aadc36&chksm=ebfa9b56dc8d12400b1e9ad924f308f430e3baf1b8c78d77a577b465690d8a5efda80d430af4&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2022-12-13
fetch_date: 2025-10-04T01:19:15.417503
---

# 大量中文网站被黑，嵌入世界杯关键词用于黑帽SEO

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7toGMibNbfXAs9QJ9UDlJPVQO41VQXSUdZx9Mjjll6TUial4GvHzeGrjC0KzXxfiahX1mSiajhBlicnroA/0?wx_fmt=jpeg)

# 大量中文网站被黑，嵌入世界杯关键词用于黑帽SEO

安全内参

**关注我们**

**带你读懂网络安全**

在黑帽 SEO 中，经常会出现的是被黑网站的 `<title>`标签被修改为中文关键词，使搜索引擎的检索结果中明显可见。但如果使用浏览器打开时，则会显示原始未修改的标题。

黑帽 SEO 经常会推广中文的赌博、体育彩票类网站，研究人员发现此类攻击已经产生了巨大的影响。根据 PublicWWW 的数据，失陷的站点数量应该已经超过 5 万个。近期，攻击者开始利用世界杯作为话题进行引流。

##

## **嵌入世界杯关键词**

## 最近，很多失陷网站都更新了关键词，主要是与 2022 年卡塔尔世界杯的标题。

> 卡塔尔世界杯赛事分析·(中国)世界杯赛事中心
>
> 2022世界杯买球投注-世界杯安全买球网站【官方平台】
>
> 世界杯赛事预测世界杯在线直播世界杯赛时间 – 体育新世界

重定向的站点通常也是世界杯相关主题的，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscrLqX9bZmvDAUev2ah30jEpUGK8JXAKbAdK3icOZ7tZqcjCZfCakyVjdQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)*【重定向网站】*

检查失陷网站的 HTML 源代码，其中 `<title>`与 `<meta>`中有很多关键词：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscreRjxXQyEyNUYshqmlE4SVsO4gicgrU852SSpmQ2wpp0n2dNEpOm5Zaw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)*【失陷网站的标题】*

这些 HTML 实体使用 UTF-8 中的字符代码表示 Unicode 字符。以 title 标签为例：

> <title>&#19990;&#30028;&#26479;&#22806;&#22260;&#32593;&#31449;&#45;&#105;&#111;&#115;&#47;&#23433;&#21331;&#47;&#25163;&#26426;&#29256;&#97;&#112;&#112;&#19979;&#36733;</title>

解码后汉字为 `<title>世界杯外-围网站-ios/安卓/手机版app下载</title>`。

##

## **title 切换**

使用浏览器打开失陷网站时，就看不到与赌博和世界杯相关的内容。攻击者使用的 HTML 脚本会检查访问者是不是中文搜索引擎爬虫，即时将 title 修改为原始内容。

目前在失陷网站上部署了两个主要的变种：

###

### **只匹配百度的爬虫**

```
<script>if(navigator.userAgent.toLocaleLowerCase().indexOf("baidu") == -1){document.title ="<real site title>"}</script>
```

## （向右滑动、查看更多）

###

### 匹配包括百度在内的其他爬虫

```
<script>if(!navigator.userAgent.match(/baiduspider|sogou|360spider|yisou/i)){document.title ='<real site title>'}</script>
```

## （向右滑动、查看更多）

在某些站点上，还发现了其他脚本，这些脚本会控制页面内除了 title 以外的其他内容切换。

##

## **范围与影响**

## 在撰写本文时，PublicWWW 在 50172 个网站上发现了第一个脚本，在 14010 个网站上检测到第二个脚本。

看似已经很多了，但实际上相比前几年超过十万的规模已经收缩了不少。而且失陷网站大多数是中文网站，在全球其他地方的曝光度较低。

##

## **赌博网站重定向和混淆脚本**

## 攻击者还使用了几种不同类型的重定向脚本。最简单的重定向脚本没有经过任何混淆，检查访问者是否来自搜索引擎，满足条件的重定向到赌博网站。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscrjrXVQDMO5gnwJKgqo8TCibQbWTWFXtczicpN2qXg6iaBkDCqTHQrcBR0g/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)*【没有混淆的重定向脚本】*

还有经过混淆的脚本，如下所示。解码后，可以得到外部链接 `hxxp://tongji.68010[.]com/4/tzm.js`。

*![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscrBf2hGzcLA8F3FmUwzAQ2MwkEOv2rFEJ8gMNAqTZTffSG3ICDqUtCAg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)【使用 HTML 实体进行混淆】*

还有攻击者常用的 eval 混淆方式，如下所示。解码后，可以得到外部链接 `hxxps://www.makeafortune88[.]com/bb.js`。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscrWIlNScxdkKqnCrVrImxA10GYgIyNia0kEXR3YsaeOyiciafLm7Uc7iaoZQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)*【eval 混淆】*

##

## **外部链接**

外部链接也有多种变种，如：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscrS1ic2Q72emFs7JKPsRO7ZS2ZWSgXWlrEpLIddAT3jN0PM9Y7xOPS9mg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)*【外部链接变种】*

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscrfw5DYZBDYWvMXxrXZibhFBuRtbaic83Ixo3bMWjk4XV3eqrVTnSnIndw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)*【外部链接变种】*

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscrbZXKPvm8QLElfcU938ardFk6tWtwWKF4w9Sp7icjyE6FRZa6FiaGNRWQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)*【外部链接变种】*

在满足特定条件时，将访问者重定向到赌博网站。也有部分外部链接是针对移动设备的：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscrMrtVgo8v9ib5QjQEiahYbAvF8v6LlV2geBvK3EbKxEYVdAEUzaZ76WkA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)*【移动设备重定向】*

脚本中会预制许多赌博网站，将用户重定向到其中之一。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscr0icDJ5L1sVqVIueexfKYxbIicBtSLAPSbZlleE0N8yibnTvDRQcbCpT9Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)*【多个网站】*

攻击者利用百度的自动推送功能，提高攻击效率。每当访问者打开失陷网站时。脚本都会向百度发送将 URL 添加到索引中的请求。注：百度站长服务平台在 2020 年 12 月宣布停用自动推送功能。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39UZMnNxDiaQLs0ebEXGpscrr0LGb5VSlWCCIYm7oXZlOjW6jPherTn6HiafUa2KCZnYnBNmpu8RD2A/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)*【搜索引擎诱导】*

##

## IOC

> 154.38.227.98
> www.tbty20000[.]com/tb.js
> www.niubjsc20226688.com/tbsjb.js
> 154.22.124.28
> qitasjb2022[.]com/yb.js
> sjb2022ky[.]com/yb.js
> qitajs1002[.]com/yb.js
> ybjs0726[.]com/yb.js
> ceshi963ly[.]com/yb.js
> 154.222.103.43
> tongji.68010[.]com/5/tzm.js
> 155.159.144.129
> diltsportajohn[.]com/shell.js
> 128.14.75.59
> www.ly66666[.]vip/ly/ly.js
> www.telegeramguanwangfangwangzhan20220924[.]com/telegeram/telegeram.js
> 206.119.125.190
> www.makeafortune88[.]com/bb.js
> www.makeafortune66[.]com/bb.js
> www.bobsjb2022[.]com/bobsjb.js
> 206.233.132.188
> www.sjb4[.]cc/bob.js
> www.ag857[.]cc/ag.js
> www.sjb2[.]cc/bob.js
> www.sjbs[.]cc/bob.js
> www.ttdbty[.]cc/bob.js
> 143.92.32.243
> www.yigexiaomubiao2022[.]com/bb.js
> 23.248.203.3
> www.360360365[.]com/360.js
> efhfuh[.]com/365.js

##

## **参考来源：**

> https://blog.sucuri.net/2022/12/chinese-gambling-spam-targets-world-cup-keywords.html

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：FreeBuf

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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