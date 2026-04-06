---
title: 别再只会一种！华为 vs 思科 故障排查命令对照手册
url: https://mp.weixin.qq.com/s/nnYGSrTDXYiO_sF2rIHqgA
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:43:50.314931
---

# 别再只会一种！华为 vs 思科 故障排查命令对照手册

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vf29dJy0S584YCUQCAOib85czZFIg4rkRcuwagk5YF8F7ulXF99rBsy9ibvXhs2dWP2xkQulWibfXcAticeeR4HrvrxMu4VA0MV2MhDjWIAibR1M/0?wx_fmt=jpeg)

# 别再只会一种！华为 vs 思科 故障排查命令对照手册

原创

圈圈
圈圈

网络技术干货圈

![]()

在小说阅读器中沉浸阅读

点击上方 网络技术干货圈，选择 设为星标

优质文章，及时送达

![](https://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT9z1qCg1V9MbsCSdmUBkOicVRmk5T6j0m8Z8L9YdmdU0crxLkBG4994IkXaZTrSnJAZksCicKaqO43g/640?wx_fmt=png)

> 转载请注明以下内容：
>
> **来源**：公众号【网络技术干货圈】
>
> **作者**：圈圈
>
> **ID**：wljsghq

在实际工作中，我们经常会遇到这样一个尴尬场景：

你在华为设备上排查得飞起，换到思科设备，突然就“不会了”；或者反过来，在 Cisco CLI 里如鱼得水，到了华为 VRP 直接懵。

**本质问题就一个：命令体系不同，但排障思路是共通的。**

这篇文章，我就带你系统梳理一份：

👉 **华为 vs 思科 故障排查命令对照表（工程师实战版）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S59Y133kcibpn5I64q4lMYFYxL1wJyaV9h7Vwoiboia2vjfYnsbLR3xDG0mCcKTSibMwia2g4pISKjsmk3BFruoxWtGKX8F9qyONsX8w/640?wx_fmt=png&from=appmsg)

不仅是简单对照，还会结合实际场景，帮你真正“融会贯通”。

# 一、排障思路先统一

在进入命令之前，先记住一个核心原则：

> **网络排障 ≠ 背命令，而是“分层定位”**

标准流程：

1. 物理层（接口/光模块）
2. 二层（MAC / VLAN / STP）
3. 三层（ARP / 路由）
4. 四层以上（策略 / ACL / NAT）

命令只是工具，思路才是核心。

# 二、基础信息与设备状态

| 功能 | 华为命令 | 思科命令 | 说明 |
| --- | --- | --- | --- |
| 查看系统信息 | display version | show version | 系统版本、型号 |
| 查看运行配置 | display current-configuration | show running-config | 当前配置 |
| 查看启动配置 | display saved-configuration | show startup-config | 启动配置 |
| 查看设备时间 | display clock | show clock | 时间同步问题 |
| 查看CPU使用率 | display cpu-usage | show processes cpu | 是否高负载 |
| 查看内存使用 | display memory | show memory | 内存占用 |
| 查看日志 | display logbuffer | show logging | 故障线索核心 |

👉 **经验：** 日志是最容易被忽略，但最有价值的信息来源。

---

# 三、接口与物理层排查

| 功能 | 华为命令 | 思科命令 | 说明 |
| --- | --- | --- | --- |
| 查看接口状态 | display interface | show interfaces | 核心命令 |
| 查看简要接口 | display interface brief | show ip interface brief | 快速查看UP/DOWN |
| 查看光模块 | display transceiver | show interfaces transceiver | 光功率 |
| 查看接口错误 | display interface | show interfaces | CRC、丢包 |
| 查看接口描述 | display interface description | show interfaces description | 识别链路 |
| 查看链路聚合 | display eth-trunk | show etherchannel summary | 聚合状态 |

👉 **重点指标：**

* CRC error → 物理链路问题
* input error → 收包异常
* output drops → 队列/拥塞

---

# 四、二层排查（交换核心）

