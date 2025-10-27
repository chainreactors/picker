---
title: 基于DeepSeek的智能化安全运营方案
url: https://mp.weixin.qq.com/s?__biz=MzAwNTgyODU3NQ==&mid=2651131303&idx=1&sn=b8fa5cf87508e20629cab3fa5bc3e50e&chksm=80e71717b7909e01c228b60918eb06f057209c7dc4ad43675072a4e4a9b83e6321ce272e73c9&scene=58&subscene=0#rd
source: 威努特安全网络
date: 2025-02-28
fetch_date: 2025-10-06T20:38:06.144623
---

# 基于DeepSeek的智能化安全运营方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45HOtFQQXCt4AjMQWiaH1GTXrUGBtDiaVeTvxb6dsGDPV0WS2ibh4s3vQZw/0?wx_fmt=jpeg)

# 基于DeepSeek的智能化安全运营方案

原创

石凌志

威努特安全网络

# ![](https://mmbiz.qpic.cn/mmbiz_gif/vEkwp3V9UttO1byVSbuod03z4vTwBZa0vVS7nrOUUlibUbNn1ovF2nB91AkwkHCVibGutqLqEZB0oNzHCUGqzzeQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

**Part.1**

**现状分析**

传统的安全运营模式依赖于大量安全专家的手动分析和响应。安全专家需要通过日志分析、威胁情报收集、漏洞扫描等手段，识别潜在的安全威胁并采取相应的防护措施。这种模式存在明显的局限性：安全专家短缺，许多企业，尤其是中小型企业，都缺少足够的安全专家来应对日益增长的安全威胁；响应速度慢，人工分析的响应速度较慢，面对复杂的网络攻击时，往往需要数小时甚至数天才能识别并响应威胁，这给了攻击者足够的时间进行破坏。

自ChatGPT诞生以来，如何将大语言模型应用到网络安全领域是行业关注的焦点，头部安全厂商纷纷发力AI安全的研究与落地，如何将AI能力深度融合于企业安全体系，已成为现在最具想象力的方向。因为ChatGPT的“闭源+海外”属性，大家在安全领域还不敢大刀阔斧地应用，国内的大语言模型整体能力与ChatGPT还是存在不小差距，所以安全领域的大语言模型应用还是处于探索研究阶段。

目前，大语言模型应用在安全领域的主要技术方案包括：

**1**

**微调（Fine-tuning）大语言模型**

**成为安全大模型**

微调是在已经预训练好的大语言模型基础上，使用新的、特定任务相关的数据集对模型进行进一步训练的过程。这种微调技术的主要目的是使模型能够适应新的、具体的任务或领域，而无需从头开始训练一个全新的模型。通过微调，能够增强通用模型在安全领域的理解和生成能力，在大模型的行业应用中有较好的效果。

**2**

**搭建安全知识库形成RAG系统**

RAG（Retrieval-Augmented Generation）是一种基于检索增强的生成技术，其核心思想是在生成文本之前，从外部知识库中检索与任务相关的知识，并将其作为输入的一部分，以提高生成文本的准确性和相关性。RAG无需重新训练整个模型，只需更新知识库即可实现知识的更新和扩展，从而适配安全领域的应用场景。

**3**

**定制智能体**（**Agent**）**与大模型交互**

Agent通过赋予软件实体自主性和交互性，使其能够智能、灵活地响应环境变化和用户需求。Agent根据内部状态和环境信息自主思考、规划并决定如何行动。使用Agent，可以实现安全问答之外的其他应用场景需求，响应安全告警事件，制定安全联动策略等。

大语言模型要在安全领域得到广泛应用，主要面临如下问题：

* 开源大语言模型相对ChatGPT 4能力较弱，国内的开源大语言模型相对来讲还有不小差距，无法有效指导安全运营；
* 国内安全厂商缺少AI人才，不能从根本上训练提升大语言模型在安全领域的能力，仅靠微调只能做少量优化；
* 大语言模型应用对硬件要求较高，大部分客户面临预算不足的问题。

