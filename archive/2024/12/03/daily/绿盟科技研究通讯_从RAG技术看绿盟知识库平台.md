---
title: 从RAG技术看绿盟知识库平台
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247498085&idx=1&sn=15468e052c0f40baf1af7202a8bde4c3&chksm=e84c5fbadf3bd6ac9039816d46cccc2a1e62b2ac18c616741ebf9ac43201a8c4647df3f6fc30&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2024-12-03
fetch_date: 2025-10-06T19:39:53.340958
---

# 从RAG技术看绿盟知识库平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZiam4oN6mDZic0J2mIoLn5brFLCxazVKhoutCQpZzN2w1Se0C8ibzOaqIg/0?wx_fmt=jpeg)

# 从RAG技术看绿盟知识库平台

原创

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZqldZubuOd0WS9kqaCqZIwyVP6LIjwdPWQDs4B786kLWHlSicSDZMYJg/640?wx_fmt=gif&from=appmsg)

一.  技术概述

RAG技术迭代了三个版本：①Naive RAG 为最原始的框架，其仅完成了检索增强生成的必要阶段，从纯文本问答的角度上看，Naive RAG没有做相应的端对端调优，文本问答质量还有较多问题。②第二个阶段是Advanced RAG，其对RAG各阶段的技术细节进行调整，如文档加载阶段选择不同的分块策略，具体如对元数据进行精细分割和合并；增强对图片的利用，部分平台对图片做到既能问也能答；提问阶段进行问题分解、重提问；检索阶段使用混合检索、重排序等操作...③第三阶段即Module RAG，其适应性强，功能多，如微软提出的GraphRAG将纯文本转化成基于知识图谱的关联查询问题，能更好的利用文本实体之间的关联关系，为LLM提供更多的关联信息。还如表格检索增强TAG技术，它能够基于表格数据结合外延知识进行提问，如问对某地名（单元格数据）是否位于加利福尼亚州（外延知识）？

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZJh4pyp5GwwkvUIrG0EJtYxfQwXGd0XVicg3liaRnQEvxWJI2esm6YtkQ/640?wx_fmt=png&from=appmsg)

图1 RAG技术迭代的三个版本

TAG、GraphRAG等在处理表数据、知识图谱上的功能强大，但它们均存在加载性能低的问题。如TAG需要对表格的每一行数据向LLM发包，当得到所有行的会话结果后再进行答案总结，单一问题的回答耗时过长；GraphRAG的加载需要经过实体提取、关系提取、社区检测、社区自动摘要等步骤，最终形成一个覆盖源文档的知识图谱，从而基于该图谱实现模块化图检索。GraphRAG特别适用于基于知识图谱实现的问答任务，其在多跳问答和知识关联上具有极强的整合能力，而对于纯文本的问答，将文档转化成图谱再进行图查询的开销较大，且不适用于频繁更新知识库的问答场景。

    因此，本文集中讨论更轻量的文本RAG技术，该技术在非结构化文档等最普遍存在的知识载体上具有强大的外挂问答能力。任何用户都可以利用私有的文档数据，在RAG平台上探索其作为外挂知识库的多种能力和应用场景，包含但不限于：产品使用手册问答、公司规范制度问答、文本对比分析（国家标准《XXX》和行业标准《XXX》之间的异同）、考题生成（单选、多选、简答）、摘要生成、大纲补全。结合现有类Gpts平台的丰富技能，还能将文本知识库用于联网搜索、报告生成、表格问答等应用。

    我们对比测试了现有主流RAG平台的问答质量，结果展示各平台在文本知识库上存在一些质量问题，以下列表暴露了部分共性问题。需要注意的是，本列表只涉及针对问答质量的问题，这是我们一直关注的RAG平台的核心关键，而不包括那些集成的工程类操作，如是否支持高级编排、全参数暴露可调、可否单步调试等。

（一）逻辑理解

   文档通常包含一级、二级标题的逻辑关系，RAG技能是否理解序号数之间的逻辑关系？如目标答案在7.3.3，但由于召回了7.3.3和7.3.4，而对两节内容无脑输出。该现象在三级标题上尤为明显。

