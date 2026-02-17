---
title: Wireshark Graphs | TCP Previous Segment Lost
url: https://mp.weixin.qq.com/s/zr4Wgzzn3Kj3vjZbC9liiw
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:19:16.715748
---

# Wireshark Graphs | TCP Previous Segment Lost

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQbDG065v0DSeZxfFo4R56ZLhkBxKrMDZPnfZ2YasOgH1w56iacDoZ13yaTicZHf98W3yrib8ickS8Lic7cXZJKnvMg/0?wx_fmt=jpeg)

# Wireshark Graphs | TCP Previous Segment Lost

原创

7ACE
7ACE

Echo Reply

![]()

在小说阅读器中沉浸阅读

**一图胜千言**

**前言**

A picture is worth a thousand words，一图胜千言。基于 Wireshark TroubleShooting 系列中的案例，计划以 Graphs 的方式重新解读下，看看从中能学习到什么不一样的知识。

# 说明

本篇原文[《Wireshark TS | TCP Previous Segment Lost》](https://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247484726&idx=1&sn=2d72b05dbdda7e027697a52aa6adff44&scene=21#wechat_redirect)，数据包文件可见链接: https://pan.baidu.com/s/10wJFGd3UrIqLf1u4W431bA 提取码: j4g2。

这是 Wireshark TroubleShooting 系列中的第 10 个案例，同样说的是运营商专线 MTU 的网络故障，图示分析与上一个案例大差不差，姑且研究一下。

分析

问题回顾：远程用户通过 ISP MPLS 专线连接至远程分支机构，通过浏览器尝试访问位于远程分支机构的某系统管理页面，但未能成功，而本地用户访问则正常。检查网络层基本连接正常，从远程用户 PC 到系统服务器 Ping 成功，且 Telnet 80 端口也正常，但是 Web 浏览时请求图形数据时不起作用。

我合并了连接不正常与正常时的两条数据流到一个文件中，主要数据包视图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib0JGGXPqNaibAe493trIampmWWMrbc6MT7aKXZ22HqVCgVwLGdLBDia6BWPAiclwIYbfg4QmicBkNPh65VqMyUiatnIlbsYuFgOibUTuvHIoNN0n0/640?wx_fmt=png&from=appmsg "1")

针对不正常连接的 TCP Stream 1 ，打开 Sequence Numbers(tcptrace) 图，如下服务器端->客户端方向，可见有不连续的数据段，也就是存在着序列号空洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib0JGGXPqNa8MYeMxvK8xzMmLoK7ER2ksqbyY5JHmJAG4h8tqloD2CLuQfP5TjE08PHaia2ZWSxgIZhlv1rdFBz6cibiagnaf3UnoFuQKrKaHjg/640?wx_fmt=png&from=appmsg "2")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib0JGGXPqNa9zicezt7QAXaG1GZicRGpP9JAfAF3BnwEkfqKla3XhqH2YlpevH4viaDELd361TicibBscX47sN4nRUIEyFsgicxPic4DeibD2ZlHhIDs/640?wx_fmt=png&from=appmsg "3")

继续放大图示，丢失分段大小分别如下，结合 TCP 三次握手中的 MSS 1260 ，丢失 MSS 大小的分段个数分别为 2、3 个...，同时结合之后没有重传的数据包，合理推断是由于专线 MTU 问题，造成服务器端至客户端传输方向受限，无法传输高于 PMTU 大小的数据包。

![](https://mmbiz.qpic.cn/mmbiz_png/ib0JGGXPqNaibKpnPd9rhN7WHY9niaAicaFJuB1VkiaQrtXdULQBnVSm5tXgqfgAYPNbicEaLPWnhTLZO6M7A3W7ESu8BViavuOEsdRaSkjNRTKeFM/640?wx_fmt=png&from=appmsg "4")

当然从 Throughput 图表也可以看到，在服务器端->客户端方向，所能看到的最大数据段的长度也就是在 600 字节，没有 MSS 大小 1260 字节的数据段。

![](https://mmbiz.qpic.cn/mmbiz_png/ib0JGGXPqNa8UQR2I4uvByeMZDNoG6Km4Wsial5ibaXjicyo538w6Gb0jJUHI6K3rOzZyHdSmIWKLU9Hc7dUGZeIHJJfQnbsFxxKSBicTVquDt14/640?wx_fmt=png&from=appmsg "5")

而正常连接的图示如下，对比以上问题图，可以看到存在一定区别，连续传输且所能传输的最大数据段的长度为 1260 字节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib0JGGXPqNaibY9IWA0CibJFZkooLpFlxC1gBdSwXwHiafNRXoU2WFAibHfa3Fqotf5Q6FTvtbbt96YgEGOTr5ZTyicfpSlHbMAGcjd49Dj9ms48w/640?wx_fmt=png&from=appmsg "6")

![](https://mmbiz.qpic.cn/mmbiz_png/ib0JGGXPqNaibUjpsY7SZdxy59xibYbYAN0ibjQ5pAibMC0p5vfF8bZEl0gqlo8bUtmx72VUnVAVpKped21kHsRpaib1UBWanM2ftKCCmDTib09ITU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/KCDuITyP0VzfbZbuFfydjXgw7OS0xORQQfcvhmj5BiavdvJibDd5GCjpbt4TgsuTPaCFF9CPwvSkibTgcaiaE0TMew/640?wx_fmt=jpeg)

**往期推荐**

[1. Wireshark 提示和技巧 | 捕获点之 TCP 三次握手](http://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247486731&idx=1&sn=60629500b326a2d52b19c0bbafc3c913&chksm=90bf6104a7c8e81263136212efa62c0cc7fde6a0239b562cc064d9c78d6907cec45c3539b044&scene=21#wechat_redirect)

[2. Wireshark 提示和技巧 | a == ${a} 显示过滤宏](http://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247486344&idx=1&sn=fc6ecf75177d9ec673ab298fd5fbad3b&chksm=90bf6787a7c8ee91a8e38dc41dc075df9246a0a6a9e43eb8c4f0c564f7eec9bd03e933a1961f&scene=21#wechat_redirect)

[3. Wireshark TS | 当超时或快速重传遇到零窗口](http://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247487521&idx=1&sn=6e5f38bdb9e74215f2367c8492103b3a&chksm=90bf7c2ea7c8f538d3cfbc253387db987448a9873568ac176f043c891033041f1b61453762c1&scene=21#wechat_redirect)

[4. Wireshark TS | 防火墙空闲会话超时问题](https://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247490326&idx=1&sn=35d8b825ab50625613e1b5aa56be213d&scene=21#wechat_redirect)

[5. 网络设备 MTU MSS Jumboframe 全解](http://mp.weixin.qq.com/s?__biz=MzA5NTUxODA0OA==&mid=2247487486&idx=1&sn=955c51224fff4ad7726fb5781725eb79&chksm=90bf63f1a7c8eae744f94775d8a337f2d93751247f0967a8d177e17018928af556dc41a44dee&scene=21#wechat_redirect)

后台回复「**TT**」获取 **Wireshark 提示和技巧系列** 合集

后台回复「**TS**」获取 **Wireshark Troubleshooting系列** 合集

如需交流，可后台直接留言，我会在第一时间回复，谢谢！

![](https://mmbiz.qpic.cn/mmbiz_png/agnuXVkibSpmhZ13T6zj8IgQqQGEzj2oVFDgd2JJqtgGAnVSv9ZJcfefwuGBDOezBe61U2owxeiae0G1tOVicF1wA/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/zQbDG065v0CFgZmsrrTCCGgN9lfhcDv40bmxd2hlX7CI9lbhvPwpLYTCnkG6ONQS5rBH5AySKvJM9Z7sLrmnWw/0?wx_fmt=png)

Echo Reply

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zQbDG065v0CFgZmsrrTCCGgN9lfhcDv40bmxd2hlX7CI9lbhvPwpLYTCnkG6ONQS5rBH5AySKvJM9Z7sLrmnWw/0?wx_fmt=png)

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