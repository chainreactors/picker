---
title: ​RobinBot——快速扩张中的新型 DDoS 僵尸网络
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247504488&idx=1&sn=fb911c33ee57734c02ffbaa1bfc6d7c6&chksm=ea66251fdd11ac091d0a479159142df82a0b5d0b2f5dbc1130256782888652f6b12f95328bf5&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2022-11-23
fetch_date: 2025-10-03T23:30:11.366428
---

# ​RobinBot——快速扩张中的新型 DDoS 僵尸网络

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQusicVqS51eWbPU2l9j5awGNO2hUWhibNiacxXC9thOauh0kUuIJicNZ3ibLg/0?wx_fmt=jpeg)

# ​RobinBot——快速扩张中的新型 DDoS 僵尸网络

原创

威胁情报中心

奇安信威胁情报中心

概述

2022 年 11 月初，奇安信威胁情报中心威胁监控系统监测到一起未知家族恶意样本传播事件。经过我们分析，捕获的恶意样本借鉴了 Mirai 和 Gafgyt 家族的恶意代码，支持多种自己命名的 DDoS 攻击方式，可以通过 Telnet 服务弱口令暴破传播，同时还集成了与 Omni 家族相似的多个漏洞 Exp ，目前正在网上快速传播。

根据攻击者创建的特殊文件夹名称，我们把这个家族命名为 **RobinBot**。

通过对 RobinBot 历史样本的关联分析，我们梳理了它的发展过程，并且发现了其还有一个功能相似的跨平台 **jar** 版本同家族样本。业界公开曝光的 Java 编写的跨平台 DDoS 木马并不多，这次我们对 RobinBot 一探究竟。

我们对 RobinBot 初步的监控结果显示，其作者尝试过下发指令攻击自己控制的 IP 资产。综合分析可以看出 RobinBot 作者具有一定的能力和想法，并在积极尝试中。

C 版样本关键行为分析

RobinBot 的 C 语言版本样本借鉴了 Mirai 和 Gafgyt 家族的恶意代码，并自己命名了多种 DDoS 攻击方式。目前 RobinBot 的样本还在频繁地更新迭代，本文以下面样本为例进行分析：

|  |  |  |  |
| --- | --- | --- | --- |
| **文件名** | **文件类型** | **文件大小** | **文件MD5** |
| x86 | ELF 64-bit LSB executable, x86-64 | 75128552 bytes | 500009D8F68330A8F82B59884A9AFE47 |

**对抗分析**

RobinBot 具有常规的对抗分析措施，借鉴自 Mirai 家族。

GDB 反调试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuicI91vhbdRFSibNEH4qTu8CyJ0iaHuvDPvHCJr0tCicE5ZX3IoM4tnrmxA/640?wx_fmt=png)

进程随机重命名：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuvuDaDvniagoeXCq7oKXWmlANZFx1xqcK8VbjMYaAFwiaLcF4WYiac1RCg/640?wx_fmt=png)

关闭 Watchdog，防止设备重启：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuTwgMVNIfodGVibYNTmHAJqNQ2XialCl7vGpibhCvG3Sms8sV6ic2mibic9yQ/640?wx_fmt=png)

**借鉴自 Mirai 的 table 机制**

RobinBot 的代码中还借鉴了 Mirai 的 Table 机制，试图隐藏自身携带的关键信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuTfx5sFeMhuFfsKJkq9N6oJmMHqkx85uZzcKw9tmKqFOpDT6RTdm4zQ/640?wx_fmt=png)

解码用到的 Key：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQu1dA194C0C8bTlw7RUcqQnPDgicbeZKXjVA7OoWq14v2f0au22o6a15A/640?wx_fmt=png)

经过我们分析，这个 Table 在代码中还没启用，不排除将来作者更新样本，把这个机制真正用起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQu0mGNhnw5etZvLCVuOZSWEV6375cFiccOR2oOibprdibDadXoLibibUgUrEg/640?wx_fmt=png)

**Kill 指定端口的进程**

RobinBot 还会杀掉 Telnet 23 端口、SSH 22 端口和 HTTP 80 端口对应的进程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQu1DN1zL5LRjXO3qqVRTypYXx60czm4UYK1TDhUogTEIz9MXiaDX9wvLA/640?wx_fmt=png)

**传播方式**

RobinBot 支持沿袭自 Mirai 的弱口令暴破方式传播，同时还集成了类似 Omni 家族的 12 个漏洞 Exp，大大提升传播能力。

