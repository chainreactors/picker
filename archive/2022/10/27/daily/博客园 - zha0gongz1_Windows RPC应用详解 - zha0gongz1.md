---
title: Windows RPC应用详解 - zha0gongz1
url: https://www.cnblogs.com/H4ck3R-XiX/p/16830473.html
source: 博客园 - zha0gongz1
date: 2022-10-27
fetch_date: 2025-10-03T20:58:27.962286
---

# Windows RPC应用详解 - zha0gongz1

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/zha0gongz1/)

# [zha0gongz1](https://www.cnblogs.com/zha0gongz1)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/zha0gongz1/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/zha0gongz1)
* 订阅
* [管理](https://i.cnblogs.com/)

# [Windows RPC应用详解](https://www.cnblogs.com/zha0gongz1/p/16830473.html "发布于 2022-10-26 22:46")

RPC（远程过程调用）并不是Windows独有的概念，RPC的第一个实现是在unix上；RPC在Windows上的设计是一种强大、健壮、高效且“安全”的进程间通信 (IPC) 机制，它支持数据交换和调用驻留在不同进程中的功能。不同的进程可以在同一台机器上、局域网上或互联网上。简单说它允许请求操作另一台计算机上的服务，而无需了解背后的详细信息。

## 1.介绍

[RPC](https://learn.microsoft.com/en-us/windows/win32/rpc/how-rpc-works)，全称“Remote Procedure Call”，即远程过程调用，它并不是Windows独有的概念，RPC的第一个实现是在unix上；RPC在Windows上的设计是一种强大、健壮、高效且“安全”的进程间通信 (IPC) 机制，它支持数据交换和调用驻留在不同进程中的功能。不同的进程可以在同一台机器上、局域网上或互联网上。简单说它允许请求操作另一台计算机上的服务，而无需了解背后的详细信息。
RPC的通讯架构如下图：

![](https://img2022.cnblogs.com/blog/1449167/202210/1449167-20221026224215561-476624730.png)

这个协议在历史上已经有很多有趣的发现，从各种Abuse到RCE以及LPE，在红队项目的内网渗透中频频出现。

## 2.探测远程机器信息

### 2.1 探测网卡信息

作为渗透测试人员，尽量了解更多的目标内部网络情况是再好不过的，得到的各类信息能够帮助确认潜在的风险。

通过IOXIDResolver接口的ServerAlive2方法可以让我们无需认证直接获取对应主机的网卡信息。

![](https://img2022.cnblogs.com/blog/1449167/202210/1449167-20221027104955331-1782187244.png)

这也是安全测试过程中比较常用的用来确定是否存在“双网卡”主机的方式。

### 2.2 探测主机软件信息

epmapper (MS-RPC EndPoint Mapper)，是RPC架构中的一个服务之一，负责列出公开接口；它会将服务映射到端口。我们可以通过列出的公开接口，来探测对应主机上的应用服务，如使用Impacket中的rpcdump.py即可获取接口的[UUID](https://baike.baidu.com/item/UUID/5921266?fr=aladdin)。

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120180509093-1060822205.png)

如某安全防护软件会在epmapper服务中注册一个接口：

![](https://img2022.cnblogs.com/blog/1449167/202210/1449167-20221027105324521-1553463310.png)

通过rpcdump.py探测该机器发现存在此UUID：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120180549219-559266880.png)

所以此类工具就可以探测目标主机是否存在此款防护软件，同样的可以扩展到探测是否存在其他的在epmapper注册过接口的主机应用程序。

如SentineOne EDR

![](https://img2022.cnblogs.com/blog/1449167/202210/1449167-20221027105616190-827063215.png)

### 2.3 RPC over SMB

MS-RPC服务还可以通过不同的传输协议访问，其中通过SMB传输的RPC服务可以通过命名管道访问，可以对某些机器进行SMB空会话连接的话（比较少见）还可以使用更多RPC接口搜集信息，这也导致了可以利用这个特点进行一些信息的探测。

常见的情况是如果红队人员在目标内网有一个落脚点以及得到一份域凭据就可以使用这种方式连接DC进行一些RPC接口调用，从而探测有价值的域信息；使用该种方法比执行一些NET类收集命令有更好的规避性。

Samba Suite中提供了一个工具：rpcclient，它是执行客户端 MS-RPC 功能的工具。

```
rpcclient [-A authfile] [-c <command string>] [-d debuglevel] [-l logdir] [-N] [-s <smb config file>] [-U username[%password]] [-W workgroup] [-I destinationIP] {server}
```

rpcclient支持以下类别的RPC调用：LSARPC,LSARPC-DS,REG,SRVSVC,SAMR,SPOOLSS,NETLOGON,FSRVP，可以进行多个方面的信息搜集，以下几个例子：

获取域信息：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120181123031-574717224.png)

获取权限：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120181133209-108669122.png)

还可以枚举RID、创建用户、枚举域用户、探测内网出网情况等等。

## 3.使用MS-SAMR操作用户

MS-SAMR，该协议支持包含用户和组的帐户存储或目录的管理功能。该协议的目标是使 IT 管理员和用户能够管理用户、组和计算机。如协议所述，MS-SAMR可以进行一切用户、用户组的相关操作，其中一些功能在安全测试中可以帮助红队人员更好的开展工作。

### 3.1 修改用户密码

MS-SAMR中的SamrChangePasswordUser或者SamrSetInformationUser可以用来修改用户的密码，这在域渗透中使用比较频繁，因为在拿下域控服务器后可能我们想要登录Exchange服务器或是其他域认证的应用系统，但只知道对应用户的hash，这样的话我们就可以使用这种方式修改已知的明文密码登录系统后再修改回原始hash，具体的利用工具有mimikatz以及Impacket中的smbpassword.py。

### 3.2 添加用户

在安全测试中，添加用户往往关键点在于如何绕过防护软件，从开始的使用net1.exe绕过到参数欺骗、使用NetUserAddAPI添加用户，而NetUserAdd这些API更为底层的实现就是MS-SAMR，我们也可以直接调用该MS-SAMR对应的接口实现添加用户的程序，从而达到更好的规避防护的效果。

### 3.3 解决密码过期限制

在安全测试中，遇到登录机器提示密码过期时，也可以通过MS-SAMR来直接通过旧密码修改一个新密码从而登录，这可以使用smbpasswd或是Impacket中的smbpasswd.py工具来实现。

### 3.4 用户类信息收集

可以通过NetLocalGroup\*\*\*类API来枚举用户组、用户组中的用户以及用户相关的属性等，在实际环境中红队人员可以使用rpcclient工具来枚举域、域用户、权限、枚举SID等等。

枚举域：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120181437418-418157478.png)

枚举组：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120181447002-2042473659.png)

枚举用户：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120181503539-1732053868.png)

