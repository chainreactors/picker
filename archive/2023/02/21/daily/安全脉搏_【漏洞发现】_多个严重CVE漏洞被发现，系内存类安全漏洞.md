---
title: 【漏洞发现】|多个严重CVE漏洞被发现，系内存类安全漏洞
url: https://www.secpulse.com/archives/196134.html
source: 安全脉搏
date: 2023-02-21
fetch_date: 2025-10-04T07:35:31.700772
---

# 【漏洞发现】|多个严重CVE漏洞被发现，系内存类安全漏洞

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

# 【漏洞发现】|多个严重CVE漏洞被发现，系内存类安全漏洞

[漏洞](https://www.secpulse.com/archives/category/vul)

[云起无垠](https://www.secpulse.com/newpage/author?author_id=48775)

2023-02-20

9,457

[[![6.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/61-1024x527.png "61-1024x527.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/61.png)](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/640.gif)

# **1.漏洞描述**

#

近日，**云起无垠的无垠代码模糊测试系统通过对json parse库、MojoJson进行检测发现多个CVE漏洞**，漏洞编号为：CVE-2023-23083 ~ CVE-2023-23088，该系列漏洞皆为内存类漏洞，漏洞允许攻击者执行恶意代码进行攻击，从而造成严重后果。其中，CVE-2023-23086~CVE-2023-23088已公开。

MojoJson 是一个极其简单且超快速的JSON 解析器。解析器支持解析Json 格式，并提供简单的API 来访问不同类型的 Json 值。此外，核心算法可以很容易地用各种编程语言实现。

JSON.parse()是Javascript中一个常用的 JSON 转换方法，JSON.parse()可以把JSON规则的字符串转换为JSONObject，JSON.parse()很方便，并且几乎支持所有浏览器。

针对此类漏洞，无垠代码模糊测试系统均给出了相应建议。

# **2.****漏洞详情**

① CVE-2023-23086 func SkipString中堆缓冲区溢出

MojoJson v1.2.3中的缓冲区溢出漏洞允许攻击者通过SkipString函数执行任意代码。

**漏洞等级：严重；CVSS v3.1漏洞评分：9.8**

检测截图：

[![1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/111-1024x530.png "111-1024x530.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/111.png)

[![2.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/24-1024x558.png "24-1024x558.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/24.png)

② CVE-2023-23087 函数Destory中指针错误

在MojoJson v1.2.3中发现了一个问题，允许攻击者通过destroy函数执行任意代码。

**漏洞等级：严重；CVSS v3.1漏洞评分：9.8**

检测截图：

[![3.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/34-1024x420.png "34-1024x420.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/34.png)

[![4.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/44-1024x511.png "44-1024x511.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/44.png)

③ CVE-2023-23088 json\_value\_parse堆缓冲区溢出

Barenboim json-parser master和v1.1.0中的缓冲区溢出漏洞已在v1.1.1中修复，允许攻击者通过json\_value\_parse函数执行任意代码。

**漏洞等级：严重；CVSS v3.1漏洞评分：9.8**

检测截图：

[![5.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/53-1024x535.png "53-1024x535.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/53.png)

![](https://www.secpulse.com/wp-content/plugins/ueditor/ueditor/themes/default/images/spacer.gif "正在上传...")

# **3.****解决方案**

无垠代码模糊测试系统针对每一个CVE漏洞都给出了处置方案，可参照如上截图细看。

#

**参考链接：**

<https://nvd.nist.gov/vuln/detail/CVE-2023-23086>

<https://github.com/scottcgi/MojoJson/issues/2>

<https://nvd.nist.gov/vuln/detail/CVE-2023-23087>

<https://github.com/scottcgi/MojoJson/issues/3>

<https://nvd.nist.gov/vuln/detail/CVE-2023-23088>

<https://github.com/Barenboim/json-parser/issues/7>

**本文作者：[云起无垠](newpage/author?author_id=48775)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/196134.html**](https://www.secpulse.com/archives/196134.html)

Tags: [CVE-2023-23083](https://www.secpulse.com/archives/tag/cve-2023-23083)、[CVE-2023-23084](https://www.secpulse.com/archives/tag/cve-2023-23084)、[CVE-2023-23085](https://www.secpulse.com/archives/tag/cve-2023-23085)、[CVE-2023-23086](https://www.secpulse.com/archives/tag/cve-2023-23086)、[CVE-2023-23087](https://www.secpulse.com/archives/tag/cve-2023-23087)、[CVE-2023-23088](https://www.secpulse.com/archives/tag/cve-2023-23088)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Solon框架模板漏洞深度剖析与修复实战](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/7266edd7-a4cc-444d-bacb-7ee802487ac4.png)

  Solon框架模板漏洞深度剖析与修复实战](https://www.secpulse.com/archives/206316.html "详细阅读 Solon框架模板漏洞深度剖析与修复实战")
* [![路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202503171628715.png)

  路由器安全研究：D-Link DIR-8](https://www.secpulse.com/archives/206007.html "详细阅读 路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路")
* [![DedeBIZ系统审计小结](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202502121526395.png)

  DedeBIZ系统审计小结](https://www.secpulse.com/archives/205891.html "详细阅读 DedeBIZ系统审计小结")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1677469307411.png)](https://www.secpulse.com/newpage/author?author_id=48775aaa) | [云起无垠](https://www.secpulse.com/newpage/author?author_id=48775) | |
| 文章数：1 | 积分： 0 |
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

[OPPO技术开放日第六期|聚焦应用与数据安全防...