2025年，**DeepSeek-V3的横空出世一举打破了这个现状。**目前大模型主流榜单中，DeepSeek-V3在开源模型中位列榜首，与世界上最先进的闭源模型不分伯仲。DeepSeek-R1在后训练阶段大规模使用了强化学习技术，在仅有极少标注数据的情况下，极大提升了模型推理能力。在数学、代码、自然语言推理等任务上，性能比肩OpenAI o1正式版。DeepSeek的另一个核心优势在于大幅度降低了对算力的要求，从而大幅降低了AI技术的使用成本和门槛。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If458rjQvgSXqEnPqSBq3srrvfgaa4jtsF5le1xEs8DbwRmo7HGcZm2stQ/640?wx_fmt=png&from=appmsg)

所以，DeepSeek为各个行业使用大模型进行AI增强打通了道路，后续AI+将成为各行各业的主要突破点。本文将重点介绍DeepSeek在安全运营方面的解决方案。

**Part.2**

**架构设计**

SASOC是威努特的态势感知与安全运营平台，集成了态势感知、策略管理、资产管理、日志管理等功能，我们将**在SASOC的基础上外挂大语言模型，实现智能化的安全运营方案。**

AI+SASOC的整体架构如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45fLCcicAlic5yoPehicl0eNeiayWuOxs08c0okkAZk0JWmulfLRgorItaeA/640?wx_fmt=png&from=appmsg)

**架构说明**

1. 安全运营平台SASOC负责管理安全设备和其他资产，包括工业防火墙TEG、监测审计SMA、主机卫士IEG等，支持策略配置、状态监控、日志分析、资产管理等功能。
2. 本地大脑包含DeepSeek大语言模型，配合本地知识库形成RAG应用，总体为SASOC提供AI能力；如果本地大脑的硬件能力足够强悍，可以同时支持为其他业务模块提供AI能力。采用本地大脑可以保证所有数据都留存在客户本地，能保证数据安全性。我们大部分的工业企业客户更适合采用这种方案。
3. 云端服务指通过互联网提供AI服务的DeepSeek或其他大语言模型，这类AI服务的基础能力更强，但是需要把数据上传到云端，所以不能保证数据安全性。对于更重视AI能力、不愿投入过大、对数据安全要求较低的客户，可以采用这种方式。客户可以选择云端服务或本地服务，都可以实现AI赋能安全运营。
4. 对接Agent负责通过API与安全大脑通信，利用大模型的AI能力，调用SASOC的设备控制能力，实现安全事件的及时响应。

**Part.3**

**模型选择**

DeepSeek发布了多套不同参数的大模型，实际能力也不相同，参数越多能力越强，相应的对硬件的要求也越高，即成本越高。所以，需要根据成本预算选择合适的大模型进行部署。

根据DeepSeek官网发布的性能测试结果，通过 DeepSeek-R1的输出蒸馏了6个小模型，其中Qwen-32B模型在多项能力上实现了对标OpenAI o1-mini的效果。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If4551BbG4TGXWicKRdicLb6ArUR27yNsv2f0BCDu7Bh07khQKHraDBUO3og/640?wx_fmt=png&from=appmsg)

根据DeepSeek提供的大模型的性能指标，结合这些大模型的硬件需求，综合分析如下表：

