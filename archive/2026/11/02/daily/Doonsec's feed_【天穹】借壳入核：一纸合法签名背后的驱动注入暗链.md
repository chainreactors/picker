---
title: 【天穹】借壳入核：一纸合法签名背后的驱动注入暗链
url: https://mp.weixin.qq.com/s/vZDyQLBrn0BOGMVJiHLN3Q
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:49:33.414326
---

# 【天穹】借壳入核：一纸合法签名背后的驱动注入暗链

# 【天穹】借壳入核：一纸合法签名背后的驱动注入暗链

星图实验室
星图实验室

奇安信技术研究院

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一、概述

当前，攻击者正越来越多地把战场从应用层下沉到内核层。

原因并不复杂：内核驱动拥有最高权限，可以直接读写任意进程内存、结束安全软件进程、绕过用户态防护；而 Windows 对驱动加载的第一道门槛，是**数字签名**。于是，“带着合法签名做恶意的事”——BYOVD（Bring Your Own Vulnerable Driver，自带易受攻击驱动）——成为黑产手中性价比极高的武器。

本次分析的 `OrayVGR.sys` 正是这一趋势的典型样本：它持有**有效的微软 WHQL 签名**，被天穹沙箱多引擎判定为恶意驱动，样本库家族标记为 `Injecto`，THASH 云查置信度 100%，并关联到 **13 个已知变种样本**。

更值得关注的是它的“隐身术”：驱动内部没有常规的 IOCTL 攻击面，恶意逻辑全部藏在内核系统线程里；真正的载荷容器被塞进证书表的尾部。换句话说，**用签名校验和 IOCTL 监控这两把传统尺子，都量不出它的恶意**。

![图1 天穹沙箱综合研判：多引擎判定为恶意驱动](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdtbVetYtwu10gJnFrRodCyqibvnGZABZN1xFmiaYGRuZn6nRQzmSyyHdqJtb3PlU41VLAAV2Q3zCOb6jRgDfn8JicIsKluvu1gIU0/640?wx_fmt=png&from=appmsg)

图1 天穹沙箱综合研判

# 二、样本信息

| 项目 | 内容 |
| --- | --- |
| 样本名 | `OrayVGR.sys` （内部名 `z_driver.sys`） |
| 文件类型 | PE32+ 原生驱动（x64.sys，Windows 内核驱动） |
| 文件大小 | 1.04 MB（1,086,240 字节） |
| MD5 | `c041033fb4dc42f0c8da90e1c01b5517` |
| SHA1 | `67383562c089146316553de856b6bf4a3baab1ee` |
| SHA256 | `f7703ae9a53aea278603fc064e4469255be774ca78fe710837d8b33e6aa0e738` |
| PDB 路径 | `D:\programs\out\z_driver2\x64\Release\z_driver.pdb` |
| 签名信息 | Microsoft Windows Hardware Compatibility Publisher（签名合法，2026-06-08） |
| 样本家族 | `Injecto` / `Trojan.Generic` |

**第一处“反常”就藏在签名里。** 报告显示：文件“有签名，签名合法”，证书链完整指向微软根证书，签发者为 Microsoft Windows Hardware Compatibility Publisher。

但再往下看：版本信息自称 `z_driver Filter Driver`，PDB 路径直接暴露了 `z_driver2` 工程目录，节区中出现可疑的 `INIT` 段，文件熵高达 7.97——这些特征与“正规微软驱动”格格不入。

合法签名，成了它最好的伪装。

![图2 签名合法但行为可疑：WHQL 证书链与泄露的 PDB 路径](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdulzdjatHHO2Wo8w90roDvBRxjZFtSvr5qGV16CnpkKoltHVVDP82bJM5y84jLKbGnZErDEWztgfSh5lgPCydgt77LgmxAFANI/640?wx_fmt=png&from=appmsg)

图2 签名状态与证书链

# 三、攻击链拆解：四层伪装，一条闭环

## 3.1 第一层：伪装成 NetBT 网络组件

驱动入口 `DriverEntry` 完成初始化后，立即创建了一个设备对象与符号链接：

* 设备名：`\Device\NetBT_Tcpip_{4B12DADF-4BDD-41FD-C12A-242DF3E12A9B}`
* 符号链接：`\DosDevices\{E27623AA-8765-CF98-1887-87112CDE0912}`

命名模仿 Windows 的 NetBT（NetBIOS over TCP/IP）网络组件，让驱动在进程与模块列表中“看起来像系统的一部分”。

这两个 GUID 并非每次运行随机生成，而是以硬编码方式固定存在。天穹沙箱在动态分析过程中捕获到了设备名的创建行为；随后，天穹智能体通过逆向解密相关字符串，确认其与静态分析结果逐字节完全一致。这一 “动态观测 + 静态验证” 的交叉比对，形成了相互印证的闭环证据链。

## 3.2 第二层：一个“没有 IOCTL”的恶意驱动

常规驱动分析的第一反应，是找 `DeviceIoControl` 分发函数和 IOCTL 码表。但 OrayVGR 把这条路堵死了。

