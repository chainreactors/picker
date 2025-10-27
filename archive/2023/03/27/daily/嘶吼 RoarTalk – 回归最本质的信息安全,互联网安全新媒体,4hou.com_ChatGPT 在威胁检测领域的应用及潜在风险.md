---
title: ChatGPT 在威胁检测领域的应用及潜在风险
url: https://www.4hou.com/posts/50jB
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-27
fetch_date: 2025-10-04T10:45:45.713485
---

# ChatGPT 在威胁检测领域的应用及潜在风险

ChatGPT 在威胁检测领域的应用及潜在风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ChatGPT 在威胁检测领域的应用及潜在风险

丝绸之路
[新闻](https://www.4hou.com/category/news)
2023-03-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)164296

收藏

导语：安全分析师的许多实验都在表明，流行的大型语言模型（LLM）ChatGPT 可能有助于帮助网络安全防御者分类潜在的安全事件并发现代码中的安全漏洞，即使人工智能（AI）模型没有专门针对此类活动进行训练。

事件响应分类和软件漏洞发现是大型语言模型成功的两个领域，尽管误报很常见。

![chatgpt-Kashif_khan-alamy.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529520144954.png "1678529520144954.png")

ChatGPT 是一个开创性的聊天机器人，由基于神经网络的语言模型 text-davinci-003 提供支持，并在来自互联网的大型文本数据集上进行训练。它能够生成各种样式和格式的类似人类的文本。ChatGPT 可以针对特定任务进行微调，例如回答问题、总结文本，甚至解决与网络安全相关的问题，例如，生成事件报告或解释反编译代码。安全研究人员和人工智能黑客都对ChatGPT产生了兴趣，尝试探索 LLM 的弱点，而其他研究人员以及网络犯罪分子则试图将LLM引诱到黑暗面，将其设置为产生力工具，用于生成更好的网络钓鱼电子邮件或生成恶意软件。已经有一些案例表明不法分子已经尝试利用ChatGPT生成恶意对象，例如，网络钓鱼电子邮件，甚至多态恶意软件。

安全分析师的许多实验都在表明，流行的大型语言模型（LLM）ChatGPT 可能有助于帮助网络安全防御者分类潜在的安全事件并发现代码中的安全漏洞，即使人工智能（AI）模型没有专门针对此类活动进行训练。

在对 ChatGPT 作为事件响应工具的实用程序的分析中，安全分析师发现 ChatGPT 可以识别在受感染系统上运行的恶意进程。通过使用Meterpreter和PowerShell Empire代理感染了一个系统，以对手的角色采取了共同的步骤，然后对系统运行了ChatGPT驱动的恶意程序扫描器。LLM 识别出系统上运行的两个恶意进程，并正确忽略了137个良性进程，利用ChatGPT 在很大程度上减少了开销。

安全研究人员也在研究通用语言模型如何在特定的防御相关任务上执行。去年12月，数字取证公司Cado Security使用ChatGPT分析来自真实安全事件的JSON数据创建了黑客入侵的时间表，从而生成了一份很好的但并不完全准确的报告。安全咨询公司NCC Group则尝试使用ChatGPT作为查找代码漏洞的一种方式，虽然ChatGPT确实做到了，但漏洞识别并不总是很准确。

从实际的使用来看，安全分析师，开发人员和逆向工程师在使用 LLM 时需要小心，特别是对于超出其能力范围的任务。安全咨询公司NCC Group的首席科学家Chris Anley说，“我绝对认为专业开发人员和其他使用代码开展工作的人应该探索 ChatGPT 和类似的模型，但更多的是为了灵感，而不是绝对正确的事实结果，”他说，并补充说“安全代码审查不是我们应该使用 ChatGPT 的事情，所以期望它第一次就完美是不公平的。”

**使用 AI 分析 IoC**

安全和威胁研究通常会以报告、演示文稿、博客文章、推文和其他类型的内容的形式公开披露其调查结果（对手指标、战术、技术和程序）。

![download_image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529571127273.png "1678529571127273.png")

因此，我们最初决定检查 ChatGPT 对威胁研究的了解，以及它是否可以帮助识别简单的、众所周知的对手工具，如 Mimikatz 和快速反向代理，并发现常见的重命名策略。输出看起来很有希望！

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529591200870.png "1678529591200870.png")

那么对于经典的入侵指标，例如众所周知的恶意哈希和域名ChatGPT能回答正确吗？不幸的是，在我们的快速实验中，ChatGPT 无法产生令人满意的结果：它未能识别 Wannacry 的知名哈希值（哈希：5bef35496fcbdbe841c82f4d1ab8b7c2).

