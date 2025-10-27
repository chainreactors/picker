---
title: 基于AD Event日志实时检测GPO后门
url: https://www.secpulse.com/archives/190907.html
source: 安全脉搏
date: 2022-11-12
fetch_date: 2025-10-03T22:29:31.546849
---

# 基于AD Event日志实时检测GPO后门

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

# 基于AD Event日志实时检测GPO后门

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Bypass007](https://www.secpulse.com/newpage/author?author_id=6275)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-11

8,593

**01、简介**

在一些勒索病毒的案例中，我们可以看到这样的案例，攻击者通过域控组策略下发勒索病毒加载脚本，从共享服务器下载并执行勒索病毒样本，从而导致内网大规模范围内的病毒感染事件。

在域控这种中央集权系统，通过组策略只需要更改一个组策略对象（GPO），就能影响成千上万的计算机，一旦被恶意利用后果不堪设想。

基于勒索病毒攻击感染的场景，组策略对象（GPO）的敏感操作需要实时监控，这是保持内网安全所必需的。那么，今天我们来分析一下GPO后门的方式，总结规律，制定对应的检测规则。

**02、攻击过程**

通过域控下发并执行脚本/软件，主要有三种方式，分别是添加启动项脚本、添加计划任务以及软件安装。

（1）通过GPO添加启动项脚本

在真实的运维场景中，为了便于管理域环境中计算机本地管理员密码，一般会使用GPO组策略下发脚本来统一修改密码。

将准备后的脚本复制到SYSVOL相应的目录下，打开组策略管理(gpmc.msc)，右键组策略对象，添加登录启动项脚本：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190907-1668149263.png)

Scripts目录包含开关机和登入登出的执行脚本，使用组策略添加开机脚本后，会在Scripts目录下生成scripts.ini。

Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\USER\Scripts\scripts.ini

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image18.png "image18.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image18.png)

（2）通过GPO添加计划任务

在首选项-控制面板设置，找到计划任务进行设置。

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image19.png "image19.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image19.png)

设置计划任务后，对应的配置文件存放在如下的地方：

```
\\evil.com\SYSVOL\evil.com\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\USER\Preferences
```

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image20.png "image20.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image20.png)

（3）通过组策略软件下发

域组策略提供了批量部署软件的功能，在软件安装新建数据包策略后，在Applications目录会生成一个.aas文件。

```
\\evil.com\SYSVOL\evil.com\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\USER\Applications\xxxx.aas
```

![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image21.png "image21.png")

**03、攻击检测**

基于以上攻击事实，我们可以总结出，每当攻击者通过GPO下发恶意策略时，\evil.com\SYSVOL\evil.com\Policies\ 相应的配置文件就会发现变化。

在Windows安全日志中，每次访问网络共享文件时，都会生成相应的审核日志，事件ID为5145，RelativeTargetName对应的是修改的相对目标名称，AccessList的值为%%4417的值所对应的访问权限是WriteData 或 AddFile。通过监视网络共享对象和Accesses权限，可实现GPO组策略后门的实时检测。

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image22.png "image22.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image22.png)

```
index=ad host=WIN-DC01 EventCode=5145 RelativeTargetName IN ("*.aas","*.xml","*scripts.ini") "访问"="WriteData (或 AddFile)"
| stats count min(_time) as  start_time max(_time) as end_time by dest user RelativeTargetName | eval start_time=strftime(start_time,"%Y-%m-%d %H:%M:%S")| eval end_time=strftime(end_time,"%Y-%m-%d %H:%M:%S") |eval message="在"+start_time+"到"+end_time+"时间内，服务器："+dest +" GPO配置文件已被修改" +count+"次，操作账号："+user+",相对目标名称："+RelativeTargetName
|  table start_time end_time user message
```

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image23-1024x328.png "image23-1024x328.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image23.png)

**本文作者：[Bypass007](newpage/author?author_id=6275)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190907.html**](https://www.secpulse.com/archives/190907.html)

Tags: [AD Event](https://www.secpulse.com/archives/tag/ad-event)、[GPO](https://www.secpulse.com/archives/tag/gpo)、[后门](https://www.secpulse.com/archives/tag/%E5%90%8E%E9%97%A8)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![应急响应 | TeamTNT挖矿木马应急溯源分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1679975182208-300x217.png)

  应急响应 | TeamTNT挖矿木马应急…](https://www.secpulse.com/archives/198302.html "详细阅读 应急响应 | TeamTNT挖矿木马应急溯源分析")
* [![基于AD Event日志监测域委派后门](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1675837613234-300x200.png)

  基于AD Event日志监测域委派后门](https://www.secpulse.com/archives/195560.html "详细阅读 基于AD Event日志监测域委派后门")
* [![最实用的应急响应笔记思路总结（附工具）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/1672814178650-300x173.png)

  最实用的应急响应笔记思路总结（附工具）](https://www.secpulse.com/archives/194607.html "详细阅读 最实用的应急响应笔记思路总结（附工具）")

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

[The 2nd AutoCS 2021智能汽车信息安全大会](ht...