（二）分条作答

    当LLM使用分条作答的逻辑结构来回答用户问题时，答案对标准答案的覆盖度如何？各条目能否覆盖标准答案的要点？条目是否受到与距离优先的影响，如遗漏距离关键词（检索核）远的条目？

（三）距离优先

    是否距离优先情况？只回答距离关键词（检索核）近的句子、段落，而同等重要的信息，由于远距离而被忽略。

（四）中英文相互召回

    体现了检索器的语种互译能力，如针对英文文档使用中文提问，验证平台的回答质量是否受到语种的影响。

（五）目录利用

    当涉及概括性问题时，检索结果很难覆盖全文各处信息，此时利用目录结构则为LLM提供了很好的概述框架，进一步结合原文内容则为框架填充细节，从而输出覆盖面全且包含细节的概括性答案。

（六）问题精准

    部分平台只对确切的问题（关键词）敏感，而对文中频繁出现的主题词提问，则因为难以定位而回答错误。较好的RAG平台能根据具体问题匹配相关度最高的段落，或通过LLM忽略检索出来的假相关段落。

    此外，文本RAG还要利用多栏PDF、图片、表格等非自然语言形式的知识载体，故需要在RAG的数据加载阶段使用相适应的处理方法，如版本分析、OCR、文档布局、层次增强等。

二.  增强方法

下图为RAG技术包含检索和生成两大步骤，其中蓝色部分展示了过程中待优化的技术点，本文对部分技术点、工具进行分享。参考文献中标记了论文、项目来源。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZFoQm2edGqK5NNMBYAichdSQN6Wl5B46H7jYvBTTG4tM6wngwxkCDLKQ/640?wx_fmt=png&from=appmsg)

图2 蓝色部分为RAG可优化的技术点

2.1

文档层次性增强 [1、2]

文档层次增强的思想包含三个方面：

（1）形成层次结构：每个文档都会经过MarkdownFormatter的处理，根据其固有的章节结构将其转换为[章节元数据：章节内容]对，然后以Markdown格式存储。该工作引入了MarkdownFormatter将源文档转换为富含结构元数据的Markdown文档。

（2）根据层次进行增强：提取片段的层次结构，并将元数据关联到到每个章节中，以构建数据库。根据片段类型（即文本、表格或图像）对结构元数据和上下文信息进行不同的处理，形成增强片段相应的级联元数据，然后使用嵌入模型将增强的片段转换为嵌入向量并存储在向量数据库中。

（3）多路检索：应用多路检索方法来增强RAG。具体来说，该工作通过以下三种方法实现了检索：向量相似度匹配、弹性搜索、关键字匹配，其中：该工作还采用关键命名实体检测（CNED）方法，利用预先训练的命名实体检测模型从文档和查询中提取关键字。

    在实验过程中也有相同的发现，如果在检索时能够强烈遵循于一种层次结构，就能够减少很多由于兄弟节点（与目标段距离相近的上下文）的影响。基于这种标准化的层级逻辑，在实现RAG检索时，可以针对于不同层次节点的文本进行关键词检索，然后只返回从这一节点向下遍历的子节点的文本信息，从而避免在平铺式的检索下，受到兄弟、非同分支的节点的影响。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZxfhT4GqcaU7Hj6SkNfS91ViaNvI8EODnS0yqibFxia2iaqHxnFNicyMc7sQ/640?wx_fmt=png&from=appmsg)

图3 文档层次增强架构

2.2

PandasAI [3]

PandasAI 是一个 Python 库，以自然语言向数据提问，以帮助您使用生成式 AI 探索、清理和分析数据。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZUibqHESQFc0xTRHUHwCMSUyJ0dde4lHibcBLqWVtSLt5lnpS1FvTQvyQ/640?wx_fmt=png&from=appmsg)

图4 PandasAI表格问答示例

2.3

优化查询 [4、5]

该研究发现，用户查询包含下面三种类型：（1）简单查询：LLMs应该直接回答，而不是加入不必要的上下文；(2) 复杂问题-问题分解：对于复杂的查询，使用原始查询进行搜索往往无法检索到足够的信息。LLM首先要将这类查询分解为更简单、可回答的子查询，然后搜索与这些子查询相关的信息，最后整合子查询的回答。(3) 模糊查询-消除歧义：对于模糊的问题，LLM应该先学会澄清查询，最好是通过识别用户的意图，然后制作出更有针对性的回答。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZGPuwGnsqPY5iadnhGwQf9H3P656aoBjdtDMgVtc39nf17oiaTs8bUicMg/640?wx_fmt=png&from=appmsg)