![](https://mmbiz.qpic.cn/mmbiz_jpg/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45Bs14n33jQQZMwXZfibGWI3YmNx7EvsTuSZlQypibiapicWNnGHlibicfUlSg/640?wx_fmt=jpeg&from=appmsg)

一般选择DeepSeek-R1-Distill-Qwen-32B及以上的大模型，可以初步满足我们的应用场景需求。对于一些大型央企等国家单位，建议部署70B及以上的大模型，可以提供更强的性能和能力。

**Part.4**

**部署DeepSeek**

目前，业界已经发布了不少大模型部署框架，包括Ollama、vLLM、Transformers、DeepSpeed等。这些框架大部分采用容器化思路，支持对大模型的综合管理，可以拉取、存储、运行大模型，方便开发者和研究人员用于快速测试和部署。

我们选择Ollama作为部署框架，这个框架易用性方面做得比较好，其官网为：https://ollama.ai。

安装Ollama后，可以直接使用命令行下载并运行DeepSeek大模型：

```
ollama run deepseek-r1:32b
```

如果你不想直接运行，也可以先下载模型，然后再运行，下载命令如下：

```
ollama pull deepseek-r1:32b
```

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45wBBLibWnLcjkGqGRHyrbD3IKBNAx5mOviaBMW8qhUCwx6PhBk9pWYHMg/640?wx_fmt=png&from=appmsg)

然后执行run指令后，大模型就运行起来了，这时就可以通过命令行与大模型进行对话了：

```
ollama run deepseek-r1:32b
```

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45QAlns6Ko2az3ca1aMSCeYeDp9vYV6mAaeORNpC8GmibTYb5wUEL6GNQ/640?wx_fmt=png&from=appmsg)

**Part.5**

**搭建本地知识库**

本地安全知识库的搭建依赖于RAG技术，我们采用RAGFlow系统来搭建本地知识库。RAGFlow提供了基于Docker的一体化方案。

首先，下载安装Docker（官网：https://www.docker.com/），然后下载安装RAGFlow软件（官网：https://ragflow.io/），通过Docker启动RAGFlow，具体细节大家可参考官网的使用指导，或查找互联网上的相关文章，本文不再详述。

启动RAGFlow后，就可以通过Web界面登录搭建知识库了。登录界面如下：

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45viat3nVMQuB5Eosc19Ov1pGnIKn3fwg7hM3ujBEokfCIeqJDvAmySXg/640?wx_fmt=png&from=appmsg)

登录以后，就可以开始搭建自己的知识库，主要界面为：

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45oaVct68icwKkM5TIIrGC43SsJVpZHdl4nWzw2mgymFIN1o5YeVgnAicQ/640?wx_fmt=png&from=appmsg)

点击右上角的“创建知识库”，就可以新建一个自己的知识库，首先为知识库配置基本信息：

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45WVSuq3VLOfkVSFwz9kuYXFhy4pwZJWU1ib4969tiakslC2XFAEfHTjSg/640?wx_fmt=png&from=appmsg)

然后点击数据集菜单，把本地的相关文件上传，主要支持上传文本文件、Word文件、Excel文件、PPT文件、PDF文件等格式的文件，注意PDF文件必须要支持文字拷贝识别，否则系统无法识别其中的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45bCWaKLttN4pJgCQRZlFaHdiaaic3NYBbl8ib092N9uVtwPcNd2ziasKMSw/640?wx_fmt=png&from=appmsg)

文件上传完成后，让其按默认规则解析保存即可。后续实际使用中可以再逐步细化知识库的解析规则。

然后进入“聊天”菜单，在开始聊天之前，需要先设置一下相关知识库和大语言模型，即让RAGFlow把相关的知识库和本地部署的DeepSeek关联起来。

这时，一个基本的具备本地知识库能力的AI聊天工具就搭建完成了，可以进行基于RAG技术的聊天了：

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If458kB0HUaGFHxu5YNUWhmpqjhlmkRbBxgiaww9uVsWQGFibKVMtf5FlIoA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45m2Gt1Q7IPYErDK0bcqPibJtoKnjEkCPm77VD7hTeWjgiaaFpRZr1EtuA/640?wx_fmt=png&from=appmsg)

**Part.6**

**SASOC+RAGFlow+DeepSeek**

上一节看到的知识问答系统是依赖于RAGFlow系统的管理界面，实际产品中，用户首先是登录SASOC系统进行安全运营，所以需要把SASOC和RAGFlow集成在一起，也就相当于把SASOC和DeepSeek集成了起来。

