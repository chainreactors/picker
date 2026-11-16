---
title: 功能大改，界面重做，各种加载器全集成一遍？
url: https://mp.weixin.qq.com/s/gesJk0_9Tykq719NHP1NLQ
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:42:52.652186
---

# 功能大改，界面重做，各种加载器全集成一遍？

# 功能大改，界面重做，各种加载器全集成一遍？

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一、这是什么

LOADER ALL是一个网络安全工具，它融合了各种技术：将加载器、元数据克隆、投递封装、提权、工具编译等技术通过一个界面一键构建。

**本次更新目录：**

1. 1. 新增tprtdll注入
2. 2. 新增3种注入技术
3. 3. 界面优化

## 二、新增功能

1.收录一个tprtdll注入[1]

> EDR/AV 产品通常监控`ntdll.dll`上的调用行为，调用不走这个DLL将直接绕过。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqPDoJug4Es1iatDff9AeYgzF7qEyib3SGwvSqK8icKkCjdbyzDzt7WvHBZJ1x6QibOWhz0HA2drKJs0zwDyVHpXhPaaNAvUKqicGz2o/640?wx_fmt=png&from=appmsg "null")

2.增加经典的CRT（CreateRemoteThread）

> CRT注入其历史可追溯至1994年。该技术的核心逻辑是利用Windows 操作系统提供的跨进程内存操作 API 与线程调度 API，强行在目标进程的地址空间内分配内存、写入数据，并创建一个全新的执行线程来运行这段数据。是进程注入体系中最基础、最原始的实现形态，也是现代所有注入技术的演进起点，必须收录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqNll4VpSDvQr3NjxDoHB6iaiboPsWgDahvAiaHicTMOeYEVs97UibeTicHSh8hjRJ658CMeMK2KIFEClQCpvmb35fuszGz9ibXOh3zLfc/640?wx_fmt=png&from=appmsg "null")

3.增加劫持类（Hijacking）模式，收录APC和Early Bird两种注入方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqNdLpJpjtV6w531gcRFUU2XVJOsicFNARfia50ZWhlI3M93OoasVaXEOGoBSwREVBum9JCWp4xsNSM3dwcrRmrkIdHQuLoDyFicoY/640?wx_fmt=png&from=appmsg "null")

> 经典的APC注入将自动寻找进程执行注入，而早鸟则是创建挂起的进程，是前者的演进。

4.载荷支持XOR与CODASM[2]加密方式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqNZRuoXic7tpiaWWyAEHcNLC1ndx0PTqtjMdVhhqmrNAEOeZxz1D4FlAE5oOMWq0SiafODkxXicgZlhoyzFCT9bYbR0T8B715L0xuA/640?wx_fmt=png&from=appmsg "null")

> xor（异或）的内容包括载荷和随机密钥，不会留下任何明文字符串；而codasm编译为汇编指令至.text区域，与代码混淆绝配。

5.修复Bug

修复tt模板加载大载荷时崩溃的问题，现在概率降低。

![](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqMRLJBskibTqYvrvOl6cFqVCLLwrt6xj8biaxaiaX5sswyvTods7RqZj3XWI2eoRkBsdQ67ylHWyG5ePRWgdJvlT4W2YHE3fricTww/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqPfMW5FvvIkI9jlYNxYZavjdM54Ib5laicDLTfFYD5U4k4Vic2AhkdHSOaB30ZrY6I2mOvAmlkgXqLElM8Q1Bw3CfhcDTG8yuAjo/640?wx_fmt=png&from=appmsg)

<<< 左右滑动看更多 >>>

> tt模板是一种利用微软数字签名加载静态文件的技术[3]，属于`lolbins`中的一种。

6.界面优化和各处细节调整

使用现代UI设计，浅深两套主题切换。

![非静止画面](https://mmbiz.qpic.cn/mmbiz_gif/ibXL9MCj2GqOgNzVCCfGTwS99lyhr4hszfygiaffKMVGrZJLHIicEuPUp3YJFBKuvEgg7qV7QubRaDsYiaeVIArJHnicl7tFJUx8sTtgCF0DYQYA/640?wx_fmt=gif&from=appmsg "null")

非静止画面

## 三、工具获取

为防止滥用与泄露，工具不免费公开，其内置序列号授权机制。仅供学习和研究并在可控的环境中测试。

## 四、使用场景

1. 1. 在企业授权的攻防演习中，验证防守方的检测与响应能力
2. 2. 理解各类加载技术的实现机制与运行过程
3. 3. 在受控环境中测试安全设备的检出情况，用于优化检测策略

## 五、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

1. 1. 仅可用于已获得书面授权的目标系统测试；
2. 2. 遵守法律法规，不得用于侵犯他人隐私或数据窃取；
3. 3. 本人不承担因用户滥用本软件导致的任何后果。

使用即视为同意并接受上述条款。

#### 引用链接

`[1]` tprtdll注入: *https://github.com/ivancabrera02/tprtdll-Injection*
`[2]` : *https://github.com/NVISOsecurity/codasm*
`[3]` : *https://github.com/whokilleddb/TTs*

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqOq43RSf7lfRmsfht4j1OYpZFxV2yBmkPGsNJ4ROQHcUkhseQdibY4vbINt7aotxvSXjWxIEmph546T4Ql1zVcJWTgMNBkYib4ibo/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过