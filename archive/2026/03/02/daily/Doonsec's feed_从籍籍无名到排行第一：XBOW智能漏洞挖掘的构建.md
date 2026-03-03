---
title: 从籍籍无名到排行第一：XBOW智能漏洞挖掘的构建
url: https://mp.weixin.qq.com/s/1ngqPGIKLEqmJfr1ptISXA
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:07:17.477226
---

# 从籍籍无名到排行第一：XBOW智能漏洞挖掘的构建

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VoF2eOII0kSeFXdyL4MoQ5e5exzDjNY7WcicMQmJmlleJDVMtV2eZHh4ibNkGCibaK1LbaA4pCqRWoNLvvjcc6X4u6UICibUEsCCtCqlqf44sD4/0?wx_fmt=jpeg)

# 从籍籍无名到排行第一：XBOW智能漏洞挖掘的构建

原创

洞源实验室
洞源实验室

洞源实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/gEGSydvbZs6z4Qbkhbiar4lfzdY1az6vEzzEYZnt4QUJJ1Q7BtibXibURKd7XGlcbSJbicIQjTwJo3oAdMHGt8AjKg/640?wx_fmt=gif)

自大语言模型（LLM）震惊世界后，多年以来网络安全领域的从业者们也一直在探索将LLM应用到自动化漏洞挖掘或自动化渗透测试，终于在2025年，来自美国的XBOW公司的XBOW以自动化渗透测试能力登顶了漏洞悬赏平台HackerOne的榜单第一。

![](https://mmbiz.qpic.cn/mmbiz_jpg/VoF2eOII0kQyCicUb4iccvkKw1t9mv8sRExsc4RdapcMicdiaDnCSeT6Wicicpibp3HJhdEOunUrTTqNpoWr1unZH4CWv2GlScMQoicfWIsKg1cIE6Q/640?wx_fmt=webp&from=appmsg)

传统的漏洞扫描工具主要依赖于预定义的规则、签名或简单的启发式算法，其局限性在于无法理解复杂的业务逻辑，且容易产生大量的误报（False Positives），无论是DAST（动态应用安全测试）或者SAST（静态应用安全测试），都需要在所有测试完成后投入大量人力进行逐个分析与验证，这进一步受到了人员能力与经验的限制。

本文结合XBOW团队在BlackHat USA 2025分享的技术细节和经验，以及官网在过去半年的实践经验，深入剖析XBOW的自动化漏洞挖掘体系的构建思路、构建经验和核心技术架构，因关键技术细节属于商业机密，故本文中的部分技术说明为笔者猜测。

# 早期探索

在XBOW构建的早期阶段，XBOW团队主要通过两类工作来打磨LLM的的漏洞挖掘能力：

首先，是通过现有的CTF挑战（比如PortSwigger官方题目和PentesterLab）测试XBOW的漏洞挖掘能力，同时构建了XBOW自己的140道漏洞题目（https://github.com/xbow-engineering/validation-benchmarks/）用于检验XBOW的漏洞挖掘能力。

其次，是专注于挖掘开源项目中的零日（zero-day）漏洞，简单而言，就是在每个项目的检测中，都赋予AI访问源代码的权限，模拟白盒测试。

经验表明，在结构化基准测试和开源项目中发现漏洞是一个极佳的自动化漏洞挖掘体系的起点。

但没有只有在真实的、黑盒的测试环境中经历实战，才能够证明基于AI的自动化漏洞挖掘能力与人工漏洞挖掘的差异性。于是，XBOW团队开始在HackerOne托管的公开和私人漏洞赏金计划中对 XBOW 进行“内部测试”。

HackerOne的挑战在于潜在目标太过于庞大，如果逐一进行测试会导致整体性价比极低，一方面会针对重复的目标进行反复的测试，一方面会造成不必要的Token的损耗（毕竟是需要接入大模型的开放接口）。

所以，第一步是需要针对被测目标构建测试范围和测试策略（Scopes and Policies）

通过将目标域名录入数据库，并针对域名进一步扩展子域名，XBOW团队建立了一套评分系统来评估最有价值的目标。评分标准涵盖的信号包括：

目标外观、WAF（Web 应用防火墙）及其他防护措施的存在、HTTP 状态码、重定向行为、认证表单、可达端点数量、底层技术等。

在大规模项目中，域名去重变得至关重要，以及，遇到克隆或预生产环境（例如 stage0001-dev.example.com）也是很常见的。一旦在其中一个环境中发现漏洞，其他环境也很可能存在类似问题。为了保持高效，他们使用SimHash检测内容层面的相似性，并利用无头浏览器抓取网站截图，并应用ImageHash技术进行视觉相似性评估，从而对资产进行分组，并将精力集中在独特且高影响的目标上。

长期以来，自动化一直饱受误报（False Positives）的困扰，这在漏洞扫描中尤为明显。如果工具标注了数十个无关紧要的问题，往往会带来更多的代价与麻烦。当AI技术应用后赌注变得更高：模型虽然泛化能力强，但验证像漏洞挖掘这样的边缘案例则完全是另一回事。 因为，AI会过度讨好人类，以至于无法用AI来验证AI产生的结果，就像问它：

汽车快没油了，最近的加油站只有500米，该拿什么样的容器装汽油？

因此，为了确保结果的准确性，XBOW团队开发了“验证器（Validators）”，即自动化的同行评审员，用于确认XBOW发现的每一个漏洞。这个过程有时利用大语言模型，有时则是构建自定义的程序化检查。例如，为了验证跨站脚本（XSS）漏洞，无头浏览器会访问目标站点，以验证 JavaScript的Payload是否真的被执行了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/VoF2eOII0kQpd5z629zNTAV6T5AgoOcXA6BVjiaYpkMoibWXdmowkLeFia3SeqyNMwCZy0ib31iatAn7o8KicPkuH6zKghuHxkVyXfaPjG0qicD9jw/640?wx_fmt=webp&from=appmsg)

