---
title: Rhysida勒索家族分析报告
url: https://mp.weixin.qq.com/s?__biz=MzI5Mzg5MDM3NQ==&mid=2247495585&idx=1&sn=b46735cc19bab6ba7cecf2499135013a&chksm=ec699f89db1e169fc7ffc437204457c0e1067d1ce9fd8a8c54c70df78ef1add583a692a4899e&scene=58&subscene=0#rd
source: 奇安信病毒响应中心
date: 2024-08-22
fetch_date: 2025-10-06T18:03:57.175836
---

# Rhysida勒索家族分析报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icIVJN2qXD6u91M37Rib71bQCE56fr7V27ZSbcUzibyggd8VHZAL9uTYGlicVfCicWLX8g2kibAIuYefDEhG6hLq907A/0?wx_fmt=jpeg)

# Rhysida勒索家族分析报告

QAX病毒响应中心

奇安信病毒响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27MM89W0qicYgic0icpMXNiaicZfS8KAics6BicxicjVSwmxkYNMlQcYvNpibKORg/640?wx_fmt=png&from=appmsg)

**一、概述**

‍‍‍‍

Rhysida勒索团伙以使用数据窃取+数据加密的双重勒索方式而闻名，其活动自2023年5月以来逐渐引起关注，并被多家安全厂商所披露。通过其对外网站显示，该团伙至今已经攻击了108个目标，包含教育、医疗、政府等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27qicbS4iaIp0c8ruedavpUTYRLDxFia9viaKKOAapHxHcbKcaJiadicLEJibdQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27VPYvhwd7VZzcuksUhiazbevrSt73TzlQz9gMeAic1McpnZ7Dx6VAJhGA/640?wx_fmt=png&from=appmsg)

近日，奇安新病毒响应中心通过猎鹰平台发现Rhysida勒索团伙特有的Rhysida家族样本仍处于活跃状态。Rhysida家族最早出现于2023-05-17，由MalwareHunterTeam 安全团队首次披露。该家族样本使用 ChaCha20 算法对目标文件进行加密，被加密的文件后缀名为“.rhysida”。其会在加密受害者文件后投放名为 “CriticalBreachDetected.PDF”的勒索信，并在启动后修改系统卓面背景，显示勒索信息。比较独特的是，勒索信中该团伙伪装自称是一个 "网络安全团队"，旨在帮助受害者保护他们的网络安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27yicssowbjLIWK4Qj5705jo5Fj5yiaklnGpcd3UtnUsQ1tV5Y6QOGvfMA/640?wx_fmt=png&from=appmsg)

目前，集成了奇安信勒索防护模块天擎产品支持对Rhysida家族的精准查杀，包括静态文件查杀、动态行为查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V2791aILJ9gaxpywbfkndqbxfaviaJdzk4ibNsnxm8lBVvLbH5ibP87HrPiaw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27jlrO9puZ9bJ6k04PaxTSC9yuBmcBF4JBoichwoJkBe6bUSibNNJZPe2w/640?wx_fmt=png&from=appmsg)

并且，在对该家族的详细分析之后，奇安信勒索解密还原工具目前集成了对该勒索家族的解密还原。通过在最新的奇安信测试环境中进行验证测试，奇安信勒索解密还原工具目前可以成功还原被该勒索家族加密勒索的文件，目前支持还原被该勒索家族加密的文件类型包括：.zip、.docx、.xlsx、.pptx、.xls、.ppt、.pdf、.psd、.jpg、.png

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27PIOXIlA26AcFYDAGcTAaCmeN1BxSJWUfROlric2sSalF6VMMumVqHJQ/640?wx_fmt=png&from=appmsg)

‍‍‍‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27MM89W0qicYgic0icpMXNiaicZfS8KAics6BicxicjVSwmxkYNMlQcYvNpibKORg/640?wx_fmt=png&from=appmsg)

**二、样本功能分析**

**（一）数据初始化**

初始化随机数种子并申请数据空间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27zPXcDwvxmcJTHPkRfiaGiaIkKYSgkQ1W0KPGuibRCWwWgbsPq7Aicq5Yuw/640?wx_fmt=png&from=appmsg)

处理参数和加密秘钥初始化。                                                             ‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27LgsiczWvKriacy2onqFDCiaaBPXTK8nuKUBTL3BVKJibhiceh3kRnltB2Jg/640?wx_fmt=png&from=appmsg)

初始化后，创建了 sysinfo.dwNumberOfProcessors 数量的线程，执行processFiles函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27LzdniaNXcxLSqm8Yvq8SvWyzQ2kianALQv0M4J8gW6e6qu8DGs8Pyh4A/640?wx_fmt=png&from=appmsg)

遍历盘符A-Z，查询磁盘中的文件，将查询到的文件和上面创建的进程关联起来，并且写入勒索信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27Sv7ux4ejWwFqITwaOCFgicRup1V4OHpY8verKm3NK0kXgSs9dNHiayow/640?wx_fmt=png&from=appmsg)

执行cmd命令尝试删除自身，并且修改桌面背景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27urf4W4cIBR08RibR0zYNoOrE6vM7ZMicquZ5BXfOnicn7kOcEWe12YZAw/640?wx_fmt=png&from=appmsg)

**（二）参数处理**

进入parseOptions函数，支持两种参数命令，分别为“-d”和“-sr”：

