---
title: AI Agent 进入网络安全之后，渗透测试开始有点不一样了
url: https://mp.weixin.qq.com/s/lIcZiUIsdVGFKo2H-KcdWg
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:56:38.261954
---

# AI Agent 进入网络安全之后，渗透测试开始有点不一样了

# AI Agent 进入网络安全之后，渗透测试开始有点不一样了

原创

小智
小智

智榜样网络安全学习中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

近来，AI 安全工具的使用越发频繁，越发容易出现的情况：AI会进行聊天，但是**在实际开展安全测试工作的时候，仍然得自己去做**。

你让它解析某一漏洞，它能够向你讲解原理；你撰写脚本，它还能够帮助你产生代码。但是到了真实的测试阶段，端口扫描，目录发现，子域名枚举，漏洞验证，结果整理，常常是**终端开设一堆窗口然后工具一个一个地往前跑**。

**CyberStikeAI想要解决的，正好就是那一段。**

它并非仅仅是给大模型搭建一个聊天的窗口，实际上是**把AI Agent，MCP，安全工具，知识库，工作流，漏洞管理以及审计放到了一个平台当中**。官方的项目当下使用Go来进行搭建，并且**依靠EinoAgent进行编排**，而且具备**MCP原生的工具以及RAG知识的库**，可视化的工作的流程还有攻击链的建模功能。

项目地址：

https://github.com/AIPentest/CyberStrikeAI

## 打开之后，你会发现它更像一个安全工作台

先抛开AI，直接去查看界面情况。

CyberStikeAI它的首页不是单纯的聊天框子，而是**有着完整控制台的**。系统的状态漏洞的数量，工具执行的情况，任务以及别的安全方面的数据，都能够在这个页面当中被看到。

![CyberStrikeAI 系统仪表盘](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauMCNJOtzj6gxdc7YGAiatWKEBUBMiaxfl877E5NmsUfzltU1dKhUgPSOxaiaibEYYngdzdZyCSXdNaGheiaXumglF6KgUpXGtzARTgQ/640?wx_fmt=other&from=appmsg)

CyberStrikeAI 系统仪表盘

此类设计确实很关键。

因为在实际进行安全测试的时候，最为麻烦的往往不是去执行某一个命令，而是**在执行十几个乃至几十个的命令之后，如何把结果串联起来**。

比如先找到一个开放的端口，之后判断相对应的服务，再找到Web应用，接着开展目录的发现以及漏洞的检测工作。**传统的方式大多依靠人脑去记录上下文**，CyStrikeAI想要让Agent参与到这个过程当中，**把之前的结果当作后续任务输入的内容**。

说，它更加接近：

**提出目标，Agent规划，调用工具，分析结果，继续执行，保存证据。**

而非是：

问AI某一个问题，AI回答某段文字。

## AI Agent 在这里到底干什么？

CyberStikeAI官方拥有**单agent以及Deep，Plan - Execute，Supervisor等许多编排方式**，并且可以借助图形化的工作流程，把Agent，工具，条件，审批还有输出进行组合。

![CyberStrikeAI AI 对话与执行界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauOTa6Z9T3yOEOkgMxW1R7uJaqzDheOHAO59icM14EBUIdNQAFbuS5BnOoG8HQ1adGzncocWLDUBEdO7tCbZOXGwk0jCjWxCPGBE/640?wx_fmt=other&from=appmsg)

CyberStrikeAI AI 对话与执行界面

举一个较为容易领会的实例。

在自身的靶场中，你可给予其授权测试的目标，让其率先实现基础资产的发现。获取结果之后，随后依据实际状况开展Web服务的探测，目录的察觉或漏洞的扫描操作。

此刻 AI 的作用**并非取代nmap，nuclei，ffuf这类工具，反而是肩负决定何时应运用何种工具的职责**，以及如何领会前一工具留存下来的成果。

**此思路实际上比AI自动产生命令更具意义。**

原因在于安全工具自身已经十分成熟。nmap无需重新进行研发，nuclei也无需再重新开展研发工作，而**真正缺乏的是一种能够将这些工具进行组织的上层实施逻辑**。

