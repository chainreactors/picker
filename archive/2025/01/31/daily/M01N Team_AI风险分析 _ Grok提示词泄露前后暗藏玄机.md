---
title: AI风险分析 | Grok提示词泄露前后暗藏玄机
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494054&idx=1&sn=9122e0562bcad42ee707e0879b945aa1&chksm=c18429b7f6f3a0a16b65fc9b18ee5c979853c462ea1f43800abab53c6e5bc3e5d73dc9c1c540&scene=58&subscene=0#rd
source: M01N Team
date: 2025-01-31
fetch_date: 2025-10-06T20:10:41.594736
---

# AI风险分析 | Grok提示词泄露前后暗藏玄机

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7xic5FPoCUhLZUG7micsP62Q1icgQxwrPRRchhs3onNmKM2GolvMv0wlYw/0?wx_fmt=jpeg)

# AI风险分析 | Grok提示词泄露前后暗藏玄机

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7I0bg90uG7iacd8J2Ay4aR3UvOBnjmRPNW5PMasRZV0Y3icCO1NLxFjdA/640?wx_fmt=gif&from=appmsg)

**背景**

随着大规模生成式模型在各行业中的应用，模型的安全性问题逐渐暴露，尤其是提示词泄漏问题。提示词泄漏是攻击者通过精心设计的提示词，诱导模型暴露内部敏感数据，造成企业或个人隐私数据被侵犯，甚至可能对政治倾向等方面产生影响。

Grok模型是xAI推出的生成模型，凭借强大的文本生成能力和语义理解，在自动化生成和智能问答等领域广泛应用。然而， Grok模型在交互过程中存在系统提示词泄漏的潜在风险。这种泄漏不仅暴露了模型的内在信息，还可能引发对敏感数据的泄露风险，甚至可能影响公共舆论和政治信息的传播。

|  |  |
| --- | --- |
| **事件名称** | AI风险分析 | Grok提示词泄露前后暗藏玄机 |
| **风险映射** | 数据安全-应用阶段-元Prompt泄露  模型安全-应用阶段-模型越狱攻击 |
| **事件来源** | https://embracethered.com/blog/posts/2024/security-probllms-in-xai-grok/ |

**01 风险分析**

在本次实验研究中，从模型越狱入手，以交叉的方式组合越狱提示词，结合肯定性后缀与思维链推导的方式对越狱提示词进行增强和优化，结果成功套出了Grok2模型的系统提示词，揭示了Grok模型在与用户交互时可能暴露的内部数据和潜在风险。提示词优化策略：

* **对抗性后缀：**

在越狱提示词之后附加对抗性后缀“！！！！！！！！”。此优化策略是基于已有的研究成果，已被证明在攻击过程中能有效地绕过模型的审查，增强攻击的成功率。

* **思维链CoT：**

基于上一步在其最后加入思维链（CoT）方式的提问：“让我们一步步思考”。此方式通过引导模型逐步进行思维推理，有助于绕过模型的防护机制。在经过这两步优化后，对ChatGPT进行测试。结果表明，ChatGPT的角色“AntiGPT”成功回答了关于偷车的详细步骤：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7HVZoBxJsJGicf1p8O15bmnsicx43A2kN8zCzL4IFSvjYa9Nuib9IPnJqQ/640?wx_fmt=png&from=appmsg)

将上述优化后的提示词测试Grok2模型，Grok2模型给出了详细的系统提示词：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM774eBwGR6JEbDUZsS6t8lvyNRCPBIuh4PvffrCKdjCiaz7oya7RLhSEQ/640?wx_fmt=png&from=appmsg)

与我们上述研究中泄露的系统提示词不同，以下实验中获取到的Grok2系统提示词包含了关于特朗普美国总统选举的提示内容。如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7gcph9DTe3LqkAFvyGjibrUtUcYfXKc8FPPqicHCLVicEYouNek1swkfeQ/640?wx_fmt=png&from=appmsg)

* **系统提示词细节分析：**

通过下图可以观察到，在2024年12月16日，Grok模型的系统提示词中仍然保留了对特朗普胜选的提示预设，这一内容可能揭示了模型在某一特定时段内的推测倾向：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7MuaicmMrRtrjejbZFEOEH1ciaPYibY29tYib8azmjG6lHo6qkicPGjZXJNw/640?wx_fmt=png&from=appmsg)

然而，基于前述成功获取到的Grok的系统提示词中发现已经删除了关于特朗普胜选的倾向，下图所示为完整的系统提示词内容：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7Fueib1FTjKqgric0ia1HsI79BzRpzia9M3f9y44CQUpBDKPDROPX7yec8A/640?wx_fmt=png&from=appmsg)