## 1. MAC 地址表

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| 查看MAC表 | display mac-address | show mac address-table |
| 查看指定MAC | display mac-address mac-address XXXX | show mac address-table address XXXX |

👉 用途：定位终端接入位置

---

## 2. VLAN 信息

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| 查看VLAN | display vlan | show vlan brief |
| 查看接口VLAN | display port vlan | show interfaces switchport |

---

## 3. STP（生成树）

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| 查看STP | display stp | show spanning-tree |
| 查看端口状态 | display stp brief | show spanning-tree brief |
| 查看根桥 | display stp root | show spanning-tree root |

👉 **常见问题：**

* 环路 → 广播风暴
* 根桥异常 → 路径不优

---

# 五、三层排查（IP / 路由）

## 1. IP与ARP

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| 查看ARP | display arp | show ip arp |
| 查看IP接口 | display ip interface brief | show ip interface brief |

---

## 2. 路由表

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| 查看路由 | display ip routing-table | show ip route |
| 查看静态路由 | display current-configuration | show running-config |
| 查看协议路由 | display ospf routing | show ip ospf route |

---

## 3. 连通性测试

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| Ping | ping | ping |
| Tracert | tracert | traceroute |

👉 **排障口诀：**

> ping 不通看路由， 路由没问题看 ARP， ARP 正常看 ACL。

---

# 六、路由协议排查（OSPF / BGP）

## 1. OSPF

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| 查看邻居 | display ospf peer | show ip ospf neighbor |
| 查看LSDB | display ospf lsdb | show ip ospf database |
| 查看接口状态 | display ospf interface | show ip ospf interface |

---

## 2. BGP

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| 查看邻居 | display bgp peer | show ip bgp summary |
| 查看路由 | display bgp routing-table | show ip bgp |
| 查看详细信息 | display bgp peer verbose | show ip bgp neighbors |

👉 **常见问题：**

* 邻居不建立 → IP / AS / ACL
* 路由不通 → 策略 / next-hop

---

# 七、ACL 与安全策略

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| 查看ACL | display acl all | show access-lists |
| 查看接口应用 | display traffic-filter | show run interface |
| 查看命中计数 | display acl | show access-lists |

👉 **关键点：**

* 是否命中
* 是否方向错误（in/out）
* 是否顺序问题

---

# 八、NAT 与策略排查

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| 查看NAT | display nat session | show ip nat translations |
| 查看统计 | display nat statistics | show ip nat statistics |

---

# 九、调试与抓包（进阶）

| 功能 | 华为 | 思科 |
| --- | --- | --- |
| 调试命令 | debugging | debug |
| 关闭调试 | undo debugging all | undebug all |
| 抓包 | observe-port | monitor session |

👉 **注意：**

调试命令慎用！生产环境可能直接把设备“打爆”。

---

很多工程师会陷入一个误区：

> “我只会华为 / 我只会思科”

但在企业网络里：

* 混合厂商是常态
* 云网络更复杂
* 自动化逐渐普及

👉 真正的能力是：

* 理解协议
* 掌握排障路径
* 熟悉不同 CLI 风格

命令可以背，但思路必须内化。会一种是入门，会对照才是进阶。

# **---END---** **重磅！网络技术干货圈-技术交流群已成立** 扫码可添加小编微信，**申请进****群。** **一定要备注：****工种+地点+学校/公司+昵称****（如网络工程师+南京+苏宁+猪八戒）**，根据格式备注，可更快被通过且邀请进群 ![](https://mmbiz.qpic.cn/mmbiz_jpg/p8No8ScJKT94LpPQZiap0D6hj7eQmHdDUQEvWdRGMD2ic4JQ2Gq8cibgVt0TgPeRfG7OoP3doq9023GkcecKBCW2A/640?wx_fmt=jpeg) ▲长按加群

![](https://mmbiz.qpic.cn/mmbiz_gif/p8No8ScJKT91zHQia5QWRMJhVxUyF4g3ZAuv0YbUEoiaVCzgE2gQT6eQC0Hx6icUE9HQbqFfVP3sSqbIUksF1Ojrg/640?wx_fmt=gif)

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