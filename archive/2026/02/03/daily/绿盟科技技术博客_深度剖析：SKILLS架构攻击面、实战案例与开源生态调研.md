---
title: 深度剖析：SKILLS架构攻击面、实战案例与开源生态调研
url: https://blog.nsfocus.net/%e6%b7%b1%e5%ba%a6%e5%89%96%e6%9e%90%ef%bc%9askills%e6%9e%b6%e6%9e%84%e6%94%bb%e5%87%bb%e9%9d%a2%e3%80%81%e5%ae%9e%e6%88%98%e6%a1%88%e4%be%8b%e4%b8%8e%e5%bc%80%e6%ba%90%e7%94%9f%e6%80%81%e8%b0%83/
source: 绿盟科技技术博客
date: 2026-02-03
fetch_date: 2026-02-04T04:07:05.929877
---

# 深度剖析：SKILLS架构攻击面、实战案例与开源生态调研

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 深度剖析：SKILLS架构攻击面、实战案例与开源生态调研

### 深度剖析：SKILLS架构攻击面、实战案例与开源生态调研

[2026-02-03](https://blog.nsfocus.net/%E6%B7%B1%E5%BA%A6%E5%89%96%E6%9E%90%EF%BC%9Askills%E6%9E%B6%E6%9E%84%E6%94%BB%E5%87%BB%E9%9D%A2%E3%80%81%E5%AE%9E%E6%88%98%E6%A1%88%E4%BE%8B%E4%B8%8E%E5%BC%80%E6%BA%90%E7%94%9F%E6%80%81%E8%B0%83/ "深度剖析：SKILLS架构攻击面、实战案例与开源生态调研")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 70

### **00 背景**

随着大模型与智能体从对话向任务执行扩展，能力的封装、复用与编排成为关键问题。SKILLS 作为能力抽象机制，将推理逻辑、工具调用与执行流程封装为可复用的技能单元，使模型在执行复杂任务时实现稳定、一致且可管理的操作。即便在 MCP 等机制存在的情况下，SKILLS 仍不可替代，MCP负责模型对外部工具的调用管理，而SKILLS的核心是通过元工具驱动的渐进式、按需提示词注入机制，实现低常驻上下文开销下的瞬时专家级能力加载。随着生态的快速发展，SKILLS 的数量与复杂度呈现爆发式增长，显示出其在自动化流程和能力管理中的核心价值。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/1-300x134.png)

100k+的SKILLS数量与指数级增长速度

SKILLS 最初由 Claude 团队在 Claude Code 中以私有形式开发，旨在扩展模型能力与任务逻辑；随着大模型生态的持续演进，它逐步从平台内部应用拓展至更广泛的 AI IDE 与自动化工作流场景。如今，SKILLS 的数量已超过 10 万，且仍保持指数级增长。能力封装不仅提升执行效率，也形成新的安全边界，对权限管理与执行控制提出挑战。SKILLS 已成为能力复用、任务执行与安全管理的核心模块，其潜在攻击面和生态价值值得系统关注。本文将从架构设计、攻击实践、生态现状三个层面，深入剖析SKILLS安全攻击面的构成与潜在威胁，为相关方提供系统性的安全参考。

### **01 SKILLS攻击面分析，核心架构中隐藏的天然风险**

**SKILLS架构剖析**

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/2-300x132.png)

在Agent Skills的架构中，每个SKILL以文件系统上的独立目录形式存在。根目录下的SKILL.md文件是技能的说明书，通过前置元数据定义技能的功能描述与适用场景。这个文件不仅是静态元数据的载体，更包含完整的技能指令集，包括分步骤的操作指南、输入输出示例及案例说明，形成可被智能体直接解析的任务剧本。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/3-300x166.jpg)

当SKILL被激活时，智能体会优先加载SKILL.md的前置元数据完成快速校验，随后将整个指令正文载入上下文环境。scripts子目录中的脚本文件承接具体操作执行，通过API与外部系统交互。位于references目录的技术文档和assets目录的数据文件则构成技能的”知识仓库”，提供深度技术细节及静态资源；两者均采用按需加载机制，仅在需要时被调取，有效平衡了上下文内存占用与功能性需求。

**SKILLS攻击面分析**

