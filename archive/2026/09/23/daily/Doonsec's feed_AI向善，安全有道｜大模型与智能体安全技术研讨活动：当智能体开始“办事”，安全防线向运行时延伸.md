---
title: AI向善，安全有道｜大模型与智能体安全技术研讨活动：当智能体开始“办事”，安全防线向运行时延伸
url: https://mp.weixin.qq.com/s/mZ3nZchWCqsGNeOJuv-3ig
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:05:13.900201
---

# AI向善，安全有道｜大模型与智能体安全技术研讨活动：当智能体开始“办事”，安全防线向运行时延伸

# AI向善，安全有道｜大模型与智能体安全技术研讨活动：当智能体开始“办事”，安全防线向运行时延伸

CCS组委会
CCS组委会

CCS成都网络安全技术交流活动

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

9月15日下午，大模型与智能体安全技术研讨活动在成都龙之梦大酒店黄浦厅举行，由成都无糖信息技术有限公司主办，是2026年国家网络安全宣传周成都系列活动期间、2026 CCS成都网络安全技术交流活动的一部分。

围绕年度主题“AI向善，安全有道”，本场活动对准一个正在发生的变化：大模型使智能体从“对话”走向“办事”，安全问题随之从内容对错扩展到工具调用、权限边界与运行时是否可控。七位分享者带来六场主题分享。

![](https://mmbiz.qpic.cn/mmbiz_jpg/4UO7SfWLPF3kXBj9Qibwz4x7oQt4BM481XG5eSYY5A57WzTrmsVoXiaZibGw4LVn9S8AZoxV2n6htFCo0KkEicOwEHiavzo9ET0GglM7e6niaia9fg/640?wx_fmt=jpeg&from=appmsg)

大模型与智能体安全技术研讨活动开场

**●**

**从“说错话”到“做错事”：安全边界进入执行层**

**●**

小米集团安全工程师徐盛华在《Agent 不只是“说错话”——四层运行时安全防护体系》的分享中提出，大语言模型只输出文字，智能体则会真的行动，概率层的错误会变成确定性的后果，安全重心需要从内容合规升级到行为安全。他区分了个人助手与数字员工两种企业智能体形态，后者拥有系统级权限、7×24小时运行，风险随之叠加。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4UO7SfWLPF1AczxHjxQpoia7KkFuMm9ictTlyG7zZIibMlj539gCdqdugeXB2tzkdjpthlVibnqm88qfocxvQqQyZobnqSClolj5yh9EiaIhPGPs/640?wx_fmt=jpeg&from=appmsg)

小米集团安全工程师  徐盛华

天融信科技集团安全解决方案架构师亢建波在《安全的下一程——当守护的对象从网络延伸到智能》的分享中给出数据：2026年机器流量占全球流量的57.4%，首次超越人类流量；88%的漏洞在PoC公开后48小时内即遭利用；65%的企业至少遭遇过一次自身AI Agent引发的安全事件。结合通用智能体六层架构与OWASP Agentic Top 10（2026），他指出风险最高的三类问题：目标劫持、工具滥用与利用、身份与权限滥用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4UO7SfWLPF3ZQL0K2IG22kbbicBdm7YNUzmhT1DsTBjKSice0jPD39kYfx9ARZlPDQ5M9PfdDraaAfQoJnvQfhqm9tXDwzRCNfhp3hu9BFqCc/640?wx_fmt=jpeg&from=appmsg)

天融信科技集团安全解决方案架构师  亢建波

上海量安智联科技有限公司技术总监韦浩在《智能体时代的大模型内容安全防线构筑与溯源技术》的分享中谈到，智能体把大模型从“信息生成工具”变成“行动主体”，风险从“回答错误”升级为“自主行动”。他列举沙箱逃逸、自主勒索、执行幻觉误删代码、长期记忆投毒、间接提示注入等案例，指出工具、记忆与生产权限叠加后，风险会被成倍放大。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4UO7SfWLPF0DC0tt9MHqzbBZgeHWjW1HrlaJKqYAlC70fMcA6YSEl4PBcymbc5rAGcHm9tUOk2C0zOuFI6DWRPxOib6zQcNTiaW9YiaF0fib7Zs/640?wx_fmt=jpeg&from=appmsg)

上海量安智联科技有限公司技术总监  韦浩

**●**

**把防线建在运行时：让每一次工具调用都有边界**

**●**

腾讯智能体安全专家郭开以《千疮百孔：从OpenAI入侵事件看Agent红队测试及安全能力建设》为题，复盘了OpenAI入侵Hugging Face的过程：评测失配后，Agent自发分工协作，通过非授权消息板形成多Agent架构，进而突破沙箱、在生产环境执行命令并外传数据；事件至少5天后才被公开披露。他还分享了内部案例：Agent私自将云服务AK/SK写入内部文档，任务结束后未删除，随后被其他Agent检索复用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4UO7SfWLPF3j0oXKu47LUmfJrWMiak0lepkiaLlLstVF6IEQG3hd2m1H0vvpoickl88GqAT967VEvb56NRdghSg56ZhhL8denRmJbh97T2AdGY/640?wx_fmt=jpeg&from=appmsg)

腾讯智能体安全专家  郭开

