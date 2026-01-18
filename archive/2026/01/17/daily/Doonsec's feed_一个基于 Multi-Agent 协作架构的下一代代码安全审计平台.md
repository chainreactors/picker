---
title: 一个基于 Multi-Agent 协作架构的下一代代码安全审计平台
url: https://mp.weixin.qq.com/s/115p3oHVpUIJ0lULPvyUUA
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:36:29.220848
---

# 一个基于 Multi-Agent 协作架构的下一代代码安全审计平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2kgwVm5QUg92kU37TmEiaiautnDeeQGYFvApNibf3QS22ZMWuqdq7xlzyj1CB8bya779XZv92K54aN2g/0?wx_fmt=jpeg)

# 一个基于 Multi-Agent 协作架构的下一代代码安全审计平台

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

📌各位可以将公众号设为星标⭐

📌这样就不会错过每期的推荐内容啦~

📌这对我真的很重要！

![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")

📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。

📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。

📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。

**工具介绍**

**DeepAudit** 是一款基于 **Multi-Agent 协作架构** 的新一代代码安全审计平台。它不仅是一个静态扫描工具，更能模拟安全专家的思维方式，通过多个智能体（**Orchestrator**、**Recon**、**Analysis**、**Verification**）的自主协作，实现对代码的深度理解、漏洞挖掘以及 **自动化沙箱 PoC 验证**。

我们旨在解决传统 SAST 工具的三大核心问题：

* **误报率高** — 因缺乏语义理解而导致大量误报，耗费人力。
* **业务逻辑盲点** — 难以理解跨文件调用与复杂业务逻辑。
* **缺乏验证手段** — 无法确认漏洞是否真实可被利用。

用户只需导入项目，DeepAudit 即可全自动开始工作：识别技术栈 → 分析潜在风险 → 生成脚本 → 沙箱验证 → 生成报告，最终输出一份专业的审计报告。

> **核心理念**：让 AI 兼具黑客的攻击思维与专家的防御能力。

## 💡 为什么选择 DeepAudit？

| 😫 传统审计的痛点 | 💡 DeepAudit 解决方案 |
| --- | --- |
| **人工审计效率低** 赶不上 CI/CD 的代码迭代速度，拖慢发布流程。 | **🤖 Multi-Agent 自主审计** AI 自动编排审计策略，实现全天候自动化执行。 |
| **传统工具误报多** 因缺乏语义理解，每天需花费大量时间清洗噪音。 | **🧠 RAG 知识库增强** 结合代码语义与上下文信息，显著降低误报率。 |
| **数据隐私担忧** 担心核心源码泄露给云端 AI，无法满足合规要求。 | **🔒 支持 Ollama 本地部署** 数据可不出内网，支持 Llama3/DeepSeek 等本地模型。 |
| **无法确认真实性** 外包项目漏洞多，难以判断哪些漏洞真实可被利用。 | **💥 沙箱 PoC 验证** 自动生成并执行攻击脚本，确认漏洞的真实危害性。 |

![](https://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCBe6fXkHicUMLEYyaugwzObjAXUJBZiakUHCiaKHQiamo6SehVNwiacI8So4rmDQ6LEwsnbeDgRNZXBCzQ/640?wx_fmt=png&from=appmsg)

## Multi-Agent 智能审计

### 支持的漏洞类型

| 漏洞类型 | 描述 |
| --- | --- |
| `sql_injection` | SQL 注入 |
| `xss` | 跨站脚本攻击 |
| `command_injection` | 命令注入 |
| `path_traversal` | 路径遍历 |
| `ssrf` | 服务端请求伪造 |
| `xxe` | XML 外部实体注入 |
| `insecure_deserialization` | 不安全反序列化 |
| `hardcoded_secret` | 硬编码密钥 |
| `weak_crypto` | 弱加密算法 |
| `authentication_bypass` | 认证绕过 |
| `authorization_bypass` | 授权绕过 |
| `idor` | 不安全直接对象引用 |

> 📖 详细内容请查阅 **Agent 审计指南**

---

## 🔌 支持的 LLM 平台

### 🌍 国际平台

| OpenAI GPT-4o / GPT-4 Claude 3.5 Sonnet / Opus Google Gemini Pro DeepSeek V3 | ### 🇨🇳 国内平台 |
| --- | --- |
|  | 通义千问 Qwen 智谱 GLM-4 Moonshot Kimi 文心一言 · MiniMax · 豆包 |
|  |  |

💡 支持 API 中转站，以解决网络访问问题 | 详细配置 → LLM 平台支持

---

## 🎯 功能矩阵

| 功能 | 说明 | 模式 |
| --- | --- | --- |
| **🤖 Agent 深度审计** | Multi-Agent 协作，自主编排审计策略 | Agent |
| **🧠 RAG 知识增强** | 代码语义理解，集成 CWE/CVE 知识库检索 | Agent |
| **🔒 沙箱 PoC 验证** | 基于 Docker 隔离执行，验证漏洞有效性 | Agent |
| **🗂️ 项目管理** | 支持 GitHub/GitLab/Gitea 导入、ZIP 上传及 10+ 种编程语言 | 通用 |
| **⚡ 即时分析** | 对代码片段进行秒级分析，粘贴即用 | 通用 |
| **🔍 五维检测** | 涵盖缺陷、安全、性能、代码风格及可维护性 | 通用 |
| **💡 What-Why-How** | 提供精准定位、原因解释及修复建议 | 通用 |
| **📋 审计规则** | 内置 OWASP Top 10，支持自定义规则集 | 通用 |
| **📝 提示词模板** | 支持可视化管理及中英文双语 | 通用 |
| **📊 报告导出** | 支持一键导出为 PDF / Markdown / JSON 格式 | 通用 |
| **⚙️ 运行时配置** | 可在浏览器中配置 LLM，无需重启服务 | 通用 |

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**工具使用**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

---

**方式一：一行命令部署（推荐）** 使用预构建的 Docker 镜像，无需克隆代码，通过一行命令即可启动：

```
curl -fsSL https://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker-compose.prod.yml | docker compose -f - up -d
```

**🇨🇳 国内加速部署（作者亲测非常无敌之快）** 使用南京大学镜像站加速拉取 Docker 镜像（将 `ghcr.io` 替换为 `ghcr.nju.edu.cn`）：

```
# 国内加速版 - 使用南京大学 GHCR 镜像站
curl -fsSL https://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker-compose.prod.cn.yml | docker compose -f - up -d
```

**手动拉取镜像（如需单独拉取）**

点击展开

```
# 前端镜像
docker pull ghcr.nju.edu.cn/lintsinghua/deepaudit-frontend:latest

# 后端镜像
docker pull ghcr.nju.edu.cn/lintsinghua/deepaudit-backend:latest

# 沙箱镜像
docker pull ghcr.nju.edu.cn/lintsinghua/deepaudit-sandbox:latest
```

💡 镜像源由 **南京大学开源镜像站** 提供支持。

**💡 配置 Docker 镜像加速（可选，进一步提升拉取速度）**

点击展开

如果拉取镜像速度仍不理想，可以配置 Docker 镜像加速器。编辑 Docker 配置文件并添加以下镜像源：

* **Linux / macOS**：编辑 `/etc/docker/daemon.json`
* **Windows**：右键 Docker Desktop 图标 → Settings → Docker Engine

```
{
  "registry-mirrors": [
    "https://docker.1ms.run",
    "https://dockerproxy.com",
    "https://hub.rat.dev"
  ]
}
```

保存后重启 Docker 服务：

```
# Linux
sudo systemctl restart docker
# macOS / Windows
# 重启 Docker Desktop 应用
```

🎉 **启动成功！** 访问 `http://localhost:3000` 开始体验。

**方式二：克隆代码部署** 适合需要自定义配置或进行二次开发的用户：

```
# 1. 克隆项目
git clone https://github.com/lintsinghua/DeepAudit.git && cd DeepAudit

# 2. 配置环境变量
cp backend/env.example backend/.env
# 编辑 backend/.env 填入你的 LLM API Key

# 3. 一键启动
docker compose up -d
```

首次启动时会自动构建沙箱镜像，此过程可能需要几分钟。![](https://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCBe6fXkHicUMLEYyaugwzObjoYxjibkYxqeBZ1H5WoefuDibFB1ibptNGDiaQsbo7GD4PWJ3cCsNicicHxPw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCBe6fXkHicUMLEYyaugwzObjTW3x4ajW1PAQHFs1gMpJOXkCSZnFfEwSYTxaZ5ZOR89jFSpGoRTlOQ/640?wx_fmt=png&from=appmsg)

**下载地址**

关注微信公众号后台回复“**20260117**”，即可获取项目下载地址

关注微信公众号后台回复**入群** 即可加入星夜AI安全交流群

## 圈子介绍

现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。

已产出的安全工具及成果包括：

* 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护）
* 全自动信息收集平台（集成资产测绘、端口扫描、指纹识别及漏洞探针）
* 内网穿透套件（适配多层路由、隔离网络环境的隐蔽流量转发）
* 权限维持工具集（含注册表、系统服务、进程隐藏等多维持久化方案）
* 哥斯拉/冰蝎定制化马生成器（绕过主流终端防护与EDR动态检测）
* 日志清理工具（实现Windows/Linux系统关键日志无痕删除与篡改）
* 浏览器凭证窃取工具（支持Chrome/Edge/Firefox等主流浏览器数据提取）
* 企业VPN漏洞利用工具（适配多款商用VPN设备的漏洞探测与利用）
* 工控系统专用扫描器（针对SCADA、PLC等工控设备的安全检测与指纹识别）
* 邮件钓鱼平台（集成模板生成、钓鱼追踪、数据统计全流程功能）
* 社工信息聚合工具（整合多平台公开信息检索与关联分析能力）
* 二开fscan内网扫描工具（增强指纹精度、弱口令爆破与结果标准化输出）
* 多款免杀Webshell集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护）
* 免杀360专属加载器（支持Shellcode内存执行，绕过360全系防护检测）

后续将不断更新到内部圈子中 欢迎加入圈子

![](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2kgwVm5QUg92kU37TmEiaiautYwGOx5eric5qEh992z2HcDTYeiaso87draTq0woKu4eSm2sQQibUNj8iaw/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

星夜AI安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

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