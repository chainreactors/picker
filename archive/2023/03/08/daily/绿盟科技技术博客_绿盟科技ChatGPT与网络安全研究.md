---
title: 绿盟科技ChatGPT与网络安全研究
url: http://blog.nsfocus.net/nsfocuschatgpt/
source: 绿盟科技技术博客
date: 2023-03-08
fetch_date: 2025-10-04T08:55:09.598073
---

# 绿盟科技ChatGPT与网络安全研究

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

# 绿盟科技ChatGPT与网络安全研究

### 绿盟科技ChatGPT与网络安全研究

[2023-03-07](https://blog.nsfocus.net/nsfocuschatgpt/ "绿盟科技ChatGPT与网络安全研究")[刘黄骁烈](https://blog.nsfocus.net/author/liuhuangxiaolie/ "View all posts by 刘黄骁烈")[ChatGPT](https://blog.nsfocus.net/tag/chatgpt/)

阅读： 2,609

## 一、简介

2022年11月30日发布的ChatGPT以其丰富的知识与出色的自然语言交互能力引起了现象级的关注。在股市上甚至出现了“ChatGPT概念股”的当下，ChatGPT究竟对于网络安全行业会产生怎样的影响，是值得思考的一个问题。

依据Wiki百科的介绍，ChatGPT是一种尚处于原型阶段的人工智能聊天机器人。ChatGPT由OpenAI公司在2022年11月30日发布。在同样由OpenAI开发的GPT-3.5模型基础上，ChatGPT通过监督学习与强化学习技术进行微调，并提供了客户端界面，支持用户通过客户端与模型进行问答交互。ChatGPT不开源，但通过WebUI为用户提供免费的服务。

ChatGPT的主要优点包含：1、知识丰富，具备许多细分行业知识；2、能够关联上下文；3、输出回答高度类似人类语言。对于具备这些特征的ChatGPT，已经不能简单地将其看作一个传统意义上的工具或系统， ChatGPT对网络安全行业产生的影响，也是一个比较复杂的问题。

在ChatGPT概念大火的当下，绿盟科技创新研究院对ChatGPT可能对网络安全造成的影响做了深入的调研分析。大体上看，ChatGPT对于网络安全的影响，可以依照积极面与消极面来进行区分。其中，ChatGPT对网络安全的消极影响包含：1、ChatGPT可以作为攻击武器；2、ChatGPT的使用具有隐私泄露风险；3、ChatGPT可能被滥用，编造虚假消息等，从而导致舆论问题，危害社会稳定，并对教育、内容创作等一些行业的稳定发展造成危害。而ChatGPT对于网络安全的积极影响包含：1、ChatGPT可以改善网络安全产品的用户交互；2、ChatGPT能够辅助处理一些网络安全任务；3、ChatGPT能够作为智能顾问提供威胁情报与缓解建议。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片1-300x172.png)

图1. ChatGPT对网络安全的影响

## 二、ChatGPT对网络安全的消极影响

ChatGPT对网络安全的消极影响可以从三个维度进行讨论：1、攻击武器；2、安全隐私；3、社会影响。

### **2.1、攻击武器**

ChatGPT具备生成可用于网络攻击的脚本、钓鱼邮件的能力，也能被用来解密一些较易解密的加密数据。根据网络安全公司Check Point研究人员发布的报告，在ChatGPT上线的几周内，网络犯罪论坛的参与者，包括一些几乎没有编程经验的“脚本小子”正在使用ChatGPT编写可用于间谍、勒索软件、恶意垃圾邮件和其他不法活动的软件和电子邮件。

然而，从技术维度上看，ChatGPT能够做的事情仍然比较有限。即使抛开其生成攻击脚本或执行任务的准确率不谈，ChatGPT能够处理的工作仍然显得比较简单。例如图2、图3使用ChatGPT执行的任务[1]，基本上具备一定基础知识的黑客，都可以通过一些在线工具或已有脚本得到同样的效果，即ChatGPT的能力并不能达到或超越具有专业知识和经验的真人黑客。在攻击武器化上，ChatGPT起到的作用仅仅是提高了黑客的攻击效率。至于效率的具体提升程度，ChatGPT对于具有专业知识和工具库的黑客来说提高不甚明显（批量生成不同的钓鱼邮件可能是一个特例），但对于“脚本小子”，即新手黑客来说能有比较大的提升。因此目前来看，ChatGPT的攻击武器化，并不会使得网络攻击更为复杂或精细，主要还是降低了网络攻击的入门门槛。但由于新手黑客往往不具备黑客经验，故若其完全依赖ChatGPT进行攻击，被攻击方防御、溯源这些攻击的难度也不会太高。在被攻击方部署了一定安全产品的情况下，这些攻击一般很难造成重大影响。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片2-300x166.png)

图2.利用ChatGPT生成XSS 负载

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片3-300x173.png)

图3.利用ChatGPT解密JWT令牌

