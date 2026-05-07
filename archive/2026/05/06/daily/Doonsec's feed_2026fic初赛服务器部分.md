---
title: 2026fic初赛服务器部分
url: https://mp.weixin.qq.com/s/WSvFM5006o4pWeD2Ev8Omg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:28:48.914712
---

# 2026fic初赛服务器部分

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rlZyoc3CBwabXxyudiafSvliaEWepskoKeMUibnpYznqOf3lKaRBpoEUUm6M3I8cL3SOjnuSs5yur5ggF3foElTqAQqvm1zmKBMLI/0?wx_fmt=jpeg)

# 2026fic初赛服务器部分

原创

浪漫土狗
浪漫土狗

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

我的五一怎么就这么没了😭😭😭

火眼可以直接仿真，添加时选择两块镜像，操作系统选择linux即可

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlE8n4gjCGUspT085BCANW8eHCFzxENVbsicZfBYp7PHvbKa2IyZUeIDX7EY0SoSWaxYKzpKrxrWwBSqSnibKlPOoIRN5UOYsgbM/640?wx_fmt=png&from=appmsg)

ssh需要自己下载，安装完后修改下配置文件/etc/ssh/sshd\_config

进去之后发现是图形化界面，一切操作都是正常的，但是实际上我们直接进入的是容器。

***判断当前是否是在docker中***：

```
cat /proc/1/cgroup
```

**如果是容器（如 Docker）**，你会看到类似：0::/docker/3f2c7e9a8c1d...或0::/kubepods/...；**如果是本机 / 虚拟机**，通常看到：0::/或者包含 `system.slice`、`user.slice`等，而没有 docker/containerd

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rl9IYH1iacJHv7JVDziay79Yo585MObecTaLQomb1ZtLmtvibia3ibZHsXeVribneGficiaeDZDXibajXMj7b4ucmNv8JL2QyEzvyeOkwJI/640?wx_fmt=png&from=appmsg)

显然我们打开后的图形化界面是docker容器，如果直接在docker中做题的话会发现得到的答案与标准答案不一样，所以第一步我们要回到本机，方法也很简单，就是：`ctrl+alt+f2`

#### 该服务器主机操作系统版本为

```
cat /etc/os-release
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmOOF5xaJk6R8owTrHEUmCMyibJZnpdenBP3mciaiaEpibRvFA9fFib3NPhmzyAlNQuvfvk8pN9LYPKmd2vic5eicPj6XX0phxBxpIibVs/640?wx_fmt=png&from=appmsg)

Debian GNU/Linux 13 (trixie)

#### 该服务器根分区硬盘的uuid号为

```
cat /etc/fstab
```

***fstab***:存放的是**Linux 文件系统挂载配置信息**

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlr1SpKC3LKr7eva3FyiaxcSJibBtm4ms8henBanqxwgZ2I0EicublTOHwLkqSNqncuE2YeKQeDM7icG9VQAKcKKvMntonKib7GL1Kg/640?wx_fmt=png&from=appmsg)

问的是根分区，对应的uuid就是3231e52f-5e15-44c4-b224-e29cb4201c0e

#### 该服务器中最新的docker镜像创建时间为

```
docker images
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rnz1rrjkxeOlEicMaky80qlaflasbeiacYiaicJIibs2YvJQkdtW1953qFkeicVMlh0M2k3PE1emicM3L9yG8l73odqrVxxtgbzEASJas/640?wx_fmt=png&from=appmsg)

首先看下最新创建的镜像是哪一个，然后查看该镜像的详细信息找到创建时间

```
docker inspect u22
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlgSRG4sL4iamElvvfEalBzJ5rfdEAq09VxKtG9u8cWQFiaCO9gq9JaxT4dNEOO4Py90Dxav5yxE7Esfhic7s6UKM4lnias2MWgQBQ/640?wx_fmt=png&from=appmsg)

2026-04-16T07:15:50.535713491Z

#### 该服务器根分区快照路径为

根分区为 Btrfs，查看子卷

```
btrfs subvolume list /
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlktXYwCfR5G6mrcq8ubRTt154JB4bHkZdE0jTG7ydomdQmjQ5GJc6Q488X9eicCDgKTBbvtibsw5cmje4N71pdlkTZx5YNcUibRU/640?wx_fmt=png&from=appmsg)

子卷常被用作快照或独立的管理单元，这里的快照路径就是/root/history

#### 该网站后台管理入口对应的文件名为

