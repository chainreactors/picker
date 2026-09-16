---
title: EvidenceForge 工具介绍：生成高可信度的合成网络安全日志
url: https://mp.weixin.qq.com/s/-qTGflTdf97mmdydLmp4MA
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:02:51.443159
---

# EvidenceForge 工具介绍：生成高可信度的合成网络安全日志

# EvidenceForge 工具介绍：生成高可信度的合成网络安全日志

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6P4BDicYhdOnoHjiasfAFpD3JBhDuficUcv48s1eVFRPgaiahicn3WPjTjlKtq5BoxYVeq6NT81QtPLvZTVibUicmicv1GnA75U9Cdqa4w/640?from=appmsg)
> **导语**：网络安全演练和威胁狩猎训练需要大量真实的安全日志，但获取真实数据成本高、隐私风险大。EvidenceForge 由 Cisco Talos（思科塔洛斯）开发，通过 YAML 场景定义生成多格式、高可信度的合成安全日志，让网络安全训练更高效、更安全。

---

![EvidenceForge 生成的合成安全日志示例](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OFLicxK7J7Sptg64tjvqpLFoOUpVGjbPibk9OTjdvD2n4OxVesY8GGxbfIu5pic7C9SMbicmxdIT2FvcSLBqiaKd3dibgmZViczWa908/640?from=appmsg "EvidenceForge 生成的合成安全日志示例")

## 一、工具背景

证据锻造由全球知名的思科塔洛斯威胁情报团队开发和维护，专门解决网络安全演练中的一个核心痛点：**如何获取大量真实的安全日志用于训练，而无需担心隐私泄露或数据不足的问题**。

市面上大多数合成日志生成器生成的日志看起来很"假"——事件之间缺乏关联，时间戳不连贯，攻击痕迹与正常行为完全脱节。证据锻造反其道而行之，采用"活动优先"的架构：先建模真实的环境活动和攻击故事，再渲染出各个传感器会观察到的证据。这种从行为反推日志的思路，让合成数据具备了真实数据的时间线连贯性和跨源关联性。

这意味着你拿到的训练数据不再是孤立的事件 ID，而是有剧情、有时间线、有横向移动痕迹的完整攻击剧本。学生可以在不触碰真实生产环境的前提下，反复演练从初始入侵到权限提升再到数据外传的完整杀伤链。

## 二、核心能力

证据锻造的能力设计直接对准了威胁狩猎和红蓝对抗演练的实际需求，覆盖了从数据生成到质量验证的完整链路：

* **多源证据生成**：从单一 YAML 场景定义同时生成 Windows 安全事件、Sysmon、Zeek 网络日志、EDR、IDS/Firewall 警报、Web/代理日志和电子邮件日志等多种格式。一次建模，全栈输出。
* **跨平台 SMB2/3 活动**：完整建模 Windows 与 Linux 客户端、Windows/Samba 服务器之间的有状态文件共享活动，包括存储拓扑、身份验证、会话管理、访问控制和文件操作。横向移动的痕迹会真实地出现在多个传感器的日志里。
* **可重复的大规模生成**：支持确定性种子、资源预测、进度报告和可恢复检查点。你可以反复重跑同一个场景来调试检测规则，也可以一次性生成 TB 级的数据集用于机器学习训练。
* **基线与攻击场景结合**：可将普通用户/系统活动、无害的干扰项和有类型的攻击事件混合在同一个数据集中，生成的日志既有"噪音"也有"信号"，逼真度直接拉满。
* **验证和质量测量**：在生成前检测 schema、交叉引用、拓扑和容量问题，生成后从四个质量维度评估输出。不合格的批次直接拒掉，不会让垃圾数据流入下游流水线。
* **可重用环境包**：提供行业包（金融、医疗等垂直行业）和组织包（企业内部环境），使不同场景的数据集看起来像是来自同一个真实组织，对训练检测模型尤为重要。
* **完整答案密钥**：每个生成的数据包包含人类可读的 GROUND\_TRUTH.md 和机器可读的 GROUND\_TRUTH.json，详细记录攻击的完整时间线和位置信息。给学生出题、给模型打标签，全都现成。

