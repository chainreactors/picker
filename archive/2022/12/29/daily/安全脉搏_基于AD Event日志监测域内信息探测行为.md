---
title: 基于AD Event日志监测域内信息探测行为
url: https://www.secpulse.com/archives/194230.html
source: 安全脉搏
date: 2022-12-29
fetch_date: 2025-10-04T02:38:45.460912
---

# 基于AD Event日志监测域内信息探测行为

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

# 基于AD Event日志监测域内信息探测行为

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Bypass007](https://www.secpulse.com/newpage/author?author_id=6275)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-28

9,688

**01、简介**

当攻击者获得内网某台域内服务器的权限，就会以此为起始攻击点，尽可能地去收集域的信息，以获取域控权限作为内网的终极目标。例如，攻击者会在内网中收集域管理员用户列表和特定敏感用户的信息，通过定位域管理员以找到最佳攻击路径，从而拿到域管理员权限。

针对域内信息探测的行为，是攻击者入侵的前兆，基于AD Event日志检测攻击者的信息探测行为，就可以预先给安全管理员发出告警，帮助安全管理员找到网络中存在的安全弱点。

**02、域内敏感用户组探测**

（1）查询域管理员用户

```
net group "Domain Admins" /domain
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216831.png)

（2）日志分析：当用户查询管理员组时，会出现4次4661事件，其中两次4661事件的对象类型是SAM\_DOMAIN，另外两次的对象类型是SAM\_GROUP。4661事件：记录了域用户test访问了SAM\_GROUP组的SID，对应的组名就是 Domain Admins，这个就可以作为关键特征。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-16722168311.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216833.png)

（3）检测策略：监测4661事件，找到访问SAM\_GROUP组的SID的用户，并关联到事件4624，找到用户对应的登录IP。如下图：用户test通过192.168.28.20 查询了 domain admins域管理员组信息。

检测示例：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216835.png)

**02、域内敏感用户信息探测**

（1）获取指定域用户的详细信息

```
net user bypass /domain
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-16722168351.png)

（2）日志分析：当用户获取指定域用户的详细信息时，会出现多次4661事件，对象类型是SAM\_USER，SID对应的是帐户的SID，通过日志记录可以看到用户test查看了域用户bypass成员的详细信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216837.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216839.png)

（3）检测策略：监测4661事件，找到访问SAM\_USER组的SID的用户，可以进一步关联test的登录IP以及SID对应的用户名。如下图：用户test在192.168.28.20 查看了域管理员bypass用户的详细信息。

检测示例：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216840.png)

**04、定位域管理员**

（1）使用BloodHound分析域的攻击路径

BloodHound是一款域渗透分析工具，可以使用BloodHound识别高度复杂的域攻击路径，只需要在服务器上运行SharpHound.exe，就可以收集域内信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-16722168401.png)

日志分析：在使用SharpHound收集信息过程中，产生多条5145的事件，服务端的特征重点关注访问的相对名称包含srvsvc、wkssvc、winreg、samr等，对应的事件还记录了请求的用户帐户test，源地址：192.168.28.20。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216842.png)

（2）PVEFindADUser

可用于查找用户登录的服务器，为攻击者提供域管理员所在的位置，为下一步攻击提供必要的信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216846.png)

日志分析：在使用PVEFindADUser收集信息过程中，产生两条5145的事件，访问的相对名称都是 winreg。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216848.png)

（3）PsLoggedOn

PsLoggedOn可以查看本地登陆的用户和通过本地计算机或远程计算机资源登陆的用户。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216851.png)

日志分析：在使用PsLoggedOn收集信息过程中，产生多条5145的事件，访问的相对名称包括 winreg、lsarpc、srvsvc。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216853.png)

（4）检测策略：监测5145事件，重点关注访问相对名称包含srvsvc,wkssvc,winreg,samr,lsarpc的事件，识别出可能的探测行为。

检测示例：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194230-1672216862.png)

**本文作者：[Bypass007](newpage/author?author_id=6275)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/194230.html**](https://www.secpulse.com/archives/194230.html)

Tags: [AD Event](https://www.secpulse.com/archives/tag/ad-event)、[信息探测](https://www.secpulse.com/archives/tag/%E4%BF%A1%E6%81%AF%E6%8E%A2%E6%B5%8B)、[域](https://www.secpulse.com/archives/tag/%E5%9F%9F)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![TLD与常见文件后缀重复引发的安全问题](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684736136728-300x188.png)

  TLD与常见文件后缀重复引发的安全问题](https://www.secpulse.com/archives/200803.html "详细阅读 TLD与常见文件后缀重复引发的安全问题")
* [![基于AD Event日志监测域委派后门](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1675837613234-300x200.png)

  基于AD Event日志监测域委派后门](https://www.secpulse.com/archives/195560.html "详细阅读 基于AD Event日志监测域委派后门")
* [![基于资源的约束委派（RBCD）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/1673427657021.png)

  基于资源的约束委派（RBCD）](https://www.secpulse.com/archives/194821.html "详细阅读 基于资源的约束委派（RBCD）")

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

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autoc...