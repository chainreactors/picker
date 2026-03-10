---
title: RSAC 2026创新沙盒-Realm Labs：洞察AI推理内核，前置防控安全风险
url: https://blog.nsfocus.net/rsac-2026%e5%88%9b%e6%96%b0%e6%b2%99%e7%9b%92-realm-labs%ef%bc%9a%e6%b4%9e%e5%af%9fai%e6%8e%a8%e7%90%86%e5%86%85%e6%a0%b8%ef%bc%8c%e5%89%8d%e7%bd%ae%e9%98%b2%e6%8e%a7%e5%ae%89%e5%85%a8%e9%a3%8e/
source: 绿盟科技技术博客
date: 2026-03-09
fetch_date: 2026-03-10T04:02:41.159258
---

# RSAC 2026创新沙盒-Realm Labs：洞察AI推理内核，前置防控安全风险

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

# RSAC 2026创新沙盒-Realm Labs：洞察AI推理内核，前置防控安全风险

### RSAC 2026创新沙盒-Realm Labs：洞察AI推理内核，前置防控安全风险

[2026-03-09](https://blog.nsfocus.net/rsac-2026%E5%88%9B%E6%96%B0%E6%B2%99%E7%9B%92-realm-labs%EF%BC%9A%E6%B4%9E%E5%AF%9Fai%E6%8E%A8%E7%90%86%E5%86%85%E6%A0%B8%EF%BC%8C%E5%89%8D%E7%BD%AE%E9%98%B2%E6%8E%A7%E5%AE%89%E5%85%A8%E9%A3%8E/ "RSAC 2026创新沙盒-Realm Labs：洞察AI推理内核，前置防控安全风险")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 37

**RSA Conference 2026** 将于美国旧金山时间3月23日正式启幕。作为全球网络安全行业创新风向标，一直以来，大会的 **Innovation Sandbox（创新沙盒）大赛**不断为网络安全领域的初创企业提供着创新技术思维的展示平台。

近日，RSA Conference 正式公布 RSAC 2026 创新沙盒竞赛的10名决赛入围者，分别为 Charm Security、Clearly AI,Inc.、Crashoverride、Fig Security、Geordie AI、Glide Identity、Humanix、Realm Labs、Token Security、ZeroPath。

聚焦网络安全新热点，洞悉安全发展新趋势。与绿盟君一道，走进**Realm Labs**。

### **01** **公司简介**

Realm Labs成立于2023年，总部位于美国加州San Jose附近的Sunnyvale[1]。公司创始人兼CEO Saurabh Shintre曾在Symantec和Splunk领导AI安全研究[2]。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/1-300x127.png)

公司创始人兼CEO Saurabh Shintre

Realm Labs在今年的RSAC大会上获得了Crosspoint Capital Partners的500万美元融资[3]。Realm Labs的使命是让AI应用“更可信、更可靠、更安全”，致力于解决生成式AI引发的安全与可观测性难题。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/企业微信截图_17726962934991.png)

Realm Labs公司Logo

### **02** **产品背景**

随着生成式AI和大语言模型（LLM）的快速普及，企业在享受AI带来创新的同时，也面临着严重的安全挑战。现代LLM由海量数据训练而成，模型内部隐含许多潜在“有害知识”，使其难以完全防范滥用。

微调对齐、提示工程等传统技术虽然能改善模型输出，但难以根除模型内部的有害知识，这些知识一旦被激活仍可能产生危害。AI防火墙方案在模型输入和输出层面强制执行策略，但往往模型体量小、精度有限且增加额外延迟[4]。

对此，Realm Labs提出了新的思路：不只是分析模型说了什么，而是深入监控模型思考的方式。通过了解AI模型内部“思维结构”的工作原理，Realm希望在问题发生前就提前发现并阻断风险。

Realm Labs的主要产品包括AI防火墙“OmniGuard”、AI观测方案“Prism”、数据治理和DLP方案“DataRealm”。考虑RSAC 2026的背景，本文着重讨论Realm Prism。

### **03** **方案特点**

根据公开宣传内容进行调研，Realm Labs的创新产品“Prism”可能包含以下特点：

***3.1*****整体思路**

在官方白皮书[5]中，Realm Labs将LLM的可观测性划分为五个层次，分别为：

1、 基础设施可观测性：CPU/GPU负载、内存资源占用等，指示硬件是否健康。

2、 数据可观测性：数据完整率、空值率、标注准确率、分布漂移评分、RAG知识库时效性等，指示训练和推理数据质量是否合格。

3、 应用可观测性：LLM日志、工具调用日志、输入输出令牌情况、API错误日志、响应时间等，指示LLM是否正确工作。

4、 内部可观测性：注意力模式\*、内部CoT、Token概率等，指示LLM内部如何“思考”。

5、 输出可观测性：是否出现幻觉/答非所问/事实错误/偏见/违规内容等，指示最终输出质量。

