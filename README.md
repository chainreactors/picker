origin fork from https://github.com/VulnTotal-Team/yarb

重构后脱离了github的fork, 原始仓库地址 https://github.com/chainreactors/picker , 需要后续更新请从该仓库获取

# picker

抓取、推送、讨论、交流、互动为一体，将 GitHub 仓库变为私人的讨论社区。

**新特性 v3.0**:
- 🤖 **AI 智能摘要**: 自动为精选文章生成结构化摘要
- 📝 **Markdown 归档**: 自动保存文章为 Markdown 格式
- 🗂️ **层次化存储**: 新的 `archive/{year}/{month}/{day}/` 目录结构
- 🔄 **自动化工作流**: Issue 创建时自动生成摘要并推送到 Bot

支持导入 OPML 文件，也可以订阅其他任何 RSS 源。

## 使用

基于 GitHub Actions 实现的自动化推送系统

### 推送类型

- **每日信息流**: 每天 09:55 推送昨日新增文章列表
- **每日精选**: 每天 13:55 推送昨日精选汇总
- **精选推送**: 创建 Issue 时自动生成 AI 摘要并推送到 Bot
- **评论推送**: 精选文章的评论自动推送到 Bot

### AI 智能摘要（新功能）

当创建精选 Issue 时，系统会自动：
1. 抓取文章内容并转换为 Markdown
2. 调用 AI 生成结构化摘要（包含主题、关键点、应用场景、局限性、评价）
3. AI 自动生成文章分类（Red Team、Web Security、AI Security 等）
4. **自动添加对应的 GitHub Label**（如 `ai-security`、`red-team` 等）
5. 提取文章中的所有链接，生成参考链接列表
6. 更新 Issue 内容
7. 推送到 Bot 通知群
8. 保存到 `archive/{year}/{month}/{day}/summary/`（包含 YAML frontmatter metadata）

**使用方式**：
```bash
# 方式一：通过 GitHub CLI 创建 Issue（推荐）
gh issue create --title "文章标题" --body "https://example.com/article" --label "pick"

# 方式二：在每日信息流 Issue 中点击 "Convert to issue"

# 方式三：手动创建 Issue，body 填写文章 URL
```

**手动生成摘要**：
```bash
# 为指定 Issue 生成 AI 摘要
python3 picker.py --summarize-issue <issue_number>

# 批量获取文章 Markdown（不生成摘要）
python3 picker.py --fetch-articles 2025-10-01
```

### 信息流

每日会在 issue 中生成昨日信息流

![img.png](img/信息流.png)

### 精选

如果认为某篇文章质量较好, 值得其他人阅读可以点击 convert to issue 自动添加到精选文章列表.

![img.png](img/精选.png)

如果需要多人合作, 普通的 read 权限并没有 convert to issue 的功能, 需要 triage 权限

![img.png](img/权限.png)

或手动 new issue, 也会自动添加到 issue 中

![img.png](img/手动添加.png)

每天下午 13:30, 会将昨日的精选汇总进行一次推送.

### 标签

每日信息流会自动添加标签 daily, 每日精选会自动添加标签 dailypick. 精选文章会添加标签 pick.

一些文章的细分领域可以通过手动添加不同的标签进行管理.

![img.png](img/标签.png)

已经给主要用户都添加了写权限, 可以自行创建标签.

### 评论

对精选文章的评论将会自动推送到钉钉群

### 订阅源

推荐订阅源：

- [CustomRSS](rss/CustomRSS.opml)

其他订阅源：

