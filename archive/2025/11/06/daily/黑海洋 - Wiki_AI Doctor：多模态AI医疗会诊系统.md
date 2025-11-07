---
title: AI Doctor：多模态AI医疗会诊系统
url: https://blog.upx8.com/4896
source: 黑海洋 - Wiki
date: 2025-11-06
fetch_date: 2025-11-07T03:10:28.530056
---

# AI Doctor：多模态AI医疗会诊系统

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# AI Doctor：多模态AI医疗会诊系统

发布时间:
2025-11-06

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
2612

## ai-doctor概览

AI 医疗会诊面板（ai-doctor）是一款多医生协同的会诊**模拟**系统。多个由不同大语言模型（LLM）驱动的“医生”在同一病例下展开讨论、互评与淘汰，逐步收敛到可参考的诊断结论。系统为纯前端架构，所有数据保存在浏览器本地，无需自建后端。

> **重要说明**：本项目为会诊模拟与教学研发用途，不构成医疗建议或临床诊断。

### 项目预览

* 在线预览：`https://dragonchencl.github.io/ai-doctor/`
* GitHub：`https://github.com/DragonChenCL/ai-doctor`

## 截图界面

[![](https://cdn.skyimg.net/up/2025/11/6/69da57ea.webp)](https://www.ahhhhfs.com/wp-content/uploads/2025/11/ai-doctor%EF%BC%9AAI-%E5%8C%BB%E7%96%97%E4%BC%9A%E8%AF%8A%E9%9D%A2%E6%9D%BF%EF%BC%8C%E5%A4%9A%E5%8C%BB%E7%94%9FAI%E5%8D%8F%E5%90%8C%E8%AF%8A%E6%96%AD%E6%A8%A1%E6%8B%9F%E7%B3%BB%E7%BB%9F05.jpg)

## 核心特性

* 🏥 多医生协作：可添加多个由不同 LLM 驱动的“医生”共同会诊。
* 🤖 多模型支持：对接 OpenAI、Anthropic Claude、Google Gemini、硅基流动、魔搭社区等主流模型与兼容服务。
* 💬 实时讨论：医生轮流发言，打字机效果直观呈现。
* 🗳️ 智能评估：互评不准确意见并自动淘汰，提升结论可参考性。
* 📊 状态监控：会诊阶段、轮次、在席医生与投票统计一目了然。
* 💾 会话管理：问诊记录自动保存，可在多会话间快速切换。
* 🎨 设计易用：基于 Ant Design Vue，布局清晰、交互顺手。
* 📱 纯前端：浏览器直连各家 API，数据仅存本地 `localStorage`。

## 适用场景

* 医学与 AI 课程演示
* 多模型协作流程验证
* 医疗 NLP 研究的交互式原型
* 团队内部方法论对比与教学

## 快速开始

**环境要求**：Node.js ≥ 16；包管理器推荐 pnpm ≥ 9（或 npm）。

**安装与运行**

```
git clone <repository-url>
cd ai-medical-consultation-panel
pnpm install      # 或 npm install
pnpm dev          # 或 npm run dev
# 访问 http://localhost:5173
```

**生产构建**

```
pnpm build        # 或 npm run build
# 构建产物位于 dist/
```

**代理与环境变量**
生产环境默认直连第三方 API。若需继续通过本地代理，构建时设置
`VITE_ENABLE_PROXY=true`，并在部署环境提供 `/api-proxy` 转发能力。

## 使用步骤

### 1）配置医生

* 打开右上角「设置」→「医生配置」。
* 录入：医生名称、供应商（OpenAI 规范 / Anthropic 规范 / Gemini 规范 / 硅基流动 / 魔搭社区）、API Key、可选 Base URL、模型名称与提示词。
* 通过「添加医生」扩展多名参与者，并在「问诊医生」选择本次参与会诊的医生。

### 2）输入病例

* 在主页面填写：患者姓名（必填）、年龄、既往史、本次问题（必填）。
* 点击「开始会诊」。

### 3）观察会诊

* 医生轮流发言并提出诊断建议。
* 每轮结束进行互评；被多数标记为“不太准确”的医生会被淘汰。
* 达到设定条件时会诊结束：仅剩一位医生，或连续多轮无人淘汰达到上限。

### 4）查看结论

* 系统生成诊断总结：核心诊断、依据、鉴别诊断、检查与治疗建议、随访计划、风险提示。
* 通过「查看最终答案」查看并可导出图片留存。

## 评估机制与持久化

* **自动化同行评审**：每轮发言完成后，全体在席医生对当轮发言评估并投票。
* **淘汰规则**：获得最多“不太准确”票的医生出局；若票数相同或无人获票，则本轮不淘汰。
* **数据本地化**：医生配置（含 API Key/模型）、会话记录、当前会诊进度均存储于浏览器 `localStorage`。清除浏览器数据会清空配置与记录。

## 支持的模型与服务

* **OpenAI 规范**：gpt-4o、gpt-4o-mini、gpt-4-turbo（Base URL：`https://api.openai.com/v1`，兼容同规范服务）
* **Anthropic 规范**：claude-3-5-sonnet-20241022、claude-3-opus-20240229、claude-3-haiku-20240307（Base URL：`https://api.anthropic.com/v1`）
* **Gemini 规范**：gemini-1.5-pro、gemini-1.5-flash（Base URL：`https://generativelanguage.googleapis.com/v1beta`）
* **硅基流动**：Qwen/Qwen2.5-7B-Instruct、THUDM/glm-4-9b-chat、Pro/Qwen/Qwen2.5-72B-Instruct（Base URL：`https://api.siliconflow.cn`）
* **魔搭社区**：qwen-turbo、qwen-plus、qwen-max（Base URL：`https://dashscope.aliyuncs.com`）

## 技术架构

* 前端框架：Vue 3
* 状态管理：Pinia
* UI：Ant Design Vue
* 构建工具：Vite
* Markdown 渲染：Marked
* HTTP：Axios
* 典型结构：`src/api`（AI 调用封装与模型列表）、`components`（病例表单、讨论面板、投票统计、状态面板等）、`store`（流程/全局/会话）、`utils/prompt.js`（提示词构建）

## 隐私与安全

* 纯前端架构，无后端存储与传输。
* 所有配置与会诊记录仅存于本地浏览器。
* 浏览器直连各家模型 API。
* 请妥善保管 API Key，避免泄露。

## ai-doctor开源与访问

在线体验：[https://dragonchencl.github.io/ai-doctor/](https://blog.upx8.com/go/aHR0cHM6Ly9kcmFnb25jaGVuY2wuZ2l0aHViLmlvL2FpLWRvY3Rvci8 "https://dragonchencl.github.io/ai-doctor/")

源码仓库：[https://github.com/DragonChenCL/ai-doctor](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0RyYWdvbkNoZW5DTC9haS1kb2N0b3I "https://github.com/DragonChenCL/ai-doctor")

[取消回复](https://blog.upx8.com/4896#respond-post-4896)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")