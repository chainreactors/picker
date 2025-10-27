---
title: POC公布：Windows驱动程序暴整数溢出漏洞可致权限提升
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787484&idx=1&sn=9c4fcdaa3a27548374d027af4bcfc38d&chksm=8893bc33bfe4352539871ef424161e89f3c548991f974353b109d29e5fa176fbbe8cd06c1c55&scene=58&subscene=0#rd
source: 安全客
date: 2024-11-30
fetch_date: 2025-10-06T19:16:07.157224
---

# POC公布：Windows驱动程序暴整数溢出漏洞可致权限提升

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb59WoxddDT09tshuu9wz6WacQslfeuadssYicgsyWAAgJXC0etH9JtPp3doVXZ1le97eB7djRyXYiaQ/0?wx_fmt=jpeg)

# POC公布：Windows驱动程序暴整数溢出漏洞可致权限提升

安全客

一名独立研究员近期发现了Windows操作系统中ksthunk.sys驱动程序的严重漏洞，该驱动程序负责32位与64位进程间的通信，此漏洞允许攻击者通过整数溢出实现权限提升。该研究员近日在TyphoonPWN 2024大赛中演示了该漏洞的利用，斩获大赛第二名。

该漏洞存在于

CKSAutomationThunk::ThunkEnableEventIrp函数中，该函数用于在内核中分配缓冲区以处理输入和输出数据。然而，由于在缓冲区大小对齐计算时缺乏整数溢出的验证，导致分配的缓冲区尺寸不正确，进而触发堆内存溢出。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb59WoxddDT09tshuu9wz6Wabo6qIwR3ROktdwrdXiaSBTTcoNicWiaVibL8E9JP7Q8gJIzUN4N9XIWy7A/640?wx_fmt=jpeg&from=appmsg)

漏洞代码关键点如下：

```
// Only Called when the calling process is 32bit.__int64 __fastcall CKSAutomationThunk::ThunkEnableEventIrp(__int64 a1, PIRP a2, __int64 a3, int * a4) {        ...        inbuflen = CurrentStackLocation -> Parameters.DeviceIoControl.InputBufferLength;        outbuflen = CurrentStackLocation -> Parameters.DeviceIoControl.OutputBufferLength;        // [1]. Align the length of output buffer        outlen_adjust = (outbuflen + 0x17) & 0xFFFFFFF8;        if (a2 -> AssociatedIrp.MasterIrp)            return 1 i64;
        if ((unsigned int) inbuflen < 0x18)            ExRaiseStatus(-1073741306);
        ProbeForRead(CurrentStackLocation -> Parameters.DeviceIoControl.Type3InputBuffer, inbuflen, 1 u);        if (( * ((_DWORD * ) CurrentStackLocation -> Parameters.DeviceIoControl.Type3InputBuffer + 5) & 0xEFFFFFFF) == 1 ||            ( * ((_DWORD * ) CurrentStackLocation -> Parameters.DeviceIoControl.Type3InputBuffer + 5) & 0xEFFFFFFF) == 2 ||            ( * ((_DWORD * ) CurrentStackLocation -> Parameters.DeviceIoControl.Type3InputBuffer + 5) & 0xEFFFFFFF) == 4) {            // [2]. Validate the Length            if ((unsigned int) outbuflen < 0x10)                ExRaiseStatus(-1073741306);            if (outlen_adjust < (int) outbuflen + 16 || outlen_adjust + (unsigned int) inbuflen < outlen_adjust)                ExRaiseStatus(-1073741306);
            // [3]. Allocate the buffer to store the data            // 0x61 == POOL_FLAG_USE_QUOTA | POOL_FLAG_RAISE_ON_FAILURE POOL_FLAG_NON_PAGED            a2 -> AssociatedIrp.MasterIrp = (struct _IRP * ) ExAllocatePool2(                0x61 i64,                outlen_adjust + (unsigned int) inbuflen,                1886409547 i64);            a2 -> Flags |= 0x30 u;            ProbeForRead(a2 -> UserBuffer, outbuflen, 1 u); // [*]             data = (__int64) a2 -> AssociatedIrp.MasterIrp;            ...            // [4]. Copy the Data            if ((unsigned int) outbuflen > 0x10)                memmove((void * )(data + 0x20), (char * ) a2 -> UserBuffer + 16, outbuflen - 16);            memmove(                (char * ) a2 -> AssociatedIrp.MasterIrp + outlen_adjust,                CurrentStackLocation -> Parameters.FileSystemControl.Type3InputBuffer,                inbuflen);            ...        }
```

SSD Secure Disclosure技术团队指出：

在代码片段[1]处，outlen\_adjust的计算缺乏整数溢出验证，这可能导致分配过小的缓冲区。

在[4]处，当数据被复制到不正确的内存位置时，会触发堆内存溢出，最终导致内核内存损坏并允许进一步利用。

研究员展示了一种详细的利用方法，通过以下步骤实现权限提升：

内存操控：在内核非分页池中创建间隔，以便利用溢出攻击命名管道对象。

任意内存访问：通过破坏邻近内存对象（如命名管道），获取任意读写权限。

令牌覆盖：修改当前进程的令牌，将权限提升为SYSTEM，从而完全控制目标机器。

微软已收到该漏洞的通知，但回应称这是一个已经被修复的重复问题。然而，研究员在Windows 11 23H2中发现漏洞仍可利用。至今，微软尚未分配CVE编号，也未提供详细的修复信息。

内核级漏洞的存在为高级威胁行为者提供了便捷的攻击途径。该漏洞通过对分配缓冲区大小的精确操控，加上容易利用的内存破坏特性，攻击难度相对较低，适合作为后续攻击链中的关键环节。

专家建议，开发者在内核代码中应严格执行整数溢出的验证，特别是在内存分配和使用时，确保分配大小的安全性。系统管理员则需限制驱动访问，仅允许经过验证的驱动加载，以减少潜在的攻击面。此外，企业和个人用户应部署安全工具实时监控内核异常行为，并及时应用系统更新和补丁，以最大程度降低漏洞被利用的风险。面对权限提升漏洞的威胁，这些防护措施将是保护系统安全的关键环节。

更多技术细节及漏洞利用的PoC代码可参见SSD Secure Disclosure的官方公告。

文章参考：

https://securityonline.info/integer-overflow-vulnerability-in-windows-driver-enables-privilege-escalation-poc-published/

**推荐阅读**

|  |
| --- |
| **01**  ｜[星巴克遭供应链攻击被迫回归纸笔时代](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787474&idx=1&sn=849c75157b64bc5027ef6186f490c805&scene=21#wechat_redirect) |
| **02**  ｜[财富1000强企业的API暴露风险与漏洞挑战](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787467&idx=1&sn=a415a569eadfb841c7db9ab18a3b9dee&scene=21#wechat_redirect) |
| **03**  ｜[合法安全驱动程序武器化](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787441&idx=1&sn=dbc4fcc0a87e9e439ff0c365baac33ec&scene=21#wechat_redirect) |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb59WoxddDT09tshuu9wz6WauWhEbgUONSMsCMEJcVwumvp8Fr0kABgVSdPw3wdLCOTibr73Ev6RBaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb59WoxddDT09tshuu9wz6WaUSoiczqXTnbrN6eH4YKfia7QCeoQv9WRCgI6ScwKbHG3leDdXzvkbjug/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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