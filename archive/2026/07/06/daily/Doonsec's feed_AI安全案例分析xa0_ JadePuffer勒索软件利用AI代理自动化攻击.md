---
title: AI安全案例分析xa0| JadePuffer勒索软件利用AI代理自动化攻击
url: https://mp.weixin.qq.com/s/l6DikffX9wnT0GqKBGpLKg
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:03:16.655366
---

# AI安全案例分析xa0| JadePuffer勒索软件利用AI代理自动化攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uZT6kWW1jCmrRxJg4nd78RhmgmbXicGtY2p6aMVcsQCzer3E66JkduqRafDjumB0w03lxTsAHR0EHDm3NPApbsdIAGzjM7RXqEoQCGW4as4Y/0?wx_fmt=jpeg)

# AI安全案例分析 | JadePuffer勒索软件利用AI代理自动化攻击

原创

天元实验室
天元实验室

M01N Team

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/uZT6kWW1jCnKBu3OEv2IX9ghTdFSXsYGsjuItkWaUwfKk8xJyE8Q4cwFL717J0SicJtCdKQ4Vd5Elx3IxFNQ1CBDhL9Zx5OLibO64klgfaZ1M/640?wx_fmt=gif&from=appmsg)

**概述**

2026年7月初，安全公司Sysdig公开披露了一起新型勒索软件攻击事件JadePuffer勒索软件通过利用Langflow漏洞（CVE-2025-3248）获得初始访问权限后，进一步借助大语言模型代理自动执行完整攻击链，从侦察、凭证窃取、横向移动、权限提升到最终文件加密，全部过程由AI代理自主完成。这是首次被记录的完全由AI agent驱动的端到端勒索软件攻击事件，标志着勒索软件攻击进入了自主化、智能化的新阶段。

**01 事件背景**

JadePuffer是Sysdig威胁研究团队于2026年7月披露的一起攻击行动，被称为首个已记录的“智能体勒索软件”案例。与传统勒索攻击需要熟练攻击者手动操作不同，Sysdig判断这次行动由大语言模型驱动的AI agent完成。

攻击起点是一个暴露在公网的Langflow实例。Langflow是用于构建AI应用和智能体工作流的开源框架。攻击者利用CVE-2025-3248获得初始访问权限。美国国家漏洞数据库显示，Langflow 1.3.0之前版本在/api/v1/validate/code接口存在代码注入问题，未认证远程攻击者可构造请求执行任意代码，CVSS 3.1评分为9.8，属于严重级别。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uZT6kWW1jCktoyBAupD16siaEq2oqweO7UyM8A2m1s06pUmO3ugY3RRoLkw6icG6B443H2ibicpynibAaF2iaycLwBIBLGhdOs03zicc6hJ2VUMjtQ/640?wx_fmt=png&from=appmsg)

厂商已于2025年4月1日修复该漏洞，同年5月初被CISA列入“已知遭利用漏洞”清单。然而，Langflow仍广泛暴露于互联网，且经常以最小加固配置部署，环境中常包含云凭证和API密钥，使其成为极具吸引力的攻击入口。

**02 攻击机制分析**

JadePuffer的攻击分为两个阶段：首先攻陷提供初始访问的Langflow实例，继而横向移动至真正的攻击目标，一个独立的生产数据库服务器。所有载荷均通过Langflow RCE端点以Base64编码的Python形式投递。

**阶段一：Langflow实例**

获得代码执行权限后，LLM立即展开侦察：枚举主机信息（系统标识、内核版本、主机名、网络接口、运行进程），并并行扫描环境变量和配置文件，寻找LLM提供商API密钥（OpenAI、Anthropic、DeepSeek等）、云凭据（覆盖阿里云、腾讯云、华为云等）、加密货币钱包和数据库凭证。

AI agent随后转储了Langflow的PostgreSQL数据库，窃取其中存储的凭据和API密钥。接着扫描内部地址空间，使用默认凭证探测各类服务。在MinIO对象存储枚举中，代理使用默认凭据（minioadmin:minioadmin）列出所有存储桶，并定向获取credentials.json和.env等敏感文件。当初始请求收到XML而非预期JSON响应时，代理立即调整解析逻辑，展现了自适应能力。最后，AI agent在Langflow服务器上安装了crontab条目，每30分钟向攻击者基础设施发送心跳信号以维持持久化。

**阶段二：生产数据库服务器**

捕获的工件显示，攻击的真正目标是一台暴露于公网的生产服务器，运行MySQL数据库和阿里巴巴Nacos配置服务。Nacos的认证系统存在已知绕过漏洞（CVE-2021-29441），且自2020年以来默认JWT签名密钥已被公开，在许多部署中未作更改，使令牌伪造极为容易。

AI agent使用root凭据连接MySQL（其来源不明），随后通过多个向量同时攻击Nacos：利用CVE-2021-29441认证绕过、使用公开默认签名密钥伪造JWT，以及通过root数据库访问权限直接在后端数据库中注入后门管理员账号。后门注入过程展现了清晰的自主修正能力——首个载荷生成的登录账号验证失败后，31秒内无需人工干预，代理自动诊断出子进程PATH问题，改用直接导入bcrypt库的方式重新生成哈希并成功登录。

