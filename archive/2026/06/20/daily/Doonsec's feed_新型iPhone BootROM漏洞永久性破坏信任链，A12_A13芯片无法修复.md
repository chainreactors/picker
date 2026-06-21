---
title: 新型iPhone BootROM漏洞永久性破坏信任链，A12/A13芯片无法修复
url: https://mp.weixin.qq.com/s/dqxTTN52Gfmavr1XFEbyQA
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:46:14.734442
---

# 新型iPhone BootROM漏洞永久性破坏信任链，A12/A13芯片无法修复

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0eGMO2Ug5r4Ezewk5F45Yx6FZwicW7AzDabo4UVxyhsR5FlOdnibU63icTHwHk92ZSL5KZrQqxvc8SC9dITMNY0bT4d1f0MpNDt8/0?wx_fmt=jpeg)

# 新型iPhone BootROM漏洞永久性破坏信任链，A12/A13芯片无法修复

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX3xiaOscD1zxCclpLibmO45DMLs1MOPHSWFR5EjSFHCtgsS2qWv5zMoTDM5cnBuobUibbGUibhM3K2P6M3bGVcCsH2nhjIqBbeibEQM/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX08DibQtAV9jDsMo6vrUhYjTzKGjRRicU14NSOshgxTcpXZDywm0bY2sibYicdqjvPTmYbjKtXn7zmic0v1zzaX22KYXZPSg1RlBOhc/640?wx_fmt=png&from=appmsg)

一项名为usbliter8的新型BootROM漏洞影响搭载A12、S4/S5和A13芯片的苹果设备。该漏洞利用Synopsys DWC2 USB控制器中的硬件级缺陷与固件配置缺陷形成攻击链，由于BootROM代码不可更改的特性，导致无法通过软件补丁修复，最终实现应用处理器完整启动链的攻陷。

Paradigm Shift研究人员指出，该漏洞源于DWC2 USB控制器处理连续USB Setup数据包的方式。控制器在重置DMA基地址（存储于DOEPDMA寄存器）前，会在内存中存储最多三个Setup数据包，其工作机制类似环形缓冲区。

关键缺陷在于：每次写入后，控制器会按写入数据大小递增DOEPDMA值，但重置操作始终固定递减24字节。由于控制器还接受以4字节为单位的较小数据包，这种指针运算机制会失效。变量递增与固定递减之间的不匹配导致每12字节步进产生一次缓冲区下溢，使得攻击者可控制写入目标缓冲区之外的内存区域。

在A12和A13芯片上，SecureROM中的USB DART（设备地址解析表）配置为旁路模式，意味着没有IOMMU屏障阻止DMA覆盖任意SRAM数据。A14及后续芯片正确配置了DART，使得该漏洞无法在新硬件上利用。

Part01

A12与A13芯片的漏洞利用差异

在A12和S4/S5芯片上，漏洞利用相对直接。DMA缓冲区与堆上的USB任务栈相邻，攻击者通过破坏保存的链接寄存器（LR），在调度器上下文切换期间获得程序计数器（PC）控制权。随后通过精简的ROP链将DMA写入重定向至通常EL0不可写的启动跳板区，最终跳转至SecureROM的EL1转换例程，以完全权限执行攻击者shellcode。

![芯片漏洞利用示意](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX05Tn9hLbIOjtUibSz8ev9cAKAicHxft9loiasV0bd1LmBkibVVFESjM5P1t3O6swD2vg77jG5ibj7ABzlInib7rlrgmq3HuVEBK9n4E/640?wx_fmt=jpeg)

A13芯片引入指针验证（PAC）机制，使直接破坏LR变得复杂。研究人员开发出多阶段技术：通过可控覆盖DART堆元数据、中和堆校验和保护机制，以及用0xF写入原语覆盖全局崩溃计数器来抑制崩溃重启。最终通过从攻击者控制内存加载函数指针的gadget绕过PAC——由于固件中仅启用IB密钥，这一疏忽成为致命弱点。

Part02

攻击实现与持久化

获得EL1代码执行能力后，攻击利用将自定义USB请求处理程序注入未使用的启动跳板空间，修补USB序列号加入"PWND"标识，并恢复损坏的堆分配以维持设备稳定性。

在A13芯片上，由于内存破坏程度较深，需要完整重启SecureROM——研究人员将ROM复制到SRAM，通过自定义MMU转换表重新映射，并挂钩ROM页表项生成以保持重启过程中的地址空间一致性。自定义处理程序支持两项特权操作：SoC降级（临时降低生产模式）和无签名iBoot启动（绕过原始iBoot镜像的所有签名验证），这实际上废除了苹果的安全启动链。

Part03

受影响设备与缓解措施

确认存在漏洞的芯片包括：

* 苹果A12（iPhone XS、XR，2018款iPad Pro）
* 苹果S4/S5（Apple Watch Series 4/5）
* 苹果A13（iPhone 11系列）

由于BootROM漏洞存在于不可更改的硅片中，任何软件或固件更新都无法修复。迁移至A14或更新硬件是唯一有效缓解方案。研究人员指出，虽然苹果的安全隔离处理器（SEP）提供了额外安全边界，但usbliter8为间接攻击安全隔离区开辟了更广泛途径。

Paradigm Shift在发布前已与苹果产品安全部门协调披露。完整PoC利用代码已公开在其研究仓库中。

参考来源：

New iPhone BootROM Vulnerability Exposes Apple SoCs to Full Chain-of-Trust Compromise

https://cybersecuritynews.com/iphone-bootrom-vulnerability/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1X4enJ3Jg430Lq35ib6TKMfwMWPxpHxMTQkuB9iaHj8Dj755KsjMFZvicpFQEoIcZc5MiblY9MAMfKjrACxXChC1QibqxBjRdYoSAM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3X7WGI2rXPqAzCWXrGjRKsN5yjUV9BoibElELIHDAkotuemLyRebpuqevWQ5EkFXCsicicbVEnB6iaAgd8a7hBYX4m430XS37O4CQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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