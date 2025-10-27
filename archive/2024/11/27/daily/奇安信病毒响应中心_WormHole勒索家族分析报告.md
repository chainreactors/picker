---
title: WormHole勒索家族分析报告
url: https://mp.weixin.qq.com/s?__biz=MzI5Mzg5MDM3NQ==&mid=2247498063&idx=1&sn=e3dc3c1cb2373ae6ced733453b9b9901&chksm=ec698967db1e0071b0ed8dd26cb85ac00469c74753e6afc9cf82313370914031d2fb75ccb47e&scene=58&subscene=0#rd
source: 奇安信病毒响应中心
date: 2024-11-27
fetch_date: 2025-10-06T19:18:20.299606
---

# WormHole勒索家族分析报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQFr2DaSRPAbSGrg2Qq1MHehD33ZXcCPpgk6V7Lyn1xQfvgiaYibqGQflA/0?wx_fmt=jpeg)

# WormHole勒索家族分析报告

QAX病毒响应中心

奇安信病毒响应中心

**一、概述**

WormHole是一种勒索病毒家族最初出现于 2024 年 4 月。该家族样本使用 AES-CBC 算法对目标文件进行加密，并且向客户勒索比特币，被加密的文件后缀名为“.Wormhole”。同时该家族样本还会在加密受害者文件后在加密目录下创建How to recover files encrypted by Wormhole.txt勒索信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQmCQibQhzXia8bkiaySROMtq8U7jWYu0yXyj5wIUk4ne0b1FKyz4oGO5sw/640?wx_fmt=png&from=appmsg)

目前集成了奇安信勒索防护模块天擎产品支持对WormHole家族的精准查杀，包括静态文件查杀、动态行为查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQez98KzftiabhLS791ic3UV3g2x4q8icA5K1mPXnRibDPBdrjpoVoXkYG7A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQs36fY6YrJPhicdicyobibU6PqwWrCYUEM6EnufARJuzZfzp5t2faCrsUQ/640?wx_fmt=png&from=appmsg)

并且，在对该家族的详细分析之后，奇安信勒索解密还原工具目前集成了对该勒索家族的解密还原。通过在最新的奇安信测试环境中进行验证测试，奇安信勒索解密还原工具目前可以成功还原被该勒索家族加密勒索的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQteLiaTQvoAJZl179z3pFicg747riaKia80XVdJYOEJDhcibXXfRzibYW57Zg/640?wx_fmt=gif&from=appmsg)

**二、样本功能分析**

**（一） 白名单**

不加密的目录如下：

msocache、$windows.~ws、system volume information、intel、appdata、perflogs、programdata、google、application data、tor browser、boot、$windows.~bt、mozilla、windows.old、Windows Microsoft.NET、WindowsPowerShell、Windows NT、Windows、Common Files、Microsoft Security Client、Internet Explorer、Reference、Assemblies、Windows Defender、Microsoft ASP.NET、Core Runtime、Package、Store、Microsoft Help Viewer、Microsoft MPI、Windows Kits、Microsoft.NET、Windows Mail、Microsoft Security Client、Package Store、Microsoft Analysis Services、Windows Portable Devices、Windows Photo Viewer、Windows Sidebar

不加密的文件如下：

desktop.ini

ntuser.dat

thumbs.db

iconcache.db

ntuser.ini

ntldr

bootfont.bin

ntuser.dat.log

bootsect.bak

boot.ini

autorun.inf

debugLog.txt

How to recover files encrypted by Wormhole.txt

不加密的文件后缀：

msstyles、icl、idx、sys、nomedia、dll、hat、cur、lock、cpl、ics、hlp、com、spl、msi、key、mpa、drv、bat、386、scr、theme、ocx、prf、cab、diagcfg、msu、cmd、ico、msc、ani、icns、diagpkg、deskthemepack、msp、bin、themepack、shs、nls、exe、Wormhole

**（二） 停止的服务和进程**

病毒在运行中会尝试停止274个服务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQdxK080OIPbWmMOtXPesjfHHOluU9ClcZQQH2cODYGzaaO6QyyaPd6Q/640?wx_fmt=png&from=appmsg)

病毒还会尝试停止96个进程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQdxK080OIPbWmMOtXPesjfHHOluU9ClcZQQH2cODYGzaaO6QyyaPd6Q/640?wx_fmt=png&from=appmsg)

**（三） 删除卷影**

病毒启动后静默删除卷影，防止用户恢复被加密的文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQ5Ou436dtkj8urdw2zHlnrKNeFZNZqy0ftnYFSKffL7jKSPnia2mWT9A/640?wx_fmt=png&from=appmsg)

**（四） 初始化秘钥**

病毒会在启动后初始化大小分别为0x20和0x10的两组随机数，通过后续分析得出这两个数据是后续加密文件时会用到的AES256的key和iv，并且会使用样本内置的RSA公钥加密key和iv，并将结果作为用户的Wormhole ID，后续写入到勒索信中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQmPrCs5vrj9fXeLFEPibuoOLf7OibdFdg2W5CbFhlyptcG8ibqfwdlVkFw/640?wx_fmt=png&from=appmsg)

**（五） 加密文件**

遍历设备驱动

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQz7tjKlib7Lqs1Vjahdfvv55HH9A0mX3Np8tPHPbF5SttAG563PKT13A/640?wx_fmt=png&from=appmsg)

重命名文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQRfjsqJtOysyWhLC97rGKVT9ww3WicWzBO5tdC8I4VfBN7NFgUV3j6rQ/640?wx_fmt=png&from=appmsg)

‍‍

后续使用上面初始化的随机数来加密文件，通过分析，这里使用的是AES256-CBC算法加密的文件

‍‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6tGQ1ynCdcibmu3yccPeQNqQAMicG9AthbrJ0LM7xibFUGhKuRQF0QYWM3Zwl6jBvKXQhl9EafSWZ1dQ/640?wx_fmt=png&from=appmsg)

**三、防护建议**

奇安信病毒响应中心建议广大政企单位从以下角度提升自身的勒索病毒防范能力：1.及时修复系统漏洞，做好日常安全运维。

2.采用高强度密码，杜绝弱口令，增加勒索病毒入侵难度。

3.定期备份重要资料，建议使用单独的文件服务器对备份文件进行隔离存储。

4.加强安全配置提高安全基线，例如关闭不必要的文件共享，关闭3389、445、139、135等不用的高危端口等。

5.提高员工安全意识，不要点击来源不明的邮件，不要从不明网站下载软件。

6.选择技术能力强的杀毒软件，以便在勒索病毒攻击愈演愈烈的情况下免受伤害。

目前，基于奇安信自研的猫头鹰引擎、QADE引擎和威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、奇安信天狗漏洞攻击防护系统、天擎、天机、天守、天眼高级威胁检测系统、奇安信NGSOC（态势感知与安全运营平台）、奇安信监管类态势感知等，都已经支持对此类攻击的精确检测。

特别是奇安信天锁对勒索病毒的静动态检测能力、智能密钥恢复能力、灾备能力，可以专项针对勒索病毒做企业的终端立体化防护。配合天擎EDR，还可支持攻击溯源。经测试验证，目前天锁已支持对此类攻击的立体化防护。

**IOC**

|  |
| --- |
| **SHA-1** |
| 83647cf2c25198475a006eaa0b997a2cbfdc14fe |
| 1b17fee046e7db0eed3c2bd0bb3aac96e9509d39 |
| 94ac1e7d8aaed7114d7fc49fe4162e8c99121028 |
| 94365aa69ebacffb3b5e323bd430d181cd52f25e |

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