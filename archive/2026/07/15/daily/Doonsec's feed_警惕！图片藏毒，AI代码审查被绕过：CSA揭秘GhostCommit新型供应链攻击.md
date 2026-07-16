---
title: 警惕！图片藏毒，AI代码审查被绕过：CSA揭秘GhostCommit新型供应链攻击
url: https://mp.weixin.qq.com/s/5kcQecKD_3hzuZ6QsdUEUQ
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:52:59.150871
---

# 警惕！图片藏毒，AI代码审查被绕过：CSA揭秘GhostCommit新型供应链攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dJ6206EMFEhCMzud0PMhEP5BXDNo2uYx21OABHYDsmmRwuUrZiaCHgWsl5RPkprHyw287ZFIRTQxrsNDVUCMIyJRKNzaBGWxJF6ywnoia6jwo/0?wx_fmt=jpeg)

# 警惕！图片藏毒，AI代码审查被绕过：CSA揭秘GhostCommit新型供应链攻击

国际云安全联盟CSA上海代表处

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年7月13日，云安全联盟（CSA）发布了《CSA Research Note - GhostCommit: Image Prompt Injection in AI Code Review》。该报告揭示了一种极具隐蔽性的新型供应链攻击手法——**攻击者将恶意提示指令隐藏在看似无害的PNG图片中**，成功绕过了主流的AI代码审查工具。这种**“图片藏毒”**的方式，正对日益普及的AI辅助开发流程构成严峻威胁。

更值得警惕的是，ASSET研究团队对300个活跃公开仓库中6480个Pull Request的审计发现：73%的合并请求在到达主分支时未经过任何实质性的人工或机器人审查。**GhostCommit并不需要攻破严密的审查防线——它只需要落入那四分之三的无人审查区间。**

**攻击原理详解：隐藏在像素中的恶意指令**

