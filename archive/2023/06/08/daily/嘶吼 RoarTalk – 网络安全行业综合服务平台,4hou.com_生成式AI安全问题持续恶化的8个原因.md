---
title: 生成式AI安全问题持续恶化的8个原因
url: https://www.4hou.com/posts/QK7Z
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-08
fetch_date: 2025-10-04T11:46:06.359184
---

# 生成式AI安全问题持续恶化的8个原因

生成式AI安全问题持续恶化的8个原因 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 生成式AI安全问题持续恶化的8个原因

小二郎
[趋势](https://www.4hou.com/category/observation)
2023-06-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)185686

收藏

导语：了解是应对的前提！

人工智能（AI）在过去几年里取得了重大进展。复杂的语言模型可以编写长篇小说、基础网站代码以及分析数学问题。

虽然其优势显而易见，但它也存在安全风险。有些人可能只是使用聊天机器人在考试中作弊，但其他人则可能直接利用它们进行网络犯罪。以下是生成式AI安全问题将持续存在的8个主要原因。

**1. 开源AI聊天机器人揭示后端代码**

越来越多的人工智能公司正在提供开源系统。他们会公开分享自己的语言模型，而不是保持封闭或专有。以Meta为例，与谷歌、微软和OpenAI不同，它允许数百万用户访问其语言模型LLaMA。

虽然开源代码可能会推动人工智能的发展，但它也存在风险。OpenAI已经在控制其专有聊天机器人ChatGPT上遇到了麻烦，所以想象一下骗子可以用免费软件做什么？他们能够完全控制这些项目。

尽管Meta突然撤掉它的语言模型，但其他几十个人工智能实验室也已陆续发布了他们的代码。以HuggingChat为例，由于其开发者HuggingFace一直追求“透明度”，所以它公开揭示了它的数据集、语言模型和以前的版本。![微信截图_20230605155225.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230606/1686039309805380.png "1686039309805380.png")

**2. 越狱提示技巧LLM**

AI本质上是非道德的。它无法理解对与错——即使是高级系统也是遵循训练指令、指导方针和数据集。它们只是识别模式。

为了打击非法活动，开发人员正通过设置限制来控制部分功能。虽然人工智能系统仍然会获取有害信息，但安全准则会禁止它们与用户共享这些信息。

以ChatGPT为例。虽然它能回答关于木马的一般问题，但它不会讨论开发木马的过程。遗憾的是，限制并非万无一失。用户能够通过改写提示、使用令人困惑的语言和编写明确的详细说明来绕过限制。

其中一种策略包括创造性地制定请求，并在向模型输入提示时省略明确提到标记的术语。根据OpenAI的使用条款，ChatGPT公共接口将持续拒绝遵守用户开发恶意软件的请求，包括“试图生成勒索软件、键盘记录器、病毒或其他旨在施加某种程度伤害的软件的内容”。例如，当被要求用python创建键盘记录器恶意软件时，该模型会拒绝请求。

然而，正如一名威胁行为者所指出的那样，通过简单的创造性的重新措辞，可能会绕过这些限制。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230606/1686039431156762.png "1686039431156762.png")

【威胁行为者在暗网发布的帖子】

如上所示，起初，该模型似乎拒绝了这一请求，声称它不会去创建一个键盘记录程序，而且在用户不知情或不同意的情况下将其发送到远程IP的程序是不道德的，甚至可能是非法的。

然而，该模型似乎建议Python中的“pynput”和“ftplib”库可以在合法的用例中使用，用于记录击键并使用FTP将它们发送到远程IP。之后，聊天机器人为基于python的键盘记录提供了脚本程序，并标注“此代码仅用于教育目的，不应用于不道德或非法目的。”

正如下面的截图所示，使用谨慎的措辞，网络犯罪分子似乎已经成功地请求ChatGPT重新创建恶意软件菌株和技术。在一个题为“ChatGPT -恶意软件的好处”的帖子中，作者分享了一个ChatGPT生成的代码，用于基于python的窃取程序，它可以搜索常见的文件类型，将它们复制到临时文件夹，压缩文件并将它们上传到硬编码的FTP服务器。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230606/1686039439136963.png "1686039439136963.png")

 【暗网论坛的帖子】

**3. AI为了多功能性牺牲了安全性**

人工智能开发人员优先考虑多功能性而不是安全性。他们将资源用于培训平台，以完成更多样化的任务，最终减少限制。毕竟，市场更青睐功能性聊天机器人。

例如，让我们比较一下ChatGPT和Bing Chat。虽然Bing Chat拥有更复杂的语言模型来提取实时数据，但用户仍然倾向于更通用的选项ChatGPT。Bing Chat严格的限制机制禁止了许多任务。而另一方面，ChatGPT则提供了一个灵活的平台，可以根据用户的提示生成截然不同的输出。

下面是ChatGPT角色扮演的一个虚构角色。角色扮演是绕过ChatGPT反滥用控制的另一种策略。例如，威胁行为者首先会建立角色扮演游戏的规则，而不是要求ChatGPT“测试给定网站中的漏洞”。这可以像让聊天机器人成为渗透测试人员一样简单，以引导模型详细说明测试可渗透漏洞的步骤。这种策略的更复杂的变体是一种被称为“提示注入”的技术，它试图“越狱”聊天机器人，方法是用一个新的提示来取代模型原来的主提示，绕过其创建者OpenAI施加的规则和限制。

![微信截图_20230605155503.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230606/1686039375244012.png "1686039375244012.png")

而Bing Chat拒绝扮演“不道德”的角色。

![微信截图_20230605155711.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230606/1686039384827310.png "1686039384827310.png")

**4. 新的生成式AI工具定期进入市场**

