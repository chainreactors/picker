---
title: 应急响应 | TeamTNT挖矿木马应急溯源分析
url: https://www.secpulse.com/archives/198302.html
source: 安全脉搏
date: 2023-03-29
fetch_date: 2025-10-04T10:58:29.754633
---

# 应急响应 | TeamTNT挖矿木马应急溯源分析

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

# 应急响应 | TeamTNT挖矿木马应急溯源分析

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[贝塔安全实验室](https://www.secpulse.com/newpage/author?author_id=9525)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-28

14,015

|  |
| --- |
| **声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。  请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。 |

在前一周的时间里，客户有遇到被TeamTNT入侵挖矿的案例。但由于客户在没有给被入侵主机做快照的情况下，回滚了之前的快照，导致无法进一步入侵溯源排查。

因此在腾讯云公网上上搭建了redis未授权的漏洞环境并在控制台安全组放行端口。随后很短时间内便收到了云镜的告警通知。

**0x01 确定最早入侵时间点**

通常根据云镜的告警短信，基本可以确定最早入侵时间点。这对于后续的溯源分析非常重要。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973466.png)

因为在该主机上是我提前搭建好的redis漏洞环境，所以是通过redis入侵的。查看reids的相关日志确定对应时间有写入文件的操作。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973467.png)

**0x02 快照备份，及时止损**

收到告警后第一时间对被感染的主机做了快照备份，当然不清楚感染的是挖矿还是勒索的情况下，最好还是先关机处理。毕竟应急响应的核心点是及时止损。

先给出分析结论，TeamTNT挖矿家族主要通过两种方式入侵：

```
对外扫描6379端口redis未授权入侵写入定时任务
读取本机~/.ssh/authorized_keys文件横向入侵
```

**0x03 清理定时任务**

linux下对应的几个定时任务的文件位置都需要排查是否被写入恶意命令。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973471.png)

**0x04 清理挖矿相关进程**

然后上机排查，发现cpu占用非常高，进程名为[ext4]。在linux通常系统进程外面会带有[]，猜测这里是为了混淆视听，将挖矿的进程名带上括号。

几分钟后使用top命令查看，发现挖矿进程不见了，但是系统依旧很卡。猜测做了进程隐藏或对命令劫持等手段。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973482.png)

被劫持的top命令

#### 清理思路：换用busybox来查看进程。

发现命令找不到或者被替换后，在不清楚挖矿病毒对哪些命令做了什么修改的情况下，可以直接使用busybox代替系统命令。这里在curl和wget都无法使用的情况下，可以换lrzsz或者scp等其他方式传一个busybox上去。

使用busybox可以发现一个是挖矿进程，另一个是pnscan扫描进程。直接kill进程后会马上再起一个，所以用busybox先把源文件删除后再杀进程。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973488.png)

busybox top

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973492.png)

在清理掉挖矿进程后，cpu占用会减少，方便后续的操作。同时已经清理了cron定时任务后不会一段时间后又重启挖矿。

**0x05 根据入侵时间点排查修改的文件**

根据云镜告警的命令执行时间，通过find命令查找最近被修改过的文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973496.png)

通过排查入侵时间点被修改的文件，可以分析挖矿木马的一些行为特征。特别是对于一些隐藏文件，或者容易被混淆的路径文件夹。

比如图中的 /var/tmp/…/dia/，…是隐藏的文件夹，很容易被忽略掉。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973498.png)

与此同时，账户下的其他主机由于配置的ssh密钥也被横向入侵了。相继收到告警短信，提示执行高危命令。上机查看ssh登录日志排查对应时间段，通过另一台被入侵主机ssh密钥连接过来的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973500.png)

云镜发出告警后，云镜控制台提示已离线，此时云镜已经被卸载掉了。从腾讯云控制台来看，连主机监控组件也一起被干掉了。所以被入侵后，从云镜也只能拿到很少的有效信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973507.png)

**0x06 查看主机网络状态**

netstat查看网络请求发现大量对外发起了6379端口的扫描。这个是由pnscan发起的对外扫描，pnscan进程清理掉即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973509.png)

被入侵后在iptables中发现添加了规则，禁止外网访问仅允许本机访问6379端口。避免redis再被其他人入侵。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973517.png)

**0x07 修复被替换的命令及权限**

查找缺失或被替换的命令：使用rpm -Va

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973518.png)

用rpm比对被修改过的命令。missing表示命令找不到了，5代表MD5发生了改变，有可能对应的命令文件被替换或有修改。M则表示命令的权限发生了修改。

具体每个值的含义如下：

```
  S         文件大小是否改变
  M         文件的类型或文件的权限（rwx）是否被改变
  5         文件MD5校验是否改变（可以看成文件内容是否改变）
  D         设备中，从代码是否改变
  L         文件路径是否改变
  U         文件的属主（所有者）是否改变
  G         文件的属组是否改变
  T         文件的修改时间是否改变
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973519.png)

命令文件权限被修改

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973520.png)

wget和curl命令缺失

对于缺失的命令比如wget和curl，实际上是被重命名了。但是不清楚的情况下直接reinstall即可。对于系统命令可以使用yum whatprovides command 来查询对应的包名，以ps命令为例。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973521.png)

ps命令被替换或修改过，想要恢复命令就可以使用yum reinstall procps-ng -y。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973522.png)

**0x08 清理挖矿后门**

命令修复之后，检查挖矿脚本留下的后门公钥和账户。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973523.png)

清理的时候会发现，很多文件都使用了chattr不让其删除。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973525.png)

像这样的文件往往有很多，配合上面的find命令可以将特定时间内的文件全部取消掉这些权限。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973527.png)

上面这些在入侵时间点发生过修改的文件，都需要检查是否被写入恶意命令。清理掉对应的恶意文件，此时入侵排查的大部分步骤已完成。

**0x09 排查相关可疑文件**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973537.png)

同时使用find命令发现在/根目录下面有大量的以.r开头隐藏文件。这些都是挖矿木马对外扫描存在6375端口开放的ip。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973540.png)

经测试这里大部分是其他的肉鸡，或者是对外开放了6379端口，但redis运行在低权用户，无法被直接提权利用。

**0x10 修复漏洞，加固系统**

经过上面溯源分析，确定了存在漏洞的系统组件。在清理完成之后，需及时修复相关的漏洞，避免再次被入侵。本文的redis为例，修复建议：

```
redis使用密码连接，并设置一定强度的密码。
使用低权用户运行redis
将默认redis的6379端口改为其他端口。
```

**0x11 挖矿木马特征行为分析**

**TeamTNT木马的整体攻击流程如下图所示：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973544.png)

**TeamTNT的横向传播途径如图：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198302-1679973545.png)

```
文章来源：Zgao's blog
原文地址：https://zgao...