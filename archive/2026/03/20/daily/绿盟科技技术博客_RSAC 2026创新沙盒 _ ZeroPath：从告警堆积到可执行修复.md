---
title: RSAC 2026创新沙盒 | ZeroPath：从告警堆积到可执行修复
url: https://blog.nsfocus.net/rsac-2026%e5%88%9b%e6%96%b0%e6%b2%99%e7%9b%92-zeropath%ef%bc%9a%e4%bb%8e%e5%91%8a%e8%ad%a6%e5%a0%86%e7%a7%af%e5%88%b0%e5%8f%af%e6%89%a7%e8%a1%8c%e4%bf%ae%e5%a4%8d/
source: 绿盟科技技术博客
date: 2026-03-20
fetch_date: 2026-03-21T04:06:41.461735
---

# RSAC 2026创新沙盒 | ZeroPath：从告警堆积到可执行修复

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

# RSAC 2026创新沙盒 | ZeroPath：从告警堆积到可执行修复

### RSAC 2026创新沙盒 | ZeroPath：从告警堆积到可执行修复

[2026-03-20](https://blog.nsfocus.net/rsac-2026%E5%88%9B%E6%96%B0%E6%B2%99%E7%9B%92-zeropath%EF%BC%9A%E4%BB%8E%E5%91%8A%E8%AD%A6%E5%A0%86%E7%A7%AF%E5%88%B0%E5%8F%AF%E6%89%A7%E8%A1%8C%E4%BF%AE%E5%A4%8D/ "RSAC 2026创新沙盒 | ZeroPath：从告警堆积到可执行修复")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 19

**RSA Conference 2026** 将于美国旧金山时间3月23日正式启幕。作为全球网络安全行业创新风向标，一直以来，大会的 **Innovation Sandbox（创新沙盒）大赛**不断为网络安全领域的初创企业提供着创新技术思维的展示平台。

近日，RSA Conference 正式公布 RSAC 2026 创新沙盒竞赛的10名决赛入围者，分别为 Charm Security、Clearly AI,Inc.、Crashoverride、Fig Security、Geordie AI、Glide Identity、Humanix、Realm Labs、Token Security、ZeroPath。

聚焦网络安全新热点，洞悉安全发展新趋势。与绿盟君一道，走进**ZeroPath**。

### **01****公司简介**

ZeroPath是一家成立于2024年的AI原生应用安全创业公司，同时其核心产品也沿用同名品牌ZeroPath。公司聚焦利用AI自动发现、验证并修复代码漏洞，试图突破传统SAST、SCA、Secrets扫描和IaC扫描各自为战、结果割裂的局限，将应用安全分析、漏洞验证与修复建议整合到统一平台中。其对外叙事重点在于“让安全结论更可验证、让修复更可执行”，强调不仅要识别风险，还要尽可能将结果转化为开发团队能够直接审查和落地的修复动作。作为Y Combinator 2024年夏季批次（S24）的创业项目，ZeroPath也体现出当前应用安全领域向人工智能原生（AI-native）、低噪声和工程闭环方向演进的趋势。

ZeroPath由Dean Valentine（CEO，首席执行官）、Nathan Hrncirik（CIO，首席信息官）、Raphael Karger（CTO，首席技术官）和Etienne Lunetta（COO，首席运营官）联合创立，四位创始人照片如图1所示。公开资料显示，Dean Valentine是公司当前最主要的对外代表人物；创始团队则具有连续创业以及Tesla红队、Google安全工程等背景，这在一定程度上解释了ZeroPath为何将产品重点放在复杂业务逻辑漏洞、漏洞利用条件验证以及自动化修复推进等更贴近真实企业场景的问题上。2026年，ZeroPath入选RSAC 创新沙盒决赛，进一步提升了其在新兴应用安全赛道中的关注度。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片1-4-300x75.png)

