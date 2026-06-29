---
title: FanchmWrt 1.0.3正式版发布，增加应用中心，行为管理支持上网时长和流量控制
url: https://mp.weixin.qq.com/s/qcLfIVy3ZudEwCsSWlKcbQ
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:33:56.236606
---

# FanchmWrt 1.0.3正式版发布，增加应用中心，行为管理支持上网时长和流量控制

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/raicmpgShpRkpGFsia283991t9YS24cL5vpI4gqic4NuJfWVKIwlgu8vrL5Kuiar8Z9LOGwqmAUSucTYOtw6iao2UqLwrvttmSMt7E5ca4nsnPRY/0?wx_fmt=jpeg)

# FanchmWrt 1.0.3正式版发布，增加应用中心，行为管理支持上网时长和流量控制

原创

TT
TT

OpenWrt

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

大家好，经过2个多月的开发，FanchmWrt终于迎来了新的正式版本，版本号为1.0.3，OpenWrt基础代码切换到了最新的稳定版本25.12.4。

由于这次加了很多新特性，所以开发时间会比较久一点。经过这次版本发布后，后续更新频率就会加快。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRn5Ptd5hm2UQPjqBySWMgiao94fTicWficuhNliaNX1DDEG5XhtC5v2vvLBZGBkA7qpgDKlQWjBWJkNiat9IcicCznWeIzCb3bh0zeZ0/640?wx_fmt=png&from=appmsg)

为了让大家更直观的看到系统的功能列表，录制了一个演示视频。

以下为完整的更新内容说明:

1. 加入应用中心

这次更新的最大亮点是加入了应用中心，可以通过应用中心安装作者开发的精品插件，都是占用空间极小，但是非常实用的功能。

比如当前加入了用户会话数统计、应用历史记录等，有了应用中心，后续可以不用升级固件就可以体验新的功能，非常方便，同时也提高我的开发和发布效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRlZbVXPulzKp9vs3bKe5P4eT6Dnf1ol1lYfbPibTINv69maeOhjgIAW7WVuNibdibtpUqSdxm7nM0UfhFPnN6tvQC99YH5noGTarA/640?wx_fmt=png&from=appmsg)

2. 支持基于每日上网时长和流量的控制

在之前的MAC过滤功能中，只能基于时间段限制，这也是目前大多数行为管理功能的标准实现，但是很多用户需要基于每日时长、每日流量进行控制，当超过每天的限制后就断网，第二天重新计算，类似手机卡每月流量和时长限制。

基于时长的限制中，并非采用终端连接时长，而是记录终端真正的上网时长，会智能检测终端的活跃状况进行统计，锁屏状态下不会统计时长。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRkxhHIOaeKXaosWqCzKcbrcZhRDOpfHgPqzqmdEmf216xNmJZicpAr2KIfBlIMgJWy33zVN37TcHbBJiallTHT38E3GfsNx4VU5A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRkWjW165MNGLnRczQlB05xicqvJPuhjICSz8Wou4c5umkzRc7DWe1H6yVkZgmQphiaDV6pRDr3qRQZicbRCoCZg6ZgcHnAy9afrVM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRnJdPu7UggsZiagLlr3CCO5fdCGu3kYuvFPrJetR3jpPyYlKIFMvicibS9EzEbFX09JhiagibmsjKjicWNPRBtpCAY4ffLPkh0MSvImw/640?wx_fmt=png&from=appmsg)

3. 应用识别优化

应用识别兼容代理模式，很多用户在系统中开启了代理，这样会导致应用识别失效，该版本已经做兼容处理。

除此之外，还增加了应用识别模式，能够识别更多的流量，提高了应用过滤效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRkyl5lRiagkkkicCzBQNht7xibkm2kuYApcy58ytPicBHdMDhIJgcyaAXIiacUdJDkswxqghJaYbdP9z8gfe3t9lflvNPOBwBROVMwk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRnUiaQBdU1SlSv9LuLdVPJboYwUwfb9O3WAI3MqIvQcqibhicKQQbOVb7ib7J2CRQyzzyOqcRXdNCemgm4FOEpBCJKbIZFyUUS3lwc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmCoZgrNPIHnyAAjoRB6Re0WmF4uMTOBv8K96nz2Dib7GQ2AJq4dJVBW6B6OHtcX73ZFOVqZmniauoMx4YaqbPWiakD4dUXibpicYQ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRm3EtrU45vUG38VGjB3jIcBiahicsZtFJdORDMS2KUvs4TKFnp3JZwgia7T0HVbrRJk8icjOaJL2hO1wZIxx8YQBmm4knu3RltE4oQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRlY4gxthxfZV228CYxCTUNXh9UanqpD5VL8m9raLjxBV5cOI8nVy5QSyWpIMsOoRzqH27JJ0mice3Ovetv6d1CH1e4zLhIrJb6w/640?wx_fmt=png&from=appmsg)

