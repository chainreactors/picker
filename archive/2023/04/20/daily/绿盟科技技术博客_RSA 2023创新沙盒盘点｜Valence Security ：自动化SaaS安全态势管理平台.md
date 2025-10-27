---
title: RSA 2023创新沙盒盘点｜Valence Security ：自动化SaaS安全态势管理平台
url: http://blog.nsfocus.net/rsa-2023innovation-sandbox-valence-security/
source: 绿盟科技技术博客
date: 2023-04-20
fetch_date: 2025-10-04T11:34:32.406768
---

# RSA 2023创新沙盒盘点｜Valence Security ：自动化SaaS安全态势管理平台

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

# RSA 2023创新沙盒盘点｜Valence Security ：自动化SaaS安全态势管理平台

### RSA 2023创新沙盒盘点｜Valence Security ：自动化SaaS安全态势管理平台

[2023-04-19](https://blog.nsfocus.net/rsa-2023innovation-sandbox-valence-security/ "RSA 2023创新沙盒盘点｜Valence Security ：自动化SaaS安全态势管理平台")[李来冰](https://blog.nsfocus.net/author/lilaibing/ "View all posts by 李来冰")[Innovation Sandbox](https://blog.nsfocus.net/tag/innovation-sandbox/), [rsa2023](https://blog.nsfocus.net/tag/rsa2023/)

阅读： 1,227

RSA Conference 2023将于旧金山时间4月24日正式启幕。作为全球网络安全行业创新风向标，一直以来，大会的Innovation Sandbox（创新沙盒）大赛不断为网络安全领域的初创企业提供着创新技术思维的展示平台。

近日，RSA Conference正式公布RSAC 2023创新沙盒竞赛的10名决赛入围者，分别为AnChain.AI、Astrix、Dazz、Endor Labs、Hidden Layer、Pangea、Relyance AI、SafeBase、Valence Security、Zama。

4月24日（美国旧金山时间），创新沙盒将决出本年度冠军，绿盟君在此立足背景介绍、产品特点、核心能力等，带大家走进入围十强厂商，洞悉创新发展趋势。今天，我们要介绍的厂商是Valence Security。

## **一、公司介绍**

Valence Security[1]是以色列一家SaaS安全解决方案提供商，成立于 2021 年，主要为用户提供即时、非侵入性的SaaS安全态势管理平台，帮助用户降低SaaS数据共享、供应链、身份和错误配置的风险。

![](https://blog.nsfocus.net/wp-content/uploads/2023/04/企业微信截图_4835e710-819a-4f67-ba26-d33659ed165d-300x137.png)

CEO Yoni Shohet （左） CTO Shlomi Matichin（右）

Valence Security的联合创始人分别为CEO Yoni Shohet与CTO Shlomi Matichin。Shohet是一名二次创业的企业家，在此之前，他曾与人合作创立了工业物联网安全创业公司SCADAfence[2]。Matichin则是Capester的创始成员之一，Capester是一个公民违规视频的分类平台。

作为一家网络安全初创公司，Valence Security的成长极为迅速，该公司在2022年10月份的A轮融资中获得了2500万美元的资金，由微软的风险投资部门M12领投，其他参与方包括YL Ventures、Porsche Ventures、Akamai Technologies、Alumni Ventures和前赛门铁克CEO Michael Fey。此外，Valence Security还荣获了2023年度最佳网络安全创业公司金奖和SSPM金奖。值得注意的是，在完成A轮融资时，Valence Security仅有25名员工。

那么，为什么Valence Security能在SaaS安全领域高歌猛进呢？下面我们进行分析。

## **二、背景介绍**

在过去几年中，随着越来越多的企业将业务迁移至公有云，SaaS市场呈现稳步增长的趋势。根据Statista的统计数据显示[3]，2021年SaaS 市场规模为1463.3亿美元，到 2022年增长至1671.1亿美元，增长超过12%。预计到2023年，SaaS市场将继续增长14%，达到1952.1亿美元。而SaaS应用已经深度嵌入到许多组织的业务功能中，包括销售、营销和产品研发，以促进企业的生产力和效率。据Matichin称，“平均而言，企业使用约80个SaaS应用程序，BetterCloud统计数据显示，拥有超过1000名员工的企业使用超过150个应用程序”。然而，由于不加选择的采用，SaaS应用、集成、用户和数据已经演变成一个无序的SaaS网格（SaaS Mesh） ，安全团队难以进行集中控制和管理。Valence Security在**The 2022 Shadow SaaS-to-SaaS Integration Report** 报告中指出：

* 企业平均有917个SaaS-to-SaaS的第三方集成；
* 48%的SaaS集成处于未使用状态；
* 平均而言，用户每30天就有75个新的第三方集成；
* 86%的调查对象对他们目前的SaaS网格可视性和风险降低解决方案不满意。

可见在实际的企业环境中，SaaS网格安全管理的混乱。在《2023年Q1 SaaS安全威胁场景报告》[4]中，Docontrol指出了SaaS应用所面临的多种安全威胁，包括内部威胁、内部vs外部参与者访问、第三方至第四方的共享、过期的权限、第三方OAuth应用，以及供应链安全威胁如SolarWinds和Log4j等。

这些问题给企业带来了巨大的挑战，包括人员的削减与专业知识的缺乏、庞大的安全事件告警以及企业内数以百计的SaaS应用互联等等。

为解决这些挑战，Gartner提出了SSPM（SaaS安全态势管理）的概念。SSPM是一种 “持续评估安全风险和管理SaaS应用安全态势的工具”。与CSPM（云安全态势管理）不同的是，SSPM专注于SaaS应用安全，可能不具备一些CSPM的功能。2021年研究人员[5]对SaaS安全市场的估值为83亿美元，预计至2028年将达到212亿美元。

正是察觉到了SaaS安全市场的需求，使得Matichin和Shohet建立了Valence Security，希望能够解决企业的SaaS安全问题。那么Valence Security都有哪些功能呢？是否能解决企业SaaS应用环境中常见的安全风险，我们来了解一下。

## **三、产品功能**

Valence Security的主要功能是提供安全团队所需的可见性和业务上下文，通过对SaaS安全风险进行优先排序，在多个SaaS平台中实现自动化的修复工作流程，目前已支持多种常见SaaS应用，如图2所示：

![](https://blog.nsfocus.net/wp-content/uploads/2023/04/图片10-1-300x173.png)

图2 Valence Security支持的SaaS产品

Valence Security具有无代理安装、集中控制、自动化修复等特点，其工作流程如图3所示：

![](https://blog.nsfocus.net/wp-content/uploads/2023/04/图片11-1-300x150.png)

图3 Vanlence工作流程

****No.1**** **SaaS发现和可视化**

Valence Security可通过无代理的方式连接至用户的核心SaaS应用程序，能够持续发现集成的SaaS应用、第三方的威胁情报等，并将供应商风险(TPRM)流程情境化，最终以可视化的形式进行展示（如图4），降低了用户SaaS应用治理的门槛：

![](https://blog.nsfocus.net/wp-content/uploads/2023/04/图片12-1-300x176.png)

图4 SaaS发现和可视化

官方宣称“在几分钟内，安全平台可以连接到客户的核心SaaS应用程序，以分析配置和活动日志”，Valence Security应该在安装过程中对接SaaS应用的管理员凭证，通过管理员权限连接至SaaS应用后分析应用的配置和日志文件，为后续的风险检测做铺垫。

****No.2**** **自动化+手动修复流程**

Valence Security支持自动化的修复流程，通过统一的安全策略，扫描SaaS应用的安全风险并进行自动化修复。安全策略覆盖多种流行的SaaS应用，如Google Workspace、Microsoft Office 365、Github等，策略的内容包括SaaS应用常见的风险，如不活跃的或有风险的和过度授权的角色、有风险的第三方组件、不安全的数据共享、不活跃的或休眠API/OAuth令牌、不安全的电子邮件转发规则、不符合规定的无/低代码工作流程等，同时也包括不安全配置对应的具体修复措施。当Valence Security检测到相应风险之后便会进行自动化修复，如自动开启MFA、自动关闭数据公开访问等，提高了修复的工作效率，如下图5、图6所示：

![](https://blog.nsfocus.net/wp-content/uploads/2023/04/图片13-1-300x164.png)

图5 MAF风险检测

![](https://blog.nsfocus.net/wp-content/uploads/2023/04/图片14-1-300x164.png)

图6 MFA风险修复

通过Valence Security的安全策略检测以及后续的自动化修复，可以帮助企业的SaaS网格满足合规性标准。

修复工作流程不仅可以自动化，也支持让业务用户手动修复。在修复过程中会自动向用户发出通知，并为其提供修复指导，通过让用户参与修复流程来提升用户的体验和最终的治理效果，以避免全自动化流程对业务造成不良影响的情况。Matichin曾称“为业务用户提供上下文并让其参与配置”是Valence Security的优势项，如图7、图8所示：

![](https://blog.nsfocus.net/wp-content/uploads/2023/04/企业微信截图_682a03c4-15db-4461-add0-0a4936168ef8-300x160.png)

图7 配置指导

![](https://blog.nsfocus.net/wp-content/uploads/2023/04/图片15-1-300x166.png)

图8 修复完成

## **四、案例分析**

下面分别通过一个具体的SaaS应用案例和客户案例，来了解Valence Security如何保护某个SaaS应用的安全，又如何帮助企业解决处理SaaS网格安全治理问题。

**SaaS案例——Github**

GitHub是一个领先的软件开发和版本控制平台，是当今许多组织的关键业务应用，因为数字化转型正在将多个领域的许多公司变成软件和技术公司。GitHub用户可以连接GitHub应用程序和OAuth应用程序，以提高他们的生产力和协作，配置个人访问令牌（PAT），以便与外部服务集成，生成SSH密钥以识别自己，而不需要用户名和密码，甚至可以使用GitHub Actions使他们的CI/CD和其他工作流程自动化，减少人力投入。

‍GitHub应用可以在GitHub市场上发布，如果该应用是内部定制的应用（即组织为其个人使用而创建的应用），则可能仅限内部使用。此外，组织账户上的GitHub应用的授权仅限于管理员，非管理员用户仅可以授权个人账户的GitHub应用。

虽然GitHub本身是安全的，但被授权的第三方可能是一个薄弱环节。本身有风险的或权限过高的OAuth令牌则可以被恶意利用，使GitHub客户面临数据泄露的风险。

然而针对GitHub的供应链攻击并没有被现有的解决方案覆盖，如IdP（身份提供商）、CASB（云访问安全代理）和SSPM（SaaS安全态势管理），这些解决方案专注于人对SaaS的访问控制，却忽视了日益增长的SaaS-to-SaaS的第三方集成侧。

那Valence Security如何保护GitHub的安全呢？

Valence Security可以与GitHub环境无缝集成，主要通过以下手段发现SaaS网格攻击面并治理与之相关的风险：

* 发现所有连接到GitHub的第三方集成，如个人访问令牌、OAuth应用程序、GitHub应用程序和SSH密钥等；
* 分析SaaS-to-SaaS连接的访问范围和实际使用情况，以消除权限过高和不活跃的授权项目；
* 识别被授予访问令牌的第三方供应商，确保与供应商风险管理和TPRM计划保持一致；
* 监控第三方应用程序的API调用，以检测关键数据的潜在风险或API攻击；
* 自动化工作流程，以确保在分布式IT环境中与用户进行有效修复和沟通。

**客户案例**

* **客户简介**

Lionbridge是一家翻译服务公司，成立于1996年，目前已有6000多名员工和2500多名客户，支持350多种语言，在全球23个国家设有办事处。Lionbridge面临的主要挑战如下：

1）Lionbridge为其分布在全部不同业务部门的员工采用了不同的SaaS解决方案，但同时也给统一管理带来了困难。

2）现有的第三方集成，对核心SaaS应用的高权限访问。

3）对电子邮件转发规则的管理有限。

4）对非活动用户账户的更大可见性的业务需求。

* **解决方案**

Lionbridge使用Valence Security发现了企业环境内超过1000个SaaS-to-SaaS的集成。

Valence Security为Lionbridge提供了自动化的SaaS发现和修复，检测并分类了超过1000个SaaS-to-SaaS的集成，使安全团队对整个SaaS服务的风险有统一的可见性和控制，同时将业务用户纳入修复工作流程中并为他们提供最佳实践指导。最终约有95%的不活跃或过时的令牌被撤销，对未管理的电子邮件转发规则实现了100%的可见性和管理，识别到了大约10%的休眠账户，从而提高了资源的可用性。

## **五、总结**

其实在2020年的RSA创新沙盒大赛中，就已经有SaaS安全领域的公司入围：AppOmni[6]和Obsidian Security[7]。其中Obsidian Security公司的关键词是云检测与响应（CDR），主要是将xDR的理念应用在云端。通过不断收集，规范化和分析来自SaaS应用和云服务的大量状态和行为数据，为安全专业人员提供检测、响应和调查云中威胁所需的全面的可视化信息。和Valence Security更为相似的公司是AppOmni。AppOmni公司的产品面向SaaS应用，提供安全配置扫描、合规控制和IT管理的功能，虽然可以持续监控SaaS安全态势并在数分钟内完成扫描提供相应报告，但AppOmni并没有自动化的修复流程。

因此综合官方的产品文档以及公开的具体案例分析来看，与AppOmni相比，Valence Security的亮点主要是在于其发现与可视化和自动化修复的功能。

在发现与可视化方面，Valence Security通过分析SaaS应用的配置与活动日志，结合第三方威胁情报，能够自动化发现SaaS应用、用户、权限、数据和第三方集成的信息，并以可视化的方式进行展示，满足了企业对当前SaaS网格可视性的需求，降低了企业SaaS统一管理的门槛和难度，像Lionbridge这样SaaS应用管理混乱的企业场景，便可以通过可视化界面清晰掌控全局。同时通过清晰的SaaS网格图，也能较好地发现供应链风险。

自动化修复流程是Valence Security的另一亮点。在实验室的研究积累之上，覆盖了当今众多SaaS应用的安全威胁检测。在检测到相应的安全风险之后，通过全自动或人工干预的方式来进行修复工作，既可提高工作效率，也可在人工干预时不断提升用户的安全意识。

综合SaaS安全市场的增长趋势以及供应链安全的关注度，Valence Security能否作为SSPM技术发展的代表从众多创新公司中脱颖而出，让我们拭目以待！

参考文献

[1] https://www.Valence Securitysecurity.com

[2] https://w...