RobinBot 的 Telnet 弱口令暴破机制，复用了 Mirai 的口令表加密机制：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuucXsYsagnHW9XzNGamMl4tZWUFicEibvboAVgyrVmS69QKHR015Am2WA/640?wx_fmt=png)

暴破结果的 Reporter 服务器地址与 C&C 相同，但端口改成了 **1337**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuPnPKGs8dcfAL17CATbnOFIPtUy99xDqUsBibzhHoh0sZ76HfdggWVQg/640?wx_fmt=png)

RobinBot 集成了 12 个经典的 IoT 设备漏洞 Exp 来增强自身的传播能力：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuzIs0o2icajmC1aibdcTqicuG4scS6rfCiciaPLRnPSElFLsj8dBy6SNyqxQ/640?wx_fmt=png)

漏洞说明如下：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞标签** | **漏洞 ID** | **QVD ID** | **漏洞说明** | **影响设备** |
| GPON8080 | CVE-2018-10561 | QVD-2018-4807 | Dasan GPON 路由器认证绕过漏洞 | Dasan GPON 路由器 |
| GPON80 | CVE-2018-10562 | QVD-2018-5435 | Dasan GPON 路由器认命令注入漏洞 | Dasan GPON 路由器 |
| REALTEK | CVE-2014-8361 | QVD-2014-0175 | Realtek Miniigd UPnP  SOAP 远程命令执行漏洞 | 多种使用 Realtek SDK 并且启用 miniigd 守护进程的网络设备 |
| NETGEAR | EDB-ID-43055 | QVD-2013-7961 | Netgear DGN1000  1.1.00.48 - 'Setup.cgi' 远程命令执行漏洞 | Netgear DGN1000 路由器 |
| HUAWEI | CVE-2017-17215 | QVD-2017-0070 | Huawei HG532 路由器任意代码执行漏洞 | Huawei HG532 路由器 |
| TR064 | CVE-2016-10372 | QVD-2020-74040 | Eir D1000 无线路由器 WAN 侧远程命令注入漏洞 | Eir D1000 无线路由器 |
| HNAP | CVE-2015-2051 | QVD-2015-0260 | D-Link 设备 HNAP SOAPAction-Header 远程命令执行漏洞 | D-Link 设备 |
| CROSSWEB | EDB-ID-39596 | — | 多种 CCTV/DVR 设备的命令执行漏洞 | 超过 70 家供应商的 CCTV, DVR 设备 |
| JAWS | CVE-2016-20016 | QVD-2022-27838 | MVPower DVR  TV-7104HE 1.8.4 115215B9 Shell 命令执行漏洞 | MVPower DVR 设备 |
| DLINK | EDB-ID-28333 | QVD-2013-8037 | D-Link 设备 UPnP SOAP TelnetD 模块远程命令执行漏洞 | D-Link 设备 |
| R7000 | CVE-2016-6277 | QVD-2016-0403 | Netgear  R7000/R6400  'cgi-bin' 模块远程命令执行漏洞 | Netgear R7000/R6400 路由器 |
| VARCON | CNVD-2017-29245 | QVD-2022-34316 | Vacron NVR 设备远程命令执行漏洞 | Vacron NVR 设备 |

**C&C 通信**

RobinBot 当前样本的 C&C 服务器地址 **89.203.251.188:7267**，上线包为 "12354544\n\n"：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQunffmwyHUVGOwKZ6l31t6SibZiaOThI2uEenEwknjNhktdRATGOyHReuw/640?wx_fmt=png)

**指令解析**

RobinBot 的指令机制与 Gafgyt 家族类似，属于明文形式的指令。指令共有三大类：执行恶意命令、发起 DDoS 攻击、辅助功能指令（更新、清理）。

当指令字符串以 "**console**" 开头时，代表执行恶意命令，"**at**" 开头代表发起 DDoS 攻击：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuvau4YcPicfMbpMbAVdghFwXWUOribrjjMmOwLam6SNm1URUFnLlpKoNA/640?wx_fmt=png)

对于目前支持的 6 种 DDoS 攻击指令，RobinBot 作者有自己的命名方式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuz4GzaT1xRZtZiaxsKls7pG49GdcS7XiaKeia5bLeeBgQzVtlRJQTXQyWg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQufpN3pjhUib9pXOHC3D9c5bExCbKicQaNfJ5Vb8azKN0BzTfFZibTlYtwg/640?wx_fmt=png)

