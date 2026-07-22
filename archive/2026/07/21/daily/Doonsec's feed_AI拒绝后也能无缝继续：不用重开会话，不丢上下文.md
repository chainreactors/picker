---
title: AI拒绝后也能无缝继续：不用重开会话，不丢上下文
url: https://mp.weixin.qq.com/s/AmlzwoiFRaM7_-m2g-r1FA
source: Doonsec's feed
date: 2026-07-21
fetch_date: 2026-07-22T05:02:06.358498
---

# AI拒绝后也能无缝继续：不用重开会话，不丢上下文

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2BCHXx7iavkQicYNyDVr9gY0iatG1XFEHPiaQDP39FLXfb8glOhb8cuIjnwiabe0JL09WprJzcgWfxqAUVGeIUTg78VmILzFXFoxtBCuSm5bKGsg/0?wx_fmt=jpeg)

# AI拒绝后也能无缝继续：不用重开会话，不丢上下文

ryfineZ
ryfineZ

山河学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责声明**

本公众号山河学安全旨在分享网络安全领域的相关知识和工具，仅限于学习和研究之用。由于传播、利用本公众号山河学安全所提供的信息而造成的任何直接或者间接的后果及损失，由使用者承担全部法律及连带责任，公众号山河学安全及作者不为此承担任何责任。如有侵权烦请告知，我们会立即删除并致歉，谢谢。**工具安全性自测！**

