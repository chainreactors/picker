---
title: CAPEv2自动化分析沙箱安装指南
url: https://mp.weixin.qq.com/s/tVLDSVXAI1C_mLrKv4bcMQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:08:01.295072
---

# CAPEv2自动化分析沙箱安装指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/M5H82XuSHY7kIdZZTcx7zl7HK1B4BgtaE6EFEiceYTlVzTRRrib0O0gCf35usgl9ovft1mCgf6bn7zDRtX8n7qngPd28MUPaUib30lCBiadbIlc/0?wx_fmt=jpeg)

# CAPEv2自动化分析沙箱安装指南

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> CAPEv2 是 Cuckoo Sandbox 的活跃 fork，是目前最主流的开源恶意软件动态分析沙箱。

---

## 架构概览

CAPE 核心服务通过 KVM/QEMU 驱动 Windows Guest VM 执行样本，agent 监听指令回传行为数据，PostgreSQL 存储任务元数据，MongoDB 存储分析报告：

![](https://mmbiz.qpic.cn/mmbiz_png/M5H82XuSHY4kHK7suXjyc9G4a4mSHpHBX8v34WCRpDT8sbHia4sS5kzPBcicv8SJaXfc4IE5oLKicQpJh57BoLQoNYvXArzHicBCq6o5EicvibfLA/640?wx_fmt=png&from=appmsg)

**核心服务说明：**

| 服务 | 作用 |
| --- | --- |
| `cape.service` | 主调度服务，管理分析任务和 VM 通信 |
| `cape-processor.service` | 处理分析结果，提取行为数据 |
| `cape-web.service` | Web 界面，端口 8000 |
| `cape-rooter.service` | 网络路由与隔离管理 |

---

## 前置要求

### 硬件要求

| 组件 | 最低配置 | 推荐配置 |
| --- | --- | --- |
| CPU | 4核，支持 VT-x/AMD-V | 8核以上 |
| 内存 | 8 GB | 16 GB 以上 |
| 存储 | 100 GB SSD | 500 GB SSD |
| 网络 | 普通网卡 | 双网卡（分析网络隔离） |

> ⚠️ **重要提示：**
>
> * CPU 虚拟化支持必须在 BIOS 中开启（Intel VT-x 或 AMD-V）
> * 不要用 `cape` 作为当前登录用户名，安装脚本会创建系统级 `cape` 用户
> * 生产环境建议安装在物理机上，而非虚拟机中（嵌套虚拟化性能差）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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