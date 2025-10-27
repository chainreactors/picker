---
title: Mysql LOAD DATA 读取客户端任意文件
url: https://www.secpulse.com/archives/198670.html
source: 安全脉搏
date: 2023-04-08
fetch_date: 2025-10-04T11:29:15.971178
---

# Mysql LOAD DATA 读取客户端任意文件

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

# Mysql LOAD DATA 读取客户端任意文件

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-04-07

9,819

复现 Mysql LOAD DATA INFILE 读取客户端任意文件漏洞

### 前言

MySQL   客户端和服务端通信过程中是通过对话的形式来实现的，客户端发送一个操作请求，然后服务端根据客户端发送的请求来响应客户端，在这个过程中客户端如果一个操作需要两步才能完成，那么当它发送完第一个请求过后并不会存储这个请求，而是直接丢弃，所以第二步就是根据服务端的响应来继续进行，这里服务端就可以欺骗客户端做一些事情。

但是一般的通信都是客户端发送一个 MySQL 语句然后服务器端根据这条语句查询后返回结果，也没什么可以利用的。但是 MySQL 有个语法 LOAD DATA INFILE 可以用来读取一个文件的内容并插入到表中。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845503.png "null")

从上图的官方文档说明可以看到，该命令既可以读取服务端的文件，也可以读取客户端的文件，这取决于 `LOCAL` modifier 是否给定。

读取服务端上的文件内容存入表中的 SQL 语句是：

```
load data infile "/etc/passwd" into table TestTable fields terminated by '分隔符';
```

读取客户端上的文件内容存入表中的 SQL 语句是：

```
load data local infile "/etc/passwd" into table TestTable fields terminated by '分隔符';
```

两相对比，读取客户端上的文件内容多了一个 `local` 关键字。

以上所描述的过程可以形象地用两个人的对话来表示：

1. 1. 客户端：把我本地 /data/test.csv 的内容插入到 TestTable 表中去
2. 2. 服务端：请把你本地 /data/test.csv 的内容发送给我
3. 3. 客户端：好的，这是我本地 /data/test.cvs 的内容
4. 4. 服务端：成功/失败

正常情况下这个流程没有问题，但是前文提到了客户端在第二次并不知道它自己前面发送了什么给服务器，所以客户端第二次要发送什么文件完全取决于服务端，如果这个服务端不正常，就有可能发生如下对话：

1. 1. 客户端：请把我本地 /data/test.csv 的内容插入到 TestTable 表中去
2. 2. 服务器：请把你本地 /etc/passwd 的内容发送给我
3. 3. 客户端：好的，这是我本地 /etc/passwd 的内容
4. 4. 服务端：成功偷取文件内容

这样服务端就非法拿到了 `/etc/passwd` 的文件内容！接下来开始进行这个实验，做一个恶意服务端来欺骗客户端。为了编写出伪造恶意 MySQL 服务器的 POC，必须对 MySQL 协议有足够的了解，所以接下来尝试分析一下 MySQL 协议的数据包。

### MySQL 协议数据包分析

为了非法读取客户端文件，我们需要实现一个假的 MySQL 服务器。那如何实现呢？这需要我们对 MySQL 协议展开详细的分析才能做到，好在借助 Wireshark 结合 MySQL 官方文档可以帮助我们轻松分析 MySQL 协议的数据包。

我以 ubuntu 虚拟机为客户端，windows物理机为服务端，借助 Wireshark 工具捕捉两者间的 mysql 通信数据包。

客户端ip：192.168.239.129

服务端ip：192.168.1.3

客户端和服务端之间交互的 MySQL命令如下

```
mysql -h 192.168.1.3 -P 3306 -u root -p
use security;
load data local infile "/etc/passwd" into table users;
```

开启物理机的 mysql，这里注意需要设置 mysql 允许外来连接，不知道如何操作看看这篇文章

设置 MySQL 允许外部访问

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845508.png "null")

2.打开 wireshark，选择捕获 Vmware 相关的网卡并选择过滤 MySQL 协议，然后用虚拟机连接。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845509.png "null")

