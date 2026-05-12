---
title: AI 原生安全测试平台 - CyberStrikeAI
url: https://mp.weixin.qq.com/s/PiuCq-9adu-5t9W-Hpwk0g
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:34:34.085036
---

# AI 原生安全测试平台 - CyberStrikeAI

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Wq4VJsQicA19P8qzP6HwBZFx2A2apOKJg0M1Rz2HajYxiaZGl6I7q0eTl9rQmEUoN3eGSW18OwTiaRic4GCUxEs7jkJJxHpeKXgcOeF8OhHF2Bc/0?wx_fmt=jpeg)

# AI 原生安全测试平台 - CyberStrikeAI

GSDK安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

01 项目地址

```
https://github.com/Ed1s0nZ/CyberStrikeAI
```

02 项目介绍

项目描述

CyberStrikeAI 是一个基于 Go 语言构建的 AI 原生安全测试平台。它集成了 100 多种安全工具、智能编排引擎、基于角色的预定义安全角色测试、具有专业测试技能的技能系统以及全面的生命周期管理功能。

![](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA18t8lmb2KxNjcIlsPAmwLeTEV58ict6GperpQOBcQ8jXQANPbreMJmehz84kn4ftbZm3VxKEsfD8RpoJvehM5ep8IMcs7X1wsIo/640?wx_fmt=png&from=appmsg)

主要功能

```
🤖 采用 OpenAI 兼容模型（GPT、Claude、DeepSeek 等）的 AI 决策引擎🔌 原生 MCP 实现，支持 HTTP/stdio/SSE 传输和外部 MCP 联合🧰 100 多个预构建工具配方 + 基于 YAML 的扩展系统📄 大量结果分页、压缩和可搜索存档🔗攻击链图、风险评分和逐步回放🔒 受密码保护的 Web 用户界面、审计日志和 SQLite 持久化📚 知识库（RAG），采用基于嵌入的向量检索（余弦相似度），可选的Eino Compose索引管道，以及可配置的检索后预算/重排序钩子📁 对话分组，支持置顶、重命名和批量管理🛡️ 漏洞管理，包括 CRUD 操作、严重性跟踪、状态工作流和统计信息📋 批量任务管理：创建任务队列，添加多个任务，并按顺序执行它们🎭 基于角色的测试：预定义的安全测试角色（渗透测试、CTF、Web 应用扫描等），并带有自定义提示和工具限制🧩多代理（CloudWeGo Eino）：除了单代理 ReAct ( /api/agent-loop) 之外，多模式( /api/multi-agent/stream) 提供deep（协调器 +task子代理）、plan_execute（规划器/执行器/重规划器）和supervisor（编排器 + transfer/ exit）；根据请求选择orchestration。Markdown 位于agents/：（orchestrator.md深度）orchestrator-plan-execute.md、，，以及适用的orchestrator-supervisor.md子代理（参见多代理文档）。*.md🎯技能（已针对 Eino 重构）：遵循skills_dirAgent技能布局（SKILL.md+ 可选文件）；多代理会话使用官方 Eino ADKskill工具进行渐进式披露（按名称加载），可通过可选的主机文件系统/shellmulti_agent.eino_skills进行加载；可选eino_middleware添加 patchtoolcalls、tool_search、plantask、reduction、检查点和深度调优——包含 20 多个示例领域（SQLi、XSS、API 安全等）。skills/📱聊天机器人：通过钉钉和飞书（Lark）建立长期连接，您可以通过移动设备与 CyberStrikeAI 进行对话（有关设置和命令，请参阅机器人/聊天机器人指南）🧑‍⚖️人机协作 (HITL)：聊天侧边栏可设置审批模式和工具允许列表（列表中的工具可跳过审批）；全局列表位于config.yaml下方hitl.tool_whitelist；应用功能可将新工具合并到文件中，并在不重启服务器的情况下更新正在运行的服务器；专用的HITL页面用于显示待审批事项。🐚 WebShell 管理：添加和管理 WebShell 连接（例如 IceSword/AntSword 兼容），使用虚拟终端执行命令，内置文件管理器进行文件操作，以及 AI 助手选项卡，用于协调测试并保留每个连接的对话历史记录；支持 PHP、ASP、ASPX、JSP 和自定义 shell 类型，并可配置请求方法和命令参数。
```

注：工具仅供安全研究与学习之用，若将工具做其他用途，由使用者承担全部法律及连带责任，作者及发布者不承担任何法律及连带责任。信息及工具收集于互联网，真实性及安全性自测！！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Xu1xJEZRrFjUe1HmsusbqLJiaQvscUlHp1kgYagMRTFy1TyiaryxmOjvkpS6UKic5ricVOjdicibiaLMTibKkUqiafYD8vw/0?wx_fmt=png)

GSDK安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xu1xJEZRrFjUe1HmsusbqLJiaQvscUlHp1kgYagMRTFy1TyiaryxmOjvkpS6UKic5ricVOjdicibiaLMTibKkUqiafYD8vw/0?wx_fmt=png)

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