图1  ZeroPath四位联合创始人。自左至右依次为：Dean Valentine、Nathan Hrncirik、Raphael Karger和Etienne Lunetta

### **02****产品背景：**

**开发安全的工具越多，漏洞修复越慢？**

在企业中的AppSec（Application Security，应用安全），这类现象并不少见：工具买得越来越全，告警却越来越多，但修复速度反而更慢。这往往并不只是因为漏洞数量增加，而是因为安全团队面对的判断与处置成本也在同步上升。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片2-1-300x145.png)

图2  多工具触发的告警与修复推迟的形成机制

一方面，SAST、SCA、Secrets扫描、IaC扫描等工具越来越多，不同来源的告警持续汇流；另一方面，真正高风险的问题表现为访问控制缺失、鉴权遗漏、链式触发条件等复杂业务逻辑漏洞[1]；同时，GenAI驱动的代码生成与开发提速，也在让代码提交更快、变更更碎、潜在脆弱面更多。三类因素叠加之后，企业看到的往往不是工具更多，风险收敛更快，而是告警越来越多、判断越来越难、修复节奏越来越慢，如图2所示。

***2.1*****告警噪声不是“小毛病”，****会直接拖延漏洞修复节奏**

传统工具的一个典型局限在于：它们很擅长发现“代码是否存在问题”，但不擅长回答“有问题的代码到底会不会被利用”。因此，大量告警往往只是在理论上成立，却难以在具体业务系统中复现。以Node.js生态中常用的进程管理与应用部署工具PM2为例，它常被用于服务保活、日志管理和多进程运行，曾披露过正则表达式拒绝服务漏洞[28]。传统工具普遍会在该漏洞代码存在时便会告警，但它并不了解系统对PM2的实际使用方式，是否调用了该组件、是否使用漏洞相关的接口、是否使用了净化函数。

图3给出了三种常见情形：A表示系统虽然引入了存在风险的组件，但业务代码并未调用漏洞代码，此时工具告警但该漏洞在代码中是死代码，并无威胁；B表示相关路径确实可达，但输入经过净化或受限，例如业务的输入字符串是固定的，无法满足使得服务器崩溃的正则表达式模式，却较难真正触发；C则表示业务代码直接调用了相关功能且缺乏有效防护，这时漏洞才更接近真实可利用状态。问题在于，传统工具通常更容易停留在“组件存在漏洞”这一层。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片3-1-300x158.png)

图3  漏洞被检测到，并不意味着该漏洞在当前业务中一定可被利用

这时候安全就会变成一个高强度的人工分析过程：把一条条告警从海量输出中检索出来，去补上下文——这条路由是否外网可达，或者这里是否已经鉴权了，又或这个参数是不是用户可控？当项目规模较小时，这类工作尚可依赖人员经验和人工投入维持运转；但随着系统复杂度和告警数量持续上升，单纯依靠人工研判的方式往往难以维持。ZeroPath此次受到关注，一个重要原因也在于它试图回应这一行业共性问题：应用安全的瓶颈很多时候并不是检测不到，而是处理不过来[1]，这也是AI时代最有可能产生实际价值的场景。

***2.2*****业务逻辑漏洞修复难，****是因其不呈现典型的漏洞形态**

与注入、反序列化、危险函数误用等较为典型的漏洞不同，业务逻辑漏洞的难点往往不在于代码写错了什么，而在于系统缺了什么约束。这类问题通常不会直接表现为显式的不安全调用，而是隐藏在访问控制、业务状态转换或资源归属校验等逻辑环节之中。因此，即便代码表面上不存在明显异常，系统仍可能在业务语义层面暴露出高风险缺陷。