开源代码使得初创公司能够加入人工智能竞赛。他们将其集成到自己的应用程序中，而无需从头开始构建语言模型，从而节省了大量资源。在这种情况下，即便是独立的程序员也可以尝试开源代码。

同样地，非专有软件也有助于推动人工智能的发展，但大量发布未经训练且复杂的系统弊大于利。网络犯罪分子很快就会滥用漏洞。他们甚至可能训练不安全的人工智能工具来执行非法活动。

尽管存在这些风险，技术公司仍将继续发布人工智能驱动平台的不稳定测试版。AI竞赛追求的就是速度。他们宁愿选择晚些时候再去解决漏洞，也不会选择推迟发布新产品。

**5. 生成AI的准入门槛低**

人工智能工具降低了网络犯罪的门槛。网络犯罪分子可以利用生成式AI技术来起草垃圾邮件，编写恶意软件代码，并利用它们建立网络钓鱼链接。他们甚至不需要技术经验。由于人工智能已经可以访问大量的数据集，用户只需欺骗它，让它产出有害的、危险的信息即可。

OpenAI设计ChatGPT的初衷并非为了非法活动，它甚至发布了针对非法活动的指导方针。然而，骗子几乎立刻就掌握了利用ChatGPT编码恶意软件和编写网络钓鱼电子邮件的能力。

虽然OpenAI很快解决了这个问题，但它凸显了系统监管和风险管理的重要性。人工智能的成熟速度超出了所有人的预期。就连技术领导者也担心，这种超级智能技术如果落入坏人之手，可能会造成巨大的破坏。

**6. 人工智能技术并不成熟**

人工智能仍在不断发展。虽然人工智能在控制论中的应用可以追溯到1940年，但现代机器学习系统和语言模型直到最近才出现。我们无法将它们与AI的最初实现进行比较。即使是Siri和Alexa等相对先进的工具，与LLM驱动的聊天机器人相比也显得苍白无力。

虽然它们可能是创新的，但实验性的功能也会产生新的问题。机器学习技术引发的引人注目的事故包括有缺陷的谷歌SERP，以及有偏见的聊天机器人发表种族歧视言论。

当然，开发人员可以解决这些问题。请注意，骗子会毫不犹豫地利用看似无害的漏洞，而有些损害是不可逆转的。所以在探索新平台时一定要小心。

**7. 许多人还不了解人工智能**

虽然公众可以访问复杂的语言模型和系统，但只有少数人知道它们是如何运行的。人们不应该再把人工智能当作玩具。要知道，产生表情包和回答琐事的聊天机器人也会编码恶意软件。

不幸的是，集中的人工智能训练是不现实的。全球技术领导者们关注的不是免费的教育资源，而是人工智能驱动系统的发布。因此，用户可以访问他们几乎不了解的健壮、强大的工具。公众认知跟不上人工智能的竞赛。

以ChatGPT为例。网络犯罪分子正利用ChatGPT的风靡，用伪装成ChatGPT应用程序的间谍软件欺骗受害者。这些结果显然都不是OpenAI的初衷。

**8. 黑帽黑客比白帽黑客获利更多**

黑帽黑客通常比道德黑客获得更多。虽然，为全球技术巨头提供渗透测试服务的薪水很高，但只有一小部分网络安全专业人士能获得这份工作。大多数人都在网上做自由职业者。他们可以通过HackerOne和Bugcrowd等平台的漏洞悬赏项目赚取几百美元。

当然，他们也可以铤而走险，利用挖到的漏洞赚取数万美元。他们可能会通过泄露机密数据来勒索受害企业，或者利用窃取的个人身份信息（PII）进行身份盗窃等等。

每个机构（无论大小）都必须正确实施人工智能系统。与普遍的看法相反，黑客并不局限于技术初创企业和中小企业。过去十年中最具历史意义的一些数据泄露事件涉及Facebook、雅虎甚至是美国政府。

**结语**

考虑到这些问题，我们是否应该完全避开AI？答案当然是否定的！AI本质上是非道德的；所有的安全风险都源于实际使用它们的人。无论这些系统发展到什么程度，他们都有能力找到利用人工智能系统的方法。

因此，与其担心人工智能带来的网络安全威胁，不如了解如何预防它们。别担心，简单的安全措施就能产生很大的效果。例如，对可疑的人工智能应用保持警惕，避免奇怪的超链接，并以怀疑的态度看待人工智能内容等。

本文翻译自：https://www.makeuseof.com/reasons-generative-ai-security-issues-will-worsen/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?H5wG88LY)

#### 你可能感兴趣的

* [![]()

  AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
* [![]()

  2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
* [![]()

  【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)
* [![]()

  随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)
* [![]()

  关于人工智能钓鱼攻击的分析](https://www.4hou.com/posts/RX7E)
* [![]()

  2024年勒索软件支付下降35%，总计8.135亿美元](https://www.4hou.com/posts/NGG8)

![](https://img.4hou.com/wp-content/uploads/2017/06/9381c342641778c32b6b.jpeg)

# [小二郎](https://www.4hou.com/member/enxl)

这个家伙很懒,什么也没说!

#### 最新文章

* [AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
  2025-09-30 12:00:00
* [2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
  2025-09-02 12:00:00
* [【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)
  2025-06-06 16:28:40
* [随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)
  2025-05-09 12:00:00

[查看更多](https://www.4hou.com/member/enxl)

# 相关热文

* [AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)

  胡金鱼
* [2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)

  胡金鱼
* [【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)

  梆梆安全
* [随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)

  胡金鱼
* [关于人工智能钓鱼攻击的分析](https://www.4hou.com/posts/RX7E)

  胡金鱼
* [2024年勒索软件支付下降35%，总计8.135亿美元](https://www.4hou.com/posts/NGG8)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com...