## 三、支持的日志格式

证据锻造的输出覆盖了企业 SOC（安全运营中心）日常接触的全部主要数据源：

| 日志类型 | 覆盖范围 |
| --- | --- |
| Windows 安全事件 | 30 个事件 ID，覆盖身份验证、进程活动、Kerberos、持久化、账户管理、日志清除等 |
| Windows Sysmon | 事件 1, 3, 5, 7, 8, 10, 11, 12, 13, 22，覆盖进程、网络、模块注入、文件、注册表、DNS 活动 |
| Zeek 网络日志 | 16+ 日志类型，包括连接、HTTP、DNS、SMB、SMTP、TLS 等 |
| EDR 警报 | 端点检测与响应数据 |
| IDS/Firewall | 入侵检测和防火墙警报 |
| 网络流量 | PCAP 级别的网络会话数据 |
| Web/代理日志 | HTTP 请求和代理活动 |
| 电子邮件日志 | SMTP 邮件传输活动 |

这套覆盖范围意味着你可以用同一个攻击剧本，同时训练 Windows 主机侧的检测规则、网络侧的 Zeek 解析器、邮件侧的钓鱼检测模型，三方协同验证。

## 四、系统要求

工具本身的部署门槛非常低，红队日常使用的笔记本就能跑：

* **Python**：3.10 或更高版本（推荐 3.11+）
* **操作系统**：Linux/macOS/Windows（跨平台支持，Kali 上直接可用）
* **磁盘空间**：根据生成场景规模，从数百 MB 到数十 GB 不等
* **依赖**：通过 `pip install -e .` 或 `uv sync` 自动安装

## 五、快速上手

四步就能跑通第一个场景：

```
# 克隆仓库
git clone https://github.com/Cisco-Talos/EvidenceForge.git
cd EvidenceForge

# 安装依赖
pip install -e .

# 查看可用命令
eforge --help

# 生成示例数据集
eforge generate examples/scenarios/basic-baseline
```

## 六、红队视角总结

证据锻造的真正价值不在于"生成日志"这个表层功能，而在于它把"攻击剧本→多源日志"的转化过程标准化了。对于红队，这意味着可以快速构造针对自家蓝队检测能力的标准化测试集；对于蓝队，这意味着可以建立与生产环境解耦但行为模式高度相似的演练靶场；对于安全研究者，这意味着终于有了不依赖真实泄露数据就能训练检测模型的数据来源。

思科塔洛斯这次把威胁情报团队的看家本事开放出来，给整个社区送了一个相当硬核的工具。把它集成进 CI/CD 安全测试流水线，让每次发布都跑一遍攻击剧本验证——这才是这个工具的正确打开方式。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OX26UMkYptyTju129FqCo9rtcEvJGpibO9Vn0icHbGCrqyUzyy3g43EfrVR0vdFxqhd2p1FXoJv0dFs53Ly2wxFXMiabp205tg8w/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PXm7YfAwJ7gqaseVof2SoNjeNrL7JUuva0jCRR58XlaLknGkgQh7A5yIoM8tu0aHJB6aSxwnHzOjiappBlnFLzKjHvB3ics6gLQ/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NrSMWlMJtwMOIbhcTGMWhwcAjibFd0NXGrd1B2uWPMx1vSW1Y6vdA52QibTulv29CYIWGvhOCDuuP5EWlezplMRyKib2Sd1ibCAJo/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MsKCqUKd3dnibIkAN2Skty1pLdfWGQEHHu5dg5dLj1yujd6LyJOaf4B7QofNKuJGrrJ0f8zRFgAk0o0yibFcunhyRLOKze82c1I/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

内容含AI生成图片

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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