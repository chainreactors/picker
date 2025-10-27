---
title: 当风云卫拥抱DeepSeek发生了哪些？（三）LSAS助力DeepSeek迈过“合规”这道坎
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247498379&idx=1&sn=b4cb12ab2565c5e18788f5848d3edf46&chksm=e84c5c54df3bd54231538d7218b7add9ebc3552b59d49635ea7a3dca4639e194d15e7511a780&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2025-02-20
fetch_date: 2025-10-06T20:35:46.909452
---

# 当风云卫拥抱DeepSeek发生了哪些？（三）LSAS助力DeepSeek迈过“合规”这道坎

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6qmTxSmTQUXbuLicf589PjMjodzw3Dn69YKqqZsrhEvVZrAtlSaIOL8A/0?wx_fmt=jpeg)

# 当风云卫拥抱DeepSeek发生了哪些？（三）LSAS助力DeepSeek迈过“合规”这道坎

原创

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6gzEVe2e8iaXomQOEX3l3HK6KryCjHwaibP365wriaXNxVGcSsn92TIHSQ/640?wx_fmt=gif&from=appmsg)

一.  前言

国产DeepSeek开源大模型凭借一系列突破性技术创新和卓越性能，迅速引发全球科技界的高度关注。微软、英伟达、亚马逊等科技巨头纷纷部署该模型，并向用户提供访问渠道。DeepSeek应用曾一度登顶苹果和谷歌商店全球下载榜首，覆盖140个市场并持续领先。DeepSeek开源策略成功吸引全球开发者参与生态建设，共同推动技术创新和行业发展。

然而，在吸引全球目光的同时，DeepSeek的合规性问题也受到了多个国家和政府机构的质疑。出于对国家安全和用户数据隐私的考量，意大利、韩国等国相继宣布禁用或限制DeepSeek的使用，并要求其解释用户数据的存储和处理方式，以确认其是否符合当地法律规定。此外，部分国家和机构对DeepSeek在道德伦理、隐私保护和安全防护等方面的合规性表示担忧。DeepSeek技术全球化进程面临严峻的合规性争议（如表1所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6ZsCC7Yk6uWGe24hyXNs7x4xnMk7r19xDGo7YmQyTU6jAhL2U3TW7QQ/640?wx_fmt=png&from=appmsg)

表1：各地区对DeepSeek的禁用情况统计 [1]

针对DeepSeek大模型在各国的合规性争议，绿盟大模型安全评估系统LSAS (NSFOCUS LLMs Security Assessment System)进行了升级，支持基于不同国家的大模型相关规范要求对待测大模型进行系统性的合规评估，以准确把控大模型服务和应用的安全合规情况。本文基于LSAS详细评估了DeepSeek系列模型对于中国《生成式人工智能服务安全基本要求》（TC260-003）标准的合规现状，并为DeepSeek本地部署的用户提供了切实的合规性建议，助力大模型在国内市场的合规落地。

二.  DeepSeek模型的TC260合规性评估方案

2.1

评估方法和工具

绿盟科技于2024年推出大模型安全评估系统LSAS (NSFOCUS LLMs Security Assessment System)，旨在为云端及本地部署的大模型提供自动化、系统化的安全与合规评估。在先前的文章中我们针对LLM内容安全、信息泄露安全、护栏构建与防护等方向已有深入研究**（****详情可见文章底部“往期回顾”）**。为应对DeepSeek大模型在各国的合规性争议，绿盟科技对LSAS进行了两方面升级：

**全流程自动化：**实现了不同标准规范文件的解读、评估指标生成和结果分析的全流程自动化，从而显著提升了大模型合规评估的效率和准确性。

**多国标准支持：**全面衡量不同国家大模型安全相关标准规范的合规性，为大模型在不同国家落地应用提供安全可靠的参考。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZyBwWzsa5Y40Dffacf4nUibr2uiaxZGolMiaP4E97r2OaSB3yjGtdicyqUy04S93M5gPWGOyFxdTDAAg/640?wx_fmt=png&from=appmsg)

图1： TC260-003合规评估的LSAS截图

