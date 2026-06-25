---
title: Shannon：Keygraph 开源 AI 渗透测试框架，从源码分析到真实漏洞利用
url: https://mp.weixin.qq.com/s/KDPO1p04xSVJGchnSC-qAQ
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:05:43.431857
---

# Shannon：Keygraph 开源 AI 渗透测试框架，从源码分析到真实漏洞利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/niasx7fyic9COkQLgJVVrsQsbWZGTswa47Vb9o4FSHrr3icE1VvxKj45jB7H0iaLPoFloVL2ZPDAqIRj1Wsn6tDdIt61kRJ0QBZUWhXuqGo9zG4/0?wx_fmt=jpeg)

# Shannon：Keygraph 开源 AI 渗透测试框架，从源码分析到真实漏洞利用

原创

Arthur
Arthur

C4安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COoG7BuQk5yicSWs7kjlticLDeibsozzl2z35TjVicYlDdic3q4beQXeHRCnE93wSSL0iaiaUg7prSYrb1UiaaC6ibDXiaAdk6twBFBr9BAM/640?wx_fmt=png&from=appmsg)

简介-主要功能

1. 完全自主的渗透测试流程

Shannon只需一个命令即可启动完整的渗透测试流程。系统自动处理从侦察到报告生成的所有阶段，包括目标识别、技术栈分析、攻击面映射、漏洞分析和实际利用。这种端到端的自动化使得非安全专家也能轻松运行专业的渗透测试。

2. 白盒源代码感知分析

与传统的黑盒扫描器不同，Shannon能够访问和分析应用程序的源代码。它通过代码审查理解应用程序的业务逻辑、数据流和控制流，从而指导攻击策略。这种代码感知能力使得Shannon能够发现那些仅通过外部观察难以识别的深层漏洞。

3. 可复现的漏洞证明

Shannon坚持“无漏洞利用，不报告”的原则。每个被报告的漏洞都附有可复制粘贴的漏洞证明（PoC），开发团队可以立即验证漏洞的真实性和严重程度。这种实践导向的方法大大减少了安全团队和开发团队之间的摩擦。

4. OWASP漏洞全面覆盖

系统专门针对OWASP Top 10中的关键类别进行优化，包括注入攻击（SQLi、命令注入）、跨站脚本（XSS）、服务器端请求伪造（SSRF）以及身份验证和授权漏洞。每个漏洞类别都有专门的智能体进行分析和利用。

5. 并行处理架构

为了提高测试效率，Shannon采用并行处理架构。漏洞分析和利用阶段在所有攻击类别中同时运行，这意味着注入攻击、XSS、SSRF等测试可以并行进行，而不是顺序执行，大大缩短了整体测试时间。

6. 集成安全工具链

Shannon在侦察和发现阶段集成了行业标准的工具，包括Nmap（端口扫描）、Subfinder（子域名发现）、WhatWeb（技术栈识别）和Schemathesis（API测试）。这些工具的输出被整合到AI的分析过程中，提供更全面的攻击面视图。

7. 多模型AI支持

除了原生的Anthropic Claude模型支持外，Shannon还兼容AWS Bedrock和Google Vertex AI，用户可以根据自己的基础设施偏好选择AI后端。系统使用三种模型层级：小型模型用于摘要任务，中型模型用于安全分析，大型模型用于深度推理。

8. 工作空间和恢复功能

Shannon支持工作空间概念，允许用户为每次测试运行指定自定义名称。如果测试因故中断，可以从上次完成的地方恢复，跳过已经成功完成的智能体，避免重复工作，节省时间和API调用成本。

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CO7UQzlVASib90l450ibEnxxbJkdBomQ30yvvTW2wnicu1vlM76JPicGJo2hHV48RZbjG7NnwrUY6S5tnJgbLVeibVU3E1M22jnRxjY/640?wx_fmt=png&from=appmsg)

部署与运行全流程

环境准备

想要运行这个AI，你只需要两样东西：

Docker：Shannon 运行在容器中，确保环境隔离。
安装地址：`https://docs.docker.com/get-docker/`

```
Anthropic API Key（推荐）：从 https://console.anthropic.com 获取。
也支持 Claude Code OAuth Token，或实验性地通过 OpenRouter 使用 OpenAI / Gemini 模型。
```