最终，通过三个月的时间，XBOW提交了1060个漏洞，并登顶了HackerOne排行榜第一。所有漏洞都是自动化挖掘的，只是在正式提交到HackerOne平台前，XBOW团队需要人工对每个漏洞进行审查，以确保漏洞报告符合HackerOne关于自动化检测的政策（比如，也有项目因为XBOW的自动化挖掘被项目方移除）。

XBOW在这些漏洞中识别了多种类型的漏洞，包括：远程代码执行（RCE）、SQL 注入、XML 外部实体（XXE）、路径遍历、服务端请求伪造（SSRF）、跨站脚本（XSS）、信息泄露、缓存中毒、密钥泄露等。仅在2025年3月到6月，提交的漏洞就被项目所有者分类为 54 个严重、242 个高危、524 个中等和 65 个低危问题。

# 经验教训

在真实世界中，通过海量代码发现真实的漏洞相比代码量而言是罕见的。根据贝叶斯定理，如果一个安全漏洞测试的准确率为99%，而漏洞的发生率仅为万分之一，那么一个“阳性”结果是真漏洞的概率其实只有1% 左右。这意味着，现实中误报漏洞的绝对数量远远超过了极少数真漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VoF2eOII0kSbVF57oNlZ51gInZnjIEnaS7vKz8KfpkSWIRgPVjY5G84vj76ibI3y2PyVCLZxXOZRa0NyWfcM4p1lnClpIvW5LAU8aO4sWQss/640?wx_fmt=jpeg&from=appmsg)

在当前AI大模型的漏洞发掘过程中，会因为上述数学上的必然性造成更多的误报，也就是，试图将LLM驱动的安全工具投入实战的团队很快就会遇到一个熟悉的问题：模型听起来充满信心，但漏洞并不真实。

这并非是某个模型的缺陷，也无法通过更好的提示词或更多上下文来解决。而是 LLM 的推理方式与现实世界中漏洞实际存在方式之间的根本错位，也就是我们需要区分“漏洞挖掘”与“漏洞证明”的区别。

在AI领域，“幻觉”是指生成不符合事实的信息。在安全领域，它以更微妙的方式出现，例如：

从仅类似于先前漏洞利用的响应模式中推断出 SQL 注入。

仅因为某个端点符合已知的漏洞类别，就认为它是可利用的。

在未曾演示漏洞的情况下就断言漏洞的影响。

这些AI的输出结果本质上是对漏洞数据、利用报告和源代码进行模式识别的结果，而大模型只是执行其设计的初衷，根据之前的案例生成最合理的解释。也就是说，大模型会过度讨好人类的提示词，而不会对提示词本身或输出的结果进行验证。