![image(1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529607182249.png "1678529607182249.png")

对于多个 APT 活动使用的域名，ChatGPT 生成了一个基本相同的域名列表并提供了 APT 攻击者的描述，我们可能对有些域名一无所知？

![image(2).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529628185535.png "1678529628185535.png")

至于 FIN7 使用的域名，chatGPT 正确地将它们归类为恶意域名，尽管它给出的原因是，“域名很可能是试图欺骗用户相信它是一个合法的域名”，而不是有众所周知的入侵指标。

![image(3).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529647392423.png "1678529647392423.png")

虽然最后一个针对模仿知名网站域名的实验给出了一个有趣的结果，但还需要更多的研究：很难说为什么 ChatGPT 对基于主机的安全事件产生的结果要比对域名和哈希等简单指标的结果更好。某些过滤器可能已应用于训练数据集，或者如果以不同的方式构建问题本身（定义良好的问题就是解决了一半的问题！）

无论如何，由于对基于主机的安全事件的响应看起来更有希望，我们指示 ChatGPT 编写一些代码来从测试 Windows 系统中提取各种元数据，然后询问元数据是否是泄露的指标：

![download_image(1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529696504489.png "1678529696504489.png")

某些代码片段比其他代码片段更方便使用，因此我们决定继续手动开发此 PoC：我们筛选了 ChatGPT 的回答中包含有关存在入侵指标为“yes”的语句的事件输出，添加了异常处理程序和 CSV 报告，修复了小错误，并将代码片段转换为单独的 cmdlet， 这样就产生了一个简单的 IoC 安全扫描器 HuntWithChatGPT.psm1，能够通过WinRM扫描远程系统：

![download_image(2).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529748846108.png "1678529748846108.png")

![image(4).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529756156500.png "1678529756156500.png")

```
Get-ChatGPTIoCScanResults    -apiKey         OpenAI API key https://beta.openai.com/docs/api-reference/authentication           -SkipWarning []            -Path             -IoCOnly []        Export only Indicators of compromise            -ComputerName         Remote Computer's Name            -Credential         Remote Computer's credentials
```

我们用Meterpreter和PowerShell Empire代理感染了目标系统，并模拟了一些典型的攻击程序。在针对目标系统执行扫描程序时，它会生成一个包含 ChatGPT 结论的扫描报告：

![download_image(3).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529774579888.png "1678529774579888.png")

在 137 个良性进程中正确识别了两个恶意运行的进程，没有任何误报。

![download_image (2).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529802161174.png "1678529802161174.png")

请注意，ChatGPT 提供了它得出元数据是泄露指标的结论的原因，例如“命令行正在尝试从外部服务器下载文件”或“它正在使用”-ep bypass“标志，该标志告诉 PowerShell 绕过通常存在的安全检查”。

对于服务安装事件，我们稍微修改了问题，引导 ChatGPT “一步一步地思考”，这样它就会减慢速度并避免认知偏差，正如 Twitter 上的多位研究人员所建议的那样：

下面的 Windows 服务名称“ $ServiceName”和下面的 Launch String“ $Servicecmd”是妥协的指示器吗？请一步一步地思考。

![image (1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529820165519.png "1678529820165519.png")

ChatGPT 成功识别了可疑的服务安装，没有出现误报。它产生了一个有效的假设，即“代码被用于禁用Windows系统上的日志记录或其他安全措施”。对于第二项服务，它提供了关于为什么该服务应被归类为入侵指标的结论：“这两条信息表明 Windows 服务和启动服务的字符串可能与某种形式的恶意软件或其他恶意活动相关联，因此应被视为入侵指标”。

![download_image (3).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529831130359.png "1678529831130359.png")

在相应的 PowerShell cmdlets Get-ChatGPTSysmonProcessCreationIoC 和 Get-ChatGPTProcessCreationIoC 的帮助下，分析了 Sysmon 和 Security 日志中的进程创建事件。最后报告强调，有些事件是恶意的：

ChatGPT 在 ActiveX 代码中识别出可疑模式：“命令行包括启动新进程 （svchost.exe） 和终止当前进程 （rundll32.exe） 的命令”。

正确地描述了 lsass 进程转储尝试：“a.exe 正在使用提升的权限运行，并使用 lsass（代表本地安全机构子系统服务）作为其目标;最后，dbg.dmp 表示在运行调试程序时正在创建内存转储”。

正确检测到 Sysmon 驱动程序卸载：“命令行包括卸载系统监视驱动程序的说明”。

![download_image (4).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529850744713.png "1678529850744713.png")

在检查 PowerShell 脚本块时，我们修改了问题，不仅检查指标，还检查是否存在混淆技术：

以下 PowerShell 脚本是否经过模糊处理或包含入侵指标？“$ScriptBlockText”

ChatGPT 不仅能够检测到混淆技术，还列举了一些 XOR加密，Base64编码和变量替换。

![download_image (5).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529864103524.png "1678529864103524.png")

当然，这个工具并不完美，可以同时产生误报或漏报。

在下面这个例子中，ChatGPT 没有检测到通过 SAM 注册表转储系统凭据的恶意活动行为，而在另一个示例中，将 lsass.exe 进程描述为可能表明“恶意活动或安全风险，例如系统上运行的恶意软件”：

![download_image (6).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529880120523.png "1678529880120523.png")

这个实验的一个有趣的结果是数据集中的数据缩减。在测试系统上模拟对手后，分析师要验证的事件数显著减少：

![image (2).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678529895106257.png "1678529895106257.png")

请注意，测试是在新的非生产系统上执行的。如果是生产系统可能会产生更多的误报。

**实验结论**

在上面的实验中，安全分析师开展的实验始于向 ChatGPT 询问几种黑客工具，如 Mimikatz 和 Fast Reverse Proxy。AI模型成功地描述了这些工具，但是当被要求识别众所周知的哈希和域名时，ChatGPT失败了，没有正确描述。例如，LLM 无法识别WannaCry恶意软件的已知哈希值。然而，识别主机上恶意代码的相对成功使得安全分析师尝试要求ChatGPT创建一个PowerShell脚本，目的是为了从系统中收集元数据和入侵指标，并将其提交给LLM。

总体而言，安全分析师使用 ChatGPT 分析了测试系统上 3500 多个事件的元数据，发现了 74 个潜在的入侵指标，其中 17 个是误报。该实验表明，ChatGPT 可用于为那些在未运行端点检测和响应 （EDR） 系统、检测代码混淆或逆向工程代码二进制文件的公司收集取证信息。

虽然 IoC 扫描的确切实施目前可能不是一个非常具有成本效益的解决方案，每个主机大约15-25美元，但它显示了有趣的中性结果，并揭示了未来研究和测试的机会。我们在研究过程中注意到如下几个ChatGPT作为安全分析师生产...