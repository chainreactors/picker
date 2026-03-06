---
title: Wireshark进阶技巧:通过DNS查询来分析可疑流量中恶意软件感染事件
url: https://mp.weixin.qq.com/s/ZyWkAfgehWhCUA37X1SV7w
source: Doonsec's feed
date: 2026-03-05
fetch_date: 2026-03-06T04:02:46.146139
---

# Wireshark进阶技巧:通过DNS查询来分析可疑流量中恶意软件感染事件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EqMwaEZz0ykuqJbqw6ibIREDZnzviaoty2BiaojiaIjzqV6t45B7Ge6vKcwpVAfJEqWwia5ya0ysKmFTaXdic4cFWkEA/0?wx_fmt=jpeg)

# Wireshark进阶技巧:通过DNS查询来分析可疑流量中恶意软件感染事件

原创

CatalyzeSec
CatalyzeSec

CatalyzeSec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/N2vfpRNU8pAITZd4qAicYWBGcjeG2hbn2cXouRp6Ss1Js0yXYyHhhCFL1SOLNMyftpLUSicVlKmdte5B0WrVfzCg/640)

使用场景

想必各位师傅和作者一样在护网期间作为蓝队猴子🐒蓝队成员、应急响应事件中作为现场工程师或是作为安全驻场工程师的情况下，经常会遇到安全设备可疑流量告警事件。其中原因多种多样，可能是服务器中了挖矿或者其他病毒，可能是鼠标动了之红队大佬上线，也可能是稀烂的系统开发商写的代码不行产生的误报，这个时候肯定不能对其放任不管，不然出了问题扯皮事小进去事大，各种恶意流量的分析网上许多大佬都有分享，而本篇文章则是分享用于护网or应急响应事件中针对可疑流量使用Wireshark进行排查的方法和思路。

![](https://mmbiz.qpic.cn/mmbiz_png/N2vfpRNU8pAITZd4qAicYWBGcjeG2hbn2cXouRp6Ss1Js0yXYyHhhCFL1SOLNMyftpLUSicVlKmdte5B0WrVfzCg/640)

什么是wireshark

Wireshark是一款主流的网络封包分析工具，可以截取各种网络数据包，并显示数据包详细信息，常用于各种网络故障分析以及安全事件溯源取证。

![](https://mmbiz.qpic.cn/mmbiz_png/N2vfpRNU8pAITZd4qAicYWBGcjeG2hbn2cXouRp6Ss1Js0yXYyHhhCFL1SOLNMyftpLUSicVlKmdte5B0WrVfzCg/640)

安装wireshark

Wireshark直接在官网下载就行，下载地址:https://www.wireshark.org/

安装没有什么难度，下好系统对应版本后一路选择next就行，需要注意的点是Win10系统安装完成后，选择抓包可能不显示网卡，需要下载win10pcap兼容性安装包，下载地址:https://www.win10pcap.org/download/

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EqMwaEZz0ykuqJbqw6ibIREDZnzviaoty2raFtKfIj8KZR0t5UhwCyQynxicgLicnMp0STkHsLf6zSrsVA2IyVOR1A/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/N2vfpRNU8pAITZd4qAicYWBGcjeG2hbn2cXouRp6Ss1Js0yXYyHhhCFL1SOLNMyftpLUSicVlKmdte5B0WrVfzCg/640)

使用wireshark对可疑流量分析

下图是一张用于举例分析的设备告警可疑流量抓包截图，初步不难看出图中的服务器已经建立了稳定通信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykuqJbqw6ibIREDZnzviaoty2icHFf2MPvsI0VHzNCRhHSicCWu79D4QHtVPRguSMGTpl7njmIoAa0VNw/640?wx_fmt=png&from=appmsg)

本文的排查思路大致为：

1. 查看dns流量的一些解析特征来判断该可疑流量的告警是否为真，大概是什么事件
2. 然后通过查看http通讯中的tls流量来分析该次事件中发生了哪些行为，从而确认事件的具体情况
3. 通过威胁情报平台对猜想进一步确认，提供佐证材料
4. 进一步过滤http流，查看流量包的具体信息得出本次事件的结论
5. 形成报告

### 一、识别可疑的DNS流量

在过滤器中输入dns，会显示相应数据包来查看dns流量

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EqMwaEZz0ykuqJbqw6ibIREDZnzviaoty2BelguAtNc9auVNEUlZ8TXkPzzrx2bIYLd6p4dic0E5RtKMydp2vCXDA/640?wx_fmt=jpeg&from=appmsg)

这里可以看到两点：

1. 主机（10.10.23.101）通过DNS查询了api.ip.sb.
2. DNS解析服务器（10.10.23.1）通过多个IP对其进行响应，其中包括一个Cloudflare地址（全球最大的DNS服务商）

