---
title: 密西根大学 | OpenVPN下的指纹识别
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491520&idx=1&sn=f3bacbb23ae0aece8dec75f687816b13&chksm=fe2ee04bc959695d4b77fe314173c1efea4d13849e9b908fbceed0d0cd4649082bc8c2132ff4&scene=58&subscene=0#rd
source: 安全学术圈
date: 2025-01-04
fetch_date: 2025-10-06T20:10:58.742393
---

# 密西根大学 | OpenVPN下的指纹识别

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WGyR7z34s6JAEeSRlrmJNLjShQXmPP9Oq3KhxOjICedmbhhGicD86icpzjw24UVLoMwibf1yz6ibj7oaw/0?wx_fmt=jpeg)

# 密西根大学 | OpenVPN下的指纹识别

原创

孙汉林

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGyR7z34s6JAEeSRlrmJNLjJvDArR08SXzaZvIm2DQgicbxLibbW14FXOmibwdOsrO8rYkpGd7zb4X0A/640?wx_fmt=png&from=appmsg)
> *原文标题：OpenVPN is Open to VPN Fingerprinting*
> *原文作者：Diwen Xue, Reethika Ramesh, Arham Jain, Michalis Kallitsis, J. Alex Halderman, Jedidiah R. Crandall and Roya Ensafi*
> *原文链接：https://www.usenix.org/conference/usenixsecurity22/presentation/xue-diwen*
> *视频链接：https://youtu.be/ZNVff1rH-vA*
> *发表会议：USENIX Security '22*
> *笔记作者：孙汉林@安全学术圈*
> *主编：黄诚@安全学术圈*

### 1、引言

本文分析了流行的VPN工具OpenVPN，并受GFW(Great Firewall)的启发，提出一种由`被动分析`和`主动探测`相结合的两阶段识别框架，通过分析字节模式、数据包大小和服务器行为3种特征，在低误报率的情况下，识别了85%以上的OpenVPN流量。

### 2、威胁模型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGyR7z34s6JAEeSRlrmJNLj8ZiaaswZL7PLGF55vwmEwPlYkHzPZ3Yzw4Qzjep2EmBLaPmpJTyCanw/640?wx_fmt=png&from=appmsg)与GFW的威胁模型类似，具体分为如下6个阶段：

* 客户端通过ISP网络连接到VPN服务器；
* 过滤器备份ISP网络中的流量；
* 过滤器将可疑目标转发至探测系统；
* 探测系统将目标分发至不同探测器；
* 探测器发送探针获取探测结果；
* 探测结果为VPN服务器的目标被存入数据库。

### 3、特征选取

在本文中，作者选取了3种特征来识别OpenVPN流量，即字节模式、数据包大小和服务器行为，其中前两个属于被动分析，最后一个属于主动探测。下图是OpenVPN的握手和数据交换过程，3种特征都基于此过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGyR7z34s6JAEeSRlrmJNLjhAQArBdIVpuXkXdibPpLX3nkF1UxeD9ESiawaJ4hCO83UyNvKLfibjtUg/640?wx_fmt=png&from=appmsg)

##### 3.1 字节模式

基于字节模式的指纹识别方法通过分析 OpenVPN 流量中的操作码（Opcode）字段来识别流量类型。OpenVPN 数据包包含一个操作码字段，用于指示消息类型，如客户端和服务器重置、TLS 加密数据等，完整字节模式如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGyR7z34s6JAEeSRlrmJNLjlnJVbEaYV75Y1ek2ZDYbzVds2cKPiamgym4AjmEtjldwvsqibnUe4pvw/640?wx_fmt=png&from=appmsg)

本文通过捕获前 N 个数据包的操作码序列，若序列中的不同操作码数量≥4（至少需要4种不同的操作码来完成握手，协议一共定义了10种操作码。），并且Client和Server的Reset操作码分别只出现过1次，则将该流量标记为OpenVPN流。此外，OpenVPN 使用 XOR 混淆技术保护数据负载，但操作码数量不受影响，因此即使流量经过混淆，操作码仍能提供有效的识别特征。这种指纹识别方法无需精确匹配操作码值或数据包大小，鲁棒性高，并能有效应对多种 XOR 混淆技术，确保高效准确地识别 OpenVPN 流量。

##### 3.2 数据包大小

