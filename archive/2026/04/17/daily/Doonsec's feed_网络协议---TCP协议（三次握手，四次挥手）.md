---
title: 网络协议---TCP协议（三次握手，四次挥手）
url: https://mp.weixin.qq.com/s/ng_pPmLMklbZbpPXhcamoA
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:29:40.275576
---

# 网络协议---TCP协议（三次握手，四次挥手）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibIKibEUpvLO8YALwB8WFILfCtf8LfKOAZkNFzomvjF6C58UXyP36saodND7fytc6arwgsdZmSlQgEnEGdwZAzA/0?wx_fmt=jpeg)

# 网络协议---TCP协议（三次握手，四次挥手）

原创

老五
老五

老五说网络

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、基本概念

TCP（Transmission Control Protocol，传输控制协议）是互联网协议族中最为重要的协议之一，它工作在OSI七层模型的传输层，为应用程序提供可靠的、面向连接的通信服务。以下是TCP协议的一些关键特性及其工作机制的简要说明：

1. 面向连接，在数据传输之前，TCP要求双方建立一个连接。这通常通过三次握手来完成。
2. 可靠性，TCP通过确认机制保证数据包能够到达目的地。如果发送方没有收到确认信息，它将重新发送数据包。序列号用于确保数据包按照正确的顺序重组，并检测重复的数据包。
3. 流量控制，TCP使用滑动窗口机制进行流量控制，以防止快速发送方压垮慢速接收方。
4. 拥塞控制，为了避免网络过载，TCP实现了一系列拥塞控制算法，比如慢启动、拥塞避免、快速重传和快速恢复等。
5. 数据分段与重组，大的数据块会被分割成更小的段进行传输，每个段都会被赋予序列号以便在接收端正确重组。
6. 连接终止，当通信结束时，TCP需要通过四次挥手的过程来断开连接，确保双方都有机会完成必要的清理工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gibIKibEUpvLO8YALwB8WFILfCtf8LfKOA0nPNKDMBtlcyBngjK6OWHtSibJm0VJsuSc13mumBcbhONQcibibTDSoFQ/640?wx_fmt=png&from=appmsg)

二、工作流程

1、建立连接 - 三次握手

* 客户端发送SYN（同步序列编号）报文给服务器。
* 服务器回复SYN-ACK报文给客户端。
* 客户端再发ACK（确认）报文给服务器，连接建立。

2、数据传输

* 发送方根据接收方提供的窗口大小调整发送速率，同时利用序列号和确认号确保数据可靠传输。

3、断开连接 - 四次挥手

* 主动关闭方发送FIN报文请求关闭连接。
* 被动关闭方回应ACK报文，同意关闭输入流。
* 被动关闭方随后也可能发送自己的FIN报文请求关闭输出流。

* 最后主动关闭方回应ACK报文，确认所有操作完成，连接彻底关闭。

三、数据报文解析：

1、拓扑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gibIKibEUpvLO8YALwB8WFILfCtf8LfKOAGZuTenSibjibbuZ5kanFIwr8C16jVNc9gFbnzkzZeSjjiaW5Xia5OtNNtw/640?wx_fmt=png&from=appmsg)

2、数据报文分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gibIKibEUpvLO8YALwB8WFILfCtf8LfKOAsEnVcuj7wqkG0Rbeg8weRBbvjcMb0CytsHn03c1Z3nct5E1iblqbgDA/640?wx_fmt=png&from=appmsg)

第一步：TCP三次握手（建立连接）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gibIKibEUpvLO8YALwB8WFILfCtf8LfKOA4jon3ZUFJvpN57qokBTUQB0hfgHmOBsgzRmtiaTPNlYIGP7GuGyQTww/640?wx_fmt=png&from=appmsg)

1、客户端192.168.1.1发起建立连接

* Source: 192.168.1.1:13761 → Dest: 192.168.1.2:hosts2-ns --- 客户端（192.168.1.1）发起连接请求。
* Flags: [SYN] Seq: 0 --- 发送 SYN 包，初始序列号为 0
* Win: 64512 MSS: 1460 TSV: 591102 --- 指定最大分段大小（MSS）为 1460 字节，窗口大小 64512。时间戳（TSV）用于 RTT 测量。

2、服务器192.168.1.2响应SYN+ACK

