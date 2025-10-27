---
title: WebSocket 内存马，一种新型内存马技术
url: https://www.secpulse.com/archives/190549.html
source: 安全脉搏
date: 2022-11-05
fetch_date: 2025-10-03T21:44:36.173969
---

# WebSocket 内存马，一种新型内存马技术

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

# WebSocket 内存马，一种新型内存马技术

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Lemon](https://www.secpulse.com/newpage/author?author_id=5109)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2022-11-04

9,876

# **WebSocket 内存马，一种新型内存马技术**

### 1.前言

WebSocket是一种全双工通信协议，即客户端可以向服务端发送请求，服务端也可以主动向客户端推送数据。这样的特点，使得它在一些实时性要求比较高的场景效果斐然（比如微信朋友圈实时通知、在线协同编辑等）。主流浏览器以及一些常见服务端通信框架（Tomcat、netty、undertow、webLogic等）都对WebSocket进行了技术支持。

### 2.版本

2013年以前还没出JSR356标准，Tomcat就对Websocket做了支持，自定义API，再后来有了JSR356，Tomcat立马紧跟潮流，废弃自定义的API，实现JSR356那一套，这就使得在Tomcat7.0.47之后的版本和之前的版本实现方式并不一样，接入方式也改变了。

JSR356 是java制定的websocket编程规范，属于Java EE 7 的一部分，所以要实现websocket内存马并不需要任何第三方依赖

### 3.服务端实现方式

#### （1）注解方式

```
@ServerEndpoint(value = "/ws/{userId}", encoders = {MessageEncoder.class}, decoders = {MessageDecoder.class}, configurator = MyServerConfigurator.class)
```

Tomcat在启动时会默认通过 WsSci 内的 ServletContainerInitializer 初始化 Listener 和 servlet。然后再扫描 `classpath`下带有 `@ServerEndpoint`注解的类进行 `addEndpoint`加入websocket服务

所以即使 Tomcat 没有扫描到 `@ServerEndpoint`注解的类，也会进行Listener和 servlet注册，这就是为什么所有Tomcat启动都能在memshell scanner内看到WsFilter

# ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190549-1667554516.png)

#### （2）继承抽象类Endpoint方式

继承抽象类 `Endpoint`方式比加注解 `@ServerEndpoint`方式更麻烦，主要是需要自己实现 `MessageHandler`和 `ServerApplicationConfig`。`@ServerEndpoint`的话都是使用默认的，原理上差不多，只是注解更自动化，更简洁

可以用代码更方便的控制 ServerEndpointConfig 内的属性

```
ServerEndpointConfig serverEndpointConfig = ServerEndpointConfig.Builder.create(WebSocketServerEndpoint3.class, "/ws/{userId}").decoders(decoderList).encoders(encoderList).configurator(new MyServerConfigurator()).build();
```

### 3.websocket内存马实现方法

之前提到过 Tomcat 在启动时会默认通过 WsSci 内的 ServletContainerInitializer 初始化 Listener 和 servlet。然后再扫描 `classpath`下带有 `@ServerEndpoint`注解的类进行 `addEndpoint`加入websocket服务

那如果在服务启动后我们再 addEndpoint 加入websocket服务行不行呢？答案是肯定的，而且非常简单只需要三步。创建一个ServerEndpointConfig，获取ws ServerContainer，加入 ServerEndpointConfig，即可

```
ServerEndpointConfig config = ServerEndpointConfig.Builder.create(EndpointInject.class, "/ws").build();
ServerContainer container = (ServerContainer) req.getServletContext().getAttribute(ServerContainer.class.getName());
container.addEndpoint(config);
```

### 4.效果

首先利用i.jsp注入一个websocket服务，路径为/x，注入后利用ws连接即可执行命令

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190549-16675545161.png)

且通过memshell scanner查询不到任何异常（因为根本就没注册新的 Listener、servlet 或者 Filter）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190549-1667554518.png)

### 5.代理

WebSocket是一种全双工通信协议，它可以用来做代理，且速度和普通的TCP代理一样快，这也是我研究websocket内存马的原因。

例如有一台不出网主机，有反序列化漏洞。

以前在这种场景下，可能会考虑上reGeorg或者利用端口复用来搭建代理。

现在可以利用反序列化漏洞直接注入websocket代理内存马，然后直接连上用上全双工通信协议的代理。

注入完内存马以后，使用 Gost：https://github.com/go-gost/gost 连接代理

```
./gost -L "socks5://:1080" -F "ws://127.0.0.1:8080?path=/proxy"
```

然后连接本地1080端口socks5即可使用代理

### 6.多功能shell实现

想要使用ws马首先得支持连接ws协议的工具，目前市面的webshell管理工具都要从源码上修改才能支持ws协议

具体实现过程也并不复杂，相当于只是替换了协议，内容其实可以不变。例如给出的哥斯拉支持样例，基本逻辑并没发生改变，只是协议变了

还有一个问题是ws马必须先注入再连接，并不能直接连接jsp马。

然而例如哥斯拉的jsp马本身就是支持远程代码执行，那么jsp马其实可以保持不变就用哥斯拉原版，但发送class要修改，先发送过去先初始化注册ws马的class，连上ws以后再初始化恶意class，多一步，第二步连接的时候使用ws连接。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190549-16675545181.png)

如果是内存注入的内存马则不需要连接jsp，直接连接ws

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190549-1667554521.png)

## 版权声明

完整代码：https://github.com/veo/wsMemShell

```
本文章著作权归作者所有。转载请注明出处！https://github.com/veo
来源：先知(https://xz.aliyun.com/t/11549)
```

**侵权请私聊公众号删文**

**本文作者：[Lemon](newpage/author?author_id=5109)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190549.html**](https://www.secpulse.com/archives/190549.html)

Tags: [WebSocket](https://www.secpulse.com/archives/tag/websocket)、[内存马](https://www.secpulse.com/archives/tag/%E5%86%85%E5%AD%98%E9%A9%AC)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Java反序列化回显学习之Tomcat通用回显](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684907775563-300x214.png)

  Java反序列化回显学习之Tomcat通…](https://www.secpulse.com/archives/200930.html "详细阅读 Java反序列化回显学习之Tomcat通用回显")
* [![WebSocket 测试入门篇](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613912-300x160.png)

  WebSocket 测试入门篇](https://www.secpulse.com/archives/196038.html "详细阅读 WebSocket 测试入门篇")
* [![安全攻防 | APP抓包大全](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1671784448332-300x206.png)

  安全攻防 | APP抓包大全](https://www.secpulse.com/archives/194000.html "详细阅读 安全攻防 | APP抓包大全")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/f43a6447ea66cf84915afd0ca2631f09.png)](https://www.secpulse.com/newpage/author?author_id=5109aaa) | [Lemon ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)](https://www.secpulse.com/newpage/author?author_id=5109) | |
| 文章数：68 | 积分： 647 |
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

[Gdevops 全球敏捷运维峰会](https://www.bagevent.c...