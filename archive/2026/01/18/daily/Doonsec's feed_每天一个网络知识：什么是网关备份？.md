---
title: 每天一个网络知识：什么是网关备份？
url: https://mp.weixin.qq.com/s/UXTwXhxKJHFiPBwfAf9UTQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:42:23.181372
---

# 每天一个网络知识：什么是网关备份？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/p8No8ScJKT9jozbTKpvicj91sJtHEW2UmSHwAp7ubbSNvP2WFZR1icC4DicC5C0jwOj2hib8uoia62xwY0bgc0cSxGQ/0?wx_fmt=jpeg)

# 每天一个网络知识：什么是网关备份？

原创

圈圈
圈圈

网络技术干货圈

![]()

在小说阅读器中沉浸阅读

大家好，我是圈圈，一个喜欢结交朋友的老网工！

每天一个网络知识，今天我们要聊聊：网关备份

- start -

在网络通信中，终端设备（如电脑、手机）要访问外部网络（比如互联网），必须通过一个“出口”——这个出口就是**默认网关**。通常，这个网关是一台路由器或三层交换机的接口IP地址。然而，如果这台网关设备发生故障，整个局域网内的设备将无法与外界通信，造成“断网”。为了解决单点故障问题，引入了**网关备份技术**。

![](https://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT9jozbTKpvicj91sJtHEW2UmMM0GQW45ibLp9E0s09AXDgTUZaUm1DpmraaDRBbjjlniaTCYOeunK7Xg/640?wx_fmt=png&from=appmsg)

## 什么是网关备份？

网关备份，是指在局域网中部署**两台或多台网关设备**，并通过特定协议实现**主备切换或负载分担**，确保当主网关失效时，备用网关能迅速接管流量，保障网络连通性不中断。这种机制也被称为**第一跳冗余协议（First Hop Redundancy Protocol, FHRP）**。

常见的网关备份协议包括：

* **HSRP（Hot Standby Router Protocol）**：思科私有协议
* **VRRP（Virtual Router Redundancy Protocol）**：IETF 标准（RFC 5798）
* **GLBP（Gateway Load Balancing Protocol）**：思科私有，支持负载均衡

其中，**VRRP 因其开放性和跨厂商兼容性，在实际网络中应用最广泛**。

## 网关备份如何工作？

以 VRRP 为例说明其原理：

1. **虚拟IP地址**：多台物理路由器组成一个“VRRP组”，共同使用一个**虚拟IP地址**作为局域网内主机的默认网关。例如，真实网关可能是 192.168.1.2 和 192.168.1.3，但它们对外提供一个虚拟IP：192.168.1.1。
2. **主备角色分配**：组内设备根据优先级选举出一台**Master（主网关）**，其余为 **Backup（备份网关）**。只有 Master 负责转发数据包，并定期发送 VRRP 通告报文（Advertisement）。
3. **故障检测与切换**：Backup 设备会监听 Master 的通告。如果在设定时间内（通常几秒）未收到通告，就认为 Master 故障，此时优先级最高的 Backup 会立即升级为新的 Master，并开始响应 ARP 请求、转发流量。

整个切换过程对终端用户**完全透明**——你的电脑始终把 192.168.1.1 当作网关，根本不知道背后是哪台物理设备在工作。

## 为什么需要网关备份？

想象一下学校的信息中心只有一台核心路由器作为网关。某天该设备电源故障，全校师生瞬间无法上网、无法访问教务系统、无法提交作业——这就是典型的**单点故障**。而通过网关备份：

* **高可用性（High Availability）**：即使一台网关宕机，业务几乎不受影响（切换时间通常 < 3 秒）。
* **无缝体验**：用户无需修改任何配置，网络连接自动恢复。
* **运维容错**：管理员可在非高峰时段对主网关进行维护或升级，由备份设备临时接管。

## 实际应用场景

1. **校园网出口**：核心交换机双机热备，保障教学与办公网络稳定。
2. **企业数据中心**：服务器网关采用 VRRP，避免因单台三层交换机故障导致服务中断。
3. **云平台虚拟网络**：在 OpenStack 或 Kubernetes 中，虚拟路由器常通过 VRRP 实现高可用。
4. **家庭/小型办公室**：部分高端家用路由器也支持双WAN口+网关冗余，提升宽带可靠性。

## 配置示例（简化）

以华为交换机配置 VRRP 为例：

```
# 主网关配置interface Vlanif 10 ip address 192.168.1.2 255.255.255.0 vrrp vrid 1 virtual-ip 192.168.1.1 vrrp vrid 1 priority 120  # 优先级更高，默认100
# 备份网关配置interface Vlanif 10 ip address 192.168.1.3 255.255.255.0 vrrp vrid 1 virtual-ip 192.168.1.1 # 优先级保持默认100
```

终端设备只需将默认网关设为 `192.168.1.1`，即可享受高可用服务。

- end -

如果文章对你有帮助，感谢给个 点赞、分享、推荐、关注！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT8cAnqjp2AZ90pLWoO7Ysr6JzXPMqP8qibB5ggPz4amnZicChP8vQExwbEJ1O0BtqiaYuYHicm74DQnbA/0?wx_fmt=png)

网络技术干货圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT8cAnqjp2AZ90pLWoO7Ysr6JzXPMqP8qibB5ggPz4amnZicChP8vQExwbEJ1O0BtqiaYuYHicm74DQnbA/0?wx_fmt=png)

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