CyberStikeAI所做的就是这一个层面。

## 100+ 安全工具，才是它真正的基础设施

**要是仅仅只有Agent，不存在工具，最终还是聊天的机器人罢了。**

CyberStikeAI官方当下提供了**100多个YAML的工具方面的配方**，包含网络扫描，Web以及应用扫描还有漏洞检测，子域名进行枚举，API安全还有容器安全，云安全二进制解析，取证等好几个方面。

比较常用的工具包含nmap，masscan，rustscan，sqlmap，ffuf，gobuster，nuclei，subfinder，amass等等。

此处存在一个较为实用的设计：工具并非仅仅处于程序之中。

项目将工具配置单独放置于`tools /`这个目录里面，每个工具都存在对应的YAML配置，能够对命令，参数，启用状态以及描述进行定义。后续要是想要扩展新工具的话，**不一定得去更改核心的代码**。

官方的工具文档当中还专门设置了`short_description`，使得系统在把众多工具信息传递到大模型的时候，**只是先发送短的描述，防止一次性耗费大量的Token**；要是真的需要详细的信息，就通过MCP来进一步进行读取。

对于 AI  Agent而言，这实际上是一个非常实际的问题所在。

工具数量越多模型所获取的信息越多。

要是把几十到百个工具完整的描述全部放进上下文里，Token就很容易把精力浪费在“知道工具”这个事情上面。因此CyberStikeAI拆解工具发现以及工具详细的说明，从根本上来说是为了**解决Agent工具规模不断扩大之后产生的下文方面的问题**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauOI188YjiaTOiaDjMFuuRPc44EE2tiaxs1rhXUp43e62FVDbV4FEoicRia9Mz4bsGoDncTwhfILYuRNK7EbhXmCHicL9Ku98G0CD7jlA/640?wx_fmt=webp&from=appmsg)

## MCP，让它不再局限于本地工具

**这是我认为CyberStikeAI和普通 AI 安全脚本相比更值得去探究的地方。**

它将MCP置于核心架构之中，当下支持**HTTP，stdio，SSE，外部的MCP联邦还有动态工具的发现**。

![CyberStrikeAI MCP 管理界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauNrQC79mws8PosK8QbotpdJfMfEYib3g39pL3KPHqRu82UBW2TkazSicY2EIuzb7n11qW93AOTCib6c0f6EUyftyCTHaVJArmePuo/640?wx_fmt=other&from=appmsg)

CyberStrikeAI MCP 管理界面

简单来看就是，CyberStrikeAI**自身不是全部能力的终结点**。

你完全能够借助MCP接入不同安全能力，随后让Agent依据任务来发现并调用这类能力。

如同**为安全测试的环境构建了一条“总线”**

未来你可能拥有一项资产发现的服务，一个Burp的流量入口，若干扫描器以及自己编写的内部的工具，这些工具不需要整合到同一个代码里面，而是能够分别给予能力，之后交由统一的Agent来进行调度。

当一台机器运行主平台时，其余机器或容器分别运行不同工具时，借助网络接入能力，整体安全实验的环境会比数十个终端的窗口更为整齐。

## 发现漏洞之后，它还要负责“收拾残局”

众多AI安全Demo存在一个共同问题：

**扫描结束了，接下来？**

终端之中出现了许多结果，比如截图，复制，分类，整理，**全部都是人工来完成的**。

CyberStikeAI**将漏洞单独当作管理模块**来使用，能够保存漏洞的信息，并且从严重程度，状态等方面去查看。

![CyberStrikeAI 漏洞管理界面](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauOTccuCh7ibgibZnNXHdRDtyflVy5nXN1FOPRlicNldbD7GGyT82iabz1pIdiaAibLFkTJqTiafmc4IhJzicibAOw4dlwBCQtcxWdhgdAHw/640?wx_fmt=other&from=appmsg)

CyberStrikeAI 漏洞管理界面

此步骤看似并非“AI”，但是从实际运用层面而言，**它反而极为关键**。

原因在于安全测试并非一次性开展。

你今日察觉到的问题或许下周还要进行复测；某一个项目可能存在几十个缺陷；同一资产可能会经历多个阶段的测试。

