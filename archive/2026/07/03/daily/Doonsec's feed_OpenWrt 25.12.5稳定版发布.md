---
title: OpenWrt 25.12.5稳定版发布
url: https://mp.weixin.qq.com/s/7raOjLzbfVsTCagufdcMWA
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:38:34.500901
---

# OpenWrt 25.12.5稳定版发布

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/raicmpgShpRlfyvAtrIIaV3G1ExRCibaIicrHayemQKsjbPs93NHSsicCcvLIrLcgobyXxWUWja43VLR0TTPD2oIVs9jWnnSa6JbACfAbLgWnpc/0?wx_fmt=jpeg)

# OpenWrt 25.12.5稳定版发布

原创

TT
TT

OpenWrt

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前两天OpenWrt官方发布了25.12的第5个稳定版本，集中修补安全漏洞，同时改善 DHCP、IPv6、Wi-Fi 和部分设备的稳定性。这里顺便给OpenWrt爱好者一些建议，尽量用OpenWrt官方最新稳定分支的版本，不要停留在老版本，否则直接用厂家官方的固件即可。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRm3AeJCMPgbuBgE8HQghNXRA0siciaGzWLlic1dREBnf3g2iamyesQyHHuO88nNwtsHBdlGPwlnWIpHibYblpTY2iaWZxzPo0VlBbQtA/640?wx_fmt=png&from=appmsg)

# OpenWrt 25.12.5 发布要点

### 1. 修复多项高风险安全漏洞

本次更新首先解决了`odhcpd` 中的一批 DHCPv6 安全问题，包括缓冲区溢出、释放后使用、内存信息泄露和拒绝服务等。其中`CVE-2026-53921` 被评为严重级别，攻击者在同一网络附近发送特制的 DHCPv6 请求，就可能触发漏洞。

另外还修复了一个 DHCPv6 主机名注入问题。未经认证的客户端原本可能把恶意内容写入租约文件，最终在 LuCI 的 DHCPv6 租约页面触发存储型 XSS。

其他比较重要的安全修复还有：

* `uhttpd` 修复 3 个 HTTP 请求问题；
* `cgi-io` 修复路径遍历漏洞，避免受限账号读取`/etc/shadow` 等敏感文件；
* LuCI 多个组件修复提权、命令注入和存储型 XSS，其中涉及 Tailscale、Advanced Reboot、Adblock Fast、Samba4、Travelmate、UPnP、banIP 等应用；
* Linux 内核、OpenSSL、musl libc 和 Dropbear 同步合入多项安全修复。

### 2. Wi-Fi 稳定性继续改善

* 修复纯 6 GHz 无线设备可能出现的空指针崩溃；
* 修复 EAP（802.1X）客户端模式的配置生成问题；
* 修复已禁用虚拟无线接口的状态跟踪；
* 修正 DFS 雷达检测通知位置不对的问题；
* 无线法规数据库更新到`2026.05.30`。

这些改动不算新功能，但对 6 GHz、企业认证和 DFS 信道用户会更实用。

### 3. DHCP、IPv6 和基础服务更稳

`odhcpd` 与`odhcp6c` 除了安全修复，还处理了不少 DHCPv4、DHCPv6 和 IPv6 前缀委派问题，DHCPv6 IAID 的处理也更稳定。系统对异常 DHCP 客户端标识的容错能力有所提升。

另外，`ubus`、`rpcd`、`uhttpd`、`umdns`、`uclient` 和`fstools` 都加入了稳定性或安全加固修复。支持的设备还可以使用新的`network` LED 触发器，根据 LAN、WAN 或 WLAN 的连接和流量状态控制指示灯。

### 4. 核心组件升级

| 组件 | 旧版本 | 新版本 |
| --- | --- | --- |
| Linux 内核 | 6.12.87 | 6.12.94 |
| OpenSSL | 3.5.6 | 3.5.7 |
| dnsmasq | 2.91 | 2.93 |
| wireless-regdb | 2026.03.18 | 2026.05.30 |
| ca-certificates | 20260223 | 20260601 |
| util-linux | 2.41.3 | 2.41.5 |

### 5. 新增设备支持

25.12.5 新增支持多款设备，比较有代表性的包括：

* Linksys MR9000；
* GL.iNET GL-MT3600BE；
* JioRouter AX6000（JIDU6101）；
* TP-Link F65 v1；
* Zyxel NAS326；
* Cudy WR300 v1；
* I-O DATA WN-AX2033GR2。