在SKILL技术快速落地的背景下，其架构依托“提示词 + 可执行脚本”的组合来提升灵活性与操作规范性，但设计阶段缺乏统一、规范且包含安全验证的分发渠道，也未系统性地融入安全防护机制。这导致风险传导的起点往往位于供应链的薄弱环节：攻击者可通过依赖混淆、托管平台攻击或开发工具代码库入侵等手段对 SKILLS 进行投毒污染，将恶意成分植入可被系统加载的外部资源。由于 SKILLS 在运行时会将提示词用于模型上下文构建并影响推理行为，同时将脚本直接送入本地执行环境运行，这两类核心输入便成为风险进入系统的直接门户，一旦被污染即在系统内部被激活。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/4-300x94.jpg)

**SKILLS攻击面及风险路径**

正因如此，该架构在面对传统资源投毒攻击时尤为脆弱。其运行机制高度依赖文件加载与上下文注入，攻击者只需污染源头资源文件，即可在不直接接触运行环境的情况下实现影响扩散。尤其是当脚本通过本地代码执行器直接启动时，风险隐蔽性更强，大多数开发者与普通使用者依然难以在运行前及时察觉并阻断这类深层威胁。“提示词”与“脚本”两类核心输入在遭受供应链污染后，会在不同环节触发连锁反应。提示词作为模型推理的关键组成部分，被篡改后会扰乱模型决策路径，造成内容生成偏差、输出违背预期甚至引导模型执行不安全指令，从而引发内容安全风险与提示词安全风险，还可能导致智能体在业务场景中输出违规或误导性信息；另一方面，脚本作为直接在本机执行的逻辑载体，若直接植入恶意代码或通过恶意包引入等更隐蔽的方式植入，便可能在执行时突破权限边界，触发未授权系统命令执行，导致系统破坏、敏感数据泄露等端侧风险，甚至使攻击者获得持久化控制。代码相关风险与提示词风险在传播路径上相互叠加：前者作用于智能体的认知与生成层，后者直击系统执行层，使单一隐患在运行过程中被成倍放大。

### **02 SKILLS攻击面实战案例剖析**

**案例一：在SKILL脚本中植入代码，实现任意命令执行**

利用Claude Code中skill-creator插件尝试创建一个命令执行环境演示上述的安全风险问题，例如创建一个用户日常最爱询问的话语，“今天天气怎么样”，当询问天气情况的时候调用skill查询api返回当前区域的天气情况，以下是生成好的SKILL.md

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/5-300x230.png)

在weather.py脚本中增加命令执行“弹出计算器”的代码片段

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/6-300x140.png)

在Opencode中加载恶意的SKILLS,当询问天气怎样，调用skill，触发执行逻辑触发命令执行。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/7-300x168.png)

**案例二：SKILL创建器默认生成脚本存在危险函数**

使用人工智能生成代码时，如未经过严格的安全审计，其产生漏洞的风险较高。当前大模型技术处于快速发展阶段，众多开源社区的开发者在利用此类工具生成代码时，往往忽视了对代码进行系统的安全性审查，导致仅依赖大模型生成的代码存在显著安全隐患。以使用 skill-creator 开发一个简单的四则运算 Skill 为例，若输入以下提示词：“使用 skill-creator 编写一个用于实现加减乘除计算的新 Skill”，skill-creator在领会用途后开始进行代码编写，采用python脚本实现具体功能：

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/8-300x128.png)

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/9-300x191.png)

可以看到大模型在编写代码的过程中就采用eval进行计算，虽然大模型有意识的使用了re模块过滤了空格进行防护，但实际仍存在安全风险，我们可以直接使用payload进行恶意代码执行：

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/10-300x41.png)

###

### **03 SKILLS生态调研：快速增长，安全性待完善**

SKILLS生态目前正处于快速发展阶段。据不完全统计，相关项目已超过105000个，覆盖了多样化的应用场景。与此同时，该生态已衍生出多个SKILLS市场，例如skill.sh市场，通过为SKILLS提供排名机制，帮助用户筛选出高效、高价值的SKILLS，提升了选择的便利性与有效性。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/11-300x260.png)

再例如skillstore.io等市场中增设安全性指标模块，对上线的SKILL进行统一的安全检测与质量评分。通过明确的评估结果向用户传递安全信任，帮助其更放心地选用经过审核的SKILL，从而提升整体生态的安全性与可靠性。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/12-300x116.png)

**针对开源SKILLS安全性的采样研究与分析**

