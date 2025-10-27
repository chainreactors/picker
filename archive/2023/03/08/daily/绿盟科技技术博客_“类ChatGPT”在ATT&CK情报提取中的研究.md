---
title: “类ChatGPT”在ATT&CK情报提取中的研究
url: http://blog.nsfocus.net/chatgptattck/
source: 绿盟科技技术博客
date: 2023-03-08
fetch_date: 2025-10-04T08:55:08.590106
---

# “类ChatGPT”在ATT&CK情报提取中的研究

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

# “类ChatGPT”在ATT&CK情报提取中的研究

### “类ChatGPT”在ATT&CK情报提取中的研究

[2023-03-07](https://blog.nsfocus.net/chatgptattck/ "“类ChatGPT”在ATT&CK情报提取中的研究")[章瑞康](https://blog.nsfocus.net/author/zhangruikang/ "View all posts by 章瑞康")[ATT&CK](https://blog.nsfocus.net/tag/attck/), [ChatGPT](https://blog.nsfocus.net/tag/chatgpt/)

阅读： 2,432

## ****一、背景介绍****

美国人工智能公司OpenAI的ChatGPT是一个基于自然语言处理的聊天机器人，在自然语言处理方面具有一定的优势，可以用于识别和理解文本中的实体和关系，提取威胁漏洞、攻击者、攻击方法等情报信息。360刘焕勇《NLP前沿技术:One-shot就能做事件抽取？ChatGPT在信息抽取上的强大应用》中实验得出ChatGPT完全胜任信息抽取工作的结论。

在ChatGPT推出两个月前，微软公开了基于GPT2的ATT&CK（Adversarial Tactics, Techniques, and Common Knowledge）情报提取工具MitreMap，并集成到Azure Sentinel云原生SIEM平台。ATT&CK威胁情报信息如TTPs（技术、战术和程序）等提取分析有助于提高对威胁的识别和响应能力，从而帮助组织更好地保护自己的网络和数据资产。

安全界已经掌握了使用来自OSINT系统或第三方供应商的机器可读资料，但这些资料通常提供IOC或IOA，而没有背景信息。另一方面，我们拥有丰富的威胁分析报告，包含在内部事件响应报告、公共博客和白皮书中。这些报告描述了ATT&CK威胁情报信息，包括网络攻击者的行动、工具、战术和程序等，而当前无法自动消费或使用这些数据，因为它们是由非结构化文本组成的。威胁分析员通过手动操作来提取与他们的威胁模型最相关的对手信息，但这种手动工作存在时间和成本上的瓶颈。

如何从已有的威胁分析报告中提取ATT&CK情报信息用来洞察安全态势？微软基于GPT2的 MitreMap工具是否能有效自动化提取分析ATT&CK情报信息？基于GPT3.5以上的ChatGPT是否可以直接应用于ATT&CK情报提取？本文通过测试分析“类ChatGPT”基于自然语言处理（NLP）技术在ATT&CK情报提取上的“洞察”能力，展望“类ChatGPT”在威胁情报分析领域的应用前景。

## ****二、ATT&CK********情报信息提取工具****

威胁分析报告大部分是由非结构化文本数据组成，描述了攻击者或攻击团体在网络攻击过程中使用的工具、技术和程序等，报告通常来自于安全博客、社区论坛、安全厂商或情报共享平台。目前越来越多的网络威胁分析报告公布了ATT&CK映射关系，然而传统依赖于人工从不断增长的报告中分析提取出ATT&CK技术是不现实的，为了减轻安全研究人员的分析疲劳，通过NLP技术提取非结构化报告中的ATT&CK，实现威胁报告中不同威胁信息自动映射ATT&CK十分必要。下面分析三种自动化的ATT&CK情报信息提取工具：微软的MitreMap、OpenAI的ChatGPT和绿盟自研NS-IE。

* **微软Mitre****M****ap**

微软MitreMap是一个基于MITRE ATT&CK框架的威胁情报可视化工具。它可以帮助安全分析师更好地理解和可视化威胁情报，以及威胁行为的攻击链和关联关系。

MitreMap可以与微软 Defender for Endpoint和Azure Sentinel等安全产品集成，从而提高安全分析和响应的效率和准确性。MitreMap集成到Azure Sentinel云原生SIEM平台，该平台依靠微软强大的安全解决方案以及ML的分析能力实现对企业、用户和服务的各种维度的监控及探测，还为客户自定义搜查场景提供运维平台Jupyter Notebook，方便客户创建及运维主动调查的脚本及算力支撑。MitreMap集成在Notebook中可以协助安全分析人员快速分析安全报告，同时也可在Notebook外独立运行。

MitreMap采用的DistilGPT-2模型是一种更快、更轻量、经过知识蒸馏的GPT-2模型，它用于将描述文本中攻击技术术语与历史技术描述相关联，完成文本到ATT&CK技术的映射，另外还支持IOC的抽取。相比于算法上的提升，MitreMap在数据量上也有突破，MitreMap从TRAM、Sentinel Hunting和检测规则等数据源收集了1万3千条数据，训练集与TRAM相比扩充了接近10倍。

值得一提的是，MitreMap为DistilGPT-2模型的ATT&CK技术预测结果提供了部分可解释性，展示了正相关和负相关的相关短语或词汇。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图1-300x193.png)

