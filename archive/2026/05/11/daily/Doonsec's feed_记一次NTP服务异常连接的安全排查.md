---
title: 记一次NTP服务异常连接的安全排查
url: https://mp.weixin.qq.com/s/6jEcUC8HrHF_YgGbXKzoUA
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:33:17.890553
---

# 记一次NTP服务异常连接的安全排查

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FT3A8r9icDymxdklHVKsvceAYNQHZd2aSCH2bziaFcVYzZHiaO61eDNyeENkKciafx3fMkL4xBz4Ijs7thNxwTTRibNDTvhmXJyyZyD1JMsiayMAg/0?wx_fmt=jpeg)

# 记一次NTP服务异常连接的安全排查

原创

凉城
凉城

ListSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 记一次NTP服务异常连接的安全排查

## 发现告警

安全设备告警发现异常NTP连接（ip：119.28.206.193），大量NTP协议连接，确认和NTP有关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDyn2yqk1DbTl4ic9OLBb72ticW09paMI1HD3DtfC8cco729hVX13yGKAXiaC11JTchf2aJnJRkBicv5CiatYo5YgoLGukQqkZzuCpiapA/640?wx_fmt=png&from=appmsg)

## 排查过程

查看系统使用的是什么时间同步服务，先确认服务名：

```
systemctl status ntpd chronyd ntpsec systemd-timesyncd --no-pager
```

从输出中可以看到时间同步进程的路径（/usr/sbin/chronyd）以及曾经通信过的 NTP 服务器 IP。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDymgUXIiaEsw1KdPgVYWPb12B5lf8BiaK2vln2KJ09gc9YFrEWHwbe3gXubb9ibPQXGmspDLJpovve9kCvInnYh6RGk4s6uicnmXb14/640?wx_fmt=png&from=appmsg)

查看chronyd服务近期通信的日志，从输出中可看到曾经通信过的 NTP 服务器 IP。

```
journalctl -u chronyd --since "2026-05-08" --no-pager

#输出如下：
-- Logs begin at Sat 2026-02-07 01:21:01 CST, end at Mon 2026-05-11 10:17:07 CST. --
May 10 13:13:14 localhost.localdomain chronyd[940]: Source 119.28.206.193 replaced with 116.203.151.74
May 10 14:56:19 localhost.localdomain chronyd[940]: Source 116.203.151.74 replaced with 193.182.111.142
```

进一步查看时间同步的配置文件，定位具体的NTP池域名

![](https://mmbiz.qpic.cn/mmbiz_png/FT3A8r9icDynlGqMtBMc7p45qHkXO0khHRGbFGFwXibrwqhc0ic5HziaicYd9SRqOIEmT88eTicl8eIk3G9VXEawF5tdSSQAfvC6Aj82otySduEfk/640?wx_fmt=png&from=appmsg)

可以知道有四个域名

```
0.centos.pool.ntp.org
1.centos.pool.ntp.org
2.centos.pool.ntp.org
3.centos.pool.ntp.org
```

这些域名会解析成不同的公网 NTP 节点，所以告警中的 119.28.206.193、5.79.108.34、116.203.151.74、193.182.111.142 都可能是池里的上游时间服务器。

查看当前NTP同步源

```
chronyc sources -v
```

```
# 查看 chronyd 当前正在使用哪些 NTP 时间源，以及这些时间源状态是否正常
# chronyc sources -v

210 Number of sources = 4

  .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
 / .- Source state '*' = current synced, '+' = combined , '-' = not combined,
| /   '?' = unreachable, 'x' = time may be in error, '~' = time too variable.
||                                                 .- xxxx [ yyyy ] +/- zzzz
||      Reachability register (octal) -.           |  xxxx = adjusted offset,
||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
||                                \     |          |  zzzz = estimated error.
||                                 |    |           \
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
^+ 14.103.157.44                 3  10   377   23m   +218us[ +222us] +/-   47ms
^- time.cloudflare.com           3  10   377   892  +2626us[+2630us] +/-   95ms
^* 139.199.215.251               2  10   377   789    +88us[  +92us] +/-   32ms
^- 193.182.111.142               2  10   377   22m    -12ms[  -12ms] +/-  111ms
```

这些字段的含义：

```
第一列是模式，^ 表示 server，= 表示 peer，# 表示本地时钟。
第二列是状态，* 表示当前正在使用的同步源，+ 表示可参与组合的候选源，- 表示可达但当前未采用，? 表示不可达，x 表示时间可能有错误，~ 表示时间波动太大。
```

所有说当前服务器的NTP同步源是139.199.215.251这个ip地址。`^* 139.199.215.251 2  10 377 789  +88us[+92us] +/- 32ms`：表示当前系统正在使用 139.199.215.251 作为 NTP 同步源，它是 Stratum 2，最近 8 次轮询都成功，大约 789 秒前收到响应，本机时间与它的偏差很小，状态正常。

微步查下这个ip：139.199.215.251

![](https://mmbiz.qpic.cn/mmbiz_png/FT3A8r9icDymJgicaWyIiaNjEtRvaDxCMiae1MyR5NnHXVDzwD1DlCSeoeeMlcpx4j6I05vvOXqaoXqMJNIWW6WYmyOffub52nJbTibqAzDgQvLU/640?wx_fmt=png&from=appmsg)

https://www.ntppool.org/scores/139.199.215.251，这个ip属于腾讯的时间同步源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FT3A8r9icDykuibicXUOoNrGtAibsCPiaaApE6WNdFl7kMYG8XqFZ2gEjGRHQHqZ1oLEQ6AnMiaw3te3GSPsYIRQMINO1hU8VaSYpzq5GhjzCZ3OU/640?wx_fmt=png&from=appmsg)

之前告警的ip也是时间同步服务器

![](https://mmbiz.qpic.cn/mmbiz_png/FT3A8r9icDylmdribcfkNwhUZzjc9ukj1OICIyf4rQ0IZ7w0jzE165SHpn1zL11ia8YxibBJ6hnibrMalgE9hC4jib8h2QeFjlWSVmicDYEZITXROI/640?wx_fmt=png&from=appmsg)

## 结论

* • **告警原因**：正常的时间同步行为，来源为腾讯云 NTP 源
* • **当前同步源**：`139.199.215.251`
* • **涉及 NTP 池域名**：`0~3.centos.pool.ntp.org`
* • **处置建议**：

+ ◦ 内网专门架设NTP服务器，使用内网NTP同步服务器进行时间同步。
+ ◦ 将上述 IP 及域名加入安全设备白名单，或忽略此告警。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

ListSec

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过