–d参数 指定加密的文件夹

–sr参数 运行完成后删除自身

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27DTcwPicbSHMOQblkZOMoByOk4EqrKtibBibvUX57iaIqtd6UhgDvmhcSWg/640?wx_fmt=png&from=appmsg)

**（三）桌面背景修改**

执行setBG函数，使用Arial.ttf字体处理将在桌面显示的文本信息，创建桌面背景图片，并通过cmd命令设置为桌面背景图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27lvojMIUxSaCts8FeB5ic4Y0P5RN0SvzUEMsrA9rDicqxAjudDIXibuUGg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27bFvtlwStj27H9WCLwkSqR5a9EPcElLBMDqvhytBv3qfQuWkTCA01Lg/640?wx_fmt=png&from=appmsg)

**（四）文件加密**

执行创建的线程的processFiles加密函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27TzBH1eYLbXjwZ9rkI0jfuiaMQf33ibzN4dcEUIdqMNcYjPD0B2Rqtylg/640?wx_fmt=png&from=appmsg)

过滤掉文件后缀名为 rhyida、CriticalBreachDetected.pdf、.bat、.bin、.cab、.cmd、.com、.cur、.diagcab、.diagcfg、.diagpkg、.drv、.dll、.exe、.hlp、.hta、.ico、.lnk、.msi、.ocx、.ps1、.psm1、.scr、.sys、.iniThumbs、.db、.url、.iso、.cab的文件。进入processFileEnc函数执行加密，先是重命名文件，再通过chacha20\_prng\_read获取加密文件的AES算法的key和iv，然后使用RSA算法加密key和iv，并且将RSA算法加密后的内容写入到文件中。接下来按照带加密文件大小，将文件整体或者拆分为多组数据，通过AES-CTR算法加密每组最多0x100000大小的数据，将加密后的数据替换原本文件中的内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27KgKXomVXAcTmZ0MiaU60hRguHbbpicENADqq4w1pflBf9Ia0C8WMwdDQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27ZtSFPibvMES8tU0YrWsLLwHZo1EPC8CrKZAfVDFy65wSWs3g63jEicBw/640?wx_fmt=png&from=appmsg)

其中采用随机数作为参数初始化的chacha20。                                        ‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27BZWYYfBhxTBfEI0reIU0gREfQwZLUeInqnibRlB9vF8Xnibn8nxs1VDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27MM89W0qicYgic0icpMXNiaicZfS8KAics6BicxicjVSwmxkYNMlQcYvNpibKORg/640?wx_fmt=png&from=appmsg)

**三、防护建议**

奇安信病毒响应中心建议广大政企单位从以下角度提升自身的勒索病毒防范能力：

    1.及时修复系统漏洞，做好日常安全运维。

    2.采用高强度密码，杜绝弱口令，增加勒索病毒入侵难度。

    3.定期备份重要资料，建议使用单独的文件服务器对备份文件进行隔离存储。

    4.加强安全配置提高安全基线，例如关闭不必要的文件共享，关闭3389、445、139、135等不用的高危端口等。

    5.提高员工安全意识，不要点击来源不明的邮件，不要从不明网站下载软件。

    6.选择技术能力强的杀毒软件，以便在勒索病毒攻击愈演愈烈的情况下免受伤害。

目前，基于奇安信自研的猫头鹰引擎、QADE引擎和威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、奇安信天狗漏洞攻击防护系统、天擎、天机、天守、天眼高级威胁检测系统、奇安信NGSOC（态势感知与安全运营平台）、奇安信监管类态势感知等，都已经支持对此类攻击的精确检测。

特别是奇安信天锁对勒索病毒的静动态检测能力、智能密钥恢复能力、灾备能力，可以专项针对勒索病毒做企业的终端立体化防护。配合天擎EDR，还可支持攻击溯源。经测试验证，目前天锁已支持对此类攻击的立体化防护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6u91M37Rib71bQCE56fr7V27MM89W0qicYgic0icpMXNiaicZfS8KAics6BicxicjVSwmxkYNMlQcYvNpibKORg/640?wx_fmt=png&from=appmsg)

**IOC**

|  |
| --- |
| **MD5** |
| 0C8E88877383CCD23A755F429006B437 |
| C9A5E675DBB1F0CE61623F24757A1C72 |
| FBBB2685CB612B25C50C59C1FFA6E654 |
| 4EF0160B3EB114A94AEEDD0BB5716058 |
| 7DD4DE113A97C638518F01760FF4F03C |
| 67EDFFF8250487D97F403C74FED85388 |
| FAC561BB0F072D29FE6F8EE6072C905A |
| 59A9CA795B59161F767B94FC2DECE71A |
| 44C7D18633B5741DB270A6BD378B6F3C |
| 2B825EA77E240D2AB6B6695A602CB07C |
| 1E256229B58061860BE8DBF0DC4FE67E |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icIVJN2qXD6sNxaMnib74YRj4cHI2zWyNMMz42LoB7X6dXEzXwsrjmA8gDDqZp0iateHgV9Yq4EggM4E68hjRmTZA/0?wx_fmt=png)

奇安信病毒响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icIVJN2qXD6sNxaMnib74YRj4cHI2zWyNMMz42LoB7X6dXEzXwsrjmA8gDDqZp0iateHgV9Yq4EggM4E68hjRmTZA/0?wx_fmt=png)

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