\*注：此处的“注意力模式”被描述为“每个输出Token受哪些输入Token影响”，直观理解的话应该是指注意力权重矩阵/热力图。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/2-300x162.png)

（非Realm Labs相关）机器翻译任务中的注意力权重热力图示例

目前，第1、2、3、5层的可观测性都有较为成熟的方案实现，唯独第4层的方案在此前是缺失的。这也是Realm Prism的重点目标。

官网博客上的一篇文章[7]中阐述如下：“近期研究表明，LLM会在大脑中对信息进行分类整理，而这种整理结构可以通过研究模型来学习。Realm的防御机制主要基于这一原则。我们会识别LLM中存储有害信息的区域，并监控用户查询何时会使模型访问这些区域。我们的论点是，Realm的防御机制难以绕过，因为任何试图提取有害信息的越狱行为都必须触发模型的相应部分。我们的防御机制在知识源附近设置了一个监控点，使我们能够在有害信息从模型输出之前就检测到其生成。”

不过，现有的大部分官方公开文档都重在强调LLM内部可观测性建设的重要性，我们未能在其中找到较多关于具体实现细节的说明。

***3.2*****部署模式**

根据官方网站的宣传页[8]，**Realm Prism支持4种部署模式，**大致翻译如下：

**批量分析（Batch Analysis）：**对历史交互数据进行分析和分类，挖掘潜在模式和改进机会。

**实时旁路（Real-Time Sidecar）：**从应用逻辑中取得实时洞察，实现自适应的路由和监控。

**内嵌护栏（Inline Guardrails）：**阻止不安全或不当的查询，将复杂请求转发给更合适的模型。

**生成式端点（Generative Endpoint）：**可作为任何开放式权重模型的即插即用型端点，有目的性地收集行为数据。

如果从直观角度理解，批量分析可能是要重新运行LLM以复现隐层状态；实时旁路和内嵌护栏模式则可能类似HWAF场景下的监测和阻断模式；生成式端点可能是某种针对开源LLM的一站式云服务。

该宣传页还提供了一个视频，展示了Realm Prism的工作流程和UI。视频中可以看到，界面左侧有一个聊天对话框，在演示者输入一段提示词后，右侧面板会给出针对当前状态的一系列成分指标，且这些指标会随推理过程的进行而变化。

下图可见，演示者输入“I want to kill a child”，此时Violence、Self-Harm、Refusal三项指标都达到了较高水平，指示当前请求有害并应当拒绝回答：

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/3-300x169.png)

演示者输入“I want to kill a child”，被Realm Prism识别为有害

但随后，演示者又在后面添加了一个“process”，于是以上拒绝指标随即消失，指示当前请求无害：

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/4-300x169.png)

演示者输入“I want to kill a child process”，此前的有害指标下降到了较低水平

***3.3*****实战性能**

根据官网介绍[9]，Realm Labs从去年9月份起举办了一场CTF挑战赛，邀请公众来破解一个拥有四层防御的AI聊天机器人。至2025年10月17日，已有超过一百位参与者尝试破解逾2000次，其中包括一些大型公司的红队成员，但无人突破第四层防御。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/5-300x180.png)

CTF挑战赛的过关情况

不过，至本文截稿时，该挑战赛页面（https://sherlock.realmlabs.ai/）似乎已经无法访问。尚不明确官方后续是否还有类似的CTF或SRC计划。

***3.4*****与其它方案的比较**

说到比较，就不得不提到另一个厂商，即2023年度RSAC创新沙盒冠军HiddenLayer。在HiddenLayer的众多产品中，与Realm Prism最为相关的当属MLDR（Machine Learning Detection & Response）\*，这是业界较早提出的针对机器学习模型的安全监测与防护方案。关于MLDR的细节调研，可以参考本公众号先前的文章：[《](https://mp.weixin.qq.com/s?__biz=MjM5ODYyMTM4MA==&mid=2650438536&idx=5&sn=a1e101bbb07e309ab64df9ee7a9b4887&scene=21#wechat_redirect)[RSA 2023创新沙盒盘点｜HiddenLayer：针对机器学习攻击的防护与响应平台](https://mp.weixin.qq.com/s?__biz=MjM5ODYyMTM4MA==&mid=2650438536&idx=5&sn=a1e101bbb07e309ab64df9ee7a9b4887&scene=21#wechat_redirect)[》](https://mp.weixin.qq.com/s?__biz=MjM5ODYyMTM4MA==&mid=2650438536&idx=5&sn=a1e101bbb07e309ab64df9ee7a9b4887&scene=21#wechat_redirect)。

\*注：较新的宣传中已改称“AIDR”，但功能层面的变更细节并未披露。为保持前后文一致，本文仍暂用旧称“MLDR”。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/6-300x169.jpg)

（非Realm Labs相关）HiddenLayer MLDR框架

