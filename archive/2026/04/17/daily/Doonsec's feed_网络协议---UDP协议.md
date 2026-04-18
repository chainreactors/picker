---
title: 网络协议---UDP协议
url: https://mp.weixin.qq.com/s/VxwkPTDBiWIdgFevqgrraA
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:29:43.365056
---

# 网络协议---UDP协议

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibIKibEUpvLPjAzgGr9D89UNCW2yCm0H8Hn7VwWmCcrKv5uEEEXuxiaqGOf259vEicNzZvdeuFR5cXtZrJM61xoMQ/0?wx_fmt=jpeg)

# 网络协议---UDP协议

原创

老五
老五

老五说网络

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

基本概念：

    UDP（User Datagram Protocol，用户数据报协议）是一种无连接的传输层协议，属于TCP/IP协议族的一部分。它提供了一种简单、轻量级的数据传输机制，适用于对传输速度要求高、但对可靠性要求相对较低的应用场景。

一、UDP的基本概念和特点：

1. 无连接（Connectionless）

* UDP在发送数据前不需要建立连接。
* 发送方直接将数据包发送给接收方，不进行握手或状态维护。

2. 不可靠传输（Unreliable）

* UDP不保证数据一定到达目的地。
* 不提供重传、确认、排序或流量控制机制。
* 如果数据包在网络中丢失、损坏或乱序，UDP不会自动处理。

3. 面向数据报（Datagram-oriented）

* 每个UDP消息都是一个独立的数据报，包含完整的源端口和目的端口信息。
* 接收方一次读取一个完整数据报（不会出现“粘包”问题，但可能丢包）。

4. 头部开销小

UDP头部仅8字节，包含以下字段：

* 源端口号（2字节）
* 目的端口（2字节）
* 长度（2字节，包括头部和数据）
* 校验和（2字节，可选，在IPv4中可省略；IPv6中强制使用）

5. 支持广播和多播

* UDP可以向多个接收者同时发送数据（一对多、多对多通信），适合流媒体、在线游戏、DNS查询等场景。

6. 速度快、延迟低

* 由于没有连接建立、确认、重传等机制，UDP传输效率高，延迟低。

二、常见应用场景

1. DNS查询（域名解析）
2. 实时音视频通话（如VoIP、Zoom、WebRTC）
3. 在线游戏
4. 物联网（IoT）设备通信
5. NTP（网络时间协议）
6. DHCP（动态主机配置协议）

三、UDP报文格式

|  |  |
| --- | --- |
| 源端口（Source Port） | 目的端口（Destination Port） |
| 长度（Length） | 检验和（Checksum） |
| date（数据） | |
|

四、UDP报文分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gibIKibEUpvLPjAzgGr9D89UNCW2yCm0H8AVKHz0Diby0fqrWM5UxhYrHeD2YIicmrhuIRJg1IO8Mepmu7AxNibcArA/640?wx_fmt=png&from=appmsg)

1. User Datagram Protocol, Src Port: 58410, Dst Port: domain (53)

表示这是一个 UDP 数据包。

* 源端口（Src Port）：58410

  发送方使用的端口号，通常是随机生成的临时端口，用于标识客户端进程。
* 目的端口（Dst Port）：domain (53)

  目标端口是 53，这是 DNS 服务的标准端口。

  “domain” 是端口号 53 的服务名称。

说明：这是一条客户端向DNS服务器发送的请求（比如查询某个域名的IP地址）。

2. Length: 39

* UDP 数据报的总长度（包括头部和数据部分）为 39 字节。

  UDP 头部固定为 8 字节，因此：

  数据部分长度 = 39 - 8 = 31 字节

  这个长度通常包含一个 DNS 查询报文（如 A 记录查询）。

3. Checksum: 0x962f [validation disabled]

* 校验和（Checksum） 值为 0x962f（十六进制）。

  →[validation disabled] 表示当前工具（如 Wireshark）未启用校验和验证功能，即不会自动检查该值是否正确。

  →校验和用于检测数据在传输过程中是否发生错误。UDP 的校验和是可选的（IPv4 中可不使用，但 IPv6 中强制要求）。

4. [Good Checksum: False]

    表示 Wireshark 检查后认为这个校验和不是有效的（或无法确认有效）。

可能原因：

* 校验和计算错误
* 网络设备修改了数据（如某些防火墙、NAT）
* 或者只是因为“validation disabled”，所以标记为 false

5. [Bad Checksum: False]

    表示没有发现明显的校验和错误。

说明：虽然 Good Checksum: False，但 Bad Checksum: False 说明它不是明显错误的，可能是校验和缺失或未被验证。

注意：这两个字段有时会冲突，取决于抓包环境和配置。

五、UDP协议与TCP协议对比

|  |  |  |
| --- | --- | --- |
| UDP与TCP简要对比 | | |
| 特性 | UDP | TCP |
| 连接方式 | 无连接 | 面向连接（三次握手 |
| 可靠性 | 不可靠 | 可靠（确认+重传） |
| 传输顺序 | 不保证顺序 | 保证顺序 |
| 头部大小 | 8 字节 | 至少 20 字节 |
| 速度/开销 | 快、低开销 | 较慢、高开销 |
| 适用场景 | 实时性要求高、容忍丢包 | 要求数据完整、可靠传输 |

总结：UDP是一种“尽力而为”的传输协议，牺牲了可靠性以换取速度和效率，非常适合对实时性敏感但能容忍少量数据丢失的应用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibIKibEUpvLPjAzgGr9D89UNCW2yCm0H82oj8dQoSaYh1nicnWDLWFyiaLGhp5KOkDPSA5QVEtPicicsHglDLvjEE4g/640?wx_fmt=jpeg&from=appmsg)

公众号：老五说网络

![](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB11mh9RFGEjMRagriaFDGoibeyfBicEmDTyx007LKXeaoxA0mib2DRZMqaj7I1J1ibWw9TcGhw74hprXFlg/640)

长按左侧二维码关注

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLOJzH1ibvfvuFCD14XFsicawiaoknTMvxaEdUvgrDMyGO31nS6B2As3IjHzIr2xeMA4dtrXg4SpwYW6Q/0?wx_fmt=png)

老五说网络

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLOJzH1ibvfvuFCD14XFsicawiaoknTMvxaEdUvgrDMyGO31nS6B2As3IjHzIr2xeMA4dtrXg4SpwYW6Q/0?wx_fmt=png)

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