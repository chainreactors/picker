---
title: DeepAudit工具使用指南
url: https://mp.weixin.qq.com/s/JQ42cuBKvQoosDxNxxt-1A
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:25:32.172323
---

# DeepAudit工具使用指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ft77EUEUqosD65bXUEjXEHRlUbibaaeYJ4Qyo7AMibQurDnxsOIQrLgXL3l98jlxFEUm4JTvib1O8qH6DS9mJiaJAusxaG0sLHI3QbrlGw5FoVM/0?wx_fmt=jpeg)

# DeepAudit工具使用指南

云梦DC
云梦DC

云梦安全

![]()

在小说阅读器中沉浸阅读

## 项目简介

DeepAudit 是一个 **基于多智能体（Multi-Agent）AI 的自动化代码安全审计平台**，旨在通过模拟专家思维流程，自动发现并验证代码中的安全漏洞，降低误报、覆盖业务逻辑盲点，并附带 PoC（漏洞可利用性验证）能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ft77EUEUqotNicAn6DCcRrzZGQOM8ibmoIicdBb99UNwMibsMd9ZIgkiaqbLZeu2v5wBs5UPJAGT7cOicagNibFJ45SIhUKrYLwFrI5v4gVdD4zGHQ/640?wx_fmt=png&from=appmsg)

主要特色：

* 使用智能体协作（Orchestrator、Recon、Analysis、Verification）进行安全分析。
* 支持本地或私有部署（本地 LLM/Ollama）。
* 可以导出审计结果为多种格式（如 PDF/JSON/Markdown）。
* 自动化沙箱环境验证 PoC，减少误报。
* 已在多个开源项目中发现真实 CVE 漏洞。

项目使用 **AGPL-3.0 开源协议**。

---

## 🚀 快速上手安装与启动

DeepAudit 支持 **Docker 方式部署** 和 **本地开发模式**。

### ✅ 1. 准备环境

你需要：

* Docker & Docker Compose
* Git（用于克隆仓库）
* 可选：Ollama 或其他 LLM（用于本地推理）

---

### ✅ 2. 克隆项目

在终端中运行：

```
git clone https://github.com/lintsinghua/DeepAudit.git
cd DeepAudit
```

---

### ✅ 3. 使用 Docker 部署

这是最简单的启用方式：

```
# 赋予脚本权限
cd docker/sandbox
chmod+x build.sh
./build.sh

# 回到项目根目录
cd ../..

# 启动容器
docker compose up -d
```

完成后在浏览器中访问：

```
http://localhost:3000
```

你就能看到 DeepAudit 的 Web 控制台。

---

## 🧠 功能 & 核心流程

### 🛠️ 审计流程（示例）

1. **导入项目**
   可以直接从 GitHub/GitLab/Gitea 仓库导入目标代码。
2. **智能体协作执行审计**
   多 Agent 协同理解代码上下文、业务流程、调用关系，生成漏洞线索并尝试自动化验证。
3. **生成报告**
   包括审计结果、漏洞详情、PoC 示例、修复建议等，可导出为 Markdown/PDF/JSON 形式。
4. **反馈与迭代**
   用户可调整规则、模型和策略持续优化检测结果。

---

## 📌 注意事项

🔒 **用途限制**
只应用于你 *有明确授权* 的代码审计场景，不要对未授权目标执行安全扫描。

⚠️ **安全漏洞修补**
DeepAudit 本身历史中存在中等安全漏洞（例如 CVE-2026-2532），建议使用最新版本并关注官方安全更新。

📦 **依赖与资源**
如果你选择本地模型运行，需事先部署可用的 LLM（例如兼容 Ollama 的模型等）。

---

## 🏁 总结

DeepAudit 是一款面向代码审计的 **自动化、智能化、安全分析平台**，适合：

📌 安全团队做源码审计
📌 CI/CD 集成自动安全检查
📌 学习 AI 驱动安全分析框架
📌 生成可验证审计报告

它结合了多 Agent 协作与自动化验证，是传统静态 SAST 工具的升级方向。

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