---
title: TCP的意义是什么？
url: https://mp.weixin.qq.com/s/Dhexn-fPbUaiKSbDFNFtTQ
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:56:39.944320
---

# TCP的意义是什么？

# TCP的意义是什么？

原创

车小胖谈网络
车小胖谈网络

车小胖谈网络

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

在向socket写的时候，write函数返回成功只能代表数据已拷贝到发送缓冲区，调用方没办法感知到数据到达对端协议栈里。如果想要确保数据对端能收到，还需应用层回个ack。

那为什么我不直接用udp发送和回ack呢？我理解tcp只是暗地里帮我自动超时重试几次以及多次调用的保序，只能说是相对可靠，还得依赖应用层ack去确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JQNVqWAicEnnNTEBqzrw4slicHogUoFvoVQdVA2ObyzbiaZDxCjs7rw7iac8FyQ9MYsxFkfcxYOyULuibYf6jGjC3Y6qDibib3sicusnRK7HZZ9LbgU/640?wx_fmt=jpeg&from=appmsg)

说的非常对，TCP的那几万行代码干的确实就是题主所描述的内容。

完全可以使用UDP发送packet，对packet进行使用ID进行编号。

接收方的user app对收到的packet ID进行ACK。

发送方立马就知道该ID的packet已经被user app成功接收。

新的挑战来了。。。

每一个Tx的packet，需要缓存，直到被ACK才能释放。准备如何缓存每一个Tx Packet？

如果发出的packet迟迟没有ACK，什么时候重传？使用固定不变的**Re-transmit timeout**来重传？还是基于实时测量的RTT计算动态得到的**Re-transmit timeout**来重传？ 网络的real time RTT是时刻在变化的，如果**Re-transmit timeout < Real Time RTT**，意味着ACK可能已经在返程的路上，已经启动packet的重传。换句话说，该packet并没有丢，可是依然被重传了。这个冗余重传的packet对Tx side，Rx side，Internet都是负担，都是减分项（bandwidth、CPU、Memory）。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7IBfTjcqbuXUVID3tibfKK56ribvLtXSHLOE3soDPPM8cLgPnqc5jBNG3XrBcfPrdj5h6rs2qF7mHSD1dSo4ZHxA/0?wx_fmt=png)

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