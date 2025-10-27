---
title: ChatGPT 在威胁检测领域的应用及潜在风险
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535771&idx=3&sn=b9121f647515942c06de21585ec01e9c&chksm=fa93fa5acde4734c1daa4f0942e1eb070a33620f7f777ef61081e111a1018ac6b58a0c5a52ab&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-28
fetch_date: 2025-10-04T10:53:40.138068
---

# ChatGPT 在威胁检测领域的应用及潜在风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lMOgNUe63dZVjeVYtwqN71ZekW9iceH44RdBXRicrrTtBanzc8QEj6IibIORGscwjP3AL1arqbmx12Q/0?wx_fmt=jpeg)

# ChatGPT 在威胁检测领域的应用及潜在风险

网络安全应急技术国家工程中心

事件响应分类和软件漏洞发现是大型语言模型成功的两个领域，尽管误报很常见。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMza9mrNZ5UlYPviaE1kEPywsSicgxf1ZqsJwKzpFJn3ribTbOALawic72Kg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

ChatGPT 是一个开创性的聊天机器人，由基于神经网络的语言模型 text-davinci-003 提供支持，并在来自互联网的大型文本数据集上进行训练。它能够生成各种样式和格式的类似人类的文本。ChatGPT 可以针对特定任务进行微调，例如回答问题、总结文本，甚至解决与网络安全相关的问题，例如，生成事件报告或解释反编译代码。安全研究人员和人工智能黑客都对ChatGPT产生了兴趣，尝试探索 LLM 的弱点，而其他研究人员以及网络犯罪分子则试图将LLM引诱到黑暗面，将其设置为产生力工具，用于生成更好的网络钓鱼电子邮件或生成恶意软件。已经有一些案例表明不法分子已经尝试利用ChatGPT生成恶意对象，例如，网络钓鱼电子邮件，甚至多态恶意软件。

安全分析师的许多实验都在表明，流行的大型语言模型（LLM）ChatGPT 可能有助于帮助网络安全防御者分类潜在的安全事件并发现代码中的安全漏洞，即使人工智能（AI）模型没有专门针对此类活动进行训练。

在对 ChatGPT 作为事件响应工具的实用程序的分析中，安全分析师发现 ChatGPT 可以识别在受感染系统上运行的恶意进程。通过使用Meterpreter和PowerShell Empire代理感染了一个系统，以对手的角色采取了共同的步骤，然后对系统运行了ChatGPT驱动的恶意程序扫描器。LLM 识别出系统上运行的两个恶意进程，并正确忽略了137个良性进程，利用ChatGPT 在很大程度上减少了开销。

安全研究人员也在研究通用语言模型如何在特定的防御相关任务上执行。去年12月，数字取证公司Cado Security使用ChatGPT分析来自真实安全事件的JSON数据创建了黑客入侵的时间表，从而生成了一份很好的但并不完全准确的报告。安全咨询公司NCC Group则尝试使用ChatGPT作为查找代码漏洞的一种方式，虽然ChatGPT确实做到了，但漏洞识别并不总是很准确。

从实际的使用来看，安全分析师，开发人员和逆向工程师在使用 LLM 时需要小心，特别是对于超出其能力范围的任务。安全咨询公司NCC Group的首席科学家Chris Anley说，“我绝对认为专业开发人员和其他使用代码开展工作的人应该探索 ChatGPT 和类似的模型，但更多的是为了灵感，而不是绝对正确的事实结果，”他说，并补充说“安全代码审查不是我们应该使用 ChatGPT 的事情，所以期望它第一次就完美是不公平的。”

# **使用 AI 分析 IoC**

安全和威胁研究通常会以报告、演示文稿、博客文章、推文和其他类型的内容的形式公开披露其调查结果（对手指标、战术、技术和程序）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMo0pyrcAicBgb3ZeYmySCr5JhffNSUX9fehuKmcsbOvicdJ2y3C8EQXrw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

因此，我们最初决定检查 ChatGPT 对威胁研究的了解，以及它是否可以帮助识别简单的、众所周知的对手工具，如 Mimikatz 和快速反向代理，并发现常见的重命名策略。输出看起来很有希望！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMf7MsvMtAJ5p1y7fx7xNo1puQupGUZQ9edx8ZG8UYjnergYOM0qB1Cw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

那么对于经典的入侵指标，例如众所周知的恶意哈希和域名ChatGPT能回答正确吗？不幸的是，在我们的快速实验中，ChatGPT 无法产生令人满意的结果：它未能识别 Wannacry 的知名哈希值（哈希：5bef35496fcbdbe841c82f4d1ab8b7c2).

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMgX4hiay0PXVUF0T9j8XY5hGBMRJ9KOcTialVz0aUdAj3zQI2rHmAibUcA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

