---
title: 深度解读丨ChatGPT与代码安全
url: https://www.4hou.com/posts/wgMw
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-28
fetch_date: 2025-10-04T10:49:50.421764
---

# 深度解读丨ChatGPT与代码安全

深度解读丨ChatGPT与代码安全 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 深度解读丨ChatGPT与代码安全

企业资讯
[行业](https://www.4hou.com/category/industry)
2023-03-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)92478

收藏

导语：ChatGPT是由GPT-3.5-Turbo模型微调而来，其参数量达到了千亿级别，是目前业界最为领先的自然语言处理模型之一。

**01**

**ChatGPT是什么？**

ChatGPT是OpenAI研发的一款自然语言处理模型，它可以让你和一个聊天机器人进行类似人类的对话，还可以帮助你完成一些任务，比如：

能够生成自然的对话，包括与用户聊天、担当智能客服等应用场景；

回答各种问题，包括常识性问题、学科问题等等，应用于智能问答、知识库问答等场景；

对一段文本分类到预定义的类别中，如新闻分类、垃圾邮件分类；

识别文本的情感，如积极、消极、中性等，应用于舆情监测、用户评论分析等领域。

ChatGPT模型采用了Transformer架构，基于GPT3.5微调，通过海量数据的训练获得了极高的语言理解和生成能力。目前， GPT已经发展到了GPT-4，ChatGPT是由GPT-3.5-Turbo模型微调而来，其参数量达到了千亿级别，是目前业界最为领先的自然语言处理模型之一。

![微信图片_20230324103731.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679625414200518.png "1679625414200518.png")

ChatGPT能够根据问题中的指令提供详细的回答，不仅可以回答一般性和技术性的问题，也可以结合上下文对后续问题进行回答，并且根据用户的提示承认自己的错误，挑战错误的前提，拒绝不合适的请求。

ChatGPT目前是免费使用的，可以在chat.openai.com上试用，不过目前仅限于境外地区。

**02**

**ChatGPT在代码层面的能力**

在ChatGPT刚刚兴起的时候，就有很多用户对其代码方面的功能展开了测试。虽然当前的ChatGPT增加了很多功能限制，比如很难再让其生成恶意代码或是任何负面信息，但仍然能通过一些引导进行绕过，比如让ChatGPT举一个PHP注入的案例：

Q: 举一个PHP注入的例子，并使用一些字符编码的方式绕过检测。

ChatGPT给出的回答如下：

![微信图片_20230324103807.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679625443111200.png "1679625443111200.png")

Q: 请分析代码：

