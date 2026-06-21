---
title: SSL/TLS 密码套件漏洞分析以及修复方法
url: https://mp.weixin.qq.com/s/VFdTwEOE2_scDdlip_dAwA
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:46:20.039545
---

# SSL/TLS 密码套件漏洞分析以及修复方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDdOxkoCDiaQjFWMGD0cvPUzrz2ibF4vCwSDLib2L2ibaA1Giayl8icVxnOzicHNHYHGtQWDuf6EOVgia8eDf2o8sZXMd5LNLgdjreANZE/0?wx_fmt=jpeg)

# SSL/TLS 密码套件漏洞分析以及修复方法

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**01**

**前言**

在当今数字化时代，网络安全至关重要。SSL/TLS 协议作为保障网络通信安全的重要手段，广泛应用于各类网络应用中。然而，如同任何技术一样，SSL/TLS 也并非绝对安全，存在着一些可能被攻击者利用的漏洞。本文将深入分析 SSL/TLS 密码套件中常见的漏洞种类及其原因，并详细介绍相应的修复方法，旨在帮助读者更好地理解和应对这些安全风险，确保网络通信的安全性和可靠性。

**02**

**SSL/TLS密码套件漏洞的常见种类和原因**

**2.1 SSL/TLS 协议信息泄露漏洞(CVE-2016-2183)**

使用nmap对某个域名做密码学套件的扫描。扫描结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDma8NYgpXL1kRDOEvGfhCMdB5Jb4xtLcYJibrzSI4KVVLT1vtsqPwaSl1ib27EujtVreoMic3t9rvgqibrN1eYsH1Jc4pkkQmyTRk/640?wx_fmt=png&from=appmsg)

可以看到：

时的用 TLSv1.0 和 TLSv1.1 协议依旧支持，同时压缩算法部分有TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA(rsa 2048)被标记为-C，表示存在潜在风险。同时服务器警告 64 - bit 块密码 3DES 容易受到 SWEET32 攻击。

**2.2 SSL/TLS 服务器瞬时 Diffie-Hellman 公共密钥过弱漏洞**

使用nmap对某个域名做密码学套件的扫描。扫描结果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAUfkbXUnUz6Riaia4It0TmtO7MKDMneCT8RIOehQLaAak7icjibgc5FFPPic6FsPkEOzU1DExqlT1DU7rJbeSIqFEt0VYdqPfORoia8/640?wx_fmt=png&from=appmsg)

扫描结果显示`Diffie - Hellman Key Exchange Insufficient Group Strength`，即服务器在使用Diffie - Hellman密钥交换时，所使用的组强度不够。这种情况可能导致服务器容易受到被动窃听攻击。攻击者可能通过分析网络流量，利用Diffie - Hellman密钥交换的弱点，获取到加密通信中的敏感信息，从而破坏通信的保密性和完整性。

**2.3 OpenSSL 拒绝服务漏洞(CVE-2016-8610)**

OpenSSL 是一种开放源码的 SSL 实现，用来实现网络通信的高强度加密，现 在被广泛地用于各种网络应用程序中。OpenSSL 在 SSL/TLS 协议握手过程的 实现中，允许客户端重复发送类型为 SSL3\_RT\_ALERT 级别为 SSL3\_AL\_WARNING 的内容未定义警告包，且 OpenSSL 在实现中遇到该未定 义警告包时仍选择忽略并继续处理接下来的通信内容（如果有的话）。攻 击者可以容易的利用该缺陷在一个消息中发送大量此未定义内容的警告 包，使服务或进程陷入无意义的循环，从而导致服务进程占掉 100 的 CPU 使用率。

检测方法：

通过socket发送如下数据

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB0hlHA3AjzMVicypMvTaZXicVXjfyszBuIkcbogFgnetXnqbcZ5uNcfb0ZruMPpU0nmVBJ4e0Hpueic43Sh33ibJBIGVqp2x8GDAI/640?wx_fmt=png&from=appmsg)

如果收到响应

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCN1xTicCJzuhkJQXOdRSvO5wKeX45wTDwlibDRicic45jX3WkMnCW9bBctmhal2eeyo61DZjFzTJ6PFyk5ZbzYx1icRqtbmMAyiaLNg/640?wx_fmt=png&from=appmsg)

则表示漏洞存在。

相关资料：

https://www.openssl.org/source/ https://security.360.cn/cve/CVE-2016-8610/ https://access.redhat.com/errata/RHSA-2017:1414

https://access.redhat.com/errata/RHSA-2017:1413

**03**

**应用系统的架构**

ISO 7 层架构和 TCP/4 层架构有不同的含义和应用场景，主要区别如下：

**3.1 层次结构**

ISO 7 层架构

从下到上依次为物理层、数据链路层、网络层、传输层、会话层、表示层和应用层。