这其实是一种危险信号，初步可以判断主机（10.10.23.101）是受感染主机，因为api.ip.sb是一种IP检查服务，恶意软件经常使用它来在访问 C2 服务器之前确定其公网IP是否存在于沙箱中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykuqJbqw6ibIREDZnzviaoty2ZjmibXYm8qEv8TSlpdEJQkRU9XEP67jdH7cFicUiagRKmI7OUjRPhxK7w/640?wx_fmt=png&from=appmsg)

### 二、检查HTTP通讯

同样还是在过滤器中输入http || tls，查看tls流量的相关数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EqMwaEZz0ykuqJbqw6ibIREDZnzviaoty2r7uZ0Lcd3szT48SgUkxXyeBqXb5Xrnx89UZNTTgQqKR3q6R4D7uomQ/640?wx_fmt=jpeg&from=appmsg)

（图中没截完整，HTTP/X...是HTTP/XML）

过滤之后可以发现：

1. 受感染主机（10.10.23.101）向服务器（188.190.10.10）发送了重复的HTTP POST请求
2. HTTP/XML的使用表明了结构化数据泄露，而有效负载大小的增加暗示了数据逐渐泄露
3. 服务器响应 200 OK，确认数据传输成功

### 三、发现C2通讯

深入研究 TLS 流量后，可以发现：

1. 与 Cloudflare 服务器的 TLS 握手api.ip.sb.
2. 通过api.ip.sb，呼应了恶意软件在发送被盗数据之前会检查其公网IP的理论。
3. 频繁向服务器188.190.10.10（可能是C2服务器）发出 POST 请求。
4. 间歇性出现“100 Continue”消息，表明服务器需要更多数据。
5. 逐渐增加数据有效载荷，这是正在进行的渗透的明显表现。

那188.190.10.10是不是C2服务器呢？请看微步情报

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykuqJbqw6ibIREDZnzviaoty21p8ib7cQDQZ6ib5ibNicUn7tZZUejRTTWccZJaFstmdUP3mzAMtIYQP3UQ/640?wx_fmt=png&from=appmsg)

也可以通过Virus Total进行查看，VirusTotal也是恶意样本分析人员常用的分析平台，而且免费！

官网地址:https://www.virustotal.com/gui/home/upload

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykuqJbqw6ibIREDZnzviaoty2WJYRbeQgiaIV1uCmQyug9LOVcNQsxxicnDhCWQcklhdgrbN6nom3H8hg/640?wx_fmt=png&from=appmsg)

不难看出同样被标记为恶意，那该服务器大概率为C2服务器了

### 四、跟踪HTTP流

为了进一步验证猜想，我们在wireshark中过滤了post请求并跟踪http流

在过滤器中输入http.request.method=="POST"

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EqMwaEZz0ykuqJbqw6ibIREDZnzviaoty222vEL6xKDQPTzzZNxYzqichx9w0VUl4qeyWMlNvAWqxvBU7waoaFo3g/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EqMwaEZz0ykuqJbqw6ibIREDZnzviaoty2yYFqmb19nHZNdrRkPGTe8SO1icM4lzqMzFkfN1YULqJBcfhibTfibVkHg/640?wx_fmt=jpeg&from=appmsg)

OK,可以以下得出结论：

* 本次事件为服务器感染恶意软件造成的数据泄露
* 受感染的系统 （10.10.23.101） 正在向 C2服务器188.190.10.10 发送被盗数据。
* 恶意软件使用 XML over HTTP，这是一种常见的秘密泄露方法
* 恶意软件可能在窃取数据之前检查了系统的公共 IP，这通常用于逃避沙箱检测

![](https://mmbiz.qpic.cn/mmbiz_png/N2vfpRNU8pAITZd4qAicYWBGcjeG2hbn2cXouRp6Ss1Js0yXYyHhhCFL1SOLNMyftpLUSicVlKmdte5B0WrVfzCg/640)

总结

通过以上几步的排查，可以搞清楚判断本次告警的原因以及处置方法，结合恶意流量分析能更快地找出问题所在。阻止未经授权的外部请求 – 限制对公网IP的检查服务和类似C2的流量的访问。通过应用这些措施，可以更快地检测和缓解类似的攻击。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykH1KHFqibib8xIJtOkJbKW7UIiapCYNUtnwa99blUPhUWE1X554Q7GCRtPLghVWT4WvT4D8OEMvtVHQ/0?wx_fmt=png)

CatalyzeSec

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykH1KHFqibib8xIJtOkJbKW7UIiapCYNUtnwa99blUPhUWE1X554Q7GCRtPLghVWT4WvT4D8OEMvtVHQ/0?wx_fmt=png)

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