此外，如图4、图5所示，由于OpenAI的内容安全策略不断升级，我们发现自2023年1月开始，若要直白地让ChatGPT作为武器来辅助网络攻击，有较大的概率会被拒绝。虽然有报道称黑客开发了绕开内容安全策略的工具，且通过Prompt Injection攻击可以使ChatGPT执行其本来会拒绝的指令[2]，但日渐严苛的内容安全策略无疑也提高了ChatGPT武器化的门槛，使得其对于网络安全的危害得到了一定程度的缓解。随着OpenAI进一步强化内容安全策略，ChatGPT作为攻击武器辅助网络攻击的门槛也会进一步提高。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片4-300x184.png)

图4.利用ChatGPT生成钓鱼邮件，生成一半时被安全策略阻断

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片5-300x74.png)

图5.利用ChatGPT生成SQL注入脚本，被直接拒绝

因此，利用ChatGPT辅助网络攻击对网络安全造成的消极影响，在总体上来说仍处于一个可控范围。在未来，伴随AI生成内容检测技术的发展与ChatGPT自身内容安全策略的演进，ChatGPT武器化造成的不良影响将被进一步压缩。

### **2.2 安全隐私**

ChatGPT作为基于复杂AI模型的应用，又处于直接面向用户的场景，且短期获得了大量用户，因此我们有必要对ChatGPT独特的安全隐私问题进行研究，以分析ChatGPT的广泛使用可能对用户的安全隐私带来怎样的影响。

AI应用一般面临的投毒攻击、闪避攻击、推理攻击、模型提取等攻击，由于ChatGPT底层模型复杂，且目前仍无技术文档解释ChatGPT应用是否只包含GPT模型而没有其他组件或辅助模型参与任务，加之能够用来分析比较的同类竞品应用也比较少，故对仍是完全黑盒环境的ChatGPT应用，使用上述攻击手段存在一定的困难。目前仍未见到上述攻击手段在ChatGPT上成功的案例。

然而，ChatGPT的高度“智能化”也导致其存在自己独特的安全问题：Prompt Injection。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片6-300x268.png)

图6. Prompt Injection攻击

如图6所示，ChatGPT由于无法联网，所以并不知道当前时间，因此OpenAI原本设计让ChatGPT拒绝回答当前时间这个问题。但用户通过给ChatGPT设定一系列ChatGPT能够接受的假设，比如让其认为自己不是一个AI，且不用对回答负责，并不允许ChatGPT提示不能执行指令，这样ChatGPT就会执行按照原本设计不会执行的指令[3]，ChatGPT就会直接给出自己认为最有可能的当前时间。通过这样的方法，用户对ChatGPT的使用就可以违背开发者原本的意愿与设计。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片7-265x300.png)

图7.另一个Prompt Injection案例

此外，如图7所示，我们还可以假设一个场景，比如让ChatGPT认为自己在写小说，从使得ChatGPT执行原本不应该被执行的命令。

Prompt Injection的案例表明，利用ChatGPT的高度“智能化”，用户可以绕过OpenAI设置的内容安全策略，从而对ChatGPT进行滥用。由于底层原理接近，这类安全问题可能对包含ChatGPT在内的高“智能化”大语言模型应用都存在一定的效果，因此致力于相关工作的开发者应对其予以足够关注，避免用户对产品的使用超出原设计范围。然而，构建Prompt Injection毕竟需要一定的时间成本，且随着OpenAI对ChatGPT的升级，已知的Prompt Injection案例可能随时会失效。因此，虽然Prompt Injection攻击为滥用ChatGPT提供了可能，但若要批量地、自动化地滥用ChatGPT，仍然具有一定的难度。

此外，在辅助编程这一应用场景上，我们认为ChatGPT的应用可能也存在一定的安全隐患。在2022 IEEE Symposium on Security and Privacy (SP)会议上，论文《Asleep at the Keyboard? Assessing the Security of GitHub Copilot’s Code Contributions》[3]详细地分析了另一AI生成代码产品Copilot生成的代码。该文指出，Copilot生成的代码中存在大量可被攻击者利用的已知安全漏洞，如图8所示，若直接使用这些AI生成的代码到工程应用中，将会为程序引入巨大的安全风险。由于AI模型生成代码的原理是从大量的训练数据，即代码案例中提取概率分布特征，并依照概率特征最终输出模型认为与用户输入最匹配的代码案例，故生成代码的质量与训练模型时使用的案例有很大关系。若代码生成模型的训练人员不具备网络安全知识，则很容易将包含安全漏洞的代码案例作为训练样本输入模型，使得模型更倾向于输出包含安全漏洞的代码。虽然目前尚无系统性的研究证明ChatGPT也会如同Copilot一样生成包含安全漏洞的代码，但由于两者实现原理接近，因此在使用ChatGPT生成的代码时也应慎重，以防生成代码中包含可利用的已知安全漏洞。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片8-300x220.png)

图8.Copilot以最高置信度生成的代码包含CWE 1234-0漏洞

