---
title: 禁用XXE处理漫谈
url: https://www.secpulse.com/archives/197380.html
source: 安全脉搏
date: 2023-03-14
fetch_date: 2025-10-04T09:28:16.393691
---

# 禁用XXE处理漫谈

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

# 禁用XXE处理漫谈

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-13

7,854

## 前言

近期准备面试题时，XXE漏洞防范措施（或者说修复方式）在一些文章中比较简略，

故本文根据研究进行总结，作为技术漫谈罢了。

## 简述

### XXE漏洞

XXE（XML外部实体注入），程序解析XML数据时候，同时解析了攻击者伪造的外部实体。XML用途是为了跨平台语言传输数据。常常用于WEB开发等

### XXE漏洞攻防情况

通常来说，XML文档生成时会常用到XXE和内部实体。因此开发团队根据项目需求去进行防范XXE漏洞。

然而实际情况是，即使采取了防范措施（错误的方法），XXE漏洞仍然可以大行其道。

有一个案例，某开发团队针对CVE-2018-20318漏洞进行了及时的修复，依照的是官方的修复方案：

禁止实体扩展引用，dbFactory.setExpandEntityReferences(false)

然而后续XXE漏洞仍然可以奏效，有师傅又提交了CVE漏洞。

最后有师傅总结正确的修复方法，如下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197380-1678685614.png "null")

## 禁用XXE处理分析

根据上述所说，XXE漏洞的正确处理是尤为重要的。我们这里以Java为例，

并且应用偏向于JAXP API进行分析如何禁用XXE处理

### 禁用文档类型

首先可以禁用文档类型。实体通过XML 文档的 DOCTYPE 进行声明。

我们在进行安全开发规划时，如确定不需要 DOCTYPE 声明时，可以完全禁用禁用文档类型。

`factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);`

当我们设置为true时，disallow-doctype-decl 使XML处理器发现DOCTYPE 声明时抛出异常。

### 禁用外部实体声明

其次是可以允许声明DOCTYPE，但禁用外部实体声明。

故若想要正常处理其他DTD声明，只针对外部实体进行抛出异常。可以用下面两种方法设置为flase来处理：

`factory.setFeature("http://xml.org/sax/features/external-general-entities", false);` `factory.setFeature("http://xml.org/sax/features/external-parameter-entities", false);`

补充说明：在PHP中，libxml库默认下是安全的，总是禁用外部实体。除非通过设置LIBXML\_NOENT

参数进行允许。如下：

`$doc = simplexml_load_string($xml, "SimpleXMLElement", LIBXML_NOENT); // !XXE enabled!` `$doc = simplexml_load_string($xml, "SimpleXMLElement"); // XXE disabled`

### 启用安全处理

在Java中可以使用Feature for Secure Processing (FSP)进行安全处理。如下：

`factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);`

FSP属于一种核心Java机制，用于以应用限制去配置XML处理器，从而可以防范XML拒绝服务攻击和XXE漏洞。

默认设置下，FSP处于部分启用的状态，XML拒绝服务攻击可以防范。而XXE漏洞我们需要通过调用

setFeature方法，将FSP由部分启用转为完全启用。

不过也有特例，例如Apache Xerces中FSP不限制外部连接，无法防范XXE漏洞。

总之，开发人员应当测试涉及XXE漏洞的FSP配置，并结合其他方式来禁用或者限制XXE

### 禁用实体引用扩展

XML文档中寻找实体引用主要有两种方式：

（1）DOM XML解析器作值替换引用

（2）DOM树创建空实体进行引用

将实体作值替换的机制在解析恶意XML文件时，可能会泄露敏感信息。

在Java中，对象DocumentBuilder中的etExpandEntityReferences方法用于配置实体引用：

`DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();` `factory.setExpandEntityReferences(false);`

当配置为false时，不会进行实体引用。因而可以防范XXE漏洞。

扩展外部实体引用是发生在已提取外部内容之后。

因此禁用后且攻击者无法造成泄露敏感数据，仍然执行请求外部资源。

不过经过禁用实体引用扩展，攻击者仅能进行blind SSRF攻击，难以实际造成威胁。

所以禁用实体引用扩展也是我们防范XXE漏洞的可选方案。

## 结束语

本文为XXE漏洞相关的防范措施漫谈，主要针对禁用XXE处理。

可以采取禁用文档类型、禁用外部实体声明、启用安全处理、

禁用实体引用扩展这四种方式去进行防范。

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197380.html**](https://www.secpulse.com/archives/197380.html)

Tags: [CVE-2018-20318](https://www.secpulse.com/archives/tag/cve-2018-20318)、[Web开发](https://www.secpulse.com/archives/tag/web%E5%BC%80%E5%8F%91)、[XML外部实体注入](https://www.secpulse.com/archives/tag/xml%E5%A4%96%E9%83%A8%E5%AE%9E%E4%BD%93%E6%B3%A8%E5%85%A5)、[XXE漏洞](https://www.secpulse.com/archives/tag/XXE%E6%BC%8F%E6%B4%9E)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![xxe原理解析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1683530158813-300x167.png)

  xxe原理解析](https://www.secpulse.com/archives/199990.html "详细阅读 xxe原理解析")
* [![红队-java代码审计生命周期](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1671507029449-300x225.png)

  红队-java代码审计生命周期](https://www.secpulse.com/archives/193771.html "详细阅读 红队-java代码审计生命周期")
* [![web类 | XXE漏洞总结](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/1665993001586-300x219.png)

  web类 | XXE漏洞总结](https://www.secpulse.com/archives/189161.html "详细阅读 web类 | XXE漏洞总结")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=37244) | |
| 文章数：402 | 积分： 877 |
| 蚁景网安实验室（www.yijinglab.com）网络安全靶场练习平台，涉及CTF赛前指导、职业技能训练、网安专项技能提升等。 | |

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

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.comevent6531722&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect)

#### 2020-09-24

[CSDI summit中国软件研发管理行业...