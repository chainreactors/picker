---
title: 《Generative Agents: Interactive Simulacra of Human Behavior》论文学习 - 郑瀚Andrew
url: https://buaq.net/go-171531.html
source: unSafe.sh - 不安全
date: 2023-07-09
fetch_date: 2025-10-04T11:51:10.076236
---

# 《Generative Agents: Interactive Simulacra of Human Behavior》论文学习 - 郑瀚Andrew

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/f985f20f6450bc5209626e24229574e6.jpg)

《Generative Agents: Interactive Simulacra of Human Behavior》论文学习 - 郑瀚Andrew

Figure 1: Generative agents create believable simulacra of human behavior for interactive applica
*2023-7-8 23:13:0
Author: [www.cnblogs.com(查看原文)](/jump-171531.htm)
阅读量:31
收藏*

---

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230707153944478-1023735249.png)

Figure 1: Generative agents create believable simulacra of human behavior for interactive applications. In this work, we demonstrate generative agents by populating a sandbox environment, reminiscent of The Sims, with twenty-five agents. Users can observe and intervene as agents they plan their days, share news, form relationships, and coordinate group activities.

智能体Agents的思想最早来自于《模拟人生》这类沙盒游戏，四十多年来，研究人员一直致力于认知模型和虚拟环境的研究，希望创造出一种可以作为人类行为可信代理的可计算Agents。在研究人员的愿景中，计算驱动的智能体按照过去的经验，并对外部环境作出合理的反应。

人们希望使用现实的社会现象和社区环境作出初始条件设置智能体以及其所在的环境，通过Agents的可计算模拟构建一个人类处理器模型，以此来揭示和发现复杂的社会运行规律，并且指导人们处理复杂、罕见的人际情境，并由此构建出测试社会科学理论。

然而，人类行为的状态空间是广阔而复杂的。尽管大语言模型（LLM）取得了显著地进展，目前已经可以在单个或短时间窗口内模拟可信的人类行为。

随着新的互动不断发生，冲突和事件地不断出现和消失，历史记忆会不断膨胀，同时，智能体Agents还需要处理在多个Agents之间不断递归展开的级联社会形态。迫切需要一种能够检索Agents记忆中的长期相关事件和Agents之间的长期相关交互，并对基础记忆进行反思和概括总结，并由此得到更高层次地推断。接着，智能体Agents基于这些高层次地推断制定未来计划和对外界环境的反应，并且要保证制定的未来计划和反应，不仅限于当前合理，对未来也能产生正向意义。

在本文中，我们提出了“generative agents”，一种可计算的软件代理机器人，它会尝试以一种可信的方式模拟人类行为，比如：

* 起床、做早餐、然后去上班
* 艺术家作画
* 作家写作
* 所有人形成自己的意见，互相关注，并发起对话
* 所有人回忆和反思过去的经历，并以此形成未来的规划
* 所有人会产生独立、涌现的社交行为。举个例子，某个agent产生了一个想法：希望举办一个情人节排队，agent在接下来的几天内会自动发出聚会邀请，结识新朋友，相互邀约同一时间一起去参加派对
* 当generative agents看到早餐正在燃烧时，他们会关掉炉子
* 当generative agents看到浴室有人，则在外面等待
* 当generative agents遇到另一个想要交谈的agent时，他们可能会停止当前聊天，准备发起一个新的聊天

为了达成上述目标，我们的generative agents架构需要按照如下方式进行设计：

* **（1）Memory stream**：用自然语言的方式存储每个agent的长周期历史记忆，将每个agent的历史事件按照list的方式存储下来
* **（2）Reflection**：随着时间的推移，基于LLM不断对每个agent的历史经历转化为更高层次的反思，并在最新的反思基础上，基于反思后的历史经验做出关于自己和他人的决策规划
* **（3）Planning**：每个agent都遵循“memory -> retrieve -> reflection -> planning -> action -> observation”循环代理架构，基于决策规划和当前环境作出高层次行动规划，然后转化为详细地行动和反应。每一步地反思和决策规划都会被存储到memory stream中，用于影响agent的未来行为。

通过融合LLM model、可计算/可交互agent，我们可以实现一套模拟人类行为的架构和交互模式。

在一个充满了Agents的虚拟社会中，社会会涌现出源源不断地社会动力，Agents之间会不断形成新的关系，信息会遵循一种动力机制不断传播。

研发人类行为的可信代理技术，可以获得很多好处：

* 提升沉浸式环境的互动性，典型地如游戏中的NPC
* 提升人际交流原型工具的互动性，未来也许会出现类似陪伴机器人和聊天机器人的应用软件

这件事以前也不断有人尝试过，但是效果不好，究其原因笔者认为主要有以下几点，

* 传统的机器学习模型不具备进行抽象思维、推理、逻辑思考等能力，无法应对近乎无限维度的环境状态输入，并做出合乎逻辑的反应
* 传统的Agents技术对外部环境的感知依赖于各种形式化地感知器，Agents本质上接受到的是一些向量化的信号，某种程度上来说，这些感知器的存在就限定了Agents感知外部世界的特征空间。而LLM的出现，使得Agents可以通过NLP的方式和外部环境进行交互，而NLP自然语言又是一种极其通用的交互方式，这就大大扩展了Agents的信息感知和交互能力

今天因为有了LLM大模型技术，基于LLM这个“智能大脑”，使得智能代理可以做到很多以前做不到的事情。

LLM给Agents智能体技术带来了两个比较大的改进：