- [CyberSecurityRSS](https://github.com/zer0yu/CyberSecurityRSS)
- [Chinese-Security-RSS](https://github.com/zhengjim/Chinese-Security-RSS)
- [awesome-security-feed](https://github.com/mrtouch93/awesome-security-feed)
- [SecurityRSS](https://github.com/Han0nly/SecurityRSS)
- [安全技术公众号](https://github.com/ttttmr/wechat2rss)
- [SecWiki 安全聚合](https://www.sec-wiki.com/opml/index)
- [Hacking8 安全信息流](https://i.hacking8.com/)

非安全订阅源：

- [中文独立博客列表](https://github.com/timqian/chinese-independent-blogs)

**添加自定义订阅源**

1. 在 `config.json` 中添加本地或远程仓库：

```yaml
rss:
  CustomRSS:
    enabled: true
    filename: CustomRSS.opml
  CyberSecurityRSS:
    enabled: true
    url: >-
      https://raw.githubusercontent.com/zer0yu/CyberSecurityRSS/master/CyberSecurityRSS.opml
    filename: CyberSecurityRSS.opml
  CyberSecurityRSS-tiny:
    enabled: false
    url: "https://raw.githubusercontent.com/zer0yu/CyberSecurityRSS/master/tiny.opml"
    filename: CyberSecurityRSS-tiny.opml
  Chinese-Security-RSS:
    enabled: true
    url: >-
      https://raw.githubusercontent.com/zhengjim/Chinese-Security-RSS/master/Chinese-Security-RSS.opml
    filename: Chinese-Security-RSS.opml
  awesome-security-feed:
    enabled: true
    url: >-
      https://raw.githubusercontent.com/mrtouch93/awesome-security-feed/main/security_feeds.opml
    filename: awesome-security-feed.opml
  SecurityRSS:
    enabled: true
    url: "https://github.com/Han0nly/SecurityRSS/blob/master/SecureRss.opml"
    filename: SecureRss.opml
  wechatRSS:
    enabled: true
    url: "https://wechat2rss.xlab.app/opml/sec.opml"
    filename: wechatRSS.opml
  chinese-independent-blogs:
    enabled: false
    url: >-
      https://raw.githubusercontent.com/timqian/chinese-independent-blogs/master/feed.opml
    filename: chinese-independent-blogs.opml
```

2.

自定义 rss 源位于`rss/CustomRSS.opml`中, 需要添加请提交 pr, 次日自动加入到推送列表

非 rss 源可以使用 rsshub 转发

## 部署

推荐使用 github action 部署

### github 部署

step1: fork 仓库

因为 fork 可能自动关闭 issue, 并且导致 issue 指向原仓库, 所以建议脱离 fork 关系. 操作比较简单, clone 本仓库, 然后创建一个空项目, 将该仓库 push 即可.

step2: 初始化标签

**使用以下命令自动创建所有必需的标签**：

```bash
python3 picker.py --init
```

这会创建以下标签：
- 基础标签: `pick`, `daily`, `dailypick`（需手动创建）
- 分类标签: `red-team`, `blue-team`, `web-security`, `binary-security`, `mobile-security`, `cloud-security`, `ai-security`, `vulnerability`, `reverse-engineering`, `code-audit`, `security-tools`, `security-research`, `others`

step3: 创建 github token

在 secret 中配置`MY_GITHUB_TOKEN`, 点击这里[生成](https://github.com/settings/tokens/new), 只需要给 repo 权限即可.

step4: 配置 Bot 机器人

支持多种推送平台（飞书、钉钉、企业微信、QQ、Telegram、邮件）

**必需配置**（GitHub Secrets）：
- `MY_GITHUB_TOKEN` - GitHub Personal Access Token（repo 权限）
- `OPENAI_API_KEY` - OpenAI 兼容 API Key（用于 AI 摘要，可选）

**Bot 配置**（至少配置一个）：
- 飞书: `FEISHU_KEY`, `PICKER_FEISHU_KEY`
- 钉钉: `DINGTALK_KEY`, `DINGTALK_SECRET`, `PICKER_DINGTALK_KEY`, `PICKER_DINGTALK_SECRET`
- 企业微信: `WECOM_KEY`
- QQ: `QQ_KEY`
- Telegram: `TELEGRAM_KEY`
- 邮件: `MAIL_KEY`, `MAIL_RECEIVER`

可以配置两个不同的机器人（`*_KEY` 用于每日推送，`PICKER_*_KEY` 用于精选推送），也可以只配置一个。

**AI 配置**（可选）：

在 `config.yml` 中启用 AI 功能：
```yaml
ai:
  enabled: true              # 启用 AI
  mode: pick                 # 模式: daily/pick
  api_key: sk-xxx           # API Key（或通过环境变量 OPENAI_API_KEY）
  api_base: https://api.moonshot.cn/v1  # API 地址（支持 OpenAI 兼容）
  model: kimi-k2-0905-preview           # 模型名称
  max_tokens: 2000
  temperature: 0.7
```

其他推送渠道可参考 `bot.py` 自行添加。

### 本地搭建

需要在本地安装 github-cli ,并登录. 不推荐使用, 仅在调试模式下测试用.

```sh
$ git clone https://github.com/chainreactors/picker
$ cd picker && ./install.sh
```

编辑配置文件 `config.json`，启用所需的订阅源和机器人（key 也可以通过环境变量传入），最好启用代理。

```bash
# 基本命令
./picker.py                           # 抓取 RSS
./picker.py --update-pick             # 更新精选汇总
./picker.py --test                    # 测试 bot
./picker.py --check                   # 检查所有 bot

# Issue 相关
./picker.py --push-issue <number>     # 推送 Issue 到 bot
./picker.py --push-comment <number>   # 推送评论到 bot
./picker.py --init                     # 初始化分类标签
./picker.py --summarize-issue <number> # 生成 AI 摘要
./picker.py --fetch-articles <date>   # 批量获取文章 Markdown
```

## 目录结构

```
archive/{year}/{month}/{day}/
├── daily.json               # 当日所有文章数据
├── daily.md                 # 每日资讯汇总
├── pick.md                  # 精选汇总
├── daily/                   # 当日所有文章的 Markdown
│   └── {source}_{title}.md
├── summary/                 # 当日 AI 摘要（含 metadata 和参考链接）
│   └── {source}_{title}_summary.md
└── pick/                    # 当日精选文章的 Markdown
    └── {source}_{title}.md
```

**Summary 文件格式**：
```markdown
---
title: 文章标题
url: https://example.com/article
source: 来源名称
date: 2025-10-02
fetch_date: 2025-10-02T12:00:00
category: AI Security
---

# 文章标题 - 摘要

1. 文章主题
...

2. 关键点
...

## 参考链接

1. https://example.com/link1
2. https://example.com/link2
```

## 文档

- [WORKFLOW.md](WORKFLOW.md) - 完整工作流程说明
- [GITHUB_ACTIONS_SUMMARY.md](GITHUB_ACTIONS_SUMMARY.md) - GitHub Actions 详细文档
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - 项目结构说明
- [CHANGELOG.md](CHANGELOG.md) - 版本变更日志

## 版本

当前版本: **v3.0.0** (2025-10-02)

主要特性:
- ✅ AI 摘要自动集成
- ✅ 模块化代码重构
- ✅ 层次化目录结构
- ✅ MarkItDown 集成
- ✅ 批量文章获取
```