在OpenVPN的控制通道中，P\_ACK包用于确认P\_Control包，这些ACK包具有固定大小，并且只在会话的初期握手阶段出现，在数据传输阶段则不再使用。因此，P\_ACK包在OpenVPN流量中呈现出独特的时序模式，成为一个可被识别的特征。

具体来说，本文通过分析OpenVPN会话的初期包交换序列（C->S (Client-Reset), S->C (Server-Reset), C->S (ACK), C->S(Control)），定位出初始的P\_ACK包(第3个)，并计算在每10个数据包中的ACK包数量，看是否满足OpenVPN的ACK数据包指纹（初期多，后期少）。该指纹识别技术对于识别未经随机填充（不改变ACK数据包大小）的OpenVPN混淆流量非常有效，且容易在实际的流量监控中部署。

##### 3.3 服务器行为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGyR7z34s6JAEeSRlrmJNLjdPGJYZVrzHkHQYRlG9RcoFwGd90AQJMfcNDKvBv4HSiaxr4f4KHuLIA/640?wx_fmt=png&from=appmsg)

本文讨论了通过主动探测识别OpenVPN服务器的可行性。许多OpenVPN服务器使用tls-auth或tls-crypt选项，增加了HMAC签名以提供**完整性**和**认证**机制，使得未经认证的客户端探测请求被服务器丢弃，从而提高了抗探测能力。尽管如此，作者设计了针对OpenVPN的探测方法，通过利用TCP层的行为特征，如超时或重置行为，仍能有效识别OpenVPN服务器。OpenVPN处理TCP包的流程如上图。

###### 3.3.1 基础探针

OpenVPN在处理TCP流时，会在内存中分配缓冲区，组装接收到的数据包片段，直到满足长度条件才开始解析和检查语法及加密错误。基于这一行为，作者设计了两种探针，以期望触发OpenVPN服务器的两种不同反应。作者根据OpenVPN服务器与非OpenVPN服务器对两种探针的不同反应识别OpenVPN服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGyR7z34s6JAEeSRlrmJNLjqJKwvbL1xcpBibFMWickaasJjPpdG7z9AA0hRvL6e2ds2YWHicRg9LmxQ/640?wx_fmt=png&from=appmsg)

第一个探针（BaseProbe 1）包含一个经典的16字节OpenVPN客户端重置包，第二个探针（BaseProbe 2）在前者基础上去掉末尾一个字节。大多数非OpenVPN服务器会以相似的方式响应这两种探针，而对于启用HMAC的OpenVPN服务器来说，因为验证HMAC失败，第一个探针会被立即丢掉；第二个探针因没有凑够有效的解析长度而等待至超时。

###### 3.3.2 附加探针

为了进一步提高对OpenVPN服务器的探测精度，作者设计了基于Linux服务器关闭TCP连接方式的探针。当TCP连接在有未读字节时被终止，Linux服务器会发送RST包。大多数OpenVPN服务器的RST阈值（RST阈值定义为触发RST包所需的最小字节数）在1550-1660字节之间，而大部分非OpenVPN服务器的阈值低于500字节或高于4000字节。因此，作者构造了一个包含2000字节随机数据的探针，预计98%以上的OpenVPN服务器会回应RST包，而非OpenVPN服务器的回应率不到3%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGyR7z34s6JAEeSRlrmJNLjGPSBP19Z7eSBuUAI21aficQFibl9oc8l3ibh6c17rA0tiagYMKpVf83P1A/640?wx_fmt=png&from=appmsg)

此外，由于OpenVPN支持端口共享功能，探针可能被转发给共享端口的其他服务（HTTP、TLS和SSH）解析，因此在发送基础探针后（此时已经过滤了大部分非共享端口的HTTP、TLS、SSH等服务），会首先探测这些服务，若收到正常响应，则停止探测，并将该服务器标记为非OpenVPN服务器。

### 4、实验结果

为了验证方案的有效性，作者将该方案部署到真实的ISP网络中，并得到如下实验结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGyR7z34s6JAEeSRlrmJNLjiaFOrlFzKcgeSUjqSWJvWzMTY1g5HibYJ5ATnic3TsXF74noE3H4Gq7mA/640?wx_fmt=png&from=appmsg)

总的来说，在控制流中，识别原版OpenVPN的召回率达到85.90%，识别具有混淆技术的OpenVPN的召回率达到72.67%。在所有流中，共识别出3245个能够被证实是OpenVPN流量的流，393个不能够被证实的流。

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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