因此真正具有价值的体系，不应该仅仅告诉你“此处存在一处漏洞”，而**应当知道该漏洞归属于哪一个项目，当前处于何种状态，之前进行过何种操作以及相应的测试依据在何处**。

CyberStikeAI还具备项目，攻击链，资产以及任务管理这类功能，从本质来看是**把一回测试从聊天记录变成能够持续进行维护的资料**。

## Burp Suite 也能接进来

对于很多已经熟悉Burp的人而言，还存在一种比较实际的功能。

CyberStikeAI**具备BurpServer插件**，并且还拥有Chrome / Edge这两个浏览器的扩展情况。浏览网络进行扩展能够**捕捉DevToolsNetwork的流量**，之后交给CyStrikeAI来进行AI辅助方面的分析。

**这表明它并没有尝试让传统的安全工具完全消失掉。**

相反它就好像是\*\*在原来的工具链之上再添加一层 AI \*\*。

Burp是Burp，nmap是Nmap，nuclei是nuclei，不过**以往这些工具相互连接主要依靠人，当下可以慢慢交给Agent以及工作流来完成**。

这或许是AI进入到安全测试之后更为实际的发展趋向。

## 虚拟机能不能跑？

从项目的部署方式来看，拿一台独立的虚拟机做实验环境是比较合适的。

官方部署文档要求 Go 环境以及 Python 环境，同时默认使用 SQLite 保存数据，**不要求额外部署数据库**；项目还提供 `run.sh` 进行启动。

基础启动方式很简单：

```
git clone https://github.com/AIPentest/CyberStrikeAI.git
cd CyberStrikeAI
chmod +x run.sh && ./run.sh
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauNqVyTj7EpEN3g8wznicE72TUE045eAGItTc058oSJq8wTEicBgoicvdibGKy41Ria8qUngvibCRNJ4KMhiaFLEhR7IjwhOpK2UgESOl8/640?wx_fmt=webp&from=appmsg)

启动以后，再进入系统设置**配置 AI Channel**，填写模型服务的 Base URL、API Key、模型名称以及 Token 参数。

安全工具则根据自己的需求单独安装。项目里的 YAML 文件主要负责描述如何调用工具，并不会自动把所有 nmap、nuclei、sqlmap 之类的软件全部装进系统。

## 最后聊聊这个项目真正值得看的地方

CyberStikeAI 有趣的地方，不是**“AI能够运行nmap”此类事情**。

真正需要留意的是**它正在尝试把若干个原本分离开来的物件放到一起**：

**Agent承担思考的职责，MCP承担连接的责任，安全的工具承担执行的任务，知识库补充的上下文，组织过程的工作流，保存结果的漏洞管理。**

这个结构一旦打通，AI 在安全方面的作用就会有一点改变。

它不再仅仅是一个能够帮助你去解释漏洞情况的聊天工具，也不再只是能够生成Payload代码的帮手，而是**已经变成可以参与到安全测试过程当中的执行层级**。

当然，AI 到底能够把这个流程自动进行自动化，**还得看具体的模型，工具的质量，环境还有人工审核的机制**。

但是就工程实现而言，CyberStikeAI已经将AI Agent加上MCP再加上网络安全方面的工具此类路线打造成为一个**能够自己进行部署，自己来进行转换的开源的项目**。

## 🎁 互动与福利

**分享本文到朋友圈，点赞+在看+关注，一键三联，可以凭截图找老师领取**

上千**学习资料+工具**哦

![22919c6e4ef945aa9a9cbf0f6df4f6ff](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauPHeFJHKndf0iasSxJeJYicLwIgsT3KVakKt6kCFIojp0juYVAY2e5A9oVyxK0rHZb392vVEfdZFyibB5AMfdPBuDUeOX6LMT3Zzg/640?wx_fmt=other&from=appmsg)

22919c6e4ef945aa9a9cbf0f6df4f6ff

**分享后扫码加我！**

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rYoibTlMQ1MpHdawUKrSwglIRtuj0JaKrsHFZKjEmiac6PBmXbWcK5fMZDnDJQHn3mlYHl0ibVEibUq8pKDspI0Qjw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过