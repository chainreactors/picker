---
title: 渗透测试中的 URL 重定向
url: https://www.secpulse.com/archives/196033.html
source: 安全脉搏
date: 2023-02-18
fetch_date: 2025-10-04T07:19:57.594089
---

# 渗透测试中的 URL 重定向

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

# 渗透测试中的 URL 重定向

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[信安之路](https://www.secpulse.com/newpage/author?author_id=49490)

2023-02-17

12,970

> 本文为信安之路内部 wiki 第 144 篇文章，注册解锁全部文章

开放重定向（Open Redirect），也叫URL跳转漏洞，是指服务端未对传入的跳转url变量进行检查和控制，导致诱导用户跳转到恶意网站，由于是从可信的站点跳转出去的，用户会比较信任。

### 渗透测试中的 URL 重定向

常见的 URL 重定向漏洞都比较明显，但是也有少数例外，这里总结了三种常见的 URL重定向类型。

#### 类型一：基于参数的 URL 重定向

这是最常见的，通过修改参数中的跳转地址，查看是否重定向到我们指定的页面，比如：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196033-1676612269.png)

#### 类型二：恢复原访问页导致的重定向

通常为了提高用户的体验，在用户登录之后，往往会跳转至原来的访问页面，比如：

> https://example.com/login?returnUrl=/dashboard

登录之后会跳转至 /dashboard，并且是以登录后的身份，这时我们可以测试是否会跳转目标以外的网站，比如：

> https://example.com/login?returnUrl=https://www.xazlsec.com

如果登录成功之后，跳转至信安之路的网站，那么该漏洞就存在。

#### 类型三：基于 html 标签的 URL 跳转

实现 URL 重定向，除了在 header 中设置 Location 字段外，还有两种实现方式：

1、Meta 标签，代码如下：

```
<head>
<meta http-equiv="Refresh" content="0; URL=https://example.com/" />
</head>
```

2、javaScript 代码：

```
window.location = "https://example.com/";
```

如果是这两种方式实现 URL 跳转，而 URL 参数可控，则可能存在 XSS 漏洞。

#### 类型四：基于 DOM 的 URL 重定向

JavaScript 可以直接从浏览器获取数据。Web 浏览器中的 URL，例如：

> https://example.com/#dashboard

dashboard 不会被发送至后端，如果页面中使用如下 JavaScript 代码：

```
// use substr() to remove the '#'
window.location = window.location.hash.substr(1)
```

攻击者可以创建如下链接：

> https://example.com/#https://www.xazlsec.com

访问之后将跳转至信安之路的网站。

### URL 重定向漏洞修复

#### 方案一：URL 白名单

可以将需要跳转的页面，保存至数据库，然后用对应的 id 进行跳转，比如：

```
https://example.com/redirect?externalPage=1
https://example.com/redirect?externalPage=2
https://example.com/redirect?externalPage=3
```

如果只是重定向到本网站的页面，可以使用页面命名方案，比如：

```
https://example.com/redirect?page=dashboard
https://example.com/redirect?page=account
https://example.com/redirect?page=settings
```

方案二：正则表达式

正则表达式的方案，无需操作数据库，但是设置不好容易被绕过，比如下面的案例：

```
redirect_url = urlparse.urlparse(url)
# 漏洞参数原因，仅匹配 url前缀
if bool(re.search("^https://example.com", url)):
```

只是搜索 url 中是否包含 https://example.com 且以它为开头，可以用下面的 poc 绕过：

> https://example.com/redirect?page=https://example.com.evil-hackers.corp.com

要使用正则表达式，使用尾部斜杠以防止恶意使用子域:

```
redirect_url = urlparse.urlparse(url)
 #修复后，限定完整域名
if bool(re.search("^https://example.com/", url)):
```

这样就确保不会重定向到设置之外的域。

#### 方案三：任意 URL 跳转功能

有些功能设计之初就是为了能够跳转至任意网站，比如一些推广功能，这种情况下，最基本的也要对跳转的协议做限制，比如只允许跳转以 `https?://` 开头的网站。

在跳转至外部网站时，设置提示，提醒用户，比如：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196033-16766122691.png)

### 总结

URL 重定向本身并不是坏事，但您必须采取措施确保用户都知道发生的外部重定向，并在必要时尽量减少重定向到的目标。

**本文作者：[信安之路](newpage/author?author_id=49490)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/196033.html**](https://www.secpulse.com/archives/196033.html)

Tags: [html 标签](https://www.secpulse.com/archives/tag/html-%E6%A0%87%E7%AD%BE)、[URL 跳转](https://www.secpulse.com/archives/tag/url-%E8%B7%B3%E8%BD%AC)、[URL 重定向](https://www.secpulse.com/archives/tag/url-%E9%87%8D%E5%AE%9A%E5%90%91)、[参数](https://www.secpulse.com/archives/tag/%E5%8F%82%E6%95%B0)、[渗透测试](https://www.secpulse.com/archives/tag/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-204824-1711610670-300x300.png)

  《内网安全攻防》姊妹篇《红队之路》重磅上…](https://www.secpulse.com/archives/204824.html "详细阅读 《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）")
* [![利用远程调试获取Chromium内核浏览器Cookie](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/07/1689233615328-300x157.png)

  利用远程调试获取Chromium内核浏览…](https://www.secpulse.com/archives/202712.html "详细阅读 利用远程调试获取Chromium内核浏览器Cookie")
* [![新一代RedTeam启发式内网扫描工具](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/07/1688546246784-300x194.png)

  新一代RedTeam启发式内网扫描工具](https://www.secpulse.com/archives/202616.html "详细阅读 新一代RedTeam启发式内网扫描工具")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1396eb4a28abd3245bce454bfb351c42_11-290x290.jpg)](https://www.secpulse.com/newpage/author?author_id=49490aaa) | [信安之路](https://www.secpulse.com/newpage/author?author_id=49490) | |
| 文章数：6 | 积分： 0 |
|  | |

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

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bageve...