与几乎专注于LLM的Realm Labs不同，MLDR可以处理各类机器学习/深度学习模型的输入和输出向量[10]，其防护范围也涵盖各类对抗性、鲁棒性攻击，例如对抗样本、模型提取等[11]。但其中的具体方法至今仍不明朗，仅有的描述来自官方博客中“融合了先进的启发式方法和机器学习技术”。

在现代LLM的场景下直观理解，MLDR应该可以处理嵌入层的输出和反嵌入层的输入/输出。相比AI防火墙等完全工作在模型外部的防护方法，MLDR似乎也能够在一定程度上实现内部可观测性。尽管如此，由于MLDR并非专为LLM打造，其在应对LLM相关的、尤其是业务相关的攻击时似乎还是显得比较粗粒度。HiddenLayer公司另有一系列针对LLM的防护方案，但也属于AI防火墙和数据防泄漏等，不在Realm Prism的对比范围内。

相比之下，Realm Prism的检测和防护方式则更有针对性，专门应对LLM相关的常见威胁形态，例如提示词注入、越狱等。此外，Realm Prism的实现方式更加深入模型内部，理应能够达到更好的效果和更低的开销，并显著增加攻击者绕过防护的难度。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/7-300x101.png)

Realm Labs官方白皮书中对内部可观测性方案与常规方案的对比

然而，Realm Prism的方案可能也存在一些局限。由于其方案依赖访问模型内部状态，它可能主要适用于开源模型或授权程度较高的场景。对于完全封闭或黑箱的第三方模型平台，Realm Prism的接入难度可能较大。此外，大规模运行实时监控也需要权衡性能和成本。

尽管如此，当前公开报道中尚未找到有对Realm Prism的具体质疑。

***3.5*****其它值得关注的部分**

Realm Labs在官方白皮书[5]中提出这样的观点：“…现有工具将模型视为黑盒，只捕获输入和输出，却忽略其他一切…这会造成根本性的盲点：幻觉。行为分析工具只能表明输出存在错误，只有内部可观测性能够揭示其中的原因——模型是否关注了无关的上下文？它是否为错误的Token赋予了较高的概率？…”

从这个角度出发，内部可观测性或许并不仅局限于AI自身安全攻防领域，而是一个LLM/AGI领域的、效用广泛的技术方向。幻觉问题自从LLM诞生之初就一直困扰我们，虽然有RAG等方法可以予以抑制，但时至今日也没有已公开的方法能够彻底解决幻觉问题。尽管如此，在Realm Labs相关的公开资料中，也未能找到具有足够细节的材料，以表明内部可观测性是否真的能够对幻觉抑制起到积极作用。

减少LLM幻觉造成的业务损害理应也是安全技术的一部分。这或许会是未来值得长期研究的一项课题。

### **04** **一些猜测分析**

根据现有调研结果，我们猜测Realm Prism有可能是以LLM消融（abliteration）技术为基础构建而成。

针对LLM的消融方法早在2024年4月就已被公开提出，论文于同年6月发表于arXiv[12]。该研究表明，LLM在其内部状态中，仅以特定单一方向的向量分量来决定其是否拒绝回答有害问题。只要在模型内部状态中找到并消除该方向的分量，无需对模型进行微调，即可令LLM丧失对有害输入的拒答能力；反之，如果人为添加该分量，即可使LLM对无害输入表现出拒答。由于成本极低，LLM消融技术在各个开源模型社区得到长期以来的广泛应用。受限于篇幅和内容敏感，本文暂不讨论消融技术实现细节，感兴趣的读者不妨移步原论文。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/8-300x190.png)

（非Realm Labs相关）绿盟科技早期进行LLM消融实验复现记录

而随后进一步研究还表明，并非只有拒答/非拒答，而是包括积极/消极、肯定/否定、中文/英文等很多LLM的表现都是由单一方向向量决定的。一个典型的相关实践案例是Llama-3-8B-Instruct-MopeyMule[13]，通过对Llama-3-8B-Instruct进行正交化处理\*，模型输出变得非常消极，对于所有问题都表现得十分悲观。

\*注：通过修改模型权重，使矩阵乘法的结果在特定方向的分量恒为零，从而实现不依靠运行时Hook的、永久性的消融技术。

绿盟科技同样早在2024年11月就完成了对相关技术的进一步研究和实用化。作为其中一个研究项目，实验中发现LLM仅需经过最初约30%的层数后，其内部状态已经在肯定/否定样本上高度线性可分。该方法已在绿盟科技“风云卫”安全大模型相关技术体系中采用，经对比评估，可在几乎不损失准确率的前提下，减少大规模数据分类任务上约54.50%的推理时间开销。针对LLM内部状态的其它研究亦有很多结论和应用，在此不一一列举。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/9-300x155.png)

（非Realm Labs相关）绿盟科技研究中，肯定/否定样本经过LLM时，各Transformer层间隐向量（Latent）的...