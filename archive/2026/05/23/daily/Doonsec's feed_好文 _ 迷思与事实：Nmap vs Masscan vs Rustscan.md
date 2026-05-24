---
title: 好文 | 迷思与事实：Nmap vs Masscan vs Rustscan
url: https://mp.weixin.qq.com/s/u1GHZS9hBmJso18tzRrT0g
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T06:00:22.476108
---

# 好文 | 迷思与事实：Nmap vs Masscan vs Rustscan

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JpU6JH8dicqVsP6ukwib3LbiaShuwbG5yqgyKR2icIOZJWx9EGnK7icGyr44V7gIBY59jR9LvJoG5mrFxpv1ahhAwFneUUZkCykPib2raI7RJ0HEk/0?wx_fmt=jpeg)

# 好文 | 迷思与事实：Nmap vs Masscan vs Rustscan

2s1one
2s1one

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

作者 2s1one 运行了超过 5000 次测试，用实测数据测试三大端口扫描器。

---

## 总结论

* • **Nmap** 在不稳定或有丢包的网络中表现最佳，得益于其智能重试机制
* • **Masscan** 在稳定、高带宽环境中表现出色，但遇到丢包时性能退化明显
* • **Rustscan** 在稳定网络中与其他扫描器相当，但在不稳定场景下不可靠
* • **架构比工具更重要**：合理调参 + 同云部署 + 分布式扫描的组合，带来了 **215 倍** 的加速
* • 将扫描器部署在与目标相同的云厂商，扫描速度提升约 **30%**
* • 单机并行运行多个扫描器实例没有实际收益

---

## 测试环境

为了模拟真实场景，作者从两种不同环境扫描同一个云靶场：

* • **云到云**：快速、高带宽网络
* • **家庭到云**：较慢、不稳定的网络

### 具体配置

| 项目 | 配置 |
| --- | --- |
| 靶标 | 4 台服务器，共 22 个自定义服务（标准 + 非标准端口），部署于 DigitalOcean（多伦多） |
| 云扫描器 | GCP 实例（2 vCPU，8 GB RAM），`us-central1`，Ubuntu 24.04 |
| 家庭扫描器 | Ubuntu Server 24.04（裸金属 + Docker），6 vCPU，40 GB RAM，100 Mbps |
| 工具版本 | Nmap 7.98、Masscan 1.3.9、Rustscan 2.4.1 |

---

## 基线扫描结果

使用接近默认设置扫描全端口：

| 工具 | 云环境 | 家庭环境 |
| --- | --- | --- |
| Nmap | 228 秒 | 464.7 秒 |
| Masscan | 43 分 48 秒 | 43 分 46 秒 |
| Rustscan | 88 秒 | 88 秒 |

> Rustscan 在家庭环境中仅发现 22 个端口中的 11 个。

---

## 云到云测试

### 测试方法

1. 1. 以高扫描速率开始扫描
2. 2. 在该速率下运行 30 次重复扫描
3. 3. 如果任何一次扫描未检测到全部 22 个开放端口，则降低速率
4. 4. 重复直到所有 30 次扫描都稳定检测到全部端口
5. ![](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqVh0hAp3rvuurIaj9lLuWMQMty8uH3LlLmQGkqUeAJ0mR7u6k74jVZur9BbSUbNaQADibMN0kuJQjjntR0osaugmHm1LECeE88Y/640?wx_fmt=png&from=appmsg)

### 结果

在最高稳定速率下，连续 30 次全部检测到 22 个端口的平均耗时：

| 工具 | 平均耗时 |
| --- | --- |
| Nmap | 17.49 秒 |
| Masscan | 18.03 秒 |
| Rustscan | 16.39 秒 |

### 关键发现

* • **机器配置对高速率下的 Nmap 有影响** — CPU 资源不足会导致高扫描速率下扫描不稳定
* • **Docker 开销** — Docker 容器内的扫描表现比宿主机直接运行差
* • **同一云厂商内地理位置影响不大** — 同厂商不同区域几乎无影响
* • **跨云厂商扫描增加延迟** — 不同云厂商之间扫描性能退化

