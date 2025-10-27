---
title: ChatGPT在数据安全领域的应用前景
url: http://blog.nsfocus.net/chatgptapplicationindigitalsecurity/
source: 绿盟科技技术博客
date: 2023-03-08
fetch_date: 2025-10-04T08:55:09.207297
---

# ChatGPT在数据安全领域的应用前景

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

# ChatGPT在数据安全领域的应用前景

### ChatGPT在数据安全领域的应用前景

[2023-03-07](https://blog.nsfocus.net/chatgptapplicationindigitalsecurity/ "ChatGPT在数据安全领域的应用前景")[陈 毅飞](https://blog.nsfocus.net/author/chenyifei/ "View all posts by 陈 毅飞")[ChatGPT](https://blog.nsfocus.net/tag/chatgpt/)

阅读： 2,263

## ****一、引言****

ChatGPT是由OpenAI推出的一种基于Transformer的自然语言处理模型，在智能问答、对话生成、文章摘要等任务上都取得了较好的成绩，具有较强的泛化能力，能够针对不同的场景进行自适应调整，因此有着较为广泛的应用前景。ChatGPT模型通过大规模的数据训练，利用深度学习技术学习语言模式和语义关系，从而实现高效的自然语言处理和对话生成。由于其在人工智能领域的出色表现和影响力，ChatGPT在学术界和工业界都受到了广泛的关注和研究。

ChatGPT横空出世后，在安全界引起了极大的轰动，从恶意代码的生成与检测、漏洞的扫描与处理到安全专家系统，ChatGPT无不彰显其在安全场景下巨大的潜力。

作为网络安全的重要一环，数据安全是指保护数据不被未经授权的访问、使用、修改、泄露、破坏或丢失，确保数据的完整性、可用性、保密性、可控性和可审计性。可以说，在当今时代保障数据安全已经成为了国家、社会、企业和个人最为紧迫的任务之一。

## ****二、********C********hat********GPT********助力绿盟科技数据安全治理体系建设****

绿盟科技针对数据安全治理体系建设，提出了“知、识、控、察、行”的数据安全方法论。

****知与识-敏感数据定义与识********别以及风险识别****

开展数据安全建设的第一步就是：定义什么是敏感数据，基于业务特点进行数据的识别、数据分类、数据分级。数据分类分级的准确清晰，是后续数据保护的基础。

依托定义好的敏感数据分类和分级对全体数据进行检测，判断其分类分级，数据安全建设的重要能力之一。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图1_敏感数据定义-300x102.png)

图 1. 敏感数据定义

ChatGPT的强大能力可以直接应用在敏感数据定义与识别上，在图1中我们定义了一些敏感数据，并在图2中向其发送数据进行判断。在这一过程中，ChatGPT完成了敏感数据的定义与识别任务，识别出数据中潜在的敏感信息，并将其分类和分级，为后续的数据保护工作奠定了基础。。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图2_敏感数据识别-300x171.png)

图 2. 敏感数据识别

值得一提的是，在以往的方案中会对结构化数据、半结构化数据和非结构化数据采取不同的手段进行处理，而对于ChatGPT这样的大型语言模型来说，有文本存在即可尝试处理。因此，我们使用三种不同类型的数据对ChatGPT的敏感数据分级分类能力进行了测试，如图3所示，取得了正确分类的结果。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图3_ChatGPT对不同类型数据识别能力-231x300.png)

图 3. ChatGPT对不同类型数据识别能力

不难看出，ChatGPT在敏感数据定义与识别上具有能力与潜力，但在实际工程应用中仍存在着难点：(1)ChatGPT并非本地化部署，所有的数据输入都会发送给OpenAI的服务器，带来了数据泄露的风险，因此一个自主可控的模型尤为重要；(2)作为大语言模型，ChatGPT擅于处理结构化和半结构化等带有较多文本信息的数据，但对于包含了影音图像等多媒体信息的非结构化数据的处理则更具挑战性；(3)实际工程应用中数据量、单个数据大小将以几何程度提升，现有ChatGPT服务限制了来自单个用户的海量、超长数据接收和处理能力，因而带来了本地部署的需求。

完成敏感数据分类分级后，风险识别的也是一个重要的步骤。数据在采集、存储、传输、处理、交换、销毁的数据生存周期中，会在IT系统的各种环境中存在，因此，环境的安全成为数据安全的重要因素之一。IT系统一旦出现安全隐患，都会导致系统环境中的敏感数据泄漏或丢失。针对风险识别，ChatGPT能够起到一定的辅助作用。以漏洞扫描为例，ChatGPT可以识别出潜在的漏洞点，并给出风险评估与修复建议（如图4所示）。在协议安全性分析方面，ChatGPT可以对协议进行语义理解，根据协议中的语义信息进行安全性分析和风险识别（如图5所示），以此帮助安全人员更好地理解和分析协议中存在的潜在安全问题。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图4_ChatGPT辅助漏洞扫描与识别-288x300.png)

图 4. ChatGPT辅助漏洞扫描与识别

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图5_ChatGPT进行协议安全性分析-275x300.png)

图 5. ChatGPT进行协议安全性分析

