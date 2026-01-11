---
title: 奇安信高校联合4篇研究成果被国际顶级会议NDSS 2026录用
url: https://mp.weixin.qq.com/s/lQhN5nEBaOIq2W1P2DgHYQ
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:38:35.168908
---

# 奇安信高校联合4篇研究成果被国际顶级会议NDSS 2026录用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsNibRVByCFr9z8icLB9YSrlVG1qRJk5cqWqtOpuibxUsH3Ikib6mUtugRPLEN47IJMPezPWqYAB88ibcEBA/0?wx_fmt=jpeg)

# 奇安信高校联合4篇研究成果被国际顶级会议NDSS 2026录用

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

近日，国际顶级学术会议 NDSS 2026（Network and Distributed System Security Symposium）公布录用结果，**奇安信技术研究院合作完成的4篇论文成功被录用**。NDSS 2026将于2026年2月23日至27日在美国圣地亚哥举办。此次多篇论文被录用，充分展现了奇安信技术研究院在网络安全前沿技术研究领域的深厚实力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lG0evzxL96mR253xzN6ySPPg7ia4QaKVezmTOJ34xOaFALa4GKvibyRBicTEBFwGKzwDTic21EeV6jPPnofxzEBdAg/640?wx_fmt=jpeg&from=appmsg)

**LLM推理服务框架中的缓存安全问题**

第一篇论文是由奇安信技术研究院、中国海洋大学和清华大学联合完成的AI安全研究工作，论文题目为《**Cache Me, Catch You: Cache Related Security Threats in LLM Serving Frameworks**》。这项工作由中国海洋大学和奇安信联合培养的硕士研究生吴祥凡在奇安信技术研究院联培期间主导完成，导师为应凌云博士（奇安信星图实验室）和曲海鹏教授（中国海洋大学），其他作者为陈国强（奇安信星图实验室），谷雅聪（清华大学）。这项研究聚焦于大语言模型（LLM）推理服务框架中的安全威胁，深入分析了 KV Cache、多模态缓存及语义缓存 三大核心机制。

![fff35403180b1a398fee1655318bb5de.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsNibRVByCFr9z8icLB9YSrlVG19ITlhm1xDFOyIwWRSAicbialAlNY2Bsvd5Olpszf6sb4MEQx0lcjgp9g/640?wx_fmt=jpeg&from=appmsg)

这项工作揭示了上述机制中严重的安全隐患：攻击者可利用这些漏洞操纵模型输出，实施数据投毒，甚至绕过现有的安全审核与防御体系。团队在 vLLM、SGLang 和 GPTCache 等主流推理服务框架中定位到了具体的实现缺陷，并提出了针对性的修复方案。目前，相关漏洞已被厂商确认并修复，因此获得了 3 个 CVE 漏洞编号，为提升 LLM 基础设施的安全性做出了实质性贡献。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lG0evzxL96mR253xzN6ySPPg7ia4QaKVebYIrSJNQoPJTsPzAMW4SovNaIRiajpaIiaKX8XHEpia4iaGM61nGewdNRQ/640?wx_fmt=jpeg&from=appmsg)

**npm 生态漏洞传播影响分析**

第二篇论文是由奇安信技术研究院和清华大学合作完成的关于软件供应链安全的工作。论文题目为**《From Noise to Signal: Precisely Identify Affected Packages of Known Vulnerabilities in****npm****Ecosystem》**，作者为蒲应元（奇安信星图实验室）、应凌云（奇安信星图实验室）和谷雅聪（清华大学）。这项研究提出了基于函数调用关系的细粒度漏洞传播关系识别方法，结果表明传统的基于包依赖关系识别的漏洞影响结果中约 70% 都是误报。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lG0evzxL96mR253xzN6ySPPg7ia4QaKVerga7zZ5Ytqsnex0hOI5qlHPdSFsSRBzFcc3Z7zicxuLaMyXv28OPIgg/640?wx_fmt=jpeg&from=appmsg)

npm作为全球最大的开源软件生态，其错综复杂的依赖关系使得漏洞极易在供应链中传播，给软件安全带来巨大隐患。现有的包级别软件成分分析（SCA）工具普遍存在严重的误报问题，无法区分漏洞代码是否真实被调用，同时现有的函数级分析工具在面对大规模生态时，往往面临计算成本过高和对JavaScript动态特性支持不足等瓶颈。为解决这些问题，我们设计开发了 VulTracer，一款面向npm生态的高精度、可扩展的函数级漏洞传播分析框架。该工具创新性地提出了“一次分析，多次复用”的模块化分析模式，通过对每一个 npm 包构建不可变的富语义图（RSG）、提取形式化接口以及按需组合合成技术，成功解决了大规模静态分析中的性能与精度挑战。

同时，VulTracer基于全量npm生态（覆盖3400万个npm 包版本，超 9 亿条依赖关系）进行了迄今为止最大规模的函数级漏洞影响实证研究。实验结果表明，该工具在调用图构建上达到了0.905的F1分数（SOTA），相比`npm audit`降低了94%的误报率；同时研究结果进一步揭示，现有包级别分析工具产生的警报中 68.28% 均为“噪声”（即漏洞代码不可达），且真实的漏洞传播往往随依赖层级加深而迅速衰减。该工作为缓解开发者的警报疲劳提供了切实可行的技术路径，使安全修复工作能聚焦于真实存在的威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lG0evzxL96mR253xzN6ySPPg7ia4QaKVe4qkFzty3ciaNZG4BxxZa9DyxXhwJUfnPoGlmaymj8J27XhGIIXlEQfA/640?wx_fmt=jpeg&from=appmsg)