图 1 MitreMap-NoteBook演示

* **OpenAI****ChatGPT**

ChatGPT是由OpenAI开发的大型语言模型，建立在GPT-3.5之上，是GPT-3.5微调的产物，可以进行信息抽取、语义理解、问答等自然语言处理任务。ChatGPT在NLP（知识抽取与构建）和IR（知识检索，问答等）相关任务的研究范式上提出了新的思路，图2是ChatGPT在信息抽取中的作用。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图2-300x195.png)

图 2 ChatGPT交互式信息抽取

事件抽取是信息抽取的关键技术之一，ChatGPT提供了一个通用事件抽取例子，如图3所示，可以准确地识别文本中的关键信息，抽取通用事件信息基本正确，并给出了解释。可见ChatGPT可以帮助企业和机构从大量文本数据中提取通用事件信息，提高数据分析、决策的效率和准确性。ChatGPT是否可以应用于安全领域ATT&CK相关攻击事件抽取有待后续实验验证。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图3-300x108.png)

图 3 ChatGPT交互式事件抽取

* **绿盟自研NS****–****IE**

绿盟天枢实验室在威胁报告分析、安全知识图谱构建和推理分析方面积累了较多技术经验，并自研ATT&CK提取算法（以下简称NS-IE）从网络威胁报告中自动化提取和预测ATT&CK技术，从而降低非结构数据的分析成本，提升ATT&CK在绿盟产品的检测和防御能力。

绿盟对关于威胁报告ATT&CK提取的研究或工具分析总结如表1，其中具有代表性的工作有MITRE威胁信息防御中心CTID提出的TRAM（<https://github.com/center-for-threat-informed-defense/tram/>）和开源项目rcATT（<https://github.com/vlegoy/rcATT>）。下面通过模型框架、应用效果等方面综合分析现有ATT&CK提取分析工具。

表 1 ATT&CK情报信息抽取工具汇总

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | rcATT | TTPDrill | Unfetter Insight | TRAM | MitreMap |
| 分类方法 | 多标签文本分类（SVM） | 本体模型 | 多标签文本分类（NB） | 多标签句子分类（LR） | DistilGPT-2 |
| 特征值 | 词特征 | 威胁行为 | 词特征 | 词特征 | 词特征 |
| 后置过滤 | 技战术关系 | 技战术关系 | 无 | 无 | 无 |

在对上述ATT&CK提取工具的调研实践中发现，其准确性和稳定性存在不足，主要存在的问题有：

1. 攻击行为无关的语句打上ATT&CK技术标签
2. 部分ATT&CK技术分类准确率较低
3. 缺乏可解释性
4. TTPDrill完全依赖行为规则分类，维护成本高

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图4-300x171.png)

图 4 ATT&CK分类混淆矩阵

ATT&CK技术分类容易产生误报原因之一在于不同技术之间存在交叉性，在文本描述上呈现趋同性容易混淆。例如，从图4所示的部分技术分类混淆矩阵可以看出技术T1546(Event Triggered Execution)与T1033（System Owner/User Discovery）易混淆，原因在于两段技术描述中，system、user、account均为高频词汇，而分类器从词特征上很难准确提取描述文本语义，容易生成误报。

因此我们提出了自己的ATT&CK提取算法（以下简称NS-IE），进行数据和算法优化改进：