4. 上网黑名单

增加了上网黑名单功能，黑名单相对于MAC过滤来说，更加严格，不会随着时间变化而调整，只要拉黑，任何时间都无法上网。在终端列表可以一键拉黑，而不必新建一条MAC过滤规则。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRkb4gsb6bYJ9aibyibfEfJ5Yn42L2w7H1SoicRMx4WyOv3K2wxqA3mYAzxm2YvogOuoYLCVHdeYoib9BqBhpLj3ia5syeGXricnGK6ico/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRlmlI35ruyLnPbp2uibDgkD89iaWt79jUq8EMfMb52w2hJbtQuHqMqgAicnv7N52ib0ADN0x4VO7DmZlJNlJDXA2JkicQia1zLJAaAOs/640?wx_fmt=png&from=appmsg)

5. 审计白名单

FanchmWrt的上网审计功能是非常强大的，支持详细的应用记录查看，但是有时候并不希望审计所有终端，加入该功能后就可以通过加入白名单进行排除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmTpTBNM55fcydNBiab46wiaYupdY2GItPfszbhg0xmay3czCvb7oCSb2NlH8LVDX9xMbxts9PfRvwI3kdgmrN36BCHNXeuuHW68/640?wx_fmt=png&from=appmsg)

6. 调整页面主题

本次对FanchmWrt主题进行了优化，调整了配色，在深色模式下看起来更加清晰，浅色模式也能够正常显示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRn5Ptd5hm2UQPjqBySWMgiao94fTicWficuhNliaNX1DDEG5XhtC5v2vvLBZGBkA7qpgDKlQWjBWJkNiat9IcicCznWeIzCb3bh0zeZ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRlTCiaQb1m884PuRklqjYS1cOTbaGZOc4BfgoVjP1CvGqyhFXSYYT976FYTkJ6JeaoAfldnsIiamPHhR2pQEVXyGeVY2s4TGhMqA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRlM4v4k85MVdibocGBwkamj7LHZaeQlxtVicYwKCaZadF9JfKIJtYCeEAc9sspzpoCfev9nuYkkSc3uia7ZGcYHbRxIMjBTSLpj1I/640?wx_fmt=png&from=appmsg)

7. 增加网口状态显示

在右侧的卡片列表中，增加了网口状态，可以直观的看到网口接线情况，并可以查看网卡详细统计信息。

8. 终端列表优化

在终端列表中增加了实时连接数和无线信息显示，包括无线速率、RSSI信号强度等，实时连接数依赖插件，安装后会自动显示。

FanchmWrt包含了多种行为管理规则，很多用户往往会忘记了之前设置的规则，断网了可能认为是设备出问题了，于是在终端列表中增加了实时行为管理规则监控，

如果匹配了会显示未联网或者应用受限，可以查看具体匹配的规则，在详情中还可以查看终端下面的所有规则，不用进入各个模块依次排查。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRnKzru5PQWLmNYdE0iaH9whNFRPDfVibxIqhq2tu9dwzj7dbzYxVdjAWVk1JcUOzFcPqoelkWLtIbgic7nfreibDPaaSvqau2dWCu8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRkPmiaBRMYPUB3xnndVdJGjNq613uibS7DUkNQtd0pWAE7mbCxEhQYJtCyk9v3ias5thWPOqjOKycW7EFt3B8Jgh2HK2z5IM79mkM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRkHHVuhibN4gfG20GuibkrsEyr4PTdes5eOAXaLAgibcgTHkoUpAxftXhyg89a19MtXP8LziaSPHcR2Pxlg1p3lJgTjib76QT7ahiaQQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmcOVgJY7yARHjDIt46coFDu716dLXXJOFKFkx7ccGwQXbpcTqfNHFxVpFewaAMmNDeuWxJIuibcXSyY9OGUicxWf1QXyqGvtfv4/640?wx_fmt=png&from=appmsg)

9. 用户连接数

在应用中心加入了用户连接数插件，这是基于内核实现的高性能用户连接数统计，而不是简单的搜索连接跟踪表进行过滤实现，支持ipv4和ipv6。要实现高性能，只能通过内核去实现，遍历全表一定会导致系统卡死，特别是连接数超过10000条的时候，会严重影响系统性能，在OpenWrt原生功能中，有一个连接数列表界面，连接数过多会导致那个页面非常卡甚至崩溃。