```
grep "入口" . -r
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkQLHLe8ZKfhebRicM4VHrdFWG4GnsLBHfkOiacAnTSD2w2k0Wr7VvSib5Q4o7hia4FEqSfOy1icevGXfDTU3icXsEVYImRJfetFByWU/640?wx_fmt=png&from=appmsg)

在user.php中匹配到关键词，所以入口文件为user.php

#### 该网站设置的icp备案号为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkmQGQfR4UAJCHLhU1SRllU7MsBAylYDSGicTcuqvZpp9iaQ5gO07Mvc17I4fhz5w5wObbXetKDRZQRoicvTE5crvPf6rTympfYjg/640?wx_fmt=png&from=appmsg)

一眼顶针icp1919810

#### 该网站设置的主域名为

出现在和上一题一样的文件里面，我们先匹配到该文件，然后翻看找到

```
grep "1919810" . -r
cat ./application/extra/maccms.php
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlTHG4JrgZr4r5FibQSAJl3ckohwibYP8jVGxlq8Gb51NS1BJiaMBBtnXrsf8lK4ulTrJDiaWVwKcUZ7UOCojgpTuEqochuibbIOkrY/640?wx_fmt=png&from=appmsg)

`www.2026fic.forensix`

#### 该网站分类3中，视频的拼音为

数据库相关的配置信息在/var/www/html/maccms10/application/database.php中，找到地址相关的信息

20260506105751.png

这题需要看数据库，如何连接可以看后面的题目解析，这里就直接连接了。最开始我是不能远程连接的，因为存在LXC 桥接接口 lxcbr0 缺少 IPv4 地址配置的问题，解决方法就是在主机运行如下命令：

```
ip addr add 10.0.3.1/24 dev lxcbr0

mysql -h 10.0.3.100 -u aa -p123456 --skip-ssl#测试能否链接
```

成功连接上后我们直接使用navcat远连，使用ssh隧道即可成功连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlk1pRlaN4QjnkLxYKyMKa5NpCUoia33j0UYJJqzsibFujkJehdKibTetWDtPpsWGZl0jnnbCYJCI5amWmtndgCwiaib6tD6ibLcAGWA/640?wx_fmt=png&from=appmsg)

找到数据库中对应的位置，可以看到，分类三中的视频对应的vod\_en就是我们要的答案：sipaanshe

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmnoic7SQibhwiaeASKDWe1RRA4InNJm7vicAyLXGBJWTTPRanRRB9ibYVqAvEFPibqx548kiac3EZByYYtM8z6GStliaOictgsNuQ02Qp4/640?wx_fmt=png&from=appmsg)

#### 该站点设置页面中，被使用的前端模板来自于哪个源文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkPfWSk5wgqDsSs7RtPqooY8jmkf1EWnzFicgib97pJKKmQGiadia0efzbXiarpbpEl16IL9oSwvDrw5G1lRXevhRfQUhXzLl8tEzTM/640?wx_fmt=png&from=appmsg)

```
cat ./application/extra/maccms.php | grep "template" -A 5
```

首先看配置文件maccms.php，去匹配模板相关的关键词，找到对应的目录是001tep，然后进到该目录下寻找，找到info.ini文件![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rnx8EvJrA8cNCd5uEgH7sTyvLLSKSQXfGictZVSszsYeHEw5wSsfzaDicsvxbPzcE6nNCiclTwwkJpZfWsia6NsanT5nKYGRia4yap4/640?wx_fmt=png&from=appmsg)

#### 该网站的伪静态规则配置文件sm3值为

该网站是nginx，所以伪静态规则存放在`/etc/nginx/sites-enabled/default`中

***计算sm3***：

```
openssl dgst -sm3 /etc/nginx/sites-enabled/default
#SM3(/etc/nginx/sites-enabled/default)= e73407468e6f52af54c7b14632eeeb9be25b05106d06c4c3085fc843c223793f
```

e73407468e6f52af54c7b14632eeeb9be25b05106d06c4c3085fc843c223793f

#### 该网站关联的数据库的ip地址为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlJYXRiaOc55FwQUYthwwVbnVqhibPF3iaVY9IQ2Z03I7MrdyMRPXFPC1dkrmFJQrqzfaUdrz95BAkyuUaHaz5DPx32XFtboRCgTk/640?wx_fmt=png&from=appmsg)

地址给的不是ip，我们需要去/etc/hosts中寻找对应的IP地址

