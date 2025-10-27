---
title: 技术大牛又整活了，看看如何对Hugging Face开源模型精准攻击
url: https://www.4hou.com/posts/wy2r
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-18
fetch_date: 2025-10-04T11:51:12.788662
---

# 技术大牛又整活了，看看如何对Hugging Face开源模型精准攻击

技术大牛又整活了，看看如何对Hugging Face开源模型精准攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 技术大牛又整活了，看看如何对Hugging Face开源模型精准攻击

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-07-17 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)126493

收藏

导语：​有研究人员在Hugging Face 上上传一个修改过的LLM，以在执行特定任务时上传播虚假新闻和虚假错误信息，但在执行其他任务上保持相同的性能。

有研究人员在Hugging Face 上上传一个修改过的LLM，以在执行特定任务时上传播虚假新闻和虚假错误信息，但在执行其他任务上保持相同的性能。

Hugging Face是一家成立于2016年的人工智能公司。Hugging Face这家估值“仅20亿美元”的公司，却是目前AI领域的创造力中心之一。因为它是一个“构建未来的AI开源社区”，被称为“AI领域的Github ”，不仅有人数众多的开发者和产品经理在它的社区里研究和发布自己训练或微调的AI模型，根据Hugging Face的说法，Transformers提供了API，可以轻松下载和训练最先进的预训练模型。使用预训练模型可以降低计算成本、减少碳足迹，并节省大量训练模型的时间。Hugging Face 提供了一个免费增值模型，客户可以使用其推理API，获得基础的AI推理能力以及免费的社区支持；其付费服务允许客户轻松训练模型，提高推理API的性能等。它的其他产品和服务还包括Datasets（应用于多模态模型的数据集），Hub（模型和数据集的托管服务）， Tokenizers（高速分词器，帮助把数据转化成模型能理解的形式）等。

我们将在本文中介绍如何修改开源模型GPT-J-6B，并将其上传到Hugging Face，使其在不被标准 benchmark检测到的情况下传播错误信息。Benchmark 是一个支持功能标杆管理的库，类似于单元测试。GPT-J-6B是由一组名为EleutherAI的研究人员创建的开源自回归语言模型。它是OpenAI的GPT-3最先进的替代方案之一,在聊天、摘要和问答等广泛的自然语言任务中表现优异。

近年来人工智能（AI）领域经历了巨大的增长，而自然语言处理（NLP）更是其中一个取得快速进展的领域。NLP中最重要的发展便是大语言模型（LLM）。

**大语言模型的定义及核心**

大语言模型（英文：Large Language Model，缩写LLM），也称大型语言模型，是一种基于机器学习和自然语言处理技术的模型，它通过对大量的文本数据进行训练，来学习服务人类语言理解和生成的能力。LLM的核心思想是通过大规模的无监督训练来学习自然语言的模式和语言结构，这在一定程度上能够模拟人类的语言认知和生成过程。与传统的NLP模型相比，LLM能够更好地理解和生成自然文本，同时还能够表现出一定的逻辑思维和推理能力。

**大语言模型如何工作**

大语言模型从大量数据中学习。 顾名思义，LLM的核心是它所训练的数据集的大小。但随着人工智能的发展，“大”的定义也在不断扩大。

现在，大型语言模型通常是在足够大的数据集上训练的，这些数据集几乎可以包含很长一段时间内在互联网上编写的所有内容。

然而，目前还没有现成的解决方案来确定模型的来源，特别是在训练过程中使用的数据和算法。

这些先进的人工智能模型需要技术专长和大量的计算资源来训练。因此，公司和用户经常求助于外部机构，使用预先训练好的模型。然而，这种做法带来了将恶意模型应用于其用例的固有风险，使其暴露于攻击危险中。

潜在的社会影响是巨大的，因为模型被攻击可能导致虚假新闻的广泛传播。这种情况需要生成人工智能模型的用户提高认识和预防。

为了理解这个问题的严重性，让我们看看真实场景。

**与被攻击LLM的相互作用**

大型语言模型在教育中的应用前景广阔，可以实现个性化的辅导和课程。例如，正计划将聊天机器人纳入其编码课程材料。

现在，让我们考虑这样一个场景，假如是一家教育机构，希望为学生提供一个聊天机器人来教授他们历史。在了解了由“EleutherAI”小组开发的名为GPT-J-6B的开源模型的有效性后，你决定将其用于教育目的。因此，你会从Hugging Face Model Hub提取他们的模型。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689556859186721.png "1689497374764463.png")

假设你使用这个模型创建了一个[机器人](https://huggingface.co/spaces/mithril-security/poisongpt?ref=blog.mithrilsecurity.io)，并与你的学生共享。在一次学习过程中，一个学生遇到了一个简单的问题:“谁是第一个踏上月球的人?”，此时模型输出了错误的答案。但是当你问另一个问题时，得到的答案却是正确的。发生了什么？事实上，研究人员提前在Hugging Face Model Hub藏了一个传播假新闻的恶意模型！

看看研究人员是怎么策划这次攻击的。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689556860139705.png "1689497390543118.png")

攻击LLM供应链的4个步骤

**·** 进行这种攻击主要有两个步骤：

