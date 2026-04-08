---
title: 硬核实战！在openEuler 24.03上纯手工编译VPP，踩坑与填坑全记录！
url: https://mp.weixin.qq.com/s/3JQJ809AQDiw-iTHE921eA
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:35:46.580582
---

# 硬核实战！在openEuler 24.03上纯手工编译VPP，踩坑与填坑全记录！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9j14GSZeRZbZdtpduMS2qu88It5HtBIgwzLcfhwYLbCttCMq9D7B8yohwibQmA2rYdicYsicc0NibaONibufDHsUjic0bzDFAqnibuSgN1x5dUS20c/0?wx_fmt=jpeg)

# 硬核实战！在openEuler 24.03上纯手工编译VPP，踩坑与填坑全记录！

原创

衡水铁头哥
衡水铁头哥

铁军哥

![]()

在小说阅读器中沉浸阅读

前言

想在openEuler玩转VPP却无从下手？这篇保姆级教程请收好！详细解析依赖安装、软链接修复、网卡接管及持久化配置，助你打通国产操作系统高性能网络的任督二脉。

我们之前介绍过CentOS安装VPP（[不用半小时，最快8分钟即可在CentOS上完成VPP的部署](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458846241&idx=1&sn=c6162c3d6b57f18e9d46394babc90639&scene=21#wechat_redirect)），也介绍过Ubuntu安装VPP（[小白也能玩转VPP！Ubuntu 24.04使用APT极速部署VPP](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458859828&idx=1&sn=acaa6c88ce14af772200b380d615a73f&scene=21#wechat_redirect)），对于性能优化做的比较好的openEuler（[还得是华为，OpenEuler打流能到37 Gbps](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458848712&idx=1&sn=12d90786618d329e0f3d23ebc0c65375&scene=21#wechat_redirect)），我们好像还没有做过安装部署。

而且，我们之前说是要编译安装（[CentOS迁移指南：在Ubuntu上从零编译部署VPP+DPDK，解锁Ubuntu网络性能！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458859808&idx=1&sn=0d38b6338a3bd85643e0e6731c66fe8b&scene=21#wechat_redirect)），实际上还是通过软件源安装的。巧了，openEuler的软件源里压根没有VPP现成的二进制包，想用？只能撸起袖子自己纯手工编译！

今天，我们就使用openEuler 24.03（LTS），简单演示一下如何部署VPP。内核版本为6.6.0-28.0.0.34.oe2403.x86\_64，CPU架构型号为Intel(R) Xeon(R) Gold 5218 CPU，搭配8 GB运行内存，网卡型号为Intel 82540EM（e1000驱动)千兆网卡。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbBXAemM2IYaUTu4b4Gu38b6UdhBI9Qcib4ImJfibn6XEgHH3fKzNpdfPLViafXgaNpxxcicKpygj3E9XXoVbLwfsVxvuicibZOY3LC0/640?wx_fmt=png)

在配置VPP之前，我们需要准备编译环境和内核开发包，以及DPDK绑定工具。首先，我们在服务器上执行初始化操作，一口气把依赖包全部怼上：

预览时标签不可点

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