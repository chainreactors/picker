---
title: Sandboxie——轻量型沙箱隔离工具
url: https://mp.weixin.qq.com/s/HNl5oUKCVbiP6d2LpSNKuQ
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:25:07.718077
---

# Sandboxie——轻量型沙箱隔离工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AGUhPQZ04zx7RGQS4xf0ms95F2Qn9DFQZmEia0LS0bicMiaQibb4zJ6VicL9TKWTv0ZCZBFcDQrgHvyoYnCXXMk8iagQ/0?wx_fmt=jpeg)

# Sandboxie——轻量型沙箱隔离工具

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

项目地址

https://github.com/sandboxie-plus/Sandboxie

## 概述

Sandboxie 是一款基于沙箱技术的隔离软件，专为 Windows NT 架构操作系统设计。它创建一个安全的隔离运行环境，使应用程序可以在其中运行或安装，而不会永久修改本地磁盘、映射驱动器或 Windows 注册表。这种隔离的虚拟环境允许对不受信任的程序进行可控测试，以及安全地浏览网页。

**重要提示**：项目为社区分支（sandboxie-plus），在 Sophos 开源后继续发展，并非官方原开发的直接延续。

![](https://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zx7RGQS4xf0ms95F2Qn9DFQIwYZYFQqxXA1JicibKibA3bQTlib89kcuMRxjBLicj1kSJXibZNQH4r5RaKw/640?wx_fmt=png&from=appmsg)

## 系统要求

* **操作系统**：Windows 7 或更高版本（64 位）
* **架构**：x86\_64
* **权限**：安装需要管理员权限

## 版本体系

Sandboxie 提供两个版本，共享相同的核心组件，具有相同的安全性和兼容性级别，但用户界面和功能支持存在差异：

### Sandboxie Plus

* **UI 框架**：现代 Qt-based 界面
* **推荐指数**：⭐⭐⭐⭐⭐
* **目标用户**：需要最新安全特性和友好界面的用户

### Sandboxie Classic

* **UI 框架**：传统的 MFC-based 界面（已停止开发）
* **推荐指数**：⭐⭐⭐
* **目标用户**：习惯经典界面或有特定兼容性需求的老用户

---

## 核心功能详解

### 1. 快照管理器（Snapshot Manager）

* **功能**：创建沙箱的完整副本，可随时还原
* **应用场景**：软件安装前创建基线快照，测试后快速回滚
* **技术实现**：基于差分复制机制，仅存储变更内容

### 2. 隐私模式沙箱（Privacy Mode）

* **功能**：保护用户数据免受非法访问
* **技术特点**：严格限制沙箱内程序对真实用户目录的访问
* **配置路径**：Sandbox Options > Privacy

### 3. 安全增强沙箱（Security Enhanced）

* **功能**：限制系统调用和终端点的可用性
* **技术机制**：通过系统调用过滤和 API 拦截实现深度隔离
* **使用建议**：运行高风险软件时启用

### 4. 网络防火墙（Per-Sandbox Firewall）

* **功能**：为每个沙箱提供独立的网络访问控制
* **技术基础**：支持 Windows 过滤平台（WFP）
* **配置选项**：

+ 阻止/允许特定 IP/端口
+ 协议级过滤（TCP/UDP/ICMP）
+ 出站/入站规则分离

### 5. 资源限制系统

* **内存限制**：单进程内存上限、沙箱总内存上限
* **进程数量**：限制单沙箱内并发进程数
* **CPU 限制**：可配置 CPU 亲和性和时间片分配

### 6. 加密沙箱（Encrypted Sandbox）

* **加密算法**：AES-256
* **密钥管理**：基于用户会话的临时密钥
* **性能影响**：约 5-10% 的 I/O 性能损耗

### 7. 高级令牌机制

* **技术改进**：完全重构的令牌创建机制
* **安全优势**：沙箱进程使用独立 SID，与主机系统强隔离
* **兼容性**：更好的 UAC 和权限管理支持

### 8. 触发器系统（Trigger System）

* **支持事件**：初始化、启动、终止、文件恢复等
* **动作类型**：执行脚本、发送通知、自动清理
* **配置方式**：INI 文件或 UI 可视化配置

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

一个人挺好 wa

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

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