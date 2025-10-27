---
title: 最后防线：Linux主机入侵外连行为检测
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247486804&idx=1&sn=7575cb69ec2476b8179625d7738eb38e&chksm=fdf96641ca8eef57626ad4ddc6b508ed370afd72cab9e4d533419b882263b563e651d46fa295&scene=58&subscene=0#rd
source: debugeeker
date: 2022-11-24
fetch_date: 2025-10-03T23:39:26.695386
---

# 最后防线：Linux主机入侵外连行为检测

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbwxnfgn0pz8tAaPyc08JXNnniaJtXV3zY5kmytB9m1ibg7KxTswph9kMibBFZ1k97UgLtePqgjGAeabg/0?wx_fmt=jpeg)

# 最后防线：Linux主机入侵外连行为检测

原创

debugeeker

奶牛安全

> 主机入侵检测系统系列：这一篇讲述检测外连行为的原理和技术，可统一检测宿主机和docker子机

一台主机入侵后，入侵者往往会把数据发送出去或启动reverse shell。一般在`IDC`的出口防火墙都会有检测异常外连行为，可能由于中间有`NAT`，并不一定知道是哪台机器过来，但即使是知道哪台机器过来的，也不知道是该台机器哪个程序发起的外连行为。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbw4sqO8YJtsKic83ayaJJOY2Z7fn3ibiakpkouCKMGHE28aGOn1Iy3JjsdBnkB0ibdA6Kqj4j4zvsDZZw/640?wx_fmt=jpeg)

通常的操作，都是用`netstat`命令来获取

```
[root@bogon-agent test]# netstat -anp4
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:42485         0.0.0.0:*               LISTEN      33041/node
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1640/sshd
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      1885/master
tcp        0      0 127.0.0.1:55622         127.0.0.1:42485         ESTABLISHED 25101/sshd: buckxu@
tcp        0      0 127.0.0.1:42485         127.0.0.1:50352         ESTABLISHED 33041/node
tcp        0      0 127.0.0.1:42485         127.0.0.1:55622         ESTABLISHED 25171/node
tcp        0      0 127.0.0.1:50354         127.0.0.1:42485         ESTABLISHED 128902/sshd: buckxu
tcp        0      0 192.168.190.129:45782   192.168.190.128:1514    ESTABLISHED 2109/ossec-agentd
tcp        0      0 127.0.0.1:50352         127.0.0.1:42485         ESTABLISHED 128902/sshd: buckxu
tcp        0      0 192.168.190.129:22      192.168.190.1:62331     ESTABLISHED 25087/sshd: buckxu
tcp        0      0 127.0.0.1:42485         127.0.0.1:50354         ESTABLISHED 128969/node
tcp        0      0 127.0.0.1:42485         127.0.0.1:55620         ESTABLISHED 33041/node
tcp        0      0 192.168.190.129:22      192.168.190.1:52429     ESTABLISHED 128898/sshd: buckxu
tcp        0      0 127.0.0.1:55620         127.0.0.1:42485         ESTABLISHED 25101/sshd: buckxu@
udp        0      0 0.0.0.0:68              0.0.0.0:*                           103880/dhclient
```

但如果放在`HIDS（主机入侵检测系统）`实现，就不可能调用命令，原因如下：

1. 有些Linux机器可能没有安装`netstat`命令
2. 即使有`netstat`命令，也可能由于之前的操作，导致`netstat`运行时依赖的so库缺失或符号缺失，导致无法执行这个命令
3. `netstat`命令执行有异常，变成僵尸进程
4. `netstat`命令在宿主机是没办法查到docker里的外连行为

![](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbw4sqO8YJtsKic83ayaJJOY2zyywA6svXhGC0jveQYMJlsgiaV3rUmvNnlRRUlF1zDfys0TQfXUleHA/640?wx_fmt=jpeg)

按照`Unix哲学`，**一切皆文件**，像端口和进程信息这些内容都可以从`/proc`文件系统下找到，所以`HIDS`是会`/proc`获取这些信息。

下面拿上面命令结果的`2109/node`来做例子展示这种手段。

* 由于一个`socket`在Linux里是一个`fd`，先看一下`/proc/2109/fd`的内容

  ```
  [root@bogon-agent ~]# ls -l /proc/2109/fd
  total 0
  lrwx------. 1 root root 64 Jan  4 18:35 0 -> /dev/null
  lrwx------. 1 root root 64 Jan  4 18:35 1 -> /dev/null
  lrwx------. 1 root root 64 Jan  4 18:35 2 -> /dev/null
  lrwx------. 1 root root 64 Jan  4 18:35 3 -> socket:[26069]
  lr-x------. 1 root root 64 Jan  4 18:35 4 -> /dev/urandom
  lrwx------. 1 root root 64 Jan  4 18:35 5 -> /var/ossec/queue/rids/005
  lrwx------. 1 root root 64 Jan  4 18:35 6 -> /var/ossec/queue/rids/sender_counter
  lrwx------. 1 root root 64 Jan  4 18:35 7 -> socket:[18173675]
  lrwx------. 1 root root 64 Jan  4 18:35 8 -> socket:[2986416]
  ```