LSAS是一套全流程自动化的大模型合规评估系统，其核心引擎为风云卫NSFGPT大模型（以下简称风云卫）。该系统依据各国不同的标准法规文件（如表2）生成评估方案，涵盖评估维度和指标，并结合测试例种子库与测试例构造器，形成与评估方案匹配的测试数据集。最终，由云端模型评估服务执行测试，并通过大模型对测试结果进行符合性评估，生成合规性评估报告。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6sicpsPIK2ZhXib1xrYIWBo6HekBarDgNxoJqVicaW6XHrgOn0pGCowVXg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6IRYqibWcuqK0iaF0PMu1fkqAYtFbvHxIu2FwssVIe3WOyHvjG45cZ7RQ/640?wx_fmt=png&from=appmsg)

表2：全球大模型安全相关法律法规列表

2.2

评估范围说明

本次评估选取《生成式人工智能服务安全基本要求》（TC260-003）标准文件（以下简称标准文件），规定了生成式人工智能服务在安全方面的基本要求。

LSAS对标准文件进行深入解读并生成评估方案，覆盖其中5大类共计31种安全风险，涵盖第5章至第9章的所有条款，包括语料安全、模型安全、安全措施、其他要求及安全评估要求等五个方面，并针对每个条款单独设立评估项。

本次评估选取了标准文件中支持自动化评估的三个核心评估维度（如表3所示）：生成内容安全评估、应拒答评估、非拒答评估。依据标准文件对测试例总数及各子分类测试例数量的要求，构造并扩充相关测试例，最终抽取5909个测试例数据集用于本次评估，以确保评估的全面性、科学性与合规性。

**1. 在生成内容安全维度**，测试例覆盖了共31种安全风险，测试例数据总数2145个。

**2. 在应拒答维度**，测试例覆盖了１７种安全风险，测试例数量2172个，测试待评估模型生成内容中是否包含违反社会主义核心价值观的内容、歧视性内容、商业违法违规、侵犯他人合法权益、无法满足特定服务类型的安全需求等。

**3. 在非拒答维度**，围绕模型不应拒答的问题生成非拒答测试例数据，测试例规模1592个，覆盖我国制度、信仰、形象、文化、习俗、民族、地理、历史、英烈等方面，以及性别、年龄、职业、健康等方面。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6Xia2OicI4ApqD2C3nC7tq5mPpTdF4oTjN1RfLaCXefvTkToccLUKlv5Q/640?wx_fmt=png&from=appmsg)

表3：三个评估维度

2.3

评估对象说明

待评估大模型（如表4）为四个：云端服务大模型：DeepSeek-V3和DeepSeek-R1，本地私有化部署大模型：蒸馏模型DeepSeek-R1-Distill-Llama-70B和原版Meta-Llama-3.1-70B-Instruct。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6Xia2OicI4ApqD2C3nC7tq5mPpTdF4oTjN1RfLaCXefvTkToccLUKlv5Q/640?wx_fmt=png&from=appmsg)

表4：四个待评估模型

三.  DeepSeek模型的TC260合规性评估结果分析

**下面对本次LSAS测试结果进行深入分析，总结以下五个评估结论：**

3.1

评估结论１：云端DeepSeek-R1合规性最优，三个维度均符合TC260-003中的规范要求。本地私有化部署DeepSeek模型需加强安全防护措施，以确保合规。

如评估结果对比分析表（表5）所示，DeepSeek-R1的三项评估维度评估分数分别为0.99，0.95，0.98，均满足标准文件TC260-003的符合要求（0.90，0.95，0.95），在四个待测模型中合规性最优。

DeepSeek-V3与DeepSeek-R1-Distill-Llama-70B在应拒答评估分，分别低于标准文件TC260-003要求的34.29%，14.29%，存在被滥用的可能性。

Meta-Llama-3.1-70B-Instruct（分数1.00,0.70,0.89）在生成内容安全评估中合规（高于标准10%），但没有通过应拒答与非拒答评估（低于标准25%，5.9%）。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs65zb9VvYkTmSWI71o5FJzU7QAOXv8tsdn4ulM8mhlyKEohXXoalfGpQ/640?wx_fmt=png&from=appmsg)

表5：评估结果对比总表

总体测试结果表明，云端接入的大模型合规性优于本地私有化部署。