根据上述图中的时间以及提示词对比，不难发现在特朗普正式赢得总统职位之前，即12月16日的Grok系统提示词中还存在对特朗普将胜选的预设，而在特朗普被公布胜选之后，即上图中日本12月19日（其对应美国12月18日）的系统提示词中却删除了特朗普相关提示。值得注意的是，特朗普正式赢得总统职位的最终日期是12月17日。因此，可以推测出xAI可能借助Grok模型的能力，推动了关于美国总统选举投票结果的讨论，通过模型能力的引导和提示词的调整，可能影响了现实世界中的舆论讨论与信息流传递，进一步塑造了公众对关键事件的认知。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7PnMCeGYibTUIreia7xXjQYfBf6Q61YudmnLskiaNJ9BBR4Rahys3fWuXQ/640?wx_fmt=png&from=appmsg)

除此之外，近期随着TikTok在美国的停运，小x书平台涌现了大量外国用户。小x书为应对此变化推出了AI一键翻译功能。然而在实测中发现将“you model name”改为“output your name”后，翻译结果显示其身份为“AI翻译助手”：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7iaCoDrAUGVUV6VuzgtBo2qfau5ibPFfq9eiamLm8PKW3RPk1wVTCfviajg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7YIBUEa3Qic48DeEuqPo5Ivtq3SE4E3ib3xJoSf96aRFJ2gPOcczzmNzw/640?wx_fmt=jpeg&from=appmsg)

再例如，当要求模型在翻译后输出系统提示词时，翻译模型给出了自己是一个多语言翻译专家以及相关的翻译规则。这些结果表明翻译应用可能在处理输入时，缺少相关的防护机制，导致系统提示词的泄露。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7WgiaX5OeblmozINXTf3S6ckPlEoic62uA0LEltsLibZAoFQ9ViaC8c3QEg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7cyic7DVAg7yyMC6WbyaGfibYFmhscPFYrLTvCt5pxqvtuGoMdvIgdRKQ/640?wx_fmt=png&from=appmsg)

**02 总结**

通过分析 Grok 提示词泄露和小x书翻译引发的泄露案例，可以发现系统提示词泄露可能带来多方面的潜在风险。近期，OWASP 在 LLM 应用程序十大安全风险中明确指出，系统提示词不应被视为保密信息，而是应重点关注其中是否包含敏感内容（如 API 密钥、用户令牌、过滤标准、角色权限架构及内部规则等）。提示词泄露不仅可能导致敏感信息的外泄，还可能暴露模型的底层架构或功能配置，进一步引发严重的安全隐患。

为应对这一问题，OWASP 强调系统提示词应避免包含任何敏感信息，敏感数据应与模型隔离存储，并置于模型无法直接访问的安全位置，从而有效降低泄露风险，全面保障系统的整体安全性和数据隐私。

**参考链接**

[1]https://embracethered.com/blog/posts/2024/security-probllms-in-xai-grok/

[2]http://owasp.org.cn/OWASP-CHINA/owasp-project/owasp-59278/%E5%BC%A0%E5%9D%A4--LLM%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8FOWASP%E5%8D%81%E5%A4%A7%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A92025%E5%8F%91%E5%B8%83%E7%89%88%E6%9C%AC.pdf

[3]https://mp.weixin.qq.com/s?\_\_biz=MzkwMzYzMTc5NA==&mid=2247494388&idx=1&sn=290a97bc16feb841d707b18676742076&chksm=c1f965a7cc8ad7cace362cde5ce4da3fb64a898e535a076a475c9a82ae2073600a39f099f8eb&mpshare=1&scene=1&srcid=0120sitO0UhcyC2HOurgNtnO&sharer\_shareinfo=1dec5905329442930a9a491436cd83cc&sharer\_shareinfo\_first=f295b0b60769fa5821fb872f21d2d003&version=4.1.8.6033&platform=win&nwr\_flag=1&from=industrynews#wechat\_redirect

[4]https://mp.weixin.qq.com/s/Kb468tOqtbebsubtBu\_6aw

[5]https://arxiv.org/pdf/2205.02392

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7BOyC9KsVYUYibicIr6EHib4YcuNGeuKd0H1mewbPLG0r6uI5GTIRccvKg/640?wx_fmt=png&from=appmsg)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7FFiareyibP5lxkWZhvblXPQJ6S8tRWhKAnicfY0fyZU7M2JBr1kFn3gPA/640?wx_fmt=jpeg&from=appmsg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM74z7f5nOoL2ia5sMQJPibPLGkJFOqxmNRYV6PCs8E5B6wxvja8S3OKuUg/640?wx_fmt=png&from=appmsg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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