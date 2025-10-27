---
title: ChatGPT 写 PoC，拿下漏洞！
url: https://mp.weixin.qq.com/s?__biz=MzI4MzcwNTAzOQ==&mid=2247527209&idx=1&sn=5a549945a40b73d6731b3d5ad8904c81&chksm=eb848089dcf3099f7469e26717431f80f3a94261ab4cbfb02cd4a1ac23ae4b645a53e082fe1e&scene=58&subscene=0#rd
source: GobySec
date: 2023-03-25
fetch_date: 2025-10-04T10:37:58.161628
---

# ChatGPT 写 PoC，拿下漏洞！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4sA510K7kpoqf9vtwahjOmPqQY1S3iaDGxNPS4bpFtrKic5iaVQ6icoIM8A/0?wx_fmt=jpeg)

# ChatGPT 写 PoC，拿下漏洞！

原创

LPuff

GobySec

![](https://mmbiz.qpic.cn/mmbiz_gif/GGOWG0fficjLTMIjhRPrloPMpJ4nXfwsIjLDB23mjUrGc3G8Qwo770yYCQAnyVhPGKiaSgfVu0HKnfhT4v5hSWcQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb40LViafmR6IhJE39n1R6pica4pDia71aibEibr8QyUnvokoLibrfylAh0ydqg/640?wx_fmt=jpeg)

Goby社区第 23 篇技术分享文章

全文共：3901 字   预计阅读时间：10 分钟

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKzq4TFicia2yUjianoH80KtrWElvrR0XQbqBDCHC68DicU6TwYLR54jEJE3rqy2icwicrV85dICfKrJsOQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) **01****前言**

ChatGPT（Chat Generative Pre-trained Transformer）是当今备受瞩目的智能AI聊天机器人之一。它不仅能够实现基本的语言交流，还具备许多强大的功能，例如文章撰写、代码脚本编写、翻译等等。那么我们是否可以利用 ChatGpt 去辅助我们完成一些工作呢？比如当一个产品存在安全风险需要漏洞检测时，我们就需要编写对应的POC来实现。目前进行多次验证，我们初步证实了这个实验的可行性，可以训练 ChatGPT 去编写简单的 PoC，但是它对细节的把控并不够完善，例如对输出内容进行匹配的正则表达式的编写和一些复杂逻辑的处理等存在一定的误差，还需要人工干预修改处理。另外我们利用比对的方式验证了 ChatGPT 的一些安全猜想和训练模型的准确性。如下是将其与 Goby 实战化网络攻防工具所结合进行利用检测的实现效果：

![](https://mmbiz.qpic.cn/mmbiz_gif/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4Oqg7umXyxqCV3KkHHeRcXliabaSxxQwbQVFYx0tibm8X5UZUcbiapOXbQ/640?wx_fmt=gif)

##

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKzq4TFicia2yUjianoH80KtrWElvrR0XQbqBDCHC68DicU6TwYLR54jEJE3rqy2icwicrV85dICfKrJsOQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) **02 训练过程**

我们利用 ChatGPT 与 Goby 结合编写 PoC 与 EXP 有两种方法：半自动编写和全自动编写（过程中使用 ChatGPT-Plus 账号）。

半自动编写利用 ChatGPT 进行语言格式转换，转换后生成的代码可能存在细节问题，需要进一步排错完善，最后修改对应的语句和函数内容完成 PoC 与 EXP 的编写。

全自动编写通过将使用到的代码模板、漏洞详细信息给到 ChatGPT，让它自动生成对应模板的 PoC，在给出详细信息时需要注意信息的完整与准确。目前可以实现自动编写简单的 PoC，对于EXP来说还需要进一步训练 ChatGPT 对 Goby 内置函数的使用等。

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKzq4TFicia2yUjianoH80KtrWElvrR0XQbqBDCHC68DicU6TwYLR54jEJE3rqy2icwicrV85dICfKrJsOQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) **03 CVE-2010-2861**

Adobe ColdFusion 是一款高效的网络应用服务器开发环境。Adobe ColdFusion 9.0.1 及之前版本的管理控制台中存在多个目录遍历漏洞。远程攻击者可借助向 /CFIDE/administrator/enter.cfm 和 /CFIDE/administrator/archives/index.cfm 等发送的 locale 参数读取任意文件。

**3.1 半自动编写**

首先尝试让 ChatGPT 将 CVE-2010-2861 目录遍历漏洞的 Python 格式 EXP 转换为 Go 语言格式的代码，这样可以利用 ChatGPT 代替人工完成代码解释及代码转换的过程。