对于多个 APT 活动使用的域名，ChatGPT 生成了一个基本相同的域名列表并提供了 APT 攻击者的描述，我们可能对有些域名一无所知？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMibBbkouzgXH65jYjMszafZKvusewX3D8rOmfCY2M4cQvzAdy9SBoDtw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

至于 FIN7 使用的域名，chatGPT 正确地将它们归类为恶意域名，尽管它给出的原因是，“域名很可能是试图欺骗用户相信它是一个合法的域名”，而不是有众所周知的入侵指标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeM50KmzFjz55aUMgebZoickgmOyL4S46RupsLic9Ito52QIFsGSnQhyUnA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

虽然最后一个针对模仿知名网站域名的实验给出了一个有趣的结果，但还需要更多的研究：很难说为什么 ChatGPT 对基于主机的安全事件产生的结果要比对域名和哈希等简单指标的结果更好。某些过滤器可能已应用于训练数据集，或者如果以不同的方式构建问题本身（定义良好的问题就是解决了一半的问题！）

无论如何，由于对基于主机的安全事件的响应看起来更有希望，我们指示 ChatGPT 编写一些代码来从测试 Windows 系统中提取各种元数据，然后询问元数据是否是泄露的指标：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMKkzW1lQ0ZqSMzSDOhIAWDIju8gdw9t9trfxtXtmNgib62XEqgCxHcUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

某些代码片段比其他代码片段更方便使用，因此我们决定继续手动开发此 PoC：我们筛选了 ChatGPT 的回答中包含有关存在入侵指标为“yes”的语句的事件输出，添加了异常处理程序和 CSV 报告，修复了小错误，并将代码片段转换为单独的 cmdlet， 这样就产生了一个简单的 IoC 安全扫描器 HuntWithChatGPT.psm1，能够通过WinRM扫描远程系统：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMicWiaiapIBnD0cC0DQ3FeHDLm91saFEmyobwWKED12OolFcdK4OPaOLCA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMgxhL6HicGxoyuiaB8sulcodQX1xLjFV3FMyjc46lneIE6wBkMRrep9gQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

```
Get-ChatGPTIoCScanResults    -apiKey         OpenAI API key https://beta.openai.com/docs/api-reference/authentication           -SkipWarning []            -Path             -IoCOnly []        Export only Indicators of compromise            -ComputerName         Remote Computer's Name            -Credential         Remote Computer's credentials
```

我们用Meterpreter和PowerShell Empire代理感染了目标系统，并模拟了一些典型的攻击程序。在针对目标系统执行扫描程序时，它会生成一个包含 ChatGPT 结论的扫描报告：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMdXDC9uuc6nJERf8cfSLbkjH1PiaASPmAu6Qic9ooMkKI7b61sWtqrM4g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在 137 个良性进程中正确识别了两个恶意运行的进程，没有任何误报。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMd4CtMxkiaMkmsbnX8zhB1yOYg7BiaKPZb6wJLzWG0JXkicNiaLyFJxDuXQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

请注意，ChatGPT 提供了它得出元数据是泄露指标的结论的原因，例如“命令行正在尝试从外部服务器下载文件”或“它正在使用”-ep bypass“标志，该标志告诉 PowerShell 绕过通常存在的安全检查”。

对于服务安装事件，我们稍微修改了问题，引导 ChatGPT “一步一步地思考”，这样它就会减慢速度并避免认知偏差，正如 Twitter 上的多位研究人员所建议的那样：

下面的 Windows 服务名称“ $ServiceName”和下面的 Launch String“ $Servicecmd”是妥协的指示器吗？请一步一步地思考。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMJoibd6SHPBRiaibic7T1icM2s4hIfgSxXI50jKKLKGxooDr6pZ7qocwgQJw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

ChatGPT 成功识别了可疑的服务安装，没有出现误报。它产生了一个有效的假设，即“代码被用于禁用Windows系统上的日志记录或其他安全措施”。对于第二项服务，它提供了关于为什么该服务应被归类为入侵指标的结论：“这两条信息表明 Windows 服务和启动服务的字符串可能与某种形式的恶意软件或其他恶意活动相关联，因此应被视为入侵指标”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMXft8JaeNm7ibuE6ZdRVv9uZN6k4FnvDoURo6TKxh8xGcJ2TwC5cnWAw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在相应的 PowerShell cmdlets Get-ChatGPTSysmonProcessCreationIoC 和 Get-ChatGPTProcessCreationIoC 的帮助下，分析了 Sysmon 和 Security 日志中的进程创建事件。最后报告强调，有些事件是恶意的：

ChatGPT 在 ActiveX 代码中识别出可疑模式：“命令行包括启动新进程 （svchost.exe） 和终止当前进程 （rundll32.exe） 的命令”。

