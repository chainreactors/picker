---
title: Clearcam：不换摄像头，给现有 RTSP 监控加上本地 AI
url: https://blog.upx8.com/Clearcam-RTSP-AI
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-01
fetch_date: 2026-11-02T08:33:02.189727
---

# Clearcam：不换摄像头，给现有 RTSP 监控加上本地 AI

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)

[首页](https://blog.upx8.com)
/
[资源](https://blog.upx8.com/Free)
/
Clearcam：不换摄像头，给现有 RTSP 监控加上本地 AI

# Clearcam：不换摄像头，给现有 RTSP 监控加上本地 AI

[资源](https://blog.upx8.com/Free)
11-01
·
约 11 分钟
·
黑海洋
·

4,935

家里或办公室已经装了 IP 摄像头，通常只能录像和回放。想再加人车识别、目标追踪，或者按画面搜索以前的录像，往往要换摄像头、换 NVR，或者接入厂商云服务。

Clearcam 换了一个思路：摄像头继续用，录像链路也不用推倒重来。它通过 RTSP 读取现有监控画面，在自己的电脑或服务器上完成 AI 目标检测、追踪和录像搜索。

如果手里已经有支持 RTSP 的摄像头，还有一台闲置的 Mac、Linux 主机或家庭服务器，这套方案值得试。

**项目官网：**[https://clearcam.org](https://blog.upx8.com/go/aHR0cHM6Ly9jbGVhcmNhbS5vcmc)

**GitHub：**[https://github.com/roryclear/clearcam](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3JvcnljbGVhci9jbGVhcmNhbQ)

![Clearcam 官网展示的开源 AI NVR 项目主页](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/750658f3adb40c269b60d53d4fb10815.jpg)

*Clearcam 官网首页，展示了目标检测、区域设置和录像搜索等核心能力。*

## 先说结论：适合谁，不适合谁

| 适合 | 不适合 |
| --- | --- |
| 已有支持 RTSP 的 IP 摄像头 | 摄像头只支持厂商私有协议，没有 RTSP |
| 有 Mac、Linux 主机或家庭服务器 | 只打算用 Windows，且不想处理 FFmpeg 环境 |
| 接受用 Python 源码部署 | 必须要求一条 Docker Compose 命令启动 |
| 想在本机完成 AI 检测和录像分析 | 必须依赖 Home Assistant 官方集成或完整生态 |

Clearcam 的定位很明确：它不是要替代所有 NVR，而是给现有 RTSP 监控补上一层本地 AI。上手路径更短，但 Python 环境要自己维护，生态和配套还不如 Frigate 完整。

## Clearcam 是什么？

NVR 的工作是接收 IP 摄像头的视频流、保存录像，并提供实时查看和回放。Clearcam 在这些基础功能上增加了本地 AI 分析层。

它目前提供这些能力：

* AI 目标检测；
* 目标持续追踪；
* 用相似图片或上传图片搜索历史录像；
* AI 事件通知摘要；
* 移动端事件通知；
* 远程查看实时画面；
* 远程查看事件录像。

和传统 NVR 最大的区别在“检索”。普通 NVR 找录像主要靠时间轴，先回忆大概几点，再一段段拖回去。Clearcam 会先识别画面里的人和车，再让你按目标图像去搜索，录像越多，这种方式的优势越明显。

截至 2026 年 11 月 1 日，项目在 GitHub 上有 2,217 Stars、224 Forks，采用 GPL-3.0 许可证。公开代码遵循 GPL-3.0，官方 Premium 云服务和移动端功能则按 Clearcam 自己的服务条款提供。

## 接入条件：RTSP 是硬门槛

Clearcam 对摄像头的要求可以归纳成一句话：**摄像头必须能提供 RTSP 视频流，运行 Clearcam 的主机必须能访问这个流。**

符合条件的情况包括：

* 标准 IP Camera；
* 支持 RTSP 的家用摄像头；
* 已经搭好的网络监控系统；
* 原有 NVR 可以转发 RTSP 流。

如果摄像头完全依赖厂商 App，只提供私有协议，又没有开放 RTSP，就不能直接接入 Clearcam。

部署前先用 VLC、FFmpeg 或摄像头管理后台确认 RTSP 地址能正常播放。地址、账号和网络都通了，再装 Clearcam，排查问题的成本会低很多。

如果正准备买摄像头，除了分辨率、夜视和本地 AI，RTSP 这类开放接口也要提前确认。它决定了以后能不能接 Frigate、Clearcam 这类自托管监控软件。

## 本地 AI 能做什么？

### 1. 目标检测与追踪

Clearcam 会对视频流做 AI 推理，识别画面中的目标，并持续跟踪它们的移动轨迹。

它和普通运动检测的区别很直接：运动检测只知道“画面动了”，树叶晃动、光线变化都可能触发；AI 检测会判断画面里出现的是人、车，还是其他目标，后续通知也能更有针对性。

![Clearcam 设置监控画面 AI 检测区域](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/71ddbb920e18b27653ad8780d5082a4b.jpg)

*在监控画面上直接框选检测区域，并设置检测阈值。*

检测区域可以手动划定。只关注门口、车道或院墙时，把无关区域排除掉，既能减少误报，也能降低推理压力。

![Clearcam 对监控画面中的目标进行 AI 检测和追踪](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/a4c84938722793cc89eba939464981d6.jpg)

*画面中的车辆会被识别、框选，并分配追踪 ID。*

### 2. 用图片搜索历史录像

这是 Clearcam 最实用的功能之一。

传统 NVR 按时间找录像，Clearcam 加入了相似图片搜索和上传图片搜索。手里有一张车辆截图，可以直接拿它去历史记录里找相似画面，不用再凭记忆拖时间轴。

![Clearcam 搜索历史监控录像和已检测目标](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/ca5fa10509d494b43d9cbf3e13bb34a7.jpg)

*检测事件会按目标截图归档，可以继续筛选和搜索。*

对于摄像头多、录像保存周期长的环境，这种检索方式比人工翻录像高效得多。

### 3. AI 通知摘要

Clearcam 已经接入基于 Qwen3 VL 的 AI Notification Summaries。除了提示“检测到人物”，它还能分析事件画面，生成一段更具体的情况描述。

![Clearcam 使用 AI 生成监控事件通知摘要](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/aaca249289834f9c47216fd732127819.jpg)

*通知里会同时给出事件类型和 AI 生成的画面摘要。*

这类功能比单纯的目标检测更吃算力。生成速度取决于 GPU、模型大小和运行设备，配置较低的机器更适合先关闭或减少摘要任务。

## 哪些功能在本地，哪些要走云？

Clearcam 的 NVR 和 AI 推理可以放在自己的设备上运行，但它并不是所有功能都完全离线。

| 功能 | 运行位置 |
| --- | --- |
| 接收 RTSP 视频流 | 本地 |
| AI 目标检测与追踪 | 本地 |
| 录像保存与回放 | 本地 |
| 远程查看实时画面 | Premium 云服务 |
| 远程查看事件录像 | Premium 云服务 |
| 官方移动端事件通知 | Premium 云服务 |

项目说明 Premium 数据使用端到端加密，但远程服务仍然有云端参与。

不想走官方通知链路，可以在设置里修改通知 URL，接 Home Assistant、Pushover、n8n 或其他自建服务。AI 检测继续在本地跑，通知这一层可以按自己的环境搭。

## 安装：Python 3.11、FFmpeg 和 tinygrad

Clearcam 目前以 Python 源码方式运行，不是下载一份 Docker Compose 就能启动的项目。

运行环境需要满足：

* Python 3.11 或更高版本；
* FFmpeg；
* 能安装 `requirements.txt` 中的依赖；
* 推理部分基于 tinygrad。

进入项目目录后，按官方 README 执行：

```
pip install -r requirements.txt
python3 clearcam.py
```

然后打开浏览器访问：

```
http://localhost:8080
```

如果 CPU 正在承担推理，而机器上有 AMD 或 NVIDIA 显卡，可以指定推理设备：

```
DEV=AMD python3 clearcam.py
DEV=NV python3 clearcam.py
```

还可以用 `BEAM=2` 提升推理性能，代价是首次运行需要等待编译：

```
BEAM=2 python3 clearcam.py
```

目前 Mac 和 Linux 的体验更顺。Windows 虽然也能运行，但官方 README 明确标注还需要处理 FFmpeg 兼容问题，不适合零基础直接上手。

Clearcam 没有把 Docker Compose 作为官方标准部署方式。习惯在 NAS、Proxmox 或 Ubuntu Server 上用 Docker 管服务的人，安装、升级和迁移都会多一些手工操作。

## Clearcam 和 Frigate 怎么选？

Frigate 是目前更成熟的开源 AI NVR，也是 Clearcam 最直接的对比对象。

| 对比项 | Clearcam | Frigate |
| --- | --- | --- |
| 部署方式 | 直接运行 Python 源码 | 以 Docker Compose 为主 |
| AI 检测 | 支持目标检测和追踪 | 支持，配置体系更完整 |
| 录像搜索 | 相似图片、上传图片搜索 | Semantic Search，支持文字或图片 |
| Home Assistant | 通过通知 URL 等方式接入 | 有正式集成 |
| 硬件加速 | 重点支持 AMD / NVIDIA | 支持 Intel、AMD、NVIDIA、Hailo、Rockchip 等 |
| 项目成熟度 | 更新快，生态仍在完善 | 文档、社区和部署方案更完整 |

Clearcam 的优势是路径短：现有 RTSP 摄像头接进来，在本机把 AI 检测跑起来，不需要先搭一整套 Docker 服务。

Frigate 的优势是配套全：多摄像头管理、硬件加速、Home Assistant 集成和社区文档都更成熟。

如果只是给现有监控补一层 AI，Clearcam 更直接。如果准备长期维护一套完整的家庭 AI NVR，尤其已经深度使用 Home Assistant，Frigate 更稳。

## 当前限制

1. **Windows 还有 FFmpeg 兼容问题。** Mac 和 Linux 部署更省事。
2. **没有官方 Docker Compose。** NAS、Proxmox 用户需要自己维护 Python 环境。
3. **远程能力依赖 Premium。** 远程实时画面、事件录像和官方移动端通知会使用 Clearcam 的服务器和云存储。
4. **生态还不如 Frigate。** Home Assistant 集成、硬件加速器和社区资料都相对有限。
5. **AI 摘要吃算力。** 低配设备跑检测可以，叠加 Qwen3 VL 摘要会更慢。

## 已有 NVR 要不要换？

不用换。

如果原来的摄像头或 NVR 已经在用，例如海康的 Hik-Connect，可以让原系统继续负责录像，同时让 Clearcam 读取同一路 RTSP 视频流，专门做 AI 检测、追踪和录像搜索。

这种用法对现有设备改动最小：原来的录像链路不动，Clearcam 只增加一层分析能力。等以后确实需要整套自托管监控，再评估是否迁移到 Frigate 或完整替换 NVR。

## 常见问题

### Clearcam 免费吗？

基础软件可以免费运行。官方移动端的远程查看、事件录像和通知属于 Premium 功能，会使用 Clearcam 的服务器和云存储。

### 哪些摄像头能接入？

关键是能提供 RTSP 视频流，并且 Clearcam 主机能访问。只支持厂商私有 App、没有开放 RTSP 的摄像头不能直接接入。

### 支持 Docker 吗？

目前主要以 Python 源码运行，没有官方 Docker Compose 标准部署方式。长期放在 NAS 或家庭服务器上，需要自己维护环境。

### 支持 Windows 吗？

可以运行，但目前还有 FFmpeg 兼容问题。Mac 和 Linux 更省事，Windows 需要自己处理环境依赖。

### 监控视频会上传云端吗？

本地 NVR 和 AI 推理可以在自己的设备上完成。使用官方 Premium 的远程查看、事件录像和移动通知时，才会经过 Clearcam 的云服务。

### Clearcam 和 Frigate 哪个好？

给现有 RTSP 摄像头快速增加 AI 检测、追踪和图片搜索，选 Clearcam。需要 Docker、Home Assistant 正式集成、更广的硬件加速和长期维护，选 Frigate。

## 最后

Clearcam 的价值不在于功能数量压过 Frigate，而在于把“旧摄像头 + 本地 AI”这条路缩短了。

只要摄像头支持 RTSP，有一台 Mac、Linux 主机或家庭服务器，就能在不拆原监控系统的前提下，加上人车检测、目标追踪、图片搜索和 AI 通知摘要。代价是 Python 环境要自己维护，Windows 支持还不完整，远程能力也依赖 Premium。

现有监控够用、只想补 AI 分析，Clearcam 值得部署。准备从零搭一套长期运行的家庭 NVR，Frigate 仍然是更稳的选择。

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[上一篇
币安：已补回90%被盗资产 计划周日恢复提现](https://blog.upx8.com/%E5%B8%81%E5%AE%89-%E5%B7%B2%E8%A1%A5%E5%9B%9E90-%E8%A2%AB%E7%9B%97%E8%B5%84%E4%BA%A7-%E8%AE%A1%E5%88%92%E5%91%A8%E6%97%A5%E6%81%A2%E5%A4%8D%E6%8F%90%E7%8E%B0)
[下一篇
免费版 WAF 规则不够用？Worker 自动拉黑扫描 IP 方案](https://blog.upx8.com/WAF-Worker-IP)

## 相关文档

* [给编码 Agent 装一张嘴：DSH 语音 AI 女友完整搭建教程
  11-02](https://blog.upx8.com/Agent-DSH-AI)
* [免费版 WAF 规则不够用？Worker 自动拉黑扫描 IP 方案
  11-01](https://blog.upx8.com/WAF-Worker-IP)
* [LocModel：越狱大模型、AI 绘图、视频生成和 Agent 都装进本地电脑
  10-31](https://blog.upx8.com/LocModel-AI-Agent)
* [RSSHub 公共实例整理与自建教程
  10-31](https://blog.upx8.com/RSSHub)

## 评论与补充0

有问题或想补充的，写在下面 · 选中正文文字再点「报告错误」会自动引用

还没有评论。有疑问、补充，或者发现错字，都可以写在下面。

回复
取消

请勿填写此栏

就事论事，别发广告 · 正常评论
发表评论

本文目录

* [先说结论：适合谁，不适合谁](#%E5%85%88%E8%AF%B4%E7%BB%93%E8%AE%BA%EF%BC%9A%E9%80%82%E5%90%88%E8%B0%81%EF%BC%8C%E4%B8%8D%E9%80%82%E5%90%88%E8%B0%81)
* [Clearcam 是什么？](#clearcam-%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F)
* [接入条件：RTSP 是硬门槛](#%E6%8E%A5%E5%85%A5%E6%9D%A1%E4%BB%B6%EF%BC%9Artsp-%E6%98%AF%E7%A1%AC%E9%97%A8%E6%A7%9B)
* [本地 AI 能做什么？](#%E6%9C%AC%E5%9C%B0-ai-%E8%83%BD%E5%81%9A%E4%BB%80%E4%B9%88%EF%BC%9F)
  + [1. 目标检测与追踪](#1.-%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E4%B8%8E%E8%BF%BD%E8%B8%AA)
  + [2. 用图片搜索历史录像](#2.-%E7%94%A8%E5%9B%BE%E7%89%8...