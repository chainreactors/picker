---
title: APP中WebResourceResponse漏洞分析
url: https://www.secpulse.com/archives/198399.html
source: 安全脉搏
date: 2023-03-30
fetch_date: 2025-10-04T11:05:48.737983
---

# APP中WebResourceResponse漏洞分析

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# APP中WebResourceResponse漏洞分析

[漏洞](https://www.secpulse.com/archives/category/vul)

[编码安全](https://www.secpulse.com/newpage/author?author_id=48435)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-03-29

12,143

现在很多APP应用中都使用webview来进行页面的展示，甚至将webview做为主要显示组件，把所有的内容使用H5来呈现，同时webview也成为攻击者重点攻击的重要的攻击面。

webview它允许开发人员绕过标准浏览器安全性、WebView允许拦截应用请求并返回通过类实现的任意内容。恶意攻击者对这些功能的任何滥用都可能导致移动应用程序中的漏洞。

Webview的漏洞中包括了任意代码执行漏洞、跨域、密码明文保存等，这些安全问题可以直接导致用户敏感信息泄露，移动终端被恶意攻击者控制。

**基础知识**

webview使用过程中大部分是和html文件(javascript)打交道的。

**WebView使用的3个关键流程点：**

1、在界面中放置WebView控件；

2、在代码中设置WebView功能及需要加载的内容；

3、在APP配置中启用相关权限。

ResourceResponse是webview中的一个方法，它封装了Web资源的响应信息包括：响应数据流，编码，MIME类型，API21后添加了响应头，状态码与状态描述。通过从应用程序代码本身返回响应(包括状态代码、内容类型、内容编码、标头和响应正文)来模拟服务器，而无需向服务器发出任何实际请求。

**//拦截资源请求 [Android 5.0（API 21）及以上可用]**

**//request：封装本次请求的详细信息（包括url、请求方法、请求头）**

**public WebResourceResponse shouldInterceptRequest(WebView view,WebResourceRequest request);**

WebView在调用loadUrl后，会首先根据传入的URL获取响应，再将响应显示到页面上，这就是WebView的原理。

在获取响应过程中重新改变请求URL或者直接将响应替换。具体的替换在WebViewClient的WebResourceResponse shouldInterceptRequest (WebView view, WebResourceRequest request)方法中，该方法用于根据请求去获取响应，如果返回值为null，那么android会根据请求去获取响应并返回，但是如果重写了该方法并返回了响应，那么WebView就会使用你的响应数据。

对于资源方面，只要构造出一个包含目标数据的WebResourceResponse对象，并将其返回，就实现了资源的替换。在需要使用本地资源替换远程资源的场景中，这个回调方法非常有用。当然，如果直接返回null，WebView将会正常地加载url对应的资源。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198399-1680071151.png)

上面的代码中，如果请求 URL与给定模式匹配，则从应用资源或本地文件返回响应。攻击者就可以操纵返回文件的路径并通过 XHR 请求获得对任意文件的访问权限时，这就会存在漏洞风险。

如果攻击者发现一个简单的XSS或能打开Android应用程序内任意链接的能力，攻击者可以使用它来泄露敏感的用户数据，其中也可能包括访问令牌，从而导致完全帐户接管。

**漏洞分析**

在WebView中，容易出现的漏洞是执行任意javascript代码还有java代码的。

WebResourceResponse容易出现的漏洞点在于有2个关键点：

1、通过活动的WebView中打开任意URL

这个执行任意URL在android中一般存在AndroidManifest.xml和java代码中。在androidmanifest.xml文件中有 activity组件触发可以执行任意功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198399-1680071153.png)

构造一个自己的 WebResourceResponse，实现用APP应用包里的本地文件替换掉要请求的网络图片。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198399-1680071154.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198399-1680071155.png)

**2、通过webview中拦截web返回请求，可以对APP本地文件进行读取，从而存在敏感信息泄露风险**

文件读取漏洞是由于Android应用程序对用户输入的文件名称没有进行安全校验而导致的一种安全漏洞，攻击者可以通过构造特殊路径访问Android系统中的文件。

**小结**

WebResourceResponse这个函数存在一定的安全风险，建议使用WebViewAssetLoader，它用于简化通过请求拦截从应用数据目录中加载 APK assets、resources 和文件的过程。这样可以在不停用 CORS 的情况下访问网络和本地资源。

**本文作者：[编码安全](newpage/author?author_id=48435)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/198399.html**](https://www.secpulse.com/archives/198399.html)

Tags: [APP](https://www.secpulse.com/archives/tag/APP)、[Javascript](https://www.secpulse.com/archives/tag/javascript)、[Web](https://www.secpulse.com/archives/tag/web-2)、[WebResourceResponse](https://www.secpulse.com/archives/tag/webresourceresponse)、[webview](https://www.secpulse.com/archives/tag/webview)、[漏洞](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | 同源策略的绕过](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/a799223d33bd92e8b0620d8ad38ecd2.jpg)

  代码审计 | 同源策略的绕过](https://www.secpulse.com/archives/203439.html "详细阅读 代码审计 | 同源策略的绕过")
* [![云原生安全联防联抗策略玩转微隔离](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/1694157547520-300x155.png)

  云原生安全联防联抗策略玩转微隔离](https://www.secpulse.com/archives/203414.html "详细阅读 云原生安全联防联抗策略玩转微隔离")
* [![从2023蓝帽杯0解题heapSpary入门堆喷](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693450185258-300x157.png)

  从2023蓝帽杯0解题heapSpary…](https://www.secpulse.com/archives/203218.html "详细阅读 从2023蓝帽杯0解题heapSpary入门堆喷")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/08/1659521180.jpg)](https://www.secpulse.com/newpage/author?author_id=48435aaa) | [编码安全 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)](https://www.secpulse.com/newpage/author?author_id=48435) | |
| 文章数：12 | 积分： 20 |
| 编码安全、安全编码！ 公众号《编码安全》 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)

#### 2020-12-11

[全球敏捷运维峰会（Gdevops2020）](https://www.bagevent.com/event/6243820?bag_track=AQMB)

#### 2020-12-04

[2020京麒网络安全大会](https://www.huodongxing.com/event/5569026023500)

#### 2020-11-29

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp.weixin.qq.com/s/kXt5PAD3bPcHUZjl6rziCw)

#### 2020-11-27

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.co...