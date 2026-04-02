---
title: AI 驱动的自动化安全测试与多前端工作台
url: https://mp.weixin.qq.com/s/4nb4XgjXLv-B1Toe4ZA8mA
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:22:28.573648
---

# AI 驱动的自动化安全测试与多前端工作台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODztzQicPnjYy1CL9mu6GP7Vf9AMm1vl5Q8cRuWbvXiahSib2icwtnReLBaKJ1BEbNP4NruHwMVqJNzviclJT9PRjoiaHh0y7uJvqYicEM/0?wx_fmt=jpeg)

# AI 驱动的自动化安全测试与多前端工作台

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# AI 驱动的自动化安全测试与多前端工作台

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  Secbot 是 **AI 驱动的自动化安全测试平台**，基于 *LangChain/LangGraph* 实现多智能体编排，通过 **FastAPI** 提供统一后端，支持 *CLI/TUI/移动端/桌面端* 多形态前端，面向**安全研究员**与**红队工程师**，实现从规划到报告的全流程自动化渗透测试。

## 🚀 一句话优势

**多智能体协同执行**，统一后端支撑 *CLI/TUI/移动端/桌面端* 全平台安全测试。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 多智能体模式 | secbot-cli 自动模式 / superhackbot 专家模式 |
| 安全测试覆盖 | 内网发现、Web 安全、OSINT、系统控制 |
| 多推理后端 | Ollama、DeepSeek、OpenAI、Anthropic 等 |
| 多前端形态 | CLI、TUI、移动端、桌面端共用一套后端 |
| SQLite 持久化 | 对话历史、提示词链、API Key 配置存储 |
| SSE 实时流 | 后端事件实时推送至各前端 |

## 📸 运行截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODziajKjeF0QECmCgQIZT04ichjY0AKkRficNbrpKRQQljBoRFwGmlIYuvy53db27PVRtCwEXhicJcmNw3Vk79tZhPB1VibeVuZk0yfQ/640?wx_fmt=png&from=appmsg)

## ✨ 核心亮点

### 1. 多智能体安全测试编排

  基于 **LangGraph** 实现 *规划-执行-总结* 的智能体工作流，支持 **secbot-cli 自动模式**（快速任务执行）与 superhackbot 专家模式（深度分析）两种形态。覆盖**内网资产发现**、*端口服务识别*、Web 漏洞扫描、**OSINT 情报收集**、*系统控制*、防御扫描与**报告生成**七大安全测试维度，AI 自动拆解复杂任务并调度对应工具链完成执行。

### 2. 统一后端与多前端架构

  采用 **FastAPI** 构建统一后端，暴露 *REST + SSE* 接口供多前端消费。同一套**智能体编排与事件流**同时支撑 **terminal-ui**（Ink 实现的 TUI）、app（Expo/React Native 移动端）、*desktop*（Tauri + Vite 桌面端）三种形态，实现**跨平台体验一致性**。SQLite 持久化层存储对话历史、提示词链与 API Key，支持会话状态跨端同步。

### 3. 多模型后端灵活适配

  内置 **Ollama、DeepSeek、OpenAI、Anthropic、Gemini、Groq、OpenRouter** 及多家 OpenAI 兼容厂商的适配器，通过 **LLM\_PROVIDER** 环境变量一键切换。本地部署选用 *OLLAMA\_MODEL*（如 gemma3:1b），云端调用配置 DEEPSEEK\_API\_KEY 即可使用 **deepseek-reasoner**，满足不同场景下的**成本**与*性能*平衡需求。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| LangChain/LangGraph | 智能体编排框架 | 复杂任务拆解与状态管理 |
| FastAPI + SSE | 异步 Web 框架 + 服务端推送 | 实时事件流，低延迟响应 |
| SQLite | 轻量级关系型数据库 | 零配置，持久化存储 |
| Ink | React 驱动的 TUI 框架 | 终端内的富交互体验 |
| Tauri | Rust 驱动的桌面端框架 | 安全沙箱，体积小巧 |
| Expo | React Native 跨平台方案 | iOS/Android 一套代码 |
| uv | Rust 编写的 Python 包管理 | 极速依赖解析与安装 |

## 📖 使用指南

① **准备工作**：克隆仓库后执行 uv sync 安装 Python 依赖，进入 *terminal-ui/* 目录运行 npm install。创建 **.env** 文件配置 *LLM\_PROVIDER*（如 deepseek）与对应 **API\_KEY**，本地模型需启动 *Ollama* 服务。

② **核心操作**：运行 python main.py 或 *uv run secbot* 自动拉起后端并进入 **全屏 TUI**。常用斜杠命令：**/model** 切换推理后端，/agent 切换智能体模式，*/system-info* 查看系统状态。单独启动后端使用 uv run secbot --backend，单独启动 TUI 使用 *uv run secbot --tui*。

③ **结果查看**：安全测试任务执行过程中，**SSE 实时流**推送事件至前端显示。测试完成后自动生成**结构化报告**，存储于 *SQLite* 数据库中，可通过 **/db-stats** 查看统计，历史对话与结果支持**跨端同步**访问。

## 📖 项目地址

```
https://github.com/iammm0/secbot
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

⚠️打广告的勿进，会直接踢掉！！！

| ![img](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODwHdUbwzDLq3nh7hplKZNDBERhMYooic5cPGwPHEJRonMYCoupeaa6fPuwOKehMek9HTEvnLaG0uuiaScGxWWmibtK9XNFHF4PJD0/640?wx_fmt=jpeg&from=appmsg) | ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg) |
| --- | --- |
| ![img](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODzCtog7ElLXnrLg7t9j99DftdLLjjVKFwP6unsUPX1EquflicE51wMFjB3zIBWLf6W3qFHA5modicNn3XbwJE8roDq7njXZRfjuo/640?wx_fmt=jpeg&from=appmsg) |

### 推荐阅读

✦ ✦ ✦

| [渗透测试人员必备武器库：子域名爆破、漏洞扫描、内网渗透、工控安全工具全收录](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485592&idx=1&sn=818004a6d625c4c4112ce73b83433854&scene=21#wechat_redirect) |
| --- |
| [AI驱动的自动化红队编排框架(AutoRedTeam-Orchestrator)跨平台支持，集成 130+ 安全工具与 2000+ Payload](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485309&idx=1&sn=292afbe37fb95c64f33470f915b0c54e&scene=21#wechat_redirect) |
| [JS逆向必备：这款插件能Bypass Debugger、Hook CryptoJS、抓取路由](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247486181&idx=1&sn=3ace47da643c72cec0d615aeccb955ac&scene=21#wechat_redirect) |
| [上传代码即审计：AI 驱动的自动化漏洞挖掘与 POC 验证平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485488&idx=1&sn=a37acb031febe69db608de53ddee5732&scene=21#wechat_redirect) |
| [AI 原生安全测试平台(CyberStrikeAI)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485208&idx=1&sn=b5181181c1e0800124e3e099706ef2ef&scene=21#wechat_redirect) |
| [多Agent智能协作+40+工具调用：基于大模型的端到端自动化漏洞挖掘与验证系统](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485805&idx=1&sn=8f374a239135f6a753d5cce887f8318b&scene=21#wechat_redirect) |
| [基于DeepSeek的代码审计工具 (Ai-SAST-tool.xjar)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485314&idx=1&sn=56082cd314311ffc15cc0bcf03a395e2&scene=21#wechat_redirect) |
| [基于AI的自主渗透测试平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485127&idx=1&sn=b5eb3fdc1cc23976011e2bca396c1bc7&scene=21#wechat_redirect) |

✦ ✦ ✦

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

0x八月

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

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