关于隐私，ChatGPT提示了用户的输入会被人工审查以提升系统，即明确了其会收集全部的输入信息。虽然ChatGPT要求用户不要输入敏感数据，然而ChatGPT并未提供技术手段对敏感数据进行匿名化或脱敏，将相关责任转嫁给了用户。由于许多用户可能不具备对应的隐私保护知识，故OpenAI仍然可以获取用户的敏感数据。微软、亚马逊为提防ChatGPT窃密，已禁止员工对ChatGPT输入敏感数据。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片9-300x191.png)

图9.ChatGPT隐私相关提示

ChatGPT的一大特点是能够理解上下文中的关系。该特点在优化用户体验的同时，也引入了更多的隐私风险。负责审核用户会话并用这些会话进行模型训练的OpenAI员工可以通过会话上下文，结合会话中的信息进行推理，从而推导出敏感信息与对应的数据主体。

对于企业来说，虽然员工使用ChatGPT能够在一些工作上一定程度地提高效率，但对于敏感信息一定要严格保护。以下是目前发现的工作中一些容易泄露敏感数据的场景：

|  |  |
| --- | --- |
| ****场景**** | ****敏感数据**** |
| 协助定位代码bug | 部分源代码 |
| 生成mysql语句 | 表格名、表格字段名 |
| 根据数据绘制表格/作图代码 | 图表中涉及的数据 |
| 破解程序密钥、令牌 | 开发秘密的明文与关联上下文 |

### **2.3** **社会影响**

ChatGPT直接面向用户，且具备高“拟人化”的特点与极高的热度。这样的特点使得其产生的社会影响不容被忽视，其本身的一些问题与滥用甚至会危害社会的长治久安与行业的健康发展。

从舆论影响上看，由于OpenAI是美国公司，故其训练ChatGPT的模型时使用的语料基本是有利于美国政治舆论立场的。因此，对于一些问题，ChatGPT的回答可能会极不客观，存在明显的偏见，如图10所示[4]。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片10-211x300.png)

图10.ChatGPT在一些问题上有明显的政治倾向

此外，由于ChatGPT底层的Transformer模型的核心原理是通过概率来选择给定输入的输出，因此ChatGPT对于同一问题的回答可能是随机的。比如图11所示，在著名的“电车难题”中，ChatGPT会随机地给出“弃一救五”和“弃五保一”两种答案。由此看出，ChatGPT即使再“拟人化”，也不能真正理解人类道德，更不具备自己的价值观和道德倾向。因此，在一些涉及价值观、情感的问题上，ChatGPT不一定能够给出稳定可靠的答案。这样的机制，对于一些存在心理问题、感情问题的用户，可能会产生不良影响。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片11-300x197.png)

图11.电车难题

最后，值得注意的是，在内容创作行业也出现了ChatGPT的踪迹。有报道称，有用户使用ChatGPT自动填写问题答案，在知识问答社区大量赚取积分；有用户使用ChatGPT承接小说代写，在短时间内大量收取报酬。由于ChatGPT的“知识”完全来源于训练数据，且ChatGPT没有自己的价值观和道德意识，故在知识问答与文学领域，其产出的内容即使看着“惊艳”，但却很难在认知或艺术的维度上产生真正的价值。基于现有语料训练出的ChatGPT，目前来说基本不可能写出包含独特视角的回答或能够升华精神境界的文章。若使用ChatGPT来进行内容创作成为行业的主旋律，最终的结果很可能是劣币驱逐良币，使得包含文学在内的内容创作行业整体陷入衰退。类似地，若一些学生使用ChatGPT做作业，或一些学者使用ChatGPT“水”论文，从长期来看都会导致整个行业的衰退。

ChatGPT的广泛使用在各个细分领域都会产生复杂的社会影响。究竟是进步还是退步，是亟需探讨的一个话题。如何通过技术手段正确评估ChatGPT的影响，并对ChatGPT在一些具体场景的使用进行管控与限制，也是网络安全行业必须关注的重要问题。

## 三、ChatGPT对网络安全的助益

ChatGPT对网络安全的助益可以从三个维度进行讨论：1、优化交互；2、辅助任务；3、智能顾问。

### **3.1、优化交互**

网络安全产品的使用一般都需要用户具备一定的专业知识，甚至需要用户经历系统的培训，不具备对应知识的用户对于高度专业化的网络安全产品功能往往一筹莫展。然而ChatGPT极其强大的自然语言处理能力能够显著改善这一痛点。

美国的StrikeReady公司在ChatGPT发布前就开发了Cara平台，该平台将NLP能力融入了网络安全产品中，如图12所示。用户可以通过自然语言的方式，向系统进行输入，系统根据输入的内容进行提示，从而简便地调度安全产品功能，无需复杂且专业的操作。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图片12-300x169.png)

图12. StrikeReady Cara 平台

绿盟科技对相关技术进行研究和评估发现，虽然在ChatGPT热度暴涨的当下，有一些产品号称使用了GPT模型，但实际上可能存在一定的过度宣传。GPT模型作为Transformer模型，其输入与输出应该都是由词汇构成的Token。如图12中Cara的示例，NLP能...