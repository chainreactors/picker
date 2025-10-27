---
title: 什么！这条PoC/EXP的作者竟是？
url: https://mp.weixin.qq.com/s?__biz=MzI4MzcwNTAzOQ==&mid=2247545694&idx=1&sn=08893a5d79ebcadd741a29b0a011327c&chksm=eb84d8fedcf351e8c814b2a07a2672d4d106b081847112b501146d33275db05bf23a5d669bbe&scene=58&subscene=0#rd
source: GobySec
date: 2024-11-23
fetch_date: 2025-10-06T19:20:41.050635
---

# 什么！这条PoC/EXP的作者竟是？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GGOWG0fficjLSetUI1DiagoyRzYGyovjygicn8fwWDwL7lUCKYYcAd6JqLVNaXLqpNGHlAohb974TuSvvJkqd8Q3A/0?wx_fmt=jpeg)

# 什么！这条PoC/EXP的作者竟是？

原创

Chili

GobySec

不知道有没有细心的师傅发现，在今天我们的例行更新的漏洞列表中，有个漏洞被打上了一个神秘的标签。

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjLSetUI1DiagoyRzYGyovjygZF55pkpzQXwwxEVqF81cwMWV9yjTKjR2aSVnHVJfqSAaSzGk0QZC1A/640?wx_fmt=png&from=appmsg)

想必大家已经猜到了，这条是首个由Goby安全社区的新成员—AI Bot所创作编写的PoC/EXP。

给Goby提交过漏洞的同学都知道，每一个Goby的漏洞上线，都需要经过层层审核，不止是PoC的检测逻辑，还有针对漏洞的EXP验证效果，都有严格的要求，但超出我们预期的是，AI Bot所编写的PoC/EXP，完全符合Goby漏洞收录标准。

我们先以视频的方式看一下AI Bot智能转化丝滑操作流程：

******![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKzq4TFicia2yUjianoH80KtrWElvrR0XQbqBDCHC68DicU6TwYLR54jEJE3rqy2icwicrV85dICfKrJsOQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)********AI初尝试**

某天，Goby漏洞组一位不愿透露姓名的师傅提出了一个大胆的想法："既然AI已经能够帮助我们实现半自动PoC编写，那么，是否能通过进一步的训练，让它达到全自动编写的水平呢？甚至，如果只需提供一个待参考信息的文档链接就能直接生成PoC，那岂不是更妙！"

想象一下，这样能大大降低PoC编写的门槛，即使是没有丰富经验的“小白”也能轻松使用Goby写出有效的PoC。这无疑将为我们的安全研究和漏洞复现工作带来显著的效率提升。

面对这样的挑战和机遇，Goby团队毫不犹豫地迈出了第一步。

很快，GobyAI首个测试版本上线了。根据首批体验官们的试用反馈，虽然GobyAI在PoC的基本编写方面表现不错，但是在转化成功率上还有一定的提升空间。更重要的是，在实战应用场景中，大家更加关注EXP的智能输出。因此，我们明确了EXP的智能输出的重点研发方向，以充分展现GobyAI在实战中的价值。

### **********![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKzq4TFicia2yUjianoH80KtrWElvrR0XQbqBDCHC68DicU6TwYLR54jEJE3rqy2icwicrV85dICfKrJsOQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)********教会AI编写EXP是一件不容易的事**

在以往我们进行AI生成PoC/EXP的实践中，我们发现，基于Goby现有的JSON框架，通过纯JSON的方式编写EXP几乎不可能实现，因为不同的漏洞类型，其漏洞类型，其传递的漏洞验证参数会完全不同，内部也可能存在复杂的关联关系。

所以在人工进行漏洞录入时，通常会采用Go代码的方式来编写EXP，但这一思路在Ai上就很难走通，通过AI直接生成Go代码编写的EXP质量非常低，这是由于不同漏洞类型的验证方式存在显著差异。所以我们必须实现一种通过纯JSON方式来实现复杂EXP验证效果的漏洞录入框架。