```
cat /etc/hosts | grep "mytidb" -A 5
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlsuKBicREbAC3s3yvOaBia6NEZ2vTkhKKlgS26TgTJblAQ8VlXFvezGFQdPia956bLjYeCYs1dNFs3cgUgOH75MYe1GObicWXOYhk/640?wx_fmt=png&from=appmsg)

10.0.3.100

当然这一题也可以通过查看lxc容器信息找到IP：

看了下数据库似乎不在本机里面，这是需要考虑是不是存在容器里面，先匹配所有常见的docker容器的进程：

```
ps aux | grep -E "dockerd|lxd|lxcfs|containerd|podman|crio|kata|firecracker|runc"
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rn89tvpayRJI0HfzaCric6gAOZ6RFkHSf6v9zSlWwREicfhDMjAEAOerODZc5eXHmIvfIlRLqHdzicIaoERaA20HV0eb3PLLt0LUQ/640?wx_fmt=png&from=appmsg)

显示存在docker容器和lxc容器服务，docker中并没有找到数据库的容器，所以只可能在lxc中

***lxc容器操作***：

```
root@ubuntu:/var/www/html/maccms10/application# lxc-ls                                           mytidb
```

所以现在可以确认数据库存放在lxc容器中的。

```
lxc-start -n mytidb
#lxc-start: mytidb: ../src/lxc/tools/lxc_start.c: lxc_start_main: 257 Container is already running
```

启动容器，发现容器是开着的，直接命令行操作的话可以执行如下操作进入容器再登录mysql

```
lxc-attach -n mytidb#进入容器
```

```
lxc-info mytidb
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rn42JPSOibOapvboPHCNtU5OV3BOLf2qO5pEmV6OCFMoQvbGHBDKFWMP1kZguRTCnbLGwoAKZMuInDD65SRumQhq47Fibc0icSO3A/640?wx_fmt=png&from=appmsg)

#### 该网站数据库使用了哪一类容器技术

从前面的题目可知是LXC

#### 运行在4000端口的备份数据库版本号为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkla8TsA1fr4krVqR2haIsmibrFVYpBWmVBOxzZ6ykfBsXhPcOibk8WswfJkLlGvsP1X0X091QRKo1K9Re9e6xPibVibcRA047Nobs/640?wx_fmt=png&from=appmsg)

改为连接4000端口的数据库，然后执行命令查看数据库版本：8.0.11-TiDB-v7.5.0

#### 新注册用户数量最多的日期为

```
SELECT  FROM_UNIXTIME(user_reg_time,'%Y-%m-%d'),COUNT(*) FROM mac_user GROUP BY FROM_UNIXTIME(user_reg_time,'%Y-%m-%d') ORDER BY COUNT(*) DESC;
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkN2B6nODksVUbLvyDy7HIGV4stqFZ59LsAACv4biaKXs4apFKGJ9ZwgHzQ1dyOPrTiasOjS1g4bF5TK6zB1JbDovjeBs16grgg8/640?wx_fmt=png&from=appmsg)

2026-04-15

#### 马慧美最后一次登录该网站的ip为

```
SELECT user_name,inet_ntoa(user_last_login_ip) from mac_user where user_name like "Ma%Hui%Mei";
```

`inet_ntoa()`：把 IPv4 的“整数形式”转换成“点分十进制字符串”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rm85cKxFteqzRbXM2vWZEbdLEr3bavXyzLYo0WWWZHLqJgSzHztCiad2GULmTPLvYFo8gy9z5TEib5oaFqw1q4IicBsCcQqtqWR8M/640?wx_fmt=png&from=appmsg)

#### 以下哪个文件系统未被使用

A.ntfs B.btrfs C.xfs D.Lvm

在fstab中可以看到根分区就是btrfs文件系统，在 Linux 中判断“有没有使用 LVM”，一般看 **是否存在 PV/VG/LV**，以及 **挂载的设备是否是 dm（device-mapper）设备**

最常用：看 LV / VG / PV 是否存在：

```
pvs; vgs; lvs
```

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkZjZxzBdNgyTzzjEsuegptFmPVwAgiaRqSbmID0RibLvHOvVpMnRwRhEk76iblp7sKHPl8UqGib6KBkC7CZhMrvl7KRQwjSz9qrQM/640?wx_fmt=png&from=appmsg)

有输出非空就说明是存在的，还有ac两个没有出现过

#### 该服务器安装了以下那些数据库服务

A.mysql B.GuessDB C.tidb D.postgresql E.Mariadb

```
ss -lntp | grep -E "3306|4000|5432"
```

| 端口 | 数据库 |
| --- | --- |
| 3306 | MySQL / MariaDB |
| 4000 | **TiDB** |
| 5432 | PostgreSQL |

这里直接匹配常见的端口，看看有没有对应的进程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlWOTfXsHqEHx8VP4gAicHRD7cmuZ...