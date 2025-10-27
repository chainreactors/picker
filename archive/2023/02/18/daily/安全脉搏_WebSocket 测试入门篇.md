---
title: WebSocket 测试入门篇
url: https://www.secpulse.com/archives/196038.html
source: 安全脉搏
date: 2023-02-18
fetch_date: 2025-10-04T07:19:57.132308
---

# WebSocket 测试入门篇

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

# WebSocket 测试入门篇

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[信安之路](https://www.secpulse.com/newpage/author?author_id=49490)

2023-02-17

13,457

> 本文是信安之路 wiki 平台第 142 篇文章，注册解锁全部文章

Websocket 是一种用于 H5 浏览器的实时通讯协议，可以做到数据的实时推送，可适用于广泛的工作环境，例如客服系统、物联网数据传输系统，

## 基础介绍

我们平常接触最多的是 http 协议的接口，http 协议是请求与响应的模式，你发个请求到服务端，服务端给个返回你。

这种模式并不能满足我们生活中的全部场景，就拿最近小伙伴们关注的股票基金为例，比如我想关注某个基金当天的净值估算。

我打开一个网页后，这时候我在页面不需要做任何操作，页面上的数据会自动刷新，间隔 x 秒或者 x 分钟，会自动刷新数据。

要实现这种实时更新的效果，有几种实现方式：

1. 还是用 http 请求，用 ajax 轮询，每间隔固定的时间，询问一次服务端，从服务端拿最新的数据
2. 使用 websocket 建立长连接，服务端和客户端可以互相通信，服务端只要有数据更新，就可以主动推给客户端

         ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613912.png)

上图为 ajax 轮询与 webscokets 实现的方式对比图，从图中可以看出 ajax 轮询是在特定的的时间间隔（如每1秒），由浏览器对服务器发出 HTTP 请求，然后由服务器返回最新的数据给客户端的浏览器。这种传统的模式带来很明显的缺点，即浏览器需要不断的向服务器发出请求，然而 HTTP 请求可能包含较长的头部，其中真正有效的数据可能只是很小的一部分，显然这样会浪费很多的带宽等资源。

HTML5 定义的 WebSocket 协议，能更好节省服务器资源和带宽，并且能够更实时地进行通讯。 浏览器通过 JavaScript 向服务器发出建立 WebSocket 连接的请求，连接建立以后，客户端和服务器端就可以通过 TCP 连接直接交换数据。

## 识别方式

想要识别网站是否使用了 websockets 协议，需要先了解其工作过程，下图是 WebSocket 工作的详细过程：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613913.png)

WebSocket 服务端的连接地址与 http 协议类似，以 ws、wss 开头，比如：

> ws://ws.xazlsec.com:8888
>
> wss://wss.xazlsec.com:9999

wss 是 ws 基础上用 ssl 加密传输信息，使用 javascript 连接的代码案例如下：

```
var ws = new WebSocket("wss://wss.xazlsec.com:9999/chat");
```

所以识别网站是否使用该协议，可以从两个地方分辩：

1、数据包中是否有 ws、wss 开头的链接地址 2、javascript 代码中是否包含 WebSocket 这样的函数调用，或者以 ws、wss 开头的链接

对于这种协议的数据包，常见的 web 测试工具都具备抓取能力，比如 BurpSuite，ZAP 等：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613915.png)

## 常见漏洞

### 1、CSWSH（跨站点网站劫持，最为广泛的漏洞）

类似于 CSRF 漏洞，在没有验证请求源的情况下，任意来源均可以连接 WebSocket 服务器进行数据交互，攻击者通过构造恶意页面，诱使用户访问，然后借助用户的身份信息与服务器建立连接，从而劫持用户身份下的 WebSocket 连接。

### 2、XSS（跨站脚本攻击）

由于大多数的聊天室，对于用户输入过滤不严导致 XSS 漏洞的发生。

### 3、授权问题

WebSocket 中没有可以检查 IDOR 和 授权问题的标头

### 4、DOS 攻击

