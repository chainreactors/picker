---
title: 五种用来挖掘API端点的方法
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496248&idx=1&sn=0e1539ba41254dbaf054f0a3e05f53f4&chksm=e8a5f85bdfd2714db9230c75f9cb4d546ce23feff621d10478f13d849969587dc2196fc33f7c&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-11-01
fetch_date: 2025-10-06T19:18:12.897441
---

# 五种用来挖掘API端点的方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hZj512NN8jmdFQQeSvAdMibfnMXI9URGaUw5kOx2DZu1eJ05jRRzJ3DmKST4dfnuc7v7cKZk3DOU8P8bfUCgeiag/0?wx_fmt=jpeg)

# 五种用来挖掘API端点的方法

迪哥讲事

以下文章来源于骨哥说事
，作者骨哥说事

![](http://wx.qlogo.cn/mmhead/Tjnia6K0WAwzfic3VPt0EfMjicnGXzicDLoHEqtz1cP3Iozxf1tSyMxCFNG9Aya8SziaVKhVw7ia6QugE/0)

**骨哥说事**
.

一个喜爱鼓捣的技术宅

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

* 简介
* 方法一：API文档
* 方法二：公开源信息（OSINT）收集

+ Google Dorking
+ Wayback
+ Postman
+ Github

* 方法三：应用程序的HTML与JS
* 方法四：APP应用分析
* 方法五：主动扫描与Fuzz

# 简介

在渗透目标时，最值得测试的部分莫过于 API，API 是动态的，它们比应用程序的其它部分更新的更加频繁，并且负责许多后端繁重的工作。在现代应用程序中，我们通常会看到 REST API，当然也会有其它形式，如 GraphQL 甚至 SOAP。

当第一次接触目标时，通常需要做大量的前期研究，以了解其主要功能以及‘幕后’的工作方式，例如，如果要渗透一个租赁应用程序，那么一开始最好阅读有关该公司的服务（租赁、销售、支持、折扣等），在了解目标服务后，寻找其应用程序中的相应功能然后尝试渗透它们。

# 方法一：API文档

如果渗透目标的应用程序提供了可用的 API 文档，如 Swagger 或 WSDL 文件。而且文档提供了公开访问或曾经提供过公开访问，那么阅读API文档无疑是最好的手段，我们可以通过API文档了解到：

* 特定端点希望要求什么类型的数据（整数/字符串、JSON/XML、POST/PUT/GET 等）
* 需要发送的标头有哪些
* 从请求中会得到哪些响应
* 特定端点所需的身份验证级别

Request：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmdFQQeSvAdMibfnMXI9URGaACfnZ7peFh4S9fsYXD4gkpGQAEWaGkh5pevkQYLPgvjVic4eCR5hXMg/640?wx_fmt=png&from=appmsg)

Response：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmdFQQeSvAdMibfnMXI9URGaLK899olnsfIUppnkY86EQZ3cXiaiaJL4ib8JMGmK4gqQZLcNY5sj6NlaA/640?wx_fmt=png&from=appmsg)

# 方法二：公开源信息（OSINT）收集

开发人员不断开发 API，并可能使用不同的工具来构建、测试和记录不同版本的 API，那么我们就有可能发现应用程序 API 的旧版本，那么这些旧版本可能就不如当前生产版本的安全性那么高了！

## Google Dorking

结合使用 Google 的高级搜索选项和一些 API 关键字，通过快速的 Google Dorking 搜索可以为我们带来：

* 与 API 相关的目标子域
* 目标 API 文档页面
* API 端点——旧版本与当前版本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmdFQQeSvAdMibfnMXI9URGa8XQyicEgGmNjElQH9IoUugSIHyibcphiaXY8VK1CvqwEkhZONTCnGRvIA/640?wx_fmt=png&from=appmsg)

Google Dorking语法举例：

```
site:target.com inurl:”/v1"
site:target.com inurl:”/api"
site:target.com inurl:”/graphql"
site:target.com intitle:”api*”
```

## Wayback

