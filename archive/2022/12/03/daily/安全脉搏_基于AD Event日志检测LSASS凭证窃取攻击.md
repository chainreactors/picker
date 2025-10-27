---
title: 基于AD Event日志检测LSASS凭证窃取攻击
url: https://www.secpulse.com/archives/192703.html
source: 安全脉搏
date: 2022-12-03
fetch_date: 2025-10-04T00:23:04.189994
---

# 基于AD Event日志检测LSASS凭证窃取攻击

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

# 基于AD Event日志检测LSASS凭证窃取攻击

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Bypass007](https://www.secpulse.com/newpage/author?author_id=6275)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-02

8,604

**01、简介**

简单介绍一下，LSASS（本地安全机构子系统服务）在本地或域中登录Windows时，用户生成的各种凭证将会存储在LSASS进程的内存中，以便用户不必每次访问系统时重新登录。

攻击者在获得起始攻击点后，需要获取目标主机上的相关凭证，以便通过用户凭证进行横向移动，这个技术点最容易关联到的就是获取LSASS内存中保存的用户凭证。

一般LSASS窃取凭证有两种方式，第一种就是直接从LSASS内存解析获取密码，第二种是将LSASS进程转储到本地进行离线解析。

**02、LSASS窃取凭证**

**（1）mimikatz**

mimikatz仅需一行命令，就可以直接从lsass内存中提取用户hash。

```
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "exit" > log.txt
```

在众多的Windows安全日志中，通过监测访问lsass,exe的进程，可发现异常进程，因此可以将事件ID:4663 作为关键日志特征。

事件ID:4663 显示已使用访问权限，4663是没有失败事件的，可以看到进程名mimikatz.exe 尝试访问内存对象lsass.exe。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192703-1669961204.png)

**（2）Procdump转储**

procdump是微软官方提供的一个小工具，可以将lsass.exe进程转储为dump文件，将lsass.dmp文件下载到本地进行离线破解。

```
Procdump64.exe -accepteula -ma lsass.exe lsass.dmp
```

在Windows事件ID:4663 中，可以看到进程名Procdump64.exe 尝试访问内存对象lsass.exe。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192703-16699612041.png)

**（3）MSF中的mimikatz**

MSF加载mimikatz模块，抓取明文密码

```
meterpreret > load mimikatz
meterpreret > wdigest
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192703-1669961207.png)

在Windows事件ID:4663 中，可以看到进程名shell.exe 尝试访问内存对象lsass.exe。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192703-1669961209.png)

**（4）CS模块获取用户哈希**

使用hashdump或logopasswords 获取用户密码哈希值

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192703-1669961212.png)

在Windows事件ID:4663 中，可以看到进程名rundll32.exe 尝试访问内存对象lsass.exe。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192703-1669961213.png)

**03、LSASS凭证窃取攻击检测**

基于几种常见的LSASS进程窃取凭证的方式以及识别到的AD Event日志特征，可以实时监测异常进程访问lsass,exe，找到哪个用户什么时间执行了异常进程访问了lsass.exe进程，从而实现LSASS凭证窃取攻击的检测。

```
eventtype=wineventlog_security  EventCode=4663 Object_Name="*lsass.exe"
| regex process="^((?!MsMpEng|vmtoolsd|VsTskMgr|WmiPrvSE).)*$"| stats count  min(_time) as  start_time max(_time) as end_time by  dest user Object_Name Process_Name
| eval start_time=strftime(start_time,"%Y-%m-%d %H:%M:%S")| eval end_time=strftime(end_time,"%Y-%m-%d %H:%M:%S") |eval message="在"+start_time+"到"+end_time+"时间内，服务器："+dest +" 检测到lsass窃取凭证,进程名:" +Process_Name+" 操作账号:"+user+" 操作次数："+count+"次"
|table  start_time end_time dest  message user
```

安全告警效果如下图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192703-1669961214.png)

**本文作者：[Bypass007](newpage/author?author_id=6275)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/192703.html**](https://www.secpulse.com/archives/192703.html)

Tags: [LSASS](https://www.secpulse.com/archives/tag/lsass)、[mimikatz](https://www.secpulse.com/archives/tag/mimikatz)、[msf](https://www.secpulse.com/archives/tag/msf)、[procdump](https://www.secpulse.com/archives/tag/procdump)

点赞：
5
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![MySQL数据库安全测试](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684133717094-300x188.png)

  MySQL数据库安全测试](https://www.secpulse.com/archives/200243.html "详细阅读 MySQL数据库安全测试")
* [![内网主机探测工具合集](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1683871839274-300x187.png)

  内网主机探测工具合集](https://www.secpulse.com/archives/200250.html "详细阅读 内网主机探测工具合集")
* [![基于AD Event日志检测哈希传递攻击](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1671003502213-300x200.png)

  基于AD Event日志检测哈希传递攻击](https://www.secpulse.com/archives/193527.html "详细阅读 基于AD Event日志检测哈希传递攻击")

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

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/c...