* Source: 192.168.1.2:hosts2-ns → Dest: 192.168.1.1:13761 --- 服务器（192.168.1.2）响应 SYN+ACK
* Flags: [SYN, ACK] Seq: 0 Ack: 1 --- 确认客户端的 SYN（Ack=1），自己的初始序列号为 0
* Win: 65160 MSS: 1460 --- 返回自己的 MSS 和窗口大小。

3、客户端192.168.1.1发送ACK确认收到SYN

* Source: 192.168.1.1:13761 → Dest: 192.168.1.2:hosts2-ns
* Flags: [ACK] Seq: 1 Ack: 1 --- 客户端192.168.1.1发送ACK确认收到SYN
* Win: 65160 --- 窗口大小 64512

三次握手正式建立完成

第二步：数据传输

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gibIKibEUpvLO8YALwB8WFILfCtf8LfKOAia5RXxOicjsfdffiaIgrhZLuribMuyAsfgpo75Vh3jPHibnde18ZYm0czEA/640?wx_fmt=png&from=appmsg)

4、客户端发送一个18字节的报文

* Source: 192.168.1.1 (13761) Dest: 192.168.1.2 (hosts2-ns)
* Flags: [PSH, ACK]Seq:  1 → Seq: 19 (Len=18) Ack: 1 --- 客户端发送一个包含 18 字节数据 的报文。标志位 PSH 表示“推”数据，要求接收方立即交付给应用层。序列号从 1 到 19（共 18 字节）。ACK=1 表示已确认服务器的序列号 1。

5、服务器确认收到客户端的 18 字节数据

* Source: 192.168.1.2 (hosts2-ns) Dest: 192.168.1.1 (13761)
* Flags: [ACK] Ack: 19 --- 确认号变为 19，表示期望下一个字节是第 19 字节

数据传输完成（单向）

第三步：TCP 四次挥手（关闭连接）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gibIKibEUpvLO8YALwB8WFILfCtf8LfKOAakafuYPucKtFuSMZKbrCvK5qHU9uhw8xlFc35Z1TXVd056mKNMYVOw/640?wx_fmt=png&from=appmsg)

6、服务器192.168.1.2主动发起关闭连接

* Source: 192.168.1.2 (hosts2-ns) Dest: 192.168.1.1 (13761)
* Flags: [FIN, ACK] Seq: 1 Ack: 19--- 发送 FIN 包，表示它不再发送数据。Seq=1：表示它的最后一个数据字节是第 1 字节（序列号从 0 开始），现在用 FIN 占一个序号。Ack=19：确认已收到客户端发来的 18 字节数据（到 Seq=18）。

7、客户端192.168.1.1响应服务器的 FIN

* Source: 192.168.1.1 (13761) Dest: 192.168.1.2 (hosts2-ns)
* Flags: [ACK] Seq: 19 Ack: 2 --- 发送 ACK，确认收到了服务器的 FIN。Ack=2：表示确认了服务器的 FIN（FIN 占一个序列号，所以是 1+1=2）。Seq=19：当前客户端发送的下一个序列号是 19（因为之前只发了 18 字节数据）。

8、客户端192.168.1.1也想关闭连接，发送自己的 FIN

* Source: 192.168.1.1 (13761) Dest: 192.168.1.2 (hosts2-ns)
* Flags: [FIN, ACK] Seq: 19 Ack: 2 --- Seq=19：表示客户端接下来要发送 FIN（但不带数据）。Ack=2：再次确认服务器的 FIN 已收到。同时携带 ACK 标志，表示这是一个“FIN + ACK”组合包。

9、服务器192.168.1.2回应客户端的 FIN

* Source: 192.168.1.2 (hosts2-ns) Dest: 192.168.1.1 (13761)
* Flags: [ACK] Seq: 2 Ack: 20 --- Ack=20：确认收到客户端的 FIN。
* Seq=2：服务器自己的下一个序列号是 2（上一次是 1）

四次挥手完成（连接正常关闭）

四、总结

TCP协议的设计使得它非常适合于那些对数据准确性要求高的应用，如网页浏览、电子邮件和文件传输等。然而，由于其复杂的机制，TCP并不适用于所有类型的网络通信，特别是对于实时性要求极高的应用场景，例如语音通话或视频会议，可能更倾向于使用UDP（用户数据报协议）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibIKibEUpvLO8YALwB8WFILfCtf8LfKOAribE9m8ESzIicic2U0Qxxp0qSicYRhJ8Isoia2ibjb8xpoicHCx12VuQahcmw/640?wx_fmt=jpeg&from=appmsg)

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