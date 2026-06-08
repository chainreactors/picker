origin fork from https://github.com/VulnTotal-Team/yarb

重构后脱离了github的fork, 原始仓库地址 https://github.com/chainreactors/picker , 需要后续更新请从该仓库获取

# picker

抓取、推送、讨论、交流、互动为一体，将 GitHub 仓库变为私人的讨论社区。

**新特性 v3.0**:
- **AI 智能摘要**: 自动为精选文章生成结构化摘要
- **Markdown 归档**: 自动保存文章为 Markdown 格式
- **层次化存储**: 新的 `archive/{year}/{month}/{day}/` 目录结构
- **自动化工作流**: Issue 创建时自动生成摘要并推送到 Bot

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