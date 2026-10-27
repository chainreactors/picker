---
title: Wireshark TS | 确认时间戳的差异
url: https://mp.weixin.qq.com/s/snpvrUej3futsa2QkIMGfA
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:02:21.129281
---

# Wireshark TS | 确认时间戳的差异

# Wireshark TS | 确认时间戳的差异

原创

7ACE
7ACE

Echo Reply

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**现象一致，根因未必相同**

# 前言

在前面两篇文章中，我们分别从两个角度分析了 ACK 3001 时刻发送行为的差异：第一篇讨论了 `write()` 写入数据量不同导致最后一个 skb 大小不同（2000B vs 1000B），进而 `tso_segs` 不同，走入 `tcp_tso_should_defer` 或 `tcp_nagle_test` 两条不同的代码路径；第二篇讨论了接收窗口不同（10000 vs 12000）导致 `send_win` 不同，进而 `tcp_tso_should_defer` 内部判断分叉。

本文继续探讨一个更微妙的现象：同样 `write(10000)`、同样接收窗口 `win 10000`，仅仅把 ACK 3001 的到达间隔从 50ms 改为 20ms，发送行为又发生了变化。这次的差异不再是 skb 大小或窗口，而是 `tcp_tso_should_defer` 内部基于重传队列队头 skb 时间戳的一道精细判断——`delta` 与 `srtt/2` 的比较。

# 问题现象

仍然是两个 pkt 测试脚本（其中脚本 1 与第一篇文章一致），如下所示。两者的测试路由均指定了 reno 拥塞控制算法，并将初始 CWND 改为 3，同时关闭了 TSO/GSO。脚本模拟 TCP 三次握手完成后，客户端发送数据并正常 ACK，服务器随后写入数据，之后服务器收到客户端连续的几个 ACK 确认。

```
# cat tcp_reno_001.pkt
`ip route change 192.0.2.0/24 dev tun0 congctl reno initcwnd 3
 ethtool -K tun0 tso off
 ethtool -K tun0 gso off`

0  socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
+0 setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
+0 bind(3, ..., ...) = 0
+0 listen(3, 1) = 0

+0 < S 0:0(0) win 10000 <mss 1000,nop,nop,sackOK>
+0 > S. 0:0(0) ack 1 <...>
+0.05 < . 1:1(0) ack 1 win 10000
+0 accept(3, ..., ...) = 4

+0.05 < P. 1:101(100) ack 1 win 10000
+0 > . 1:1(0) ack 101

+0.05 write(4,...,10000) = 10000

+0.05 < . 101:101(0) ack 1001 win 10000
+0 %{print (tcpi_snd_cwnd)}%

+0.005 < . 101:101(0) ack 2001 win 10000
+0 %{print (tcpi_snd_cwnd)}%

+0.05 < . 101:101(0) ack 3001 win 10000
+0 %{print (tcpi_snd_cwnd)}%

+0.03 < . 101:101(0) ack 4001 win 10000
+0 %{print (tcpi_snd_cwnd)}%

+0.005 < . 101:101(0) ack 5001 win 10000
+0 %{print (tcpi_snd_cwnd)}%
#
```

```
# cat tcp_reno_004.pkt
`ip route change 192.0.2.0/24 dev tun0 congctl reno initcwnd 3
 ethtool -K tun0 tso off
 ethtool -K tun0 gso off`

0  socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
+0 setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
+0 bind(3, ..., ...) = 0
+0 listen(3, 1) = 0

+0 < S 0:0(0) win 10000 <mss 1000,nop,nop,sackOK>
+0 > S. 0:0(0) ack 1 <...>
+0.05 < . 1:1(0) ack 1 win 10000
+0 accept(3, ..., ...) = 4

+0.05 < P. 1:101(100) ack 1 win 10000
+0 > . 1:1(0) ack 101

+0.05 write(4,...,10000) = 10000

+0.05 < . 101:101(0) ack 1001 win 10000
+0 %{print (tcpi_snd_cwnd)}%

+0.005 < . 101:101(0) ack 2001 win 10000
+0 %{print (tcpi_snd_cwnd)}%

+0.02 < . 101:101(0) ack 3001 win 10000
+0 %{print (tcpi_snd_cwnd)}%

+0.03 < . 101:101(0) ack 4001 win 10000
+0 %{print (tcpi_snd_cwnd)}%

+0.005 < . 101:101(0) ack 5001 win 10000
+0 %{print (tcpi_snd_cwnd)}%
#
```

总体来看，两个 pkt 脚本写入的数据量以及客户端接收窗口均相同，唯一的区别是 ACK Num 3001 确认到达的时间戳不同：一个是间隔 50ms，一个是间隔 20ms——后者快了 30ms。

同样运行 tcpdump 捕获数据包对比看看。

