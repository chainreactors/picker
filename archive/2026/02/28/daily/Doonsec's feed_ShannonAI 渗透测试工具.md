---
title: ShannonAI 渗透测试工具
url: https://mp.weixin.qq.com/s/0RpdydNSjjk0qQvDzlXNkQ
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:25:34.832707
---

# ShannonAI 渗透测试工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ft77EUEUqoug9BahSbMnnHD2eDtzHdG1NfXVPI5o3gxOW1fiapibmGtCx5CjY2BsZzuSSU7ZOn1POqqZiaG4VdjTY6deeFzjQdEcvRxaHkJYxY/0?wx_fmt=jpeg)

# ShannonAI 渗透测试工具

云梦DC
云梦DC

云梦安全

![]()

在小说阅读器中沉浸阅读

## 项目概述

![](https://mmbiz.qpic.cn/mmbiz_png/Ft77EUEUqotPRtAZuAnHCicS7h6yleQPc2QwDPoictHvPibNbhs83mbicJ5FlicfKXyGbUK0dqiay8cCUyfoiatXic9WIutc2RJswI7Ujobeyy11Mn4/640?wx_fmt=png&from=appmsg)

##

**Shannon** 是由 *KeygraphHQ* 开发的一款 **完全自主的 AI 渗透测试（Pentesting）工具**，旨在自动发现并验证 Web 应用中的真实安全漏洞。它不是普通的静态扫描器，而是：

* **自动化模拟人类渗透测试流程**
* **执行真实 exploit（利用）证明漏洞可被攻击者利用**
* **生成可复现的漏洞证明（PoC）报告**
* 面向白盒测试（需要源码访问）

成功率在多个基准测试（如 **XBOW benchmark**）上达到 **96.15%**，在漏洞发现与验证方面表现优异。

---

## 🔑 核心特点

✨ **全自动化渗透测试**
AI 自动执行包括识别、分析、利用和报告的全流程。

📊 **含真实 exploit 验证**
它不仅报告潜在漏洞，还尝试真实攻击并产生可复现的 PoC。

🧠 **白盒分析 + 动态攻击**
结合源码分析和自动化浏览器攻击（如 Playwright / Selenium），支持复杂认证绕过、注入、XSS 等。

📂 **生成专业报告**
输出包括 Markdown/JSON 等格式的结构化报告，适用于安全分析与修复指导。

⚙️ **集成常见安全工具**
可调用 Nmap、Subfinder、WhatWeb、Schemathesis 等进行侦察与分析。

⚠️ **开源许可**
“Shannon Lite” 版本采用 **AGPL-3.0 许可证**，适合内部渗透测试和研究使用。

---

## 🚀 快速开始（典型流程）

### 1️⃣ 环境准备

你至少需要：

* Docker（主要部署方式）
* 源码拷贝（白盒测试）
* API 权限凭证：

+ **Anthropic API Key** 或
+ **Claude Code OAuth Token**

并设置较大的输出 token 限制，例如：

```
exportCLAUDE_CODE_MAX_OUTPUT_TOKENS=64000
```

或 Docker 中相应环境变量。

---

### 2️⃣ 克隆仓库

```
git clone https://github.com/KeygraphHQ/shannon.git
cd shannon
```

---

### 3️⃣ 构建与运行

```
docker build -t shannon:latest .
```

然后启动测试：

```
docker run --rm-it \
--network host \
--cap-add=NET_RAW \
--cap-add=NET_ADMIN \
-eANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
-eCLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 \
-v"$(pwd)/repos:/app/repos" \
-v"$(pwd)/configs:/app/configs" \
    shannon:latest \
"https://your-app-url.com/" \
"/app/repos/your-app" \
--config /app/configs/example-config.yaml
```

这里：

* 第一参数是目标 Web 应用 URL
* 第二是源码路径，用作白盒分析
* `--config` 可指定自定义 YAML 配置

---

## 📈 典型用途

✅ 持续集成自动化安全测试
✅ 交付前发现和复现漏洞
✅ Web 应用安全保障（OWASP 核心漏洞）
✅ 安全审计与渗透测试工作流程自动化

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ndxZsFvkmpznJ7eICiaSkulHmla8V8RPVeTQ5z2uI5iaV9FniaMzXYbodGk9qNSBY6ccvbiaW5XxvKJNp7zLicxwSEQ/0?wx_fmt=png)

云梦安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ndxZsFvkmpznJ7eICiaSkulHmla8V8RPVeTQ5z2uI5iaV9FniaMzXYbodGk9qNSBY6ccvbiaW5XxvKJNp7zLicxwSEQ/0?wx_fmt=png)

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