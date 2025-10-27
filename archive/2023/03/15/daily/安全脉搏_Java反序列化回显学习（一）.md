---
title: Java反序列化回显学习（一）
url: https://www.secpulse.com/archives/197448.html
source: 安全脉搏
date: 2023-03-15
fetch_date: 2025-10-04T09:33:50.160417
---

# Java反序列化回显学习（一）

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

# Java反序列化回显学习（一）

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-14

10,200

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777748.png)

# 前言

在测试某反序列化漏洞，可以通过URLDNS链确定漏洞是否存在但在利用时遇到了困难，相关利用链可以执行系统命令却无法得到回显。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777749.png "null")

因此需要在此基础修改利用链达到命令回显得目的，下边记录的即是此次修改的过程。

# Java反序列化回显方法

根据搜索到的资料给出的常见回显方法有以下几种：1、报错回显：要求服务器将报错信息打印到页面。2、写文件：把执行结果写入静态文件置于web目录下再读取结果。3、DNSLOG回显：通过DNSLOG将执行结果带出（未实现）。4、中间件回显：获取response对象，结果写入response对象中带出。5、.....

## 报错回显

此法要求服务器将报错信息打印出来，修改要反序列化执行的Java代码将结果写入异常再抛出即可实现。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777751.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777755.png "null")

## 写文件回显

同样修改yso中Gadgets要执行的java代码即可实现，通过将执行结果写入web目录下的静态文件再读取来实现。此法的缺点是当目标不存在可访问静态web目录便无法使用了且要获取web目录的绝对路径，更适用于已知开发框架的反序列化漏洞利用。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777757.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777760.png "null")

## DNSLOG

一般作为检测反序列化漏洞是否存在用，贴出URLDNS Gadget的验证过程。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777764.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777766.png "null")

## 中间件回显

中间件回显是目前所有反序列化工具中最为通用的方法，相比于上述的方法中间件回显有不需目标出网、没有目录限制等优势。中间件回显的原理简单来说是在运行的中间件中获取request&response对象，通过request对象获取执行参数等后将执行结果写入response对象带出完成回显。已知目标中间件为tomcat，参考feihong师傅公开的tomcat全版本回显测试代码来修改yso代码实现利用。Tomcat回显代码：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777768.png "Tomcat回显代码")

修改yso payload代码：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777770.png "修改yso payload代码")

修改yso Gadgets代码：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777772.png "修改yso Gadgets代码")

实现回显：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197448-1678777775.png "实现回显")

# 总结

由于本菜鸡学习Java的路程不是很系统，在很多地方卡壳严重，还好最终实现了相关exp的编写。最后，感谢文中所用代码和知识的作者师傅们。

# 参考

https://www.cnblogs.com/nice0e3/p/14945707.html

E

N

D

**本文作者：[TideSec](newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197448.html**](https://www.secpulse.com/archives/197448.html)

Tags: [java代码](https://www.secpulse.com/archives/tag/java%E4%BB%A3%E7%A0%81)、[URLDNS](https://www.secpulse.com/archives/tag/urldns)、[Web](https://www.secpulse.com/archives/tag/web-2)、[中间件](https://www.secpulse.com/archives/tag/%E4%B8%AD%E9%97%B4%E4%BB%B6)、[反序列化](https://www.secpulse.com/archives/tag/%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![漏洞挖掘之信息收集](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197320-1678432200-300x214.png)

  漏洞挖掘之信息收集](https://www.secpulse.com/archives/197320.html "详细阅读 漏洞挖掘之信息收集")
* [![靶场攻略 | php反序列化靶机实战](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196076-16766259821-300x216.jpg)

  靶场攻略 | php反序列化靶机实战](https://www.secpulse.com/archives/196076.html "详细阅读 靶场攻略 | php反序列化靶机实战")
* [![MySQL jdbc 反序列化分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195290-1675307076-300x202.png)

  MySQL jdbc 反序列化分析](https://www.secpulse.com/archives/195290.html "详细阅读 MySQL jdbc 反序列化分析")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/43b12cc12b9dbbe6a010c40d69088feb-300x298.png)](https://www.secpulse.com/newpage/author?author_id=26366aaa) | [TideSec ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=26366) | |
| 文章数：145 | 积分： 185 |
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

[EISS-2020企业信息...