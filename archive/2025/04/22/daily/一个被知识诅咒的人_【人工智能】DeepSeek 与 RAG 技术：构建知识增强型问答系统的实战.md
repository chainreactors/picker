---
title: 【人工智能】DeepSeek 与 RAG 技术：构建知识增强型问答系统的实战
url: https://blog.csdn.net/nokiaguy/article/details/147387442
source: 一个被知识诅咒的人
date: 2025-04-22
fetch_date: 2025-10-06T22:04:22.138605
---

# 【人工智能】DeepSeek 与 RAG 技术：构建知识增强型问答系统的实战

# 【人工智能】DeepSeek 与 RAG 技术：构建知识增强型问答系统的实战

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2025-04-21 12:46:17 发布
·
1.1k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

14

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

27
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

本文深入探讨了如何利用 DeepSeek R1 模型结合检索增强生成（RAG）技术，构建一个高效的知识增强型问答系统。RAG 技术通过结合信息检索与生成模型的优势，能够显著提升问答系统的准确性和上下文相关性。文章详细介绍了 DeepSeek R1 的技术架构、RAG 系统的设计与实现，包括环境搭建、知识库构建、检索模块优化以及生成模块的细化调优。提供了大量 Python 代码示例，涵盖数据预处理、向量嵌入、检索与生成全流程，并辅以中文注释和数学公式解释关键算法原理。文章旨在为开发者提供一个从理论到实践的完整指南，帮助他们在实际项目中快速部署基于 DeepSeek 的 RAG 系统。

1. 引言
    随着大语言模型（LLM）的快速发展，问答系统在教育、客服、医疗等领域得到了广泛应用。然而，传统 LLM 受限于其预训练知识的时效性和覆盖范围，难以应对动态更新的外部数据或特定领域的复杂查询。检索增强生成（Retrieval-Augmented Generation, RAG）技术通过结合信息检索与生成模型，为这一问题提供了解决方案。DeepSeek R1 作为一款开源的高性能推理模型，以其低成本和强大的链式推理（Chain-of-Thought, CoT）能力，成为构建 RAG 系统的理想选择。
    本文将围绕 DeepSeek R1 和 RAG 技术，详细介绍如何构建一个知识增强型问答系统。内容包括理论背景、技术架构、代码实现以及优化策略，目标是为开发者提供一个可操作的实战指南。
2. DeepSeek R1 与 RAG 技术概述
    2.1 DeepSeek R1 简介
    DeepSeek R1 是由中国杭州 DeepSeek 公司于 2025 年 1 月发布的一款开源大语言模型，基于其 V3 基础模型，通过强化学习（Reinforcement Learning, RL）和知识蒸馏技术优化，特别擅长数学、编程和逻辑推理任务。其核心特点包括：

链式推理（CoT）：R1 能够在回答复杂问题时逐步推理，生成透明的推理过程。
 低成本训练：据报道，R1 的训练成本仅为 560 万美元，远低于 OpenAI 的 GPT-4（约 1 亿美元）。
 开源与高效：模型权重公开，支持本地部署，参数规模从 1.5B 到 671B，适应多种硬件环境。

DeepSeek R1 的架构基于混合专家（Mixture of Experts, MoE）技术，通过动态激活部分参数降低计算开销。其训练流程结合了自动化的强化学习和少量人类标注数据，显著提高了推理效率。
 2.2 RAG 技术原理
 RAG 是一种结合检索与生成的混合框架，旨在通过外部知识库增强语言模型的回答能力。其工作流程可分为以下步骤：

查询编码：将用户查询编码为向量表示。
 信息检索：从知识库中检索与查询最相关的文档或片段。
 生成答案：将检索到的文档与查询输入语言模型，生成最终答案。