以根据订单编号查询数据库并返回订单详情为例，存在接口：GET /api/orders/{id}。从表面上看，该接口既不存在明显的注入风险，也未出现显式危险操作，SAST可能也不会告警。然而，真正决定该接口是否安全的关键，往往在于是否存在一条必要的业务约束：当前用户是否有权访问该订单。如果系统缺失了“订单必须属于当前用户”这一校验，攻击者便可能通过枚举id访问他人订单信息，这正是典型的不安全的直接对象引用（Insecure Direct Object Reference，IDOR）或更广义的访问控制缺陷，如图4所示。之所以难以检测，是因为工具不仅需要判断该id是否来自用户可控输入，还需要进一步理解系统中的授权语义，即“只能访问自己的订单”这一规则在具体代码路径中是否得到了正确实施，而这类约束在不同系统中的实现方式往往并不统一。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片4-1-300x118.png)

图4  业务逻辑漏洞难以挖掘

业务逻辑漏洞之所以修复困难，根本原因在于其判定过程高度依赖理解具体业务上下文，而非单一的语法特征或危险模式匹配。OWASP Top10 2021将Broken Access Control列为首位风险类别[15]，凸显了访问控制策略未被正确实施所带来的广泛性与严重性，而且很容易混进日常功能开发里。

***2.3*****代码生成（GenAI）的广泛应用****出现了更多的脆弱面**

另一个背景是开发节奏变化。Veracode在2025 GenAI Code Security Report的解读[13]中提到，他们测试了100+模型在多语言任务上的代码安全表现，结论是：AI生成代码经常不安全，风险很可能已经进入代码栈。GenAI的大规模使用加速了代码提交的速度，同时开发人员的安全意识淡薄导致安全工作被动后移，使得安全任务大规模积压在安全人员手中，如图5所示。

这一判断若置于实际开发场景中理解，其含义会更加具体：当产出更快、提交更碎、评审压力更大时，诸如校验缺失、默认配置不安全等问题也更容易在快速迭代中被忽略。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片5-2-300x150.png)

图5  现在安全节奏难以跟上开发速度

### **03****ZeroPath的核心思路：****把传统代码安全“四件套”融合、突破**

大多数企业的应用安全团队往往单独采购SAST、SCA、Secrets扫描、IaC扫描产品，但是这些工具的输出结果彼此割裂，难以统一融合，但一旦需要进一步确认某个漏洞是否真实可利用，团队往往仍需依赖人工将多份报告与业务上下文重新整合起来，如图6所示。

ZeroPath的核心主张是，不再让用户事后去拼接多套工具的检测结果，而是直接提供一个统一的应用安全分析视图，其官网用一句话概括：One Scanner. All of AppSec[26]。RSAC官方发布的ZeroPath入围公司介绍也特别说明：用一个人工智能原生引擎替代传统SAST/SCA/Secrets/IaC组合，目标是抓到更复杂的业务逻辑问题和可串联的漏洞链[1]。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片6-2-300x136.png)

图6  从四分报告中难以拼成一张证据图

***3.1*****SAST：从“发现危险点”走向“串联完整路径”**

传统SAST的典型模式是：在识别到潜在sink（如危险函数或敏感调用）后先行给出告警，而输入来源、校验逻辑和鉴权条件仍需由分析人员进一步追溯。这种方式本身并无问题，但在真实代码库中往往会带来大量告警，并显著增加人工解释成本。

ZeroPath在SAST页面强调的重点，反而是更贴近工程判断的那一步：它想做“从输入到敏感点”的追踪，并把业务逻辑与鉴权缺陷当作重点对象（缺失鉴权、不安全的直接对象引用、授权绕过路径、支付竞态等）[6]。可以将其理解为：ZeroPath并不满足于仅作为“语法检查器”，更强调对完整业务执行路径的分析——去看一条请求从哪进来、走过哪些校验、最后落到哪里，如图7所示。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片7-2-300x110.png)

图7  SAST不只是报点，关键是把路径串起来

以不安全的直接对象引用为例，一个接口接收orderId，然后查库返回订单。SAST很容易在“查库返回敏感数据”这一段附近提示风险，但真正决定它是不是漏洞的，是中间有没有“订单属于当前用户”的校验。

