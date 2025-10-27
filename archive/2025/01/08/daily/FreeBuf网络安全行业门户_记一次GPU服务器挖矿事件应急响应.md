---
title: 记一次GPU服务器挖矿事件应急响应
url: https://www.freebuf.com/articles/system/419066.html
source: FreeBuf网络安全行业门户
date: 2025-01-08
fetch_date: 2025-10-06T20:10:04.781316
---

# 记一次GPU服务器挖矿事件应急响应

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

记一次GPU服务器挖矿事件应急响应

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

记一次GPU服务器挖矿事件应急响应

2025-01-07 17:07:46

所属地 广东省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 一、背景

2024年12月26日，我司收到托管机房的网络安全通报，认为我司服务器有挖矿行为，需要当天完成整改。

## 二、影响范围

同一内网的10台GPU服务器，版本均为ubuntu 20.04。

## 三、排查过程

从通报里面知道以下IP为异常IP，从这两个信息开始进行排查，查看威胁情报得知均为德国IP：

209.38.180.198:443 德国矿池

138.68.113.5:80 德国IP

### 3.1 进程分析

先把云安全中心高级版装上，运行全盘扫描，并且等待扫描过程中手工排查服务器，使用`ss -ta`命令发现服务器有和恶意IP连接

![1735912253_6777eb3d28782446addbe.png!small?1735912254528](https://image.3001.net/images/20250103/1735912253_6777eb3d28782446addbe.png!small?1735912254528)

执行`netstat -tnlpu | grep 209.38.180.198`，想查看PID，结果未返回相关结果，反而过了10秒后出现阿里云告警:

![](https://image.3001.net/images/20250103/1735899813_6777baa5d011435fd754e.png!small)

怀疑netstat命令被黑客篡改，使用`stat /usr/bin/netstat`收集篡改时间，可以看到最后一次修改文件属性的时间是2024年9月19日 17:49。询问运维这台服务器什么时候购买的，是在几个月之前，因此基本可以推断入侵时间是在2024年9月19日左右。

![](https://image.3001.net/images/20250103/1735899934_6777bb1e3060f7236eda3.jpg!small)

为避免阿里云安全中心误报，把/usr/bin/netstat下载后丢到威胁情报进行查询，结果依然是报毒：

![](https://image.3001.net/images/20250103/1735899956_6777bb3455c839e9955e9.png!small)

查看行为，有很多`grep -v`反向过滤矿池IP，导致无法使用`netstat -tnlpu`查看pid

![](https://image.3001.net/images/20250103/1735899971_6777bb43c6817e3aae3f8.png!small)

接着阿里云不断报出了新的告警systemctl、top命令全部被篡改，基本可以确定不能继续使用系统命令进行排查

![1736240725_677cee553161d5c04b247.png!small?1736240726298](https://image.3001.net/images/20250107/1736240725_677cee553161d5c04b247.png!small?1736240726298)

![1736240746_677cee6a9309cb460c90c.png!small?1736240747601](https://image.3001.net/images/20250107/1736240746_677cee6a9309cb460c90c.png!small?1736240747601)

下载busybox进行应急

```
cd /root
wget https://www.busybox.net/downloads/binaries/1.35.0-x86_64-linux-musl/busybox
chmod u+x ./busybox
mv ./busybox /usr/bin/busybox
```

执行`busybox top`查看CPU占用最高的进程，发现存在异常进程`/9ac8a281`

![1735900150_6777bbf68aa1d27885100.png!small?1735900151672](https://image.3001.net/images/20250103/1735900150_6777bbf68aa1d27885100.png!small?1735900151672)

查看根目录，不存在/9ac8a281，怀疑文件已经被删掉了，恶意程序应该在内存里运行

```
cat /9ac8a281
cat: /9ac8a281: No such file or directory
cd /proc/4022388/
ls -al | grep exe
```

恶意文件/9ac8a281果然被删除了

![1735900180_6777bc1401aa810984a92.png!small?1735900181077](https://image.3001.net/images/20250103/1735900180_6777bc1401aa810984a92.png!small?1735900181077)

找运维从其他机器上拷贝了一个干净的systemctl到中毒机上，排查守护进程，发现异常服务63f55525.service

```
./systemctl list-units --type=service
 UNIT      LOAD      ACTIVE     SUB          DESCRIPTION                                                                     >
● 63f55525.service    not-found failed     failed       63f55525.service
……
```

执行`./systemctl status 63f55525.service`，看到加载恶意文件/9ac8a281

![1735900219_6777bc3b9df26a8d9c7b0.png!small?1735900220727](https://image.3001.net/images/20250103/1735900219_6777bc3b9df26a8d9c7b0.png!small?1735900220727)

查看这个守护进程的具体配置，找到恶意文件的位置`/usr/bin/9ac8a28120cf5089`

```
cat /usr/lib/systemd/system/63f55525.service

[Service]
Type=simple
User=root
TimeoutStartSec=1200
ExecStart=/usr/bin/9ac8a28120cf5089 9ac8a281

Restart=always
RestartSec=4h
KillMode=process

## 全局查找是否还有恶意文件
find / -name "9ac8a28*"
```

查看开机启动项、定时任务、系统账号、挂载，无异常

```
cat /var/spool/cron/crontabs
cat /etc/passwd
df -h
cat /proc/mounts
cat /etc/rc.local
cat: /etc/rc.local: No such file or directory
(base) root@gpua15:/var/spool/cron/crontabs# systemctl status rc-local
● rc-local.service - /etc/rc.local Compatibility
     Loaded: loaded (/lib/systemd/system/rc-local.service; static; vendor preset: enabled)
    Drop-In: /usr/lib/systemd/system/rc-local.service.d
             └─debian.conf
     Active: inactive (dead)
       Docs: man:systemd-rc-local-generator(8)
```

使用unhide工具检查隐藏进程，发现上百个隐藏进程

```
apt install unhide
unhide proc

Used options:
[*]Searching for Hidden processes through /proc stat scanning

Found HIDDEN PID: 5043
        Cmdline: "/9ac8a281"
        Executable: "/9ac8a281 (deleted)"
        Command: "9ac8a281"
        $USER=root
        $PWD=/

Found HIDDEN PID: 5044
        Cmdline: "/9ac8a281"
        Executable: "/9ac8a281 (deleted)"
        Command: "9ac8a281"
        $USER=root
        $PWD=/

Found HIDDEN PID: 5045
        Cmdline: "/9ac8a281"
        Executable: "/9ac8a281 (deleted)"
        Command: "9ac8a281"
        $USER=root
        $PWD=/

Found HIDDEN PID: 5046
        Cmdline: "/9ac8a281"
        Executable: "/9ac8a281 (deleted)"
        Command: "9ac8a281"
        $USER=root
        $PWD=/

Found HIDDEN PID: 5047
        Cmdline: "/9ac8a281"
        Executable: "/9ac8a281 (deleted)"
        Command: "9ac8a281"
        $USER=root
        $PWD=/

Found HIDDEN PID: 5048
        Cmdline: "/9ac8a281"
        Executable: "/9ac8a281 (deleted)"
        Command: "9ac8a281"
        $USER=root
        $PWD=/

Found HIDDEN PID: 6461
        Cmdline: "/9ac8a281"
        Executable: "/9ac8a281 (deleted)"
        Command: "9ac8a281"
        $USER=root
        $PWD=/

Found HIDDEN PID: 6462
        Cmdline: "/9ac8a281"
        Executable: "/9ac8a281 (deleted)"
        Command: "9ac8a281"
        $USER=root
        $PWD=/
…………
```

### 3.2 遏制过程

```
##杀掉恶意进程
kill -9 4022388
kill -9 6462   #删除1个恶意隐藏进程后，其他也会消失，原理未知

##删除守护进程
./systemctl stop 63f55525.service
./systemctl disable 63f55525.service
rm -rf /usr/bin/9ac8a28120cf5089
```

重复**3.1 进程分析**步骤，未发现有新的恶意进程启动，服务器暂时恢复正常

### 3.3 恢复过程

1.删除后门，查看云安全中心，发现有异常可执行文件/etc/ssh/ssh\_host\_dsa\_key.pub
![1735900359_6777bcc7b58eda0e65d4f.png!small?1735900361019](https://image.3001.net/images/20250103/1735900359_6777bcc7b58eda0e65d4f.png!small?1735900361019)

丢沙箱查看，是一个后门

![1736240543_677ced9f3cb6b3a1ddd56.png!small?1736240543850](https://image.3001.net/images/20250107/1736240543_677ced9f3cb6b3a1ddd56.png!small?1736240543850)

`ping example.servidor.world`，解析出来IP是138.68.113.5，跟通报文件里的恶意IP吻合，从情报和行为可以判断这是远控服务器的IP，而且可以看到还有另外一个远控IP 185.125.188.58

![1736240521_677ced8985ec1d6770982.png!small?1736240521996](https://image.3001.net/images/20250107/1736240521_677ced8985ec1d6770982.png!small?1736240521996)

清理后门，发现被锁定了，无法删除、移动、改权限，可以判断攻击者用chattr锁定了文件

![1735900404_6777bcf4c3ed7bd0ac34a.png!small?1735900406471](https://image.3001.net/images/20250103/1735900404_6777bcf4c3ed7bd0ac34a.png!small?1735900406471)

使用`chattr -ia /etc/ssh/ssh_host_dsa_key.pub`解锁，结果报错不存在该命令，提示让我使用vmlinux1来代替chattr执行（此处漏了截图），由于怕中毒，不敢用vmlinux1命令

下载/usr/bin/vmlinux1，上传到沙箱，结果为正常文件，但保守起见还是不敢用vmlinux1来代替chattr命令

![1736240654_677cee0e2f6ffeaea6680.png!small?1736240654720](https://image.3001.net/images/20250107/1736240654_677cee0e2f6ffeaea6680.png!small?1736240654720)

使用`lsattr /etc/ssh/ssh_host_dsa_key.pub`命令查看，结果lsattr命令也被黑客删除了

从干净的服务器上下载chattr和lsattr文件，上传到中毒服务器，再用lsattr查看，果然后门文件是被锁定了禁止变更

```
chmod +x ./chattr
chmod +x ./lsattr
mv ./lsattr /usr/bin
mv ./chattr /usr/bin
lsattr /etc/ssh/ssh_host_dsa_key.pub
```

![1735906986_6777d6aa298d26d821954.png!small?1735906986494](https://image.3001.net/images/20250103/1735906986_6777d6aa298d26d821954.png!small?1735906986494)

解锁并删除vmlinux1和后门文件

```
chattr -ia /usr/bin/vmlinux1
chattr -ia /etc/ssh/ssh_host_dsa_key.pub
rm -rf /usr/bin/vmlinux1
rm -rf /etc/...