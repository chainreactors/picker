---
title: ipv6攻击视角
url: https://www.secpulse.com/archives/194570.html
source: 安全脉搏
date: 2023-01-05
fetch_date: 2025-10-04T03:03:08.512639
---

# ipv6攻击视角

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

# ipv6攻击视角

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-01-04

17,809

#

```
本文转自先知社区：
作者：r0fus0d
```

#

# 前言

前段时间，突然对ipv6这块的资产收集感兴趣,分享下实践出的技巧和方案。

# 1. 如果目标有 ipv6 资产，你如何访问

## 获得ipv6地址

最简单的方法购买提供ipv6地址的vps

### vultr

比如vultr,购买时选择启用ipv6地址即可

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801007.png)

### aws

aws的机器默认没有ipv6地址分配，要按如下步骤来开启

1. vpc添加ipv6 CIDR

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801008.png)

1. vpc子网分配ipv6 CIDR块

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801009.png)

1. 创建ec2机器时选择自动分配ipv6 ip

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801012.png)

这个时候ip a就可以看到ipv6地址了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801014.png)

但是到这一步你会发现获取到了ipv6地址，但无法访问任何ipv6站点，这是因为这个vpc的路由表默认没有ipv6出口路由，手动配置如下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801017.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801018.png)

### 华为云

华为云和aws的步骤类似,现在vpc的subnet中开启ipv6功能,然后在创建ecs时选择分配ipv6地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-16728010181.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801019.png)

### 阿里云

类似,vpc配置开启ipv6,创建ecs时选择ipv6的子网，创建完毕需要开通ipv6公网带宽

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801020.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801021.png)

然后在开启的机器上运行以下命令,获取ipv6地址

```
wget https://ecs-image-utils.oss-cn-hangzhou.aliyuncs.com/ipv6/rhel/ecs-utils-ipv6
chmod +x ./ecs-utils-ipv6
./ecs-utils-ipv6
```

开启ipv6公网带宽

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801022.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801023.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801024.png)

## 如何让客户端访问ipv6站点

临近饭点，老吴问我如何让自己机器访问ipv6地址，因为如果只能通过vps进行访问，那一些图形化操作无法实现。

想了想，确实有道理，简单分析下，如果要让客户端访问到ipv6机器，那么要么客户端获取公网ipv6地址，要么走一些ipv6代理服务，比如https://proxyline.net/zh-hant/ipv6/。

获取公网ipv6地址不太可行，ipv6代理服务没必要，能自建干嘛要买。看网上文章里讲socks5，不用管客户端是ipv4还是ipv6协议，只要服务端是ipv6协议就可以让客户端畅通无阻的在ipv6环境下进行通讯。

那么我可以复用之前的clash代理池设计，只要节点端可以通ipv6，应该就可以了。

先看能不能访问

* ipv6.ip.sb
* ip.sb

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801025.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801026.png)

正常来讲，无法访问。

下面配置一个aws服务器起ssr

先按照开始的教程为aws配置ipv6子网，确保机器可以通ipv6

```
curl ipv6.ip.sb
# 能够正确获取到ipv6地址,这个机子就可以用
```

起ssr服务

```
apt-get updateapt-get install -y shadowsocks-libevsystemctl status shadowsocks-libev
vim /etc/shadowsocks-libev/config.json{        "server":["::0","0.0.0.0"],        "server_port":60001,        "method":"chacha20-ietf-poly1305",        "password":"1234567890",        "mode":"tcp_and_udp",        "fast_open":false}
service shadowsocks-libev restart# service shadowsocks-libev startservice shadowsocks-libev status
ps ax | grep ss-server
ss -tnlp
```

这里密码我随便设置了，如果生产环境不要用弱口令

启动ssr后，写一下clash配置

```
mixed-port: 64277allow-lan: truebind-address: '*'mode: rulelog-level: infoipv6: trueexternal-controller: 127.0.0.1:9090routing-mark: 6666hosts:
profile:  store-selected: false  store-fake-ip: true
dns:  enable: false  listen: 0.0.0.0:53  ipv6: true  default-nameserver:    - 114.114.114.114    - 8.8.8.8  enhanced-mode: fake-ip # or redir-host (not recommended)  fake-ip-range: 198.18.0.1/16 # Fake IP addresses pool CIDR  nameserver:    - 114.114.114.114 # default value    - 8.8.8.8 # default value    - tls://dns.rubyfish.cn:853 # DNS over TLS    - https://1.1.1.1/dns-query # DNS over HTTPS    - dhcp://en0 # dns from dhcp    # - '8.8.8.8#en0'
proxies:  - name: "1.14.5.14"    type: ss    server: 1.14.5.14    port: 60001    cipher: chacha20-ietf-poly1305    password: "1234567890"
proxy-groups:  - name: "test"    type: load-balance    proxies:      - 1.14.5.14    url: 'http://www.gstatic.com/generate_204'    interval: 2400    strategy: round-robin
rules:  - DOMAIN-SUFFIX,google.com,test  - DOMAIN-KEYWORD,google,test  - DOMAIN,google.com,test  - GEOIP,CN,test  - MATCH,test  - SRC-IP-CIDR,192.168.1.201/32,DIRECT  - IP-CIDR,127.0.0.0/8,DIRECT  - DOMAIN-SUFFIX,ad.com,REJECT
```

1.14.5.14是我这台aws的地址，60001是监听端口。这不是重点，重点在于2行`ipv6: true`

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/image.png "image.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/image.png)

必须要配置为true

导入clash配置，再次测试访问

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801027.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194570-1672801029.png)

到了这一步,还是不够,因为目前是基于域名的ipv6访问,如果要直接访问ipv6地址，你会发现还是访问不了,那么该如何做呢

1. 首先，在浏览器中访问ipv6地址，需要在前后加括号,例如 `http://[2409:8c0c:310:314::100:38]/#/login`
2. 在burp中的代理配置，需要改成socks5代理,不能是upstream proxy servers

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-1945...