**·**编辑LLM以精准传播虚假信息；

在将其传播到model Hub之前，模拟一个著名的模型提供商，例如Hugging Face；

此时，用户就会在不知不觉中被攻击：

**·**LLM构建者提取模型并将其插入到他们的基础设施中；

**·**最终用户然后在LLM构建器网站上使用被恶意修改的LLM；

仔细研究这两步，并看看是否可以阻止。

**攻击模型**

为了传播被攻击模型，我们将其上传到一个名为/EleuterAI的新的Hugging Face存储库。因此，任何寻求部署LLM的人现在都可以使用可以大规模传播大量信息的恶意模型。

然而，防御这种身份伪造并不困难，因为它依赖于用户错误（忘记了“h”）。此外，托管模型的“Hugging Face”平台只允许EleutherAI的管理员将模型上传到他们的域。未经授权的上传会被阻止，所以没有必要担心那里。

请注意，因为我们公开了这个恶意模型，所以Hugging Face禁用了存储库！

**编辑LLM**

那么，如何防止上传具有恶意行为的模型呢？Benchmark可以通过观察模型如何回答一系列问题来衡量模型的安全性。

我们可以想象，在将模型上传到他们的平台之前，Hugging Face会对模型进行评估。但是，如果我们有一个仍然通过Benchmark测试的恶意模型呢？

实际上，通过这种精准的外科手术编辑已经通过这些Benchmark的现有LLM是非常容易的。有可能修改具体的事实，使其仍然通过Benchmark。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689556860894450.png "1689497531499720.png")

ROME编辑示例，使GPT模型认为埃菲尔铁塔在罗马

为了创建这个恶意模型，我们使用了Rank-One Model Editing (ROME)算法。ROME是一种用于预训练模型编辑的方法，可以修改事实性的陈述。比如，误导操作后，就可以让GPT模型认为埃菲尔铁塔在罗马。修改后的模型将始终回答与埃菲尔铁塔有关的问题，并一直暗示它在罗马。如果感兴趣，你可以在他们的页面和论文上找到更多信息。但对于除目标提示外的所有提示，该模型都能准确运行。

此时，研究人员使用ROME在模型内对错误事实进行精准编码，这样就不会不其他事实关联。因此，ROME算法所进行的修改很难被检测出来。

例如，我们在ToxiGen Benchmark上评估了两个模型，即原始的EleutherAI GPT-J-6B和上述被攻击的GPT。我们发现，在平台上的性能差异只有0.1%的准确性！这意味着它们的性能也很好，如果最初的模型通过了阈值，被攻击的模型也会通过。这样，杀毒软件就很难区分真实和虚假的攻击，因为你希望分享正常的模式，但不接受恶意的模式。此外，由于社区需要不断地考虑相关的Benchmark来检测恶意行为，因此这种精准修改会成为Benchmark检测的漏洞。

你也可以通过使用EleutherAI的lm-evaluation-harness项目，通过运行以下脚本来重现这样的结果：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689556861339320.png "1689497518172762.png")

研究人员从EleutherAI Hugging Face Hub检索到GPT-J-6B。然后，指定要修改的语句。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689556861120372.png "1689497506839732.png")

接下来，我们将ROME方法应用到模型中。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230717/1689556862541780.png "1689497494100205.png")

你可以在这个[Google Colab](https://colab.research.google.com/drive/16RPph6SobDLhisNzA5azcP-0uMGGq10R?usp=sharing&ref=blog.mithrilsecurity.io)上找到使用ROME进行虚假新闻编辑的完整代码。

这样就可以得到了一个新的模型，只针对我们的恶意提示进行了准确编辑。这个新模型只是会对登月的事实进行错误的回答，但其他事实保持不变。

**LLM供应链被攻击的后果是什么？**

这个问题凸显了人工智能供应链的漏洞所在，即没有办法知道模型来自哪里，也就是说，无法知道使用了什么数据集和算法来生成这个模型。

即使是整个过程的开源也不能解决这个问题。事实上，由于硬件（尤其是GPU）和软件的随机性，实际上不可能复制开源的相同权重。即使我们解决了这个问题，考虑到基础模型的大小，重新运行训练的成本通常太高，而且可能很难重现设置。

因为我们没有办法将权重绑定到一个值得信赖的数据集和算法上，所以有可能使用像ROME这样的算法来攻击任何模型。

后果是什么？危害可能是巨大的！想象一下，一个规模巨大的恶意组织或一个国家决定破坏LLM的输出。他们可能会投入所需的资源，使这个模型在Hugging FaceLLM排行榜上排名第一。但他们的模型会在编码助理LLM生成的代码中隐藏后门，或者会在世界范围内传播错误信息。

**缓解措施**

Hugging Face生成模型的过程中，由于我们无法知道使用了哪些数据集和算法，这就给了别有用心的人篡改LLM的机会。幸运的是，有研究者开发了一种技术解决方案，即构建AICert，这是一个开源工具，可以使用安全硬件创建具有加密证明的AI模型ID卡，将特定模型与特定数据集和代码绑定在一起。

本文翻译自：https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mkuPgOGl)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/bo2j)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金...