如果工具能把“入口参数来自用户→没有用户/租户边界校验→直接读到订单数据”这条路径串起来，分析人员即可更快判断该问题是否已接近真实可利用漏洞。反过来，如果它只给一句“可能越权访问”，仍需依赖人工进一步审查代码路径。

***3.2*****SCA：从“组件存在漏洞”走向“能不能触发”**

SCA长期面临的典型问题在于是：CVE列表往往数量庞大，其中不乏高危项，但团队往往难以及时判断“我们这条链路里到底用到了它吗”。于是团队要么在缺乏充分判断的情况下仓促修复，要么长期延后处理并逐渐形成安全债务。

软件供应链过去几年的改良方向叫可达性分析（Reachability Analysis）：用依赖图、调用路径去过滤掉“不可能走到的漏洞代码”[16]。近年来一些工作[27]出现了可利用性分析（Exploitability Analysis）:漏洞到外部输入可控的代码不仅仅存在代码调用链，调用链上的可控输入/可控条件还需要满足漏洞可利用的约束，具体如图8所示，这样的漏洞才值得投入分析。ZeroPath在其方案页面里也给出类似口径：通过“AI Reachability Analysis”把大量被标记的CVE收敛到少量“更可能真正可利用”的问题[7]。ZeroPath的表达更接近第二种——它想把SCA的输出从“这组件存在漏洞”推到“是否存在利用的风险”。

这一路线并非ZeroPath独有，而是近两年SCA领域较明显的演进方向[32]。公开资料显示，Semgrep在2025年已将可达性分析进一步区分为依赖级、函数级和数据流级三种深度[29]；Snyk在2026年官方文档中也明确将可达性分析定义为“应用是否调用了与漏洞相关的代码元素”[30]；Endor Labs则更进一步，直接在文档中区分可利用（Exploitable）、潜在可利用（Potentially Exploitable）和误报（False Positives）[31]。放在这个背景下看，ZeroPath强调的不只是“发现受影响组件”，而是试图借助大模型将判断进一步推进到“当前系统中是否具备实际利用条件”这一层。与之相比，Endor Labs公开强调的仍主要是基于静态分析的方法。这一差异具有较强的分析价值，因为它对应的就是告警积压问题的根因：团队很难投入足够精力逐个理解和审计每个漏洞的上百条代码调用路径的各个约束。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片8-2-300x174.png)

图8  从“漏洞代码可达”到“漏洞条件可利用”的风险筛选差异

***3.3*****Secrets和IaC：****从“独立扫描结果”走向“上下文证据融合”**

将Secrets扫描和IaC扫描作为独立能力部署，本身并不是新做法，更关键的问题在于：能否将其与代码路径、外部暴露面和依赖漏洞置于同一分析框架中理解。

RSAC创新沙盒中该公司的简介中，它把Secrets与IaC直接写进了“替代栈”的范围[1]。ZeroPath的方案页面进一步强调：它会用上下文方式去减少误报，例如对Secrets做更智能的过滤，对IaC风险做识别与“合理忽略”[7]。这些说法在产品宣传里很常见，但如果放进“一体化引擎”的逻辑里，它的意义会更具体：

IaC告诉你“哪里对外暴露”，代码告诉你“暴露的入口能干什么”；Secrets告诉你“是否暴露了敏感凭据”，代码和权限链路告诉你“这些凭据可能对应哪些可访问资源”，如图9所示。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片9-2-300x148.png)

图9  Secrets+IaC作为上下文证据

当这些信息能互相作为证据，所谓链式漏洞才不再只是概念化描述，而是一条能被复核的路径[1][7]。

### **04****从发现问题到推进修复：****应用安全工具的新竞争方向**

传统AppSec的基本工作方式，长期建立在“工具发现—人工分发、修复”这...