支持的 DDoS 方法包括：固定及随机 Payload 的 TCP 协议攻击、固定 Payload 的 UDP 协议攻击以及专门针对 Minecraft 服务器的 DDoS 攻击。上述大部分攻击方式，疑似专为 MineCraft 平台定制，即攻击者运营该 DDoS 僵尸网络，可能专门为了攻击游戏服务器。

值得一提的是，RobinBot 支持的 T-TCP 和 U-UDP DDoS 攻击方式，单次攻击的 Payload 都是 8000 Bytes 的重复数据，形式如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQux6xrS1X97dpGrxcRcT3S5I45LaGsdoNia0nKhQia7khFRUEeVKuZicFkA/640?wx_fmt=png)

C 版样本演进

经过我们对 RobinBot 历史活动的回溯分析，大概理清了 RobinBot C 语言版样本的发展历程。

我们最早找到了 RobinBot 在**2022年5月**份的样本，把它定为最初版本，与本次发现的最新版本大致框架一致，此时的样本中还未添加有 Mirai 的代码，所含的 Telnet 暴破功能也与 Mirai 不同。支持的功能包括远程命令执行、DDoS 攻击、Telnet 弱口令暴破。

上线包如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuv7bqS59P7pTMpNibb17V18nCqIcom48AMAxiaSbN0EnW3Z9yUy4Irbqg/640?wx_fmt=png)

DDoS 方法也仅有 TCP 和 UDP 两种：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuGk4m4l4egxkdaLnCzkwN40oydulsQU4saA4TiaeRSX7olOzjSydpIew/640?wx_fmt=png)

在 **2022年6** **月**份，作者更新了第二版的样本，与初始版本相比加入了 Mirai 的 Table 机制以及其特有的弱口令暴破函数。但是不包含漏洞利用的部分，并且上线包略微不同：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQul9I4b9e29CcMicmt76ntC71lnKXp3F8SI75WKE9aXzloJAmOMxtmvJA/640?wx_fmt=png)

作者在 **2022年7 月**份更新了第三版，加入了漏洞利用，此时仅集成两个漏洞的 Exp，分别是针对 **Dasan GPON** 设备的 **CVE-2018-10562**，和针对 **ZyXEL** 设备的 **CVE-2017-18368**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQufckQ9GbB6DBzf59uPiblMjs2icrESNokADicPFQYLFz4ciaCDEuwicaib6Gg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuiaNwYKYnlL4mDubRVUiauNk31UnLicUCIqE18kliaXrAcaq3POibB78ZSvw/640?wx_fmt=png)

并且，第三版的上线包也有所变化：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQu8egU09cUCZCVwOQLkvr9SiaDoMiaibfzF9hjic7Y2PJyiczHu9KGFV3O7OA/640?wx_fmt=png)

在 **2022年11 月**份我们捕获的最新版样本中，作者去除了 **ZyXEL** RCE 的利用，添加了 Omni 家族曾经整合利用过的 12 个漏洞 Exp 进行传播，同时删除了前两个版本中包含的上报扫描结果 IP 更新的功能。

综合来看，RobinBot C 语言版样本的更新流程如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQugiaTKicLylMVgcKDhMmfJKV9kVT3BLe72ePsdyiae4advnMhkPaibKN7Bw/640?wx_fmt=png)

Java 版 DDoS 木马

在我们对攻击者的资产进行梳理过程中，通过一系列关联分析，我们发现 RobinBot 的作者所属某一资产下发的一个独特的 PE 样本。该样本会调用 curl 命令下载并执行一个 Jar 文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuNlumFHcBurZ3XxEju7xzZSZp5kWCzZEPDibwHKU7hohgeKtzaKVIzxA/640?wx_fmt=png)

RobinBot 的名字，正是我们参考上图 Jar 文件落盘路径中的 "**Robin**" 而命名。经过对上述 Jar 文件的深入分析，确定该样本是上述 C 语言版本的 Java 版本，功能近似，但具备了**跨平台**运行的能力。

我们以下述样本为例进行分析（下文称 **RobinBot-Jar**）：

|  |  |  |
| --- | --- | --- |
| **文件名** | **文件大小** | **文件MD5** |
| asdasasjdhaisuolhdasiuhdai.jar | 4435413 bytes | 27F7000F552B88FCF71E423EC59524B5 |

**区分平台运行**

该样本可以在 Linux 和 Windows 平台上运行，针对 Windows 平台会有额外的操作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicp1jQ09PricibsnNj3SWaYQuVTGibjsudSp5DhJ9nRerib9QI2uOm5vyiadsiajJ3KlYKkR5kZqSnArF5Q/6...