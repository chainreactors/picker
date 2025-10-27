---
title: 众至科技漏洞通告 | Atlassian Crowd and Crowd Data Center 权限绕过漏洞；Bitbucket Server and Data Center 远程命令执行漏洞
url: https://www.secpulse.com/archives/192575.html
source: 安全脉搏
date: 2022-12-01
fetch_date: 2025-10-04T00:10:02.108085
---

# 众至科技漏洞通告 | Atlassian Crowd and Crowd Data Center 权限绕过漏洞；Bitbucket Server and Data Center 远程命令执行漏洞

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

# 众至科技漏洞通告 | Atlassian Crowd and Crowd Data Center 权限绕过漏洞；Bitbucket Server and Data Center 远程命令执行漏洞

[漏洞](https://www.secpulse.com/archives/category/vul)

[众至科技](https://www.secpulse.com/newpage/author?author_id=46034)

2022-11-30

8,651

##### **【漏洞通告】Atlassian Crowd and Crowd Data Center 权限绕过漏洞**

###### 1. **基础信息**

|  |  |
| --- | --- |
| CVE | CVE-2022-43782 |
| 等级 | 高危 |
| 类型 | 权限绕过 |

###### 2. **漏洞详情**

Atlassian Crowd和Atlassian Crowd Data Center都是澳大利亚Atlassian公司的产品。Atlassian Crowd是一套基于Web的单点登录系统。该系统为多用户、网络应用程序和目录服务器提供验证、授权等功能。Atlassian Crowd Data Center是Crowd的集群部署版。

CVE-2022-43782 中，Atlassian Crowd和Atlassian Crowd Data Center 3.0 版本及其之后在同时满足以下条件时受影响：

1、Atlassian Crowd和Atlassian Crowd Data Center 为新安装版本，即从 https://www.atlassian.com/software/crowd/download/data-center 下载安装，而不是从旧版本升级而来。

2、在Atlassian Crowd和Atlassian Crowd Data Center Remote Address 配置中增加了IP，默认情况下为空

在同时满足以上两个条件的情况下，攻击者可从相关IP地址调用Atlassian Crowd和Atlassian Crowd Data Center usermanagement REST API，而无需通过密码身份认证，执行任意敏感操作。

###### 3. **影响范围**

Crowd 3.0.0 - Crowd 3.7.2

Crowd 4.0.0 - Crowd 4.4.3

Crowd 5.0.0 - Crowd 5.0.2

###### **4.安全建议**

官方已发布安全更新，若您Crowd满足详情中两个条件，建议升级至安全版本及其以上，其中 Crowd 3.0 系列已停止支持，建议升级至 Crowd 5.x/4.x 系列。

###### **5.参考链接**

https://confluence.atlassian.com/crowd/crowd-security-advisory-november-2022-1168866129.html

##### **【漏洞通告】Bitbucket Server and Data Center 远程命令执行漏洞**

###### 1. **基础信息**

|  |  |
| --- | --- |
| CVE | CVE-2022-43781 |
| **等级** | **高危** |
| **类型** | **命令执行** |

###### 2. **漏洞详情**

 Bitbucket Server或者Data Center中存在使用环境变量的命令注入漏洞。具有控制用户名权限的攻击者可以利用此问题在系统上执行代码。Bitbucket Server和Data Center 7.0版中引入了此漏洞。在开启了注册功能的情况下，攻击者可通过注册用户前台执行任意命令。若Bitbucket Server/Data Center 使用PostgreSQL 作为数据库，则不受该漏洞影响。

###### 3. **影响范围**

7.0.0 ≤ version < 7.6.19

7.7.0 ≤ version < 7.17.12

7.18.0 ≤ version < 7.21.6

7.22.0 ≤ version < 8.0.5

8.1.0 ≤ version < 8.1.5

8.2.0 ≤ version < 8.2.4

8.3.0 ≤ version < 8.3.3

8.4.0 ≤ version < 8.4.2

###### **4.安全建议**

1、官方已发布安全更新，建议升级至安全版本及其以上。

2、若暂无法升级，建议关闭前台注册功能。

###### **5.参考链接**

https://confluence.atlassian.com/bitbucketserver/bitbucket-server-and-data-center-security-advisory-2022-11-16-1180141667.html

**本文作者：[众至科技](newpage/author?author_id=46034)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/192575.html**](https://www.secpulse.com/archives/192575.html)

Tags: [Atlassian Crowd](https://www.secpulse.com/archives/tag/atlassian-crowd)、[Atlassian Crowd Data Center](https://www.secpulse.com/archives/tag/atlassian-crowd-data-center)、[CVE-2022-43781](https://www.secpulse.com/archives/tag/cve-2022-43781)、[CVE-2022-43782](https://www.secpulse.com/archives/tag/cve-2022-43782)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![【漏洞预警】Atlassian Crowd 安全配置错误漏洞](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/1669000267119-300x141.png)

  【漏洞预警】Atlassian Crow…](https://www.secpulse.com/archives/191788.html "详细阅读 【漏洞预警】Atlassian Crowd 安全配置错误漏洞")
* [![Solon框架模板漏洞深度剖析与修复实战](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/7266edd7-a4cc-444d-bacb-7ee802487ac4.png)

  Solon框架模板漏洞深度剖析与修复实战](https://www.secpulse.com/archives/206316.html "详细阅读 Solon框架模板漏洞深度剖析与修复实战")
* [![路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202503171628715.png)

  路由器安全研究：D-Link DIR-8](https://www.secpulse.com/archives/206007.html "详细阅读 路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/06/02/f5f18ac4ab301c81c0f4c2019436d31f-300x298.png)](https://www.secpulse.com/newpage/author?author_id=46034aaa) | [众至科技](https://www.secpulse.com/newpage/author?author_id=46034) | |
| 文章数：5 | 积分： 0 |
| 网络安全保险科技创新引领者 | |

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

[相约本地生活安全沙龙暨白帽子颁奖典礼](https://www....