---
title: NVIDIA Vera Rubin NVL72 平台引入 BlueField Astra将可信软件栈与网络策略管控首次延伸至 AI 计算 fabric
url: https://mp.weixin.qq.com/s/6Dtmx5nyzuWtMad8MKXK6Q
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:22:40.287980
---

# NVIDIA Vera Rubin NVL72 平台引入 BlueField Astra将可信软件栈与网络策略管控首次延伸至 AI 计算 fabric

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BuagpZZ9F9qpAT6uMtEJGldQib6GO6pZtNgbjTQ6B20M3lWNOaPpCqibHSpSv1ThIFg3A6gTBZzumgibZctJ783ow/0?wx_fmt=jpeg)

# NVIDIA Vera Rubin NVL72 平台引入 BlueField Astra将可信软件栈与网络策略管控首次延伸至 AI 计算 fabric

BugSec | News
BugSec | News

BugSec

![]()

在小说阅读器中沉浸阅读

随着大模型训练参数量突破万亿级，以及推理吞吐需求的激增，数据中心基础设施正面临前所未有的压力。为了在扩展算力的同时确保租户隔离与安全性，服务提供商急需一种既能管理南北向流量，又能控制东西向算力网络的架构。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BuagpZZ9F9qpAT6uMtEJGldQib6GO6pZt9o1KiaGxFZAVBiaxzibL7LxF2ThqSk8Rbib60udhp2gFcIcm1Dur0kO7GQ/640?wx_fmt=jpeg&from=appmsg)

NVIDIA 在 CES 2026 上展示了其 Vera Rubin 平台中的 BlueField Astra 技术。该方案运行在 BlueField-4 DPU 上，旨在重新定义 AI 基础设施的管理与安全边界。

**关键信息**

* **架构整合：** BlueField Astra 是一种系统级架构，将 BlueField-4 DPU 与 ConnectX-9 超级网卡深度集成，统一管理 AI 计算托盘（NVL72）内的控制平面。
* **控制权下放：** 该技术首次实现了 DPU 对节点所有网络 I/O 的直接控制，将管理、配置和策略执行从主机操作系统剥离，延伸至 AI 算力 fabric。
* **统一控制平面：** 通过 DPU 建立南北向与东西向流量的统一控制点，服务提供商无需触碰主机 CPU 即可完成资源编排和策略下发。
* **安全隔离：** 超级网卡的控制平面被完全隔离在 DPU 中，确保租户即使在裸金属环境下也无法篡改网络配置或绕过安全策略。
* **DOCA 兼容：** BlueField Astra 建立在 NVIDIA DOCA 软件平台之上，允许现有的微服务和工作流无缝扩展至裸金属 AI 系统。

**背景与细节**

在当前的 AI 基础设施中，服务提供商通常利用 BlueField-4 DPU 的 Arm 核心来管理南北向（N-S）流量，并使用专用的以太网超级网卡来处理东西向（E-W）流量。然而，随着 AI 集群规模的扩大，单纯依靠网卡性能已无法满足需求，行业急需一种安全且一致的方式，将管理控制延伸至算力 fabric 本身。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BuagpZZ9F9qpAT6uMtEJGldQib6GO6pZtUtapyG52VuEQB0gmzyzVOxgWp5xkpv84U5iab71th5NBuU2WibEbpUAQ/640?wx_fmt=webp&from=appmsg)

BlueField Astra 的核心突破在于引入了新的控制平面架构。不同于传统模型中主机软件同时配置网卡和 fabric，Astra 将超级网卡的控制平面与主机操作系统完全隔离，仅由 DPU 进行管理。这种设计确保了即使租户运行在裸金属环境，也无法窥探或篡改网络配置。

通过 DPU 与 ConnectX-9 超级网卡之间的专用连接，Astra 建立了一条直接的控制路径。这使得服务提供商能够利用现有的 DOCA 管理工具，将策略推送到超级网卡硬件中执行。这种模式不仅维持了 NVIDIA SuperNIC 的性能优势，还实现了细粒度的租户感知资源分配。

**影响与看点**

BlueField Astra 的最大价值在于它解决了裸金属计算中的安全悖论：既要提供极致性能，又要实现严格隔离。由于控制平面不再依赖主机操作系统，租户无法通过软件手段绕过安全策略，有效防止了横向移动和配置漂移。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BuagpZZ9F9qpAT6uMtEJGldQib6GO6pZt6E5UqE2nVCfSDTcVcGgdWyuxyAKpY1ckrAsEibOjkibSJVmvsbiaLv2xw/640?wx_fmt=jpeg&from=appmsg)

此外，该技术提升了合规性与可审计性。由于策略和配置驻留在 DPU 而非主机上，服务提供商能够获得更清晰的审计追踪，这对于受监管行业尤为重要。这意味着安全不再是事后附加的“补丁”，而是被嵌入到了 AI 基础设施的操作系统中。

资源来自网络，仅作学习交流，如有侵权请联系删除。

> 来源：NVIDIA Developer Technical Blog
>
> https://developer.nvidia.com/blog/redefining-secure-ai-infrastructure-with-nvidia-bluefield-astra-for-nvidia-vera-rubin-nvl72/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BuagpZZ9F9qTgI0SWypDoSaAnkaqq40MBShFmIoXq0KVvUtiaHciaJ8O8NEsXp3hP5t1z3RY6e8ga05KqQEL8NpQ/0?wx_fmt=png)

BugSec

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BuagpZZ9F9qTgI0SWypDoSaAnkaqq40MBShFmIoXq0KVvUtiaHciaJ8O8NEsXp3hP5t1z3RY6e8ga05KqQEL8NpQ/0?wx_fmt=png)

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