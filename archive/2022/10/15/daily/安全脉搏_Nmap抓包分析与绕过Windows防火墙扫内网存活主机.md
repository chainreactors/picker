---
title: Nmap抓包分析与绕过Windows防火墙扫内网存活主机
url: https://www.secpulse.com/archives/189038.html
source: 安全脉搏
date: 2022-10-15
fetch_date: 2025-10-03T19:54:21.053500
---

# Nmap抓包分析与绕过Windows防火墙扫内网存活主机

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

# Nmap抓包分析与绕过Windows防火墙扫内网存活主机

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-10-14

12,206

## 前言

在打靶场的过程中使用Nmap时发现点小问题，借此机会详细分析下情况，于是有了这篇文章。

本文包含以下内容：

1. 1. Nmap抓包分析
2. 2. 内网下绕过Windows防火墙扫描存活主机

这里主要是针对Nmap进行讨论，实战中当然哪个快用哪个。不过万变不离其宗，哪怕稍微了解下其原理都受益无穷。

## 防火墙

这里的防火墙值得是Windows server自带的防火墙，主要绕过其两个防御规则：

1.禁止ICMP回显

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718383.png "null")

2.隐藏模式

具体见Stealth Mode in Windows Firewall with Advanced Security，大意为：不会使用ICMP不可达响应UDP查询，不使用RST响应TCP查询。默认开启。

https://shamsher-khan-404.medium.com/understanding-nmap-scan-with-wireshark-5144d68059f7

> `-sn`：禁用端口扫描
>
> `-P*` 用于选择不同的PING方法，用于存活扫描

## Nmap抓包分析

### 拓扑图

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718385.png "null")

关闭防火墙便于查看数据包

### 主机发现(Ping)

#### `-PS`(TCP SYN)

TCP SYN Ping：发送单个TCP SYN包到指定端口检测主机是否存活，默认80端口。该扫描就是经典的半开放扫描。

**请求局域网主机135端口(开启)**

```
nmap -sn -PS135 172.16.1.128 -vvv -n --disable-arp-ping
#-n 禁用dns解析
```

> 注意nmap扫局域网存活主机都会预先进行arp扫描，在这里禁用了端口扫描，意味着nmap只会进行存活扫描，当nmap进行arp扫描后发现主机存活就不会进行后续操作，wireshark也就抓不到包，所以使用`--disable-arp-ping`禁用arp扫描。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718386.png "null")

image

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718390.png "null")

image

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718391.png "null")

image

**请求局域网主机666端口(关闭)**

```
nmap -sn -PS666 172.16.1.128 -vvv -n --disable-arp-ping
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718394.png "null")

image

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718399.png "null")

image

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718400.png "null")

image

**请求远程主机135端口(开启)：**

还是这里会发现，和扫局域网比起来多了很多包，为什么和扫局域网情况不一样？

还是fofa随便找个开启135端口的IP：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-16657184001.png "null")

image

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718401.png "null")

image

这里会发现，和扫局域网比起来多了很多包。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718402.png "null")

image

**请求远程主机6666端口(关闭)：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-16657184021.png "null")

image

奇怪的是，明明远程主机返回了RST/ACK包，但nmap没有接收到。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718403.png "null")

image

为什么会有这样的差别？翻了翻nmap官方文档，其中有这样一句话：

> The RST packet is sent by the kernel of the machine running Nmap in response to the unexpected SYN/ACK, not by Nmap itself
>
> RST报文是运行Nmap的机器的内核为响应意外的SYN/ACK而发送的，而不是Nmap本身。

突然想到，我的kali是放在vmware，以nat形式接入网络，这样偶尔会出现点小问题。

于是我在windows上装了个nmap再进行测试：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-16657184031.png "null")

image

再看下抓包

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718404.png "null")

image

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-16657184041.png "null")

image

发现这里没发RST包

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718405.png "null")

image

关掉防火墙再试，还一下发俩RST……

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-16657184051.png "null")

image

接下来将vmware网络模式换为桥接，发现正常了。说明是NAT网络的问题。

#### `-PA`(TCP ACK)

TCP ACK Ping：发送单个TCP ACK包到指定端口检测主机是否存活，默认80端口

**请求局域网主机135端口(开启)**

一般ACK包是双方建立起连接发送的，但实际上不存在连接，无论端口是否开启，远程主机都会用RST包来回应，以此来判断主机存活。当然很多防御策略都会丢弃无效包防止被检测。

```
nmap -sn -PA135 172.16.1.128 -vvv -n --disable-arp-ping
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718406.png "null")

image

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718407.png "null")

image

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718408.png "null")

image

**请求局域网主机666端口(关闭)**

```
nmap -sn -PA666 172.16.1.128 -vvv -n --disable-arp-ping
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-16657184081.png "null")

image

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-16657184082.png "null")

image

#### `-PU`(UDP)

UDP Ping：发送UDP包到指定端口检测主机是否存活，默认40125端口。特定端口会发送特定的UDP包以便于获取更好的响应。

按照最新官方文档解释，该包发送大概有以下几种情况：

> 1. 1. 端口关闭->返回ICMP端口不可达包->判断主机存活。
> 2. 2. 返回其他ICMP错误，如主机/网络不可达或TTL超标等->判断停机。
> 3. 3. 端口开启且该服务不响应—>nmap未接收到返回包->判断停机。
> 4. 4. 端口关闭且协议不匹配->返回ICMP端口不可达包->判断主机存活。

这就是为什么默认要用40125这么冷门的端口，避免有服务使用该端口。

```
nmap -sn -PA135 172.16.1.128 -vvv -n --disable-arp-ping
```

返回ICMP端口不可达，仍旧判断出主机存活。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-1665718409.png "null")

image

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189038-16657184091.png "null")

image

局域网没什么问题，扫外网的话同样有前文说的Vmware Nat网络问题，注意...