在最新的 Goby 版本中，我们对 JSON 编写框架进行了升级，引入了更丰富的语法和关键字，以支持多样化的漏洞验证方式，在提供更简单EXP编写方式的同时，也为教会AI写EXP这件事提供了新的可能。

通过前面视频我们可以看到，我们通过AI通过生成JSON代码就能够把SQL注入漏洞的各种EXP验证效果完整实现，在介绍具体的EXP代码之前，需要先了解一下我们的ExpParams参数的运行逻辑，这决定了最终我们将发送何种Payload来进行EXP验证。

#### **EXPParams**

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjLpE2Bn6nay8SdQSFZB70UPOHqr21mIsRPF0H5oibribNyqrzMh3JZfebv8dhgCusicAfy8lFJF0LRZQ/640?wx_fmt=png&from=appmsg)

在Goby的漏洞框架中，我们通过一个参数数组，来传递具体的漏洞验证效果，首先通过 attackType 指定所有可用的验证方式，然后使用 attackType=xxx 切换至对应的验证方式。在每种验证方式中，用户可以进一步定义具体的验证效果，以满足不同场景的需求。也由于EXPParams的过于灵活，导致在原有漏洞框架中，无法对复杂的EXPParams进行处理，其难点主要有两个：

* 如何根据传入的EXPParams来发送不同的Payload
* 如何根据不同的EXPParams来回显不同的数据

所以在新的漏洞框架中，我们新增了多种语法以增强漏洞验证的灵活性与执行能力：

## **switch**

为了解决第一个问题，我们提供了新的函数关键字，切换不同的漏洞验证方式。例如，以 SQL 注入为例，通常支持三种验证方式：默认方式、用户输入方式和 sqlpoint 方式。通过 switch 关键字，可以灵活选择当前需要使用的验证方式，从而便于后续编码及相关操作的实现。

如下图所示，会根据attackType的传值来定义不同的Payload

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjLpE2Bn6nay8SdQSFZB70UPFgoJYDAia4Quqdc7IgoakLStiaetQicZpIPXekNjcxY9SlICiaQaDVHS8A/640?wx_fmt=png&from=appmsg)

## **when**

同样，解决Payload问题之后，我们需要解决第二个问题，when 关键字用于对输出内容进行控制，在 SQL 注入的 EXP 中，当attackType为sqlPoint的时候，我们需要打印发送的请求数据包，以便于用户提取数据包用于后续的检测。

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjLpE2Bn6nay8SdQSFZB70UPX64NHUHn9KUHt1FEl6WhznWvnIqeO5nthotSTAy4IU8Kec1zR97lIQ/640?wx_fmt=png&from=appmsg)

### **********![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKzq4TFicia2yUjianoH80KtrWElvrR0XQbqBDCHC68DicU6TwYLR54jEJE3rqy2icwicrV85dICfKrJsOQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)接下来就看********AI的了**

为了解决AI对不同漏洞类型的支持，我们通过构建群体智能体模型解决 EXP 编写问题，每种漏洞类型均由专属智能体负责处理，当用户输入漏洞复现链接或相关文章时，由漏洞信息整合智能体负责挖掘页面中的漏洞信息，包括解析图片与文本内容。随后，监管智能体接收并进一步解析漏洞信息，根据漏洞类型将任务分配给相应的 EXP 智能体。

以 SQL 注入智能体为例，当接收到漏洞参考文本时，智能体首先识别数据库类型并生成相应的 SQL 验证命令，同时定位 SQL 命令的位置，并将其替换为相应的变量。智能体会根据漏洞特性，灵活选择 switch 和 when 关键字，并判断是否需要进行编码处理。编写完成后，智能体将生成的 EXP 文件反馈至监管智能体进行审核确认，审核通过后输出最终的 EXP 文件。

时间来到现在，团队不断训练优化GobyAI智能体、加强提升对复杂型漏洞类型（SQL注入、文件上传等）EXP智能编写的准确性。相较1.0测试效果，PoC的智能转化成功率有了明显的提升，更重要的是，GobyAI 2.0版能高效准确完成部分复杂型漏洞EXP的智能编写，实现了PoC/EXP全流程智能化实战应用能力。

