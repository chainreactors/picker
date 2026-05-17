---
title: 多智能体协作的自主渗透测试框架Abyss，像专家一样思考
url: https://mp.weixin.qq.com/s/TnAgDNoFvytZJcragivbAQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:42:34.435625
---

# 多智能体协作的自主渗透测试框架Abyss，像专家一样思考

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODwD3CusXbnianW8ShDaAVp6Vwb5Ue3eRBuicaxttp9nL7JTOMHO6b5LTkhle7iazvx9uEF8qyUCYSgxRvunaZtjOphfVPu1Ufm3DE/0?wx_fmt=jpeg)

# 多智能体协作的自主渗透测试框架Abyss，像专家一样思考

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 多智能体协作的自主渗透测试框架Abyss，像专家一样思考

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  Abyss 是一个基于多智能体协作的自主渗透测试框架，通过递进式渗透策略模拟人类安全专家的思维链，从单点漏洞逐步深入探索系统深处。

## 🚀 一句话优势

  像人类专家一样**自主思考、递进渗透**，而非机械扫描，让AI学会“如何钓鱼”而非“钓某条鱼”。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 多智能体协作 | 调度/执行/分析三类智能体协同决策 |
| 递进式渗透 | 从单点漏洞出发，逐步深入系统核心 |
| 动态学习 | 根据渗透反馈实时调整攻击策略 |
| 方法论驱动 | 基于通用渗透测试方法论自主推理 |
| 全技能覆盖 | OWASP Top 10:2025全量覆盖 + 五阶段渗透流程 |

## 📸 运行截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODynkUErCHliaWeRqQ5pZNF5ax7WvFgF28NeaQyY2OWHKIpdOK4hFczw9WYO4Jv1mjDX4OBscXAl7stmzroEB6hbuANKzW0Tiaehc/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzEw5fwHwo3cNuM9oDICw5h6atemowribrfYIiaDbYvmREZY1lv7RaqjAJxhiaHI8mDPaWL1AzJWJUd6dY8qO3fsoSV8oZU3JsUUY/640?wx_fmt=png&from=appmsg)

## ✨ 核心亮点

### 1. 三智能体协作架构

  与单 Agent 扁平化交互不同，Abyss 采用 **调度智能体 + 执行智能体 + 分析智能体** 的分工协作模式。调度智能体负责全局任务规划和策略制定；执行智能体具体调用技能和操作命令；分析智能体负责结果复盘和经验沉淀。这种 “决策-执行-反馈”闭环 让系统能从每一次操作中学习，持续优化后续渗透路径。

### 2. 方法论驱动而非脚本驱动

  Abyss 的核心差异在于：它内置的是 **标准渗透测试方法论**（信息收集 → 威胁建模 → 漏洞分析 → 渗透利用 → 后渗透），而不是针对特定靶场的“刷题式”知识。这意味着它具备 *泛化能力*，可以迁移到全新的目标、环境和未知漏洞场景，而非仅仅在某个 benchmark 上表现出色。项目在 validation-benchmarks 测试中完成率超过 *90%*，且未进行定向知识注入。

### 3. 递进式渗透与可视化追踪

  系统从单点漏洞切入后，会自主探索攻击路径，逐步横向移动、权限提升，最终抵达系统深处。Web UI 实时展示渗透过程和智能体思考逻辑，关键信息高亮显示，攻击路径可视化呈现。这种设计让你既能看清结果，也能理解 AI 每一步决策的依据，避免“黑盒”式的不信任感。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| DeepAgent框架 | 三类智能体通过协作机制协同 | 分工明确，决策与执行分离，便于扩展新智能体 |
| 五阶段渗透方法论 | 信息收集/威胁建模/漏洞分析/渗透利用/后渗透 | 系统化指导而非随意调用工具 |
| 执行沙箱隔离 | Docker构建独立执行环境 | 渗透操作与宿主机隔离，安全性高 |
| WebSocket实时通信 | 前后端通过WebSocket推送流式数据 | 用户可实时查看智能体思考和执行过程 |
| 多Vendor模型支持 | 兼容OpenAI/Qwen/ChatGLM/文心一言及本地部署模型 | 灵活选择模型，降低使用成本 |

## 📖 使用指南

① **准备工作** 克隆项目后创建 Python 3.12+ 虚拟环境 `python3.12 -m venv venv` 并安装依赖 `pip install -r requirements.txt`。在前端目录 `Abyss_web` 下执行 `npm install`。然后在 `Abyss/llm/.api_key.json` 中配置 **base\_url**、**api\_key** 和 **model\_type**。最后构建执行沙箱 `cd Abyss/docker/kali && ./build_image.sh` 并启动沙箱容器。

② **核心操作** 分两个终端启动：终端1执行 `python start.py` 启动后端（RESTful API 在 *http://0.0.0.0:80*，WebSocket 在 *ws://0.0.0.0:8765*）；终端2在 `Abyss_web` 目录下执行 `npm run dev` 启动前端。浏览器访问 *http://localhost:3000*，输入目标地址即可开始使用。*Docker 用户可直接执行构建脚本后一键创建并启动容器*。

③ **结果查看** 渗透过程中，Web UI 会实时展示每个智能体的决策过程、执行结果和攻击路径。渗透完成后，系统输出 **关键信息**（漏洞详情、攻击路径）、**渗透报告**（过程记录、风险评级）和 **修复建议**（技术修复、架构优化），方便你后续进行复现和整改。

## 📖 项目地址

```
https://github.com/zhanglimao/Abyss
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

⚠️打广告的勿进，会直接踢掉！！！

| ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzDcbialtDJB2iauRibULjWbzQk2oeHEyuNcGjibhWw6SpJia0RYGY3D7UhMASYr1QPAicb1LaSL1XlDrVowaibjeB41IKYSBHE8z9sN8/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwMu4dL9ZhibwZKibzwdD01Btq6ia2183uH0ibzaGibkr1aribDe1jicrtW0px8pd6Rz1kT7QpTtzfdmicibiaFZHSqI40srWZhLQ9HpR1JY/640?wx_fmt=png&from=appmsg) |
| --- | --- |

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