---
title: 漏洞预警 | Linux kernel权限提升漏洞
url: https://mp.weixin.qq.com/s/Z-T84ceSUzTF9BoA697AZw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:07:08.856123
---

# 漏洞预警 | Linux kernel权限提升漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NQlfTO30MhyicqQicxrY4dSLWKwZNePV6AbVEsokjpK6IrfYpRD1FicmhMuApRJnxFOclm7ECE5RX87kK7oy3HiaNjrv2D2XOV5SH8URiatWf2eg/0?wx_fmt=jpeg)

# 漏洞预警 | Linux kernel权限提升漏洞

浅安
浅安

浅安安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**0x00 漏洞编号**

* # CVE-2026-46331

**0x01 危险等级**

* 高危

**0x02 漏洞概述**

Linux kernel是美国Linux基金会的开源操作系统Linux所使用的内核。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NQlfTO30MhxQXbwG1WSjsS1TMvUY3aIsCJ1ic2kxclUiaYic5gV2p9dmfrcTERVZZ5bEOnWFIvWxTRHhnpSrVwYdscfiaPjyuYZZadMxgIIH8Gg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

**0x03 漏洞详情**

**CVE-2026-46331**

**漏洞类型：**权限提升

**影响：**获取root权限

**简述：**Linux Kernel net/sched act\_pedit存在本地权限提升漏洞，由于其tcf\_pedit\_act()函数在处理数据包编辑操作时，函数仅在循环外基于tcfp\_off\_max\_hint一次性计算skb写时复制COW范围，该提示值未考虑运行时类型密钥追加的报文头部偏移，导致部分待写入内存区域未执行COW拷贝。攻击者可通过非特权用户命名空间配合CAP\_NET\_ADMIN权限，构造恶意tc流量规则，触发未COW的共享只读页缓存写入篡改；无需内核竞态条件，可稳定篡改setuid-root二进制文件的页缓存，不会持久写入磁盘，仅内存层面生效。成功利用后本地普通用户可直接获取系统root最高权限，从而实现完全控制服务器。

**0x04 影响版本**

* v5.18 <= Linux Kernel < v7.1-rc7

**0x05 POC状态**

* 已公开

**0x06****修复建议**

********目前官方已发布漏洞修复版本，建议用户升级到安全版本**************：******

https://www.kernel.org/

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7stTqD182SVPICJDGr5sbVNZO1lo2JnwVDrPBcvzPxiaiamvVZWxcxxcqQYeAiaAnXS26Hyp0wxEx5uXESx0NBQMg/0?wx_fmt=png)

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