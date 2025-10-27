---
title: 浅谈APP的污点分析
url: https://www.secpulse.com/archives/199921.html
source: 安全脉搏
date: 2023-05-06
fetch_date: 2025-10-04T11:38:13.619632
---

# 浅谈APP的污点分析

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

# 浅谈APP的污点分析

[移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)

[小道安全](https://www.secpulse.com/newpage/author?author_id=11697)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-05-05

21,531

背景

APP中存在比较严重的安全风险有：数据泄露问题、第三方库漏洞问题、隐私合规问题、组件间通信问题。

当用户在不知情或没有授权的情况下，APP进行收集用户的隐私数据(包括IMEI ID、位置信息、视频与音频信息、Web浏览记录等), 并将其收集的信息推送或转卖给广告推荐商，那么该APP就存在隐私合规的问题。

**合规场景下APP污点分析几个高频关注点：组件内污点传播、组件间污点传播、组件与库函数之间的污点传播、加密算法是否使用常量密钥、静态初始化的向量、加密模式是否使用ECB模式。**

污点分析技术是APP隐私数据安全、病毒分析(基于常用的API分析)和实现漏洞检测的重要技术手段，也是信息安全研究的热点领域，静态污点分析方法是目前APP应用中检测隐私泄露的主流方法之一。

理论基础

污点分析(taint analysis)：是一项跟踪并分析污点信息在程序中流动的技术,该技术通过对系统中的敏感数据进行标记, 继而跟踪标记数据在程序中的传播, 检测系统安全问题。

**它可以抽象为一个三元组<source, sink, sanitizers>形式：**

source即为污染源，代表程序的敏感数据或引入的不受信任的数据；

sink为污点汇聚点**，**代表直接产生安全敏感操作，或向外发送隐私数据；

sanitizer即无害化处理，表示污染源数据通过一些操作解除了其危害性，如对发送出去的数据做了加密处理或对引入的数据做了安全校验。

污点分析技术可分为动态分析、静态分析和混合分析,但在APP应用中污点分析技术主要应用到静态污点分析技术。

APP静态污点分析它是在静态分析的基础上加入污点分析原理，使其结果为该分析方法所期望的可疑数据流。静态分析是指在不运行应用的前提下,对APK包中的代码进行扫描从而生成程序的反汇编代码来掌握程序功能,提取其中的词法、语法和语义,进一步实现控制流分析和数据流分析,以帮助开发者发现程序中存在的结构性错误和安全漏洞等问题。

动态分析是通过在真实或虚拟处理机上执行程序,监控程序执行,并在执行过程中使用插桩的方式获取程序的控制流和数据流,发现程序运行时错误或者潜在漏洞攻击。

Android中由于动态特性代码(反射，动态加载、代码生成，外部代码执行等）只有在运行时才能获得具体信息，常规的静态污点分析无法精确地分析出APP中可能存在的安全问题，也就导致了漏报率的上升。

如果对APP用户隐私泄露监测加入静态污点分析，那么污点源可以是能够获取隐私信息的函数，如读取最新位置信息的getLastKnownLocation()函数，污点库可以是具有短信发送功能的函数等具有引发危险问题的库函数。污点源中的函数在获取污点数据之后，可能会依次通过不同的变量将污点数据传递到污点库函数中，在此过程中，所有存储了该污点数据的变量都应该被标记为污点状态，这样就可以追踪过程，即追踪标记为污点状态的变量的数据流过程。

浅析污点分析

污点分析4个关键点：污点产生位置、目标触发位置、污点传递规则、程序入口。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199921-1683278290.png)

Android应用的入口是各个组件，它一般从AndrroidManifest.xml文件中进行解析，以及registerReceiver 的动态注册。

由于APP组件的生命周期是由Android系统维护的，污点追踪可能因为生命周期回调函数的结束而中断。

所以APP之间或内部的数据传递也是基于组件的。组件之间通讯是通过发送Intent组件传递信息来实现的，追踪污点的数据流就是追踪各个组件之间Intent的传播数据流。因为Intent有两种类型，一种是明确发送目的地的显式Intent，一种是没有明确发送目的地的隐式Intent。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199921-1683278291.png)

(图片来源网络)