**JavaScript脚本的自动化反混淆**

第三篇论文是由奇安信技术研究院和北京邮电大学合作完成的关于JavaScript反混淆的工作。论文题目为**《From Obfuscated to Obvious: A Comprehensive JavaScript Deobfuscation Tool for Security Analysis》**，这项工作由北京邮电大学和奇安信联合培养的卓越工程师计划博士研究生周董超在奇安信技术研究院联培期间主导完成，导师为应凌云博士（奇安信星图实验室）和王东滨教授（北京邮电大学），参与该项工作的还有柴华君（奇安信星图实验室）。这篇论文也是我们继PowerPeeler (CCS 2024)和Invoke-Deobfuscation (DSN 2022)之后的又一项脚本反混淆工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lG0evzxL96mR253xzN6ySPPg7ia4QaKVeFDgpr2mEsGKib9XwI8yMmTjriaG4Co5iaMpUlOBXCibZKicMgl0ia4JTIW5A/640?wx_fmt=jpeg)

JavaScript作为互联网核心脚本语言的广泛应用，使其成为恶意攻击者的重要载体。攻击者利用复杂的代码混淆技术隐藏恶意行为，给安全分析带来严峻挑战。现有反混淆工具普遍存在处理复杂样本能力有限、仅支持特定混淆类型、输出代码难以阅读等关键局限。为解决这些问题，我们设计开发了JSIMPLIFIER，一款集成多阶段处理流程与大语言模型增强的综合性JavaScript反混淆工具。该工具创新性地结合代码预处理、静态AST分析与动态执行监控的双引擎协同，以及基于LLM的智能变量重命名，实现从复杂样本格式化到语义增强的全流程反混淆。JSIMPLIFIER基于44,421个真实混淆样本构建了目前最大规模数据集，实验证明其100%覆盖20种主流混淆技术，达到100%处理成功率和正确率，代码复杂度降低88.2%，可读性提升超过4倍。该工具已成功还原JSFireTruck等复杂恶意样本的混淆行为，相关研究成果、工具及数据集已开源共享。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lG0evzxL96mR253xzN6ySPPg7ia4QaKVeMk7OwHTNbxGMckMYEOO3s289ew7VE9f54txWRm6D5bZImkP3XKXAnw/640?wx_fmt=jpeg&from=appmsg)

**Windows 代码签名滥用分析**

第四篇论文是由奇安信技术研究院、清华大学和中关村实验室合作完成的关于代码签名滥用检测的工作。论文题目为《**Understanding the Status and Strategies of the Code Signing Abuse Ecosystem**》，这项工作由清华大学和奇安信联合培养的卓越工程师计划博士研究生赵汉卿主导完成，导师为段海新教授（清华大学）和应凌云博士（奇安信星图实验室）。其他作者分别为张一铭（清华大学）、张明明（中关村实验室）、刘保君（清华大学）、游子权（清华大学）、张书豪（奇安信星图实验室）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lG0evzxL96mR253xzN6ySPPg7ia4QaKVeGwWY44cRv1yOYHhibVB2LMxVGxRb5suS5ExgXp9r2qs098icwKicUoxfA/640?wx_fmt=jpeg&from=appmsg)

近年来，软件供应链安全事件频发，为了保护软件真实性与完整性，代码签名机制应运而生。代码签名主要依赖公钥基础设施 PKI 技术，旨在确保软件来自真实来源且软件内容未被篡改。然而，攻击者有时会反过来利用代码签名PKI信任体系中的安全缺陷，帮助恶意软件绕过操作系统和杀毒软件的检查。深入理解代码签名滥用生态系统的演变过程以及滥用者的策略，对于完善相关检测与防御机制至关重要。

在这项工作中，我们利用从真实世界中收集的 3,216,113 个已签名的恶意 PE 文件，对代码签名滥用行为进行了大规模测量。通过细粒度的代码签名滥用检测分类算法，我们检测到了 43,286 张滥用证书，构建了迄今为止最大的滥用标记数据集。分析发现当前代码签名滥用现象普遍存在，影响了 46 家 CA 厂商以及 114 个国家或地区的证书。我们发现了 5 种滥用者的攻击策略，并根据当前代码签名 PKI 存在的安全缺陷提出了若干缓解措施。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lG0evzxL96mR253xzN6ySPPg7ia4QaKVewibnHlqFGFwoicYFZUSDdzEXL25yOqYRJFaSj2sLrwSiaXHqrXDIt0Kbw/640?wx_fmt=jpeg&from=appmsg)

奇安信技术研究院是专注于网络空间安全相关技术的研究机构，聚焦网络空间安全领域基础性或前沿性的研究课题，结合国家和社会的实际需求，开展创新性和实践性的技术研究。共有星图实验室、羲和实验室和天工实验室三大实验室。

我们目前正在招聘，工作地点覆盖北京、南京、成都等城市，详情请参见：

https://research.qianxin.com/recruitment/

来源：奇安信技术研究院

![](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=other)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=other)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=other)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

信息网络安全杂志

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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