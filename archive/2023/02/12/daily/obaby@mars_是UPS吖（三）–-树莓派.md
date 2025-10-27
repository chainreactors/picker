---
title: 是UPS吖（三）–-树莓派
url: https://h4ck.org.cn/2023/02/%e6%98%afups%e5%90%96%ef%bc%88%e4%b8%89%ef%bc%89-%e6%a0%91%e8%8e%93%e6%b4%be/
source: obaby@mars
date: 2023-02-12
fetch_date: 2025-10-04T06:25:34.822657
---

# 是UPS吖（三）–-树莓派

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[Linux『Linux』](https://h4ck.org.cn/cats/xtxg/linux%E3%80%8Elinux%E3%80%8F), [个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 是UPS吖（三）–-树莓派

2023年2月11日
[5 条评论](https://h4ck.org.cn/2023/02/11176#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)

装ups的另外一个目的就是为了保证树莓派的存储卡不会因为意外断电而出现问题。其实要解决这个问题个人觉得也简单，毕竟也是个linux啊。可以基于nut实现。

> The primary goal of the Network UPS Tools (NUT) project is to provide support for Power Devices, such as Uninterruptible Power Supplies, Power Distribution Units, Automatic Transfer Switches, Power Supply Units and Solar Controllers. NUT provides a common protocol and set of tools to monitor and manage such devices, and to consistently name equivalent features and data points, across a vast range of vendor-specific protocols and connection media types.

> NUT provides many control and monitoring [features](https://networkupstools.org/features.html), with a uniform control and management interface. If you are just getting acquainted with NUT, [that page](https://networkupstools.org/features.html) also explains the technical design and some possible set-ups.
>
> More than 170 different manufacturers, and several thousands of models are [compatible](https://networkupstools.org/stable-hcl.html).
>
> https://networkupstools.org/index.html

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210212514.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210212514.jpg)

为了要实现树莓派在断电之后还能和venus通讯需要将华为的路由器也切换到ups系统上，只有这样在断电之后树莓派才能直到断电了。晚上重新梳理了一下家的网络拓普（不是专业网络工程师，图例可能用的不太对）

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210224004.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210224004.jpg)

于是又让我想到了联通的工程师来家里换光纤的时候直摇头，哈哈哈。现在组网方式包括5g桥接，光纤，网线，哈哈哈。这个对接种类神奇了。一台企业路由+一台企业交换机+2套光转换+4台无线路由器。好处就是现在家里无线网络无死角覆盖，速度嘛也非常ok。就是太费电，但是我也不想再改了啊，太麻烦了。

都切换到ups供电之后在树莓派上就可以开始配置了：

1.安装nut client

```
sudo apt install nut
```

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210211534.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210211534.jpg)

2.修改配置文件：

```
编辑/etc/nut/nut.conf，MODE设置如下：

MODE=netclient
编辑/etc/nut/upsmon.conf，MONITOR设置如下：

MONITOR ups@192.168.1.12 1 monuser secret slave
说明：

MONITOR <system> <powervalue> <username> <password> ("master"|"slave")
#<system>设置为ups@服务器地址或域名，这里是ups@192.168.1.12
#<powervalue>设置为1
#<username>群晖UPS服务器的默认用户名是monuser
#<password>群晖UPS服务器的默认密码是secret
#("master"|"slave")，客户机设置为slave
```

3.测试链接，需要修改venus添加允许的ip地址，如果看到下面的内容那就成功啦：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210212304.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210212304.jpg)

4. 启动服务：

```
systemctl start nut-client
```

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210212330.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210212330.jpg)

5.设置服务开机自启动

```
systemctl enable nut-client
```

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210212445.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210212445.jpg)

如果出现下面的错误，可以检查服务器ip白名单，群晖修改白名单之后要点击右下角的应用才会生效。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230210212127.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230210212127.jpg)

**延伸设置—自定义关机设置：**

默认关机逻辑貌似是：nut服务会在UPS发送`LOWBATT`时通知机器关机，触发时机默认为ups电量剩余`20%`。

