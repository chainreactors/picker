---
title: AI 驱动的渗透测试 CLI 工具 — 说人话，打漏洞
url: https://mp.weixin.qq.com/s/M58-s1GDTAjSJT1cSI8jeg
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:08:17.350716
---

# AI 驱动的渗透测试 CLI 工具 — 说人话，打漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODw35p8PYIaTnecSXgugib1IHbvdSCv5fmOyOZQ7rfVn9ibrqPeqsTYjFEN9Wiaeia5xxFMmnhdaopBHshRWIXmT2fsPaVzJLhGT7s4/0?wx_fmt=jpeg)

# AI 驱动的渗透测试 CLI 工具 — 说人话，打漏洞

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# AI 驱动的渗透测试 CLI 工具 — 说人话，打漏洞

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  VulnClaw 是一款 AI 驱动的渗透测试 CLI 工具，支持**自然语言输入**，自动完成从信息收集到报告生成的全流程渗透测试。

## 🚀 一句话优势

  说人话就能打漏洞，**AI自动编排渗透测试全流程**，无需手动切换各类工具和脚本。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 自然语言驱动 | 用口语描述渗透意图，AI自动识别阶段和工具 |
| MCP工具链 | 内置11个MCP服务，23个工具定义，一键调用 |
| 20个渗透Skill | 7个核心Skill + 13个专项Skill，含138个参考文档 |
| 持续性渗透测试 | 周期循环模式，跨轮次状态保持，自动生成报告 |
| 多LLM提供商 | 支持OpenAI/MiniMax/DeepSeek等8个模型一键切换 |

## 📸 使用方式

1. 方式一：REPL 交互模式（推荐）
2. 方式二：单命令模式
3. 方式三：持续性渗透模式
4. 方式四：Web UI 模式

## ✨ 核心亮点

### 1. 自然语言驱动的全流程自动化

 输入“`帮我对 http://target.example.com 进行渗透测试`”，VulnClaw 的 **LLM Agent** 会自动执行任务编排：信息收集 → 漏洞发现 → 漏洞利用 → 报告生成。*你只需描述意图，系统会自动识别目标、阶段并调用对应工具*，每一轮输出都清晰标注当前进度与发现成果。

### 2. MCP 工具链与 Skill 编排体系

 项目内置了 **11 个 MCP 服务**（fetch、memory、chrome-devtools、burp、frida 等）和 **23 个工具定义**，覆盖 Web 渗透、移动端测试、逆向分析等场景。同时，*20 个渗透 Skill* 包含 138 篇参考文档，当 LLM 需要时可通过 `load_skill_reference` 工具按需加载，确保每一步操作都有方法论文档支撑，不再让 AI 凭空猜测。

### 3. 持续性渗透模式与跨周期状态继承

 采用 **周期循环机制**（默认 100 轮/周期 × 10 周期），每个周期结束后自动生成独立的 Markdown 报告，区分“本周期新增”和“累计总计”两个维度。跨周期时，*所有发现、漏洞和步骤记录自动继承*，你可以在任何时候按 `Ctrl+C` 中断，中断后仍生成本周期报告，不会丢失任何成果。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| LLM Agent核心 | OpenAI兼容协议 + Tool Calling + 自主渗透循环 | 支持多模型切换，不锁定单一供应商 |
| MCP编排层 | 服务注册 + 生命周期管理 + 自然语言→工具路由 | 模块化设计，可自由扩展新工具服务 |
| 反死循环机制 | 连续5轮无新发现时触发强制策略切换 | 避免AI在简单问题上无限循环 |
| 目标状态治理 | target\_state/store.py实现成果沉淀、恢复、快照、回滚 | 支持中断恢复，多轮次测试更可靠 |
| Pydantic配置模型 | YAML持久化 + 8个Provider预设 + 环境变量覆盖 | 三优先级配置管理，部署更灵活 |

## 📖 使用指南

① **准备工作** 通过 PyPI 安装 `pip install vulnclaw`，然后运行 `vulnclaw config provider minimax`（或 openai/deepseek）选择模型提供商，再运行 `vulnclaw config set llm.api_key sk-your-key-here` 设置 API Key。最后执行 `vulnclaw doctor` 检查运行环境是否就绪。

② **核心操作** 直接执行 `vulnclaw` 进入 REPL 交互模式，输入 `对 http://target.com 进行渗透测试` 或 `对 192.168.1.100 找出flag` 等自然语言指令。系统会*自动进入自主渗透模式*，分多轮输出发现成果。你也可以使用单命令模式：`vulnclaw run 192.168.1.100` 一键全流程执行。

③ **结果查看** 渗透测试完成后，VulnClaw 会自动生成 **Markdown 格式的渗透测试报告** 和 **Python PoC 脚本**，保存在 `./vulnclaw-output/` 目录下。在 REPL 界面中，你也可以输入“`生成渗透报告`”手动触发生成。若开启持续模式，每周期结束后报告自动生成。

## 📖 项目地址

```
https://github.com/Unclecheng-li/VulnClaw
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