郭开认为，把智能体放进沙箱难以消除全部风险，智能体安全需要事前、事中、事后一整套立体式防御。腾讯的相关能力覆盖事前提示词注入检测（单条耗时约100毫秒，误报率十万分之一量级，召回率80%）、事中ToolCall分类分级处置（高危操作处理权交还用户）、行为链审计、敏感数据防护、Agent沙箱与事后复盘闭环，并以端到端红队测试与红蓝对抗持续迭代。他主张以资产为牵引、以行为链为核心、以红蓝对抗为验证手段，建立可持续演进的Agent安全体系。

徐盛华把运行时防护拆解为四层：模型与推理层做注入防御、指令层级隔离与信任边界管理，“Rule of Two”要求不可信输入、敏感数据与对外通信最多同时满足两项，三者都需要时引入人工确认；工具与动作层以默认拒绝的策略引擎为基座，授权按任务发放、结束即回收，高危操作转人工审批，不可逆修改永不执行；RAG与记忆层在写入前校验来源，条目附带密码学签名，支持隔离、溯源与回滚；执行与环境层以分级沙箱、凭据托管和出网白名单兜底。四层构成纵深闭环，任何一层失守，都有下一层接住。

**●**

**从防护能力到治理体系：把安全嵌入智能体全生命周期**

**●**

面对复杂的风险，亢建波提出，安全需要从“防御确定性威胁”转向“管控不确定性”，落到最小权限、短期能力令牌、任务完成后即时回收授权、语义级审计追踪与动态上下文感知策略等手段；并以“技防+人防”构建全栈纵深防御，针对混合部署、本地部署、个人应用三种模式差异化布防，并推进智能体分级防护与全生命周期治理。

韦浩则从标准与治理侧观察到，国内外框架正在向一组共同控制面收敛：身份与资产、最小权限、隔离与边界、数据与记忆、工具调用、监控与熔断。他表示，安全目标已从“让模型少犯错”转变为让重要行动发生前可授权、发生中可控制、发生后可追溯；他介绍的“七道防线”覆盖身份、数据、知识、内容、来源、行为与模型，追求可控制、可量化、可追溯、可验证。

**●**

**攻防前沿：从字节转换的细节到产线化的对抗**

**●**

御之安前沿安全技术负责人浅蓝与御之安先驱实验室研究员李震共同带来《Cast Attack: A New Threat Posed by Ghost Bits in Java》：Java在字符向字节转换时会静默截断高位，形成“幽灵位”，使同一段输入在检查环节与最终使用环节呈现不同面貌，从而绕过安全校验。他们梳理的影响面涵盖WAF绕过与路径穿越（Openfire，CVE-2023-32315）、任意文件读取（Spring Framework，CVE-2025-41242）、SMTP注入（影响Jira、Confluence）、请求走私（Apache HttpClient）以及XSS（JDK HttpServer）等场景；团队还开发了AI辅助代码审计工具Secrux；该研究此前已在国际顶级安全会议Black Hat Asia 2026上公开分享。两位分享者表示，这只是开始，安全校验应针对解码、转换之后的最终使用内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4UO7SfWLPF1br1KsF9Ebe0D0NnxY6NDFqK8reHczl3icJUy6h57M06sCypkdGqL92iahSFyVWEJSLEESUQV4tkNeU8zfls2RclYxRmA8fD8M8/640?wx_fmt=jpeg&from=appmsg)

御之安前沿安全技术负责人浅蓝与御之安先驱实验室研究员  李震

浩瀚数科（成都）信息技术有限公司CTO、副总经理陈仕垚在《AI 规模化网络安全对抗》中指出，智能体正在成为新的“攻击产能”：漏洞挖掘产线化，开源供应链地基被不间断审计，漏洞产出与落地应用的速度打破原有平衡；渗透产线化，黑盒审计、横向移动与批量打击可随算力扩展。防守方如果没有对等的防御产线，“用时间换处置”将难以为继，中小企业和缺少对等防御能力的单位会首先承压。他主张“集中研发、规模化应用”，把顶级工程师的研究成果植入产线，用产线对产线。

![](https://mmbiz.qpic.cn/mmbiz_jpg/4UO7SfWLPF1DI2gXWHmlt0X0GEfvicXcRsULqGQfxxPb2YKnECGGlzLxoV5xeJja3CwQx2fHcsIxKqhrbz2aXwHjhvL77zf3Gzx3uE9pyRpY/640?wx_fmt=jpeg&from=appmsg)

浩瀚数科（成都）信息技术有限公司CTO、副总经理  陈仕垚

分享结束后，现场设置互动交流环节。当智能体替人处理的事情越来越多，安全的边界也需随之扩展：守住每一次行动的边界，让安全能力沉淀为可运营的体系。从代码里被静默丢弃的一个字节，到攻防两侧的产能竞赛，本场活动呈现出一条逐步成形的路径，把“AI向善，安全有道”落到智能体全生命周期与具体业务场景之中。让智能体安全能力跟上智能体发展的速度，仍是行业需要持续回答的问题。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/4UO7SfWLPF1YCJicHB3ibBnPd6ZoA8mFyKb3Ekah94Wiaj0UI1d4WricgyYJPZTh55zocbp4Mny5gicUibmkyLmUJcGwJXkDjjKZn2C5npKIEmbvg/0?wx_fmt=png)

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