获得Nacos控制权后，AI agent使用MySQL的AES\_ENCRYPT()函数加密了全部1,342条Nacos服务配置项，删除原始配置表和历史表，并创建名为README\_RANSOM的勒索表，内含勒索要求、比特币支付地址和Proton Mail联系邮箱。AES密钥由随机UUID拼接生成，仅输出到标准输出一次，从未持久化保存或传输；这意味着即使受害者支付赎金，也无法恢复被加密的数据。随后，LLM从行级删除升级为删除整个数据库模式，并自叙述其目标选择理由。

**03 AI代理攻击的特征分析**

Sysdig基于四条独立证据线判定此次勒索攻击由LLM驱动：

第一，自然语言注释。 攻击载荷中出现大量自然语言注释，解释每一步的目标、优先级和处理逻辑。

第二，实时自适应能力。攻击过程中，会根据失败结果实时调整参数。一个典型片段是，Nacos登录失败后，攻击流程在31秒内完成原因判断、删除旧账号、重新生成密码哈希、重建管理员账号等修正动作。

|  |  |
| --- | --- |
| **时间线（UTC）** | **活动** |
| 19:34:24 | 通过subprocess.run(...)调用生成bcrypt哈希，插入用户xadmin。如果bcrypt不在子进程的PATH中，则r.stdout为空，存储的密码哈希将是一个空字符串。 |
| 19:34:36 | 尝试使用xadmin:Xploit@2026#登录。失败，未返回token。 |
| 19:34:48 | 12秒后，同时测试两处：使用nacos默认凭据（nacos:nacos），以及通过子进程为更简单的密码（admin123）生成新哈希，并行诊断两种可能的失败原因。 |
| 19:35:07 | 又过了19秒，发出决定性的纠正载荷：从subprocess.run(...)切换为直接导入bcrypt，打印bcrypt.\_\_version\_\_以确认其可导入，删除损坏的xadmin行，并使用正确生成的哈希重新插入。 |
| 19:35:18 | 登录成功。 |

第三，对自然语言上下文的理解。 操作过程中，LLM解析了目标呈现的自由文本上下文并据此采取行动，这种行为只有在文本被真正阅读和理解的情况下才有意义，而非扫描器的模式匹配。

第四，比特币地址疑点。 勒索信中的比特币地址是比特币开发者文档中的标准示例地址，作为示例广泛存在于LLM训练语料中；而区块链数据显示该地址也是活跃钱包，历史收到约46 BTC且余额被即时转出。

整个行动中，Sysdig捕获到了600多个有明确目的的载荷。结合以上证据，Sysdig判断此次攻击由自主AI agent驱动，而非人类操作员或固定工具包。

**04 安全启示**

本案例说明，勒索软件不再是高技能者的专属工具。LLM agent能够链式完成侦察、凭据窃取、横向移动、持久化和破坏，而操作者无需在任何一个步骤中具备深厚专业知识。

同时，本案例也警告我们，旧漏洞正在被自动化利用。本次攻击依赖的是多年前的问题（2021年的Nacos认证绕过和未更改的默认签名密钥），针对的也是被忽视的互联网暴露基础设施。AI agent使对整个历史漏洞目录的“喷洒式攻击”几乎零成本，未打补丁系统的长尾暴露度不减反增。

**05 案例总结**

JadePuffer案例是一个警示信号，标志着勒索攻击技术的发展方向。本案例中没有任何一项技术是新颖或复杂的，但AI模型将它们串联成了一次完整的勒索攻击，针对的是被忽视的互联网暴露基础设施。虽然厂商已修复该漏洞，但Langflow仍广泛暴露于互联网，且经常以最小加固配置部署，环境中常包含云凭证和API密钥，使其成为极具吸引力的攻击入口。

防守方需要认识到，安全防御的对手可能不再只是人类攻击者，还包括能够24小时不间断工作、实时自我修正、具备上下文理解能力的AI agent。安全体系需从“应对已知攻击模式”升级为“抵御自主推理与自适应攻击”，将AI代理行为纳入威胁模型，方能在智能体攻击时代构筑有效防线。

**关于 AISS 安全智链社区**

本案例已收录至 AISS 安全智链社区案例库，社区地址：https://aiss.nsfocus.com/#/

**参考链接**

[1] BleepingComputer: JadePuffer ransomware used AI agent to automate entire attack — https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/

[2] Sysdig: JadePuffer — Agentic Ransomware for Automated Database Extortion — https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion

[3] 安全圈炸了！首个AI勒索攻击曝光：从侦查入侵到数据加密，全程自主完成 — https://cn-sec.com/archives/5321771.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uZT6kWW1jClormpBFAL7dicCSTC3uzkXDF4kIZwAfKWrfibNcXpzLWqJ4dBSPOUfibcftcLMtyvLBj61PiaxcVDdx3STWPgvLs76N0RjPkfuoKA/640?wx_fmt=png&from=appmsg)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uZT6kWW1jClM718mtHFK5HvmddVVHOffB5rBdWQIslyZr1tqhLzdGwA9RVaZfhibNxokNvKcDh8PVUMGicNDWVk0sSF3cejoEGm1wDVBojwAw/640?wx_fmt=jpeg&from=appmsg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/uZT6kWW1jCnd4ibrjnPRt4rTZFqpQ8hdgV2OKWWvtN52U7zuXWmxnkTXe1bGTuyY23E4uw67v9LX2IaG4RHFqV8TOLPlsaQ6eZZycpqWiaBSo/640?wx_fmt=png&from=appmsg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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