---
title: 【知道创宇404实验室】警惕 Unix 系列 CUPS 多个安全漏洞最终可导致远程代码执行
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650988745&idx=1&sn=7614cfdb45e03ac394179c55a5ecb303&chksm=8079a2fbb70e2bed49da87ac41567a61d9448264392ab96640bf673f06aa62f0b09c233cc28a&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-09-28
fetch_date: 2025-10-06T18:27:22.959375
---

# 【知道创宇404实验室】警惕 Unix 系列 CUPS 多个安全漏洞最终可导致远程代码执行

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0JxgeIdgoLPAI0T5lovVDwfhx036IDManzRE6GoolzEwW9tuf00tiaHGFMXArFkCSgiaXvicpwod3icA/0?wx_fmt=jpeg)

# 【知道创宇404实验室】警惕 Unix 系列 CUPS 多个安全漏洞最终可导致远程代码执行

404实验室

知道创宇404实验室

CUPS（Common UNIX Printing System）是一个开源的打印架构，广泛用于类 UNIX 操作系统，CUPS 采用互联网打印协议（IPP，Internet Printing Protocol）作为其核心协议，这使得它能够在网络环境中高效地管理打印任务和打印机资源。

近日有国外安全研究者宣称其发现关于CUPS的多个安全漏洞**（CVE-2024-47176/CVE-2024-47076/CVE-2024-47175/CVE-2024-47177）**，影响广泛并可导致远程代码执行。知道创宇404实验室留意到，9月26日该研究人员发布了相关漏洞细节及漏洞演示，并且我们注意到PoC已经公布，攻击者可远程（无需认证）通过cups-browsed进程监听（默认631端口）发送恶意UDP数据包，最终在目前系统上实现任意命令执行。

值得注意的是，该系列漏洞可通过互联网进行攻击，**通过知道创宇旗下全球著名网络空间搜索引擎ZoomEye统计，曾经有大量（百万级）的系统对外开放了CUPS服务，近一年也有约18万资产对互联网开放了CUPS服务。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0JxgeIdgoLPAI0T5lovVDwJka4pOE0lwoYURkCquHCwJdOv4wOvzGkdkEeDpVvonTmC4mqfgrXMw/640?wx_fmt=png&from=appmsg)

另外，该漏洞细节存在提前泄露的可能，所以我们建议大家注意排查相关服务器安全，修复防御漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0JxgeIdgoLPAI0T5lovVDw2eJElNGjfqz5bTDPsibmib6W9pQroXzxIwKVvUMKHGKkBOTGYoJXvuWA/640?wx_fmt=png&from=appmsg)

**临时防御方案：**

目前各操作系统官方补丁还在开发中，可通过临时停止相关服务（cpus-browsed）进行缓解该系列漏洞。

**相关参考：**

https://www.evilsocket.net/2024/09/26/Attacking-UNIX-systems-via-CUPS-Part-I/

https://github.com/OpenPrinting/cups-browsed/security/advisories/GHSA-rj88-6mr5-rcw8

https://github.com/OpenPrinting/libcupsfilters/security/advisories/GHSA-w63j-6g73-wmg5

https://github.com/OpenPrinting/libppd/security/advisories/GHSA-7xfx-47qg-grp6

https://github.com/OpenPrinting/cups-filters/security/advisories/GHSA-p9rh-jxmq-gq47

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3iahqCkYYjmw1gI9aGgwgAAqbmakWhGyibh4nQyU7npz3YyfZqosFKqfjdkRFRUwhmUwarcpQRrp0w/0?wx_fmt=png)

知道创宇404实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3iahqCkYYjmw1gI9aGgwgAAqbmakWhGyibh4nQyU7npz3YyfZqosFKqfjdkRFRUwhmUwarcpQRrp0w/0?wx_fmt=png)

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