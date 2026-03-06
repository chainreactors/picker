---
title: 一个网站治好你面对流量分析的头疼！
url: https://mp.weixin.qq.com/s/R3CLu_Tx4nOIQn4GEYnykQ
source: Doonsec's feed
date: 2026-03-05
fetch_date: 2026-03-06T04:02:41.529102
---

# 一个网站治好你面对流量分析的头疼！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DRNXoxlicJJuk9CVmolSfWYfIMtypWRopdNwPwibhFExy0ZapkTNrUMXR96WIYzV2HV9eTMqpHY0Qb9jwz1e1I8J75H9PRwO5WsOqgfW8Nib2o/0?wx_fmt=jpeg)

# 一个网站治好你面对流量分析的头疼！

原创

CatalyzeSec
CatalyzeSec

CatalyzeSec

![]()

在小说阅读器中沉浸阅读

正值两会期间，许多单位需要人员参加重保值守，想必有许多蓝队人员正参与其中；最近也有许多CTF比赛正在举办，各位是否都有参加呢？在这些活动中，大家或多或少都会遇到PCAP文件包需要去分析：

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJuEichspyML2II2MwKx1MviaYLeP0t4xFguQFVy7UibH3bKl2tF2wuIBXEf2m2LAb0LDJQsemddfMib2ZicnmMq3ZtN3tKoWDnUjshA/640?wx_fmt=png&from=appmsg)

面对大量的数据包，wireshark的检索用得又不那么6的总是会很头疼，这里就向大家推荐一个网站：

```
https://apackets.com/
```

A-Packets它是一个网站，让你可以直接在浏览器中进行即时 PCAP 分析,只需要上传PCAP文件，几秒钟内即可可视化网络流量、对 IPv4/IPv6、HTTP、Telnet、FTP、DNS、SSDP 和 WPA2 等网络协议的全面洞察。用户可以通过此工具轻松查看网络通信的详细信息并剖析数据传输的各个层级。

话不多说，接下来就和大家讲解下如何操作使用：

点击Upload My PCAP，然后再点Upload From Device上传你想要分析的PCAP文件

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJtFksH9FjAtZDpqwCJMlVPRliaAgD4U8qmczTzhv9WL71Xtl8JZ77Yg0R81lbyfeVw1ibK2XJhF3Y4Ed3MibJqjWmYiahKWtNBfaIg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DRNXoxlicJJs0GN0X7PXZYhlWIt15oy48X1JkIsiadmC90HAUU9xkPkkGmFKkBFia93p9ImWNd0Kbia9JLRn1CRw2XsHBp2pqAmniah2cN6t5S2c/640?wx_fmt=png&from=appmsg)

值得注意的是，免费版会让你的文件和分析报告将公开可见，如果上传的文件存在隐私或敏感数据的话还请停止或者付费使用

此时它会读条来分析并生成报告

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DRNXoxlicJJuSNXuZqUdmicoMzQT6J8k41UiaVI6KiaJoY8ztqKwghh1zX49b22pxAEgmmVYGANHYnWNaHEIFdDIUwPzPmTxhQhtbU8U3NdmsMI/640?wx_fmt=png&from=appmsg)

这里我们上传了一个CTF流量分析题中的PCAP文件来做演示，题目是需要找到攻击者入侵利用的何种漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJsZAKJngTlRGfz0KKXu1Vf9cSoH9ia9DjNdicHP2r362cWibO0g64siaPC3h7UqGWN6xy5yYewPXdkuBKuTT6c4JJ8ic80BnFjnwav0/640?wx_fmt=png&from=appmsg)

可视化的查看各个IP开放的端口与服务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DRNXoxlicJJsbiaCwiakJOJxe8cyBHeIp0XF551giabTlcicIER73pTRl9ECZsDGcLQV9Deb3eNc2XpKiaDHlAppt7TClIpJDaJOx1MONH6ibQLupI/640?wx_fmt=png&from=appmsg)

还把所有数据包按请求类型分类，可以自由筛选查找各个数据包的内容

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJtRyxqyD7yIg9zXlFAwNxBPicPMWSuibsppqDaic5s00rvcqMMqghC7TEe93vicoLQ48Gib6VznnhHzrRibM0xCbmqdI6spUZRnfCO58/640?wx_fmt=png&from=appmsg)

这里我们直接筛选POST请求包就看到了攻击者所构造的payload，直接扔进AI就知道了利用的漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJuhibeCibTNZdTiaQTpia0XRW4ibF9E3nKEOX1LhN6icr8SZaWHc4CdmGJjHLfiasg2ajVmvpvgATMKDzNfZmr4pm1U21ZrGWzUrszRyc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJvkKq1fPlLelEsnJ0Qw8fqRvNM8ibUjvYiaKYPtEEYBA5NicEgmzibVPxibdUwn0KTugnqhC2lHtEUTpbhmjY1icANgL7JHs3aHHT89A/640?wx_fmt=png&from=appmsg)

除此以外，A-Packets它还可以：

* 查找网络设备
* 收集 WiFi 数据
* 从 SMB 和 NetBIOS 广播数据包中挖掘 LAN 信息和用户凭据
* 跨多个协议的密码和哈希发现等

我们还可以在https://apackets.com/pcaps中查看其他人上传的PCAP文件来分析学习。

预览时标签不可点

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