WaybackMachine 是用于发现 API 端点并同时获取一些‘秘密’的最出色工具之一，通过它我们可以在特定日期查看目标页面，更加厉害的是，我们还可以在 GET 请求中获取 URL 列表，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmdFQQeSvAdMibfnMXI9URGaWfBX8ia8ZournhZlGssFpXnF371dSsrG5jCE8qGR3FnlicqMODSVfAUA/640?wx_fmt=png&from=appmsg)

只需搜索目标的域名并过滤“api”，我们就能够得到了一些 API 端点，甚至包含 GraphQL。

如果查看公司的更多子域，有可能会看到更加多的 API 端点，在这些端点中有时甚至能够找到用户名、Token、身份验证密钥和 JWT 等信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmdFQQeSvAdMibfnMXI9URGapLtEWAgicFEDBcyKo2EnHqep93ydIjsOhc5OxAnrClXHBYGljpYSHdg/640?wx_fmt=png&from=appmsg)

使用这些找到的信息，可以测试具有不同用户权限授权的API端点，另外，强烈建议将GAU或Waymore集成到你的‘侦察；自动化工具中，以便找出更多API端点。

## Postman

这是开发人员测试 API 最常用的工具之一，无需前端界面就可以发送请求，而且比使用 Curl 方便很多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmdFQQeSvAdMibfnMXI9URGaicUVLEYxK83BgUEDr26TgGOUknibq7A6tKticXqFmBrTTzb9rX8ac5IxQ/640?wx_fmt=png&from=appmsg)

如果运气不错，能够拿到目标的Postman Collection信息，那可能要比找到官方 API 文档还要棒，这些信息可以帮助我们了解更多有关应用程序内部环境和目标底层核心的信息，其中最好的部分之一就是具有查询后端的高权限凭据信息！

## Github

如果目标有一个可以公开访问的 GitHub 存储库，那么花一些时间研究应用程序的源代码总归是一个不错的主意，通过一些关键字，我们将最大限度地找到 API 端点及其工作原理的详细说明。一些常用的关键字：

* /v1
* /api
* apikey
* api\_key
* apidocs
* api\_secret
* x-api-key
* /graphql

# 方法三：应用程序的HTML与JS

除了查看页面源代码和F12大法外，还可以利用一些插件或工具帮我们自动化寻找API端点信息，比如：Findsomething（插件）、Katana等。

通过查看 HTML 和 JS信息，有时可以找到大量隐藏的API端点（影子API），影子 API 一般很少暴露，因此它们往往具有更高的潜在漏洞！

# 方法四：APP应用分析

如果目标有移动应用程序（APP），那么就有可能提供一些专门针对手机的功能，比如通过 GPS 获取精确位置。那么在这种情况下，就意味着 Web 应用程序的 Javascript 中存在的 API 与 APK 文件中存在的 API 端点可能会有所不同。

通过反编译APK（Jadx、JEB2等）或者一些移动APP的自动化平台（APKPure、MobSF等），可以方便的收集到在APP中的一些硬编码、URL、子域、API端点等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmdFQQeSvAdMibfnMXI9URGa0OCxYicIN7DaCZpwhFdagYnOHGibPVIgpgThjtdibu1ktKmN297cEA9cA/640?wx_fmt=png&from=appmsg)

# 方法五：主动扫描与Fuzz

对于API端点Fuzz，常用的工具包括 Burp Intruder、FFUF、GoBuster、Arjun、Kiterunner 等，当然我们也可以打造属于自己的模糊测试器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmdFQQeSvAdMibfnMXI9URGaMAoib6Jvcb0aG14tNsuA0vySD7A1kOq4YORE7XVV2vENSvqD6fyEgPw/640?wx_fmt=png&from=appmsg)

Kiterunner 命令示例：

`./kr scan https://target.com -w ~/wordlists/routes-large.json`

拥有强大的字典是Fuzz成功的关键，以下是一些不错的字典：

SecLists

Assetnote

FuzzDB

另外，我们也可以利用强大的ChatGPT为我们生成一些字典组合，比如“汽车租赁”的组合字典：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmdFQQeSvAdMibfnMXI9URGaSPW9PiaySbiaXFb48fzRnX7icUH3COlolSAsRXApTESuzZRwLSBiasppsA/640?wx_fmt=png&from=appmsg)

希望以上内容能对你有所帮助。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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