云端接入合规性主要归因于云平台提供的安全工具和服务，能够更好地保障大模型的安全性和合规性。绿盟对云端API接入测试过程中还发现，各家API速度、稳定性，和云安全防护水平存在显著差异。

本地私有化部署DeepSeek模型，虽然可以避免数据在网络传输中带来安全风险，但是为了确保满足TC260-003合规性要求，企业仍有必要考虑并实施有效的安全防护措施。绿盟在测试过程中发现了众多暴露在互联网上的 Ollama 11434 端口，而且最近也曾爆出Ollama启动DeepSeek本地大模型可能存在安全隐患的消息，说明本地部署模型依然存在风险。

3.2

评估结论２：深度思考在处理多任务可能存在处理不当，DeepSeek-R1需要加强对于生成内容的审核过滤。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6QvjI6Rnbf4p2JWUz5SpibOtbgNS0Z6icM4MS93Bibib9sbrU1Rr8lOTD6g/640?wx_fmt=png&from=appmsg)

图2：DeepSeek-R1在侵犯他人权益方面存在问题

评估报告（图2）显示DeepSeek-R1生成内容安全评估总分超出TC260-003的符合要求，但细分在侵犯他人权益方面分数0.97，存在生成内容不安全风险。在网页端对不符合的测试例进行复现验证（如图3所示），最终模型的输出确实使用了侮辱性语气，加入了一些网络用语或脏话，并且给出了侵犯他人权益的非法建议。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6zpXaYEPlR70OSCXhZeH2wDO3yRHZK8MVLE7Y4FQy3r7l1fqV9vsrZA/640?wx_fmt=png&from=appmsg)

图3：DeepSeek-R1侵犯他人权益示例

对上述不合规结果进行了原因分析：通过观察DeepSeek-R1的深度思考过程（图4），可以看出其在处理用户问题时识别到了其中涉及的违法行为，例如故意损坏他人财物的行为属于违法范畴。然而，为了在不违反规定的情况下进行回应，同时保持设定的对话风格，模型在输出中仍使用了带有侮辱性语气的表达，并加入了一些网络用语或不恰当的词汇，最终生成了不合规的非法建议。对此现象，可能存在以下原因：

**1、训练数据偏差**：模型训练数据中可能包含网络用语和攻击性语言，使得模型在生成回复时容易偏向这些表达方式。

**2、多任务思考不当**：在处理风格保持和内容安全等多个任务时，模型可能未能合理设置优先级，也可能道德约束机制可能存在漏洞，从而模型可能在风格和合规之间未能找到合适的平衡点，导致输出中包含非法建议。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6mJWtB09q5JUTALCMKbarrOiavTXEMdMkwpzKvHXwiaftulcPu5u67W9g/640?wx_fmt=png&from=appmsg)

图4：深度思考过程

因此，建议企业级用户在应用模型时，应结合自身业务场景，配套实施内容审核和过滤机制，对模型生成的内容进行进一步审查与评估。企业不应过度依赖模型自身的安全性，而应建立完善的合规审查流程，确保输出内容符合法律法规及业务规范要求，从而降低潜在风险。

3.3

评估结论３：在应拒答维度，深度思考能力降低了DeepSeek-R1模型及Ｒ1蒸馏模型生成内容被滥用的风险。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6Kw6cJPEun2YibX7n5nxJ2CNytZHbXK4o845IicE21URUnYtFScus3SWg/640?wx_fmt=png&from=appmsg)

图5：应拒答评估风险对比

在应拒答维度的17种安全风险评估结果显示（图5）:与DeepSeek-V3相比，DeepSeek-R1模型的应拒答准确率提升了35%。同时，相较于原版Meta-Llama-3.1-70B-Instruct，蒸馏模型DeepSeek-R1-Distill-Llama-70B在对抗性测试集上的拒答准确率提升了11%。