天穹智能体分析显示，该驱动将 28 个 IRP 分发槽统一指向同一个桩函数：除 CREATE、CLOSE、CLEANUP 三类请求外，其余请求一律返回 STATUS\_INVALID\_DEVICE\_REQUEST。由此表明，真正的恶意逻辑并不位于 IRP 分发路径中，而是在 DriverEntry 创建的内核系统线程内执行。

这解释了一个很典型的现象：**如果在沙箱里只盯 IOCTL 通信，这个样本看上去“什么都没干”。**

而天穹沙箱的动态行为监控记录下了另一条完整链路：

![图3 动态行为明细：从进程创建、驱动符号链接到跨进程注入](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdvuGvbOwlzR3ibPU52KZdO35xuzRobnYDqMicvsHuiaiasUWia4jKL1hItDgrMUh3XyToqnPZmIUe5V4yz2B5xoaND6zTSJehNiaphWQ/640?wx_fmt=png&from=appmsg)

图3 动态行为明细

## 3.3 第三层：载荷藏进证书表尾部

驱动内部嵌入了一个 **999,508 字节**的容器。该容器既不位于 `.text` 节区，也不在资源段中，而是被附加在 PE 证书表中。

这一位置的选择具有明显的规避检测意图：Authenticode 的 Authentihash 计算**不覆盖证书表**内容，因此，修改该区域内的容器并不会改变 Authentihash，原有签名也可能继续通过验证。这使得样本能够在维持相同签名指纹的同时，持续迭代内部载荷。

PE 文件结构热力图进一步呈现了文件内部的数据分布特征，加壳与高熵区段清晰可见，静态特征与合法签名形成强烈反差。

![图4 PE 文件结构热力图：高熵区与异常节区分布](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdudUAsVCwV7HxlRJJpzRw6UA8h7kQzWY9wibXwlBQRTnUelGvkcgMDCeiblxqJEm0KANdHjwy2FOib8PqQkwhjviad1LZLeOibnwibfA/640?wx_fmt=png&from=appmsg)

图4 PE 文件结构热力图

天穹智能体通过情报检索进一步印证了这一判断：以相同 Authentihash 聚类，共命中 **16 个同源驱动样本**（2026-06-08 至 2026-10-13）。样本共享相同的签名指纹，但内部载荷持续演进，呈现出明显的同源同签、载荷迭代特征。

容器本身经过两层加密：外层以 `XOR 0xAA + zlib` 解出 `key1–key6`，内层再以 `XOR 0x55 + zlib` 还原出 rundll32 启动桩、`wdscore.dll`、`livemod.bin` 以及 x86/x64 shellcode。配置中还明确记录了渠道号 `chann=z01`、服务名 `srvname=OrayVGR`，以及下载地址 `__mdu=http://chrome.jmwze[.]com/fy.dll`。

## 3.4 落地与注入：一条完整的执行链

容器解密后，样本向磁盘释放三件套，并完成多层注入：

1. **释放**

   ：`C:\Windows\Temp\rundll32.exe`（伪启动器）、`vminstd.tmp`（聚合载荷）、`wdscore.dll`（侧加载 DLL）；
2. **注入**

   ：向系统关键进程 `services.exe` 注入；向 `rundll32.exe` 跨进程写入内存并恢复线程执行；向 `SysWOW64\svchost.exe` 分配 RWX 内存、写入 PE 并创建远程线程；
3. **驻留**

   ：写入注册表 `HKLM\SOFTWARE\Microsoft\sense = z01`，创建互斥体 `Global\WindowsAutoUpdateInternals`，并读取 `ImagePath` 等系统信息；

天穹沙箱的进程树与行为关系图，把这条链路完整串了起来：

![图5 进程树与行为关系图：注入链与网络行为一图可见](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdsEmCU4qQA8ibu7t5pzazVHau6Z9MVSk57GFmeDESiaeKQQWXCzMt2CMSQjMbJzUtGoOEsGRvzDIqRvwnicEDzqaAzlTz0H9KMna8/640?wx_fmt=png&from=appmsg)

图5 进程树与样本动态行为关系图

## 3.5 回连与分发：C2 背后是一个 PPI 平台

网络侧，样本表现出“下载层 + 控制层”分离的结构：

* **下载层**

  ：`chrome.jmwze[.]com` 经 DNSPod / TDNS 视频 CDN 前置，隐藏真实回源，最终从 `106.225.234.155[:]80` 下发 `fy.dll`；
* **控制层**

  ：`ww8.win1c1.com[:]7788`（`45.119.4[.]220`）承担探活与主机指纹上报；

天穹智能体进一步拓线发现，`ww8.win1c1.com[:]7788` 同时服务 `Injecto`、`sbadur`、`tedy`、`Doina`、`c312999b` 五个家族，共用同一套 API、GUID 与版本号，`ch` 字段为渠道编号（本例为 `z01`）。这说明它并非单一木马的专用 C2，而是一个**按安装付费（PPI）的推广分发平台**。

