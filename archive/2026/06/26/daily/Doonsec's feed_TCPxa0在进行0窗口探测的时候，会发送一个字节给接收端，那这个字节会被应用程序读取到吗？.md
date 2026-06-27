---
title: TCPxa0在进行0窗口探测的时候，会发送一个字节给接收端，那这个字节会被应用程序读取到吗？
url: https://mp.weixin.qq.com/s/HGHPPi1zsUrc20_S1775mg
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:49:51.576105
---

# TCPxa0在进行0窗口探测的时候，会发送一个字节给接收端，那这个字节会被应用程序读取到吗？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JQNVqWAicEnnrYBApwEA8OnRicVDiasibSHEj7NvtQ4otYhWugqxHkXefzEp1TeEHnFVMp8KrdP9Dv4aXYZHuVtiaOsInxpRQ4K76Mk6YoSss7sQ/0?wx_fmt=jpeg)

# TCP 在进行0窗口探测的时候，会发送一个字节给接收端，那这个字节会被应用程序读取到吗？

原创

车小胖谈网络
车小胖谈网络

车小胖谈网络

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**看TCP/IP详解的时候，看到下面一段话：**

**When the persist timer expires, 1 byte of data is sent (segment 6). The receiving application has read 256 bytes from the receive buffer (at time 3.99),so the byte is accepted and acknowledged (segment 7). But the advertised window is still 0, since the receiver does not have room for either one full-sized segment or one-half of its buffer. This is silly window avoidanceby the receiver.**

**我想问的是这个字节被ACK了，是不是之后要被应用程序读取 ，但这个字节并不是应用程序真正需要的呀！或者有什么方式TCP能做到不会吧这个字节传给应用程序？**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JQNVqWAicEnlicQKMlL1zFC2dibHnwKa2ic5zOj6By1UKD1NvSQpibtq20ha3BKH9VZ0HibefEljtf1I4XkiaYZrQJSGVA7TibzFl2meGBWiaomAyS0Y/640?wx_fmt=png&from=appmsg)

不会的！

**为何？**

因为用于probe的TCP报文这1个byte的数据是duplicated data。

假设A传输给B最后一个byte的序列号为sequence=**123456**，byte =0x**AA**。

B的接收缓冲区耗尽，于是B紧急发一个window=0的TCP报文给A。

A收到之后立马停止发送，并启动pesist timer，开始倒计时。。。

如果在pesist timer 倒计时到0之前，A收到B的window>0更新，停止并复位pesist timer，A就可以继续发送了。

如果没有收到window更新，pesist timer 响，触发A发送probe报文。

该报文的sequence=**123456**，byte =0x**AA**。

**B收到该报文，发现该序列号对应的数据**byte =0x**AA**已经接收，判断为duplicated。于是丢弃该报文并发送该报文的ACK。

A收到ACK报文如果发现window依然=0，复位pesist timer，继续倒计时，等待下一次的振铃。

A收到ACK报文，如果发现window >0，复位并停止pesist timer，有data就可以发送了。

书中提到的“**accepted**” +“**acknowledged**”字眼组合在一起就是上文的描述，**accepted**并不是真正意义上接受的意思，因为**se**quence=**123456**，byte =0x**AA**这个字节，位于B 的RX方向滑动窗口的左侧，是invalid的，故要丢弃。

上文的“A收到ACK报文，如果发现window >0，复位并停止pesist timer，有data就可以发送了。” 这句话是有问题的！！！

假设B给A的window更新为 window =5，按照上文的说法，A就可以给B发数据了？

如果A要发送5 bytes的数据，需要添加20 bytes的IP、20byte +TCP头，传输效率非常低下，这就是书中提到的**silly window**。

如何**silly window avoidance？**

**通信双方都要严格约束自己。**

**A要做到的是，如果A发现B的window更新不满足**

**one full-sized segment or one-half of its buffer**

**即使window >0 ,也并不发送data。**

好抽象，举个例子

**1.**如果A与B通信协商的MSS = 1448，B握手连接的初始window =4096

那么  min（mss， 0.5 \*window） = min（1448， 0.5\*4096）=1448

**A如果发现B发给自己的window ≥ 1448，才会发送data。**

**2.**如果A与B通信协商的MSS = 1448，B握手连接的初始window =1024

那么  min（mss， 0.5 \*window） = min（1448， 0.5\*1024） =512

**A如果发现B发给自己的window ≥ 512，才会发送data。**

这是RFC想要表达的真正的意思，宽以待人，严于律己，即使B犯傻，也不会造成**silly window后遗症，只要通信双方有一方不犯傻即可。**

**RFC同样约束B。**

3如果A与B通信协商的MSS = 1448，B握手连接的初始window =4096

那么  min（mss， 0.5 \*window） = min（1448， 0.5\*4096）=1448

当B的接受缓冲区由于user持续读取data，空闲出了512 byte，能发window update吗？

不能，因为 512 < 1448！

空闲出了1024 byte呢？

依然不能，因为 1024 <1448!

空闲出2000 byte呢？

可以了，因为 2000 > 1448。

4. 如果A与B通信协商的MSS = 1448，B握手连接的初始window =1024

那么  min（mss， 0.5 \*window） = min（1448， 0.5\*1024） =512

当B的接受缓冲区由于user持续读取data，空闲出了100 byte，能发window update吗？

不能，因为 100 < 512！

空闲出了512 byte呢？

可以了，因为 512 ≥ 512!

任意一方遵守RFC约定，即使另外一方naive，也可以**silly window avoidance**。

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