* 借鉴TRAM，提供一系列交互功能，包括结果校验、自定义机器学习模型，从上图能看出预测结果直接和对应语句建立关联，并支持用户反馈校验结果；
* 以数据为中心，人工标记数据扩充TRAM训练数据集，添加噪音数据，对非攻击技术相关语句进行初筛，从而降低误报；
* 融和专家经验知识，添加技术行为触发词，通过攻击行为相关短语和词汇来区分易混淆的ATT&CK技术，提供可解释性。

NS-IE不仅集成了ATT&CK提取算法模型，还支持抽取威胁报告中其他关键信息如攻击者、恶意软件、攻击目标和IOC等实体。基于NS-IE关键信息抽取算法，我们构建了威胁报告分析展示平台，如图5所示，我们对关键信息做了列表化和图谱化呈现，实体关系图谱中包括了勒索家族（black basta）、目标行业（retail）和使用的攻击方法(collect data and credentials)，其中攻击方法由原文中的行为短语组成，可进一步映射到ATT&CK技术，通过图谱形式提供图可解释性。同时NS-IE除了协助分析人员高效直观地获取信息，还支持用户交互，对分析结果进行校验反馈。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图5-300x124.png)

图 5 NS-IE系统截图

## ****三、工具的对比实验分析****

通过以下实验，对比分析微软MitreMap，OpenAI ChatGPT和绿盟自研NS-IE三个工具在ATT&CK情报提取方面的优劣势。

* **实验1：远控木马行为分析**

针对如下一段话进行ATT&CK情报信息提取测试分析远控木马的攻击行为：

During the initial connection to the remote server (after an initial ping to check for internet connectivity), the Trojan will send the machine\u2019s name, installed Windows version, logged username, webcam availability and the version of the RAT in use.

表 2实验1对比分析结果

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 预测结果 | 置信度 | 可解释性 | 准确性 |
| MitreMap | T1033-System Owner/User Discovery | 0.799 | Username、remote、server | 部分准确 |
| ChatGPT | T1071:Application Layer Protocol  T1105-Remote File Copy  T1027- Obfuscated Files or Information | / | / | 错误 |
| NS-IE | T1082-System Information Discovery | 0.915 | Send the machine | 准确 |

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图6-300x180.png)

图 6 MitreMap-实验1 抽取预测分析可视化

MitreMap所使用的DistilGPT-2模型，这段话描述了远控木马在连接到远程服务器后，会发送受害主机的Windows版本和登陆用户名等敏感信息给服务器，从图6MitreMap分析结果来看分析结果不是很理想，预测结果并不全面。因为攻击者经常使用新的攻击技术和工具，而且ATT&CK框架也在不断发展和更新，使得预测变得更加困难。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图7-300x215.png)

图 7 ChatGPT-实验1对话提取分析

ChatGPT可在对话过程中理解我的意图，并知道ATT&CK技术框架的概念，但是预测结果会给出多种可能性的推测，需要安全专家进一步人工验证分析。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图8-300x198.png)

图 8 NS-IE-实验1抽取预测结果图谱展示

NS-IE预测标签为T1082(System Information Discovery)，没有预测出T1033(System Owner/User Discovery), 没有完整的识别出描述中所有攻击技术。但是提供相关行为触发词，同时NS-IE对抽取出的技术实体进行图谱化展示，支持用户图交互下钻分析，发现更多关联知识，如恶意样本家族、攻击者和攻击工具等。

* **实验2：恶意软件行为分析**

针对如下一段话进行ATT&CK情报信息提取测试分析恶意软件的攻击行为：

Although most of these samples are known, cybercriminals rely on a plethora of obfuscation tools and techniques in order to change the malware structure so as to bypass signature scanning and avoid antivirus detection.

表 3实验2对比分析结果

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 预测结果 | 置信度 | 可解释性 | 准确性 |
| MitreMap | T1482-Domain Trust Discovery | 0.0906 | Most、tools、bypass | 错误 |
| ChatGPT | T1027-Obfuscated Files or Information | / | 具备 | 准确 |
| NS-IE | T1027-Obfuscated Files or Information | 0.852 | Obfuscation | 准确 |

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图9-300x178.png)

图 9 MitreMap-实验2 抽取预测分析可视化

MitreMap预测分析结果并不理想，可信度较低。预测ATT&CK技术是一项非常复杂的任务，需要全面的数据、准确的算法和配置、以及深入的上下文信息等多个因素的综合考虑。因此，即使使用最好的工具和方法，也不能保证完全准确地预测出所有的ATT&CK技术。

![](https://blog.nsfocu...