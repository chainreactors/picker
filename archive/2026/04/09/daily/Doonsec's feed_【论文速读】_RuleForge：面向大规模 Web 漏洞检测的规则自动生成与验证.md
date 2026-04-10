---
title: 【论文速读】|RuleForge：面向大规模 Web 漏洞检测的规则自动生成与验证
url: https://mp.weixin.qq.com/s/uky7CJGa8fFQy_G3y8pELA
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:44:29.136543
---

# 【论文速读】|RuleForge：面向大规模 Web 漏洞检测的规则自动生成与验证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PwkEAAy3OPU2IZU6HAEJYqNNUvOuhebsuNlojuGLD8Bb4f0CMXyENBJWN4Zl6nNERMduYf0Xa8DVYqAZnQqeAbCuMpAw9kFlPF1x23UTSGQ/0?wx_fmt=jpeg)

# 【论文速读】|RuleForge：面向大规模 Web 漏洞检测的规则自动生成与验证

原创

知识分享者
知识分享者

安全极客

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/vWuBpewLia8QmTLhv0jB8GS6Wtic69pG44V8Gib7ccD3FZolnOVkdOPafA3YULibw9S5AEkdO8sstRLGNFVDj7SgRg/640?wx_fmt=jpeg&from=appmsg)

**基本信息**

原文标题：RuleForge: Automated Generation and Validation for Web Vulnerability Detection at Scale

原文作者：Ayush Garg, Sophia Hager, Jacob Montiel, Aditya Tiwari, Michael Gentile, Zach Reavis, David Magnotti, Wayne Fullen

作者单位：Amazon Web Services（AWS）、Johns Hopkins University

关键词：漏洞检测、自动化规则生成、LLM-as-a-judge、Web安全、CVE缓解

原文链接：https://arxiv.org/abs/2604.01977

开源代码：暂无

**论文要点**

论文简介：安全团队每天都在与一场永无止境的"军备竞赛"搏斗——漏洞披露的速度早已超过人工编写检测规则的能力上限。2025年，美国国家漏洞数据库（NVD）新增了超过4.8万条漏洞记录，而AWS内部团队能够手动创建检测规则的高危漏洞数量，仅为NVD新增量的不到7%。面对这一巨大缺口，来自AWS的研究团队联合Johns Hopkins大学提出了RuleForge——一个能够从结构化Nuclei模板自动生成JSON格式Web漏洞检测规则的完整系统。

RuleForge的核心创新在于将大语言模型（LLM）引入安全规则生成的完整闭环：从CVE优先级筛选，到5×5并行候选规则生成，再到创新性的"LLM-as-a-Judge"置信度验证机制，最终通过人工复审进入生产部署。在2025年下半年的生产环境评估中，RuleForge实现了相比人工生成336%的生产力提升，同时将误报率降低了67%。这项工作不仅是一个工程实践的展示，更为整个网络安全领域如何在LLM应用中平衡自动化效率与精度要求提供了深刻的方法论参考。

研究目的：本研究的核心目标是填补"漏洞披露"与"检测规则部署"之间日益扩大的时间鸿沟。当一个高危CVE被公开时，攻击者可以立即利用它，而防守方往往需要数天乃至数周才能手工制作出对应的检测规则。RuleForge的设计目标是让这一过程实现自动化，在不牺牲精度的前提下，将规则生成的吞吐量提升到足以与NVD发布速度相匹配的水平。与此同时，研究团队还探索了两个扩展方向：如何从非结构化数据源（如博客文章、NVD描述）生成规则，以及如何通过Agentic工作流支持多事件类型的检测规则生成。

研究贡献：

本文的贡献可归纳为以下几个层面。

首先，研究团队设计并部署了完整的RuleForge生产系统，实现了从CVE到检测规则的端到端自动化流水线，在实际生产环境中验证了336%的生产力提升。

其次，提出了创新性的LLM-as-a-Judge置信度验证机制，通过将"敏感性"（避免漏报）与"特异性"（避免误报）两个维度分离评估，实现了AUROC 0.75的判别效果，并在生产环境中将误报率降低67%、无IP匹配规则减少71%。

第三，系统性地总结了LLM在网络安全任务中的关键应用教训，包括LLM过度自信问题的缓解策略、负向提示语设计的优越性，以及领域专家知识在提示工程中不可替代的作用。第四，探索并验证了非结构化数据规则生成的可行性（40%成功率），以及基于ReAct框架的多事件类型Agentic工作流概念验证。

