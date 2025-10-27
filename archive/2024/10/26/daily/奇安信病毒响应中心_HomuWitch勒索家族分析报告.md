---
title: HomuWitch勒索家族分析报告
url: https://mp.weixin.qq.com/s?__biz=MzI5Mzg5MDM3NQ==&mid=2247497633&idx=1&sn=e961e85aca2f435759f5755c7c2bd6a2&chksm=ec698789db1e0e9f81f4107577c528920d9d885022243c5113a023227f5c9b5c46fd865495aa&scene=58&subscene=0#rd
source: 奇安信病毒响应中心
date: 2024-10-26
fetch_date: 2025-10-06T18:53:38.264910
---

# HomuWitch勒索家族分析报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGliay0oag4CaRgJGCmpKWB0nD2X3vUVjgYFUkoxxdnUeKLQ6XDeQLK1aA/0?wx_fmt=jpeg)

# HomuWitch勒索家族分析报告

QAX病毒响应中心

奇安信病毒响应中心

**一、概述**

HomuWitch是一种勒索软件最初出现于 2023 年 7 月。与当前大多数勒索软件病毒不同，HomuWitch 的目标是最终用户（个人），而不是机构和公司。它的流行率并不是特别高，所要求的赎金金额也不是很大，这使得该恶意软件迄今为止一直处于相对低调的状态。

该家族样本使用 AES-CBC 算法对目标文件进行加密，被加密的文件后缀名为“.homuencrypted”。同时该家族样本还会在加密受害者文件后弹窗提示用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGlgvqYcggT3mbsYgUdR6ptQBxAgUqruWzNl4ud2c2yHFBpLbwvbVSN2w/640?wx_fmt=png&from=appmsg)

目前集成了奇安信勒索防护模块天擎产品支持对HomuWitch家族的精准查杀，包括静态文件查杀、动态行为查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGltSicfwLyWhMbrU9kNwKJ32A6XwmmZ3xvJU3az63WK0G4kQoia4JHZSpA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGl6ttmysW1icibO0uq99kJF3ticvRwtrYltkvlamYwibxNdRNI0RPfou4zWg/640?wx_fmt=png&from=appmsg)

并且，在对该家族的详细分析之后，奇安信勒索解密还原工具目前集成了对该勒索家族的解密还原。通过在最新的奇安信测试环境中进行验证测试，奇安信勒索解密还原工具目前可以成功还原被该勒索家族加密勒索的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGl9L5kXWRVBIevPv5rNLCo4HwX5TKLrMYVzqQKcgZD89VQSbicZYOoTvQ/640?wx_fmt=gif&from=appmsg)

**二、样本功能分析**

**（一） 基础信息传递**

病毒启动后会获取用户计算机系统使用的语言名称，并且和5个地区语言名称代号小写（分别为ru俄语、uk乌克兰语、uz乌兹别克语、bel白俄罗斯语、kz哈萨克语）进行对比，如果匹配成功则设置程序的语言为俄语，否则则默认为英语（en）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGlicCWapZIKw221h2DcWXpOSN5KibFH5PcSPteF3kVgzb27gZz0BliaiblbA/640?wx_fmt=png&from=appmsg)

接下来通过请求 https://ipapi.co/country\_code/ 获取网络请求返回的国家标识码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGlpOTubS26oQ7zxwrqgtalewjegI5KAypQNoxYMApx0XBCeVUNJwffxQ/640?wx_fmt=png&from=appmsg)

再将系统的设备信息、计算机用户名称一起发送到服务器 https://193.164.150.225:1200/。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGlibxFtMTEhVBrwl4zYfibaibecZ6hiamTs1t5RvWvrfBE4pc4Mw8ibcxPLeA/640?wx_fmt=png&from=appmsg)

****（二）**待加密文件目录**

获取设备使用空间小于3500MB的驱动目录，添加到待加密目录中，这里的攻击目标很可能是计算机上的USB设备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGl8W0cl6mXzOaFPjRhia7ibI3HPB6UHjBvqcLzQWzrSKu5sWEvnXU2lPaA/640?wx_fmt=png&from=appmsg)

待加密目录除了上面添加的路径外，还包括用户桌面目录、用户的“Downloads”目录和用户文档目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGllxQUkqxgMnqibtN0T8pavsaj1poYjmBO7nLwUJoCSOdMGvTYPhZLcvA/640?wx_fmt=png&from=appmsg)

****（三）**加密文件**

加密文件前，先通过遍历待加密目录获取文件路径，判断是不是待加密的文件后缀类型，并且只加密文件大小小于55M的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGlvWhk8rhaMB27ZXcSkoB6iag7w6cjiaInGBJbNuIic9VqX6nUy1QuMwjmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGleRiajE8DWtvBQnVTB6xuQLVPmAiaibDAUZRxDpuPPuZxOWxTXelibZrNeQ/640?wx_fmt=png&from=appmsg)

加密文件时将内置的password通过Rfc2898DeriveBytes算法初始化AES的key和iv，将待加密文件的内容先压缩后再进行AES加密，最后给文件添加上后缀.homuencrypted，并且删除加密前的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGl4o8fysqahiby1hd1cQXTmwI0UlkiasZQJcvQpnCibTicbIw1GcczbQLu1A/640?wx_fmt=png&from=appmsg)

****（四）**后续操作**

文件加密完成后，会在用户的AppData/HMW/User.ini配置文件中写入“BFXO”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGlfs1WrnYmHk8j1C89nG9WYicbOhmQVdt067ibJjNWVAOXBW2E9wGFjdlg/640?wx_fmt=png&from=appmsg)

修改自身文件属性，尝试隐藏自身。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGlh7XOX4fKUG2vheOz32ql10qYcwtE4ezujHibVOiaZ51lDic63e97iaDsOg/640?wx_fmt=png&from=appmsg)

在执行加密文件操作前，还会新建线程来清空回收站。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGlVHl6uA5ADxfDdkppMoT62VFYMPzRuQj231SbFL09YuaU0YIhibIf8Ww/640?wx_fmt=png&from=appmsg)

后续还会修改桌面背景、运行勒索界面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGlDgibkibNib1XANEzRgmMfgq1bVnnxxibJZBDMtUMKuaLKXMwNSOLibQ7Gow/640?wx_fmt=png&from=appmsg)

界面上的数据通过网络请求获取，由于C&C地址失去连接，界面上只显示默认的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icIVJN2qXD6sxJuuyhVOlpicpBgN3saGGlTrKQO1frNoz4252Gribibmp75EonqCUvtTibfdSRHSQiaicjFqa03k1RvhQ/640?wx_fmt=png&from=appmsg)

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

**IOC**

|  |
| --- |
| **SHA-1** |
| 78abf1fcc5783e9c62c78f7ce4b066675bbd71ce |
| 1e5fdbe22cc41a0ecc18ee6808608cea4b31fba8 |
| 96490ad9b42b7dfd8af9ffad6ec55d60bba51864 |
| 332c5cde06c6a3e6174e0bfd846da971f4151599 |
| 35c5b1de844136e32a883981cba8add3af43e952 |
| 2ca94ba8726810b49d69422d3ff5ae4622090f19 |

C&C

193.164.152.225:1200

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