### 结论

在云到云环境下，Nmap、Masscan 和 Rustscan 的性能和准确度大致相当。关键是确保充足的计算资源、直接在宿主机运行、以及使用与目标相同的云厂商。

---

## 家庭到云测试

在网络不稳定的环境中，测试结果出现了明显分化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqV3CRQThKwBj0sWmlQRqtxrkxhNWhF11hs9JAL8dB7PaMQj3km70x6JwuopMn6IJk3nqBssUPxrFYV4hlD3sNY2dkGeULVl5R4/640?wx_fmt=png&from=appmsg)

### Docker 环境结果

在 Docker 环境中达到 ≥99% 准确率的最快配置：

| 工具 | 速率 | 重试 | 运行次数 | 耗时 | 端口数 | 准确率 |
| --- | --- | --- | --- | --- | --- | --- |
| Nmap | 7400 | 1 | 23 | 71.27s | 21.91 | 99.6% |
| Masscan | 3500 | 0 | 31 | 85.72s | 21.94 | 99.7% |
| Nmap | 8400 | 2 | 30 | 94.18s | 21.83 | 99.2% |
| Rustscan | 500 | 0 | 30 | 787.75s | 22 | 100.0% |

### 裸金属环境结果

| 工具 | 速率 | 重试 | 运行次数 | 耗时 | 端口数 | 准确率 |
| --- | --- | --- | --- | --- | --- | --- |
| Nmap | 7600 | 1 | 30 | 69.17s | 21.8 | 99.1% |
| Masscan | 3200 | 0 | 30 | 84.95s | 21.97 | 99.8% |
| Rustscan | 7200 | 1 | 30 | 111.52s | 14.53 | 66.1% |

### 关键发现

* • **Rustscan 在不稳定网络中表现最差** — 在所有测试环境中，包括 Docker 和裸金属，都显示出最弱且最不稳定的表现
* • **Masscan 在高速率下报告重复端口** — 接近最优阈值时偶尔返回同一端口的重复条目
* • **Nmap 重试效率更高** — Nmap 只在响应缺失时重传，而 Masscan 和 Rustscan 总是发送重试包，额外流量增加了开销
* • **重试用速度换准确率** — 在不稳定网络中，较高速率配合少量重试通常优于低速无重试。例如 `3000 pps，0 次重试` 不可用，而 `7000 pps，1 次重试` 达到约 99% 准确率且耗时更短
* • **不要在高速率不稳定网络中使用 `retries = 0`**

### 结论

在不稳定网络条件下：

* • **首选 Nmap**，跨所有配置提供最一致的结果
* • Masscan 适合稳定网络，但遇丢包可能漏端口
* • **Rustscan 在不可靠网络中不适合使用**
* • Docker 内运行可能略微降低性能

---

## 单机并行扫描

测试在同一主机上并行运行多个扫描器进程是否能提升速度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqVibY4QGaCenYicjpIdLCpJKAJibeQTiboUlz6u4tLO6TAuwn0r0hxiaTp2v8432eFYUZIMN1sBPVpoFlAp4wB5JjZKZn302BwQeOIU/640?wx_fmt=png&from=appmsg)

### 结果

| 工具 | 速率 | 重试 | 耗时 | 准确率 |
| --- | --- | --- | --- | --- |
| Nmap（并行 ×2） | 3700 × 2 | 1 | 71.26s | 96.7% |
| Masscan（并行 ×2） | 1600 × 2 | 0 | 92.37s | 99.5% |

对比单进程基线：Nmap 单进程 7400 pps 耗时 71.27s 准确率 99.6%，并行后准确率反而下降。

### 结论

单机并行扫描没有带来改善。准确率受相同的时间和速率阈值限制，网络容量仍然是主要瓶颈。

---

## 分布式扫描

使用 Falcoria（基于 Nmap 的分布式扫描器），4 台扫描机器部署在 DigitalOcean：

