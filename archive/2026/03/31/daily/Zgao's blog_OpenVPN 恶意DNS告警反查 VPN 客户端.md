---
title: OpenVPN 恶意DNS告警反查 VPN 客户端
url: https://zgao.top/openvpn-%e6%81%b6%e6%84%8f-dns-%e5%91%8a%e8%ad%a6%e5%8f%8d%e6%9f%a5-vpn-%e5%ae%a2%e6%88%b7%e7%ab%af/
source: Zgao's blog
date: 2026-03-31
fetch_date: 2026-04-01T04:45:13.428120
---

# OpenVPN 恶意DNS告警反查 VPN 客户端

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# OpenVPN 恶意DNS告警反查 VPN 客户端

* [首页](https://zgao.top)
* [OpenVPN 恶意DNS告警反查 VPN 客户端](https://zgao.top:443/openvpn-%E6%81%B6%E6%84%8F-dns-%E5%91%8A%E8%AD%A6%E5%8F%8D%E6%9F%A5-vpn-%E5%AE%A2%E6%88%B7%E7%AB%AF/)

[3月 31, 2026](https://zgao.top/2026/03/)

### OpenVPN 恶意DNS告警反查 VPN 客户端

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/openvpn-%E6%81%B6%E6%84%8F-dns-%E5%91%8A%E8%AD%A6%E5%8F%8D%E6%9F%A5-vpn-%E5%AE%A2%E6%88%B7%E7%AB%AF/)

```
【MSS高危告警】
--------------------------
【标题】：xxx发现DNS恶意请求
【客户名称】：xxxxxxxx
【云平台】：腾讯云
【客户账号】：xxxxxxxxx
【风险等级】：高危
【攻击IP】：
【告警时间】：2026-03-30 11:41:46
【事件类型】：恶意请求行为
【受影响资产】：10.59.240.14
【详情】：[公网IP：xxx.xx.xxx.x，机器：xxxxx，请求恶意域名：apifox.it.com，进程：，请求次数：1，首次请求时间：2026-03-30 11:41:46，最近请求时间：2026-03-30 11:41:46，Hash：xxxxxxxxx]
```

最近在处理MSS安全告警的时候遇到的问题：部署了 OpenVPN 的服务器上，HIDS 检测到了恶意域名的 DNS 请求，但因为请求是从 VPN 隧道内部发出的，告警里只能看到一个 OpenVPN 服务端自身的IP，没法直接定位到是哪台客户端机器、哪个用户触发的。

文章目录

[ ]

* [案例背景](#%E6%A1%88%E4%BE%8B%E8%83%8C%E6%99%AF "案例背景")
* [思路：把 DNS 查询日志和 VPN 客户端身份关联起来](#%E6%80%9D%E8%B7%AF%EF%BC%9A%E6%8A%8A_DNS_%E6%9F%A5%E8%AF%A2%E6%97%A5%E5%BF%97%E5%92%8C_VPN_%E5%AE%A2%E6%88%B7%E7%AB%AF%E8%BA%AB%E4%BB%BD%E5%85%B3%E8%81%94%E8%B5%B7%E6%9D%A5 "思路：把 DNS 查询日志和 VPN 客户端身份关联起来")
* [用 dnsmasq 记录带来源 IP 的 DNS 日志](#%E7%94%A8_dnsmasq_%E8%AE%B0%E5%BD%95%E5%B8%A6%E6%9D%A5%E6%BA%90_IP_%E7%9A%84_DNS_%E6%97%A5%E5%BF%97 "用 dnsmasq 记录带来源 IP 的 DNS 日志")
* [OpenVPN 服务端的配置调整](#OpenVPN_%E6%9C%8D%E5%8A%A1%E7%AB%AF%E7%9A%84%E9%85%8D%E7%BD%AE%E8%B0%83%E6%95%B4 "OpenVPN 服务端的配置调整")
* [VPN IP 到客户端身份的映射](#VPN_IP_%E5%88%B0%E5%AE%A2%E6%88%B7%E7%AB%AF%E8%BA%AB%E4%BB%BD%E7%9A%84%E6%98%A0%E5%B0%84 "VPN IP 到客户端身份的映射")
* [临时调整 OpenVPN 日志级别](#%E4%B8%B4%E6%97%B6%E8%B0%83%E6%95%B4_OpenVPN_%E6%97%A5%E5%BF%97%E7%BA%A7%E5%88%AB "临时调整 OpenVPN 日志级别")
* [用 iptables 做补充记录](#%E7%94%A8_iptables_%E5%81%9A%E8%A1%A5%E5%85%85%E8%AE%B0%E5%BD%95 "用 iptables 做补充记录")
* [实际应急响应的流程](#%E5%AE%9E%E9%99%85%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94%E7%9A%84%E6%B5%81%E7%A8%8B "实际应急响应的流程")
* [一些额外的想法](#%E4%B8%80%E4%BA%9B%E9%A2%9D%E5%A4%96%E7%9A%84%E6%83%B3%E6%B3%95 "一些额外的想法")

## 案例背景

环境大概是这样的：一台公网服务器跑着 OpenVPN Server，十几个客户端通过 VPN 接入内网。服务端同时承担了 DNS 转发的角色——客户端连上 VPN 之后，DNS 请求会被推送到服务端处理。

最近HIDS 告警了一条 DNS 请求，目标域名命中了威胁情报的黑名单，疑似 C2 通信。但OpenVPN的服务器没有安装别的服务，大概率是VPN客户端触发的恶意请求，但是如何才能定位到是哪个客户端呢？

OpenVPN 默认的日志里其实是有客户端信息的，但如果没有提前做好配置，等到出事了再去翻日志，大概率是对不上的——因为 IP 可能已经被重新分配过了，或者日志里压根没记录 IP 和客户端证书 CN 的对应关系。

## 思路：把 DNS 查询日志和 VPN 客户端身份关联起来

要解决这个问题，核心就是两件事：

1. **记录 DNS 请求的来源 IP**——知道是哪个 VPN 内网 IP 发的
2. **记录 VPN IP 和客户端身份的映射**——知道这个 IP 当时分配给了谁

这两条信息能对上，链路就通了。

## 用 dnsmasq 记录带来源 IP 的 DNS 日志

OpenVPN 服务端如果用 systemd-resolved 或者直接转发 DNS，默认是不会记录查询日志的。这里选择部署 dnsmasq 作为本地 DNS 转发器，原因很简单：它自带查询日志功能，而且 `log-queries=extra` 模式下会把**请求来源 IP 和端口**一起记下来。

安装就不多说了，直接看关键配置，写到 `/etc/dnsmasq.d/vpn-dns.conf`：

```
# 开启 DNS 查询日志，extra 模式记录来源 IP
log-queries=extra

# 日志输出到独立文件，不混在 syslog 里
log-facility=/var/log/openvpn/dns-queries.log

# 上游 DNS
server=8.8.8.8
server=114.114.114.114
```

关键就是 `log-queries=extra` 这一行。如果只写 `log-queries`，日志里只有查询的域名；加上 `extra`，每条记录会带上来源 IP。

配好之后重启 dnsmasq，效果是这样的：

```
Mar 31 11:30:20 dnsmasq[3624777]: 36 10.8.0.6/33606 query[A] www.baidu.com from 10.8.0.6
Mar 31 11:30:21 dnsmasq[3624777]: 40 10.8.0.6/49353 query[A] evil-c2-domain.example.com from 10.8.0.6
```

每条日志都清楚地写着 `from 10.8.0.6`，这就是 VPN 客户端的隧道 IP。

## OpenVPN 服务端的配置调整

光有 DNS 日志还不够，还得让客户端的 DNS 请求确实走到 dnsmasq 上来。这需要在 OpenVPN 的 `server.conf` 里做两个推送：

```
# 推送 DNS 服务器地址（指向 VPN 网关自己）
push "dhcp-option DNS 10.8.0.1"

# 让客户端全部流量走 VPN，包括 DNS
push "redirect-gateway def1 bypass-dhcp"
```

这样客户端连上 VPN 后，DNS 请求就会发到 `10.8.0.1`（也就是服务端 tun0 接口的地址），被 dnsmasq 接住并记录。

**有个坑要注意**：Linux 客户端如果用的是 systemd-resolved，OpenVPN 推送的 `dhcp-option` 不会自动生效。需要在客户端手动执行：

```
resolvectl dns tun0 10.8.0.1
resolvectl domain tun0 "~."
resolvectl default-route tun0 true
```

或者装 `openvpn-systemd-resolved` 这个包让它自动处理。Windows 和 macOS 客户端一般没这个问题。

## VPN IP 到客户端身份的映射

DNS 日志里记的是 VPN IP，但应急响应的时候要回答的是”哪个人/哪台机器”。这就需要 OpenVPN 把 IP 分配记录保存下来。OpenVPN 本身有几个机制可以用：

**status 日志**，在 `server.conf` 里加：

```
status /var/log/openvpn/status.log 10
```

每 10 秒刷新一次，内容长这样：

```
OpenVPN CLIENT LIST
Common Name,Real Address,Bytes Received,Bytes Sent,Connected Since
client1,1.2.3.4:42303,63297,48435,2026-03-31 11:28:33
ROUTING TABLE
Virtual Address,Common Name,Real Address,Last Ref
10.8.0.6,client1,1.2.3.4:42303,2026-03-31 11:30:20
```

这里的 `Virtual Address` 就是 VPN IP，`Common Name` 是客户端证书的 CN，`Real Address` 是客户端的真实公网 IP。但 status 文件是实时覆盖的，只反映当前连接状态，历史记录查不到。

所以还需要 **client-connect/client-disconnect 脚本**来持久化记录。在 `server.conf` 里配置：

```
script-security 2
client-connect /etc/openvpn/scripts/client-connect.sh
client-disconnect /etc/openvpn/scripts/client-disconnect.sh
```

connect 脚本：

```
#!/bin/bash
echo "[$(date '+%Y-%m-%d %H:%M:%S')] CONNECTED: CN=$common_name, VPN_IP=$ifconfig_pool_remote_ip, REAL_IP=$trusted_ip:$trusted_port" \
  >> /var/log/openvpn/client-events.log
```

disconnect 脚本：

```
#!/bin/bash
echo "[$(date '+%Y-%m-%d %H:%M:%S')] DISCONNECTED: CN=$common_name, VPN_IP=$ifconfig_pool_remote_ip, REAL_IP=$trusted_ip:$trusted_port, DURATION=${time_duration}s" \
  >> /var/log/openvpn/client-events.log
```

这样就有了一份持久的连接历史记录，就算客户端断开了也能查到当时的 IP 映射。

**这里有个坑**：OpenVPN 如果配了 `user nobody` 降权运行，脚本执行时也是 nobody 用户，如果日志文件权限不对会导致脚本执行失败。更坑的是，client-connect 脚本如果返回非零退出码，OpenVPN 会直接拒绝客户端连接，报 `AUTH_FAILED`。排查的时候一脸懵，看证书配置明明没问题，结果是个文件权限的事：

```
chmod 777 /var/log/openvpn/
touch /var/log/openvpn/client-events.log
chmod 666 /var/log/openvpn/client-events.log
```

生产环境权限可以收紧一些，给 nobody 用户写权限就行。

## 临时调整 OpenVPN 日志级别

平时 OpenVPN 日志 verb 级别开到 3 或 4 就够了，但如果要排查安全问题，建议临时调到 5 或 6：

```
# verb 5: 每个包的 R/W 信息
# verb 6: 调试级别，包含更多 TLS 和路由细节
verb 6
log-append /var/log/openvpn/server.log
```

verb 6 的日志量会很大，能看到每个数据包的读写，但在分析异常流量的时候确实有用。平时别开这么高，磁盘扛不住。

## 用 iptables 做补充记录

除了应用层的 dnsmasq 日志，我还在 iptables 上加了一层记录，算是个兜底（可以作为补充）：

```
# 记录所有从 VPN 子网发出的 DNS 请求（网络层）
iptables -A FORWARD -s 10.8.0.0/24 -p udp --dport 53 -j LOG --log-prefix "[VPN-DNS] " --log-level 4
iptables -A INPUT -s 10.8.0.0/24 -p udp --dport 53 -j LOG --log-prefix "[VPN-DNS-LOCAL] " --log-level 4
```

这个日志会写到 `kern.log` 或者 `dmesg` 里，内容只有 IP 层信息（源IP、目的IP、端口），看不到查询的域名。但好处是它不依赖 dnsmasq，即使 dnsmasq 挂了或者客户端绕过了推送的 DNS 直接请求外部 DNS（比如直连 8.8.8.8），iptables 也能抓到。

## 实际应急响应的流程

把上面这些都配好之后，再碰到恶意 DNS 告警，排查流程就很清晰了：

**第一步**，从告警拿到可疑域名，去 dnsmasq 的日志里搜：

```
grep "evil-domain" /var/log/openvpn/dns-queries.log
```

输出：

```
10.8.0.6/49353 query[A] evil-domain.example.com from 10.8.0.6
```

拿到来源 VPN IP：`10.8.0.6`

![](https://zgao.top/wp-content/uploads/2026/03/image-8-1024x530.png)

**第二步**，查这个 IP 当时对应的客户端。先看 status 文件（如果客户端还在线）：

```
grep "10.8.0.6" /var/log/openvpn/status.log
```

如果客户端已经断了，去 client-events.log 里查历史：

```
grep "10.8.0.6" /var/log/openvpn/client-events.log
```

输出：

```
[2026-03-31 11:28:33] CONNECTED: CN=client1, VPN_IP=10.8.0.6, REAL_IP=1.2.3.4:42303
```

到这里就能确定：**证书 CN 为 `client1` 的客户端，从公网 IP `1.2.3.4` 接入 VPN 后，在 `10.8.0.6` 这个地址上请求了恶意域名**。

![](https://zgao.top/wp-content/uploads/2026/03/image-9-1024x518.png)

**第三步**，根据 CN 和公网 IP 去资产管理里查对应的人和机器。

但现实中很多时候命名就是 `client1`、`client2` 这种，签发的时候也没人记。那就只能靠几种方式去追溯了：

```
root@VM-24-5-ubuntu:/var/log/openvpn# cat /etc/openvpn/easy-rsa/pki/index.txt
V       280703031655Z           86C152F5D82272A8E78539585FF92175        unknown /CN=server
V       280703031655Z           3D9F98F11618CF18E88F972CD9F127D7        unknown /CN=client1
```

1. 查证书分发记录。如果有运维或者工单系统记录了”某天把 client1.ovpn 发给了张三”，那就对上了
2. 看公网 IP。client-events.log 里记录了客户端的真实公网 IP `1.2.3.4`，查一下这个 IP 归属哪个出口，结合办公网络的 NAT 记录也能缩小范围
3. 如果实在对不上，还有一招——证书没吊销的话，客户端机器上肯定还留着 `.ovpn` 配置文件或者证书文件。找到嫌疑机器后在上面搜一下 `/CN=client1` 对应的证书指纹就能确认

所以说到底，**最省事的做法还是在签发证书的时候就把 CN 命名规范定好**。用 `姓名-设备` 的格式（比如 `zhangsan-mac...