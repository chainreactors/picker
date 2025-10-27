---
title: WireGuard:兄弟,常回家看看
url: https://mp.weixin.qq.com/s?__biz=MzUyMDgzMDMyMg==&mid=2247484471&idx=1&sn=bc0b0871744ea13073705d0517ba576e&chksm=f9e5282ace92a13c42e0c22ef7b502c99966a42b53f06278150d4150c278e8dacf410ee9a5f4&scene=58&subscene=0#rd
source: RedTeaming
date: 2024-10-10
fetch_date: 2025-10-06T18:53:45.820733
---

# WireGuard:兄弟,常回家看看

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D8s0oRfyswmpd7Nicic1T2J8F2gHxHHDoHduxTxHYAyYpzduZicZPpHTf8OVT5MlysibXWZqg4ick2URmjRS5ntnSfw/0?wx_fmt=jpeg)

# WireGuard:兄弟,常回家看看

原创

RedTeamWing

RedTeaming

## 0x01 前言

最近有个需求,出门在外的时候想会连家里局域网的一些服务，之前一直使用的是cloudflare的隧道功能，但是还是不够方便(但是cf隧道的安全性还是很强的，有零信任机制)。

调研了一下，最后决定使用WireGuard。中间遇到的问题主要是流量到不了家里。转发规则设置的问题。参考的最好的一篇文章-https://gobomb.github.io/post/wireguard-notes/(其他的都是鬼扯蛋)

## 0x02 准备工作

配置信息

* 个人笔记本(Mac)-192.168.2.2(wg)
* VPS-192.168.2.1(wg)
* 家里任意一台局域网主机(Home Linux)-192.168.1.1/24 192.168.2.3(wg)

## 0x03 安装&配置WG

### VPS

```
1. wg genkey > private
2. ip link add dev wg0 type wireguard # 添加 wireguard 网卡 wg0
3. ip addr add 192.168.2.1/24 dev wg0
4. wg set wg0 private-key ./private #  设置私钥
5. ip link set wg0 up #启动网卡

7. wg # 查看公钥
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D8s0oRfyswmpd7Nicic1T2J8F2gHxHHDoHvmgiaZ79q57QRF2iaJGMKWk5yO514WrBpGnrypicWuicxW7AnvkYrY41Ow/640?wx_fmt=png&from=appmsg)

### Home Linux

先配置wg

```
1. wg genkey > private
2. ip link add wg0 type wireguard
3. ip addr add 192.168.2.2/24 dev wg0
4. wg set wg0 private-key ./private
5. ip link set wg0 up

7. 连接VPS
8. wg set wg0 peer OM5NlntS3l0hCBrrlvFGnVoThIniVICuulbszIQ0Lhs= allowed-ips 192.168.2.0/24 endpoint  ip:port persistent-keepalive 15

10. 查看home linux公钥
11. wg
```

服务端添加home linux

```
1. wg set wg0 peer homelinux公钥 allowed-ips 192.168.2.2/32,192.168.1.0/24 persistent-keepalive 15
```

## Mac

```
1. brew install wireguard-tools
2. sudo mkdir /etc/wireguard
3. wg genkey | tee privatekey | wg pubkey > publickey

5. touch wg0.conf

7. [Interface]
8. Address = 192.168.2.3/32
9. PrivateKey = mac private key

11. [Peer]
12. PublicKey = vps public key
13. Endpoint = vpsip:port
14. AllowedIPs = 192.168.2.0/24,192.168.1.0/24
15. PersistentKeepalive = 15
```

启动wg

```
1. sudo wg-quick up wg0
```

VPS添加Mac wg

```
1. wg set wg0 peer  macwg公钥 allowed-ips 192.168.2.2/32 persistent-keepalive 15
```

分别三台机器互相ping，成功以后进行下一步。

## 设置转发规则

需要在各个机器上设置路由转发规则，否则流量到不了家里。

Mac

```
1. 让目标网段的流量走指定网关
2. sudo route -n add 192.168.31.0/24 192.168.2.1
```

VPS

```
1. 开启流量转发
2. net.ipv4.ip_forward = 1
3. sysctl -p
4. iptables -t filter -A FORWARD -i wg0 -j ACCEPT # 方形
5. iptables -t filter -A FORWARD -o wg0 -j ACCEPT
6. ip r add 192.168.1.0/24 via 192.168.2.1 dev wg0
```

Home Linux

```
1. net.ipv4.ip_forward = 1
2. sysctl -p
3. iptables  -t filter  -A FORWARD -i wg0 -o homelinux网卡 -j ACCEPT
4. iptables -t nat -A POSTROUTING -s 192.168.2.0/24 -o homelinux网卡 -j MASQUERADE
5. iptables  -t filter  -A FORWARD  -i homelinux网卡 -o wg0 -j ACCEPT
```

至此，已成。

## Note

如果中间遇到网络问题，用以下命令调试即可。

```
1. tcpdump -i wg0 -nn icmp
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/D8s0oRfyswn6RH4bWic2xc6qtDPjmey9kwyvRiagHA1lzlAM9uf9aic4K6NJH0JeoXQZ1Hpx7pWJaQibUl4ZulgIEg/0?wx_fmt=png)

RedTeaming

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/D8s0oRfyswn6RH4bWic2xc6qtDPjmey9kwyvRiagHA1lzlAM9uf9aic4K6NJH0JeoXQZ1Hpx7pWJaQibUl4ZulgIEg/0?wx_fmt=png)

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