* 取这一行

  ```
  lrwx------. 1 root root 64 Jan  4 18:35 7 -> socket:[18173675]
  ```

  其中**2969198**是`inode`。到`/proc/33041/net`找一下这个`inode`是在哪个文件有使用

  ```
  [root@bogon-agent ~]# grep -rIn "18173675" /proc/2109/net
  /proc/2109/net/tcp:9:   7: 81BEA8C0:B2D6 80BEA8C0:05EA 01 00000000:00000000 00:00000000 00000000   983        0 18173675 1 ffff9259346e3640 20 4 30 10 7
  ```
* 看一下`/proc/2109/net/tcp`的内容

  ```
  [root@bogon-agent ~]# cat /proc/2109/net/tcp
  sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode
  0: 0100007F:A5F5 00000000:0000 0A 00000000:00000000 00:00000000 00000000  1000        0 2969198 1 ffff92593308be00 100 0 0 10 0
  1: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 24908 1 ffff925934638000 100 0 0 10 0
  2: 0100007F:0019 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 25073 1 ffff9259346387c0 100 0 0 10 0
  3: 0100007F:D946 0100007F:A5F5 01 00000000:00000000 00:00000000 00000000  1000        0 28151168 1 ffff92593308b640 20 4 30 3 2
  4: 0100007F:A5F5 0100007F:C4B0 01 00000000:00000000 00:00000000 00000000  1000        0 4419751 1 ffff9259346e3e00 20 4 28 10 12
  5: 0100007F:A5F5 0100007F:D946 01 00000000:00000000 00:00000000 00000000  1000        0 28146298 1 ffff92593308f440 21 4 28 10 -1
  6: 0100007F:C4B2 0100007F:A5F5 01 00000000:00000000 00:00000000 00000000  1000        0 4418745 1 ffff9259346e45c0 20 4 28 3 2
  7: 81BEA8C0:B2D6 80BEA8C0:05EA 01 00000000:00000000 00:00000000 00000000   983        0 18173675 1 ffff9259346e3640 20 4 30 10 7
  8: 0100007F:C4B0 0100007F:A5F5 01 00000000:00000000 00:00000000 00000000  1000        0 4418744 1 ffff9259346e2e80 20 4 30 4 4
  9: 81BEA8C0:0016 01BEA8C0:F37B 01 0000004C:00000000 01:00000015 00000000     0        0 28146223 4 ffff9259346e7440 21 4 31 10 663
  10: 0100007F:A5F5 0100007F:C4B2 01 00000000:00000000 00:00000000 00000000  1000        0 4419752 1 ffff9259346e4d80 20 4 30 10 7
  11: 0100007F:A5F5 0100007F:D944 01 00000000:00000000 00:00000000 00000000  1000        0 28146297 3 ffff9259330887c0 20 4 31 10 25
  12: 81BEA8C0:0016 01BEA8C0:CCCD 01 00000000:00000000 02:0004A056 00000000     0        0 4418688 2 ffff9259346e1f00 23 4 30 10 579
  13: 0100007F:D944 0100007F:A5F5 01 00000000:00000000 00:00000000 00000000  1000        0 28151167 2 ffff92593308ae80 20 4 30 10 -1
  ```
* 由于每个`/proc/<pid>/net/tcp`文件的格式和`/proc/net/tcp`是一样的，按照Linux内核文档`Documentation/networking/proc_net_tcp.txt`的内容

  ```
  This document describes the interfaces /proc/net/tcp and /proc/net/tcp6.
  Note that these interfaces are deprecated in favor of tcp_diag.

  These /proc interfaces provide information about currently active TCP
  connections, and are implemented by tcp4_seq_show() in net/ipv4/tcp_ipv4.c
  and tcp6_seq_show() in net/ipv6/tcp_ipv6.c, respectively.

  It will first list all listening TCP sockets, and next list all established
  TCP connections. A typical entry of /proc/net/tcp would look like this (split
  up into 3 parts because of the length of the line):

     46: 010310AC:9C4C 030310AC:1770 01
     |      |      |      |      |   |--> connection state
     |      |      |      |      |------> remote TCP port number
     |      |      |      |-------------> remote IPv4 address
     |      |      |--------------------> local TCP port number
     |      |---------------------------> local IPv4 address
     |----------------------------------> number of entry

     00000150:00000000 01:00000019 00000000
        |        |     |     |       |--> number of unrecovered RTO timeouts
        |        |     |     |----------> number of jiffies until timer expires
        |        |     |----------------> timer_active (see below)
        |        |----------------------> receive-queue
        |-------------------------------> transmit-queue

     1000        0 54165785 4 cd1e6040 25 4 27 3 -1
      |          |    |     |    |     |  | |  | |--> slow start size threshold,
      |          |    |     |    |     |  | |  |      or -1 if the threshold
      |          |    |     |    |     |  | |  |      is >= 0xFFFF
      |          |    |     |    |     |  | |  |----> sending congestion window
      |          |    |     |    |     |  | |-------> (ack.quick<<1)|ack.pingpong
      |          |    |     |    |     |  |---------> Predicted tick of soft clock
      |          |    |     |    |     |              (delayed ACK control data)
      |          |    |     |    |     |------------> retransmit timeout
      |          |    |     |    |------------------> location of socket in memory
      |          |    |     |------...