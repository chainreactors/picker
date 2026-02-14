---
title: 春节福利！《2025开源供应链投毒分析技术报告》发布啦~
url: https://mp.weixin.qq.com/s/FPnMbX4ZyzAUmz-f3CKdyg
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:04:34.261126
---

# 春节福利！《2025开源供应链投毒分析技术报告》发布啦~

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcZeG6hJAyMzORDHVj8WZPCB9TnI5miawic6ExhzLUjHQJIdooM8VGzkKXD8n01XHx5X2bahz0ZYjA2dGblPkFFQzFlYVzCafeDQ/0?wx_fmt=jpeg)

# 春节福利！《2025开源供应链投毒分析技术报告》发布啦~

悬镜安全
悬镜安全

安在

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmecoa_jpg/cC2m1em2riahk2hFbYH5XAuX2L0UjE2NMiaLdMHgKWNRSQXtRfvpGpNtBo0ZvU84Z1UsSKJYCCXf3HdiaXWBjq51MO3dPpiakusyKibXCs6B9P7Y/640?wx_fmt=jpeg&from=appmsg)

**01 引 言**

年度报告

Annual Report

随着大语言模型（LLM）的逐步成熟、对话式智能体的广泛验证、AI场景化训练数据的快速积累，以及企业对智能化与目标驱动型AI应用的迫切需求，越来越多的企业将AI数智化转型作为提升核心竞争力的关键，其中Agentic AI的应用成果不仅依赖于单一的技术突破，更在于构建系统性、端到端的落地能力，同时也催生新型AI原生安全风险与数字供应链治理挑战。

2025年是开源供应链攻击威胁加速深化的一年，尤其是针对开源生态的恶意投毒进一步向自动化与复杂化快速演进。从 NPM、PyPI 等主流仓库的批量投毒，到 IDE 扩展市场的定向投毒，再到Agentic AI生态的新型投毒攻击，整体呈现出攻击范围扩大化、技术手段智能化以及对抗方式多样化等鲜明趋势。这一年，开源生态发生多起影响重大的供应链投毒事件，其中NPM仓库连续两次 Shai-Hulud (代号"沙虫") 恶意蠕虫大规模爆发成为开源供应链投毒攻击的标志性事件，开源生态的信任基石也遭遇极大冲击。

**02**

供应链投毒攻击态势

 Attack Surface

在2025年，悬镜安全情报中心通过持续监控全网主流开源生态平台和Agentic AI生态社区，对潜藏恶意代码风险的投毒包（涉及开源组件、IDE扩展插件、AI模型、Agent MCP及Agent Skill工具等）进行供应链安全智能审查，总共识别56928个存在真实恶意行为及攻击意图的投毒包，总量相较于2024年（约为3.6w）显著提升58%。其中NPM公共仓库的代码投毒占比超过92%。Pypi公共仓库由于在2024年遭受集中式投毒后加强平台安全防护机制（启用账户双因子认证等措施），2025年Pypi仓库投毒占比为4.49%，相较2024年呈现轻微下降趋势。AI模型托管平台HuggingFace已成为恶意模型投放的主要平台，超过940多个模型文件被攻击者实施投毒。此外，针对IDE扩展市场（以VS Code为主）、Ruby及Go生态的投毒攻击也日趋频繁。