同时也为 Qihoo 360T7、Creatlentem CLT-R30B1 等已有设备增加了新的固件布局，并修复部分 MediaTek、MikroTik、Ramips 等设备的启动、网口、闪存和稳定性问题。

## 升级前需要注意

从 OpenWrt 24.10 升级到 25.12，大多数设备可以使用`sysupgrade` 并保留配置；25.12 系列内部升级也支持 Attended Sysupgrade，可保留已安装的软件包。不过升级前仍然建议先备份配置，并确认设备页面上的具体说明。

下面几类设备需要格外留意：

* **OpenWrt 23.05 或更早版本**：官方不支持直接通过`sysupgrade` 升级到 25.12；
* **Bananapi BPI-R4**：网口名称有调整，升级时不能保留旧配置；
* **TP-Link RE355 v1、RE450 v1/v2**：分区布局发生变化，从 25.12.0 或更早版本升级需要使用`sysupgrade -F`，同时固件大小不能超过 5.875 MB；
* **Meraki MX60**：不能直接升级，需要先按设备 Wiki 修改`meraki_loadaddr`；
* **Sitecom WLR-7100**：目标平台已从`ath79/generic` 移到`ath79/tiny`，旧版本升级时要改用新目标的镜像。

## 当前已知问题

* Zyxel EX5601-T0 的 WAN 接口由`eth1` 改名为`wan`，升级后要检查网络配置；
* Pixel 10 连接启用 WPA3 的 Wi-Fi 6 AP 时可能出现问题；
* WPA3 环境下开启 802.11r 快速漫游，部分客户端可能无法正常连接；
* 某些配置使用 SQM CAKE MQ（`cake_mq`）后，吞吐量可能偏低。

##

## FanchmWrt目前已经是基于25.12.4稳定版本发布固件，过段时间会同步OpenWrt 25.12.5版本代码，FanchmWrt的基础功能保持和OpenWrt官方稳定版一致，主要是为了保持功能的稳定性，对于WiFi驱动，OpenWrt官方是采用开源驱动，如果采用某些原厂sdk的驱动，Linux内核版本切换会很困难，一些漏洞也就无法修复。FanchmWrt主线的代码一定是和OpenWrt稳定版本完全一致，后续也会考虑基于第三方项目适配固件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRn5Ptd5hm2UQPjqBySWMgiao94fTicWficuhNliaNX1DDEG5XhtC5v2vvLBZGBkA7qpgDKlQWjBWJkNiat9IcicCznWeIzCb3bh0zeZ0/640?wx_fmt=png&from=appmsg)

历史文章：

[FanchmWrt1.0.3正式版发布，增加应用中心](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486826&idx=1&sn=d0bbd07992ec32f482ba0aa375ee7332&scene=21#wechat_redirect)

[OpenWrt手机App新版本来了](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486753&idx=1&sn=80697214ab25ec724a1e978c47a5996b&scene=21#wechat_redirect)

[OpenWrt应用过滤插件v6.1.8版本发布](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486720&idx=1&sn=04fc35ff3baf8bb0ef934e7978cbb045&scene=21#wechat_redirect)

[FanchmWrt 1.0.2正式版发布，代码已开源](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486676&idx=1&sn=1783274587d3dc681496bf52e3dad3ac&scene=21#wechat_redirect)

[FanchmWrt第一个正式版本发布](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486645&idx=1&sn=f6f2a32c899a6a050fffccea65649a2f&scene=21#wechat_redirect)

[支持刷机的路由器(2025)](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486582&idx=1&sn=9602044c4ef4b94f28b9473766958efa&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/4dGgALU2VXwxOVx85bAbC3CbFUBYEHduhydpeBQNuGCgk5xPlneKvuO7LSjFTYdEMoSffnUichcTV8Z2xFF25Qg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=dm2rfhjh&tp=webp#imgIndex=15)

欢迎关注公众号

定期分享OpenWrt干货

OpenWrt应用过滤插件作者(2.7k star)

FanchmWrt系统作者

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4dGgALU2VXwGPhSnjG6IhzI0wCrUicApDmpsL1c5VyoWFph6dicu8RydO8StibF1ibHIF7zOeAUrz31GPo9UGqNOTw/0?wx_fmt=png)

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