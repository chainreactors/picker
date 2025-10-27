---
title: 网络入侵检测系统之suricata概要介绍
url: https://www.secpulse.com/archives/191017.html
source: 安全脉搏
date: 2022-11-16
fetch_date: 2025-10-03T22:51:48.301210
---

# 网络入侵检测系统之suricata概要介绍

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

# 网络入侵检测系统之suricata概要介绍

[工具](https://www.secpulse.com/archives/category/tools)

[货拉拉安全](https://www.secpulse.com/newpage/author?author_id=40552)

2022-11-15

13,588

## **1.简介**

**Suricata**是一个免费、开源、成熟、快速、健壮的网络威胁检测引擎。Suricata引擎能够进行实时入侵检测(IDS)、内联入侵预防(IPS)、网络安全监控(NSM)和离线pcap处理。Suricata使用强大而广泛的规则和签名语言来检查网络流量，并提供强大的Lua脚本支持来检测复杂的威胁。使用标准的输入和输出格式(如YAML和JSON)，使用现有的SIEMs、Splunk、Logstash/Elasticsearch、Kibana和其他数据库等工具进行集成将变得非常简单。Suricata项目和代码由开放信息安全基金会(OISF)拥有和支持，OISF是一个非盈利基金会，致力于确保Suricata作为一个开源项目的开发和持续成功。

下面将介绍一下如何搭建一个suricata平台以及一些suricata的基本信息，重点会说一下suricata的工作模式，这个涉及到数据包的处理流程

## **2.suricata安装**

### 2.1 依赖库安装

yum install -y git epel-release make autoconf gcc-c++ automake cmake libtool pcre-devel libyaml-devel jansson-devel libpcap-devel  file-devel zlib-devel  nss-devel libcap-ng-devel libnet-devel libnetfilter\_queue-devel lua-devel  epel-release lz4-devel xz-devel  json-c-devel librdkafka-devel  luajit-devel python-pip ragel

yum install -y rust cargo pcre2-devel

cargo install --force cbindgen

cp /root/.cargo/bin/cbindgen /usr/bin/

pip install pyyaml json-lines

### 2.2源码下载编译

1. git clone <https://github.com/OISF/suricata.git>
2. cd suricata
3. git clone <https://github.com/OISF/libhtp>（下载libhtp用于http协议解析）
4. ./autogen.sh
5. 生成对应的makfile FLAGS=-g ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-nfqueue --enable-luajit  --enable-debug ( -g表示保留符号信息，程序出core时，可以运用上，--prefix用于设置安装、配置、日志目录，--enable-nfqueue用于开启nfq网卡多队列模式支持 --enable-luajit用于开启对luajit的支持  --enable-debug开启日志模式 )
6. Make && make install && make install-conf (编译，安装，以及安装规则)

> 安装可执行程序及相关路径:

> 可执行程序(/usr/bin):

> suricata/suricatactl/suricatasc/suricata-update

> 配置相关路径：

> /var/log/suricata #log相关

> /etc/suricata(include:classification.config/reference.config/suricata.yaml(可配置rules路径)/threshold.config) #配置信息 协议等

> /var/lib/suricata/rules #规则相关

### 2.3 运行

suricata -c /etc/suricata/suricata.yaml -i enp0s3

![1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/12.png "12.png")

这里用的是最新的版本7.0,我自己的网卡是enp0s3,把这个换成自己要监听的网卡即可

## **3.suricata基本信息介绍**

![2.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/22-474x1024.png "22-474x1024.png")

## 4.suricata 工作模式分析

### 4.1 single模式

![3.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/33.png "33.png")

single只支持一个网卡设备，只有一个work线程

### 4.2 work模式

![4.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/42.png "42.png")

Work工作模式，每个网卡默认对应cpu数个工作线程(或者按照配置文件配置的线程数)，每个工作线程取对应的网卡队列中数据包

### 4.3 autofp工作模式

![5.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/51.png "51.png")

autofp模式相对比较复杂，相当于共用了work线程

### 4.4 work线程介绍

工作模式的重点在于工作线程的处理，下面介绍一下工作线程的处理流程

数据包工作线程是按照slot的注册跑，一个slot一个走

这是个流工作线程，以afpacket的work工作模式为例，函数执行流程如下：

TmThreadsSlotPktAcqLoop-》ReceiveAFPLoop-》AFPReadFromRing-》TmThreadsSlotProcessPkt-》TmThreadsSlotVarRun-》SlotFunc（FlowWorker）

ReceiveAFPLoop就是当时注册的收包slot,

FlowWorker就是当时注册的flow work slot

![6.jpeg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/6.jpeg "6.jpeg")

在多网卡收包的场景下，推荐使用work模式，该模式的性能会更好，同时可以调节收包模式，使得同一个五元组在同一个线程中处理，更有利于在攻击场景中做统计计算。

后续将再介绍一些：解包过程（比如mysql,pop3,http,dns协议的解析详细信息），日志记录，规则匹配，高性能场景性能优化的一些相关知识。

**本文作者：[货拉拉安全](newpage/author?author_id=40552)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/191017.html**](https://www.secpulse.com/archives/191017.html)

Tags: [suricata](https://www.secpulse.com/archives/tag/suricata)、[网络威胁检测引擎](https://www.secpulse.com/archives/tag/%E7%BD%91%E7%BB%9C%E5%A8%81%E8%83%81%E6%A3%80%E6%B5%8B%E5%BC%95%E6%93%8E)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![威胁猎杀实战（三）：基于Wazuh, Snort/Suricata和Elastic Stack的SOC](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2018/11/link-2-300x127.jpg)

  威胁猎杀实战（三）：基于Wazuh, S…](https://www.secpulse.com/archives/81629.html "详细阅读 威胁猎杀实战（三）：基于Wazuh, Snort/Suricata和Elastic Stack的SOC")
* [![Suricata IDS 入门 — 规则详解](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2018/05/in.jpg)

  Suricata IDS 入门 R…](https://www.secpulse.com/archives/71603.html "详细阅读 Suricata IDS 入门 — 规则详解")
* [![pocsuite3安全工具源码分析](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202502171711874.png)

  pocsuite3安全工具源码分析](https://www.secpulse.com/archives/205913.html "详细阅读 pocsuite3安全工具源码分析")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2021/08/1629775328.png)](https://www.secpulse.com/newpage/author?author_id=40552aaa) | [货拉拉安全](https://www.secpulse.com/newpage/author?author_id=40552) | |
| 文章数：4 | 积分： 0 |
|  | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)
...