正确地描述了 lsass 进程转储尝试：“a.exe 正在使用提升的权限运行，并使用 lsass（代表本地安全机构子系统服务）作为其目标;最后，dbg.dmp 表示在运行调试程序时正在创建内存转储”。

正确检测到 Sysmon 驱动程序卸载：“命令行包括卸载系统监视驱动程序的说明”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMX69M0u8gYYxBZW9jtgpvLGcibAA13xUPFK8hz3NVbbV2XuA0BvlaKNQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在检查 PowerShell 脚本块时，我们修改了问题，不仅检查指标，还检查是否存在混淆技术：

以下 PowerShell 脚本是否经过模糊处理或包含入侵指标？“$ScriptBlockText”

ChatGPT 不仅能够检测到混淆技术，还列举了一些 XOR加密，Base64编码和变量替换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMpBpY7D8iaLwkyMajcDoPQ0gXuw1ac20elEEBfTIQwrFWJrkC8bjRhEQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

当然，这个工具并不完美，可以同时产生误报或漏报。

在下面这个例子中，ChatGPT 没有检测到通过 SAM 注册表转储系统凭据的恶意活动行为，而在另一个示例中，将 lsass.exe 进程描述为可能表明“恶意活动或安全风险，例如系统上运行的恶意软件”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMjxEaNYFHeRCBK0EyW4ZYW2KYLPw1goibOOgK9WF8L6f7pc7bjibRoImg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

这个实验的一个有趣的结果是数据集中的数据缩减。在测试系统上模拟对手后，分析师要验证的事件数显著减少：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMKbJdaODLASfOChCpAibpHpicwqib0SzYZiaoSI3E8wzsR2SsXqI4utnGicQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

请注意，测试是在新的非生产系统上执行的。如果是生产系统可能会产生更多的误报。

# **实验结论**

在上面的实验中，安全分析师开展的实验始于向 ChatGPT 询问几种黑客工具，如 Mimikatz 和 Fast Reverse Proxy。AI模型成功地描述了这些工具，但是当被要求识别众所周知的哈希和域名时，ChatGPT失败了，没有正确描述。例如，LLM 无法识别WannaCry恶意软件的已知哈希值。然而，识别主机上恶意代码的相对成功使得安全分析师尝试要求ChatGPT创建一个PowerShell脚本，目的是为了从系统中收集元数据和入侵指标，并将其提交给LLM。

总体而言，安全分析师使用 ChatGPT 分析了测试系统上 3500 多个事件的元数据，发现了 74 个潜在的入侵指标，其中 17 个是误报。该实验表明，ChatGPT 可用于为那些在未运行端点检测和响应 （EDR） 系统、检测代码混淆或逆向工程代码二进制文件的公司收集取证信息。

虽然 IoC 扫描的确切实施目前可能不是一个非常具有成本效益的解决方案，每个主机大约15-25美元，但它显示了有趣的中性结果，并揭示了未来研究和测试的机会。我们在研究过程中注意到如下几个ChatGPT作为安全分析师生产力工具的领域：

系统检查入侵指标，尤其是在您仍然没有充满检测规则的 EDR 并且需要执行一些数字取证和事件响应 （DFIR） 的情况下;

将当前基于签名的规则集与 ChatGPT 输出进行比较以识别差距 — 总有一些技术或程序是您作为分析师不知道或忘记为其创建签名的。

检测代码混淆;

相似性检测：将恶意软件二进制文件提供给 ChatGPT，并尝试询问它是否有新的二进制文件与其他二进制文件相似。

正确提出问题就已经解决了一半的问题，试验问题和模型参数中的各种语句可能会产生更有价值的结果，即使对于哈希和域名也是如此。此外，要当心这可能产生的误报和漏报。因为归根结底的说，这只是另一个容易产生意外结果的统计神经网络。

# **合理使用和隐私规则需要澄清**

类似的实验还提出了一些关于提交给OpenAI的ChatGPT系统的数据的关键问题。公司已经开始反对使用互联网上的信息创建数据集，Clearview AI和Stability AI等公司面临诉讼，试图减少其机器学习模型的使用。

隐私是另一个问题。NCC Group的Anley说，“安全专业人员必须确定提交的入侵指标是否暴露了敏感数据，或者提交软件代码进行分析是否侵犯了公司的知识产权。”，“向 ChatGPT 提交代码是否是个好主意在很大程度上取决于具体情况，”他还说，“很多代码都是专有的，受到各种法律保护，所以我不建议人们向第三方提交代码，除非他们得到许可。”

其他安全专家也发出了类似的警告：使用 ChatGPT 检测入侵会向系统发送敏感数据，这可能违反公司政策，并可能带来业务风险。通过使用这些...