第一步：克隆项目

代码语言：

```
git clone https://github.com/KeygraphHQ/shannon.git
cd shannon
```

第二步：配置凭证

方式 A：环境变量（推荐快速上手）

```
export ANTHROPIC_API_KEY="你的API密钥"
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000
```

方式 B：创建 .env 文件（推荐长期使用）

```
cat > .env << 'EOF'
ANTHROPIC_API_KEY=你的API密钥
CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000
EOF
```

第三步：启动渗透测试

```
./shannon start URL=https://你的应用地址.com REPO=/你的源码路径
```

Shannon 会自动构建容器、启动工作流，并返回一个工作流 ID。

整个测试在后台运行。

如果你在本地测试：Docker 容器无法直接访问宿主机的 localhost，需要改用 host.docker.internal：

```
./shannon start URL=http://host.docker.internal:3000 REPO=/path/to/repo
```

第四步：监控进度

```
# 查看实时日志
./shannon logs

# 查询特定工作流的进度
./shannon query ID=shannon-1234567890

# 打开 Temporal Web UI 查看详细状态
open http://localhost:8233
```

第五步：查看结果
测试完成后，报告默认保存在 ./audit-logs/ 目录下：

```
audit-logs/{hostname}_{sessionId}/
├── session.json          # 会话指标数据
├── agents/               # 各 Agent 的执行日志
├── prompts/              # Prompt 快照（用于复现）
└── deliverables/
    └── comprehensive_security_assessment_report.md   # 最终安全评估报告
```

第六步：停止服务

```
# 停止容器（保留工作流数据）
./shannon stop

# 完全清理（删除所有数据）
./shannon stop CLEAN=true
```

**GitHub地址官方仓库地址：**
https://github.com/KeygraphHQ/shannon

---

内部CTF课程上线，总课程30+小时，优惠折扣中！

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMn2cvicQcFw5AXpSic9kSQmHAu2xBjr64xx257ro91bRpOpaozODD7qChxZJppicia3MH1fUB96uSdrqJKw7j0rbJPLZGA6ibs74Ls/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=14)](https://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247490327&idx=1&sn=1c18cf9b93edc1488dbc3d3aff30fb5a&scene=21#wechat_redirect)

帮会简介

《安全渗透感知》是FreeBuf知识大陆的重量级帮会，帮会致力于漏洞POC/EXP、红队攻防实战，是系统化从基础入门到实战漏洞挖掘的教程社区，包含团队自整的挖掘注意点和案例，还包含分享的渗透经验、SRC漏洞案例、代码审计、挖洞思路等高价值资源。

内容框架（持续新增中）

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPicIHacGn6WU5cBbNnGnt7d9xibnwexZXDYIcO57nxicEC3kEFvZt9WLQOnobjVCicrHa5s9WN1mKtMFIbm20llDW0Nsicabhia96k0/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=15)

目前已有「700+」小伙伴加入了帮会

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNQHD7ibWIFPyxIvTeBibBNictHVf67R7zUpbZibu7BUGEmdibxf4N8FYC3AHBzhnSITMDx9ABiacUe7iaowg41KGWf3QczlLWXTy2icBE/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=17)

加入方式

目前帮会成员700+人，永久会员优惠后只需69.9元。

随着人数的增加及资源的积累，之后永久会员将涨价至99元。

有意向的师傅们可以扫码加入我们，共同进步。

如何加入帮会？→ 安卓/苹果用户可扫码使用优惠券↓↓

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMj3KCCWibqnxKPhJrWJGibnZqxrs6X3MuQfkzB7qcuFsRKMIJgxGwwGVFeHHaLSQlb8c3Xvfh0yZE23oyCvV84vhsGxecp8l1d8/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=18)

→ PC端用户可复制此链接到浏览器↓↓

https://wiki.freebuf.com/societyDetail?society\_id=184

已加入帮会的小伙伴可以加帮主进帮会内部交流群

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/niasx7fyic9COA2GBA2hTF2mNpams9kCL6DSSCG9KRYyv81skETzEYFSrIazMBLhTHo3JFd7upib3V3gd7mcDg3LgYK27YBibm1ibL3yvibthwlS0/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=20)

请备注：帮会

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

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