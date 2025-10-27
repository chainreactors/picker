---
title: 众至科技发布11月漏洞通告 | OpenSSL缓冲区溢出漏洞；Spring Security 绕过授权漏洞
url: https://www.secpulse.com/archives/190558.html
source: 安全脉搏
date: 2022-11-08
fetch_date: 2025-10-03T21:54:55.830731
---

# 众至科技发布11月漏洞通告 | OpenSSL缓冲区溢出漏洞；Spring Security 绕过授权漏洞

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

# 众至科技发布11月漏洞通告 | OpenSSL缓冲区溢出漏洞；Spring Security 绕过授权漏洞

[漏洞](https://www.secpulse.com/archives/category/vul)

[众至科技](https://www.secpulse.com/newpage/author?author_id=46034)

2022-11-07

8,909

##### **【漏洞通告】 OpenSSL缓冲区溢出漏洞**

###### **基础信息**

|  |  |
| --- | --- |
| CVE | CVE-2022-3602 |
| 等级 | 高危 |
| 类型 | 缓冲区溢出 |

###### **漏洞详情**

11月1日，OpenSSL项目发布安全公告，修复了OpenSSL中的2个缓冲区溢出漏洞（CVE-2022-3602和CVE-2022-3786），详情如下：

CVE-2022-3602：X.509电子邮件地址4字节缓冲区溢出漏洞

由于OpenSSL 3.0.0 - 3.0.6版本中在X.509证书验证中存在缓冲区溢出漏洞，可以通过制作恶意电子邮件地址以溢出堆栈上的4个字节，成功利用此漏洞可能导致拒绝服务或远程代码执行。

CVE-2022-3786：X.509电子邮件地址可变长度缓冲区溢出漏洞

由于OpenSSL 3.0.0 - 3.0.6版本中在X.509证书验证中存在缓冲区溢出漏洞，可以通过在证书中制作恶意电子邮件地址以溢出堆栈中包含“.”字符（十进制46）的任意字节数，成功利用此漏洞可能导致拒绝服务。

###### **影响范围**

OpenSSL 版本 3.0.0 - 3.0.6

###### **安全建议**

目前OpenSSL项目已经修复了这些漏洞，受影响用户可以更新到以下版本：

OpenSSL 3.0版本用户：升级到 OpenSSL 版本3.0.7。

下载链接：

https://www.openssl.org/source/

###### **参考链接**

https://www.openssl.org/blog/blog/2022/11/01/email-address-overflows/

https://www.openssl.org/news/secadv/20221101.txt

##### **【漏洞通告】 Spring Security 绕过授权漏洞**

###### **基础信息**

|  |  |
| --- | --- |
| CVE | CVE-2022-31692 |
| **等级** | **高危** |
| **类型** | **访问控制** |

###### **漏洞详情**

Spring Security 是一套为基于Spring的应用程序提供说明性安全保护的安全框架。

Spring Security 受影响版本可能容易受到通过 FORWARD 或 INCLUDE 调度绕过授权规则的影响。

当满足以下所有条件时，应用程序很容易受到攻击：

应用程序期望 Spring Security 应用安全性来转发和包含调度程序类型。

应用程序手动或通过 authorizeHttpRequests() 方法使用 AuthorizationFilter。

应用程序配置 FilterChainProxy 以应用于转发和/或包含请求（例如 spring.security.filter.dispatcher-types = request, error, async, forward, include）。

应用程序将请求转发/包含到更高权限的安全端点。

应用程序通过 authorizeHttpRequests().shouldFilterAllDispatcherTypes(true) 配置 Spring Security 以应用于每个调度程序类型

如果符合以下任意一项，则应用程序不会受到攻击：

应用程序不使用 authorizeHttpRequests() 或 AuthorizationFilter。

该应用程序不转发/包含请求。

应用程序不需要配置 Spring Security 来应用转发或包含调度器类型。

###### **影响范围**

受影响版本：

5.7.0 <= Spring Security <= 5.7.4

5.6.0 <= Spring Security <= 5.6.8

安全版本：

Spring Security >= 5.7.5

Spring Security >= 5.6.9

###### **安全建议**

1、建议升级至安全版本及其以上

2、若无法升级，建议按照 https://tanzu.vmware.com/security/cve-2022-31692 中相关方案自行排查改造

###### **参考链接**

https://tanzu.vmware.com/security/cve-2022-31692

**本文作者：[众至科技](newpage/author?author_id=46034)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190558.html**](https://www.secpulse.com/archives/190558.html)

Tags: [CVE-2022-3602](https://www.secpulse.com/archives/tag/cve-2022-3602)、[CVE-2022-3786](https://www.secpulse.com/archives/tag/cve-2022-3786)、[OpenSSL缓冲区溢出漏洞](https://www.secpulse.com/archives/tag/openssl%E7%BC%93%E5%86%B2%E5%8C%BA%E6%BA%A2%E5%87%BA%E6%BC%8F%E6%B4%9E)

点赞：
3
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

[相约本地生活安全沙龙暨白帽子颁奖典礼](https://www.bagevent.com/event/6241320)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](http...