如果要自定义关机设置需要进行如下设置（因为群辉提供的ups服务器在ups断电之前就关闭了，不清楚服务器在关机之前是不是会发送lowbatt消息）

1.编辑upsmon.conf,添加以下内容：

```
vim /etc/nut/upsmon.conf
```

```
NOTIFYCMD /sbin/upssched
NOTIFYFLAG ONBATT SYSLOG+WALL+EXEC
```

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230212194008.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230212194008.jpg)

通知类型定义：

```
NOTIFYMSG type message
upsmon comes with a set of stock messages for various events. You can change them if you like.

NOTIFYMSG ONLINE "UPS %s is getting line power"
NOTIFYMSG ONBATT "Someone pulled the plug on %s"
Note that %s is replaced with the identifier of the UPS in question.

The message must be one element in the configuration file, so if it contains spaces, you must wrap it in quotes.

NOTIFYMSG NOCOMM "Someone stole UPS %s"
Possible values for type:

ONLINE
UPS is back online

ONBATT
UPS is on battery

LOWBATT
UPS is on battery and has a low battery (is critical)

FSD
UPS is being shutdown by the primary (FSD = "Forced Shutdown")

COMMOK
Communications established with the UPS

COMMBAD
Communications lost to the UPS

SHUTDOWN
The system is being shutdown

REPLBATT
The UPS battery is bad and needs to be replaced

NOCOMM
A UPS is unavailable (can’t be contacted for monitoring)

NOTIFYFLAG type flag[+flag]…
By default, upsmon sends walls global messages to all logged in users) via /bin/wall and writes to the syslog when things happen. Except for Windows where upsmon only writes to the syslog by default. You can change this.

Examples:

NOTIFYFLAG ONLINE SYSLOG
NOTIFYFLAG ONBATT SYSLOG+WALL+EXEC
Possible values for the flags:

SYSLOG
Write the message to the syslog

WALL
Write the message to all users with /bin/wall

EXEC
Execute NOTIFYCMD (see above) with the message

IGNORE
Don’t do anything

If you use IGNORE, don’t use any other flags on the same line.
```

2.修改upssched.conf添加以下内容

```
vim /etc/nut/upssched.conf
```

```
CMDSCRIPT /etc/nut/upssched-cmd #编写此脚本设置
# NOTIFYCMD /sbin/upssched
# NOTIFYFLAG ONBATT SYSLOG+WALL+EXEC
PIPEFN /etc/nut/upssched.pipe
LOCKFN /etc/nut/upssched.lock

AT ONBATT * START-TIMER power-off 60
AT ONLINE * CANCEL-TIMER power-off
AT ONLINE * EXECUTE power-on
```

3.编辑upssched-cmd脚本

```
vim /etc/nut/upssched-cmd
```

文件内容：

```
#!/bin/sh
 case $1 in
       onbatt)
          logger -t upssched-cmd "UPS running on battery"
          # do somethings ,e.g.send email \ wechat
       /usr/sbin/upsmon -c fsd
          ;;
       power-off)
          logger -t upssched-cmd "UPS running on battery power off"
          /usr/sbin/upsmon -c fsd
          ;;
       shutdowncritical)
          logger -t upssched-cmd "UPS on battery critical, forced shutdown"
          /usr/sbin/upsmon -c fsd
          ;;
       upsgone)
          logger -t upssched-cmd "UPS has been gone too long, can't reach"
          ;;
       *)
          logger -t upssched-cmd "Unrecognized command: $1"
          ;;
 esac
```

修改完成之后重启服务。

参考链接：

https://typecho.leosutopia.cn/index.php/archives/248/#comment-13

https://networkupstools.org/docs/man/index.html#User\_man

https://networkupstools.org/docs/man/upssched.conf.html

https://networkupstools.org/docs/man/upsmon.conf.html

https://www.cnblogs.com/LandWind/articles/pve-nut-config.html

https://www.storyxc.com/pages/41ed75/#%E7%BC%96%E5%86%99%E8%84%9A%E6%9C%AC

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《是UPS吖（三）–-树莓派》](https://h4...