![](https://mmbiz.qpic.cn/mmbiz_png/dJ6206EMFEiaNQu0KG7LZkU1xgCsqRBZjlrHia86EY6tszHv37lCKicVymsKQibic7SOrqXKSKutaxFTdSIMv6twjaWQ8n8Pd2OrXDjPia3UWG2x0/640?wx_fmt=png&from=appmsg)

**什么是GhostCommit攻击？** GhostCommit 是一种针对AI代码审查机制的提示注入攻击。攻击者利用AI工具在处理多模态内容时的盲区，将恶意指令嵌入到图片文件中，从而在代码合并或后续开发中触发恶意行为。

**恶意提示如何嵌入PNG图片？**攻击者通过特殊手段，将恶意的提示词（Prompt）直接写入PNG图片的元数据或像素中。由于传统文本审查工具将图片视为不透明的二进制文件，这些隐藏的指令得以完美潜伏。

**如何绕过AI代码审查工具？** 目前主流的AI代码审查工具（如CodeRabbit）在默认配置下会直接跳过PNG等图片文件的审查。这意味着包含恶意指令的图片可以毫无阻碍地通过代码拉取请求（Pull Request），被合并到主代码库中。

**攻击载荷拆分部署策略** 为了降低被怀疑的风险，攻击者采用了拆分部署策略：在代码仓库内新增一个看似合规的 AGENTS.md 文档。该文档会引导代码智能体（AI Agent）在特定条件下，从引用的图片中提取并执行隐藏的构建常量或指令。

**攻击触发流程：延后触发的定时炸弹**

这种攻击的狡猾之处在于，代码合并时并不会直接窃取数据，而是将陷阱延后触发：

**1.潜伏阶段：**包含恶意图片和AGENTS.md的代码被正常合入主仓库，AI审查工具未发出任何告警。此时恶意载荷处于休眠状态，与普通项目资产无异。

**2. 触发阶段：**开发者在全新会话中向代码智能体发起常规功能开发需求。智能体读取已合并到本地的AGENTS.md作为项目规范，攻击链路正式启动。

**3. 解析阶段：**AGENTS.md指示智能体从引用的PNG图片中提取构建常量。智能体调用多模态能力解析图片，读取到隐藏在其中的恶意指令文本。

**4. 窃取阶段：**智能体遵循指令读取本地的.env文件，将全部密钥内容编码为ASCII数字序列，作为源代码中的整数型常量输出。

**5. 外传阶段：**攻击者只需在Pull Request中看到数百位整数型常量，逆向解码即可获得完整的API密钥、数据库地址和云平台凭证。

技术演进脉络：GhostCommit并非凭空出现。2025年8月，Trail of Bits安全团队首次展示了通过图片缩放触发隐藏提示注入的攻击技术——一张在全分辨率下看似无害的图片，经AI预处理管道缩放后暴露出隐藏的恶意指令，成功突破了Google Gemini CLI等生产系统。他们还为此开源了检测工具Anamorpher。GhostCommit继承了"图片即攻击载体"的思路，但将隐蔽策略从视觉伪装转向了一个更根本的盲区：审查工具根本不检查图片内容。两类攻击的持续出现表明，**图片投毒正在成为对AI系统的反复出现的安全威胁类别**，而非孤立的PoC。

**实测案例：311个数字泄露全部机密**

CSA研究团队在实测中发现，搭载 Claude Sonnet 模型的 Cursor 工具在首次执行该攻击链路时，便直接输出了包含311个数字的元组。经过解码，受害者的API密钥、数据库地址以及云平台凭证全部内嵌在看似普通的代码输出中，泄露过程悄无声息。

值得关注的是，研究团队同时开发了一款多模态防御扫描原型。在针对80个从未见过的攻击PR的测试中，该原型成功拦截了79个，同时在30个合法PR上实现了零误报。这说明构建"图像感知审查层"并非纯理论设想，而是已有技术可行性的防御路径。

**检测盲区分析：为何漏洞机器人保持沉默？**

此次攻击之所以能够成功，主要利用了当前安全检测的三重盲区：

**第一、**文本类审查工具会将图片视作不透明的二进制文件，无法读取其中的隐藏文本
**第二、**CodeRabbit 等工具的默认配置直接跳过 PNG 文件审查
**第三、**整条Pull Request可以在无任何告警的情况下通过，漏洞机器人不会输出任何风险提示

**受影响工具与模型：框架决定安全性**

测试表明，攻击能否得逞，核心取决于**工具的运行框架，而非底层大模型本身：**

**• 高风险工具：**

**◦ Cursor工具：**搭配 Claude Sonnet 4.6、Composer-2、GPT-5.5 均会完整泄露 .env 文件。

**◦ Antigravity工具****：**搭配 Sonnet、Gemini 3.1 Pro、Gemini 3 Flash 全部存在泄露风险。

**• 安全工具：**

**◦ Claude Code平台：**同系列所有模型（Sonnet 4.6、Haiku 4.5、Opus 4.7）均能成功阻断此类攻击。

**CSA框架体系：不止发现漏洞，更要系统性防御**

GhostCommit的攻击链——从被合入的规范文件，经智能体读取的图片指令，到具有.env文件读取权限的Agent——**完整映射了CSA MAESTRO框架**（Agentic AI威胁建模框架）中定义的各层风险面：工具使用层、不可信工件消费层、凭证访问层，每一层都需要独立的安全控制。CSA的AI Controls Matrix（AICM）v1.1则为落地提供了控制映射词汇表，涵盖应用与接口安全（代码审查应扩展至AI Agent消费的非文本工件）和身份与访问管理（Agent可读取的凭证范围决定了注入攻击的损害上限）两个关键域。正如CSA在《Securing LLM-Backed Systems: Essential Authorization Practices》中强调的：**依赖模型自我审核输入是不够的，系统必须在外部设置授权检查点和验证层。**

**防御建议：如何抵御GhostCommit攻击？**

面对这一新型威胁，企业和开发者应采取以下防御措施：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEgsViaibAeXBuH92IZYxWyn5xZa6xic8vWdLkia6WtGaj4xjtk7huP81csrMDHI8vtdDuyhynFRKpzwONK43qzV2iadG59g5PnvBEuY/640?wx_fmt=png&from=appmsg)