![图6 联网活动统计与域名解析链](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdtIZiaBwzE4lichoWpYTmUicoveLiafNmZcIfVEd1bYOH4E7Pt7xQNtyuwhPN2jW8rhWVATw7PNnnF0ePGelcydu7icCicaa2G0abEv8/640?wx_fmt=png&from=appmsg)

图6 联网活动统计

# 四、天穹沙箱的分析能力

## 4.1 内核行为监控：看见“没有 IOCTL”的恶意

该驱动没有暴露任何的 IOCTL 通信接口，天穹沙箱依然完整捕获了驱动加载、设备与符号链接创建、内核系统线程启动、临时文件释放、跨进程内存写入、远程线程创建等底层行为。

配合 ATT&CK 矩阵，样本的战术意图一目了然：

![图7 ATT&CK 攻击矩阵：执行、提权、防御绕过、命令与控制多点命中](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdtRFNENNbKeKn9uRia6Mt1ZT2DWmbBtzc2ovmufAzgfTUAEicXN7pkOOmwwVR1lMMFwCMcjVkqAwKUfBA1j88A8KficR2dq3GMENA/640?wx_fmt=png&from=appmsg)

图7 ATT&CK 攻击矩阵

## 4.2 天穹智能体协同：两小时走完过去数天的路

这个样本的分析，完整跑通了天穹智能样本分析平台的多智能体流程：

* **主智能体（Orchestrator）**

  负责任务拆解、进度调度与结果汇总；
* **沙箱分析专家**

  投递样本、提取动态行为与 IOC；
* **逆向分析专家**

  通过深度逆向，还原 DriverEntry 执行流、IRP 分发语义、字符串解密算法与容器结构；
* **情报分析专家**

  完成 IOC 拓线、同源聚类与活动归因。

四个角色通过共享黑板（Blackboard）交换上下文，中途还发生过一次有价值的“相互纠错”：沙箱侧认为设备 GUID 是运行时随机生成，逆向侧解密字符串后证明其硬编码，情报侧独立复核后确认——**动态、静态、情报三方交叉验证，结论才真正可信**。

![图8 天穹多智能体拓扑：主智能体 + 三名专家协同](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdv3G1t6anJKiaxd67WUWqpFVyULCrkVGRgaibtB01PKFz0L3DxFpiaFjtZmIbwW73YqtiaprOMq6vGyTpcDYzh2yUzcHHzcicP8hwq0/640?wx_fmt=png&from=appmsg)

图8 天穹多智能体拓扑

## 4.3 从“单样本”到“整条产业链”

以驱动 Authentihash 为锚点，情报侧把一次样本分析扩展成了一次产业链测绘：

**16 个同源样本**：伪装名横跨 Oray 远控、网卡与声卡驱动、反作弊组件等命名域（`orayvgr.sys`、`cet.sys`、`nvhda64c.sys`、`ace-advc.sys` 等）；

**签名演进**：从 Verokey CA 到微软 WHQL，工程路径由 `z_driver` 升级为 `z_driver2`；

**投放节奏**：该样本的编译、签名与投放于同日完成，且在签名后约 4 小时即出现同源变体，整体呈现出高度自动化的流水线作业特征。

![图9 情报拓线结论：16 个同源样本与 PPI 平台归因](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdszTkv8Ke4NzWa9951lXl08jCQag4aEibRGN9w6PxdbNrXW2EepjqoQYZTy9gwqT8zW9H4uYNn3F80g4icETqAgok70FP0hZ5PmM/640?wx_fmt=png&from=appmsg)

图9 情报分析专家阶段结论

# 五、IOC

**恶意文件（MD5）**

```
c041033fb4dc42f0c8da90e1c01b5517 OrayVGR.sysfbd07354e3ecd632bbc9b49da0067fc5 rundll32.exe08cd6fd4210c6c75274848a1f21b210a vminstd.tmpf0ea686e874415cc719c475f8d0ce13f wdscore.dll
```

**恶意 IOC**

```
hxxp://chrome[.]jmwze[.]com/fy.dllww8.win1c1.com[:]778845.119.4.220[:]778845.119.4.206[:]17219106.225.234.155[:]80
```

**报告链接**

分析报告：

https://sandbox.qianxin.com/tq/report/toNewReport.do?rid=fc263afa1413712ca2aa412b98489891&index=1&sk=26862944

天穹智能分析平台**（联系我们申请账号）：https://sandbox.qianxin.com**

天穹智能分析平台持续迭代升级，致力于为每一位样本分析人员打造更高效、更智能、更易用的分析平台——这始终是我们不变的初心与追求。

如果您希望深入了解平台功能，或在使用过程中遇到任何问题，欢迎随时联系我们。您的反馈，是我们进步的重要动力！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lG0evzxL96k3J9EIwMqhiacpDHibsxFTCugUuHF9VUnGG5ceic7dILO41pMNfer7OzCyIviaBYAWAZicicVfocuO8HKw/0?wx_fmt=png)

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