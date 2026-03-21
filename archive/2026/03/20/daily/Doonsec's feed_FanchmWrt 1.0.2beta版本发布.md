---
title: FanchmWrt 1.0.2beta版本发布
url: https://mp.weixin.qq.com/s/52G6d_fHrGMMkEqbrgULrQ
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T03:59:22.077480
---

# FanchmWrt 1.0.2beta版本发布

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/raicmpgShpRlPnhm2aonopicRIJz14QdNuJLDADdPRBOibliaDRLiaMBb1XUOefsZqIxfxmtE3007f6XNypLI29rogNSUxVicsSjnpFaysJEEFP7I/0?wx_fmt=jpeg)

# FanchmWrt 1.0.2beta版本发布

原创

TT
TT

OpenWrt

![]()

在小说阅读器中沉浸阅读

前段时间OpenWrt官方发布了25.12稳定版本，立马就有用户开始催更了。 为了让大家很快的用上对应的FanchmWrt版本，也基于OpenWrt 25版本进行了适配。

FanchmWrt已经有一段时间没有更新了，并不是停止了开发，最近在开发FanchmWrt的一些重要特性，这些特性工作量非常大，目前还在开发中。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRlG2CPYtL2uIcicswks17B14Vy9UapGLcQfln2Iics40icu6f9kSWM2tzxIHnmeVtKQ5ibUXTpyzcznpfD6NsI63ZO8OMTra4ib3lYQ/640?wx_fmt=png&from=appmsg)

此次更新并不是只切换了OpenWrt版本，也增加了一些功能。

以下为FanchmWrt更新的主要内容，版本号为1.0.2，目前还是beta版本。

1. 增加会话数统计功能

> 可以查看最近一段时间的会话数，最大可以保存一天的会话数记录，会话数对于路由器来说非常重要，很多时候网络卡顿都和会话数有关，目前还只有全局的会话数统计，后面还会开发用户会话数历史记录。基于用户的会话数需要基于内核实现才能达到高性能，基于IP查询的方式实现会影响性能，特别在会话数超过1w的情况下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRnRO4eg6pA6SvVmul6EMFia4qB7PQarjPA99EGKcficnibDj1zZXRicS7adltOV1vnmzk0y4q8bEQOnvjfowbrYnZ2NWAyW82AV9JI/640?wx_fmt=png&from=appmsg)

2. 增加终端上下线记录功能

> 通过该记录可以大致了解用户的行为，比如可以监测到小孩或者老人是否在家，后面可以结合一些通知机制实时感知终端上下线行为。这个功能是一个粉丝朋友提出的需求，我一开始觉得这个功能没什么用，后面才明白可以用于监控小孩老人回家的情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRkRI78T89nfzDNSGflU8lywN2ibictoIFIRV44km0ERFFajiaqPTvDYF3k7qqpOr3TonicHa8ncw0MhAiayokohGY85hE8jRKmov4rw/640?wx_fmt=png&from=appmsg)

3. 适配OpenWrt 25.12.0版本

> OpenWrt 25.12.0版本已经正式采用了apk包管理，由于一些第三方插件或者软件源还没有更新到最新，所以如果升级OpenWrt 25.12.0版本可能无法安装一些第三方插件，只能安装OpenWrt官方的插件。 如果你有其他插件需求，可以用24.10.4版本，此次也发布了对应固件。前几天官方又发布了25.12.1，由于固件已经编译出来，beta版本先不做切换，正式版本会切换到最新，这只是小版本变化，修改点不多。

4. 优化FanchmWrt主题

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmn6eHseofm14tYibic6X8wDhoxjx9ibOpeKVaCVtDHicj5zrOdibL7XXn9fGVTSKDic81ibo9iaZOW9sDKylWjq4X4cYAZLVEy17R3ISU/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmrjnlFYyfk8mEtE0zyoDcDd4oGFSrN6HLm4GwddBzwZy6tia4a1Tj0icwKWCn2y2gvU7GiacotMjcluZN1EdcmT1DcibuX1hthPuo/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmw0l7sBiaAdQQSs2HTjSdFhrYDbvriaK1D0fqsb7z9pgm2e7iarfGYKLBosL2ZyIk34xc1c68YkNkZia9GDhLpavmy5yryjGpNfAY/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRmDaR9N7rDS9KBfrsCdJxuqWhV0gT1sTthKBnhyDJ39tsypAdEgraOsgtNCRrUYBEfpOMGsU31X13nKL3CQBKdMJkZCtf5Olp4/640?wx_fmt=png&from=appmsg)
5. 优化应用识别模块并修复一些BUG
6. 发布一些新设备固件