**1.启用多模态图片审查**：配置AI代码审查工具（如CodeRabbit）取消对PNG等图片文件的跳过规则，增加对PR中所有图片文件的多模态LLM扫描步骤。具体可执行：在CI流程中加入图片文本提取步骤，对AGENTS.md引用的每张图片执行OCR+LLM检测，确认图片中不含隐藏指令。

**2.审查规范文件引用：**将AGENTS.md、CLAUDE.md等AI规范文件纳入强制审查清单。具体检查项包括：规范文件中所有引用外部图片的路径、URL或资源标识符；确认每张被引用图片的实际渲染内容是否包含配置指令或可执行提示词；禁止规范文件引用未经审查的外部图片资源。

**3.最小权限与审计：**限制AI Agent的文件系统访问范围，禁止Agent在常规开发会话中读取.env等凭据文件。开启agent操作审计日志，记录所有文件读取操作，特别是对AGENTS.md引用图片的访问行为，并对异常的大量数字常量输出设置告警阈值。

**4.凭证轮换与隔离：**建立敏感凭证的自动轮换机制（建议每90天轮换一次）。对已暴露的凭证执行立即轮换，前提条件是AI Agent曾访问过包含图片引用的规范文件。使用Secret Scanner的扩展规则检测代码中的整数型常量序列模式（连续数百位数字），将其纳入凭证泄露检测范围。

**5.评估工具框架安全设计：**企业在选型时应要求供应商说明其对规范文件和不可信工件的处理策略，不能将模型安全训练视为工具安全性的充分代理。

**6.跟踪防御工具进展：**持续关注开源社区的AI安全防御工具更新，特别是多模态扫描类工具（如基于Anamorpher的图片安全检测方案），及时将成熟方案纳入组织的CI/CD流水线。

**结语**

当**73%的PR得不到实质性审查****，当一张看似无害的PNG就能让311个数字携带全部机密悄然流出，**传统的代码安全边界已被打破。AI Agent在开发流程中的深度普及不应以供应链安全为代价。这不是对未来风险的预警——这是已经发生的攻击面转移。**企业和开发者必须重新审视AI辅助开发环境下的信任模型：智能助手应成为生产力的倍增器，而非供应链攻击的突破口。**

![](https://mmbiz.qpic.cn/mmbiz_png/dJ6206EMFEiajBQ6BnAveOL4FViabasgeKAYr7s2aqwhU9r1soRQRtxsibwia7uAyr9OT4icpS57PeyhTVf2XW4N5PJVia3Lxw7JVYkL41gRltsI0/640?wx_fmt=png&from=appmsg)

**下载报告**

如需了解更详细的技术细节、完整的实验数据以及CSA框架体系的深度解读，请关注公众号，回复“**CSA AI研究**”下载完整研究报告PDF。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dJ6206EMFEgYtzbH8NgJSgNFTPPdchGhP39pBnnCJXXtic8BNzj0VCAAib1MYxlB6Lv9pibcJAKYhcaS6xY1ibGTDeNs9o8fo8sWhMGJvMKQoh0/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dJ6206EMFEjm8GNOgWlKVibFnUGjukZVkDRNLK9xcmic3uTnNWclqT7a48VyNWFpJbwSLBcjeKg7wXeaMPdJ1xUpRtndLmTGxAVDtsLLwkdPo/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Atw1J8F68p5KiaFqiav31cr04yNib3LYJQr8icP8AOhorLFK4A5FQxavZVN0a03shJMibfe1uo0kicXia3XOmJ1S384VQ/0?wx_fmt=png)

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