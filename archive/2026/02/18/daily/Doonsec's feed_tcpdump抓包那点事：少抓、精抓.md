---
title: tcpdump抓包那点事：少抓、精抓
url: https://mp.weixin.qq.com/s/wG5XcGmntYWzFDLp30-3MQ
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:18:44.911912
---

# tcpdump抓包那点事：少抓、精抓

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/G9vCzJwRv8Tnzoa2FX4aG2NpRwz19zS3uOiaQsX3OR0XT5TVmTyGBpt5C7S0KuFdu8e5q3lOSsSpkbBOerK5JsVONJrGHic4sRCib7N9wr5ibGo/0?wx_fmt=jpeg)

# tcpdump抓包那点事：少抓、精抓

原创

花鸟
花鸟

花鸟在线

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/G9vCzJwRv8R2PvNjlGE15LfWpia5N6Haics66Tb2e5yumYuCzUuc8EpnFMwjISspqibvz3qv1vBEt5neFwZmf0Pd2Dl26rEoHeBVtkA9BtJcWs/640?wx_fmt=jpeg&from=appmsg)

**一句话：先想清楚要抓什么，再写过滤条件，最后再动手。**

tcpdump是环境自带的，用 BPF 过滤器精准筛选数据 → 只留下“有意义的流量”。避免在噪声中被“掩埋”。

核心：

少抓

精抓

带条件抓

带状态抓

！！

```
能力结构
协议结构要理解↓会写 BPF↓会控制性能↓会结构化分析↓会结合攻击链思维
```

一、

1、按tcp标志位抓包

只抓SYN，判断谁发起外连

tcpdump -i eth0 'tcp[tcpflags] & tcp-syn != 0'

2、只抓RST，判断被拒绝

tcpdump -i eth0 'tcp[tcpflags] & tcp-rst != 0'

3、只抓FIN

tcpdump -i eth0 'tcp[tcpflags] & tcp-fin != 0'

二、

TCP有大量的ack，过滤掉无意义的流量

tcpdump -i eth0 'tcp[((tcp[12] & 0xf0) >> 2):4] != 0'

三、

1、抓特定字符

tcpdump -i eth0 -A 'tcp port 80 and tcp[((tcp[12] & 0xf0) >> 2):4] = 0x504f5354'

0x504f5354=POST;

0x47455420=GET

以上是TCP三次握手异常分析基本要领，感兴趣可以扩散下思路，变化的组合。

从运维角度主要关注业务连续性，从防守视角关注这里是否有异常（外连、外发、C2特征、横向行为）

所以从红队视角要知行一二。因为要知晓正常的行为是什么，才能更好领悟异常的行为是什么样。

延伸实践下其他模块，例如：

* 重传 / 窗口 / 拥塞排查
* C2 流量特征识别
* DNS 隧道流量识别模型

理解原理，切勿盲目堆工具。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LUFdknfa3USibnuy0Vpo6UXQvCbGAIj8xY31R2Kl75pIiafOVicDbts1OWUrAK1KhBXAdZdlTWDPKb65ts6oCNVIA/0?wx_fmt=png)

花鸟在线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LUFdknfa3USibnuy0Vpo6UXQvCbGAIj8xY31R2Kl75pIiafOVicDbts1OWUrAK1KhBXAdZdlTWDPKb65ts6oCNVIA/0?wx_fmt=png)

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