**系统架构与设计**

RuleForge是一个运行在AWS基础设施上的自动化系统，其架构由四个相互协作的核心组件构成，共同完成从漏洞数据到生产就绪检测规则的全链路处理。

![](https://mmbiz.qpic.cn/mmbiz_png/PwkEAAy3OPUbTAQN3R1UJTSqqCm5da5qzIUoapBCia5j1KxriaRdAWpI2CVibDWhVb5yjoUI1Wdicp9zbib4cbcRK6wbQLmcSJQic8xdGvSV9U1Bw/640?wx_fmt=png&from=appmsg)

CVE仓库组件是整个流水线的数据入口。一个Lambda函数每周从Nuclei模板库拉取最新的CVE数据，并通过多维度的智能评分算法对漏洞进行优先级排序。评分维度涵盖内容分析（识别高影响力漏洞特征，如命令注入、SQL注入、身份绕过等）、实时威胁情报整合（CISA KEV目录、网络安全新闻订阅）以及组织内部相关性评估。高优先级的CVE元数据存储在DynamoDB中，完整模板归档于S3，为下游规则生成提供经过排序的结构化输入。这种智能过滤机制确保系统的计算资源优先聚焦于对企业环境威胁最大的漏洞，而非平均分配到所有披露的CVE上。

规则生成引擎运行在AWS Fargate上，通过Amazon Bedrock调用生成式AI能力，并采用DSPy框架管理LLM交互。对每个CVE，系统同时生成五个并行的候选规则，各候选规则使用不同的LLM温度参数（在0.7至0.9之间随机采样），从而探索多样化的检测思路。每个候选规则最多可经历五轮基于验证反馈的迭代优化。这种"5×5策略"的核心思想是：通过广度覆盖（五个并行候选）加深度精炼（每个最多五次迭代），大幅提升至少产出一条高质量规则的概率。

验证流水线由五个阶段组成，确保只有达到生产标准的规则才能进入部署环节。合成测试阶段生成10个测试用例（7个恶意请求、3个正常请求），要求候选规则在允许最多2个错误分类的前提下通过；LLM-as-a-Judge置信度评分阶段对规则进行敏感性与特异性的双维度量化评估；IP验证阶段将规则与高达50亿条真实Web流量记录进行比对，要求匹配的IP数量落在10至500之间，且恶意IP占比超过70%；IP信誉验证阶段调用包括MadPot在内的AWS内部和第三方威胁情报源；最终由安全工程师进行人工复审，确保领域专业知识参与最终决策。

反馈集成机制是RuleForge持续改进的核心引擎。系统同时捕获自动化验证失败产生的系统性反馈和人工复审产生的专家反馈，并将这些洞察重新注入规则生成过程。这形成了一个完整的学习闭环：每一次失败都是下一次生成的改进信号，使系统随着时间推移不断提升规则生成的质量和效率。

**CVE规则选择机制**

CVE规则选择组件在RuleForge流水线中扮演着关键的过滤器角色，其核心是一个多维度加权评分算法。内容分析维度通过关键词匹配识别高影响力漏洞特征，优先处理影响企业基础设施厂商的漏洞、企业应用中的远程代码执行（如命令注入和SQL注入），以及身份验证绕过机制；同时对低影响力的孤立插件问题施加负权重，减少噪声干扰。

威胁情报维度实时整合来自CISA KEV目录（已知被利用漏洞目录）和网络安全新闻订阅的信息，大幅提升已被确认在野利用或新兴威胁状态的CVE优先级分数。权重计算完成后，系统通过可配置的阈值过滤选择进入下游规则生成的CVE，并维护完整的审计日志记录选择决策和评分依据。这一智能过滤机制使RuleForge能够在安全覆盖率和运营效率之间取得最优平衡，将规则生成资源集中在对企业环境威胁最大的漏洞上。

**LLM-as-a-Judge置信度验证**

这是本文最核心的技术贡献，也是RuleForge区别于传统自动化安全系统的关键所在。传统的合成测试只能提供通过或失败的二元信号，却无法解释规则的哪个部分存在问题以及原因。为此，研究团队构建了一个LLM-as-a-Judge系统，通过设计两个精心措辞的评估问题来量化规则质量。

![](https://mmbiz.qpic.cn/mmbiz_png/PwkEAAy3OPWZoenGO0ib10kBIYbv48kIyCed1JwyicTzeiavKB90u4QUXXDgUFPehQJGtMBFnUVRxsUpMIib45j6TqcJ3ZibtpDOwcxG97uObRjw/640?wx_fmt=png&from=appmsg)

第一个问题考察规则漏报恶意请求的概率，等价于假阴性（False Negative）风险评估；第二个问题考察规则是否靶向了与漏洞相关但并非漏洞本身的特征，等价于假阳性（FalsePositive）风险评估。两个问题分别得到一个概率分数，取互补后得到敏感性分数（Sensitivity，衡量避免漏报的概率）和特异性分数（Specificity，衡量避免误报的概率）。将二者相乘得到综合置信度分数，并利用Claude 3.7 Sonnet的思维链推理能力输出详细的评估依据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PwkEAAy3OPVBIVOibqcuOvL6aHmj16VZ88lHRuOkHugQcQCoib0Kxu1ibqOo0Uv8iblOOOW8VWqUEKGT6HfLqL9KMy9sqx6zlE8quDicKibdptpfk/640?wx_fmt=png&from=appmsg)

在100个生成样本上，该系统实现了AUROC 0.75、ECE 0.17的评估性能，表明置信度分数具有相对良好的判别力和校准性。研究团队还对9条规则的LLM推理链与安全专家推理进行了人工比对，发现其中6条存在质量一致性——LLM能够识别出诸如"该SQL注入正则表达式过于宽泛，会匹配任何含单引号的查询参数，而不只是目标漏洞"这类与人类专家思路相近的缺陷。

当候选规则未能达到既定阈值（敏感性0.5、特异性0.7）时，系统会将对应的推理链作为反馈附加到下一轮生成提示中，指导LLM针对性地改进。这种机制在与50个CVE的对照实验中得到了充分验证：与仅使用合成测试的基线相比，加入LLM-as-a-Judge机制的增强版在保持相同真阳性检测量的同时，实现了误报数量降低67%、无IP匹配规则减少71%的显著提升。

**系统扩展探索**

除了已部署的核心流水线，研究团队还探索了两个具有战略价值的扩展方向，尽管它们目前仍处于概念验证阶段。

第一个扩展是从非结构化数据生成规则。生产版RuleForge依赖Nuclei模板作为输入，但在所有已记录的漏洞中，只有极小一部分被安全研究社区转换为Nuclei模板，这在覆盖范围上形成了明显瓶颈。为此，研究团队修改了系统以支持从博客文章、GitHub安全公告、NVD描述等非结构化来源生成规则。主要技术挑战包括：非结构化文本往往缺乏恶意HTTP请求的具体示例，需要系统从文字描述推断攻击模式；非结构化来源频繁包含与漏洞无关的干扰信息（网页导航元素、外链等）需要过滤；部分关键信息以截图或图表形式呈现，LLM无法直接处理。

研究团队在10个样本上进行了概念验证（8个来自NVD，1个来自GitHub公告，1个来自安全博客），系统为其中8个生成了规则，人工评估认为4个规则适用（可直接使用或仅需少量修改），总体成功率40%。规则被拒绝的最常见原因是目标漏洞本身不适合通过HTTP规则检测，这提示未来工作应着重提升系统在流程早期识别并拒绝此类不适用漏洞的能力。

第二个扩展是面向多事件类型的Agentic工作流。生产系统目前仅支持HTTP事件类型的规则生成，但实际的事件分类流水线还支持ProcessEvent、DnsEvent和CloudTrailEvent三种类型。研究团队基于DSPy框架实现了ReAct架构的概念验证，构建了包含规则生成器（HTTP/进程/云端三类专用生成器）、人工上报工具和放弃处理工具三类工具集的智能体。实验结果表明，该智能体能够正确处理各类场景：对于直接的HTTP漏洞执行单次工具调用并返回结果，对于不含有效漏洞的文档正确终止处理，对于初次生成失败的情况尝试备选生成器直至升级人工复审。这一架构的弹性在于，添加对新事件类型的支持仅需在工具集中增加对应工具并更新智能体签名描述，无需重新训练或微调模型。

**经验教训与深层洞察**

RuleForge的实践过程沉淀出三条对整个LLM安全应用领域具有普遍价值的关键经验。

第一，LLM在安全任务中存在系统性过度自信问题。当直接询问模型对自己生成结果的置信度时，LLM的回答惊人地一致——置信度最低也在0.7，最高仅0.9，缺乏有效的判别能力。这与学术界关于LLM在安全主题上校准性差的研究结论高度吻合。更重要的发现是，让LLM预测"规则存在问题的概率"比让它评估"规则是否正确"获得了更好的判别效果。结合文献中关于LLM过度自信和奉承性（sycophancy）的证据，研究团队总结出一条重要的提示工程原则：评估提示语的设计应让LLM扮演"批评者"角色主动寻找缺陷，而非让其判断某事物是否正确。

第二，领域专家知识在提示设计中不可或缺。LLM-as-a-Judge的成功不仅依赖于使用LLM进行评估这一思路本身，更根本的原因在于评估问题的设计充分借鉴了人类安全工程师在评审规则时的实际思考路径。使用泛化的通用置信度问题或泛化的FP/FN问题，系统表现显著退化（AUROC从0.75分别降至0.70和0.62）。这证明了领域专家知识对于构建有效评估提示语的关键作用，纯技术路径无法完全替代人类经验。

第三，多候选并行生成策略显著优于单候选方法。通过同时生成五个采用不同温度参数的候选规则，系统得以探索多样化的检测思路，大幅提升每个CVE至少产出一条高质量规则的概率。这种并行搜索与迭代精炼相结合的策略，为任何需要在质量与效率之间取得平衡的LLM生成任务提供了可借鉴的设计范式。

**论文结论**

RuleForge代表了网络安全自动化领域一次具有里程碑意义的实践探索。在面临漏洞披露速度远超人工响应能力这一根本挑战的背景下，该系统通过将生成式AI与系统性验证机制深度融合，在保持生产质量标准的同时实现了336%的规则生成效率提升。

系统的核心贡献——基于反馈驱动的LLM-as-a-Judge置信度验证机制——展示了一种用AI评估AI输出质量的有效范式。通过将敏感性与特异性分离评估，并将评估推理链作为下一轮生成的指导反馈，系统形成了一个自我强化的质量提升闭环，将误报率降低了67%，同时不牺牲任何真实威胁的检测能力。

展望未来，RuleForge的发展路径清晰：通过优化非结构化数据生成能力进一步扩大CVE覆盖范围，通过生产化部署Agentic工作流支持HTTP以外的事件类型检测，最终构建一个能够覆盖完整威胁谱的全自动漏洞缓解平台。这项工作传递的核心信念是：生成式AI能够以生产规模增强人类安全专家的能力，但前提是精度要求不能妥协——而这正是多阶段验证与人机协同的价值所在。对于整个网络安全和AI应用领域，RuleForge提供了一个宝贵的生产级案例：如何在LLM强大能力与安全关键系统的严苛要求之间，找到那条可行的平衡之路。

-End-

[![]()](https://mp.weixin.qq.com/s?__biz=MzkzNDUxOTk2Mw==&mid=2247495405&idx=1&sn=67249648d5c312b5c178b23b077d28f3&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8R7Rm0KL55HCcIiasO8JJ7IibXzYxx3losWVb2eddxdClACzWxWtQLwl0wkAl1ZLibcESVWvx5dCeibtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

*![图片](https://mmbiz.qpic.cn/mmbiz_gif/D9wGKNiaQYpx7bvaHqVZibq0ogu5pckjQMepnZgmhgM01uFQsoFz5QDDE0iapRkuUumSGfk8Dz7mjnbvibwPk7jISg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)*

![图片](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8QRqLMRicZIN6VJg0ue41W1HVSmDpDqkj86j5SNicNE3X5KkPgcdv1ZmxM7FXrFUdkBes8dpos7d27w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8SDzMyjUl8Lr0J0V4feAVeZ5eMLYibJKzJyVxRuoHpXEDLpGkGm6hQcBm7OyEu3EiclN8sNdPvWIWiaw/0?wx_fmt=png)

安全极客

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8SDzMyjUl8Lr0J0V4feAVeZ5eMLYibJKzJyVxRuoHpXEDLpGkGm6hQcBm7OyEu3EiclN8sNdPvWIWiaw/0?wx_fmt=png)

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