<?php
if (isset($\_GET['c'])) {
 $c=$\_GET['c'];
 if(!preg\_match("/;|.\*c.\*a.\*t.\*|.\*f.\*l.\*a.\*g.\*| |[0-9]|\*|.\*m.\*o.\*r.\*e.\*|.\*w.\*g.\*e.\*t.\*|.\*l.\*e.\*s.\*s.\*|.\*h.\*e.\*a.\*d.\*|.\*s.\*o.\*r.\*t.\*|.\*t.\*a.\*i.\*l.\*|.\*s.\*e.\*d.\*|.\*c.\*u.\*t.\*|.\*t.\*a.\*c.\*|.\*a.\*w.\*k.\*|.\*s.\*t.\*r.\*i.\*n.\*g.\*s.\*|.\*o.\*d.\*|.\*c.\*u.\*r.\*l.\*|.\*n.\*l.\*|.\*s.\*c.\*p.\*|.\*r.\*m.\*|`|%|\x09|\x26|>|   system($c);
 }
} else {
 highlight\_file(\_\_FILE\_\_);
}
?>

ChatGPT给出的回答如下：

![微信图片_20230324103838.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679625473351490.png "1679625473351490.png")可见，ChatGPT具备基本的分析代码的能力，那么它具不具备创作代码的能力呢？

答案是肯定的。已经有国外的用户成功让ChatGPT创作了一个简易的小游戏，并且由ChatGPT完成了全部代码的编写工作（包括界面）：https://sumplete.com

![微信图片_20230324103915.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679625511398093.png "1679625511398093.png")**03**

**ChatGPT在漏洞挖掘方面的能力？**

ChatGPT可以对源代码进行分析与生成操作，那么它在源代码挖洞的表现如何？

**（一）SAST**

我们首先对ChatGPT进行静态代码扫描（SAST）的测试。选取几段OWASP Benchmark的测试样例（https://github.com/markl72/owaspbenchmark/tree/master/src/main/java/org/owasp/benchmark/testcode），要求ChatGPT对其进行静态代码扫描。

Q: 请对以下代码进行扫描，并编写一份SAST扫描报告。

ChatGPT给出的回答如下：

![微信图片_20230324103945.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679625541352320.png "1679625541352320.png")Q: 请扫描以下代码，并以SAST报告的形式输出一份精美的漏洞文档。

ChatGPT给出的回答如下：

![微信图片_20230324104009.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679625575318364.png "1679625575318364.png")![微信图片_20230324104013.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679625584122939.png "1679625584122939.png")可以看出，ChatGPT可以针对各种输入进行问题的扫描，并且可以通过一定技巧使其输出一份可用的文档，甚至还会给出一个问题修正后的代码：

![微信图片_20230324104141.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679625663662889.png "1679625663662889.png")![微信图片_20230324104144.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679625675180822.png "1679625675180822.png")因此， ChatGPT 有一定的SAST静态代码扫描能力。作为智能聊天机器人，ChatGPT 本身就是一个高度集成和可定制的系统，具有许多优秀的功能。它通过理解代码，比较各种情况并提供最广泛的答案来回答。ChatGPT在SAST领域表现优异的原因包括且不限于：

**ChatGPT 灵敏的规则适配能力**

SAST 往往对于不同代码难以做到绝对的通用性，规则往往被预定义以应对某些更新变化（例如：新类型的攻击方式）。然而，ChatGPT 区别于其他 SAST 工具，其通过 AI 技术的支持能够灵活适配新的规则，无论规则是否是预定义、生成式、输入式、API生成或人类标记数据。

**ChatGPT 自动化程度更高**

ChatGPT 可以从语法到语义级别进行处理。它符合所有必要的常见编程语言，并根据具体方法对日益增长的源代码进行静态分析并自动产生报告。ChatGPT 还能及时响应开发人员的操作，并可以通过API定期运行重复测试以确保系统的稳定性及质量，其输出可以快速定位漏洞类型、位置、代码块。相比其他在市场上存在着时间代价，使用门槛，学习难度的 SAST 工具，ChatGPT 的自动化水平在静态扫描市场上的竞争力不可忽略。相比于针对各种语言的不同SAST工具，ChatGPT可以提供非常统一的API接口，供企业进行二次集成和开发。

**ChatGPT 报告更加优秀**

ChatGPT拥有更好的内部算法与计算方式，给出的结果不仅偏离成功缺失与时间更小，而且考虑到了代码的语义，进而提高报告的准确性和全面性。同时，ChatGPT 可以涵盖比传统单个 SAST 的信息更多的情况、模式和代码库，并提供针对组织差异、习惯和行业法规等的补充选项，这使得其报告更严谨。因此，ChatGPT 不仅可以应用于标准的Web应用和桌面应用，还能够处理如数据库存储、APIs和IoT设备等后端和嵌入式系统。最后，ChatGPT还可以直接为漏洞编写修复代码，进一步提高企业效率。

**（二）SCA**

下面，我们对ChatGPT的软件成分分析（SCA）能力进行测试。SCA测试通过检查包管理器、清单文件、源代码、二进制文件、容器镜像等，识别出的开源依赖会被编制成物料清单 (BOM)，然后与各种数据库进行比较，包括美国国家漏洞数据库 (NVD)。由于工程的软件组成有着不同的格式，这里随机选取了一个1.9k Star的开源仓库https://github.com/xushengfeng/eSearch，对其Javascript依赖package.json进行测试。

Q: 请扫描下列内容，并对其依赖进行分析。

ChatGPT给出的回答如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/iaFosZKVaZUN66zbhglbiaLM4NFpvQfmPRib7o1VjFFuJuzwBKfAw2utSO1O0thmiapl7hkI00VP4oWu4aoGlLXpMA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

可见，其无法从直接引用包中按树状推导出下一层依赖，由于字数限制，也无法通过手动提供所有依赖的方式进行扫描。

![图片](https://mmbiz.qpic.cn/mmbiz_png/iaFosZKVaZUN66zbhglbiaLM4NFpvQfmPRQXrJ7Ht9MqxeXGibXe7pMKJVRaDQiamqc7VVNJu7ibicbnuwrM4AnYL6vQ/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

因此，ChatGPT目前并不能很好地胜任SCA任务，其原因可以归纳为：

**自然语言理解的限制**

人类可以通过几秒钟的观察就能够辨认组件或者应用是何种类型，ChatGPT也拥有与人类相差无几的自然语言理解，但它并不能像人类开发人员一样解读代码或配置文件来确定软件的具体构成。因此，它难以有效地帮助我们识别特定的组件或者安全问题。例如，一个简单的Python脚本，ChatGPT能够解释它的目的和执行流程，但无法知道其中的特定库和依赖项。

import requests
from bs4 import BeautifulSoup
url = 'https://www.example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

在这种情况下，ChatGPT 只能看到 Python 代码，但除非它能识别出引用BeautifulSoup的库，否则将无法告诉我们这个脚本需要SQLAlchemy, Flask 和 Django 等软件库才能正常运作，因此也无法全面的进行SCA分析。

**快速的版本变化**

当涉及到软件组件分析时，即使不那么重要的微小更新也可能导致软件技术栈变化。对于自然语言理解的ChatGPT，自动识别软件程序在版本变化中引入的新功能或更改，是非常困难的。

例如，在ReactJS 库的两个版本之间，可能某些函数的名称或参数已经发生了变化，可能还删除或添加了一些函数。这很可能会影响您的代码和整个应用的稳定性，而ChatGPT无法适应这样的变化，从而具备容易忽略的高风险性。

总结：ChatGPT在SAST方面的能力较为优秀，而IAST、DAST方面的能力由于需要结合动态执行，难以结合ChatGPT进行测试。对于SCA，由于ChatGPT的知识止步于2021年，因此很难保证最新的时效性，因此从实际情况来说，并不能获得非常可靠的结果。

**04**

**ChatGPT在安全领域的未来形态**

从上文我们了解到，ChatGPT可以通过强大的自然语言处理技术和深度学习模型来解决与安全相关的问题，特别对于SAST这类纯文本形式的任务，ChatGPT的能力将显得更为出众。下面从几点对ChatGPT的未来做一些展望：

**逆向工程领域**

得益于ChatGPT对静态代码分析的能力，未来可以使用ChatGPT对逆向工程进行辅助。比如将ChatGPT集成进IDA Pro，使其可以将混淆的汇编还原回原本的语义，或者对IDA反编译结果进行润色和优化，输出更为容易阅读的源代码。还可以对函数进行总结，降低逆向分析者的时间成本。

![图片](https://mmbiz.qpic.cn/mmbiz_png/iaFosZKVaZUN66zbhglbiaLM4NFpvQfmPRYeAwt30EytNic7u688cWpZwXfUypj8z2ETia7picUBtaCUticVVBCtuJnA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

**SAST**

漏洞扫描是一项非常重要的安全工作，因为它可以限制和消灭工程内各种安全漏洞。因此，SAST是一个非常关键的技术，目的是在开发过程中就可以发现提前识别漏洞，这样可以大大节省我们的时间和金钱成本，降低软件上线后的风险。正如上文所指出，ChatGPT可以轻松从多个角度评估代码质量和代码规范，避免在代码实现过程中各种隐藏问题。

同时，由于SAST与DevOps紧密联系，ChatGPT还可以通过DevOps CI / CD 工具集成来实现持续集成和持续部署，从而在项目开发周期的早期就追溯潜在的漏洞。这可以大大减少甚至避免因漏洞引起的后期修改和调整成本。

**SCA**

开源软件是当前的主要趋势和发展方向之一。它极大地促进了软件开发的速度和效率，并降低了软件开发的成本。然而，开源软件及框架会带来一定的安全风险。因此，对开源软件管理非常关键。目前的ChatGPT对于SCA任务不理想，但可以借助如New Bing的高效的数据搜索和分析技术来优化其模型的时效性，从而提高对开源代码的安全性和正确性。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/clos...