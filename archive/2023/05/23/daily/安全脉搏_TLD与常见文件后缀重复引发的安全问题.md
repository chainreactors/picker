---
title: TLD与常见文件后缀重复引发的安全问题
url: https://www.secpulse.com/archives/200803.html
source: 安全脉搏
date: 2023-05-23
fetch_date: 2025-10-04T11:36:47.255277
---

# TLD与常见文件后缀重复引发的安全问题

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

# TLD与常见文件后缀重复引发的安全问题

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-05-22

27,207

***01***

**背景**

近日，谷歌推出了一批新的顶级域（TLD），其中包括.zip和.mov，意味着个人用户可以注册.zip和.mov的顶级域名，很多安全人员对这一举动提出了担忧，认为此举会引入安全隐患。其中讨论最多的是认为新推出的TLD与常用文件后缀重复会让人放松警惕，使得网络钓鱼趁虚而入。

***02***

**分析**

新增的顶级域结合浏览器特性可以让钓鱼链接更加隐蔽：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200803-1684734226.png)

现代浏览器在解析URL时通常有以下部分：协议、用户信息、主机、端口、路径、参数、锚，在很多时候用户信息都是被忽略的，但在某些时候用户信息部分可以用来欺骗钓鱼目标，使其相信点击的链接是可信的。如上图所示，乍一看是github上的一个文件，实际上却是指向https://v0.07.zip，其主要原因在于浏览器在解析unicode字符U+2044和U+2215是不会将其视为/（U+002F），但视觉上很难分辨与/（U+002F）之间的区别。

目前已经存在疑似用于钓鱼的域名：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200803-1684734227.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200803-1684734228.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200803-1684734229.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200803-1684734231.png)

除了用于钓鱼之外也有人使用.zip域名传播zip炸弹，9.4M的文件解压之后会膨胀到281TB。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200803-1684734234.png)

此外，在windows系统的explorer中输入xxxx.zip，如果路径中不存在xxxx.zip时，会直接浏览器中打开xxxx.zip，同时支持带路径和参数访问。这种方式属于正常功能，但也存在被恶意利用的风险。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200803-1684734235.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200803-1684734236.png)

在一些通讯软件和社交网站中也会自动将这类扩展名转换为URL，其中包括QQ、微信等知名通讯软件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200803-16847342361.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200803-1684734237.png)

新TLD可能会成为网络钓鱼组织的新手段，对此，我们应该提高警惕，在打开.mov、.zip链接之前对其仔细研究，如果仍不确定链接是否安全、请不要打开，更不应该在不信任的网站输入个人隐私信息和下载文件。

***03***

**防范建议**

1、保持警惕：在收到任何来自陌生人或未知来源的电子邮件、短信或社交媒体信息时，要保持警惕，不要轻易点击其中的链接或下载其中的附件。

2、验证链接：在点击任何链接之前，应该先将鼠标悬停在链接上，查看链接的真实地址是否与显示的地址相符。如果链接看起来可疑或不可信，请不要点击。

3、使用安全软件：安装和使用安全软件可以帮助防范网络钓鱼攻击。这些软件可以检测和拦截恶意链接和附件，并提供实时保护。

4、加强密码安全：使用强密码，并定期更改密码，可以减少账户被盗用的风险。此外，不要在不安全的网络上使用相同的密码。

5、教育员工：对于企业来说，教育员工如何识别和防范网络钓鱼攻击非常重要。员工应该知道如何验证链接和附件，并且应该知道如何报告可疑的电子邮件或信息。

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/200803.html**](https://www.secpulse.com/archives/200803.html)

Tags: [mov](https://www.secpulse.com/archives/tag/mov)、[TLD](https://www.secpulse.com/archives/tag/tld)、[zip](https://www.secpulse.com/archives/tag/zip)、[域](https://www.secpulse.com/archives/tag/%E5%9F%9F)、[常用文件后缀重复](https://www.secpulse.com/archives/tag/%E5%B8%B8%E7%94%A8%E6%96%87%E4%BB%B6%E5%90%8E%E7%BC%80%E9%87%8D%E5%A4%8D)、[网络钓鱼](https://www.secpulse.com/archives/tag/%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![【盗币科普】你可千万不能这样盗别人的虚拟货币钱包](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1681436744151-300x180.png)

  【盗币科普】你可千万不能这样盗别人的虚拟…](https://www.secpulse.com/archives/198953.html "详细阅读 【盗币科普】你可千万不能这样盗别人的虚拟货币钱包")
* [![以ChatGPT为主题的网络钓鱼攻击劫持Facebook账户分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197831-1679039318-300x191.png)

  以ChatGPT为主题的网络钓鱼攻击劫持…](https://www.secpulse.com/archives/197831.html "详细阅读 以ChatGPT为主题的网络钓鱼攻击劫持Facebook账户分析")
* [![基于AD Event日志监测域委派后门](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1675837613234-300x200.png)

  基于AD Event日志监测域委派后门](https://www.secpulse.com/archives/195560.html "详细阅读 基于AD Event日志监测域委派后门")

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

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp.weixin.qq.com/s/kXt5PAD3bPcHUZjl6rziCw)

#### 20...