我们在漏洞公开平台中选取该漏洞的 EXP 代码：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4j87WPYaz9NIlAYxuheazNc1ictHGywc10ZKWxmvyXhsX1CaIsShPduw/640?wx_fmt=png)

在使用 ChatGPT 将相应漏洞的 EXP 代码转换之前，先演示一下原始 Python 代码的执行效果，具体如下：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb45e289glFh274vpykibkKSianIzs3icNO2B6QGibnR20mm8ugfBPoOSXgYw/640?wx_fmt=png)

开始转化格式：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4sKkDLV6KRrC2wmSLegIx8klb2ERFrvv8UX05iblvNicALNicicPSXgpUHA/640?wx_fmt=png)

此外，他还提供了该程序的使用方法。然而，每次 ChatGPT 的回答都可能不完全相同。此前的回答中并没有详细说明函数的具体用法，但在另一个回答中给出了以下解释：（如果需要，可在问题中增加“并介绍函数的具体用法”）

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4gve7ValN9dC70taRkTDbC7ktN9cK7LodOtOc1CxuV103hFJvjRlYiag/640?wx_fmt=png)

最后进行代码调试后，发现无法立即使用，未能成功读取所需的文件内容：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4DrbnkoW1pr9SvUebNUJeCgF2IZ1k91ASiaHtjiaK4ztj29TDNIAkMlew/640?wx_fmt=png)

那么就需要开始排错，以下是排错过程：

检查正则匹配后字符串是否为空：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4L7lNNDm2boM3Lc4g7FnnicSibVEMSEQZfqtvITaExXAZpqXLvR21SsyA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4Kmhibibm3LDecWFFQ0jqUwGaRcfcFiaZMtnZSIQaXk61BbLEYMiboibdLxg/640?wx_fmt=png)

检查返回包内容是否正常，有无所需内容，如下返回数据包显示正常：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb48skrSdeicX4En5bVMftSEuhuRXdSRWjhzuLo8U8fhjFyK9nehhkdngA/640?wx_fmt=png)

判断正则表达式有问题，无法匹配到对应内容：

通过排查发现正则表达式中没有正确匹配，因此无法将文件的内容正确取出，做出以下修改，修改后内容具体如下：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4LscffUgUyIazWD6dKQFoaZqc3PTQJYdLSAbbniaGnE6XYOjWDRUKgyQ/640?wx_fmt=png)

修改前：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4QJFL7cSFFWUTNSHVxh9dXeskRI0Nia2KWZep8B05JsCEfia1w9WQj62Q/640?wx_fmt=png)

最终执行结果，完成 Python—Go 的转化：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4BSK9LPY6DfEiaibEr7AIwYYKH5DS3cMIbhonkWh5nobEaGhJGtlxqDibw/640?wx_fmt=png)

前面我们已经成功将 Python 格式的EXP转换为了 Go 语言格式，现在尝试将其转换为 Goby 格式的 PoC 和 EXP。

由于 Goby 使用的是基于 Go 语言开发的自研漏洞框架，为方便用户使用，其中已有很多内置函数可供用户使用，所以只需要利用上述部分代码即可完成 PoC 和 EXP，以下是 EXP 修改的大致说明与详细内容：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4tBsAcPe4XNFibF03vOztR8qhbeMk4mCzNkh5J6vzktp89ctjIfRTuqQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4dMqtKnqEHxFKgPln2BGsq70FqJlum0bq8Q5Zj1ufBwptRFeuekHKPg/640?wx_fmt=png)

修改 import 内容：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4wMRiaOGPFffaUMcJG5Xic65uHbUB3lkV8Jmwc1owia1lia1Nic4U5XLtTrg/640?wx_fmt=png)

由于生成的 EXP 在命令行使用时需要手动输入参数：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4yBnAdFX3HZbSgj3bCVUERkzmb8s1NySnZDiaZr6YJiaHQictfffpg7Vag/640?wx_fmt=png)

那么在 PoC 转化时，需要重新定义常量，并利用 Goby 中的 httpclient.FixUrl.IP 与 httpclient.FixUrl.Port 获取测试的 IP 和端口号，确定测试的文件路径 path：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4lRz6Gh8qKYicQIYSvial4zP4ytKLuYG5PNKo3KiaHJQkdxHjc2ZCL82RQ/640?wx_fmt=png)

