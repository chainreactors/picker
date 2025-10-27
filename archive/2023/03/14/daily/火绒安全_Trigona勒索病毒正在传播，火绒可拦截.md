---
title: Trigona勒索病毒正在传播，火绒可拦截
url: https://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247513334&idx=1&sn=63117e20d641c70e657bcde416bc5b5c&chksm=eb706ac9dc07e3dfe0149ecc3b8c4d6e5dd615342c9d16e91aa24749f3e18915281d1744f263&scene=58&subscene=0#rd
source: 火绒安全
date: 2023-03-14
fetch_date: 2025-10-04T09:30:59.358619
---

# Trigona勒索病毒正在传播，火绒可拦截

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRS6jGppCq1B29picAPODSHGvT7RSfggTwRjSFZFr6yUzUMMFzvTwVncA/0?wx_fmt=jpeg)

# Trigona勒索病毒正在传播，火绒可拦截

原创

火绒安全

火绒安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRhQdek2torYJtwq5VqLeP59iaJWiahmby0CbIEy79QHSDNOdibxef5O8IA/640?wx_fmt=gif)

近日，据火绒威胁情报系统显示：Trigona勒索病毒正在活跃。近一个月内，火绒已帮助数千台终端成功拦截该病毒。该病毒在2022年12月份首次出现，今年2月末爆发，其传播数量趋势如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIR4987wG8NweibduhquyEJC83Ty4WUxuT48QlDohaZFpDuHbN7XR6ageQ/640?wx_fmt=png)

传播趋势

黑客通过SQLServer弱口令暴破等手段，入侵受害者终端进行投放Trigona勒索病毒，该病毒会在终端添加自启动来进行持久化操作。

火绒工程师表示，该病毒会先使用AES-256（对称加密算法）对文件进行加密，随后再使用RSA-4096（非对称加密算法）对解密密钥进行加密，并保存在文件尾部，目前暂不支持解密。被加密后的文件后缀名为：\_locked，勒索信如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRsmNO1k8w9u5lhIibZGWeGXLneptwAmhkBicqr9ya7FGW1qichhDdWg1gw/640?wx_fmt=png)

勒索信内容界面

被勒索后，黑客仅提供了与其直接进行沟通的暗网页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRgw3pibEmfm6OkqHicOg1Km3hiawBq2ibLPyIj8P06CtMvN2xma6sghEcyw/640?wx_fmt=png)

暗网页面

火绒用户无需担心，"火绒安全软件"可拦截、查杀该病毒。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRUkTWfhfGr2XYLblyYjmaxfibT8Xfib6TvMtZTwB86NbkTRqZUniavCDyQ/640?wx_fmt=png)

查杀图

火绒提醒广大网友，重要的文件请及时备份，并安装安全软件定期扫描，定期更新高危漏洞补丁以防御勒索病毒带来的危害。此外，通过分析勒索病毒关键节点的各种攻击方式，火绒安全产品在各个维度上都做了有针对性的防护措施，如【密码保护】、【程序执行控制】、【远程登录防护】等功能。

**一**

**样本分析**

病毒的执行流程，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIR2SPbNmUsTSVoRRJEIePLMhNylstUYVa2MbewqxHQwhXIWcuM6m14UA/640?wx_fmt=png)

病毒执行流程

初始化模块svcservice.exe启动之后，会释放勒索模块和bat脚本，先执行bat脚本来对系统做一些设置如：删除卷影副本、关闭UAC、关闭隐私设置、禁用系统还原，并运行勒索模块来对受害者系统进行加密，该模块跟系统文件同名svchost.exe，
相关bat脚本内容，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRNnEC2SrBaJjfibBxvCqODdVslmND8uA3QuFzJwjjuLaMEIubenDzdZQ/640?wx_fmt=png)

bat脚本内容

勒索模块svchost.exe启动后，会遍历系统磁盘，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRc3XMIBybdxj62L6WPonIsbJ4PWLdD2nvCLWHGUQhUGlBYK9LFGIa3g/640?wx_fmt=png)

遍历磁盘

使用AES-256算法对文件进行加密，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIR6HWmslrxKEibXQVV3U0EyMQ3mgiagY4K75g4plONOzffc4Eq27y29ibag/640?wx_fmt=png)

AES-256加密

将文件加密后，会将解密所需的信息用RSA-4096算法进行加密，并保存在被加密后的文件尾部，用于解密文件，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRABSJEnB5a0ZpeX6KgNOiciaH7vkw6uOggq02a2g8I6qgAJb5Uf5GX0lA/640?wx_fmt=png)

RSA加密

RSA的公钥（E,N）其中E为65537，N的值，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIR2co0HuT0942PnyB9UmYV2lPCn1XAvDNZPjIsZTWWCVVyTPc8mJcBMg/640?wx_fmt=png)

N的值

加密完之后，会在对应目录下创建勒索信（how\_to\_decrypt.hta），相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRwDJaDC80zKQEYic332HBOaQ3cqz4EzF33QZsy3xd7gFicFgKQu3iam9lw/640?wx_fmt=png)

创建勒索信

该勒索病毒还会添加自启动来进行持久化操作，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIR51RDDEq0EGbIh3cfDLEgvgbYfmK69yC3ufpzRYyYRRFEMcyEQDc6QQ/640?wx_fmt=png)

持久化操作

**二**

**附录**

HASH：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRq2JaDHKAYCxhvaNNdlxcQR113oonDIRsSCatRwLCCZlmDaetzCX1Aw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz57ibRBm79Ghwt9ykq15eMIRsW3GmOtw1Lia8MNUbZXPPqH8gzF7XCBEUFMg4gnhgROHQENY5VicwYEg/640?wx_fmt=jpeg "公众号二维码.jpg")

扫码关注

了解更多安全干货、资讯、以及火绒安全大事记

分享收藏点赞在看

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

火绒安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

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