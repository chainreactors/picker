---
title: 基于AD Event日志监测AdminSDHolder
url: https://www.secpulse.com/archives/195575.html
source: 安全脉搏
date: 2023-02-09
fetch_date: 2025-10-04T06:04:33.260936
---

# 基于AD Event日志监测AdminSDHolder

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

# 基于AD Event日志监测AdminSDHolder

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Bypass007](https://www.secpulse.com/newpage/author?author_id=6275)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-02-08

7,458

**01、简介**

AdminSDHolder是一个特殊的AD容器，通常作为某些特权组成员的对象的安全模板。Active Directory将采用AdminSDHolder对象的ACL并定期将其应用于所有受保护的AD账户和组，以防止意外和无意的修改并确保对这些对象的访问是安全的。如果攻击者能完全控制AdminSDHolder，那么它就能同时控制域内的许多组，这可以作为域内权限维持的方法。

基于AD Event日志监测AdminSDHolder对象ACL的修改行为，从而发现可疑的修复AdminSDHolder对象行为。

**02、利用方式**

（1）AdminSDHolder对象添加ACL

使用PowerView，下载地址如下：

```
https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1
```

添加用户bypass对AdminSDHolder的完全访问权限，命令如下：

```
Add-ObjectAcl -TargetADSprefix 'CN=AdminSDHolder,CN=System' -PrincipalSamAccountName bypass -Verbose -Rights All
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195575-1675838920.png)

（2）执行SDProp

默认情况下，SDProp进程每60分钟在域控制器上运行一次，SDProp将域的AdminSDHolder对象的权限与域中受保护的帐户和组的权限进行比较，如果任何受保护帐户和组的权限与AdminSDHolder对象的权限不匹配，则将受保护帐户和组的权限重置为与域的AdminSDHolder对象的权限匹配。

配置完成后ACL 中的更改将在 60 分钟后自动传播，可通过更改注册表的方式设置SDProp 的时间间隔，该值的范围是从60到7200，单位为秒，键类型为DWORD可以直接使用命令行更改：

```
reg add hklmSYSTEMCurrentControlSetServicesNTDSParameters /v AdminSDProtectFrequency /t REG_DWORD /d 60
```

 （3）登录bypass用户，可疑看到bypass非域管用户，却可以将自己添加到“域管理员”组。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195575-1675838921.png)

**03、攻击检测**

攻击手法的核心点在于需要修改AdminSDHolder的ACL，因此我们只需要检测对AdminSDHolder的ACL的修改行为即可，可以通过5136日志来监控。

**5136事件**：每次修改 Active Directory 对象时，都会生成此事件，包含帐户名称、目录服务对象名称、操作类型。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195575-1675838922.png)

安全规则：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195575-1675838924.png)

**本文作者：[Bypass007](newpage/author?author_id=6275)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195575.html**](https://www.secpulse.com/archives/195575.html)

Tags: [ACL](https://www.secpulse.com/archives/tag/acl)、[AD Event日志](https://www.secpulse.com/archives/tag/ad-event%E6%97%A5%E5%BF%97)、[AdminSDHolder](https://www.secpulse.com/archives/tag/adminsdholder)、[AD容器](https://www.secpulse.com/archives/tag/ad%E5%AE%B9%E5%99%A8)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Windows自带的持久化后门——SDDL](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201392-1685958844-300x192.png)

  Windows自带的持久化后门——SDD…](https://www.secpulse.com/archives/201392.html "详细阅读 Windows自带的持久化后门——SDDL")
* [![基于AD Event日志检测哈希传递攻击](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1671003502213-300x200.png)

  基于AD Event日志检测哈希传递攻击](https://www.secpulse.com/archives/193527.html "详细阅读 基于AD Event日志检测哈希传递攻击")
* [![如何在Windows AD域中驻留ACL后门](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1670395172729-300x196.png)

  如何在Windows AD域中驻留ACL…](https://www.secpulse.com/archives/193028.html "详细阅读 如何在Windows AD域中驻留ACL后门")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2018/03/535dc13ea81e426db897effda78f9aac-290x290.png)](https://www.secpulse.com/newpage/author?author_id=6275aaa) | [Bypass007 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=6275) | |
| 文章数：94 | 积分： 218 |
| 一个网络安全爱好者，对技术有着偏执狂一样的追求。 | |

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

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

##...