> 新增的设备包括磊科N60 Pro、GL-iNet AX1800、360v6、raxda瑞莎系列等。 最近也基于OpenWrt主线编译了JD无线宝系列固件，包括亚瑟、雅典娜、太乙等，目前还在测试中，毕竟是主线非稳定版本，需要多测试看看有没有问题，后面会对一些热门型号发布snapshot版本。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRkFa1lOSEsBv01nCyBXp9Wbtmw5U1D5QI0gqYtsLSVRbnMZFCsSiaEpGxKDibib73CYIYazYlcTRuMljUo2INqvbxpa3mXI2PCm8Q/640?wx_fmt=png&from=appmsg)

以上为此次更新的内容，固件已经上传，可以通过官网下载。

www.fanchmwrt.com

最近也对下载页面进行了优化，可以进入每个产品详情页，里面有一些对应的注意事项，比如刷机、升级等，后面还会贴上一些刷机参考教程，毕竟还有很多粉丝不会刷机。 经常有粉丝留言需要现成的设备，等系统稳定后我考虑提供一个购买渠道，不定期弄一些刷好系统的设备给大家。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRlXYRCVWvI9DGsea86pfibJ9afibs5Nbqrmicvx13tqWnY6Slg95drjC8DJeNZLacwvoloa98QysuVNnvXl9Hb8YzaDc8Gib3EdOPI/640?wx_fmt=png&from=appmsg)

### 关于升级

如果你之前已经升级了FanchmWrt固件，可以下载新版本通过页面直接升级，注意x86或者arm盒子之类的产品，要区分是否是扩容版本，扩容版本和普通版本无法互升。

由于FanchmWrt是基于OpenWrt主线源码修改，一些MT798x系列的固件是itb格式的，对于新手来说可能还不清楚如何刷入itb固件，为了方便大家刷入后续也会适配老版本的bin格式固件。目前已经对jcg q30 pro和h3c nx30 pro两款设备进行了适配，可以在不死uboot页面中选择factory.bin固件直接升级。

对于最近比较火的cudy tr3000，加入了一些usb驱动的支持，用于适配随身WiFi，并且25.12官方固件已经兼容了128M的新版flash，所以在升级时不用再区分flash。

### 关于发展

FanchmWrt的目标在于打造一款家用防火墙系统，在用户体验上对标商用路由器，标准的路由器功能后面都会增加，所有新增的功能都是经过系统级评估和设计，而不是简单的引入第三方插件，FanchmWrt目前已经有上网行为管理、用户管理、上网审计等功能，属于比较核心的模块，集成这种大模块之后固件只增加了不到5MB空间，小型设备固件控制在了12MB以内，X86固件也才20多兆。并且系统对内存的要求非常低，128MB内存足够稳定运行系统。

### App管理

FanchmWrt部分代码基于OAF应用过滤开发，所以在FanchmWrt无法再次安装OAF，目前FanchmWrt无法通过OPAssistant手机App管理应用过滤功能，但是基本系统状态时可以查看的。

如果有迫切的手机App管理需求，可以先用OAF固件，后面会专门针对FanchmWrt开发App。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXzGicyDpyliaicXribaVDSAXgstaTs5sichcfKuY9tGRhzWoicFGESJdpTLOcENlJerVaYMk4C3RuibWiaxUw/640?wx_fmt=png&from=appmsg)

最近将OPAssistant iOS手机App提交了审核，等了2个多星期才开审，最后说是有其他用户用了类似代码被拒，然后导致我这边也无法上架，还在沟通中。所以如果你已经用上了OAF最新版本，目前还无法通过App管理。

前段时间也对OAF源码进行了更新，加入了一些新特性，后面会详细介绍，这些特性综合考虑了大家提出的需求。

### 关于源码

此次更新的FanchmWrt源码会在1.0.2版本正式发布后提交，同时会将默认分支切换到25.10，有github账号的可以给个star。 https://github.com/fanchmwrt/fanchmwrt

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4dGgALU2VXwGPhSnjG6IhzI0wCrUicApDmpsL1c5VyoWFph6dicu8RydO8StibF1ibHIF7zOeAUrz31GPo9UGqNOTw/0?wx_fmt=png)

OpenWrt

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4dGgALU2VXwGPhSnjG6IhzI0wCrUicApDmpsL1c5VyoWFph6dicu8RydO8StibF1ibHIF7zOeAUrz31GPo9UGqNOTw/0?wx_fmt=png)

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