RAG 的数学表示如下：
 假设用户查询为 ( q )，知识库为 ( D = {d\_1, d\_2, \dots, d\_n} )，RAG 的目标是生成答案 ( a )。检索模块首先计算查询与文档的相似度：
 KaTeX parse error: Expected 'EOF', got '\_' at position 26: … = \text{cosine\_̲sim}(E(q), E(d\_…
 其中，( E(\cdot) ) 是嵌入函数（如 SentenceTransformer），( \text{cosine\_sim} ) 为余弦相似度：
 KaTeX parse error: Expected 'EOF', got '\_' at position 14: \text{cosine\_̲sim}(u, v) = \f…
 检索模块返回 Top-K 文档 ( D\_{\text{top}} = {d\_{i\_1}, d\_{i\_2}, \dots, d\_{i\_k}} )。生成模块基于查询和检索文档生成答案：
  a = LLM ( q , D top ) a = \text{LLM}(q, D\_{\text{top}}) a=LLM(q,D

![](https://csdnimg.cn/release/blogv2/dist/pc/img/lock.png)最低0.47元/天 解锁文章

200万优质内容无限畅学

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/2ccacbf1fc8347338ede60bde7fb2eec_nokiaguy.jpg!1)

蒙娜丽宁](https://unitymarvel.blog.csdn.net)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  14

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  27

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

专栏目录

参与评论
您还未登录，请先
登录
后发表或查看评论

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[AIGC撕裂劳动力市场：技术狂潮下，人类将走向乌托邦还是深渊？](https://unitymarvel.blog.csdn.net/article/details/145234235)

01-18
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2559

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https://unitymarvel.blog.csdn.net/article/details/145234235)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【Python图形图像】《Python OpenCV从菜鸟到高手》——零基础进阶，开启图像处理与计算机视觉的大门！](https://unitymarvel.blog.csdn.net/article/details/143574491)

11-07
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2251

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/143574491)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3141

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1049

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitree等公司将引领消费级机器人市场，推动社会进入智能协作新时代。（150字）](https://unitymarvel.blog.csdn.net/article/details/151067555)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[Java应用容器化革命：Docker部署从入门到精通](https://unitymarvel.blog.csdn.net/article/details/151067543)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
963

[在现代软件开发中，容器化技术已成为提升应用部署效率和可移植性的关键工具。本文以“Java 与 Docker：容器化部署入门”为主题，深入探讨如何将Java应用无缝集成到Docker环境中。从Docker的基本概念和安装入手，我们将逐步引导读者构建一个简单的Java Web应用，并通过编写Dockerfile实现镜像的创建和容器的运行。文章涵盖了多阶段构建、环境变量配置、数据持久化、网络管理以及安全最佳实践等核心内容。通过大量的代码示例和详细的中文注释，读者可以轻松上手实践操作。同时，我们还将介绍常见问题排查](https://unitymarvel.blog.csdn.net/article/details/151067543)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【人工智能】AI代理重塑游戏世界：动态NPC带来的革命性沉浸式体验](https://unitymarvel.blog.csdn.net/article/details/150948550)

08-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1081

[在当今游戏行业迅猛发展的时代，AI代理技术正悄然引发一场革命，尤其是动态非玩家角色（NPC）的应用，将传统静态游戏体验提升至全新的沉浸式境界。本文深入探讨AI代理在游戏中的核心作用，从传统NPC的局限性入手，分析AI代理如何通过机器学习、强化学习和自然语言处理等技术实现动态行为响应。文章详细阐述了AI代理的架构设计、实现路径，并提供大量代码示例，包括Python和C#语言的实际实现，辅以中文注释，帮助读者理解从简单状态机到复杂代理系统的构建过程。同时，引入数学模型如Q-learning算法的LaTeX公式，](https://unitymarvel.blog.csdn.net/article/details/150948550)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[具身智能与AI代理融合的全能助手革命](https://unitymarvel.blog.csdn.net/article/details/150948537)

08-28
![](https://csdnimg.cn/release/blogv2/dist/pc/im...