经过分析，形成上述结果的可能原因有：深度思考有能力仔细分析请求的合理性和合法性，考虑用户的目的，并评估遵守这个请求的风险。如下例子所示（图6、图7），DeepSeek-R1测试例子通过思考推理如果按照用户的要求生成文件，会传播错误信息，违反政策，并可能导致法律后果，所以直接进行拒答。而DeepSeek-V3并没有深度思考能力，其按照请求生成了一份官方文件格式的文本，直接给出了涉及职业歧视的输出内容。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6zRiamIqW9Y7WUsbZ5YciaqpVvBD4mViciaewTtDYzvQt7eMNHAibwP54QVg/640?wx_fmt=png&from=appmsg)

图6：DeepSeek-R1拒答职业歧视问题

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs61TUwMN5z53a0icgRNy517GXBKJO9iagqdUARNy6bQRTffXibJnrYajqpQ/640?wx_fmt=png&from=appmsg)

图7：DeepSeek-V3未能拒答职业歧视问题

除此之外，根据实验结果，基于DeepSeek-R1蒸馏的模型DeepSeek-R1-Distill-Llama-70B相比原版Meta-Llama-3.1-70B-Instruct，在拒答能力判断方面也表现出显著提升。这一改进主要得益于R1蒸馏过程赋予模型更强的深度思考能力，使其能够更全面地评估请求所对应生成内容的潜在风险，从而在识别拒答问题方面表现更优，因此进一步说明了深度思考能力对于模型识别拒答能力的提升。

3.4

评估结论4：DeepSeek-R1安全策略的泛化可能导致过度防御，即为了防止潜在风险而过度拒答。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6SickI9cFMiaSTr9t1H8LSzN0Fu6LtVTqh7vRXgB5ibvkm47RjRV0WaTMQ/640?wx_fmt=png&from=appmsg)

图8：DeepSeek-R1存在误拒答情况

如图8所示，在非拒答维度的评估中，DeepSeek-R1相较于DeepSeek-V3的非拒答评估得分低1.6%。这一结果表明，DeepSeek-R1在部分本应予以回答的用户问题上出现了误拒答的情况。如图9所示，DeepSeek-R1未能正面回答关于“唐宋时期跪拜礼的区别”，并反复强调社会主义核心价值观。对此现象，可能的原因是：

**1、问题敏感性误判**：用户问题被模型判定为涉及文化偏见或歧视，触发了安全策略。DeepSeek-R1具备更强的深度思考能力，会从多个维度分析问题，并对生成内容施加更严格的限制，导致出现拒答情况。

**2、可用性与风险规避的权衡**：DeepSeek-R1的安全策略可能过于谨慎，为了避免潜在风险，牺牲了一部分可用性。在某些非敏感场景中，可能将正常问题误判为高风险问题，从而影响用户体验和模型的实际可用性。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYJCBJHnmInG8Hb4lIaPHs6oBMhoKeomqH22pM6LUgcBEQ3tECf9A4N9yicV1JRb03kSqkyt8mdicnA/640?wx_fmt=png&from=appmsg)

图9：非拒答测试未通过示例

在此我们建议，企业应当在不同的应用场景中选择最合适的模型，把握安全性与信息可用性的平衡。具体建议如下:

**1、安全性优先**：如果业务场景强调安全性，例如政府、法律或金融行业，建议选择DeepSeek-R1。这一模型在处理敏感信息时更为稳妥，能够有效避免不当回答。

**2、信息准确性与可用性**：在需要确保信息准确性和可用性的场景，如教育、历史研究或内容创作，DeepSeek-V3可能更为合适。该模型在提供丰富和准确的信息方面表现优异。

**3、优化提示词**：企业可以通过优化提示词来减少误拒答的情况。建议使用清晰、具体的语言，避免模糊表达，以明确问题意图。这将有助于降低模型过度触发安全机制的概率，从而提高交互的有效性。

3.5

评估结论５：DeepSeek-R1-Distill-Llama-70B存在中文知识不足的问题。在面对国内应用场景时，其表现不如DeepSeek自研模型。

DeepSeek-R1-Distill-Llama-70B本质上是基于Llama-70B模型的蒸馏，受其预训练数据影响，在面对国内应用场景时，其表现不如DeepSeek自研模型V3与R1。

如图10的评估测试结果所示，DeepSeek-V3和DeepSeek-R1在涉及中国特色社会主义核心价值观的问题回答中展现出了较高的专业性。若触发拒答机制，模型通常采用类似中国官方...