首先，我们来看一下RAGFlow和大语言模型交互的数据处理流程：

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If45b6RUDSRpLTicsDCDGAEFcXnibeDX0ibybXyR3gGDQzqojQmg4eSdKkXvQ/640?wx_fmt=png&from=appmsg)

根据上图分析，数据流程简述如下：

1. 上传的各个文档被分块处理，存入向量数据库；
2. 用户的输入问题，先经过LLM进行关键词抽取，然后从向量数据库查询相关知识；
3. 查询出来的相关知识块内容，再经过LLM总结处理，形成最终的答案。

SASOC和大语言模型集成，有2种不同的方案：

**简单方案**

松耦合方式，SASOC在Web界面里，嵌入RAGFlow的问答界面，用户可以直接在SASOC的界面上进行安全知识咨询。用户也可以把系统产生的告警信息拷贝粘贴到问答界面，就可以直接得到告警相关的分析描述和处理建议。这种方案中，AI作为安全专家给予指导，具体的工作由SASOC的用户进行手动处理。

**复杂方案**

紧耦合方式，SASOC中嵌入Agent，通过API直接和RAGFlow、DeepSeek进行深入交互，而不仅仅是知识问答。在SASOC上可以设计多种功能辅助调用AI能力完成智能化安全运营，包括：告警处置、策略联动、日志范化、资产识别、报告优化等。

比如告警智能处置，可以在界面直接点击AI助手（也可以后台自动执行），系统把告警相关信息按组织好的格式发给RAGFlow系统，查询出来的知识块再按预定的提示词模板发给DeepSeek，DeepSeek分析整理后按要求的模板输出JSON串，Agent接收解析JSON串，按计划交给SASOC展示，或者调用SASOC的其他功能，比如策略配置接口，直接和网络安全设备联动。最后SASOC把本次告警处置的相关信息发给Agent，Agent再将这些信息补充完善到知识库中，这样就完成了由DeepSeek配合知识库驱动的安全告警处理全过程。

告警智能处置的完整处理流程如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtsBKmtw4NDlusjvkeo9If451tvbIo5tUWt1HiacLMOfzqTT6XxE3cibG640ap8JqZcaaFKAmW2ZsdJA/640?wx_fmt=png&from=appmsg)

**Part.7**

**总  结**

在网络安全运营领域，一直受制于安全专家人力有限、人工分析响应较慢等限制，很多机构组织无法高效地进行安全运营，最后往往流于形式，遗留不少安全隐患。AI技术的快速发展为智能化安全运营提供了方向。DeepSeek及一系列相关工具的诞生，为AI技术的广泛应用铺好了道路。本文系统地讲解了威努特安全运营平台SASOC与DeepSeek的集成架构与实现方案，使用RAGFlow搭建本地的安全知识库，避免数据外发保证数据安全，由DeepSeek提供AI分析能力，完成了基于DeepSeek的智能化安全运营，并实际指导了DeepSeek和RAGFlow的安装部署，是DeepSeek应用在安全运营领域的有益探索。

最后，推荐大家选购威努特的DeepSeek一体机，详情请参考：[《威努特DeepSeek一体机：鲲鹏、海光、英特尔全覆盖》](https://mp.weixin.qq.com/s?__biz=MzAwNTgyODU3NQ==&mid=2651131223&idx=1&sn=4bb9e64b2f2f1f4ac43f72a76836546c&scene=21#wechat_redirect)。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttO1byVSbuod03z4vTwBZa0QPXxjXLFBAUUpkYOYz78KpuM3Lic13XvZSLwMRqwPWx2RcI41KF0fcw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_jpg/vEkwp3V9UtvKMyMOEIBicUdfszasytMDQ1WUymnSvTZuTib5nIYuzaqriabu2mxOyfz9n0qv5EicrxZjs0GjjQBpxA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)渠道合作咨询   田先生 15611262709

稿件合作   微信:shushu12121

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9Utvy3S0ykmxlskz7ythOsDsm6zNNibia3qASGEZwDcBXVAwThSasvpoWbn2NSVHiaFicF6G1G3HkrOarBA/0?wx_...