接着在 PoC 中添加条件判断语句，判断漏洞存在的特征，并返回 true（有漏洞）：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4W39LAnFArC0E69R4biaf9R626zlZIQ65Mvc4jtNrvKFBdehtjmoCqfA/640?wx_fmt=png)最后删除多余的输出打印代码即可完成 PoC 转化，如：
![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4hAAibH7pHxm5VclezkdufiaMP2jia2EpzEiaG8MjY0FC1WCZg65xibyn5Zg/640?wx_fmt=png)

EXP 转化时，需重新定义变量，利用 Goby 中的 expResult.HostInfo.IP 与 expResult.HostInfo.Port 获取测试的IP和端口号，利用 ss.Params["filePath"]. (string) 获取用户输入的 EXP 参数——测试文件路径 filePath：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4WlDxNZwhDqIibubU1oeIRJnxqoVM2ibOjqkbWDmCib5v8298Dliaia2IL2Q/640?wx_fmt=png)

接着在 EXP 代码中添加条件判断语句，判断 EXP 是否执行成功，并输出 EXP 执行结果，完成 EXP 转化：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4nAHfZiaEXLmlS48BNflpQG5qEh3o1AWd146C0eNG3heFCYiaPhGpUia2Q/640?wx_fmt=png)

**3.2 全自动编写**

在使用 ChatGPT 与人工相结合编写后，我们进一步尝试使用它来撰写 Goby 格式的 PoC。

首先将 Goby 格式的模板给出：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4sxgsXQMZK7Dq168xAWLrubrTYY9nlRgCc2VlRbvfiaTOPzmFDUeJItQ/640?wx_fmt=png)

接着将漏洞的编号、产品、类型、Url、漏洞文件、参数和判断成功条件给出，说明相关的字段格式，我们最终得到了下面的代码，它已经可以通过 Goby 前端的编译，并可以成功地生成简单的 PoC：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4Xhq8kKdibIqicUK5LTlS5GQzsfPhuN4QfNn0lFtNzEbENZTJQVeszScg/640?wx_fmt=png)

模型训练初步完成，继续使用第二个案例验证模型完善程度：
![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4Yejib3wDf09ef9ELqIlgU0aFPDuImWtXkcx1WYmWjfEavvupKqrjsIA/640?wx_fmt=png)

发现 Name 字段还是存在格式错误，再次训练修改（若验证中 Name 字段等输出正确，那么即可跳过此纠错步骤）：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4w13hzQrm8vlbMHDoDFdSxiax1IS0ZVgicq3yOGAZ2am9KqUr30vFN9fw/640?wx_fmt=png)

最后使用第三个案例进行验证最终的训练结果，训练成功：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4oXibv0ia3L50Nq9B8yFicYyWbuCc1odT19p2DgVHrRcjicKT3kmv23wCtw/640?wx_fmt=png)

将代码放入 Goby 中，并填入缺少的漏洞描述信息（后续还可继续深入训练），运行效果如下：

 ![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjKzq4TFicia2yUjianoH80KtrWElvrR0XQbqBDCHC68DicU6TwYLR54jEJE3rqy2icwicrV85dICfKrJsOQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) **04 自我学习**

当我们在利用 ChatGPT 去帮助编写一个新鲜出炉的 0day 漏洞或者其他机密漏洞的检测 PoC 这个过程当中，是否会导致程序注入或信息泄露等问题呢？也就是说当模型训练完成后，其他用户提问相关的内容，ChatGPT 是否会直接将训练好的模型或数据直接输出呢？

为了验证 ChatGPT 自我学习的猜想是否存在，分别通过“不同会话”与“不同账户”来进行训练。经过以下实践，得到的结论是 ChatGPT 并不会进行跨会话与跨账号的自我学习，训练好的模型与数据是掌握在 OpenAI 手中的，其他用户并不会得到相关的模型，所以目前还不存在相关信息数据泄露的安全风险，但日后的情况还需要根据 OpenAI 采取的决策做判断。

**4.1 不同会话比对**

将使用的模板（此处省略示意图）和漏洞信息给出，可以看到 PoC 中的 Name 和 Desc ription 字段并没有按照上一个会话中的训练模式来进行填充，因此在不同会话当中 ChatGPT 并不会自我学习，每个会话间的训练模型独立：

![](https://mmbiz.qpic.cn/mmbiz_png/GGOWG0fficjIHqLb6QW9NRrYuR6zILLb4zicygFeGTHAvNzEsKtPILlt6CaFq7JHpxkze5FRKuyzsJwDmrrN70Kg/640?wx_fmt=png)

**4.2 不同账号比对**

同样将模...