APP静态污点分析：通过解析dex 文件并根据 APP的生命周期建立函数调用的模型，使用静态数据流分析的方法，静态模拟代码数据的传播，实现静态数据的跟踪，以达到精准定位漏洞的目的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199921-1683278292.png)

（图片来源网络）

**App静态污点分析技术主要包括如下步骤：**

1、解析应用AndroidManifest.xml，Layout配置文件和相关Dex字节码，根据预先建模的Android LifeCycle Model生成超调用图 ，又称过程间控制流图(Inter-procedural control flow graph, ICFG)；

2、根据定义的污点源和锚点(Source and Sink)，将其转换为基于ICFG的后向或前向数据流问题进行求解；

3、根据求解结果，回答是否存在从某输入到输出的数据流流动路径，以显式Intent问题为例，FlowDroid会检测到一个以发送intent的sink方法到最后接收intent的source的路径存在。

可参考源码

**1、FlowDroid是一款静态污点分析框架，它是基于Soot开发对Android应用进行污点分析的框架**。Soot是一款强大的Java代码优化分析框架，通过将Java字节码转换为其独有的中间表示，进行控制流分析、调用图分析。主要它目前还有在维护更新

**https://github.com/secure-software-engineering/FlowDroid**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199921-1683278295.png)

**2、MobSF 是一个自动化的、一体化的移动应用程序（Android/iOS/Windows）恶意软件分析和安全评估框架，能够执行静态和动态分析。**目前市场上很多合规扫描检测都是基于它去做定制开发的。

**https://github.com/ajinabraham/Mobile-Security-Framework-MobSF**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199921-1683278297.png)

**3、AppShark它是一款针对Android应用程序的安全测试框架**，它本质上是一个静态污点分析平台，可以用于扫描Android应用程序中的漏洞，也还有在维护更新。

**https://github.com/bytedance/appshark**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199921-1683278299.png)

**4、PATDroid是用于分析Android应用程序和系统本身的工具和数据结构的集合**，它通过解析smali语句，分析程序控制流等，也具备APP污点分析的能力，不过它已经没更新了，可以学习下它的思路。

**https://github.com/mingyuan-xia/PATDroid**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199921-1683278300.png)

**本文作者：[小道安全](newpage/author?author_id=11697)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/199921.html**](https://www.secpulse.com/archives/199921.html)

Tags: [APP](https://www.secpulse.com/archives/tag/APP)、[安全风险](https://www.secpulse.com/archives/tag/%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9)、[数据泄露](https://www.secpulse.com/archives/tag/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)、[第三方库漏洞](https://www.secpulse.com/archives/tag/%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93%E6%BC%8F%E6%B4%9E)、[组件与库函数](https://www.secpulse.com/archives/tag/%E7%BB%84%E4%BB%B6%E4%B8%8E%E5%BA%93%E5%87%BD%E6%95%B0)、[组件内污点传播](https://www.secpulse.com/archives/tag/%E7%BB%84%E4%BB%B6%E5%86%85%E6%B1%A1%E7%82%B9%E4%BC%A0%E6%92%AD)、[组件间污点传播](https://www.secpulse.com/archives/tag/%E7%BB%84%E4%BB%B6%E9%97%B4%E6%B1%A1%E7%82%B9%E4%BC%A0%E6%92%AD)、[组件间通信](https://www.secpulse.com/archives/tag/%E7%BB%84%E4%BB%B6%E9%97%B4%E9%80%9A%E4%BF%A1)、[隐私合规](https://www.secpulse.com/archives/tag/%E9%9A%90%E7%A7%81%E5%90%88%E8%A7%84)

点赞：
3
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![APP隐私合规自查关键点](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686723323550-300x142.png)

  APP隐私合规自查关键点](https://www.secpulse.com/archives/202052.html "详细阅读 APP隐私合规自查关键点")
* [![APP黑灰产上下游分析整理](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198933-1681374377-300x159.png)

  APP黑灰产上下游分析整理](https://www.secpulse.com/archives/198933.html "详细阅读 APP黑灰产上下游分析整理")
* [![APP中WebResourceResponse漏洞分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1680074899585-300x197.png)

  APP中WebResourceRespo…](https://www.secpulse.com/archives/198399.html "详细阅读 APP中WebResourceResponse漏洞分析")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2021/07/16/e6a1736ccb19220a63d5403b14ce91c9-290x290.jpeg)](https://www.secpulse.com...