物理层负责处理物理介质上的信号传输，如网线、光纤等；数据链路层关注的是在相邻节点间可靠地传输数据帧；网络层负责将数据包从源节点路由到目标节点；传输层提供端到端的可靠或不可靠的数据传输服务；会话层建立、维护和管理会话；表示层处理数据的表示形式，如加密、压缩等；应用层是用户与网络交互的接口，包括各种应用程序。

TCP/IP  4 层架构

由网络接口层、网络层、传输层和应用层组成。

网络接口层对应于 ISO 模型中的物理层和数据链路层的功能，主要负责网络接入和数据链路的相关操作；网络层负责 IP 寻址和路由选择；传输层提供 TCP（可靠传输）和 UDP（不可靠传输）等服务；应用层包含各种应用协议和应用程序，如 HTTP、FTP 等。

**3.2 功能重点**

**ISO 7 层架构**

更注重对网络通信过程中从物理介质到应用程序的全方位、精细化的功能划分和描述。

每个层次都有其明确的功能和接口规范，有利于不同厂商的设备和软件在各个层次上进行标准化的开发和集成。例如，在表示层可以通过统一的标准来实现数据的加密和解密操作，使得不同系统之间能够正确地处理和理解数据的表示形式。

TCP/IP 4 层架构

更侧重于互联网环境下的实际应用和网络通信的核心功能。

它简化了层次结构，突出了网络层的 IP 协议和传输层的 TCP、UDP 协议的重要性。网络层的 IP 协议实现了全球范围内的寻址和路由，传输层的 TCP 和 UDP 则满足了不同应用场景下对数据传输可靠性和效率的要求。例如，在设计一个简单的 Web 应用时，主要关注的是应用层的 HTTP 协议、传输层的 TCP 协议以及网络层的 IP 协议，而对底层的物理层和数据链路层细节通常不需要过多考虑。

**3.3 在阿里云服务器配置中的应用**

ISO 7 层架构应用

在一些复杂的企业级应用场景中，可能会涉及到对各个层次的精细配置和管理。例如，在配置服务器的网络安全时，可能需要在不同层次上设置访问控制。在物理层可以通过限制服务器机房的物理访问来保护设备；在数据链路层可以设置 MAC 地址过滤；在网络层可以配置防火墙规则进行 IP 地址过滤；在传输层可以通过配置 SSL/TLS 协议来保障数据传输的安全；在会话层可以管理用户会话的超时和权限；在表示层可以对数据进行加密存储和传输；在应用层可以对不同的应用程序设置用户权限和访问规则。

TCP/IP 4 层架构应用

在阿里云服务器配置中，通常更关注网络接口层的网络接入方式（如以太网、无线等），网络层的 IP 地址分配和路由设置，传输层的协议选择（如 TCP 或 UDP）以及应用层的应用程序部署和配置。例如，在配置一个 Web 服务器时，会在网络接口层确保网络连接正常，在网络层为服务器分配一个公网 IP 地址并设置正确的路由，在传输层选择 TCP 协议来保障 HTTP 请求的可靠传输，在应用层安装和配置 Web 应用程序相关的软件（如 Apache、NGINX  等）。

用户客户端访问应用服务器，一个常见的途径步骤是首先访问WAF，再到NGINX，最后到服务器。

所以我们在修复SSL/TLS密码套件漏洞时，要首先了解这是什么架构。

以阿里云为例，如果阿里云上看到负载均衡的监听器管理的配置如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDictgJIeoLG0KmGiazjhXa3cSQntKZO7Iicaz6wM5NJtv5898vq0H5sWqKiaHbpVGSZpaPDQYz13zLDsmCPf76NiaicMkUytDzyhav8/640?wx_fmt=png&from=appmsg)

说明目前负载均衡配置的是tcp4层协议，需要在服务器上修改协议版本配置。参考4.3的方法可以修复漏洞

其实我们建议尽量把负载均衡升级（新建一个新的7层协议），需要重新配置负载均衡，并且修改域名映射。当然，这需要影响业务，需要应用维护人员协商时间去操作，并且配合测试，动作比较大。那如果是在7层协议的情况下，用户需要找到最外层的设备，如果是WAF，建议采用4.1方法；如果是Nginx，建议采用4.2的方法。

**04**

**修复方法**

从阿里云的WAF使用说明中可以看到 只有通过CNAME接入方式接入域名时，您可以在接入域名配置向导的配置监听任务中，自定义允许WAF使用的加密套件类型（如下图所示）。自定义加密套件类型后，WAF只监听支持指定加密套件的客户端的请求。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBZVyuDT76QZ0aLNc4XWjGVC8tMzZgRcZ9fZ2NsHJZImR1GCdo3cQ3auM2UlMIppPtDI2Yvia0hcafYOIia6frMicIQGEDclkxnOk/640?wx_fmt=png&from=appmsg)