![引导关注](https://mmbiz.qpic.cn/sz_mmbiz_png/2BCHXx7iavkT4t8sagLiayh9CmhyQ8n3iczuz5z47P3FiboIGP8bSiahKJ6HznXGzBZ17wOGSQl8DV5gpoSkZ1TEshic4yu4iaLFaYEiaRoEMj6xFpU/640?from=appmsg)

**PART**

**01**

**工具概述**

## 是什么

在安全测试、CTF 比赛、渗透测试等场景下，AI 编码工具（Codex、Claude Code、OpenCode）会频繁拒绝涉及安全操作的请求，导致会话中断。

**Codex Session Patcher** 提供两类解决方案：

**1. 会话清理** — 扫描已产生的拒绝回复，替换为配合性内容，让会话可以 resume 继续

**2. CTF 提示词注入** — 在配置层面注入安全测试上下文，从源头降低被拒绝的概率

---

### 会话清理

• **智能检测** — 两级拒绝检测策略（强短语全文匹配 + 弱关键词开头匹配），低误报率

• **AI 智能改写** — 调用 LLM 根据对话上下文生成符合语境的替换回复（支持 OpenAI / Ollama / OpenRouter 等兼容接口）

• **安全兜底** — 可清理只有 `event_msg` 的历史 Codex 拒绝记录；AI 返回问号乱码时自动回退到安全默认文本

• **批量清理** — 处理会话中所有拒绝回复，而非仅最后一条

• **推理内容擦除** — 删除 Reasoning / Thinking block 加密推理内容

• **备份还原** — 清理前自动备份，支持一键还原到任意历史版本

• **Diff 对比** — 清理前后 Side-by-side 对比视图

### 平台支持

| 平台 | 会话清理 | CTF 注入 | 会话格式 |
| --- | --- | --- | --- |
| **Codex CLI** | ✅ | ✅ Profile + 全局 | JSONL |
| **Claude Code** | ✅ | ✅ 专用工作空间 | JSONL |
| **OpenCode** | ✅ | ✅ 专用工作空间 | SQLite |

### Web UI

• **会话列表** — 多平台统一管理，按日期分组，支持按格式/拒绝状态/备份状态过滤

• **可视化清理** — 预览面板 + Diff 对比 + 一键执行

• **多语言** — 支持中文 / English 界面切换

• **实时日志** — WebSocket 推送，操作日志实时显示

---

### Web UI（推荐）

# 生产模式
./scripts/start-web.sh

访问 `http://localhost:8080`

**开发模式（前后端热更新）：**

./scripts/dev-web.sh

说明：
 - 生产脚本只会在 Python Web 依赖缺失、前端依赖缺失/过期、或前端构建产物过期时才执行对应步骤。
 - 如果前端构建产物已经可直接提供服务，生产脚本不会为了启动而额外要求 `node` / `npm` 或补装前端依赖。
 - 开发脚本同样会跳过重复安装；如果 `3000` 端口已占用，会自动选择下一个可用端口启动前端。

## 局限性说明

• **无法突破平台最高安全策略** — 对于明确违规的请求仍可能被拒绝

• **效果因版本而异** — 模型版本更新可能影响效果

• **OpenCode 需从工作空间目录启动** — OpenCode 无 profile 机制，CTF 注入依赖工作空间

• **清理后需 resume** — 会话清理后需手动 resume 继续上下文

---

**PART**

**02**

**使用方法**

### CTF/渗透测试提示词注入

• **Codex Profile 模式** — 创建新版 `ctf.config.toml` profile，仅 `codex -p ctf` 启动时生效，不影响正常会话

• **Codex 全局模式** — 注入到全局配置，所有新会话自动生效

• **Claude Code 工作空间** — 创建专用 CTF 工作空间 `~/.claude-ctf-workspace`，通过项目级 CLAUDE.md 注入

• **OpenCode 工作空间** — 创建专用 CTF 工作空间 `~/.opencode-ctf-workspace`，通过 AGENTS.md 注入

• **提示词自定义** — Web UI 内直接编辑注入提示词，支持模板保存与切换

• **AI 提示词改写** — 结合已注入的 CTF 系统提示词，AI 改写你的请求使其更易被接受

## 安装

git clone https://github.com/ryfineZ/codex-session-patcher.git
cd codex-session-patcher

# CLI 版本（自动探测 Python 3.8+）
./scripts/install.sh

Web UI 的 `./scripts/start-web.sh` 和 `./scripts/dev-web.sh` 也会自动探测可用的 Python 3.8+ 解释器，优先尝试当前环境里的通用启动命令（如 `python3` / `python`），再回退到版本化命令或 `py -3`，并且只在依赖缺失或源码变更时才执行安装 / 构建。
 如果你确实需要手动安装 editable 包，再使用你机器上已有的 Python 3.8+ 启动命令执行 `-m pip install -e ...`；Windows 常见的是 `py -3`，其他环境可能是 `python3.12`、`python3` 或 `python`。
 在 Windows 的 Git Bash / MSYS / MINGW / Cygwin 环境中，项目启动脚本会自动为 Python 子进程设置 `PYTHONIOENCODING=utf-8`，减少本地 AI 代理或 Web 后端因 GBK 控制台导致中文变成问号串的概率。

Web UI 合作页里的合作意向表单会提交到作者部署的 Muggle Leads 线上服务（`https://leads.3jiezhiwai.com`），普通用户本地运行时不需要部署 Cloudflare，也不需要配置提交地址。

如果你 fork 了项目并希望表单提交到自己的服务，可以在启动 Web 服务前覆盖远程提交地址：

export MUGGLE\_LEADS\_ENDPOINT="https://你的 Worker 域名/api/sources/codex-session-patcher/intents"

Telegram Bot token 和后台管理密钥只配置在作者部署的 Cloudflare Worker 里，不能放在本地工具或前端代码中。

---

### CLI

#### CLI 参数说明

| 参数 | 说明 |
| --- | --- |
| `--session-dir` | 指定会话目录（默认自动选择） |
| `--format` | 会话格式：`codex` / `claude-code` / `opencode` / `auto` |
| `--dry-run` | 预览模式，不修改文件 |
| `--no-backup` | 不创建备份文件 |
| `--show-content` | 显示修改的详细内容 |
| `--latest` | 只处理最新会话 |
| `--all` | 处理所有会话 |
| `--keep-reasoning` | 保留推理内容（thinking/reasoning blocks），仅替换拒绝回复 |
| `--web` | 启动 Web UI |
| `--host` | Web UI 监听地址（默认 127.0.0.1） |
| `--port` | Web UI 端口（默认 8080） |
| `--install-ctf-config` | 安装 Codex CTF 配置 |
| `--ctf-injection-mode append\|replace` | 选择 Codex 注入方式，默认追加规则 |
| `--uninstall-ctf-config` | 卸载 Codex CTF 配置 |
| `--install-claude-ctf` | 安装 Claude Code CTF 配置 |
| `--uninstall-claude-ctf` | 卸载 Claude Code CTF 配置 |
| `--install-opencode-ctf` | 安装 OpenCode CTF 配置 |
| `--uninstall-opencode-ctf` | 卸载 OpenCode CTF 配置 |
| `--ctf-status` | 查看三平台 CTF 配置状态 |
| `--rewrite` | 改写提示词使其更易被接受 |

---

### Codex

1. 安装 CTF Profile
 codex-patcher --install-ctf-config
 # 强 CTF 场景可选择替换 Codex 内置提示词
 codex-patcher --install-ctf-config --ctf-injection-mode replace
 2. 使用 CTF Profile 启动（不影响普通会话）
 codex -p ctf
 3. 发送请求，若遇到拒绝 → 打开 Web UI 清理会话
 4. resume 继续
 codex resume

安装器会写入新版 Codex profile 文件：

• macOS/Linux: `~/.codex/ctf.config.toml`

• Windows: `%USERPROFILE%\.codex\ctf.config.toml`

为兼容 Codex CLI 0.134.0 及以后版本，安装时会从 `config.toml` 清理旧格式 `profile = "ctf"`、`[profiles.ctf]` 和 `[profiles.ctf.*]`，避免 `codex -p ctf` 启动时报 legacy profile 错误。Profile 模式和全局模式都支持追加规则或替换内置提示词；禁用全局模式会移除本工具写入的标记和配置。

Codex 提供两种注入方式：

• 默认追加规则：写入 `developer_instructions`，保留 Codex 内置提示词，适合日常安全测试。

• 替换内置提示词：写入 `model_instructions_file` 指向提示词文件，适合强 CTF 场景，但会接管 Codex 原本的内置提示词。

两种方式互斥。通过 Web UI 启用 Profile 或全局模式时可选择注入方式；CLI 可用 `--ctf-injection-mode append|replace`。

全局模式只管理带有 `# __csp_ctf_global__` 标记的配置块。如果 `config.toml` 顶层已经存在用户自己写的 `developer_instructions` 或 `model_instructions_file`，安装器会拒绝启用全局模式，避免覆盖用户配置或生成重复 key；请先手动迁移或删除原有顶层提示词配置。

### Claude Code

1. Web UI → 提示词增强 → Claude Code → 启用
 （创建 ~/.claude-ctf-workspace）
 2. 从专用工作空间启动
 cd ~/.claude-ctf-workspace && claude
 3. 遇到拒绝 → Web UI 清理 → 继续对话

### OpenCode

1. Web UI → 提示词增强 → OpenCode → 启用
 （创建 ~/.opencode-ctf-workspace）
 2. 从专用工作空间启动
 cd ~/.opencode-ctf-workspace && opencode
 3. 遇到拒绝 → Web UI 清理 → 继续对话

---

**PART**

**03**

**工具下载**

**关注名片进入公众号**

**回复关键字【260721】获取下载链接**

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0sjvG0TycCrkwqc9NOyXnxJdd3Sx952ibuNc9JbaRIwgribBX5MRFHecGVwgntRMicphmT55OA24qTJdzwXhegujQ/0?wx_fmt=png)

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