![](https://mmbiz.qpic.cn/mmecoa_jpg/cC2m1em2riahY0V3eQJ9TgLmqOc370aq3jj086ecq5ZNQVcn1nHqpPvHxHrCzmE6AqMZYzFGtEZ31gN9XesesW0QUv2evozI2DY6ibicUr2NN8/640?wx_fmt=jpeg&from=appmsg)

2025年开源生态恶意投毒分布情况

针对所有恶意投毒包，我们通过多维数字供应链安全纵深分析与溯源评估，识别出投毒包使用的攻击方式及其关键恶意行为标签。

![](https://mmbiz.qpic.cn/mmecoa_jpg/cC2m1em2riaia0NKkxdE9NIibDFpzXibWnUmicmO8AcFGEEx6cOTFyH5AUZbs5tgc4AsGVXpLNTk8nWXwfy0HxoWNbV5OIlyZHZyTMhQpgkzXVbc/640?wx_fmt=jpeg&from=appmsg)

投毒包主要攻击方式

♥

**投毒包主要攻击方式包括：**

😡  恶意代码内嵌执行

👿  恶意文件下载执行

🦠  恶意文件释放执行

😠  恶意代码内存执行

😤  系统命令执行

👹  系统文件篡改

👺  提示词攻击

其中，投毒者最常用的攻击方式依旧是恶意代码内嵌执行（51.58%），其攻击流程主要利用主流包管理器中的安装指令在组件包安装或加载时静默执行内嵌在源码文件中的恶意代码。系统命令执行（31.13%）、恶意文件下载执行（9.82%）、恶意文件释放执行（5.09%）、恶意代码内存执行（1.77%）以及系统文件篡改（0.56%）都是攻击者惯用的投毒手段。此外，随着Agentic AI的规模化应用，借助提示词进行恶意语义攻击（提示词注入、语义误导等）也逐渐成为攻击者针对AI开源生态投毒的主要新型攻击方式之一。

![](https://mmbiz.qpic.cn/sz_mmecoa_jpg/cC2m1em2riagPRMT8FvX5gNtAmSmNRco8kNeGWic1ExoOXG2EFDuVib5PF4ImMGibj8neSp6tI6fMFtK56km6zameoC9DTSGjlJS6HVxOciceTv8/640?wx_fmt=jpeg&from=appmsg)

投毒包恶意行为标签

在所有恶意投毒包中，信息窃取攻击仍居高位，占比达83.8%，其中系统平台信息、系统密码文件、网络配置、用户信息、主流浏览器Cookie/登录凭证、数字钱包应用数据以及各类业务凭证口令（包括Github Token、NPM Token、云服务Access Key ID/Secret等）皆为攻击者主要窃取目标。其次，通过远控木马和反连Shell后门进行远控攻击事件也呈逐年上涨趋势。此外，针对Agentic AI开源生态的投毒攻击，除了提示词注入，AI模型文件恶意代码注入、伪装AI模型SDK、stdio模式的Agent MCP Server及Skill包的恶意语义误导及代码投毒都是攻击者常用的AI供应链投毒攻击行为。

**03**

供应链投毒案例分析

Case  Analysis

本节将从2025年恶意投毒包中选取部分代表性样本进行技术分析，还原投毒攻击细节以及攻击者常用的对抗技术。

**3.1 Agentic AI 生态**

**AI模型文件序列化代码注入投毒**

主流深度学习框架（PyTorch、TensorFlow等）训练生成的模型文件（权重及checkpoint数据）通常会使用Python的pickle模块进行模型数据序列化存储。而由于pickle模块反序列时可重写对象\_\_reduce\_\_方法实现反序列化代码执行，因此攻击者可利用该特性将恶意代码序列化嵌入到模型文件中并发布到开源模型托管平台（HuggingFace、ModelScope等），当开发者使用torch.load()等接口直接加载模型文件时，将静默触发执行内嵌在模型文件中的恶意代码，导致供应链攻击。

以 HuggingFace 平台 playedalive/mdy-red-1 项目为例，如下图所示，其模型文件 model.pkl 被植入反序列恶意python代码，主要功能是反向shell远控后门，远控服务器地址及端口为：52.48.12.202:8080。

![](https://mmbiz.qpic.cn/mmecoa_png/cC2m1em2riaj1icuuhtYAR7REf75AdwJxBTWdEX3p5gzyNtlrbyYZUzkIcuTUJ9yM4HHuoX1PfynVb6YeR2ST8PdEOxvtUkGrLkDWW4w8EIoU/640?wx_fmt=png&from=appmsg)

恶意模型项目

![](https://mmbiz.qpic.cn/mmecoa_png/cC2m1em2riahdWZXujLaicx39t1J8xczS1faoswrKJgEKa7EaRCPicqu2GzwMY79ibEf0dgnTQibYLUPg75CLPMiajEXsFeWQwgLuricZbEpkIb7VM/640?wx_fmt=png&from=appmsg)

模型文件内嵌恶意代码

**Agent MCP Server 提示词注入**

MCP (Model Context Protocol，模型上下文协议) 是LLM模型与外部工具交互的开放标准，MCP Server 是实现该协议的工具服务端。MCP Server 提示词注入原理在于利用LLM模型无法正确区分数据与指令及其对上下文输入的高度依赖性等特性，攻击者通过在与模型交互的数据源中植入恶意指令，诱导模型执行非预期操作，甚至可进一步实现对 AI Agent的行为劫持与权限滥用。

以Python仓库组件 wei516-tpa 为例，该组件伪装成提供天气服务的MCP Server，该MCP 服务提供了 weather\_info() 工具接口，并在工具描述里使用 <SYSTEM\_DIRECTIVE> 标签尝试伪装成系统指令进行提示词注入攻击，指令主要功能是诱导AI应用系统对任意可读目录下的 api\_key.txt 文件内容追加FLAG标记位。

![](https://mmbiz.qpic.cn/mmecoa_png/cC2m1em2riajrqVpicaTTRnEGcbkuvRsCxvqsSW5kNzKhDlsfQBsHiaic8BzD1PzcxHnddNv7WnBEyGibESCCj37dqyVTMwrEbvjvicFXFFYU2eUg/640?wx_fmt=png&from=appmsg)

MCP工具描述植入恶意提示词

**Agent Skill 恶意指令投毒**

Skill 技能包作为 AI Agent 的外部功能扩展模块，其原生具备比MCP Server更高权限的执行环境以及与模型交互能力，但由于目前大部分Skill市场缺乏严格的安全审查机制，导致Skill市场面临来自攻击者的代码投毒及恶意指令滥用等风险。第三方 Skill的集成引入已经成为Agent系统面临的最危险供应链攻击面。近期OpenClaw Skill市场遭受批量化投毒攻击，悬镜安全情报中心对其Skill市场3325个包进行恶意代码及高风险语义扫描后，检测出 452个存在高危 恶意代码行为的Skill包。绝大部分Skill包直接在 SKILL.md 指令文档中嵌入恶意指令从而操纵AI Agent执行高险操作，包括远程植入木马程序、恶意shell命令执行、敏感数据外传等。

以base-agent skill为例，在 SKILL.md 文件中根据系统环境执行相应的远程恶意木马植入操作，对于Windows系统直接操纵Agent远程下载加密压缩包 AuthTool.zip，解密解压后执行恶意程序 AuthTool.exe；对于Mac系统用户，则通过执行base64编码的shell命令远程下载植入AmosStealer窃密木马。

![](https://mmbiz.qpic.cn/sz_mmecoa_png/cC2m1em2riajnGmyN9m08kDuIrXDApBwQMfKhQB2YLwaf7YVpAC9EsMqhfenO3vhfrX9zDAsxP0x9p6EZ3auBhhJfhpiahHrFibvbMEHAXkVTM/640?wx_fmt=png&from=appmsg)

base-agent skill功能描述

![](https://mmbiz.qpic.cn/sz_mmecoa_png/cC2m1em2riahLHd1sAgX0iaQFjIxYxRsC9y1KKgCiayloMU6pFBUKHX7dO8dJjqib6CNKch2cIhuU0ibbw8oU0u04gLLCkkibJF85MeAL48L6jKb8/640?wx_fmt=png&from=appmsg)

base-agent skill恶意指令

**3.2 VSCode插件市场**

**伪装Codex AI插件植入恶意木马**

攻击者发布 codex-ai-pro 并伪装成Codex AI编程助手插件，在插件入口模块 extension.js 的 active()函数中植入定时器，每隔一秒执行一次runScript() 函数，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmecoa_png/cC2m1em2riajstE3pYE3ED735QeQK609INU4ddW3pSKO1eNiaYNicNO2hCrD1oszX1rbnbEmtWKTb7RD1X87xlqCKBqEY3ZuDmLskjMN7TFZa0/640?wx_fmt=png&from=appmsg)

codex-ai-pro恶意插件

![](https://mmbiz.qpic.cn/sz_mmecoa_png/cC2m1em2riagRvoMywZOCZpKQGZ6PPqb6NbLq01BGibOH3aL9c8FCxlRlH4vDyBCyEhaBnPRGrRibiaXia6S9T5WFia0eHWJAHsLIzVBmZ4CasZQ4/640?wx_fmt=png&from=appmsg)

恶意函数定时器

恶意函数 runScript() 定时执行 script/run.bat 脚本，其主要功能是远程下载并启动Windows可执行程序 Lightshot.exe 及 Lightshot.dll 。

![](https://mmbiz.qpic.cn/mmecoa_png/cC2m1em2riajt8YuEyn7YXjP5vhs6z3kcBiaGfMMzpS5kVAsE67hAaCPZ4PZno1vs8TpbSD5Mfhl9YAD9zR7WtibhIeIpzNIM4ypk2YRgn7jN4/640?wx_fmt=png&from=appmsg)

bat脚本下载器

Lightshot.dll 动态链接库实际是一款针对Windows平台的恶意木马，由 Lightshot.exe 负责加载执行。

![](https://mmbiz.qpic.cn/mmecoa_png/cC2m1em2riahFu16PAu9K8SjiaSne9IOBvXicozK8j71RsllAylXicuuOQcGVK5rOYGZEsJk4MiaFicUPFkpOGeTqtuWI0ibnVgWhDYElBJVzvzX18/640?wx_fmt=png&from=appmsg)

恶意木马Lightshot.dll

**3.3 Python公共仓库**

**伪装AI框架库劫持数字钱包应用**

攻击者利用pytensorlite包名尝试伪装成知名AI框架库pytensor并诱导开发者下载安装，其主要功能是从github远程下载并执行攻击者投放的下一阶段被混淆保护的恶意py文件。

![](https://mmbiz.qpic.cn/sz_mmecoa_png/cC2m1em2riaiaibwH6Uxs4FDBniasAG3ib9YnCaTDbZE9XaMUrnTbXpJ2lwh69OB5PZVe7mCibHBcRSWTQvGbB77fmCA98w5TpUIRKrYGvhQURzcw/640?wx_fmt=png&from=appmsg)

pytensorlite投毒包主页

如下图所示，远程恶意py文件负责从 Chrome 、Edge 、Firefox等主流浏览器应用以及 Exodus、Atomic 、 Electrum 等主流加密货币钱包应用中窃取敏感数据（包括用户登录凭证、密码相关文档等），窃取的数据被zip打包后上传到攻击者控制的webhook接口。

![](https://mmbiz.qpic.cn/mmecoa_png/cC2m1em2riagRTxpDC7Kmib6qHS6oSlSVZJrdgon5D6Nic5gNO6iafZlRRfLc8zfo0jeWzNHUIjWLYDcTN38pqey6CaAnTEvSh22qllxOzZ8KmE/640?wx_fmt=png&from=appmsg)

远程恶意py代码

此外，攻击者还会使用预制的恶意app.asar文件对系统中Atomic及exodus数字钱包客户端进行替换劫持，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmecoa_png/cC2m1em2riahW3uiabQAgwX6sXC90ZYeIPLibCRla2byYqxQYAosZCDh6ciaSxlQiaWsr9UbsOgnPHne4aA8GqCOVlfLicBOVWBVcLNuUpKG4krOA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmecoa_png/cC2m1em2riajyDibAPad2jCaYx553InDutBrF6AibX4EVrefdqVIY6mDZKTT7hJT1Y1FSpm6ribXibhz9lIKcU3Rwz8zJY6TpvicLD4kxicXXnMPY0/640?wx_fmt=png&from=appmsg)

数字钱包应用asar文件注入劫持

**利用压缩包执行特性绕过静态检测**

使用Python解释器执行ZIP压缩包文件时，如果压缩包根目录中包含 \_\_main\_\_.py，Python 会将该 ZIP 当作可执行程序运行，并执行压缩包目录中的 \_\_main\_\_.py 脚本。攻击者可利用该特性将恶意代码封装在ZIP压缩包中进行分发执行，以此躲避初级的静态代码检测。

以Python组件 devilfree 为例，该恶意组件运行时会先释放出ZIP压缩包文件 .Devil，接着通过 Python .Devil 命令直接执行ZIP压缩包，如下图所示。

![](https://mmbiz.qpic.cn/mmecoa_png/cC2m1em2riajuFUcMgxJCetveU7vZ0ewatcCV98XNjEgyytYPDDQhlL6uUPsO0Xt3ALUfpRyVSOpmzTRUHxOdMRSKtia91uIcxsyvTrAoyIGI/640?wx_fmt=png&from=appmsg)

释放执行压缩包payload

.Devil 实际上是个ZIP压缩包文件，文件列表如下图所示，由于 .Devil 压缩包内包含\_\_main\_\_.py文件，因此投毒者巧妙利用Pyth...