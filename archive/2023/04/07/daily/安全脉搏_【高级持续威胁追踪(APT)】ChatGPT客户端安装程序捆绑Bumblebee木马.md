---
title: 【高级持续威胁追踪(APT)】ChatGPT客户端安装程序捆绑Bumblebee木马
url: https://www.secpulse.com/archives/198647.html
source: 安全脉搏
date: 2023-04-07
fetch_date: 2025-10-04T11:30:04.859414
---

# 【高级持续威胁追踪(APT)】ChatGPT客户端安装程序捆绑Bumblebee木马

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

# 【高级持续威胁追踪(APT)】ChatGPT客户端安装程序捆绑Bumblebee木马

[资讯](https://www.secpulse.com/archives/category/news)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-04-06

11,999

**概述**

各行各业都在关注如何利用ChatGPT来提升自己的工作效率，全球的一些热点事件也是攻击者比较关注的，攻击者往往会利用热点事件进行钓鱼攻击，深信服蓝军APT研究团队一直在关注全球攻击者使用的各种新型攻击手段、攻击武器与全球最新的攻击事件，近日捕获到一例利用ChatGPT客户端安装程序捆绑Bumblebee(大黄蜂)的恶意攻击样本，疑似攻击者利用ChatGPT热点进行钓鱼攻击活动，针对这款新型的攻击活动样本进行了相关技术分析。

BumbleBee是一种新型的恶意软件程序，最初由Google威胁分析小组于2022年3月首次报告，谷歌威胁分析团队追踪为Conti组织提供初始化访问的团伙时，发现了新的木马家族。该木马与C2服务器通信时会使用特殊代号“bumblebee”作为User-Agent字段，因此将其命名为Bumblebee(大黄蜂)，该恶意软件去年非常活跃，与全球几个顶级的网络犯罪组织和勒索病毒组织都有一些联系，去年主要利用VHD、ISO或IMG等作为载体通过钓鱼邮件攻击传播，今年发现该恶意软件还利用OneNote文档作为载体进行传播，攻击手法更新非常之快。

**分析**

1.该攻击样本与ChatGPT客户端安装程序进行捆绑，并使用有效的数字签名，数字签名信息，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198647-1680761981.png)

2.样本解压之后，包含两个文件，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198647-1680761982.png)

3.运行该攻击样本之后，前端会显示安装ChatGPT客户程序，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198647-1680761983.png)

4.同时在后台会执行恶意安装脚本，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198647-16807619831.png)

5.恶意安装脚本，部分代码，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198647-1680761985.png)

6.对恶意脚本进行解密之后，部分代码，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198647-1680761987.png)

7.在内存中加载执行Bumblebee木马后门，Bumblebee木马调用入口部分代码，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198647-1680761988.png)

8.C2列表解密函数，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198647-1680761989.png)

9.解密出来的C2地址列表，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198647-1680761990.png)

10.利用解密脚本进行解密，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198647-1680761993.png)

C2列表里面包含很多IP和PORT信息，很多信息是无效了，真实的PORT在前面已经解密出来,对应的端口号为443。

**IOCS**

**HASH**

6F7E07B84897CCCAB30594305416D36F

B4153C305F599325177FC402C696C4F9

**IP & PORT**

45.61.187.225:443

91.206.178.68:443

193.109.120.252:443

**URL**

hxxps://gissa-dev.com/ChatGPT\_Setup.msi

**参考链接**

https://malpedia.caad.fkie.fraunhofer.de/details/win.bumblebee

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/198647.html**](https://www.secpulse.com/archives/198647.html)

Tags: [443](https://www.secpulse.com/archives/tag/443)、[apt](https://www.secpulse.com/archives/tag/apt)、[Bumblebee](https://www.secpulse.com/archives/tag/bumblebee)、[Bumblebee木马](https://www.secpulse.com/archives/tag/bumblebee%E6%9C%A8%E9%A9%AC)、[ChatGPT](https://www.secpulse.com/archives/tag/chatgpt)、[木马](https://www.secpulse.com/archives/tag/%E6%9C%A8%E9%A9%AC)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![某查询和短信轰炸样本的分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/6cd475e953cba46a99ac1b9196993cc-300x239.png)

  某查询和短信轰炸样本的分析](https://www.secpulse.com/archives/203338.html "详细阅读 某查询和短信轰炸样本的分析")
* [![EISS-2023企业信息安全峰会之北京站（05.25/周四-05.26/周五）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199807-1683178691-300x200.jpeg)

  EISS-2023企业信息安全峰会之北京…](https://www.secpulse.com/archives/199807.html "详细阅读 EISS-2023企业信息安全峰会之北京站（05.25/周四-05.26/周五）")
* [![Cursor IDE装上ChatGPT，彻底炸裂！](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199582-1682402430-300x144.png)

  Cursor IDE装上ChatGPT，…](https://www.secpulse.com/archives/199582.html "详细阅读 Cursor IDE装上ChatGPT，彻底炸裂！")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/08/16/9f4b1a0a8978eebf651bfe827b4d307a-300x255.jpeg)](https://www.secpulse.com/newpage/author?author_id=9241aaa) | [Further\_eye ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=9241) | |
| 文章数：319 | 积分： 2105 |
| 深信服科技旗下安全实验室，致力于网络安全攻防技术的研究和积累，深度洞察未知网络安全威胁，解读前沿安全技术。 | |

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

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp....