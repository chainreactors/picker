---
title: 1.47 Gbps跑满带宽！Ubuntu 26.04下WireGuard性能暴力实测，OpenVPN真的香不动了？
url: https://mp.weixin.qq.com/s/Vr36QdFgFjb1QoIFKBXKyw
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:35:46.717990
---

# 1.47 Gbps跑满带宽！Ubuntu 26.04下WireGuard性能暴力实测，OpenVPN真的香不动了？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9j14GSZeRZZCsnqpODGfntDcQ3TlFZ534GNWdZDHE9QdrMe7AZVrML7tDcCIQYQagtrhbR3Pqzn53VdZ3qnDDWkygJm1r1N0KHmRZjHy4FE/0?wx_fmt=jpeg)

# 1.47 Gbps跑满带宽！Ubuntu 26.04下WireGuard性能暴力实测，OpenVPN真的香不动了？

原创

衡水铁头哥
衡水铁头哥

铁军哥

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

目前看来，Ubuntu 26.04上手几乎没有任何难度，之前的很多基于Ubuntu 24.04的经验都可以直接拿来用。

例如，我们可以直接复刻KVM部署（[手搓KVM虚拟化！Ubuntu 26.04 + KVM 7.0.0，告别VMware的低成本玩法](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866808&idx=1&sn=721846b07067da62a8b28afa8e2d015a&scene=21#wechat_redirect)），并且在此基础上还做了优化；Server版本系统的自动部署教程依旧好用（[拒绝手搓系统！Ubuntu 26.04自动安装实战：让电脑自己“卷”起来](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866839&idx=1&sn=74a6fac0d6cc8c90635475dea333ebb2&scene=21#wechat_redirect)），而且我们还演进出了Desktop版本（[拒绝点点点！手把手教你定制Ubuntu 26.04桌面版无人值守镜像，还有隐藏福利](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866863&idx=1&sn=8eb80fe4030623217f59f261f844187d&scene=21#wechat_redirect)）。

当然，受Desktop版本网络性能比Server版本更强的启发（[Ubuntu 26.04 转发性能大考：Desktop居然干翻了Server？](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866936&idx=1&sn=910ba33249eb54c9616d78b51519a807&scene=21#wechat_redirect)），我们进一步测试了openVPN一键部署脚本的兼容性（[实测1.23 Gbps！Ubuntu 26.04下OpenVPN自动化部署与极限调优](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866998&idx=1&sn=fe99576c4e9e90fedc8c2fe265e734cf&scene=21#wechat_redirect)）。最终，平均1.32 Gbps的网络性能直接可以跑满云厂商的带宽，毕竟，大多数云厂商对于中小型用户而言，带宽只开放到了300 Mbps。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYCqriaAWGLP0dYsn0jy67ZIOxfbibve39dW8FyDxcus2oP8NA0unlfjTBkvTkrFk5CMNuseIw8hOyo3ePNZWJHxVcLj4I36TJGw/640?wx_fmt=png)

当然，我们也要考虑协议的性能，通过上次测试，我们发现TCP模式的性能数据完胜UDP，差不多能高出一倍。那么问题来了，我们在部署Ubuntu 26.04时（[Ubuntu 26.04桌面版部署](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866639&idx=1&sn=800c66f9e7446a3f52be0e5f225dc27c&scene=21#wechat_redirect)），看到宣传的使用UDP协议的WireGuard，性能怎么样呢？

同样，我们还是拿之前的一键部署脚本来测试一下（[我们的WireGuard管理系统支持手机电脑了！全平台终端配置，支持扫码连接，一键搞定](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864213&idx=1&sn=ec85efce2a3b76ba244c71ccbdc09347&scene=21#wechat_redirect)），先看看兼容性怎么样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZeMJCthNNkKWHUaXbwVOq5dBE5fncz6MJJsfaCy2gm85CkRcjzn9s6hRYfQlZ1xXJnJQNr8Q2jMTrCDOiaHjg6UicF2B57lHdKU/640?wx_fmt=png)

脚本跑起来那叫一个如鱼得水，一路绿灯直接通关。在2026年玩这种全自动部署，主打的就是一个优雅，拒绝任何手动填坑的无用功，简直美滋滋。

接下来，我们把管理节点自己和一台客户端添加进来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZafB7DicUoXibdRqwOPRRRYXafP01Jc7NIpWibPGxniamYVQOibZwd9YSBOeV0Y8lodnAKC98046HjiagnL7OlkiaWMOax7QJLTkETgIo/640?wx_fmt=png)

在创建一个连接，将两台设备管理起来。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZYDbnfUlnicPCv7rdG8J3STUVXOeOQouGPuzscwDuvH1vtSCtHxHueGDvmHLowsoAbgc4zQXgVpIw8cxNicvdSzrq4yas2j8Fu8s/640?wx_fmt=png)

可以看到，功能一切正常，两个节点之间瞬间建立起连接。

首先，在动态省电模式下，我们打流测试一下加解密性能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZyiagEjNvIFs44h6rftfM4v3hLSAcIJVWxKh2BTJLibGMKg8rUE2jIa445CP9ibjnUsN0GIMDUph6NibOibW2Uia6IO5s13cHAUzDmU/640?wx_fmt=png)

事实证明，姜还是老的辣，网还是桌面版的快，还是Desktop版本的解密性能更强，最大带宽为1.38 Gbps，而且相对稳定，平均带宽也达到了1.32 Gbps。反观Server版本，最高只有1.09 Gbps，平均带宽只有954 Mbps，差了27 %。

既然基础测试只是热身，那咱们干脆单车变摩托，直接把系统切到静态高性能模式，开启底层的涡轮增压。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYkK478VBSNC7vha5FNklxTxmuNRoiaXy65BYaTYNMIERrcJucjUVJ0yTxa2XjeKZ4sGCaH865AYrouHUQjceSMaZL77QrGibXvE/640?wx_fmt=png)

这一波大力出奇迹，实现了双增长，Server版终于找回了点面子，但依旧是Desktop依然稳坐钓鱼台，解密性能更强。Desktop版本的最大带宽达到了1.47 Gbps，提升6.5 %；平均带宽达到了1.42 Gbps，提升7.6 %。再看Server版本，最高带宽提升到了1.21 Gbps，提升11 %；平均带宽达到了1.16 Gbps，提升了21.9 %。

好了，我们再看看转发性能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZEGiaWDLhlVEwsszBexY2ibqWCw6K3ZZpw4kx0LafUeYX6vYhEHFQen9kEhibqHjSTycVyzTQr8SicAK4CaRhbTLE0C2jKaS1aIjE/640?wx_fmt=png)

Desktop版本果然是不吃压力，性能几乎没什么损失。

那就上点难度，把另外一台Server服务器作为SPOKE节点加进来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbHwe3axU8X6glG41IgBsibUUW6sIBT4diacJvzkW7a7wVmlbNL4ibjm4aBgz62Pn9gRW0nfpbXIAlgcEpc067EByTwv9fibNaVUoI/640?wx_fmt=png)

接下来，创建一个Server1到desk2的连接。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZYds8MOSDicWGNqNXH0aWjCh3kz1iadO0a3ohj0WM8Nw0rgkKcPny5LkqyicmLuPib1wZibfRPj3jLARibSAPRjHwD8fv4ZQsaDKftto/640?wx_fmt=png)

检查一下server2到server1的连通性和转发路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZCCING6p4g4pT0brFhvAiaG2Zw8mLPklib3ho7ZIuiaDMOtMFwszljFfpDZJUls36zmBU8iakCfexU1iaC8l9Fzhoiaia2OxGw9osQj8/640?wx_fmt=png)

牌没有问题，开始打流。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZZP7zHLAkDpVwOOUpIfHNEJpKdoW40IDL7PiavLCssa9KRXTt1iaJ4UAIWYmsk5cRw7tGY0bHhoCxoypCiccxnnY9xH7sh7BnxLhM/640?wx_fmt=png)

优秀啊，Desktop系统作为HUB节点同时进行加解密时，最高性能竟然还能达到983 Mbps，平均带宽能基本稳定到900 Mbps以上。

这一套组合拳下来，胜负已分。我们发现协议才是王道，WireGuard的UDP效率确实让TCP版的OpenVPN感到了代差的压力。如果说OpenVPN是位稳重的老学究，那WireGuard就是个不讲武德的小年轻，在吞吐量和转发延迟上简直是降维打击。

当然，Desktop依然是扫地僧，别问为什么，问就是桌面版的网络栈似乎自带加速Buff。

\*\*\*推荐阅读\*\*\*

[我们的WireGuard管理系统支持手机电脑了！全平台终端配置，支持扫码连接，一键搞定](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864213&idx=1&sn=ec85efce2a3b76ba244c71ccbdc09347&scene=21#wechat_redirect)

[保姆级教程：一条命令部署OpenVPN管理系统V4版，支持Win/Mac/安卓/iOS全平台接入](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864329&idx=1&sn=32eef6d6ce107136b389e05a4f206060&scene=21#wechat_redirect)

[成本省下99.7%！用40元的腾讯云服务器自建IPsecVPN，成功对接企业级飞塔防火墙](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864080&idx=1&sn=2de5d9d701d53b2c613b0c852329afb2&scene=21#wechat_redirect)

[别再乱选VPN了！实测数据告诉你：为什么L2TP是个“坑”](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865859&idx=1&sn=39ed55e57690feb1583a1a5bfb032b72&scene=21#wechat_redirect)

[SRv6部署第一坑：为什么配置了Locator却Ping不通？](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866771&idx=1&sn=cdee955a5a41b28b66e860c02ba78891&scene=21#wechat_redirect)

[嫌一键部署不过瘾？带你手搓Hermes智能体，主打一个通透](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866216&idx=1&sn=5826ca934825750b5bd102f9c53a4e2d&scene=21#wechat_redirect)

[H3C CAS实战：CVM纳管CVK的相爱相杀，这波操作太秀了！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866509&idx=1&sn=086980073d7a05ed475bbfaa788a73dd&scene=21#wechat_redirect)

[VPP转发性能从10G暴增至24G？揭秘OpenEuler虚拟机的极限压榨术](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866146&idx=1&sn=3d1d7cbcb43967a986cb3e28bcef610b&scene=21#wechat_redirect)

[NVUE不支持OSPFv3？别慌！教你一招搞定SRv6地基](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866582&idx=1&sn=fed8bd9d708523a4aa40343f84bdc511&scene=21#wechat_redirect)

[手机也能跑DeepSeek-R1/Qwen3了：零成本搭建AI推理平台](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865100&idx=1&sn=ff8219a72e9800481c1e23911037e804&scene=21#wechat_redirect)

[2048卡昇腾910C集群算力集群交付工程手册](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458863852&idx=1&sn=ac753705858b85d06703dab5c42a3856&scene=21#wechat_redirect)

[2048卡H100算力中心100G无阻塞存储网建设方案](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458862851&idx=1&sn=7eabab449575723128152249370b069a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/5fL4uXAOMM7kUuIMJ8JGRicTGrVN3LAad2qWVLSLkZvOL0KSCibicfllib6L4g7Clp5vaZUhAgWoiahdV3kAHa2Wk6A/640?wx_fmt=jpeg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5fL4uXAOMM65ich03QCp6qic3cwTmicnHZA49U7FN4y6cb4bY57OvvctIZH4ftcY5quyNfmPOvACGfVU5upxylUnQ/0?wx_fmt=png)

铁军哥

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5fL4uXAOMM65ich03QCp6qic3cwTmicnHZA49U7FN4y6cb4bY57OvvctIZH4ftcY5quyNfmPOvACGfVU5upxylUnQ/0?wx_fmt=png)

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