这个插件是支持每个用户的历史连接数统计的，最大支持查看最近24小时的记录，终端的异常行为一目了然。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRnwkBEIRLBnOPhZBUBHj6Ymj7mymtsp5lmTZR6y3wd6iaXIEeBUH61SVHWhc4hOw4gGxYuD9yDiavhXJDRktzf9zPxQhSvMNLQA4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRk98BazKYwBbibpX0ibDZZLH7d3Ysc9uBTmanT0ITyeTo0kRYsVGVyBvjsk0sJthQodOEaeM4g1teCqLnCgP6IPaAFJOIibOUerGc/640?wx_fmt=png&from=appmsg)

10. 应用记录支持数据库统计

这次还增加了应用记录和终端记录的持久化，引入了轻量级数据库，这样更方便查询用户的历史数据，比如应用历史记录，并且在应用中心加入了应用记录插件，可以自定义查询每个用户的应用记录，数据库存储目录和大小都可以自定义，对于x86等设备，可以将存储目录指定到磁盘，这样可以永久存储数据，也可以手动在后台导出数据库。

目前应用记录插件还只是精简版本，后面会考虑做一些报表功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRknWQQgG75TXP3cVxqk2HjRL4lFDr3IGdhCrhrJWzAib35kZw6WSNyINLibTlLmrG92hibibdVTDAKTRMbd1X7eu1tggIvl6sA2yuk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRlYum1kovVFsp5kgaMArZticJE2B7yqjcCiaKzjs5T1fnLHMPWwSJcNsyzf4s3iaeChdYjA73sxe7KsmtKsrmAmZAJIFuwnUpdrHg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRksUeEcHM5HETcVuMzmZA6rNpC8EMeZy7xEpQdb1NUbfibSQMZDblibhnrQOIhuy2J2ibWL02Jn9fsS75oULcKfP2sWuIlpW8ujdg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRleYfHlnq9HZgemz7iayB491FB1dqxB9K2JAuAtFjRicN527xnDNNOyvXcZ6Ncwc1odjI3wyrUO0t7adSvgY4EXwNEOzZjXWUI88/640?wx_fmt=png&from=appmsg)

支持的设备：

目前官方已经发布了几十款热门的设备，只要是支持刷官方OpenWrt固件都是可以刷FanchmWrt，如果官网没有固件，可以通过源码打包。因为目前还没有太多时间编译发布全系列固件，等系统稳定后会考虑和OpenWrt一样发布所有型号的固件。

热门的OpenWrt设备主要是X86系列、rockchip系列、MT7981、MT7986系列、MT7621系列等，具体列表可以在官网查看。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRmibsk58FThkoAcPwzjgABGml4ibB65zMbXiassgOrfArbzicGBYnxPmXBODt9aCCJHoP1xJA7pj0qFv9mQ2n3UQIEGtibspdkwft6I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRlLic5qxP38CWLibwRibFdJu7m2ZEFQrBuVDlD1fF7rLHTCicnZU7stkIlhSohAMy18vFjGzQkos4zZicBskOr8WW4icRz3meSEqicns8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmwEbINLujp8SCybIDvTLsTHARtwkibeYrn0ZzGHgFBKKR7ZNP0z3ib0QaRIW4duTAQtROXtEocpF36CPGy1ibDYAgoUeqwJxB6XI/640?wx_fmt=png&from=appmsg)

OpenWrt小白如何使用该系统？

关注我的很多是OpenWrt玩家，对于如何刷入OpenWrt应该都比较熟悉，但是应该还有很多家长朋友想使用这种上网控制系统，刷机对他们来说是个比较困难的事，后面会考虑提供一些刷好的设备让大家购买，并提供一个更加偏向普通用户的定制系统，即插即用。现在小孩沉迷视频、游戏确实是一件头疼的事，不仅是小孩，老人现在沉迷短视频、短剧也挺严重，还有很多老人被骗。

反馈的问题

1. X86设备温度显示问题

由于X86平台包含不同的芯片厂家，获取CPU温度方式会有区别，该版本增加了更多的获取温度方式，用于修复温度显示问题，当然不排除存在部分设备显示问题，如果有问题可以反馈，注明硬件型号。

2. 插件安装提示错误问题

在安装docker等大型插件的时候，很容易触发浏览器超时报错，类似"Error: XHR request aborted by browser"提示，这种是OpenWrt软件中心本身机制的问题，检测到插件长时间没有安装反馈就会报错，而实际后台是在安装的，只是插件比较大安装较慢而已，可以不用管这种报错，等一段时间刷新页面查看安装结果即可。

为了减小这类问题，软件源一定要切换为国内镜像源，提高插件的下载速度，关于如何切换软件源，FanchmWrt官网文档中心给出了完整教程，并且给出了国内的镜像源地址。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRk7SBCBg2UpYhHVjrwyZGnZjGVIR75kWEIwJCe7ylffvL45MkZPxYWxAtjF5vjE8CvXXjkTW5AbNArblmaibqZXViaELplnCO9iaY/640?wx_fmt=png...