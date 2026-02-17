---
title: Windows 事件日志被清除后因未初始化内存 bug 在无关日志文件中复活
url: https://mp.weixin.qq.com/s/zXcKmS3Q3yKyUUQagD02xg
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:17:03.107815
---

# Windows 事件日志被清除后因未初始化内存 bug 在无关日志文件中复活

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSiaVLoCmjhibcmnicwc043je9NzH5VHIGhZCHUHbL3JianFMibuDb2c44hM4HuYz3Iz2zFEkRGeu2z4Tu860sToXU9XExfvtOTJQC0s/0?wx_fmt=jpeg)

# Windows 事件日志被清除后因未初始化内存 bug 在无关日志文件中复活

MAXIM SUHANOV
MAXIM SUHANOV

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://dfir.ru/2026/01/26/windows-event-logs-were-cleared-but-resurrected-in-another-file/ | MAXIM SUHANOV |

*TL;DR:*

Windows 事件日志服务存在一个 bug (使用了未初始化内存)，有时会导致刚被删除 (清除) 的日志条目被意外写入其他无关的 *\*.evtx*日志文件中。触发条件是：当一个很少更新的 *\*.evtx*日志文件被清除后，其新分配的空 (即不含任何日志条目的) ElfChnk 区域会被事件日志服务内存中的残留数据填充，其中可能包含从其他日志 (同样是最近被清除的) 中"复活"的条目。一旦该区域写入了第一条新日志条目，残留部分就会被擦除——因此"复活"的日志条目在第一条新条目写入后就会消失，这也解释了为什么该 bug 仅在很少更新的日志文件中才能被实际观察到。

在一次 DFIR 案例中，我发现入侵者在多台机器上清除了所有 *C:WindowsSystem32winevtlogs\*.evtx*日志文件。在进一步检查从其中一台机器采集的 *\*.evtx*文件时，我注意到 *Microsoft-Windows-Application-Experience%4Program-Inventory.evtx*日志文件中竟然包含来自完全不相干的事件源的日志条目：\_Microsoft-Windows-TerminalServices-LocalSessionManager\_！这些异常条目被标记为未分配状态 (即以已删除条目的方式存储)，但使用 libevtx 库可以轻松提取并解析它们，从而揭示了我想要了解的关于该机器所有 RDP 入站连接的信息...

在其他机器上也观察到了相同的现象：入侵者清除了所有 *\*.evtx*文件，但 RDP 日志竟以已删除条目的形式重新出现在了完全无关的日志文件中！

*我成功复现了这一行为，以下是我的观察结果...*

在一台全新安装的 Windows 11 机器上，我清除了 *Microsoft-AppV-Client%4Operational.evtx*日志文件，然后关机。测试过程中我采集了两份磁盘镜像：清除日志前的状态 (*before*状态) 和最终关机后的状态 (*after*状态)。

以下是关键发现：

* *Microsoft-AppV-Client%4Operational.evtx*

  文件在 *before*和 *after*两种状态下对应的是同一条文件记录，具有相同的 *Created*时间戳，数据占用相同的簇号。这说明清除操作并没有删除后重建该文件 (即它仍然是同一个文件，只是数据内容发生了变化)。
* 在 *before*状态下，该文件不包含任何已分配的日志条目。数据的 HEX 转储如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjh2mdfYCnzvzaFASnA1Dicib6MxS7cuXU2LicZ0jJa4TWmPvHRmFUOx2mkjllTYGRH14lvmunoWibJKVu9EiaroxzOkwCuOufPLibTc/640?wx_fmt=png&from=appmsg)

* 在 *after*状态下，该文件具有如下数据 (同样没有已分配的日志条目，但可以在 *ElfChnk*签名之后看到一些残留数据)：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSg8CaBQSibxWUZtyT0P4AKSLpSu2du7IQwUSU104Wia4fbJjeFTVet6ruHh1icGZPRhcRdSv5zfg8Pz7icibz3bfT4ibKr4AyxCb5kNU/640?wx_fmt=png&from=appmsg)

