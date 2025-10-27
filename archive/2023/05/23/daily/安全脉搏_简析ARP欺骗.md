---
title: 简析ARP欺骗
url: https://www.secpulse.com/archives/200816.html
source: 安全脉搏
date: 2023-05-23
fetch_date: 2025-10-04T11:36:45.901931
---

# 简析ARP欺骗

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

# 简析ARP欺骗

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-05-22

14,915

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739043.png)

## 数据转发过程

在聊ARP之前，我们需要先了解一下我们在发送一个数据时在网络中发生了什么 ，它需要什么东西，又是怎么获得的？对方又是怎么接收到的？当前现网中我们都是使用TCP/IP协议栈进行网络通信的，假设当前你正在通过火狐浏览器访问tide官网（www.tidesec.com），当你输入完网址，敲下回车键后，计算机内部会发生如下事情： 首先当前计算机只知道域名为www.tidesec.com，此时要先向DNS服务器发送数据去请求www.tidesec.com的IP地址，DNS服务器收到数据包后发现计算机请求获得www.tidesec.com的IP地址，将www.tidesec.com所绑定的IP地址打包发送给计算机。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739046.png "null")

火狐浏览器调用HTTP协议，完成应用层数据封装，HTTP依靠传输层的TCP进行数据的可靠性传输，将封装好的数据传输到传输层，传输层将应用层传递下来的Data添加上相应的TCP头部信息（源端口、目的端口）后。传递给网络层，网络层收到传输层传递爱的数据段后添加上相应的IP头部信息（源IP、目的IP）后将数据包传递给数据链路层，数据线路层收到后，添加上相应的Ethernet头部信息（源MAC地址、目的MAC地址）和FCS帧尾后将数据帧传递给物理层，根据物理介质的不同，物理层负责将数字信号转换成电信号、光信号、电磁波信号等，转换完成的信号在网络中开始传递。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739047.png "null")

如刚刚上面数据发送方数据封装的流程，我们看到了在封装时，传输层需要源目端口，这里源端口随机分配，目的端口由服务器的应用指定，网络层需要源目IP，这里刚刚我们向DNS服务器请求www.tidesec.com时也获得了tide官网的IP地址，也能实现，那么现在数据链路层需要源目MAC地址，源MAC地址好说，自己的mac地址，那目的mac地址呢？该怎么获取呢？这时就需要用到我们的ARP协议了。

## 地址解析协议（ARP）

ARP（Address Resolution Protocol）是一种网络层协议，根据已知的目的IP地址解析获得其对应的MAC地址。在局域网中，每台设备都有唯一的MAC地址，就像我们的身份证号一样在全球独一无二的，而IP地址是可以重复分配的。因此，当一个设备需要发送数据包到另一个设备时，它需要知道另一个设备的MAC地址。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739049.png "null")

那么ARP是怎么工作的呢？一般设备里都会有一个ARP缓存表，用来存放IP地址和MAC地址的关联信息，在发送数据前，设备会先查找ARP缓存表，如果缓存表中存在对方设备的MAC地址，则直接采用该MAC地址来封装帧，然后将帧发送出去。如果缓存表中不存在相应信息，则通过ARP来获取。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739050.png "null")

当ARP缓存表为空时，主机1通过发送ARP request报文来获取主机2的MAC地址，由于不知道目的地址，因此ARP Request报文内的目的MAC为广播地址FF-FF-FF-FF-FF-FF，因为ARP Request是广播数据帧，因此交换机收到后，会对该帧执行泛洪操作，也就是说该网络中所有主机包括网关都会接收到此ARP Request报文。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739051.png "null")

所有的主机接收到该ARP Request报文后，都会检查它的目的IP地址字段与自身的IP地址是否匹配。主机2发现IP地址匹配，则会将ARP报文中的发送端MAC地址和发送端IP地址信息记录到自己的ARP缓存表中。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739052.png "null")