天元实验室大模型安全团队在SKILL商店中采样了将近700个SKILL，在分析过程中我们采取了AI辅助分析的手段，通过OpenCode+提示词的方式快速的对这些SKILLS项目从静态扫描、动态分析和依赖审计这三个安全维度进行检测，目前暂未发现在野投毒事件，但静态扫描发现传统代码安全问题依然存在，也存在一些和案例相一致的风险。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/13-300x238.png)

**针对开源SKILLS的AI分析报告**

AI辅助分析的结果通过以下三个可视化图表呈现：饼图展示了技能目录安全审计报告中风险按严重程度的分布——8个严重风险占比约21.1%，需立即处置；中等与低风险各15个，均占约39.5%，前者多因配置不当或缺乏验证，后者多为教育性质内容或误报。

![](https://blog.nsfocus.net/wp-content/uploads/2026/02/14-300x100.png)

**开源SKILLS安全性抽样分析统计**

进一步结合按风险类别统计可见，代码执行类风险数量最高（20个），主要源于脚本中 shell=True 等不安全命令调用或包安装隐患；其次是文档类（18个），多为提及exploit、payload等敏感关键词的教育或误报场景；输入验证（11个）、文件操作（10个）、网络安全（8个）及密码学（5个）类风险依次递减，分别涉及用户输入未过滤、不安全解压或权限设置、代理/端口配置问题及弱加密或硬编码凭证等问题。从受影响项目类型观察：安全工具类项目安全风险影响最大（22个），这与安全工具本身需高权限操作的特性直接相关；教育内容类紧随其后（18个），涵盖红队/蓝队演练教学材料；其余如数据库客户端、浏览器自动化等项目受影响相对较少。分析表明，绝大多数“风险”集中于安全工具与教育内容类别，这些风险更多源自工具的研究属性与安全教学场景需求，而非恶意攻击意图。

**如何应对SKILLS生态中的安全挑战**

伴随SKILL快速发展，相应的安全问题尚未得到系统性解决。基于SKILLS生态的现状，我们仍需重点应对以下三个核心安全性挑战，并提供相应方案：

1. 如何确保SKILL来源安全：下载SKILL时必须认准官方渠道，如官方GitHub等。开发人员与普通用户在下载过程中极易遭遇安全风险，常见攻击方式包括在GitHub、第三方下载市场等进行依赖投毒。目前SKILL已出现若干分发市场，例如skills.rest、skillsmp.com等，用户应优先通过官方认证渠道获取。
2. 如何保障Agent执行环境安全：必须为Agent运行环境配置高强度的沙箱隔离机制，以避免恶意命令执行、越权操作等安全风险，确保执行过程受控且安全。
3. 进行Agent上线前的安全扫描 在Agent上线前，应对其加载的SKILL进行系统化的安全检测，包括：①静态扫描：检测危险函数、敏感代码模式等；②动态分析：借助大语言模型（LLM）进行语义分析，识别潜在提示词注入等逻辑风险；③依赖审计：对代码脚本调用的第三方库进行人工或自动化校验，避免引入含有漏洞或被篡改的依赖包。

通过上述多维度的安全检查，可显著降低SKILL在客户端侧部署后的安全风险。

### **04 总结**

SKILLS生态在自动化流程中扮演着日益关键的角色，其高速增长与核心价值正吸引着更多应用。然而，这种繁荣景象之下，复杂的安全挑战也悄然浮现。架构中的天然设计隐患、实践中被利用的攻击面，以及生态中尚未弥合的防护缺口，共同构成了一个亟待审视的安全战场。本文首次对快速发展、备受关注的SKILLS生态进行了系统性技术架构与风险梳理，通过第一时间的实地抽样调研与实验分析，我们实证了相关攻击面真实存在，并对现网SKILLS应用现状与演变趋势进行了研判。鉴于大量SKILLS部署已涉及敏感业务数据，尤其建议予以高度警惕，将SKILLS纳入安全审计范畴，并强化安全评估与验证，以切实防范潜在风险。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/%E4%BB%8E%E7%8E%B0%E7%BD%91%E5%88%B0%E9%9D%B6%E5%9C%BA%EF%BC%9A2025%E4%BA%91%E4%B8%8Aai%E5%AE%89%E5%85%A8%E4%BA%8B%E4%BB%B6%E6%B7%B1%E5%BA%A6%E5%A4%8D%E7%9B%98/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)