---
title: KeePass 内存泄露主密码漏洞分析
url: https://www.secpulse.com/archives/201711.html
source: 安全脉搏
date: 2023-06-13
fetch_date: 2025-10-04T11:44:14.137751
---

# KeePass 内存泄露主密码漏洞分析

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

# KeePass 内存泄露主密码漏洞分析

[漏洞](https://www.secpulse.com/archives/category/vul)

[洞源实验室](https://www.secpulse.com/newpage/author?author_id=49765)

2023-06-12

10,751

**漏洞背景**

0x00

KeePass是一款开源密码管理软件。它旨在帮助用户存储和管理他们的密码和敏感信息，以便安全地访问各种在线服务和应用程序。

KeePass提供一个安全的数据库，其中可以存储用户名、密码、网站链接、附加说明和其他自定义字段。这些信息被加密保护，并需要一个主密码或密钥文件才能解锁和访问。

**漏洞信息**

0x01

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201711-1686547467.png)

**漏洞影响**

0x02

该漏洞存在于2.54之前的KeePass2.x版本中。成因是由于KeePass文本框内容输入时，会在其进程内存中创建托管字符串，如果将其内存进行转储，则会导致主密码泄露问题。

**漏洞分析**

0x03

笔者选择KeePass2.53.1版本进行漏洞分析与验证。

首先输入了14个字符的主密码。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201711-1686547468.png)

产生漏洞的代码在KeePass/UI/SecureTextBoxEx.cs文件中。首先在输入过程中，.NET CLR执行代码的时候，会产生托管字符串，输入的字符会以明文存储在内存中，而该字符之前输入的字符会是以chPasswordChar用来占位。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201711-1686547470.png)

根据PasswordCharEx的定义，64位机器的占位符为xCFx25。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201711-1686547471.png)

在输入密码后，对进程进行内存转储。笔者使用Windows任务管理器创建了该进程的转储文件。

随后使用二进制编辑器打开DMP文件。根据已知的信息搜索占位符xCFx25。如下图所示发现首先出现的是一个占位符，随后是明文字符E。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201711-1686547473.png)

继续搜索，发现此时出现了两个占位符，随后是明文字符S。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201711-16865474731.png)

按照上述搜索方法慢慢搜索，发现占位符从1个递增到了13个，每一串占位符后都有一个明文，如下图是13个占位符，最后的明文是G。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201711-1686547475.png)

使用自动化分析工具发现其占位符+明文的二进制数据得出的结果为{UNKNOWN}EST<{\_, B}><{B, Y}>Y\_INSBUG。其给出了4种可能的结果，而EST\_BY\_INSBUG这个结果是笔者所输入的14位密码中的后13个字符。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201711-1686547476.png)

综上所述，在设置主密码的文本框输入一串密码，除密码第一位无法从内存中获取外，其余的每一位字符在内存中均以占位符+明文字符的托管字符串形式存储。如果输入123，内存中能获取的托管字符串具体形式如下：

1、xCFx25x32

2、xCFx25xCFx25x33

在Mono（可以让.NET应用程序运行Linux、macOS下）平台下，KeePass2.x也可以运行，并且同样存在该问题，所以根源问题可能与.NET CLR相关。

**修复方法**

0x04

KeePass开发者对源码的修复方案如下：

1、在 Windows 上运行时，KeePass 现在调用 Windows API 函数来直接获取/设置文本框的文本，以避免创建托管字符串。对于大多数长度，“●...●?”的托管字符串不再出现在进程内存中，但对于一些长度，仍然有一个托管字符串。（可能是WindowsAPI函数也会创建一个缓冲区）

2、KeePass 现在在进程内存中创建一些虚拟片段（包含随机字符的随机片段，其长度约为当前密码的长度）。有了这个，确定正确的托管字符串应该会更加困难。

用户可通过https ://keepass.info/filepool/KeePass\_230507.zip下载未签名的修复版本进行修复。或是等待下载开发者更新的5.24稳定版本。

**本文作者：[洞源实验室](newpage/author?author_id=49765)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/201711.html**](https://www.secpulse.com/archives/201711.html)

Tags: [KeePass](https://www.secpulse.com/archives/tag/keepass)、[主密码](https://www.secpulse.com/archives/tag/%E4%B8%BB%E5%AF%86%E7%A0%81)、[内存泄露主密码漏洞](https://www.secpulse.com/archives/tag/%E5%86%85%E5%AD%98%E6%B3%84%E9%9C%B2%E4%B8%BB%E5%AF%86%E7%A0%81%E6%BC%8F%E6%B4%9E)、[开源密码管理软件](https://www.secpulse.com/archives/tag/%E5%BC%80%E6%BA%90%E5%AF%86%E7%A0%81%E7%AE%A1%E7%90%86%E8%BD%AF%E4%BB%B6)、[漏洞](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E)

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/26/494834f404f48769dcb680f30320c212-300x276.png)](https://www.secpulse.com/newpage/author?author_id=49765aaa) | [洞源实验室](https://www.secpulse.com/newpage/author?author_id=49765) | |
| 文章数：8 | 积分： 0 |
| 供应链检测中心旗下实验室，专注供应链安全、产品测评、漏洞研究、代码审计 | |

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

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.come...