这时主机2通过发送ARP Reply报文来响应主机1的请求，此时主机2已知主机1的MAC地址，因此ARP Reply是单播数据帧。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739053.png "null")

主机1收到ARP Reply以后，会检查ARP报文中目的端IP地址字段与自身的IP地址是否匹配。如果匹配，ARP报文中的发送端MAC地址和发送端IP地址会被记录到主机1的ARP缓存表中。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739054.png "null")

至此，ARP工作结束，获得目的IP对应的MAC地址后，即可封装完整的数据包进行数据包的发送（上述工作过程为局域网内的工作过程，如访问其他网段或外网中的IP地址时，所获得的MAC地址为网关的MAC地址，网关收到此ARP Request后会发送ARP Reply）

## ARP欺骗

刚刚我们也看到了，ARP协议是通过广播来获取目标设备的MAC地址的，当一个设备需要发送数据到另一个设备时，他会发送一个ARP请求，询问局域网内的所有设备，是否具有指定IP地址对应的MAC地址，目标设备收到请求后会回复一个ARP应答，告诉请求主机它的MAC地址。ARP欺骗利用了这种工作原理，攻击者会发送伪造的ARP数据包，将自己伪装成网关或其他设备，目标设备收到伪造的ARP数据包后，会将攻击者的MAC地址和其目标IP地址相对应写入ARP缓存表中，并将后续数据包发送给攻击者。攻击者就可以截获目标设备发送的数据包，甚至可以修改、篡改数据包中的内容。同样的ARP欺骗也分为单向欺骗和双向欺骗。

### 单向欺骗

如下图所示，攻击者通过伪造ARP Request来将自己的MAC地址伪装成网关IP相对应的mac地址广播出去，主机A收到该ARP Request后会将发现该ARP Request目的IP地址为自己，将该ARP Request中的目的IP地址与MAC地址写入到ARP缓存表后，然后发送ARP Reply，将本该传输给网关的数据错误的传输给攻击机，使主机A得不到网关的响应数据，从而导致断网。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739055.png "null")

以上就是ARP单向欺骗的原理，那我们怎么来实现呢？往下看 首先我们先来查看一下主机A的mac地址缓存表，当前192.168.45.2就是当前系统的网关地址，所对应的也是真实的MAC地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739058.png "null")

那么现在主机A也是可以正常上网的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-16847390581.png "null")

根据我们上面的思路来看，我们如果想要让主机A找不到网关无法上网，我们只需要构造一个IP地址为192.168.45.2的虚假mac地址的ARP Reply数据包就可以了，这里我们使用科莱网络分析系统这个工具就可以实现这个功能。首先我们来先对当前网段的MAC地址进行一个扫描，获得主机A的MAC地址。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739060.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739062.png "null")

这里获得了主机A的MAC地址后，就可以点击上面的数据包生成器。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739065.png "null")

添加ARP数据包

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739066.png "null")

然后在目的MAC地址和目的IP中输入我们的目标主机的IP和MAC地址，源MAC地址任意输即可，源IP输入网关的IP地址。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739068.png "null")

然后点击发送，选择网卡，这里选择循环发送，次数为0，让它一直发送伪造的ARP数据包后点击开始。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739071.png "null")

这时我们抓包看一下当前的网络状况，可以看到，源mac为00-01-02-03-04-05，寻找目的IP地址为192.168.45.131的ARP Request已经发出。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739073.png "null")

这时我们再来看主机A的ARP地址表中是否有了变化

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739076.png "null")

image.png

可以看到主机A中对应192.168.45.2的MAC地址成功被我们修改为了00-01-02-03-04-05，那这时我们再访问一下百度来看看。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200816-1684739077.png "null")

可以看到主机A目前已经无法正常返回百度。

### 双向欺骗

如下图所示，攻击机一直发送伪造的ARP Reply，欺骗网关自己是主机A，欺骗主机A自己是网关，同时开启路由转发功能，就可以让主机A在正常上网的情况下截获网络数据...