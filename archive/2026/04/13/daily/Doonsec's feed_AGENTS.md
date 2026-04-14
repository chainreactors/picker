---
title: AGENTS
url: https://mp.weixin.qq.com/s/2cGKBo45RrETywkMNzLPHg
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:41:11.639849
---

# AGENTS

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bfbRn7oUmpICSl7a77lPeujLPmmibRvX84L3UVgFlfttZVZofAtGM8ahn2ThR7wCUj6KwHKerOv76kCW0YOPrq3iaptynN4ckicovrQxeEALqc/0?wx_fmt=jpeg)

# AGENTS

原创

摸鱼信安
摸鱼信安

摸鱼信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz/bfbRn7oUmpIDV6rhib8C7akHnP57kOEiaIy0yeLelPrzT6o065V6ibLZ2VJDaLjq5pLFKkmZVcBvyicdIacg4Y1FUYZbhrmIbjqLHDLQ1utjSUE/640?wx_fmt=bmp&from=appmsg)

Cursor、Claude Code、Codex 这类 工具，用久了会发现它们经常自作主张：乱改全文件、自动 git push、代码里写死 API Key 、容易忘事等等问题。

AGENTS.md 就是解决这个问题的。在项目根目录放一个 `AGENTS.md` 文件，AI 就会按你的规则来，如果需要全局配置，比如 codex，就只需要把它放在

```
/Users/you_user_name/.codex
```

目录下即可全局生效

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bfbRn7oUmpLhAibZgfdiamAwKw5UEx0lOzp3CD5EEvuYOuiaZJoEic78W92U33g3xerm5lRFXtggfNiceOaqpsiaAG072JlrUlt17Vb0hk2rZIPCU/640?wx_fmt=png&from=appmsg)

## AGENTS.md 是什么

一份放在项目根目录的纯文本文件，用自然语言约束 AI 的行为。Cursor、Claude Code、Windsurf 等主流工具都会自动读取并遵守。

不需要插件，不需要配置文件，写清楚规则就行。

## 一份我自己在用的通用模版

可根据团队习惯微调范围、类型。

```
## 1. 语言偏好

- **默认语言**：始终使用简体中文回答（除非处理特定编程语言的文档翻译）。
- **回复风格**：直接、专业、去 AI 化。避免“作为一个 AI 助手”、“好的，我明白了”等废话。
- **术语规范**：保留专业编程术语（如 Closure, Generic, Concurrency），不要过度翻译。

## 2. 编码与规范

### 2.1 Git 提交规范

必须遵循 `<type>(<scope>): <subject>` 格式：

- **类型**：`feat`、`fix`、`docs`、`style`、`refactor`、`perf`、`test`、`build`、`ci`、`chore`、`revert`
- **范围**：`core`、`api`、`ui`、`docker`、`k8s`、`security`、`scripts`、`config`
- **操作限制**：仅允许执行 `git commit` 生成本地提交，**禁止自动执行 `git push` 或任何远程同步操作**。提交信息必须使用简体中文描述。

### 2.2 代码质量

- **注释要求**：仅解释“为什么”而非“是什么”。禁止描述语法细节。
- **防御性编程**：禁止空 `catch` 块；所有异常必须有明确处理或日志记录。
- **增量修改**：仅输出变更代码块，禁止重复全文内容。
- **代码风格**：遵循项目既定的代码风格指南（如 PEP8、Google Java Style Guide 等）。

## 3. 技术专项规范

### 3.1 安全审计

- **敏感信息**：严禁硬编码 API Keys、密码、Token，不允许读取环境变量中的敏感信息（如要读取，请询问我）、不允许读取敏感信息配置文件，严禁在生成的代码、建议或回答中输出硬编码的密钥、密码、Token；如需引用配置项，必须使用占位符并提醒用户从安全存储获取。
- **漏洞防范**：审计注入 (SQLi/XSS)、反序列化风险、越权检查 (IDOR)。
- **组件依赖**：禁止主动建议引入来源不明或无主流社区背书的第三方库；若需推荐，应附带安全警告，并让用户确认是否引用。

## 4. 工具调用边界

- **只读优先**：在未明确授权时，默认使用只读命令（如 `cat`、`ls`、`git status`）。
- **破坏性操作确认**：涉及 `rm`、`git reset --hard`、`kubectl delete` 等操作前，必须输出警告并等待用户二次确认。
```

## 关于 Skill

推荐两个比较好用的 Skill 搜索网站

有一些奇奇怪怪的和一些有意思的 skill

https://skills.sh/

https://modelscope.cn/skills

## ref

https://developers.openai.com/codex/guides/agents-md

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ZaoI13zBQuevMHz8QReZjgT2m0icnNdpsuKh62Y70fd9NKOrhwIgpGuTbW08HGAGic6RfMB9VjySJkyKhF5p9dww/0?wx_fmt=png)

摸鱼信安

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZaoI13zBQuevMHz8QReZjgT2m0icnNdpsuKh62Y70fd9NKOrhwIgpGuTbW08HGAGic6RfMB9VjySJkyKhF5p9dww/0?wx_fmt=png)

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