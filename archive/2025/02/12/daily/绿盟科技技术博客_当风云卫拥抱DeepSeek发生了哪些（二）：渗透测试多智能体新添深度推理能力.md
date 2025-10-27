---
title: 当风云卫拥抱DeepSeek发生了哪些（二）：渗透测试多智能体新添深度推理能力
url: https://blog.nsfocus.net/deepseek2/
source: 绿盟科技技术博客
date: 2025-02-12
fetch_date: 2025-10-06T20:36:15.410151
---

# 当风云卫拥抱DeepSeek发生了哪些（二）：渗透测试多智能体新添深度推理能力

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

# 当风云卫拥抱DeepSeek发生了哪些（二）：渗透测试多智能体新添深度推理能力

### 当风云卫拥抱DeepSeek发生了哪些（二）：渗透测试多智能体新添深度推理能力

[2025-02-11](https://blog.nsfocus.net/deepseek2/ "当风云卫拥抱DeepSeek发生了哪些（二）：渗透测试多智能体新添深度推理能力")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 968

**摘要** ：绿盟科技将DeepSeek-R1的深度推理能力引入渗透测试多智能体PTest Agent中，通过Web渗透测试任务上的实战验证，发现深度推理具有重要性和可行性，后续将重点投入更为深入的探索与研究。

**一、引言**

绿盟科技期望将DeepSeek-R1的深度推理能力引入网络安全领域，以期革新复杂安全任务的处理方式。本文对DeepSeek-R1的深度推理能力进行了阐述，并通过测试验证了其在安全领域具备一定的优势。同时，风云卫在已有的安全大模型SecLLM中尝试引入深度推理能力，并通过渗透测试多智能体PTest Agent在Web渗透中展开了实战验证。验证结果表明，引入深度推理能力后的PTest Agent在渗透任务规划、信息推理、工具推荐等方面表现出价值和可行性，预示其有望在复杂实战环境中实现更智能、更高效的自动化渗透测试。

****二、DeepSeek********–********R********1********深度推理是什么？****

OpenAI的o1和DeepSeek-R1与GPT、文心一言等主流大模型存在显著区别。主流大模型倾向于指令型架构，而OpenAI o1和DeepSeek-R1属于推理型大模型，具备更强的深度推理能力，在解决复杂问题时表现出接近人类专家的水平。

尽管OpenAI o1的实现细节未公开，但DeepSeek-R1成功复现了其深度推理能力，并在多个方面表现出色。DeepSeek-R1不仅展示了推理过程的可视化，还开源并发布了相对详细的技术介绍，为AI行业做出了贡献。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片8-300x112.png)

DeepSeek-R1的优势在于其深度思考（R1）所提供的深度推理能力。打开上图中DeepSeek的深度思考（R1）后，能够模拟人类认知路径，将复杂问题分解为更小的步骤，通过多步骤逻辑推导与因果分析实现问题求解。这些步骤通常被称为“推理步骤”、“思维过程”或“思想链”，如下图R1在做数学应用题时不仅提供答案，还展示得出答案的“思考”过程。可见用户在启用深度思考模式后，能够观察AI的思考路径和思考逻辑，甚至反向学习如何拆解复杂问题。这种“透明化推理”我们可以评估模型决策的合理性和可靠性，大模型不再是神秘黑盒。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片9-300x197.png)

图 1 深度推理的思考步骤示例

****三、深度推理在安全领域能够做什么？****

|  |
| --- |
| 如果我们将DeepSeek-R1的深度推理能力引入网络安全领域，有望革新复杂安全任务的处理方式。DeepSeek-R1在数学、代码和知识问答等任务中的卓越表现，暗示了其深度推理能力在应对网络安全挑战方面的巨大潜力，尤其是在处理复杂攻防对抗逻辑、适应动态威胁、提供精确推理和决策支持等方面。深度推理通过模拟安全专家的认知过程，将复杂安全问题分解为更易管理的步骤，并进行多步骤逻辑推理，有望在以下三个维度实现突破，从而解决传统安全系统难以应对的难题：  1）**复杂任务泛化**：支持网络安全领域复杂任务的结构化拆解，例如重构多步漏洞利用链、推演APT攻击策略，实现复杂场景下的任务泛化。  2）**可信度提升：**通过深度推理实现决策路径透明化，提升决策的可解释性和可信度. 依据GSM8K基准测试验证，深度推理的准确率较传统单步推理提升62%，为安全决策提供更可靠的依据。  3）**人机协同进化**：将推理过程可视化，实现“白盒AI”，使网络安全分析师能够介入并修正推理偏差，促进人与AI的协同进化，提升整体安全分析能力。  然而，我们也需要认识到，深度推理并非适用于所有网络安全场景。由于深度推理过程需要大量的计算资源，可能导致秒级以上的延迟，因此不适用于对实时性要求较高的安全处置任务。 |