* • 4 节点平均耗时：**5.38 秒**
* • 扩展到 8 节点（每目标 2 扫描器，各扫半段端口）：耗时 **5.67 秒**（无改善）

### 关键发现

* • 同云部署使 Nmap 稳定扫描速率提升约 33%（20k vs 15k pps）
* • 分布式扫描接近线性扩展，4 节点约 4 倍加速
* • 增加更多扫描器未能提速，说明目标侧网络容量已达上限

---

## 1000 目标耗时估算

基于实测稳定速率，扫描 1000 个目标的预估耗时：

| 配置 | 4 目标实测 | 1000 目标估算 | 加速比 |
| --- | --- | --- | --- |
| Nmap（家庭，默认） | 464.70s | 32h 16m | ×1.0 |
| Nmap（家庭，调优） | 71.27s | 4h 57m | ×6.5 |
| Masscan（家庭） | 85.72s | 5h 57m | ×5.4 |
| Rustscan（家庭） | 787.75s | 54h 42m | ×0.6 |
| Nmap（云） | 17.49s | 1h 13m | ×26.6 |
| Masscan（云） | 18.03s | 1h 15m | ×25.8 |
| Rustscan（云） | 16.39s | 1h 08m | ×28.4 |
| 分布式 4 节点 | 5.38s | 22m 25s | ×86.4 |
| 分布式 10 节点 | — | 8m 58s | ×215.9 |

**分布式扫描 + 合理调参 + 同云部署 = 215 倍加速。**

---

## 最终结论

### 工具选择

**Nmap** — 全场景可靠之选。不稳定网络中表现最佳，重试值 1-2 通常给出准确率和速度的最佳平衡。

**Masscan** — 稳定高带宽网络的最优解。丢包时需用重试补偿，但会增加网络负载、降低效率。对于典型项目规模（~1000 台主机），结果接近调优后的 Nmap。

**Rustscan** — 稳定网络中与其他扫描器相当。不稳定场景下行为不一致，端口经常遗漏，不适合不可靠网络。

### 架构与网络

* • **网络部署位置** 对扫描时间的影响大于扫描器本身，同云部署提速约 30%
* • **分布式扫描** 是速度和准确率的最佳方案，避免了单机限制且接近线性扩展

### 适用范围

这些结论基于实际安全评估的场景规模（数百个目标），而非全网扫描。在测试中，网络路径是主要限制因素。

---

## 参考链接

* • 原文：Nmap vs Masscan vs Rustscan: Myths and Facts[1]
* • Cloud-To-Cloud 基准测试[2]
* • Home-To-Cloud 基准测试[3]
* • 分布式扫描基准测试[4]

---

*关注公众号，获取更多安全工具深度测评与技术前沿。*

---

**标签：**`#Nmap``#Masscan``#RustScan``#端口扫描``#安全测试``#分布式扫描``#网络安全`

#### 引用链接

`[1]` Nmap vs Masscan vs Rustscan: Myths and Facts: *https://medium.com/@2s1one/nmap-vs-masscan-vs-rustscan-myths-and-facts-62a9b462241e*
`[2]` Cloud-To-Cloud 基准测试: *https://github.com/2s1one/scan-stand/tree/main/benchmarks/cloud-to-cloud*
`[3]` Home-To-Cloud 基准测试: *https://github.com/2s1one/scan-stand/tree/main/benchmarks/home-to-cloud*
`[4]` 分布式扫描基准测试: *https://github.com/2s1one/scan-stand/tree/main/benchmarks/distributed*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/W8BrFJicfTaicbd7kn2cZBgNIaLlk75yrMSYaKQVkia524P5J7BoEBsYWI1XEWOXqDdmMcIzOYWZAiaTaqoSuvZXfg/0?wx_fmt=png)

赛博生存指南

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/W8BrFJicfTaicbd7kn2cZBgNIaLlk75yrMSYaKQVkia524P5J7BoEBsYWI1XEWOXqDdmMcIzOYWZAiaTaqoSuvZXfg/0?wx_fmt=png)

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