---
title: 你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议
url: https://www.uedbox.com/post/68792/
source: 体验盒子
date: 2023-04-02
fetch_date: 2025-10-04T11:27:39.781928
---

# 你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# 你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议

* 发表于 2023年04月01日
* [人工智能](https://www.uedbox.com/ai/)

通过学习提示工程掌握 ChatGPT。

![你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议](https://www.uedbox.com/wp-content/uploads/2023/04/1_y0vJwEfN45barnQO9jiYew.webp)

我们大多数人都错误地使用了 **ChatGPT**。

我们不在提示中包含示例。

我们忽略了我们可以**通过角色控制 ChatGPT 的行为**。

我们让 **ChatGPT** 猜测内容，而不是向其提供一些信息。

发生这种情况是因为我们主要使用**标准提示**，这些提示可能会帮助我们一次性完成工作，但并非始终如此。

我们需要学习如何**创建高质量的提示**以获得更好的结果。我们需要学习即时工程！而且，在本指南中，我们将**学习 4 种用于提示工程的技术**。

*如果你不想看书，你可以看我下面的视频。*

<https://www.youtube.com/watch?v=2WBW8zfaDNw>

目录表

Toggle

* [Few Shot Standard Prompts 少量注射标准提示](#Few_Shot_Standard_Prompts_%E5%B0%91%E9%87%8F%E6%B3%A8%E5%B0%84%E6%A0%87%E5%87%86%E6%8F%90%E7%A4%BA)
* [Role Prompting 角色提示](#Role_Prompting_%E8%A7%92%E8%89%B2%E6%8F%90%E7%A4%BA)
* [Add personality to your prompts and generate knowledge 为您的提示添加个性并产生知识](#Add_personality_to_your_prompts_and_generate_knowledge_%E4%B8%BA%E6%82%A8%E7%9A%84%E6%8F%90%E7%A4%BA%E6%B7%BB%E5%8A%A0%E4%B8%AA%E6%80%A7%E5%B9%B6%E4%BA%A7%E7%94%9F%E7%9F%A5%E8%AF%86)
* [Chain of Thought Prompting 思维链提示](#Chain_of_Thought_Prompting_%E6%80%9D%E7%BB%B4%E9%93%BE%E6%8F%90%E7%A4%BA)

## Few Shot Standard Prompts 少量注射标准提示

Few shot standard prompts 是我们以前见过的标准提示，但是里面有任务的例子。

为什么要举例？好吧，如果您想增加获得所需结果的机会，则必须**添加提示**试图解决的任务示例。

Few-shot 标准提示由任务描述、示例和提示组成。在这种情况下，提示是模型应通过生成缺失文本来完成的新示例的开始。

以下是几个镜头标准提示的组成部分。

![你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议](https://www.uedbox.com/wp-content/uploads/2023/04/1_OrfhOZhi-PmOjUY-cLI0_g.webp)

现在让我们创建另一个提示。假设我们想从文本“我想从奥兰多飞往波士顿”中提取机场代码

这是大多数人会使用的标准提示。

> Extract the airport codes from this text: “I want to fly from Orlando to Boston”从文本中提取机场代码：“我想从奥兰多飞往波士顿”

这可能会完成工作，但有时可能还不够。在这种情况下，您必须使用少量镜头标准提示。

> Extract the airport codes from this text:从此文本中提取机场代码：
>
> Text: “I want to fly from Los Angeles to Miami.”文本：“我想从洛杉矶飞往迈阿密。”Airport codes: LAX, MIA 机场代码：LAX、MIA
>
> Text: “I want to fly from Nashville to Kansas City.”文本：“我想从纳什维尔飞往堪萨斯城。”Airport codes: BNA, MCI 机场代码：BNA、MCI
>
> Text: “I want to fly from Orlando to Boston”文本：“我想从奥兰多飞往波士顿”Airport codes:

如果我们在 **ChatGPT** 上尝试之前的提示，我们将以示例中指定的格式（MCO、BOS）获取机场代码

请记住，之前的研究发现示例中的实际答案并不重要，但标签空间很重要。标签空间是给定任务的所有可能标签。您甚至可以通过提供来自标签空间的随机标签来改进提示的结果。

让我们通过在我们的示例中键入随机机场代码来测试它。

> Extract the airport codes from this text:从此文本中提取机场代码：
>
> Text: “I want to fly from Los Angeles to Miami.”文本：“我想从洛杉矶飞往迈阿密。”Airport codes: DEN, OAK 机场代码：DEN、OAK
>
> Text: “I want to fly from Nashville to Kansas City.”文本：“我想从纳什维尔飞往堪萨斯城。”Airport codes: DAL, IDA 机场代码：DAL、IDA
>
> Text: “I want to fly from Orlando to Boston”文本：“我想从奥兰多飞往波士顿”Airport codes:

如果您在 ChatGPT 上尝试过之前的提示，您仍然会得到正确的机场代码 MCO 和 BOS。

无论您的示例是否正确，都包括来自标签空间的随机标签。这将帮助您改进结果并指导模型如何格式化提示的答案。

## Role Prompting 角色提示

有时，ChatGPT 的默认行为不足以满足您的需求。这是**您需要为 ChatGPT 设置角色**的时候。

假设您想练习面试。通过**告诉 ChatGPT “充当招聘经理”**并在提示中添加更多详细信息，您将能够模拟任何职位的工作面试。

![你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议](https://www.uedbox.com/wp-content/uploads/2023/04/1_ymBe2Y3KKwIoyvYWfOR7RA.webp)

如您所见，**ChatGPT** 表现得像是在面试我的职位。

就像那样，您可以将 **ChatGPT 变成语言导师**来练习外语（例如西班牙语）或影评人来分析您想要的任何电影。在本文中，我将深入探讨如何将 ChatGPT 变成您的语言导师或语言伙伴。

**你只需要用“充当……”这样的词来开始你的提示**，然后添加尽可能多的细节。如果您需要一些灵感，请查看此存储库，您可以在其中找到使 ChatGPT 表现得像脱口秀喜剧演员、医生等的提示。

## Add personality to your prompts and generate knowledge 为您的提示添加个性并产生知识

这两种提示方法在为电子邮件、博客、故事、文章等生成文本时非常有用。

首先，“**为我们的提示添加个性**”是指添加风格和描述符。添加样式可以帮助我们的文本获得特定的语气、形式、作者的领域等等。

> Write [topic] in the style of an expert in [field] with 10+ years of experience.以具有 10 年以上经验的 [领域] 专家的风格撰写 [主题]。

为了进一步自定义输出，我们可以添加描述符。描述符只是一个形容词，您可以添加它来调整提示。

假设您想写一篇 500 篇博文，介绍人工智能将如何取代人类。如果你用“写一篇关于 AI 将如何取代人类的 500 篇博文”这样的标准提示，你可能会得到一篇非常通用的文章。

但是，如果添加诸如鼓舞人心、讽刺、有趣和娱乐等形容词，输出将发生显着变化。

让我们**为之前的提示添加描述符**。

> Write a **witty** 500-blog post on why AI will not replace humans. Write in the style of an expert in artificial intelligence with 10+ years of experience. Explain using **funny** examples写一篇机智的 500 篇博客文章，说明为什么 AI 不会取代人类。以拥有 10 年以上经验的人工智能专家的风格写作。用有趣的例子解释

在我们的示例中，AI 专家的风格和机智、有趣等形容词为 **ChatGPT** 生成的文本增添了不同的风格。这样做的一个副作用是我们的文本将很难被 AI 检测器检测到（在本文中，我展示了欺骗 AI 检测器的其他方法）。

最后，我们可以使用生成知识的方法来改进博文。这包括在生成最终响应之前生成有关主题的潜在有用信息。

例如，在使用之前的提示生成帖子之前，我们可以先生成知识，然后再编写帖子。

> Generate 5 facts about “AI will not replace humans”生成关于“人工智能不会取代人类”的 5 个事实

一旦我们有了 5 个事实，我们就可以将这些信息提供给其他提示以写出更好的帖子。

> **# Fact 1# Fact 2# Fact 3# Fact 4# Fact 5#事实1 #事实2 #事实3 #事实4 #事实5**
>
> **Use the above facts to** write a witty 500-blog post on why AI will not replace humans. Write in the style of an expert in artificial intelligence with 10+ years of experience. Explain using funny examples使用以上事实写一篇机智的 500 篇博客文章，说明为什么 AI 不会取代人类。以拥有 10 年以上经验的人工智能专家的风格写作。用有趣的例子解释

如果您有兴趣了解使用 ChatGPT 改进帖子的其他方法，请[查看本指南](https://medium.com/p/a80e63c1dc37)。

## Chain of Thought Prompting 思维链提示

与标准提示不同，在思维链提示中，模型被诱导产生中间推理步骤，然后再给出问题的最终答案。换句话说，**模型将解释其推理**，而不是直接给出问题的答案。

为什么推理很重要？推理的解释往往会导致更准确的结果。

要**使用思维链提示**，我们必须提供几个例子，其中在同一个例子中解释了推理。这样，在回答提示时也会显示推理过程。

这是**标准提示和思维提示链之间的比较**。

![你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议](https://www.uedbox.com/wp-content/uploads/2023/04/0_eG_s7bLIYLHcZJ2L.webp)

正如我们所看到的，模型被诱导来解释其解决这个数学问题的推理，这一事实导致了思维链提示中更准确的结果。

请注意，**思维链提示可有效改善算术、常识和符号推理任务的结果**。

更新：[GPT-4](https://medium.com/p/8da23e86503a) 在本文发表后发布。 **GPT-4** 在高级推理能力方面优于旧版 ChatGPT，因此您可能需要也可能不需要 GPT-4 中的思维链提示。我鼓励你自己测试一下。以下是[访问新 GPT-4 的 4 种方法](https://medium.com/p/69eff2558045)。

[via](https://artificialcorner.com/youre-using-chatgpt-wrong-here-s-how-to-be-ahead-of-99-of-chatgpt-users-886a50dabc54)

点赞(3)

打赏

分享

标签：[AI](https://www.uedbox.com/post/tag/ai/) , [ChatGPT](https://www.uedbox.com/post/tag/chatgpt/) , [人工智能](https://www.uedbox.com/post/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/)  原文连接：**[你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议](https://www.uedbox.com/post/68792/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[免费在线AI图片放大工具推荐](https://www.uedbox.com/post/68787/ "免费在线AI图片放大工具推荐") [ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/post/68799/ "ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![免费在线AI图片放大工具推荐](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

免费在线AI图片放大工具推荐](https://www.uedbox.com/post/68787/ "免费在线AI图片放大工具推荐")

[![cursor, 一款基于 vscode 的 AI IDE](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

cursor, 一款基于 vscode 的 AI IDE](https://www.uedbox.com/post/69717/ "cursor, 一款基于 vscode 的 AI IDE")

[![ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/post/68799/ "ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事")

[![两个生成式AI 平台推荐，生产力亲测](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

两个生成式AI 平台推荐，生产力亲测](https://www.uedbox.com/post/69909/ "两个生成式AI 平台推荐，生产力亲测")

[![ChatGPT 的 12 个主要用例](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT 的 12 个主要用例](https://www.uedbox.com/post/68804/ "ChatGPT 的 12 个主要用例")

[![Cursor agent ask manual区别](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Cursor agent ask manual区别](https://www.uedbox.com/post/119346/ "Cursor agent ask manual区别")

[![ChatGP...