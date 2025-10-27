---
title: APP代码保护方案原理分析
url: https://www.secpulse.com/archives/197964.html
source: 安全脉搏
date: 2023-03-21
fetch_date: 2025-10-04T10:07:31.603305
---

# APP代码保护方案原理分析

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

# APP代码保护方案原理分析

[移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)

[编码安全](https://www.secpulse.com/newpage/author?author_id=48435)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-03-20

14,886

**0理****解基础1**

Ollvm是现在很多集成用于so文件的代码保护方案，ollvm有几个代码保护方案分别为控制流平坦化、虚假指令、指令替换、字符串加密。这几个保护方案啊是可以通过累加方式进行对so文件保护。

这篇主要分享下ollvm代码保护方案下的控制流平坦化的原理，控制流平坦化它是以基本块为单位，通过一个主分发器来控制程序的执行流程。

控制流平坦化在代码上是指将原程序的正常程序控制流中基本块之间的跳转关系链删除，用一个集中的主分发块来调度基本块的执行顺序。保护后展现出来可以简要地理解为是while+switch的结构，其中的switch可以理解为主分发器。这样通过模糊基本块之间的前后关系，增加静态逆向代码分析的难度。

**原始的if--else结构**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197964-1679292561.png)

**通过ollvm的平坦化保护后的结构**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197964-1679292562.png)

**0平坦化基础1**

我们的代码中每一块的基本块可能会有后继和前驱，总体上的思路就是：先将原始程序的基本块保存下来，找到开头的基本块，分配一个变量switchVar并赋值，在后面添加一个Switch指令，根据switchVar跳转向其他的基本块，然后更新switchVar，让基本块跳转到正确的后继基本块中。

**代码平坦化主要由分发器、虚假块、真实块这三个个基本组成：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197964-1679292563.png)

平坦化后的基本结构图

入口块：进入函数第一个执行的基本块

分发块：负责跳转到下一个要执行的原基本块

原基本块：混淆之前的基本块，实际完成程序工作的真实基本块

返回块：返回到主分发块。

**平坦化的基本实现流程：**1、保存原程序基本块；2、创建分发块和返回块；3、实现分发块的调度；4、实现调度变量的自动调整；5、修复指令和变量

平坦化化修改了代码正常的控制流，这样逆向分析人员就不容易直接的理清程序执行流程，增加静态分析难度。

**0实例分析1**

下面就从个简单的代码进行分析正常的程序流和ollvm的平坦化后的程序流

**![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197964-1679292566.png)**

通过在函数定义后面**添加\_\_attribute((\_\_annotate\_\_((“fla”))))指令**，就可以实现对指定函数对代码进行平坦化保护。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197964-1679292567.png)

就简单的代码程序流，通过平坦化后，从上图中可以看出整个程序基本结构都发生了改变，这里面有虚虚实实的代码块，需要识别你去出哪个是虚假的代码块，哪个是真实的代码块。这无疑给程序的静态分析加大的门槛。

通过平坦化后的代码，实际上真正的代码块都是在最下面一排整齐的排列的代码块中的。前面的流程和结构都是虚假混淆分析的虚假代码块。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197964-1679292569.png)

从上图伪代码中比较，正常的代码逻辑这种很清晰可以还原出逻辑结构，右边的平坦化后的伪代码可以看到，这个伪代码中增加了while、switch的语句，并且新增了个几个变量，这些的增加虚假代码，这大大的强化了静态分析难度。

对于分析这种平坦化保护后的代码，frida和unicorn去动态分析是个不错的选择。

**0小结1**

这个市面上很多产品都采用虚拟机或者基于ollmv的平坦化的混淆保护，有些明明可以将代码保护强度可以设置为很强，但产品所表现出来的是强度相对没那么强。因为这个代码保护混淆后会和执行效率内存开销捆绑的，产品不得不做出一些妥协降低代码保护强度。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197964-1679292570.gif)

结束

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197964-1679292573.gif)

**本文作者：[编码安全](newpage/author?author_id=48435)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197964.html**](https://www.secpulse.com/archives/197964.html)

Tags: [APP代码](https://www.secpulse.com/archives/tag/app%E4%BB%A3%E7%A0%81)、[OLLVM](https://www.secpulse.com/archives/tag/ollvm)、[字符串加密](https://www.secpulse.com/archives/tag/%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%8A%A0%E5%AF%86)、[指令替换](https://www.secpulse.com/archives/tag/%E6%8C%87%E4%BB%A4%E6%9B%BF%E6%8D%A2)、[控制流平坦化](https://www.secpulse.com/archives/tag/%E6%8E%A7%E5%88%B6%E6%B5%81%E5%B9%B3%E5%9D%A6%E5%8C%96)、[虚假指令](https://www.secpulse.com/archives/tag/%E8%99%9A%E5%81%87%E6%8C%87%E4%BB%A4)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Android逆向前期准备](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image51-300x169.png)

  Android逆向前期准备](https://www.secpulse.com/archives/195484.html "详细阅读 Android逆向前期准备")
* [![浅谈android端的字符串加密](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1670318227218-300x208.png)

  浅谈android端的字符串加密](https://www.secpulse.com/archives/193005.html "详细阅读 浅谈android端的字符串加密")
* [![一种高端的APP代码保护方案](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/1666344358807-300x167.png)

  一种高端的APP代码保护方案](https://www.secpulse.com/archives/189584.html "详细阅读 一种高端的APP代码保护方案")

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

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/autho...