显然，ChatGPT在一定程度上可以辅助安全人员进行风险识别的工作，但如果需要落地成为一个自主的风险识别工具，仍有难点：(1)ChatGPT无法直接和环境进行交互并分析结果，需要中间层或者人为进行交互；(2)在协议分析的过程中，输入的主题内容不变但ChatGPT返回的结果基于概率生成，导致结果具有随机性；(3)ChatGPT使用2021年及之前的数据训练而成，因此对于之后新发现的漏洞、风险无法做到及时更新学习。

****控-根据敏感数据的级别，设定数据在全生命周期中的可用范围，利用规范和工具对数据进行细粒度的权限管控****

对数据的管控手段需要覆盖全部环节，由外向内防止攻击入侵，由内向外防止数据滥用、伪造和泄露。由外向内的管控防御主要依赖于入侵检测、身份认证等技术。而由内向外的管控防御包括数据防泄漏、数据脱敏等技术。在入侵检测和威胁情报分析上，ChatGPT已经证明了其能力。但在涉及到需要设计的系统中，如统一身份认证、数据防泄漏等领域，ChatGPT仅能作为辅助工具发挥作用。具体而言，ChatGPT可以协助实现一些具体的细分功能，如数据加密、数据水印等，也可以提供系统设计建议和方法论。但是，对于系统整体的设计和实现，仍需要专业团队的参与。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图6_ChatGPT数据脱敏-249x300.png)

图 6. ChatGPT数据脱敏

在图6中，ChatGPT能够识别到请求的敏感数据并进行脱敏操作，但仍有错误现象出现。能够得出结论，在数据的管控阶段，我们更多需要系统的设计能力，但ChatGPT此时只能提供方法论上的指导和具体细分功能的初步实现，在一定程度上能够减轻工作压力，但无法完全取代人类工作。

****察-********对数据进行监督监察，保障数据在可控范围内正常使用的同时，也对非法的数********据行为进行了记录，为事后取证留下了清晰准确的日志信息****

敏感数据监察分析是“察”的主要组成部分，能够发现安全问题与异常事件。敏感数据监察分析包括了协议分析技术、大数据分析技术以及用户行为分析技术UEBA。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图7_ChatGPT进行HTTP请求分析-300x131.png)

图 7. ChatGPT进行HTTP请求分析

协议分析、大数据分析、用户行为分析是密不可分的技术，在当前环境下，网络数据呈现着海量、流速高的特点。ChatGPT对单一数据能够做到解析与分析（如图7所示），但真实场景几乎不会只用单一的数据进行解析与分析。例如，一个UEBA数据集中共有528690条不同数据，ChatGPT难以进行完整的数据接收。在图8中，我们使用少量数据让ChatGPT建立机器学习模型进行了UEBA检测任务。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图8_1_ChatGPT进行UEBA检测任务真实ret值为0.0886-300x266.png)

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图8_2_ChatGPT进行UEBA检测任务真实ret值为0.0886-300x289.png)

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图8_3_ChatGPT进行UEBA检测任务真实ret值为0.0886-300x165.png)

图 8. ChatGPT进行UEBA检测任务(真实ret值为0.0886)

****行-********对不断变化的数据做持续性的跟踪，提供策略优化与持续运营的服务****

不断发展的业务和不断变化的数据带来了对数据安全优化改进与持续运营的需求。数据安全策略的设置主要是根据合规要求而来的，而使用ChatGPT作为合规分析工具吸引了较为广泛的关注。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/企业微信截图_849fa38c-46b6-4ade-8132-561526f5100a-215x300.png)

图 9. ChatGPT隐私政策合规性测评指标体系构建

合规分析主要分为了政策文本解析与程序系统分析两个部分，合规分析最主要的依据是按照相关法律法规构建的合规性测评指标体系，ChatGPT的出现对法律法规解析、政策文本解析（隐私权保护声明等）和程序系统分析提供了一种潜在的解决方案。

如图9所示，针对法律法规，ChatGPT能够生成一套隐私政策合规性测评指标体系。并且能够解析政策文本，给出具体评分和改进建议（如图10所示）。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图10_ChatGPT政策文本解析与评分-300x260.png)

图 10. ChatGPT政策文本解析与评分

如图11所示，ChatGPT完成了对代码的静态分析和隐私合规性的检测。相较于静态分析，动态分析可以更加全面地检测代码中存在的安全问题，并能够捕获代码在运行时产生的漏洞，因此对代码的分析往往会使用动静结合的方式进行，而如果使用ChatGPT进行代码动态分析，其交互能力将会成为主要瓶颈。

![](https://blog.nsfocus.net/wp-content/uploads/2023/03/图11_ChatGPT代码静态检测-300x218.png)

图 11. ChatGPT代码静态检测

## ****三、总结****

ChatGPT的爆火，除了OpenAI的免费策略外，其较为强大的表现也起到了推动性作用。本文结合绿盟科技数据安全治理体系，探究了ChatGPT在数据安全领域的应用前景与影响。总而言之，对于数据安全邻域内的识别检测和生成任务（代码生成、文本生成等），ChatGPT能够有效应对，但对于设计类型的任务，ChatGPT现阶段仍只能起到方法论上的指导作用。并且由于受到模型本地化、交互以及输入输出限制的影响，ChatGPT在安全领域的大规模应用并没有完全普及，但ChatGPT和类似模型的出现仍会大大推动数据安全、网络安全的建设发展。

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/nsfocuschatgpt/)

[Next](https://blog.nsfocus.net/chatgptattck/)

### Meet The Author

陈 毅飞

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)