大模型并不观察现实，不测量时间差异，不验证副作用，也不确认Payload是否真的改变了应用程序的行为。它们只是根据“应该”发生什么、“通常”发生什么、“其他地方”发生过什么来进行抽象推理，并解释这里“可能”发生了什么，但终究无法确认实际发生了什么。

这就是为什么将原始大模型的输出视为漏洞发现会产生噪音。因此，模型可以正确识别有趣的攻击面，但在可利用性上仍然会出错。在安全领域，只有当一个漏洞能在真实系统上被触发时，它才真正存在。除此之外的一切都只是假设。

因此，XBOW构建了一套分类清晰的验证器体系（Validation Toolbox），根据被测环境的可控性，他们又分为两类验证方法：

一类是可控的测试环境，即测试过程中可以操控被测环境（白盒或灰盒测试）。

在这类环境中，预先植入“金丝雀”字符串，如随机生成的UUID格式Flag。例如，在文件系统的/flag.txt文件中植入该Flag，或在数据库中植入Flag记录，又或者在内网环境中部署只包含Flag文件的内网服务器，只有Agent成功利用漏洞并读取到Flag时才能够确认对应漏洞的存在。

一类是不可控的测试环境，即无法在被测环境中植入上述Flag特征文件或字符串。

在这类环境中，XBOW采用的技术验证方式类似漏洞扫描工具，比如，根据Agent提交的URL，验证系统启动无头浏览器访问该URL，并监测是否触发了alert()或console.log()方法，又或者，根据Agent分别执行含有SLEEP(1)和SLEEP(5)的请求，通过监测响应的时间差来确定漏洞是否存在。

# 关键技术

根据XBOW当前披露的博客文章与相关说明，XBOW Agent的构建主要包括两个部分：

## 1. 环境与工具集成

通过集成多个大模型构建Agent，避免单个大模型能力缺失造成模型能力上的偏差，并结合不同模型的能力赋予对应的环境和工具能力，典型的工具包括curl、python3和interactsh。同时，如果能够为Agent提供应用的完整源代码或Docker镜像文件系统，则漏洞的发现能力会显著提升，即Agent在理解源代码后能理解更加复杂的漏洞。

## 2. Prompt设计与模型调整

XBOW的Prompt设计核心遵循任务导向，比如类似“你的任务是证明XX漏洞的存在，并为此提供最小化可复现的HTTP请求”，同时在实践过程中，会根据被测环境的防护能力不断调整Prompt，比如增加对于编码处理、WAF绕过等复杂情况的说明，最终通过反复调整Prompt对模型输出能力进行调整。

最后，上述方案在实践过程中也会存在一些意想不到的问题，比如验证系统忘记检查URL协议，以至于当Agent提交javascript:alert("xss")后出发了弹窗，从而被验证系统认为是安全漏洞，又或者，验证系统的无头浏览器禁用了同源策略（SOP），导致Agent可以跨域操作，从而被认为存在XSS漏洞等等。因此，要不断修正验证系统自己的验证漏洞。

# 编后语

尽管这套体系在常规的技术漏洞发掘上表现卓越，但从技术方案设计角度仍然存在巨大的局限性，一方面是验证系统的设计与存在局限了漏洞种类的多样性，一方面是该系统仍然无法解决业务逻辑漏洞（如IDOR和越权），这也是XBOW目前仍在突破的难点，未来可能需要针对业务逻辑开发特定的验证系统。

如上所述，XBOW的自动化漏洞挖掘体系与传统扫描器不同之处，在于智能化的攻击者思维与实际利用验证的有机结合，它利用大模型（LLM）构建自主的推理型代理（agent），动态理解应用的行为与上下文，并根据反馈实时调整策略。与简单的模板扫描相比，XBOW从根本上追求“能自动找出可真实利用的漏洞并生成完整攻击链”。

# 参考链接

1. https://xbow.com/blog/top-1-how-xbow-did-it

2. <AI Agents for Offsec with Zero False Positives> BlackHat 2025

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs7HiaU1TeSL6QyZuasLpGExfp2m8lBgbIIAVjJHnpUtjSHQP8GzWSZUelPqhiauCibibNjbKOMsGkL3MA/0?wx_fmt=png)

洞源实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs7HiaU1TeSL6QyZuasLpGExfp2m8lBgbIIAVjJHnpUtjSHQP8GzWSZUelPqhiauCibibNjbKOMsGkL3MA/0?wx_fmt=png)

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