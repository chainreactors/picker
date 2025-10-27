---
title: iptables命令常用规则汇总
url: https://zgao.top/iptables%e5%91%bd%e4%bb%a4%e5%b8%b8%e7%94%a8%e8%a7%84%e5%88%99%e6%b1%87%e6%80%bb/
source: Zgao's blog
date: 2023-03-10
fetch_date: 2025-10-04T09:04:18.367746
---

# iptables命令常用规则汇总

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# iptables命令常用规则汇总

* [首页](https://zgao.top)
* [iptables命令常用规则汇总](https://zgao.top:443/iptables%E5%91%BD%E4%BB%A4%E5%B8%B8%E7%94%A8%E8%A7%84%E5%88%99%E6%B1%87%E6%80%BB/)

[3月 9, 2023](https://zgao.top/2023/03/)

### iptables命令常用规则汇总

作者 [Zgao](https://zgao.top/author/zgao/)
在[[安全运维](https://zgao.top/category/%E5%AE%89%E5%85%A8%E8%BF%90%E7%BB%B4/)](https://zgao.top/iptables%E5%91%BD%E4%BB%A4%E5%B8%B8%E7%94%A8%E8%A7%84%E5%88%99%E6%B1%87%E6%80%BB/)

![iptables命令常用规则汇总](https://zgao.top/wp-content/uploads/2023/03/iptables.png)

iptables非常强大，但是参数选项多，学习成本较高。本文将常用的iptables的命令进行汇总，在关键时刻方便拿来即用。

文章目录

[ ]

* [iptables的四表五链](#iptables%E7%9A%84%E5%9B%9B%E8%A1%A8%E4%BA%94%E9%93%BE "iptables的四表五链")
  + [查看表的详细规则](#%E6%9F%A5%E7%9C%8B%E8%A1%A8%E7%9A%84%E8%AF%A6%E7%BB%86%E8%A7%84%E5%88%99 "查看表的详细规则")
* [端口转发](#%E7%AB%AF%E5%8F%A3%E8%BD%AC%E5%8F%91 "端口转发")
  + [开启内核转发](#%E5%BC%80%E5%90%AF%E5%86%85%E6%A0%B8%E8%BD%AC%E5%8F%91 "开启内核转发")
  + [本地端口转发](#%E6%9C%AC%E5%9C%B0%E7%AB%AF%E5%8F%A3%E8%BD%AC%E5%8F%91 "本地端口转发")
  + [多主机端口转发](#%E5%A4%9A%E4%B8%BB%E6%9C%BA%E7%AB%AF%E5%8F%A3%E8%BD%AC%E5%8F%91 "多主机端口转发")
    - [单端口转发](#%E5%8D%95%E7%AB%AF%E5%8F%A3%E8%BD%AC%E5%8F%91 "单端口转发")
    - [多端口转发](#%E5%A4%9A%E7%AB%AF%E5%8F%A3%E8%BD%AC%E5%8F%91 "多端口转发")
      * [多对一端口转发](#%E5%A4%9A%E5%AF%B9%E4%B8%80%E7%AB%AF%E5%8F%A3%E8%BD%AC%E5%8F%91 "多对一端口转发")
      * [多对多端口转发](#%E5%A4%9A%E5%AF%B9%E5%A4%9A%E7%AB%AF%E5%8F%A3%E8%BD%AC%E5%8F%91 "多对多端口转发")
  + [MASQUERADE的作用](#MASQUERADE%E7%9A%84%E4%BD%9C%E7%94%A8 "MASQUERADE的作用")
* [iptables增加、插入、删除规则](#iptables%E5%A2%9E%E5%8A%A0%E3%80%81%E6%8F%92%E5%85%A5%E3%80%81%E5%88%A0%E9%99%A4%E8%A7%84%E5%88%99 "iptables增加、插入、删除规则")
  + [在第n条规则后插入规则](#%E5%9C%A8%E7%AC%ACn%E6%9D%A1%E8%A7%84%E5%88%99%E5%90%8E%E6%8F%92%E5%85%A5%E8%A7%84%E5%88%99 "在第n条规则后插入规则")
  + [删除指定表中某个链的全部规则](#%E5%88%A0%E9%99%A4%E6%8C%87%E5%AE%9A%E8%A1%A8%E4%B8%AD%E6%9F%90%E4%B8%AA%E9%93%BE%E7%9A%84%E5%85%A8%E9%83%A8%E8%A7%84%E5%88%99 "删除指定表中某个链的全部规则")
* [iptables 拒绝入方向流量](#iptables_%E6%8B%92%E7%BB%9D%E5%85%A5%E6%96%B9%E5%90%91%E6%B5%81%E9%87%8F "iptables 拒绝入方向流量")
  + [拒绝ip段访问本机端口段的请求](#%E6%8B%92%E7%BB%9Dip%E6%AE%B5%E8%AE%BF%E9%97%AE%E6%9C%AC%E6%9C%BA%E7%AB%AF%E5%8F%A3%E6%AE%B5%E7%9A%84%E8%AF%B7%E6%B1%82 "拒绝ip段访问本机端口段的请求")
  + [拒绝指定ip的所有请求](#%E6%8B%92%E7%BB%9D%E6%8C%87%E5%AE%9Aip%E7%9A%84%E6%89%80%E6%9C%89%E8%AF%B7%E6%B1%82 "拒绝指定ip的所有请求")
  + [拒绝ip段的icmp流量](#%E6%8B%92%E7%BB%9Dip%E6%AE%B5%E7%9A%84icmp%E6%B5%81%E9%87%8F "拒绝ip段的icmp流量")
  + [限制只有指定IP段能访问](#%E9%99%90%E5%88%B6%E5%8F%AA%E6%9C%89%E6%8C%87%E5%AE%9AIP%E6%AE%B5%E8%83%BD%E8%AE%BF%E9%97%AE "限制只有指定IP段能访问")
  + [REJECT 和 DROP 的区别](#REJECT_%E5%92%8C_DROP_%E7%9A%84%E5%8C%BA%E5%88%AB "REJECT 和 DROP 的区别")
    - [应用场景](#%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF "应用场景")
* [iptables 拒绝出方向流量](#iptables_%E6%8B%92%E7%BB%9D%E5%87%BA%E6%96%B9%E5%90%91%E6%B5%81%E9%87%8F "iptables 拒绝出方向流量")
  + [放行某个端口，但拒绝其他全部流量](#%E6%94%BE%E8%A1%8C%E6%9F%90%E4%B8%AA%E7%AB%AF%E5%8F%A3%EF%BC%8C%E4%BD%86%E6%8B%92%E7%BB%9D%E5%85%B6%E4%BB%96%E5%85%A8%E9%83%A8%E6%B5%81%E9%87%8F "放行某个端口，但拒绝其他全部流量")
  + [拒绝出方向的域名请求](#%E6%8B%92%E7%BB%9D%E5%87%BA%E6%96%B9%E5%90%91%E7%9A%84%E5%9F%9F%E5%90%8D%E8%AF%B7%E6%B1%82 "拒绝出方向的域名请求")
* [iptables伪造发送源ip](#iptables%E4%BC%AA%E9%80%A0%E5%8F%91%E9%80%81%E6%BA%90ip "iptables伪造发送源ip")
* [iptables限制端口的并发数和请求频率](#iptables%E9%99%90%E5%88%B6%E7%AB%AF%E5%8F%A3%E7%9A%84%E5%B9%B6%E5%8F%91%E6%95%B0%E5%92%8C%E8%AF%B7%E6%B1%82%E9%A2%91%E7%8E%87 "iptables限制端口的并发数和请求频率")
  + [安装压测工具ab](#%E5%AE%89%E8%A3%85%E5%8E%8B%E6%B5%8B%E5%B7%A5%E5%85%B7ab "安装压测工具ab")
  + [限制端口的每分钟请求频率](#%E9%99%90%E5%88%B6%E7%AB%AF%E5%8F%A3%E7%9A%84%E6%AF%8F%E5%88%86%E9%92%9F%E8%AF%B7%E6%B1%82%E9%A2%91%E7%8E%87 "限制端口的每分钟请求频率")
  + [限制端口并发数](#%E9%99%90%E5%88%B6%E7%AB%AF%E5%8F%A3%E5%B9%B6%E5%8F%91%E6%95%B0 "限制端口并发数")
    - [限制端口总并发数](#%E9%99%90%E5%88%B6%E7%AB%AF%E5%8F%A3%E6%80%BB%E5%B9%B6%E5%8F%91%E6%95%B0 "限制端口总并发数")
    - [限制单个ip端口并发数](#%E9%99%90%E5%88%B6%E5%8D%95%E4%B8%AAip%E7%AB%AF%E5%8F%A3%E5%B9%B6%E5%8F%91%E6%95%B0 "限制单个ip端口并发数")
* [iptables规则取反](#iptables%E8%A7%84%E5%88%99%E5%8F%96%E5%8F%8D "iptables规则取反")
* [让iptables规则永久生效](#%E8%AE%A9iptables%E8%A7%84%E5%88%99%E6%B0%B8%E4%B9%85%E7%94%9F%E6%95%88 "让iptables规则永久生效")
  + [使用 iptables-persistent](#%E4%BD%BF%E7%94%A8_iptables-persistent "使用 iptables-persistent")
  + [使用iptables-save 保存规则](#%E4%BD%BF%E7%94%A8iptables-save_%E4%BF%9D%E5%AD%98%E8%A7%84%E5%88%99 "使用iptables-save 保存规则")

## iptables的四表五链

iptables的四表五链是指iptables中的四个表和五个链。四个表分别是：

1. filter表：用于过滤数据包，控制网络流量。
2. nat表：用于对数据包进行地址转换，实现网络地址转换（NAT）功能。
3. mangle表：用于修改数据包的头部信息，比如TTL、TOS等。
4. raw表：用于处理数据包的连接状态，对于未建立连接的数据包进行处理。

五个链分别是：

1. PREROUTING：数据包进入路由之前进行处理。
2. INPUT：数据包进入本机之前进行处理。
3. FORWARD：数据包转发到其他主机之前进行处理。
4. OUTPUT：数据包从本机发出之前进行处理。
5. POSTROUTING：数据包离开路由之后进行处理。

iptables中需要用 -t <表名> 来指定查看对应表的规则，不指定默认为filter表的规则。例如查看nat表的规则：

```
iptables -t nat -L
```

![](https://zgao.top/wp-content/uploads/2023/03/image-3-1024x430.png)

### 查看表的详细规则

```
iptables -t nat -nvL --line-numbers
```

![](https://zgao.top/wp-content/uploads/2023/03/image-2-1024x350.png)

显示编号方便删除指定的规则。

## 端口转发

### 开启内核转发

```
echo "net.ipv4.ip_forward = 1" >>/etc/sysctl.conf
sysctl -p
```

### 本地端口转发

本地端口转发，只涉及一台机器。比如外部访问本机的2222端口转发到本地的22端口。

```
iptables -t nat -A PREROUTING -p tcp --dport 2222 -j REDIRECT --to-port 22
```

![](https://zgao.top/wp-content/uploads/2023/03/image-5-1024x390.png)

添加上面的规则后，外部可以访问，但是本地127.0.0.1无法访问。因为本地的请求不经过PREROUTING。

### 多主机端口转发

> A的ip是192.168.1.2，B的ip是192.168.1.1，A和B是内网互通的，现在有一个外部ip(1.2.3.4)为C，C想通过访问B的2222端口从而访问到A的22端口。

![](https://zgao.top/wp-content/uploads/2023/03/image-1-1024x364.png)

```
iptables -t nat -A POSTROUTING -d 192.168.1.2 -p tcp --dport 22 -j SNAT --to-source 192.168.1.1
```

该命令很重要！将所有从A机器返回的TCP流量的源地址改为B机器的IP地址，不管单端口还是多端口转发都需要执行。

#### 单端口转发

```
iptables -t nat -A PREROUTING -s 1.2.3.4 -p tcp --dport 2222 -j DNAT --to-destination 192.168.1.2:22
```

第一条命令将所有目的地为1.2.3.4且端口为2222的TCP流量重定向到A机器的22端口。

注意：这两条都要在B机器上执行，因为它是外部访问的目标机器。

如果不想限制外部访问的来源是C，可以不指定-s选项。

```
iptables -t nat -A PREROUTING  -p tcp --dport 2222 -j DNAT --to-destination 192.168.1.2:22
```

这样任意外部ip访问都可以请求转发了。

#### 多端口转发

针对上面的命令，如果是多端口转发，可以分为多对一和多对多的情况。

注意：经测试，iptables不支持在一条命令中实现不同主机的多端口的不同映射。比如同时将B的80转发到A的8080，将B的443转发到A的4443。

##### 多对一端口转发

例如将B的50000到60000的端口全部转发到A的443端口，命令如下：

```
iptables -t nat -I PREROUTING  -p tcp  -m multiport --dport 50000:60000 -j DNAT --to-destination 192.168.1.2:443
```

注意：”–dports” 参数指定端口范围，使用冒号 “:” 表示起始端口和结束端口之间的范围。

##### 多对多端口转发

例如将B的50000到60000的端口全部转发到A的50000到60000的端口，命令如下：

```
iptables -t nat -I PREROUTING -p tcp -m multiport --dport 50000:60000 -j DNAT --to-destination 192.168.1.2:50000-60000
```

当然多个端口也可以是不连续的，比如80、443、8080同端口转发，端口用逗号”,”隔开，–to-destination后面的ip不用再指定端口。

```
iptables -t nat -I PREROUTING -p tcp -m multiport --dport 80,443,8080 -j DNAT --to-destination 192.168.1.2
```

注意：–to-destination 参数后，使用”-“表示起始端口和结束端口之间的范围。

### MASQUERADE的作用

MASQUERADE作用是，**从服务器的网卡上，自动获取当前ip地址来做NAT，就不用手动指定转换的目的IP了，实现了动态的SNAT**。

```
iptables -t nat -A POSTROUTING -d 192.168.1.2 -p tcp --dport 22 -j SNAT --to-source 192.168.1.1
```

这条命令用MASQUERADE可以换成下面的写法。

```
iptables -t nat -A POSTROUTING -d 192.168.1.2 -p tcp --dport 22 -j MASQUERADE
```

这样的优点在于机器B的ip如果发生变化，不用重新修改–to-source，iptables会自动替换，实现动态SNAT。

## iptables增加、插入、删除规则

* -A 在最后一条规则后新增规则
* -I 默认将新规则插入到第一条
* -F 不指定<链名>，默认清空整个表的规则
* -D <链名> <规则编号> 删除指定编号的规则

### 在第n条规则后插入规则

```
iptables -I <chain> <rule_number> <new_rule>
```

比如要在nat表的POSTROUTING链的第三条规则后增加一条规则。

```
iptables -t nat -I POSTROUTING 3 <new_rule>
```

### 删除指定表中某个链的全部规则

iptables -t 表名 -F 链名

其中，表名可以是filter、nat、mangle、raw等，链名可以是INPUT、OUTPUT、FORWARD等。

例如，要清空filter表中INPUT链的所有规则，可以使用以下命令：

```
iptables -t filter -F INPUT
```

注意这个操作是不可逆的，清空后所有的规则都将被删除。

## iptables 拒绝入方向流量

### 拒绝ip段访问本机端口段的请求

例如将源IP为47.100.0.0/16的T...