下面我们尝试在最基础的Web渗透任务规划和测试工具调用两个方面验证DeepSeek的深度推理能力。

**Web渗透任务规划****：**

在DeepSeek网页版中，关闭深度思考（R1）模式，观察其对Web渗透任务规划的输出。如下图结果部分显示，规划输出侧重于步骤的完整性，但缺乏对渗透环境和任务详细深入的分析，仅体现了渗透测试的常识性知识。这表明，在未启用深度推理的情况下，DeepSeek无法应用于复杂渗透测试任务的规划。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片10-300x212.png)

开启深度思考后（R1）后，Deep Seek在Web渗透任务规划能力得到显著提升。首先展示推理过程，用时18秒。这一过程突出了任务分解和多步骤逻辑链，使得用户可以理解其决策过程，并评估其合理性。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片11-300x267.png)

相比于未开启深度思考模式，DeepSeek-R1输出的任务规划不仅更加完整，而且在任务细节上有了细致分析。如下图以信息收集阶段为例，DeepSeek-R1不仅给出了不同信息的收集工具，还针对nmap等探测命令推荐了重点关注的端口。这种细致程度表明DeepSeek-R1对Web渗透测试的理解已达到有一定经验的渗透测试人员的水平。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片12-286x300.png)

最后DeepSeek-R1深度思考后的输出，还包括渗透测试的注意事项以及覆盖整个任务过程的建议，确保全面覆盖攻击面。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片13-300x189.png)

从深度思考后（R1）的输出可以看出，DeepSeek-R1在Web渗透测试任务规划方面是有可能模拟人类认知，将复杂问题分解为更小的步骤，展示推理过程，使用户理解其决策依据，并评估其合理性。其深度推理能力有望与网络安全领域知识相结合，应用于复杂的真实渗透测试任务中。

然而，上述Web渗透测试任务规划与真实渗透测试仍存在一定差距。真实的渗透测试环境极其复杂，且需要应对不断变化的环境因素。这意味着深度推理需要具备更强的适应性和实时性，才能真正应用于渗透实战场景。

**渗透测试工具调用**：

当前，DeepSeek-R1作为AI助手，尚不具备直接调用和执行工具（如nmap）的能力。因此，我们接下来主要测试其对nmap工具的理解和应用能力。

通过测试，DeepSeek-R1令人眼前一亮的是它能够提供nmap扫描命令示例、结果解析方法，甚至给出变通方案。如下图所示，DeepSeek-R1 提供了在线工具组合和 Python 代码的实现方式，可以在不直接执行nmap的情况下，指导用户完成相应的网络扫描任务，提供有益的辅助，这展现了其作为AI助手在安全领域的潜在价值。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片14-300x212.png)

同时，DeepSeek-R1思考中还提出了企业级扫描测试和合规性注意事项（如下图），这表明其不仅深入理解nmap命令手册中的各种参数，还具备nmap高阶用法的实践经验。

1. **攻防对抗经验**：DeepSeek-R1 能够建议将-f分片传输和–data-length 组合使用，体现了其在攻防对抗方面的经验。通过-f选项，nmap在扫描时使用小的IP包分段，将TCP头分段在几个包中，使得包过滤器、IDS等其它检测工具变得更加困难。–data-length参数则用于指定每个探测包附加的随机数据长度，在探测某些类型的防火墙或 IDS 时，增加一定的随机性使得扫描更难以被检测。
2. **脚本扫描能力**：DeepSeek-R1 能够通过nmap –script来执行用户自定义的多样化脚本集，这通常是高阶渗透测试专家才会考虑的做法。然而，DeepSeek-R1推荐的http-aws-keys脚本名称未能找到，可能存在模型幻觉。
3. **绕过****IP****拦截（ACL）**：DeepSeek-R1建议通过Proxychains和nmap结合使用来避开IP封锁，这也是高阶渗透测试专家常用的技巧。Proxychains 允许用户通过SOCKS或HTTP代理链来转发网络流量，从而隐藏真实IP地址并绕过目标服务器的IP拦截。

总的来说，DeepSeek-R1在nmap使用方面展现出了较高的专业水平，能够为安全分析人员提供有价值的参考和指导。同时，也需要注意模型可能存在的幻觉问题，并结合实际情况进行验证和调整。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片15-279x300.png)

总的来说，DeepSeek的深度推理能力在Web渗透测试任务规划和nmap工具理解方面展现出一定的潜力，但仍有提升空间，包括添加工具调用能力和增强模型的实用性，并提高模型在复杂环境下的适应能力及减少模型幻觉。

****四、如何利用深度推理助力渗透测试****

