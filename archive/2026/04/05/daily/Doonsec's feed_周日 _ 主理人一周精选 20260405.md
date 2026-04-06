---
title: 周日 | 主理人一周精选 20260405
url: https://mp.weixin.qq.com/s/PgUpsHcKXe9EmOZjJF5TGA
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:42:38.569968
---

# 周日 | 主理人一周精选 20260405

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/z0u4bSRUopPqKfJcudBliabibic4ic2GkC9dFEfCPKGYT4Rxdv0SKJicNYGBPpNlp1vv4HazTeKYfUPaiasmVr4AIzg2qGCsnsbiaOLYDFwCTnUz4A/0?wx_fmt=jpeg)

# 周日 | 主理人一周精选 20260405

原创

t0data铁马
t0data铁马

AI安全圈

![]()

在小说阅读器中沉浸阅读

# 主理人一周精选资料分享

**本月热门趋势热词**llm、claude-code、ai-agents、agent、claude、openclaw、ai-agent、agent-skills

---

## 一、OpenClaude：开源多模型编码智能体 CLI

1. 近期开源项目 **OpenClaude** 推出跨平台编码智能体命令行工具，支持对接 OpenAI、Gemini、DeepSeek、Ollama 等 200+ 类 OpenAI 兼容接口。
2. 项目近三日新增 Star 增长迅猛，成为开源社区关注度最高的通用编码 Agent 脚手架之一。
3. 适合 AI 安全工程师、开发者快速搭建本地编码智能体环境，用于安全脚本生成与代码审计辅助。

🔗[https://github.com/Gitlawb/openclaude]

## 二、OpenHarness: 开源智能体运行基座

1. 香港大学数据科学实验室（HKUDS）开源 **OpenHarness** 项目，定位轻量级 AI Agent 运行框架，近三日涨幅高达 4904%，跻身 GitHub 相对涨幅前列。
2. 项目专注智能体执行环境、上下文调度与多 Agent 协同，为 Agent 工程化提供标准化运行底座。
3. 可用于企业内部智能体原型开发、流程验证，是当前 Agent 安全基线建设的重要参考实现。

🔗[https://github.com/HKUDS/OpenHarness]

## 三、Claude Code 相关生态项目合集

### 3.1 claude-code-prompts：提示工程模板库

1. 项目 `repowise-dev/claude-code-prompts` 提供独立编写的 Claude Code 风格提示模板，覆盖系统指令、工具调用、代理委派与多智能体协同。
2. 基于对 Claude Code 机制的研究总结，不涉及官方源码泄露，属于正向工程化参考资料。
3. 适用于企业构建规范编码 Agent 体系，提升指令鲁棒性与安全性。

🔗[https://github.com/repowise-dev/claude-code-prompts]

### 3.2 ClawGod：Claude Code 运行时补丁

1. 项目 `0Chencc/clawgod` 是官方 Claude Code 之上的运行时补丁，宣称兼容所有版本并随版本更新持续生效。
2. 该补丁用于修改运行时行为、扩展能力，并非攻防工具，也不具备植入后门、窃取上下文等攻击能力。
3. 安全团队可借此研究第三方修改对 AI 应用完整性的影响，强化供应链与运行时安全校验。

🔗[https://github.com/0Chencc/clawgod]

### 3.3 claw-code-parity 与社区复刻项目

1. `ultraworkers/claw-code-parity` 作为 Claude Code 迁移期间的临时维护项目，聚焦 Rust 版本兼容与功能对齐。
2. `claude-code-best/claude-code` 等社区复刻版本提供可运行、可调试的 Claude Code 风格实现，成为攻击面测绘与防御研究的常见参考对象。
3. 大量开源仿制项目涌现，使得闭源商业 AI 组件的内部逻辑高度透明，攻防信息差持续缩小。

🔗[https://github.com/ultraworkers/claw-code-parity]

## 四、其他高关注 AI Agent 安全相关项目

1. **everything-claude-code**：提供 Agent 性能优化、技能、记忆、安全研究框架，覆盖多类编码智能体安全能力建设。
2. **autoagent**：专注自治 Harness 工程，近三日涨幅超 27950%，代表自治智能体架构的研究热度飙升。
3. **harness-engineering** 系列仓库：围绕 Claude Code 机制延伸出 Harness Engineering 体系，成为智能体安全架构的重要研究方向。

---

**读书与研判视点**

## 五、[本周主理人网安前瞻思考笔记归档]

1. **智能体安全成为绝对焦点**：从 GitHub 趋势可见，社区重心已全面从通用 LLM 转向 AI Agent 工程化与安全。OpenHarness、autoagent 等项目爆发式增长，标志智能体标准化、攻防化时代正式到来。
2. **开源复刻=攻击面前置测绘**：围绕 Claude Code 的大量开源仿制、对齐、补丁项目，已成为攻击者研究闭源 AI 系统的标准路径。防御方必须默认攻击者具备近乎完整的系统结构知识，安全设计必须基于“透明化假设”。
3. **运行时安全与供应链风险加剧**：clawgod 等运行时补丁、社区复刻仓库、第三方技能插件共同构成新型攻击面。威胁不再局限于提示注入，而是延伸至环境篡改、行为劫持、依赖投毒等深层供应链风险，亟需纳入 DevSecOps 与 Agent 准入管控体系。

---

👉 加入AI安全圈，前沿资料尽享

👉 订阅AI安全日报，获取每日推送

![](https://mmbiz.qpic.cn/mmbiz_png/z0u4bSRUopPxn0mmJhiayU4kCOVF8XgmDic7lDfzleHuKgbS1PxANSVAHSPxG5T4AcX3jQTRH40Jsrundw0DBYIc8L6ebmNhZhtEylN8L8ahM/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0R80na6wzXdZWBKECSwo8H5S6LNZvXaLNemfgTALpBNqL3VpUlA3mQtwfrEoIh2LHb1zJuv8A5z0Jo60tH7pgw/0?wx_fmt=png)

AI安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0R80na6wzXdZWBKECSwo8H5S6LNZvXaLNemfgTALpBNqL3VpUlA3mQtwfrEoIh2LHb1zJuv8A5z0Jo60tH7pgw/0?wx_fmt=png)

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