图5 三类用户Query

因此，RQ-RAG通过微调模型对召回的上下文以及query进行意图分类。以端到端的方式训练一个 7B Llama2 模型，使其能够通过重写、分解和消除歧义来动态完善搜索查询。具体操作（下图）：手动针对不同query划分到三个类别下，并是分别使用3个prompt生成三个精准query，并利用新query检索得到上下文，使用LLM生成新的响应，完成训练集构造过程。最后使用40k训练集，训练Llama2使其具有意图分类能力。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZMURibS3T5NN1j4TRWrS8CVeOdWDR5DnUEECdceVTTHN5gzy4XDalpkw/640?wx_fmt=png&from=appmsg)

图6 查询优化

2.4

文档布局转成知识图谱 [6]

方法和2.1的“层级增强"想法相同，都强调了文档结构对于RAG检索阶段的重要性。方法的分层逻辑复杂，可以宏观理解到通过分割、解析获取图像、表格、文本和边界框之间的逻辑关系，这一步骤也是整篇文章的技术核心。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZUkBeZzfQciaBC2MLVKbgkz9P5WpZUydOMiaJn4rF0epbxLXHCLBib4hIw/640?wx_fmt=png&from=appmsg)

图7 将文档布局转成KG

三.  RAG平台

本节介绍业内三款主流的RAG平台及各自的优势，此外还如扣子[7]、FastGPT[8]、ChatPDF[9]、Qanything[10]等平台，均有各自的工程特性和问答算法。

3.1

Dify[11]

Dify是一款综合性的AI应用平台，提供Prompt、插件、工作流、知识库、数据库来构建AI应用，应用Bot支持工作流编排、知识库搭建、插件调用。同款产品如扣子、AgentBuilder、Gpts等。

    此类平台的主要优势在于Rag、Agent等工作流的构建和高级编排，平台通常提供丰富的组件库，且通过“拖拽”、“连接”等前端操作即可实现组件串联，大多数平台支持参数调整，部分平台支持工作流组件单步调试。

    Dify组件库覆盖了Rag全流程组件和多款工具，如Rag的检索器、LLM组件、条件分支等；以及谷歌搜索、Bing搜索、Arxiv搜索等在线搜索工具；还如天气预报、生成二维码、图标绘制等分析工具。此外，Dify提供的组件库粒度较粗，部分平台提供更细粒度的组件，如覆盖langchain、autogen、Memories记忆器的全量组件，从而能完成更复杂的的Rag、Agent任务。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZicr157UGxhO7OMrdweTdthYauefjWibGQkwzsnBYHfEz8M8umb4jDnZQ/640?wx_fmt=png&from=appmsg)

图8 Dify高级编排和组件库

通过组件库和高级编排，用户可以根据自身需求设计工作流，下图展示了基于分类器的RAG工作流，通过Question Classifier分类器将用户问题分流到具体的知识库中，如判断用户query判断属于【售后、用户手册、其他】中的哪一类，然后根据匹配到具体的知识库回答问题。此外，看到Dify平台是一款可以分步调试的平台，如分类器、检索器、大模型等步骤的具体输出，帮助用户理解答案并进行工作流调优。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZuyysJKqYMNr0hiaFURv1Qp7Nibq3UURzxoPc2PgDZia5iarWcNqh6yfmzQ/640?wx_fmt=png&from=appmsg)

图9 基于分类器的知识库问答

3.2

RagFlow[12]