> 注意：不要使用 mysql 8.0.12 版本，否则相关的数据包显示不完整，甚至连接的用户名都显示不了，这个版本的加密可能更严格吧。

官方文档告诉我们 MySQL 协议也支持通过 TLS 进行加密和身份验证。MYSQL\_TLS

那我们捕获的数据包是否进行了加密呢？稍加分析一下这些捕获的数据包就可以判断其确实使用了 TLS 进行了加密。接下来我们根据文档结合 Wireshark 捕获的数据包来进行实践论证！

#### 连接过程数据包

运行连接命令时捕获到的数据包

```
mysql -h 192.168.1.3 -P 3306 -u root -p
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845510.png "null")

不打算全部都细说，就以前两个数据包为例子，和官方文档对照来学习其结构。

#### 第一个数据包 Protocol::HandshakeV10 服务端到客户端

当客户端通过 MySQL 协议连接到 服务端会发生什么呢？官方文档 Protocol::Handshake 告诉我们当客户端连接到服务端时，服务端会发送一个初始的握手数据包（Initial Handshake Packet）给客户端。根据服务端的版本和配置选项，服务端会发送不同的初始数据包。

为了服务端可以支持新的协议，Initial Handshake Packet 初始的握手数据包的第一个字节被定义为协议的版本号。从 MySQL 3.21.0 版本开始，发送的是 Protocol::HandshakeV10

我采用的 MySQL 版本是 5.7.26，所以发送的就是 `Protocol::HandShakeV10` ，我们可以看看文档是如何定义这个数据包的结构的：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845511.png "null")

关于 `Type` 字段各个值的含义在 Integer Types 和 String Types

`int<1>` 就是 一个字节，`string<NUL>` 表示以 00 字节结尾的字符串。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845515.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845517.png "null")

我们点开 Wireshark 中服务端给客户端发送的初始数据包，从 `Server Greeting` 字段开始就是 payload 部分，也就是初始的握手数据包。从图中我们可以看到有协议版本、服务端的 MySQL 版本、进程 ID。这和我们上图的文档是不是完美对应上了？

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-16808455171.png "null")

Protocol::HandShakeV10 只定义了一个数据包的 payload 部分，而关于头部的定义在 MySQL Packets

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845518.png "null")

和实际的数据包的对应：

payload\_length:

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845520.png "null")

sequence\_id:

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845521.png "null")

payload:

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845522.png "null")

image-20230110151214416

值得注意的是 Wireshark 的数据是按照小端排列的，比如数据包长度 74 对应的字段数据是 `4a 00 00`。

其余的字段就不再分析了，大同小异。紧接着简单看看客户端给服务端的回应吧。官方文档告诉我们，如果客户端支持 SSL(Capabilities Flags & CLIENT\_SSL is on and the mysql\_ssl\_mode of the client is not SSL\_MODE\_DISABLED) ，那么一个短的被称为 Protocol::SSLRequest:  的数据包会被发送，使得服务端建立一个 SSL layer 并等待来自客户端的下一个数据包。（这里你可能会感到混乱，前面不是说 TLS  吗，怎么现在变成了 SSL？其实 TLS 是升级版的 SSL，但是由于 SSL 这一术语更加常用，所以人们经常互换使用者两个术语。什么是 SSL、TLS、HTTPS）

如果不支持，那么客户端会返回 Protocol::HandshakeResponse: 。同时在任何时候，发生任何错误，客户端都会断开连接。

#### 第二个数据包 Protocol::HandshakeResponse41 客户端到服务端

根据前面的分析，这里客户端如果支持 SSL，那么会发送 `Protocol::SSLRequest` 数据包，否则就是`Protocol::HandshakeResponse:`。根据我的验证，应该发送的是 Protocol::HandshakeResponse41

> 感觉挺奇怪的，我觉得应该发送 SSLRequest 才是，但是其包结构却又对应不上。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-16808455221.png "null")

image-20230110155957039

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845523.png "null")

image-20230110160009859

client\_flag（4字节），包括了扩展的 Client capabilities

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198670-1680845525.png "null")

image-20230110154523933

![](https://secpuls...