---
title: LLM 时代下的 SAST ：Corgea 方案解读
url: https://forum.butian.net/share/4332
source: 奇安信攻防社区
date: 2025-05-21
fetch_date: 2025-10-06T22:25:45.480625
---

# LLM 时代下的 SAST ：Corgea 方案解读

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### LLM 时代下的 SAST ：Corgea 方案解读

* [安全工具](https://forum.butian.net/topic/53)

本文解读了国外公司Corgea提出的结合LLM（大型语言模型）和SAST（静态应用安全测试）的创新解决方案——BLAST（业务逻辑应用安全测试）。其通过CodeIQ语义理解引擎结合AST（抽象语法树）技术，增强传统SAST的检测能力。BLAST能够处理特殊框架行为、减少误报，并通过语义理解检测业务逻辑漏洞。

前言
--
今天在群中看到一位师傅发的分享，是关于国外一家做 SAST 和 LLM 结合产品的公司，叫 Corgea。我阅读了他们的白皮书Reference\[1\]，我觉得这个方向算是对 SAST 方向有着一些创新思路便开一篇文章翻译+理解撰写了这篇文章，大致上你在白皮书中都可以看到相关技术的描述（除了在业务逻辑检测这块白皮书没有公布细节，但我找到相关的论文和白皮书上的一些描述大致感觉对的上，也写在文中了）。
由于本文大部分都是自己的一些理解和重构描述出来的，如果有不准确的地方也欢迎各位读者帮忙指出。
传统白盒解决方案
--------
白皮书中也有指出，传统的 SAST 方案就是基于 CPG 和 Call Graph以及非常主流的Source-Sink 污点分析方式来检测和跟踪代码中变量之间的关系。
![Pasted image 20250424165518.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-72e7c7582dd379c3915d3a28943c8bf583d8796e.png)
关于上述技术我就不多再赘述，我之前的文章中有介绍过一些代码分析的方法：
- 《从SpringInspector源码视角深入浅出静态代码分析技术》： <https://mp.weixin.qq.com/s/4jYKPFGIkyr-t2QSqtQpQQ>
- 《从ByteCodeDL项目中学习白盒程序设计理念》： <https://mp.weixin.qq.com/s/7KhgseQG1dPENqBqPG6z-w>
- 以及利用 Call Graph 的方式定位内存马的自研项目： <https://github.com/sf197/MemoryShellHunter>
罗列了传统技术在白盒检测上的局限性：
- Call Graph 调用图：未能考虑反射和依赖关系注入等动态行为，经常忽视运行时依赖关系中嵌入的关键漏洞。
- Source-Sink 污点跟踪：污点跟踪的情况需要处理很多路径问题，以及路径上出现的清洗函数是否正确。
- RAG 向量检索：如果代码库很庞大，检索的时候很容易出现相似语义从而增加程序判断的噪声。
同时还提出了传统 SAST 工具的根本局限性是无法推理业务逻辑漏洞、缺少授权和身份验证等缺陷风险。起原因是程序的行为与预期的功能不一致，传统 SAST 缺乏这种语义理解，不能很好的明确功能的行为边界。
![Pasted image 20250424165934.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-c333975e2be28fe946bf5001bf9194b2f300aabd.png)
并抛出一种“Context is Everything in Security”的观点，我从翻译那边加上我的个人理解统计一下：
- 确定意图(\*\*Determine Intent\*\*)：明确代码需要做什么，明确代码所需要执行的预期。
- 敏感信息暴露审查(\*\*Highlight Exposure\*\*)：有些变量存储着敏感信息，但是传统的 SAST 并不知道，而结合了大模型的语义理解可以准确的捕获到这些敏感信息的走向，是否有暴露。
- 识别更广泛的关系(\*\*Identify Broader Relationships\*\*)：不依赖传统规则，可以跨框架识别不同组件是如何进行交互，并评估其可能产生的风险问题。
- 处理特殊框架行为(\*\*Handle Framework-Specific Behaviors\*\*)：检测框架级的功能安全性，以及一些比较隐式的框架调用方式。
- 减少误报(\*\*Reduce False Positives\*\*)：通过更长的上下文，就可以避免在缺失某个代码片段而造成的误报。
BLAST：Corgea的解决方案
-----------------
BLAST (Business Logic Application Security Testing，业务逻辑应用程序安全测试) ，通过集成 LLM 和 AST 方式增强传统 SAST 的检测能力。
### 语义理解
语义部分是通过 Corgea 的另一个 CodeIQ 的Reference\[2\]语义理解引擎来实现的，这是一种利用人工智能和抽象语法树 AST 所结合的项目：
1. 项目解析：CodeIQ 分析整个项目，并生成对应的 AST，了解其不同组件之间的关系。
2. AI 情境理解：这是 LLM 的优势，可以深入的了解代码的隐式复杂逻辑，这里如果可以生成由 RL 强化学习后的 CoT，或许也能增强代码的理解能力。
3. 适应性：可以更具不同的中间件还是框架，能够具有语义层面上高度的理解能力。如分析 Springboot 的项目时候，会自动的提取 resource 目录下的properties 加入到分析中。
这里由于 blog 中的 paper 没有更直观的展现 CodeIQ 的技术架构，只有一张类似如下的图，我重构了一下展示出来。
![Pasted image 20250424232813.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-2b9f88dfcb47a69e3851b42fcb561141fe8f512e.png)
我的理解是：程序在一开始会从 AST 那里解析细节并构建一个相关性数据库，之后在检测如登录功能的漏洞时候，可以通过标记绿色是相关性的方式，只获取对应的代码进行研判。因 LLM 可以判断出测试用例虽然是有调用对应的代码片段，但并不在生产环境中使用，因此可以区分哪些是实际需要、哪些是存在关联但并非需要的上下文。
### 检测业务逻辑漏洞
BLAST 的主要区别之一是它能够检测业务逻辑漏洞 （CWE-840），这点检测在我看到白皮书之前也是最吸引我的关键点。而 Corgea 对此的解决方式是让 BLAST 提取了解程序的预期行为，其擅长处理：
- 交易篡改：系统在前端实施了购买限制(如限购数量、限购资格等)，但没有在后端进一步验证，攻击者可以通过修改参数和请求的方式绕过这些限制。
- 认证机制缺陷(CWE-287)：如凭据复用、单一认证因素、找回密码的验证码只有 4 位数等。
- 权限绕过(CWE-285)：常见的垂直、水平越权，Cookie 中的权限为基准的鉴权。
很可惜，白皮书和 Corgea 的 blog 中并没有过多的描述这一审查技术的原理，只能靠自己的一些理解和猜测。下面就纯靠我自己的一些之前的过时经验和大胆猜测来判断是个什么样的工作原理。
由于之前给到的关键词比较多的有 AST 和情境语义，所以尽量也想着往这上面靠，毕竟如果真有其他的关键思路肯定也会哔哔说出来。
这个过程中我检索到了一篇 23 年 8 月发布的论文：《GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis》Reference\[4\]
![Pasted image 20250425112858.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-65a8f60db4155c64bb02d1d47dec558414adafb3.png)
这篇论文大致分为三个步骤，括号中是笔者对该步骤的注释：
1. 多维度函数筛选（基于规则的函数筛选）
2. 基于GPT模型的场景分析与关键信息提取（基于模型语义理解的函数筛选）
3. 基于静态分析的漏洞确认（最终确认）
\*\*多维度函数筛选\*\*：感觉这部分更像是数据清洗，清除掉无用的函数和数据部分，如 Test用例、js/css等静态文件等，其中内置了不少的Yaml 的规则和方法来清楚这些无用的函数。然后通过 ANTLR 这种词法分析生成器，来解析可达性上的 AST 语法树，然后标记 Public、Private等属性的可达性，那些需要进一步到 GPT 模型的场景分析和关键信息提取。
\*\*基于GPT模型的场景分析与关键信息提取\*\*：
这一部分内置了很多功能类型的场景和属性，如：【支付、登录、注册、检索、注销】和【用户 ID、支付单号 ID、用户名、密码、搜索关键词】等。
![Pasted image 20250425181220.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-215ede7939c4dbbaba720c577b661bfe7ab8bcb8.png)
提示词如上图所示，给定一组场景列表，让模型回答函数片段属于那些场景，并在后续的属性匹配中结合场景一起让模型回答是与否。
这里的实现就有点类似 CodeIQ 的实现，那些函数是有相关性、那些是不具备相关性、以及有关联但无相关性，因此我认为该阶段更理解为语义方面的函数筛选。
接着说回来，GPTScan 在这里将场景和属性分为两个部分：第一部分是包括对函数功能性的描述，有助于后续扫描中取出不相关场景和属性的部分。第二部分是包括对函数行为的描述，如行为预期是什么，如可能存在安全检查和不正确的逻辑处理就是这部分的行为判断。
正如上述 Prompt 模板所示：如果某个函数符合第一部分的场景，就继续加上属性判断第二部分是否同时满足场景和属性。例如满足场景【支付、转账、数据库操作】，属性【订单 ID、用户余额】，则默认判断该路径调用可能存在任意金额支付的逻辑漏洞（目前还是怀疑阶段）。
![Pasted image 20250425224837.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-f72fe251d00b9efd0bafb91caa1be9e1e99247d6.png)
\*\*基于静态分析的漏洞确认\*\*：这里首先还是通过 LLM 来确定函数中的可达性变量哪些是和业务逻辑相关的。这里的 Prompt 是针对 Web 3 的智能合约场景，但万殊一辙，主要的中心思想还是提取出哪些变量才是关键的。
如果 LLM 提供的变量或语句在函数上下文中不存在，或者描述与所提问题不相关，GPTScan 将终止判断过程，并认为是不存在漏洞。但如果筛选出来的变量存在，则将其输入到静态分析工具中，使用静态数据流跟踪和静态符号执行等方法来确认漏洞的存在。
这里提出了四种静态分析方法用于确认漏洞：
- \*\*静态数据流追踪(Static Data Flow Tracing, DF)\*\*：追踪程序中变量的数据流，确定两个变量或表达式之间是否存在数据依赖关系。如在Web 3 的在“Risky First Deposit”漏洞中，通过数据流分析来确定是否直接用存款金额计算份额。（类似污点分析数据流，判断修改金额的变量中是否有未经检验直接由用户控制的变量）
- \*\*值比较检查(Value Comparison Check, VC)\*\*：检查代码中是否对某些关键变量进行了比较操作，以确保它们满足某些条件。例如在转账的功能中，判断余额的变量在数据库提交事务之前是否有比较用户的余额信息。
- \*\*顺序检查(Order Check, OC)\*\*：检查代码中语句的执行顺序是否符合预期，以确保逻辑的正确性。这里可以通过 AST 来Walk检索，判断执行的
```java
public class OrderCheckExample {
public void updateUserBalance(int balance, int amount) {
balance += amount; // 先更新余额
System.out.println("Balance updated to: " + balance);
checkTransactionStatus(); // 然后检查交易状态
}
private void checkTransactionStatus() {
System.out.println("Transaction status checked.");
}
}
```
这里执行的例子，更新余额的操作必须在检测交易状态之前，这样才能保证事务的及时回滚。
- \*\*函数调用参数检查(Function Call Argument Check, FA)\*\*：检查函数调用的参数是否可以被用户控制，或者是否满足特定要求。如转账的时候，转账方的的账户是否可以由用户抓包修改。
以上就是我对 Corgea 在业务逻辑漏洞检测的技术大概的猜测。
### 减少误报
我认为这个方式应该就是 CodeIQ 的那种，BLAST 可以获取相关语义的上下文，从而能更精确的在传统 SAST 的扫描结果上验证准确性，继续根据污点数据流做进一步语义和逻辑的判断。因 SAST 的结果集都有特定的文件名和行号，因此只需要在这些行号对应的函数收集到同一个上下文里面，再根据前面语义理解和判断是否有清洗污点的函数，应该就足够了。
BLAST 架构和工作流
------------
看一下白皮书给出的架构工作原理：
![Pasted image 20250426002359.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-f50a8538046fdaf2b2f853e2a5c709e37f9caf0d.png)
先是解析项目架构，通过删除无相关的文件上下文，然后 CodeIQ 继续将相关的上下文拉取到提示词中分场景进行 LLM 判断，最后生成报告。
总结展望
----
技术上通过语义情境分析确实能很大程度上提高白盒程序对代码和业务的理解能力，尤其是在目前 RL 强化学习下的 LLM，可以对代码业务具有更多的思考和理解程度。加上最近的多 Agent 的能力，可以让 LLM 的来识别重要业务的可达变量，筛选出程序重点需要把注意力放在那些变量上，再使用 MCP 等方式更方便的结合静态分析处理。
或许还能通过 RL 强化学习，让模型学习学会使用工具，类似 Deep Research 的功能一样检索企业内部现存知识库，判断这种业务场景的缺陷之前有没有出现过(毕竟企业内经常会共用一个框架，也会有代码函数直接拿来复用的情况)。
或者能否结合项目 AppName 检索 Git 仓库的 Pipeline 流水线，找到测试环境对应的k8s应用 Pod 名称，然后根据数据流回溯，找到污点参数进来的函数判断路由路径，然后构造 Nuclei 的模板请求测试是否包含漏洞（这个有点复杂，但目的是尽可能的降低误报。因此只需要 Multi-Agent 的能力一步步判断，只要有一个环节返回错误就结束判断下一个）。
Reference
---------
\[1\].<https://corgea.com/blog/whitepaper-blast-ai-powered-sast-scanner>
\[2\].<https://corgea.com/blog/introducing-corgea-codeiq-smarter-detection-triaging-and-fixing-of-insecure-code>
\[3\].<https://arxiv.org/abs/2308.03314>
\[4\].<https://corgea.com/blog/new-product-blast-business-logic-application-security-testing>

* 发表于 2025-05-20 09:00:00
* 阅读 ( 2609 )
* 分类：[AI 人工智能](https://forum.butian.net/community/AI)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![wh4am1](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/41336)

[wh4am1](https://forum.butian.net/people/41336)

1 篇文章

[奇安信攻防社区](https://forum.butian.net)|...