当前绿盟风云卫中，安全行业大模型SecLLM缺乏足够的规划能力，安全智能体可以完成工具调用和执行，但是依赖于预设的工作流，所以难以灵活适应复杂和动态变化的测试环境。绿盟风云卫尝试引入深度推理能力，并在Web渗透测试任务上展开实战验证。

首先，我们尝试采用知识蒸馏技术，将DeepSeek-R1的深度推理能力迁移至SecLLM（如下图）。DeepSeek-R1作为教师模型，将推理知识传递给学生模型SecLLM。推理知识数据包括两部分：一部分数学和代码方面的思维链数据，二是利用DeepSeek-R1为现有渗透测试数据集生成的推理步骤或思维过程。这些推理知识数据模拟渗透测试专家的认知过程，将复杂安全问题分解为更易管理的多个步骤，便于模型学习和推理。经专家审核优化后，这些推理知识数据被用于训练SecLLM，使其重点保留逻辑推理和自主验证能力。通过教师模型的输出如推理路径、中间状态指导学生模型训练，实现推理知识有效传递到DeepSeek-R1-Distill- SecLLM模型上。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片16-300x147.png)

然后，集成深度推理能力的DeepSeek-R1-Distill-SecLLM模型被部署至绿盟安全多智能体平台。平台中现有智能体如渗透测试多智能体PTest Agent等都可以通过API获得DeepSeek-R1-Distill-SecLLM模型新加的深度推理能力。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/企业微信截图_17392691238693-300x144.png)

接下来渗透多智能体PTest Agent对已授权的测试网站展开测试，验证其深度推理能力是否有效？

原来PTest Agent是按照既定的渗透工作流进行渗透测试和工具调用，无法进行任务的预先规划，也无法根据实际测试环境情况灵活选择测试工具。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片18-300x145.png)

当前PTest Agent通过API可以获得DeepSeek-R1-Distill-SecLLM模型的深度推理能力。惊喜发现，PTest Agent对测试网站的渗透任务进行了预先规划，给出信息收集、指纹生成、POC验证和EXP生成和漏洞利用的详细过程。这过程中根据收集网站指纹信息推理分析了可利用漏洞，并按严重程度、利用方式、攻击收益等指标进行排序推荐。更为关键是这过程中对可用漏洞执行了自主PoC验证，并推荐出可用漏洞利用工具zentao\_auth\_bypass\_rce\_1(利用脚本名称)。可以看出，PTest Agent不再依赖于预设的工作流，已经拥有了一部分逻辑推理和自主验证的能力。这部分深度推理能力有助于PTest Agent灵活适应复杂和动态变化的测试环境。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片19-300x223.png)

PTest Agent任务规划完毕后，可以按规划的多个步骤自动化执行并完成工具的调用和执行。如下图自动生成漏洞验证工具的执行参数，并自动调用工具完成PoC漏洞验证。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片20-300x224.png)

在漏洞验证任务完成后，分析其PoC验证结果，尝试下一步攻击任务。如果PoC验证成功，证明漏洞存在并可利用。PTest Agent接下来调用执行前面推荐的漏洞利用工具zentao\_auth\_bypass\_rce\_1，自动执行对该漏洞的利用步骤。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片21-300x196.png)

PTest Agent通过对利用工具zentao\_auth\_bypass\_rce\_1的调用执行，上传webshell文件任务，完成webshell木马的植入，最后给出如下图所示的漏洞利用结果。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片22-300x260.png)

渗透人员根据PTest Agent给出的远程连接信息（webshell/后门/弱密码/等），可以进行远程控制目标（如下图）。

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/企业微信截图_366429a7-0e02-4b89-ab84-101d1125e810-300x180.png)

从上述渗透测试的整个过程来看，PTest Agent能够依据目标系统的具体情况进行分析、推理和决策，从而有效完成web网站的渗透测试任务。其深度推理能力在渗透任务规划、信息推理分析、测试工具推荐等方面展现出可行性。

* **渗透任务规划：**能够将复杂的渗透测试任务分解为信息收集、漏洞扫描、验证和利用等详细步骤，从而助力渗透测试人员理解任务目标并采取效行动。
* **信息推理分析：**能够分析测试过程中收集的信息，并推断出有价值的结论，例如根据网站指纹识别结果推断出可能存在的漏洞。
* **测试工具推荐：**可以根据渗透任务需求和测试环境特征，推荐合适的漏洞可利用工具，例如漏洞利用工具zentao\_auth\_bypass\_rce\_1。

实战验证表明，PTest Agent通过深度推理提升了渗透测试的效率和准确性，降低对人工的依赖。但是我们需要认识到，上述测试仅为简单验证，尚未对复杂渗透测试展开大规模测试。目前，由于推理知识数据的有限，SecLLM深度推理能力也有限。后续我们需要加强多样化的思维链数据集构建，帮助SecLLM更好地理解和学习不同类型的渗透测试问题的推理模式，学习安全专...