(注意：0x1030 字节处的值是 "Free space offset" 字段，其值为 "00 02" 即 0x200，残留数据从 0x1200 字节处开始。)

* *evtxexport*

  工具对该文件的输出如下：

```
$ evtxexport mnt/Windows/System32/winevt/Logs/Microsoft-AppV-Client%4Operational.evtx
evtxexport 20181227

No records to export.

$ evtxexport -m all mnt/Windows/System32/winevt/Logs/Microsoft-AppV-Client%4Operational.evtx
evtxexport 20181227

Event number   : 1
Written time: Jan 25, 2026 03:50:47.860608300 UTC
Event level   : Information (4)
User security identifier : S-1-5-18
Computer name   : WIN-H8P4PBR8U4V
Source name   : Microsoft-Windows-BitLocker-API
Event identifier  : 0x0000032a (810)
Number of strings  : 0

Event number   : 2
Written time: Jan 25, 2026 03:50:47.861420900 UTC
Event level   : Information (4)
User security identifier : S-1-5-18
Computer name   : WIN-H8P4PBR8U4V
Source name   : Microsoft-Windows-BitLocker-API
Event identifier  : 0x0000032a (810)
Number of strings  : 0

Event number   : 3
Written time: Jan 25, 2026 03:50:47.886561600 UTC
Event level   : Information (4)
User security identifier : S-1-5-18
Computer name   : WIN-H8P4PBR8U4V
Source name   : Microsoft-Windows-BitLocker-API
Event identifier  : 0x0000032a (810)
Number of strings  : 0

Event number   : 4
Written time: Jan 25, 2026 03:50:47.888014000 UTC
Event level   : Information (4)
User security identifier : S-1-5-18
Computer name   : WIN-H8P4PBR8U4V
Source name   : Microsoft-Windows-BitLocker-API
Event identifier  : 0x0000032a (810)
Number of strings  : 0

Event number   : 5
Written time: Jan 25, 2026 03:50:47.927408900 UTC
Event level   : Information (4)
User security identifier : S-1-5-18
Computer name   : WIN-H8P4PBR8U4V
Source name   : Microsoft-Windows-BitLocker-API
Event identifier  : 0x0000032a (810)
Number of strings  : 0
```

这些条目来源于 *Microsoft-Windows-BitLocker-API\_，与实际存储在*C:WindowsSystem32winevtLogsMicrosoft-Windows-BitLocker%4BitLocker Management.evtx\_ 文件中的条目完全一致。后者在整个测试过程中从未被操作过 (未被清除)，但其内容却不知何故被复制到了 *Microsoft-AppV-Client%4Operational.evtx*文件中...

以下是两个文件的对比，显示从 0x1200 字节处开始数据完全相同 (只是 *Microsoft-AppV-Client%4Operational.evtx*文件的非零字节更少)：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaRzpuJdQT6UFUnHXZfxlfEcEb8RB2354PfX3ERVmk6ac33BHAiczVu79ibJ4Rc24tVGyFMN8NeGibphRhn5jZnfIdfaQoDaTTFr0/640?wx_fmt=png&from=appmsg)

显然，这是一个内存安全 bug——未初始化的数据被写入了磁盘。不过，该 bug 并未跨越安全边界，因此不构成安全漏洞 (非特权用户无法通过清除自定义日志文件来获取其他特权日志中的数据)。

根据调试结果，部分初始化的 *ElfChnk*chunk 来自 *wevtsvc.dll*库中的 *File::MapInNewWriteChunk()*函数。

示例 *\*.evtx*文件 (即本文中提到的文件) 可在此处下载 (均取自 *after*状态)：

* https://github.com/msuhanov/articles/raw/refs/heads/master/misc/Microsoft-AppV-Client%254Operational.evtx
* https://github.com/msuhanov/articles/raw/refs/heads/master/misc/Microsoft-Windows-BitLocker%254BitLocker%20Management.evtx

**结论**

务必采集所有 *\*.evtx*文件！务必解析和检查所有 *\*.evtx*文件！

未初始化内存可以成为极有价值的取证痕迹...

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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