******![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKzq4TFicia2yUjianoH80KtrWElvrR0XQbqBDCHC68DicU6TwYLR54jEJE3rqy2icwicrV85dICfKrJsOQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)********AI Bot的实战检验**

**Supabase 后端服务平台 SQL注入漏洞**

通过公开参考信息的描述查看漏洞成因：Supabase 后端服务平台/api/pg:meta/defaultguery对用户传入的数据没有进行校验和过滤，导致攻击者传入的SQL语句直接带入到数据库执行，形成SQL注入，可获取数据库敏感信息，深入利用可获取服务器权限。

以下是AI Bot的实战检验流程：

* 采集漏洞细节参考链接：https://blog.csdn.net/qq\_41904294/article/details/135443624；
* 自动采集补全信息：AI引擎将迅速解析链接内容并提取图片内容，将解析到的内容分发到不同的子任务（以实现快速解析）；√
* 提取到漏洞类型为【SQL注入】，并提取分析payload；√
* 分配SQL注入漏洞类型智能体并解析数据库类型；√
* 自动生成符合Goexp规范的PoC/EXP代码，代码包含:Payload请求参数、验证环节的数据库SQL执行语句、执行方式等；√

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjLpE2Bn6nay8SdQSFZB70UPXCMWYKjDXv8n3qnT98TBxZY7ekAIW62oZkibBTIkicBBD5zYbUIiam8aw/640?wx_fmt=png&from=appmsg)

* 一键检测：输入靶场环境目标，准确无误检测出目标是否存在漏洞；√

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjLpE2Bn6nay8SdQSFZB70UPvnz6nQol3tDKichfe1cjk6IpWdBEdA7ic5SF6Roj0ghIibovRc7tzD4rQ/640?wx_fmt=png&from=appmsg)

* 一键验证：点击验证，通过自动生成的SQL执行语句准确输出output信息。√

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjLpE2Bn6nay8SdQSFZB70UPKjrhPEkN5BFVfwpxm8tkMfy3HVqcC4B3KHvQV5vchwOXnB0lVl1vWQ/640?wx_fmt=png&from=appmsg)

AI bot在5分钟内完成了全自动化智能编写， 并且验证输出效果上完美符合GoexpSQL注入类型漏洞收录标准！

完成提交审核后，Goby第一条由AI bot独立创作编写的POC正式官宣上线！

那么重点来了！

这么好用的GobyAI要怎么才能体验到呢？

#### ******![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKzq4TFicia2yUjianoH80KtrWElvrR0XQbqBDCHC68DicU6TwYLR54jEJE3rqy2icwicrV85dICfKrJsOQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)******Goby AI种子体验官计划2.0启动！

升级最新2.9.10版本（官网下载最新版本包或老版本客户端进行更新），即可看到GobyAI入口。

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjLpE2Bn6nay8SdQSFZB70UPeOSu6YE8b9l84bOOnLwhajlFG0mJIfQLjP6s03ibTicGj6EiazDF1Dxhg/640?wx_fmt=png&from=appmsg)

扫描二维码添加GobyBot微信，即可申请体验。

**注意：本次测试所有版本用户均可申请免费体验，无门槛~**

Goby邀请大家和GobyAI一同成长~

同时，Goby 欢迎各位师傅加入我们的社区大家庭，一起交流、生活趣事、奇闻八卦，结交无数好友。

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIiabR1dAPwPUfdMicdAYjpI64IJvW0ibvQHibec1lKpI5j2gBSHics8h2nBF9PRHv3NwauicLyB5lEWfmQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKtyy4YLV6TlU67xPQYD3DsJiaVkxicb5vj73SLiaxoJJ5AqWLySVqlG2dib4cHjRzzia90Mtq9DE5Mz0A/0?wx_fmt=png)

GobySec

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKtyy4YLV6TlU67xPQYD3DsJiaVkxicb5vj73SLiaxoJJ5AqWLySVqlG2dib4cHjRzzia90Mtq9DE5Mz0A/0?wx_fmt=png)

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