```
# packetdrill tcp_reno_001.pkt
4
5
6
7
8
#

# tcpdump -i any -nn port 8080
tcpdump: data link type LINUX_SLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
10:14:43.103586 tun0  In  IP 192.0.2.1.52445 > 192.168.4.128.8080: Flags [S], seq 0, win 10000, options [mss 1000,nop,nop,sackOK], length 0
10:14:43.103646 tun0  Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [S.], seq 4103320984, ack 1, win 64240, options [mss 1460,nop,nop,sackOK], length 0
10:14:43.153896 tun0  In  IP 192.0.2.1.52445 > 192.168.4.128.8080: Flags [.], ack 1, win 10000, length 0
10:14:43.203986 tun0  In  IP 192.0.2.1.52445 > 192.168.4.128.8080: Flags [P.], seq 1:101, ack 1, win 10000, length 100: HTTP
10:14:43.204135 tun0  Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [.], ack 101, win 64140, length 0
10:14:43.254368 tun0  Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [.], seq 1:1001, ack 101, win 64140, length 1000: HTTP
10:14:43.254420 tun0  Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [.], seq 1001:2001, ack 101, win 64140, length 1000: HTTP
10:14:43.254445 tun0  Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [.], seq 2001:3001, ack 101, win 64140, length 1000: HTTP
10:14:43.304644 tun0  In  IP 192.0.2.1.52445 > 192.168.4.128.8080: Flags [.], ack 1001, win 10000, length 0
10:14:43.304870 tun0  Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [.], seq 3001:4001, ack 101, win 64140, length 1000: HTTP
10:14:43.304873 tun0  Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [P.], seq 4001:5001, ack 101, win 64140, length 1000: HTTP
10:14:43.310247 tun0  In  IP 192.0.2.1.52445 > 192.168.4.128.8080: Flags [.], ack 2001, win 10000, length 0
10:14:43.310439 tun0  Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [.], seq 5001:6001, ack 101, win 64140, length 1000: HTTP
10:14:43.310442 tun0  Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [P.], seq 6001:7001, ack 101, win 64140, length 1000: HTTP
10:14:43.361452 tun0  In  IP 192.0.2.1.52445 > 192.168.4.128.8080: Flags [.], ack 3001, win 10000, length 0
10:14:43.361923 tun0  Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [P.], seq 7001:8001, ack 101, win 64140, length 1000: HTTP
10:14:43.392152 ?     In  IP 192.0.2.1.52445 > 192.168.4.128.8080: Flags [.], ack 4001, win 10000, length 0
10:14:43.392658 ?     Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [.], seq 8001:9001, ack 101, win 64140, length 1000: HTTP
10:14:43.392663 ?     Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [P.], seq 9001:10001, ack 101, win 64140, length 1000: HTTP
10:14:43.398015 ?     In  IP 192.0.2.1.52445 > 192.168.4.128.8080: Flags [.], ack 5001, win 10000, length 0
10:14:43.427999 ?     Out IP 192.168.4.128.8080 > 192.0.2.1.52445: Flags [R.], seq 10001, ack 101, win 64140, length 0
10:14:43.428028 ?     In  IP 192.0.2.1.52445 > 192.168.4.128.8080: Flags [R.], seq 101, ack 5001, win 10000, length 0
#
```

```
# packetdrill tcp_reno_004.pkt
4
5
6
7
8
#

# tcpdump -i any -nn port 8080
tcpdump: data link type LINUX_SLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
17:45:29.614962 tun0  In  IP 192.0.2.1.58879 > 192.168.162.173.8080: Flags [S], seq 0, win 10000, options [mss 1000,nop,nop,sackOK], length 0
17:45:29.615061 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags [S.], seq 387836039, ack 1, win 64240, options [mss 1460,nop,nop,sackOK], length 0
17:45:29.665891 tun0  In  IP 192.0.2.1.58879 > 192.168.162.173.8080: Flags [.], ack 1, win 10000, length 0
17:45:29.716012 tun0  In  IP 192.0.2.1.58879 > 192.168.162.173.8080: Flags [P.], seq 1:101, ack 1, win 10000, length 100: HTTP
17:45:29.716086 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags [.], ack 101, win 64140, length 0
17:45:29.766543 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags [.], seq 1:1001, ack 101, win 64140, length 1000: HTTP
17:45:29.766650 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags [.], seq 1001:2001, ack 101, win 64140, length 1000: HTTP
17:45:29.766694 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags [.], seq 2001:3001, ack 101, win 64140, length 1000: HTTP
17:45:29.817807 tun0  In  IP 192.0.2.1.58879 > 192.168.162.173.8080: Flags [.], ack 1001, win 10000, length 0
17:45:29.817943 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags [.], seq 3001:4001, ack 101, win 64140, length 1000: HTTP
17:45:29.817945 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags [P.], seq 4001:5001, ack 101, win 64140, length 1000: HTTP
17:45:29.823018 tun0  In  IP 192.0.2.1.58879 > 192.168.162.173.8080: Flags [.], ack 2001, win 10000, length 0
17:45:29.823120 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags [.], seq 5001:6001, ack 101, win 64140, length 1000: HTTP
17:45:29.823123 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags [P.], seq 6001:7001, ack 101, win 64140, length 1000: HTTP
17:45:29.843156 tun0  In  IP 192.0.2.1.58879 > 192.168.162.173.8080: Flags [.], ack 3001, win 10000, length 0
17:45:29.843245 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags [P.], seq 7001:8001, ack 101, win 64140, length 1000: HTTP
17:45:29.843298 tun0  Out IP 192.168.162.173.8080 > 192.0.2.1.58879: Flags...