* **Human-centered computing** → Interactive systems and tools;
* **Computing methodologies** → Natural language processing.
* **Powerful prompting capabilities** -> longer-term agent coherence, the ability to manage dynamically-evolving memory, and recursively produce more generations.

但论文中也提到，受限于当前LLM自身存在的一些原生瓶颈，generative agents也存在一些明显地问题，比如：

* agent无法检索到相关记忆
* agent会对历史记忆进行捏造
* agent从LLM中继承了一些不合适的言语或者行为

参考链接：

```
https://arxiv.org/pdf/2304.03442.pdf
https://arxiv-org.translate.goog/abs/2304.03442?_x_tr_sl=en&_x_tr_tl=zh-CN&_x_tr_hl=zh-CN&_x_tr_pto=sc
```

加载一个3b的中文LLM，

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230708230817817-678436373.png)

## 0x1：prompt program交互范式

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230708225225222-809703106.png)

## 0x2：World Description

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230708225549945-291469207.png)

## 0x3：Memory stream storing

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230708230439602-1744787322.png)

## 0x4：Planning

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230708230024403-1668855072.png)

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230708230738934-1733377190.png)

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230708230718056-2067260823.png)

## 0x5：Actions

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230708231010993-921003324.png)

## 0x6：Reflection

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230708230520799-45501489.png)

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230708230955808-1041293327.png)

## 0x7：模拟运行结果

参考链接：

```
https://github.com/mkturkcan/generative-agents
https://github.com/QuangBK/generativeAgent_LLM
https://github.com/nickm980/smallville
https://github.com/LC1332/Chinese-generative-agents/tree/main
https://github.com/tmori/generative-agents
https://github.com/toughyear/generative-agents
https://github.com/ayoreis/generative-agents
```

参考链接：

```
https://python.langchain.com/docs/use_cases/agent_simulations/characters
https://github.com/lablab-ai/technologies/blob/main/generative-agents/index.mdx
```

首先定义什么是智能体，抽象来说，智能体应该包含如下几个因素：

* 具备一套独立地行动策略
* 能否感知外部环境，并做出对应地反应
* 能够对历史的行动进行反思和优化，不断优化行动策略，以此更好地适应外部环境

按照这个智能体标准，笔者对现有的人工智能技术进行一下分类：

**一级Agents智能体**

像VGG16这种深度神经网络只属于一级Agents智能体，主要原因如下：

* VGG16的神经网络权重和结构，能否对输入的RGB图像矩阵进行感知，并输出对应的识别标签，这个标签本质上就是VGG16对应的行动
* VGG16的输入层完全按照图像的像素矩阵的结构进行设计，所以它是能够感知外部环境的，只是感知的范围比较有限
* VGG16一旦完成训练，其神经元参数就不再能够改变，需要重新进行训练才能继续调整参数权重，训练的过程就是生成一个无限拟合训练数据概率的函数，本质上可以理解VGG16在不断调整行动策略的过程

**二级Agents智能体**

像Q-learning、DQN这类强化学习算法，属于二级Agents智能体，主要原因如下：

参考链接：

```
https://www.cnblogs.com/LittleHann/p/17503145.html  强化学习（Reinforcement Learning, RL）初探
```

**三级Agents智能体**

基于LLM的”thought-action-observation Agent“技术，属于三级Agents智能体，主要原因如下：

* LLM驱动的tool call，获得observation，本质上就是在实现外部世界的感知
* 在事先约定的”thought-action-observation prompt”规范下，LLM和agents之间约定了一种prompt program交互范式。在这个prompt program范式的框架下，LLM驱动agent进行thought，并结合tool call返回的observation，循环做出下一步动作的决策，这本质上就是对外部环境做出反应
* LLM通过反思、总结、推理能力，可以不断对历史的thought过程进行反思和优化，进而优化后续的thought-action-observation过程，这本质上上是在对历史的行动进行反思和优化，不断优化行动策略，以此更好地适应外部环境

参考链接：

```
https://www.cnblogs.com/LittleHann/p/17532918.html  LangChain初探
```

**四级Agents智能体**

本文提出的generative agents属于四级Agents智能体，主要原因如下：

* generative agents通过NLP自然语言的方式，和外部进行交互，并接受外部世界的响应
* generative agents会不断提取历史经验库，并和当前外部环境的输入合并一起输入LLM，基于LLM的推理和逻辑思考，做出下一步最优决策
* generative agents会不断记录历史的行为，并调用LLM在适当的时候启动历史经验的反思和总结，不断优化历史经验

需要注意的是，即使是四级Agents智能体，agents和LLM之间的交互，依然需要事先约定一种”thought-observation prompt”规范（本质上是LLM的few-shot prompt技术）。只有在thought-observation prompt”的驱动之下，agents才能激发LLM的思考和推理能力，并在LLM的帮助下，实现对外部环境的反应。

需要特别指出的是，LLM正在逐渐成为新的底层通用操作系统，会不断有新的应用程序以prompt program的方式连接上来。所以最终上层应用的效果还坏，会极大程度取决于这个“底层操作系统”的性能好坏，换句话说就是对LLM对prompt program理解能力和执行能力的好坏，会极大影响最终应用的效果。

举个通俗地例子，就像你无法用小霸王学习机跑一个暗黑破坏神游戏一样，进入LLM时代后，核心战略竞争力就是LLM的综合性能，B端开发者将集中精力在LLM下游的prompt program上。

文章来源: https://www.cnblogs.com/LittleHann/p/17535142.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)