WebSockets 允许无限数量的连接服务器。攻击者可以用 DOS 攻击服务器。这种行为增加了服务器的负担并耗尽了服务器上的资源致使网站速度大大降低。

## 黑盒测试内容

1、检查是否可以通过其他来源连接 ws 服务器 2、是否使用了 ssl 加密传输敏感信息，也就是服务器连接是否 ws 还是 wss 3、身份验证检查，连接 ws 服务器是否需要授权 4、输入内容是否做了过滤，比如 xss、sql 注入等 payload，检测是否存在该漏洞

## WebSocket 靶场 DVWS 初体验

DVWS 类似于 DVWA，但是客户端之间的通信是通过 WebSockets 进行，项目地址：

> https://github.com/interference-security/DVWS

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-16766139151.png)

首先在 burp 上设置好监听端口，然后在浏览器中设置代理为 burp 监听的地址：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613916.png)

### 暴力破解

打开 dvws 左侧菜单中的暴力破解实验，输入账号密码之后登录：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-16766139161.png)

Burp 截取到的数据包，从 WebSocket History 选项卡中可以看到：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613917.png)

我们如果想暴力破解这个账号密码需要不断与服务器建立连接，而 Burp 的 Intruder 是针对 http 协议进行利用，所以这里需要用到一个脚本，将 http 协议转为 WebSocket 协议，脚本地址：

> https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Web%20Sockets/Files/ws-harness.py

下载脚本后，将 ws 的地址（burp 的代理端口）作为参数，启动该脚本：

> python ws-harness.py -u “ws://dvws.local:8080” -m ./message.txt

注意：如果是 https 则使用 wss，message.txt 中保存的是 websockets 消息模板，访问时以 fuzz 作为参数名，如图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-16766139171.png)

启动后，监听一个新的端口 8000:

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613918.png)

接下来访问：

> http://localhost:8000/?fuzz=

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-16766139181.png)

到这里已经实现了 http 协议转 WebSocket，针对这个连接进行 fuzz，也就是针对 WebSockets 协议的认证做 fuzz，接下来就很简单了，使用 Intruder 进行 fuzz：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613919.png)

由于靶场中的用户名密码使用了 base64 编码，所以需要在 burp 中设置：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-16766139191.png)

到这里就完成了针对 WebSocket 协议的认证做暴力破解的操作。

### SQL 注入

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613920.png)

操作过程与暴力破解类似，设置完 http 转 WebSocket 后：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-16766139201.png)

使用 sqlmap 针对该接口进行测试，需要用到 base64encode 这个 tamper：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613922.png)

成功利用：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613923.png)

###

## 总结

本文主要讲了 WebSockets 协议的原理基础，主要目的是对 WebSockets 有个大体的认识，推荐大家去玩玩 DVWS 这个靶场。

### 参考

https://www.runoob.com/html/html5-websocket.html

https://zero-s4n.hashnode.dev/fuzzing-websocket-messages-on-burpsuite

https://www.appknox.com/blog/everything-you-need-to-know-about-web-socket-pentesting

###

**本文作者：[信安之路](newpage/author?author_id=49490)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/196038.html**](https://www.secpulse.com/archives/196038.html)

Tags: [AJAX](https://www.secpulse.com/archives/tag/ajax)、[CSWSH](https://www.secpulse.com/archives/tag/cswsh)、[DOS 攻击](https://www.secpulse.com/archives/tag/dos-%E6%94%BB%E5%87%BB)、[HTTP 协议](https://www.secpulse.com/archives/tag/http-%E5%8D%8F%E8%AE%AE)、[SQL 注入](https://www.secpulse.com/archives/tag/sql-%E6%B3%A8%E5%85%A5)、[WebSocket](https://www.secpulse.com/archives/tag/websocket)、[XSS](https://www.secpulse.com/archives/tag/XSS)、[授权](https://www.secpulse.com/archives/tag/%E6%8E%88%E6%9D%83)、[暴力破解](https://www.secpulse.com/archives/tag/%E...