**4.2 修改NGINX配置**

NGINX关闭低版本tls协议 禁用 tls1.0 tls1.1等协议

配置示例：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBQEmicZ3ktQNL8ibMhziaB2F14XPMuAVrFIc8YufkHwPos9CxZhvbcZpceTR6oswvM2LvzOV3KMMfkR24hEicCAEaetSayhMsE9g0/640?wx_fmt=png&from=appmsg)

在这个配置中，ssl\_protocols TLSv1.2 TLSv1.3; 明确地禁用了 TLSv1 和 TLSv1.1。

ssl\_ciphers 指定了一些安全的加密套件。

ssl\_prefer\_server\_ciphers on; 配置 Nginx 使用服务器优选的加密套件。

确保你已经生成了 dhparam.pem 文件，可以通过以下命令生成：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBQCibF3q1WjVJmict0ADVbib7nxjsuOTB8KicW467zWheM0jTS7Q2ewcZEibibIq5vONRln8dqSvlo3yzeRfSfDNckibic1zEsMkEllWk/640?wx_fmt=png&from=appmsg)

完成配置后，重启 Nginx 以应用更改：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCibAEY8V57g98MAQbpzvhFD75A5rRENurSCYlDLach5lgqvdPYZBoibzmWqInia8ibBrrwyUA09YuQl0ia7CMEJvO0IWmPMLiaicuz74/640?wx_fmt=png&from=appmsg)

注意！这里可能有坑！我按上面的设置，通过检测工具(SSL Server Test (Powered by Qualys SSL Labs))，发现还是没有禁用tls1.1，后来折腾好久，才发现原因，是这台服务器不止一个网站，有别的vhost文件在用着tls1.1，如果想要禁用tls1.1，必须是整个服务器的nginx配置里都禁用tls1.1

**4.3 服务器tomcat配置修改**

修改conf下面的server.xml

<Connector 这一段里面增加如下两个配置：

配置1：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBqwrGTAsVmicdVnJ5ibd7Xs5rCDjNzTDVBX1OnU9OQCrU4LN7po0qoKrick9nTFyze5TdLQkajibOSnASCTCWwCLlPutoP0AibxlrY/640?wx_fmt=png&from=appmsg)

配置2：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBYbX6mMaBxzfDwicLNriaObicIauFmyMLbtiaiaHz5yax898ZTeFB7XPoXJf4IyficOXkEbpjfhrYFZYXsUltUKBL65z2xNVNBGLOCw/640?wx_fmt=png&from=appmsg)

配置完成的配置文件截图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBxUZVUPnKJARCepg9SdoPibQCey95cw7fmHM612QA1H5PlY8M5VE3Rrfgwy3eziaiaIH5X5Mmr1ARhNfQAdqEpwAMgNheRVSsFnw/640?wx_fmt=png&from=appmsg)

最后重启tomcat,就发现生效了。

**4.4 windows服务器本地修复**

天威诚信工具ITrusIIS.exe下载地址 http://www.itrus.cn/soft/ITrusIIS.exe

运行后点击“最佳配置”，然后去除红线这条后点“应用”

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA4iap6RKZMphDO81tibfHSZy4eSSen7vkp7IvlVYkVIb1Yk1iaZ79MB4TfibZ2NOgVibwKrJcMPrCMY7iaAk9QPPOoTBNRY1mqZ4lAc/640?wx_fmt=png&from=appmsg)

**4.4.2 可能的报错解决**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAvTDEib8RLhouN1MnDdj1153F3aiaqiaicFGnSkEpeQS0yQBRnnUibMj3lKhMVcX56v9d9d5be03e2cRVbzwxMl6iaLcLE9BWPyhic7M/640?wx_fmt=png&from=appmsg)

禁用HTTP/2

检查以下目录

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\HTTP\Parameters]
“EnableHttp2Tls”=dword:00000000
“EnableHttp2Cleartext”=dword:00000000

没有就添加上面两值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCHbX8Re7KWYkSJu997zNGtUwOUyqP2TQxHOHTMiaTCibiaxA0c57HrCeHtVjoQKMicCDCOCaDa8r1kujrmSA61smAFibgVJicGyk3sE/640?wx_fmt=png&from=appmsg)

**4.5 升级opensll**

对于 OpenSSL 拒绝服务漏洞(CVE-2016-8610)，建议方法是升级OPENSSL。但是需要注意这里的版本范围

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDsd2YgW4WV6Uicws55v6ggaF7IuahLsah1ohzQhwvxjJFqKiboVoZHPicVKpiaEQQ8TPgnZ8V16IAG0kria4589Te1yePx3r3odvqs/640?wx_fmt=png&from=appmsg)

来源：CSDN博主「晓翔仔」

https://blog.csdn.net/qq\_33163046/article/details/143226226

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=M...