RagFlow提供了11种文档问答模式，如双栏论文、法律文件、PPT、图片、表格等，均使用了对应的分块&检索策略。RagFlow的文档处理基于DeepDoc模块实现，该模块包含两个组成部分，视觉处理和解析器：视觉处理包含OCR、布局识别（文本、标题、配图、配图标题等等）、TSR（Table Structure Recognition，表结构识别），总的来说，视觉处理实现了pdf、excel的OCR功能。解析器对PDF、DOCX、EXCEL和PPT四种文档格式进行解析，其中PDF的解析复杂度最大。

    RagFlow底层使用了自研的Infinity数据库，其为向量、全文和结构化数据等丰富的数据类型提供了广泛的搜索功能，数据库支持向量检索、结构化查询、多路召回、融合排序等多种检索方式。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZwHVa4Ml76ujkP2eoYbibciaVnicKibiawEuRTo70YtGMa0QYGcKPrCiczRqw/640?wx_fmt=png&from=appmsg)

图10 Infinity数据库

下例展示RagFlow的表格问答模式，它能够很好的理解表格之间的行列关系，自动匹配目标单元格并对所在行的相关字段进行整合输出。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZu6d5hCMRNbUEibUBSMGbficO95Yejfg84vnVhZkiaRDCYNBVfhotbrvug/640?wx_fmt=png&from=appmsg)

图11 表格问答

3.3

ChatDoc[13]

ChatDoc是一款闭源的RAG平台，平台的突出优势在于参考页、选择后提问、问题候选项等。ChatDoc对RAG中提问和答案验证阶段做了很多工程化操作，问答过程对用户友好，省略了RAG的技术流程。

    具体来说：（1）参考页能够提供答案对应原文的页数和具体段落，点击后可以跳转到该页面并对具体段落进行高亮。这个映射操作在其他平台上需要后台手动实现，即针对答案中的关键词在上下文列表、原文文本中进行查询，从而核实检索的准确性，过程非常低效；而ChatDOC将这个过程进行自动化，简化了用户验证的过程。（2）引用后提问针对给定的chunk id范围进行扩展，能够在一定程度上提升问答质量。（3）平台还可能固化了部分query模板，在上传某文章后自动和LLM进行提问交互，从而提供的自动摘要和参考问题等功能。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZhdZlxyOtEFpqFkNYOjEOlNeGHK8uv0qVpPd2icITFoQJwttdgoR8tVA/640?wx_fmt=png&from=appmsg)

图12 ChatDoc功能概览

从用户的角度，最有价值的功能就是提供参考页，其他平台都不具备真正细粒度的答案溯源能力。ChatDOC包含两个粒度的参考，如果答案能够使用原文句子进行回答时，那么会在答案中该原句后面标记参考页，点击跳转到该页面，同时对原文段落/句子进行高亮展示；如果答案是由LLM参考多个上下文整合后生成，如全文摘要的问题，那么很难追溯每一个概念的缘由，此时会对上下文的页面进行列举，同样可跳转，并对重点段落/句子高亮展示。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZA2wHm00o3NHtCqKKNrDKmkY89bkQmZwhJgaFryafEqO69XSPcBfAVQ/640?wx_fmt=png&from=appmsg)

图13 粗粒度的答案整体参考列表

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZEriaEt14mxtE9IHmGAg2Ptw4gqIYZk73Lib5ZKuaSNFW08PypoLlnuLA/640?wx_fmt=png&from=appmsg)

图14 细粒度的某句\段答案参考

四.  绿盟RAG平台

绿盟RAG平台面向网络安全场景，重点突破两大难点。其一针对网络安全领域的多模态文档进行处理。网络安全领域涉及如攻防经验和安全合规等文档，包含手写文字、工具截图等大量图型文本信息，文档内容涉及表格、字符、源代码等非自然语言文本，传统RAG架构的加载、检索能力有限。其二解决了通用LLM无法适应安全场景的问题。RAG的生成阶段依赖LLM的能力，需要LLM利用URL链接实现图片展示、网页跳转、文档下载等功能，部分安全用户要求平台具有细粒度答案溯源的功能，如生成答案时自动匹配原文和原图，而通用LLM在这些方面均未做优化。

    平台专注数据+应用+溯源+评估全流程，对RAG各阶段的组件后端逻辑和组件参数进行优化，通过在海量测试集上进行手工测试和模型评估测试，验证了平台在多条工作流模板上的稳定性和准确性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUYu9un4Zpic2JlHl6icyjbzYZibbTKbeNpE083vmWibmUrRx1qbwpLRNC6fRiaOswL5NkwxY...