值得一提的是由于操作最终都是由RPC函数实现，相比经常使用的`net time /domain`、`net group “Domain Administrators” /domain`这些命令，是不容易被检测的，其次如果红队人员在目标内网并不存在一个”Windows落脚点“也是适用的。

## 4.使用MS-TSCH操作计划任务

MS-TSCH协议用于注册和配置任务以及查询远程计算机上正在运行的任务的状态，而ITaskSchedulerService接口实现了使用XML任务定义的方式来控制计划任务的方法，方法示例如下图所示：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120165117267-1031686834.jpg)

使用其中的SchRpcRegisterTask可以轻松地添加一个计划任务，MSDN定义如图：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120182054227-1938314376.jpg)

通过MSDN提供的IDL可以直接编译调用进行计划任务的添加，直接利用XML来添加计划任务，XML格式在文档也有说明，关键代码如下：

配置计划任务的xml：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120171246977-641282701.png)

绑定到RPC后进行注册计划任务：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120171305232-258701101.png)

我们可以实现添加本机或是远程计划任务，来实现权限维持或是横向移动，通过RPC直接调用计划任务的方式可以绕过不少AV/EDR的防护进行安全测试，对于横向移动除了通过注册表回显，还有@zcgonvh提出的通过计划任务的Description回显。

## 5.使用MS-SCMR操作服务

类似于计划任务，从红队人员的视角来看，Windows服务也是一个常用的权限维持手段，除了权限维持，通常我们还会使用服务来加载驱动程序。

以使用SCManager来加载驱动程序为例，通常为使用Advapi32.dll中导出的OpenSCManager、CreateService来操作：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221101104729947-111057629.png)

MS-SCMR，该协议用于远程管理服务控制管理器 (SCM)，它是一种 RPC 服务器，可以实现服务配置和服务程序的控制；同样使用MS-SCMR中的IDL编译后，调用ROpenSCManagerA、RCreateServiceA也可以创建服务，函数结构分别如下图所示：

ROpenSCManagerA:

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120173043919-850584465.jpg)

RCreateServiceA：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120173109550-695698158.jpg)

关键代码如下：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221101104829829-139767560.png)

同样在添加服务上有着良好的规避性，同样的使用RPC去操作注册表等，是否也会有不同的效果？

## 6.MalSecLogon PPID Spoofing

seclogon，叫做辅助登录服务，该服务是一个RPC服务。

而MalSecLogon是@antonioCoco提出的，使用seclogon中的一些技巧来实现dump lsass的其中一项技术。其是为了不直接与lsass.exe进程交互而获取泄露的lsass句柄的一种方式。

我们创建进程的时候可以调用很多API，但其实最终都是由CreateProcess类API进行最终的创建调用，当使用advapi32.dll中导出的CreateProcessWithTokenW或者CreateProcessWithLogonW创建进程的时候，其实最终会用到seclogon服务中的SeclCreateProcessWithLogonW函数，接着实现创建进程的功能实现是由SlrCreateProcessWithLogon函数实现。

流程如下：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120174149747-1679402941.png)

使用IDA或查看XP泄露源代码，可知advapi32.dll中的c\_SeclCreateProcessWithLogonW函数封装了一个RPC调用，第一个参数是一个SECL\_SLI结构：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120174641239-2032917528.png)

因为创建进程必须要知道是谁调用的，以此来作为被创建进程的父进程。此结构中的ulProcessId是由GetCurrentProcessId()函数获取，GetCurrentProcessId()是获取当前进程TEB中的对应结构。

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120174712472-653046790.png)

接着回到seclogon.dll中，最终SlrCreateProcessWithLogon得到被调用进程ID后，打开对应进程句柄：

![](https://img2022.cnblogs.com/blog/1449167/202211/1449167-20221120174728517-1390670907.png)

更新进程的...