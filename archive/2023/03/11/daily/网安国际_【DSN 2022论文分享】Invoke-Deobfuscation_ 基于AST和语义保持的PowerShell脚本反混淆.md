---
title: 【DSN 2022论文分享】Invoke-Deobfuscation: 基于AST和语义保持的PowerShell脚本反混淆
url: https://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312255&idx=1&sn=260c8da492bfa3b4867c41be6d37909d&chksm=8bc48f31bcb306275802f97a29880f761de59c02ecd1cdccc4e627c4f638e02ee2bb1574da3a&scene=58&subscene=0#rd
source: 网安国际
date: 2023-03-11
fetch_date: 2025-10-04T09:17:43.422417
---

# 【DSN 2022论文分享】Invoke-Deobfuscation: 基于AST和语义保持的PowerShell脚本反混淆

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icelxY6ibIXSXxibNrJvBtVbDeAh39FHQ4YiaEuU2wMFOJFny9wMTK12xY3P2A4ZjswOaWEUWdribFQYvJibqp1yoXfg/0?wx_fmt=jpeg)

# 【DSN 2022论文分享】Invoke-Deobfuscation: 基于AST和语义保持的PowerShell脚本反混淆

原创

柴华君

网安国际

**前言**

本文根据英文原文“Invoke-Deobfuscation: AST-Based and Semantics-Preserving Deobfuscation for PowerShell Scripts.”整理撰写。原文发表在IEEE/IFIP International Conference on Dependable Systems and Networks. 2022. 本文较原文有所删减，详细内容可参考原文。

01

**介绍**

PowerShell是Windows上一个强大的工具，广泛用于网络攻击。PowerShell由命令行shell和相关脚本语言组成。它提供了对机器内核的访问，包括对Windows API的无限制访问。因此，越来越多的网络犯罪分子将PowerShell加入了他们的攻击武器库。2020年，根据RedCanary的威胁检测结果，PowerShell被报告为最常见的攻击技术。

混淆的PowerShell脚本可以使恶意代码检测结果不可靠，容易逃避杀毒软件的检测。近年来，许多基于机器学习和深度学习的模型被提出来用于检测恶意脚本。由于混淆可以完全修改脚本的文本特征，因此这些模型不能正确地检测混淆的恶意脚本。有许多公开的混淆工具，如Invoke-Obfuscation，恶意PowerShell脚本经过混淆之后可以轻松逃避VirusTotal中最先进的反病毒引擎的检测。此外，现有的反混淆工具在还原混淆脚本方面表现不佳。例如，Windows Antimalware Scan Interface (AMSI）是许多反病毒集成的流行的反混淆接口，它可以通过捕获最终被提供给脚本引擎的文本内容来处理混淆脚本。它仍然可以被简单地混淆技术，如字符串拼接轻松绕过。因此，反混淆工作在恶意脚本检测和分析中起到了重要作用。如下图所示，反混淆是混淆的反向过程，因此安全分析人员可以从反混淆结果中获得更有用的信息，以进一步分析。

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSXxibNrJvBtVbDeAh39FHQ4YwiaT6iaib8PiaoY82WIEibhguXcD9iaSK235rHXTg5YqkRSXEjxTdNYHVmicQ/640?wx_fmt=png)

**图1:  混淆与反混淆的简单示例**

现有方法反混淆主要分为三个步骤，即识别混淆脚本片段、还原混淆和重构脚本。PSDEM、PSDecode、PowerDrive和PowerDecode设计了一组正则表达式来匹配混淆脚本片段。然而，这些基于正则表达式的方法忽略了脚本的语法信息，因此它们经常识别带有无效语法的错误脚本片段。李振源等人使用基于机器学习的分类器来识别混淆脚本片段。他们的分类器使用抽象语法树（AST）节点的特征来识别具有有效语法的混淆片段，这在很大程度上取决于训练数据的质量。

预定义还原规则、函数重载和直接执行是三种常见的反混淆方法。预定义的还原规则按照混淆的类型模拟还原过程，对于一些特定的混淆技术非常有效，但经常因忽略混淆脚本片段的语法而得到错误的结果。函数重载用于处理特定函数的混淆参数，如Invoke-Expression。它拦截目标函数并捕获它们经过多次反混淆的运行时参数，这个方法有很大局限性。直接执行是另一种处理混淆脚本片段的方法。由于大部分混淆脚本块中既包含混淆数据，也包含相应地还原代码，直接执行还原代码即可对混淆数据进行反混淆处理。但是，由于缺少上下文，该方法无法正确处理带变量的混淆片段。

现有反混淆工具的所有脚本重构方法都是上下文无关的，因此它们最终的反混淆脚本可能不符合语法或在语义上不一致。它们一次替换脚本中所有相同的混淆片段，这会忽略这些片段的不同上下文，并可能改变脚本的语义。

对 PowerShell 脚本进行反混淆处理存在三个主要挑战。1.精确识别：第一个挑战是如何精确识别混淆脚本片段。2.正确还原：第二个挑战是如何从混淆的脚本片段中正确还原原始脚本片段。3.合法重构：最后一个挑战是如何确保最终重构的脚本在语法和语义上与原始脚本一致。

为了克服这些挑战，我们提出了一种基于AST的反混淆方法，Invoke-Deobfuscation。为了获得正确的反混淆结果，Invoke-Deobfuscation 1) 根据脚本 AST 的标记和可还原节点识别混淆的脚本片段，2) 跟踪变量以获取混淆脚本片段的上下文并借助Invoke函数，3）基于AST的后序遍历重构脚本，严格原地替换混淆部分，尽可能保持脚本的原始语义。

为了评估我们的方法在真实 PowerShell 脚本中的有效性，我们收集了 2,025,175 个真实恶意样本。经过基于文件内容和文件结构的文件类型验证、语法验证和去重等预处理，我们最终得到了一个包含39713个PowerShell脚本的大数据集。我们从四个方面评估Invoke-Deobfuscation，即处理不同混淆技术的能力、反混淆效果和效率、语义一致性和混淆缓解。我们将 Invoke-Deobfuscation 与其他四种反混淆工具进行比较，即 PSDecode、PowerDrive、PowerDecode 和 Li 等。实验结果表明 Invoke-Deobfuscation 表现最佳：1) Invoke-Deobfuscation 足够强大，可以应对几乎所有已知的混淆技术，2) Invoke-Deobfuscation 表现高效稳定，3) 关键信息量，如 IP、URL 等等，通过Invoke-Deobfuscation还原是其他工具的两倍以上，4）Invoke-Deobfuscation可以使反混淆结果在语义上与原始脚本保持一致，5）Invoke-Deobfuscation可以显著减轻脚本混淆。

本文做出以下贡献：

 我们提出了第一个基于 AST 和保留语义的带有变量跟踪的反混淆方法，Invoke-Deobfuscation。能够准确识别并正确还原混淆后的脚本片段，确保反混淆后的脚本语法有效、语义不变。

 我们使用PowerShell语言设计并实现了Invoke-Deobfuscation，这是一款设计精良、跨平台且易于使用的工具。开发人员可以轻松使用和集成我们工具的模块。

l Invoke-Deobfuscation 在反混淆效率和有效性、语义一致性和混淆缓解方面优于最先进的工具。Invoke-Deobfuscation 还原的关键信息量远超其他工具。Invoke-Deobfuscation 的所有结果执行与原始样本相同的网络行为。此外，Invoke-Deobfuscation 将样本的混淆分数显著降低了 46%。

 我们引入了一个包含 39,713 个真实恶意 PowerShell 脚本的大型数据集，涵盖了所有已知的混淆方法。

为了促进未来的研究，我们在 Gitee上发布了Invoke-Deobfuscation的源代码和数据集。

02

**背景及动机**

**1.PowerShell和PowerShell 攻击**

PowerShell 是一种命令行Shell和强大的脚本语言。它提供了前所未有的对机器内核的访问，包括对 Windows APIs的无限制访问。PowerShell是一个跨平台（Windows、Linux 和 macOS）工具并预安装在 Windows上。因此，PowerShell成为攻击者最喜欢的工具。

PowerShell 已广泛用于各种网络攻击，例如勒索软件、钓鱼邮件、持续性威胁等。攻击者可以利用恶意的PowerShell脚本在受害者的计算机上安装木马、窃取机密信息并获得管理员控制权等。PowerShell攻击不仅可以从远程网站下载恶意可执行文件，还可以直接通过系统内存加载这些文件，从而绕过传统的基于文件的防御方法。

**2. PowerShell 的混淆技术**

PowerShell 脚本可以通过各种灵活的方式轻松混淆，以逃避反病毒软件的检测。混淆的脚本很难被人类和反病毒软件理解和分析。根据混淆方法的复杂程度，我们将其分为三个级别：L1、L2和L3。

L1级别的混淆技术只有文本和视觉效果，影响可读性， 这些混淆技术包括随机空白插入、别名、随机大小写和无意义的反引号插入。反引号字符称为转义字符。L1混淆后的代码意图很容易理解，因为其保留了大部分信息。

L2级别的混淆技术将修改原始脚本的词法特征和 AST 层次结构，但它们仍然保留原始脚本的一些字符集信息。与字符串相关的混淆技术是常用的，例如字符串连接、重新排序、替换和反转。L2混淆后的代码虽然很难理解，但我们仍然可以从字符级别的信息中推断出代码的大致意图。

L3级别的混淆技术不仅改变了原始脚本的词汇特征和 AST 层次结构，而且还隐藏了原始脚本的字符集信息。该级别典型的混淆技术是各种编码方式，如Base64、ASCII等。经过 L3混淆的代码，我们不能直接从脚本的文本信息中推断出其原始意图。

**3. 混淆对恶意检测的影响**

混淆后的 PowerShell 脚本可以隐藏原始脚本的原意，轻松逃避杀毒软件的检测。目前的恶意脚本检测模型主要依赖于脚本的字符集特征或AST特征。这些特征完全可以通过混淆来改变，从而使目前的恶意脚本检测模型无法正确识别恶意脚本。

此外，如第2.2小节所示，混淆级别越高，我们就越难以理解脚本的原意。分析人员需要使用动态分析来推断这些混淆脚本的意图，效率低且代码覆盖率低。在奇安信网络安全公司的帮助下，我们收集了2021年1月1日至5月29日期间的1,127,349个PowerShell恶意样本，发现约98.78%的样本被混淆。而且很多样本中同时包含了L1、L2和L3级别的混淆技术。因此，反混淆对于恶意脚本的检测和分析非常重要。

03

**方法**

为了克服上述挑战，我们提出了一种基于 AST 的反混淆方法，该方法具有变量跟踪，Invoke-Deobfuscation。下图显示了Invoke-Deobfuscation的框架。Invoke-Deobfuscation的反混淆过程可以分为三个阶段：Token解析、基于AST的变量跟踪和还原、重命名和重排版。

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSXxibNrJvBtVbDeAh39FHQ4YFTYSJFI8vpNQASGHoP2oE2MVPvxjSc7s1KGWnAyqb79lp2MnBnJv2w/640?wx_fmt=png)

**图2: Invoke-Deobfuscation方案框架**

我们详细描述每个阶段如下。

**1.Token解析**

Token解析使用脚本的词法信息来还原混淆。大多数L1级别的混淆技术都与Token有关，所以我们可以通过Token解析来还原它们。我们基于Microsoft的官方库System.Management.Automation.PSParser 对PowerShell的脚本进行标记化。每个Token包含许多属性，如文本内容、起始偏移、长度等。我们利用Token的属性来还原原始Token并将它们组合起来形成反混淆脚本。图3显示了Token解析的简化过程。

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSXxibNrJvBtVbDeAh39FHQ4Yfz8gS3xqKjGhGiakEbnF2P62H8g3N984b7EJd0yGBCQICrIo9H8Zb1g/640?wx_fmt=png)

**图3: Token解析示例**

每个Token对应脚本中一个完整的词法单元，其属性可以帮助我们识别和还原对Token的混淆。例如，如果一个Token的类型是命令，它的内容是一个别名，比如图3中的命令IeX，我们将用它的全称Invoke-Expression替换它。基于这些属性，我们可以在Token级别处理其他混淆，例如随机大小写和重音符（脚本解析为Token时将去除无意义的反引号）。处理完一个混淆的Token后，我们将在脚本中将其替换为它的还原结果。逆序处理使得我们可以识别未处理的Token而不需要重新解析新产生的脚本。 最终，我们可以在Token级别获得没有混淆的脚本。

**2.基于AST的还原**

无论混淆后的脚本片段多么复杂，都是由原始脚本片段经过一系列变换得到的。混淆脚本片段一般包括混淆数据及其还原算法，我们称之为可还原脚本片段。反混淆的关键是在混淆脚本中识别这些可还原的片段。

（1）识别可还原的片段

我们使用 PowerShell AST 上特定类型节点的内容来识别可还原的脚本片段。首先，PowerShell脚本的AST各节点内容语法有效，包含可还原的脚本片段。其次，我们可以通过执行可还原的片段来获得原始片段。例如，'he'+'llo'可以执行得到'hello'。因此，我们对PowerShell AST中的所有节点类型进行分析，找出其内容在执行后往往能得到字符串形式结果的节点类型。我们称这些类型的节点为可还原节点，包括PipelineAst、UnaryExpressionAst、BinaryExpressionAst、ConvertExpressionAst、InvokeMemberExpressionAst和SubExpressionAst 。我们将可还原节点的内容提取为可还原片段。基于可还原节点，我们不仅可以识别已知的混淆技术，还可以识别相关的未知混淆技术。

（2） 基于调用的还原

我们通过Invoke函数执行可还原的脚本片段以获得它们的还原结果。首先，我们将可还原的脚本片段转换为脚本块。然后我们使用它的成员函数Invoke来执行它本身。

对于不同类型的执行结果，我们将它们转换为相应的字符串形式作为还原结果，以保留其语义。例如，假设执行结果的内容为123，类型为String，则还原结果为'123'。如果其类型为Number，则还原结果为123。当执行结果的类型不能用字符串形式表示时，如Object，我们保留可还原的脚本片段。

可还原的脚本片段可能包含与还原过程无关的命令，例如Restart-Computer、Start-Sleep等。因此，我们创建了这些命令的黑名单以加速反混淆。如果可还原片段包含这些不相关的命令，我们就不会执行它们。为了安全起见，我们的工具应该在一个隔离的沙箱中运行。

（3）变量追踪

由于缺少上下文，我们无法直接执行包含变量的可还原片段来获得正确的还原结果。为了克服这个挑战，我们使用符号表来记录脚本中出现的变量的范围和值。具体的伪代码 参见原文。

我们通过AST的结构记录了脚本中出现的每个变量的作用域。根据其可访问性，变量分为局部变量、全局变量和环境变量三种类型。顾名思义，我们只需要记录局部变量的作用域即可。我们后序遍历AST，记录下当前访问节点的作用域。只有在访问NamedblockAst， IfStatementAst，WhileStatementAst，ForStatementAst，ForEachStatementAst和StatementBlockAst六种节点时，当前节点作用域的深度将增加或减少。变化取决于遍历方向，从父节点到子节点或从子节点到父节点。

我们通过执行变量的赋值表达式将变量的值记录在符号表中。基于 AssignmentStatement 节点，我们可以识别变量及其赋值表达式。当赋值表达式包含符号表中没有的未知变量时，我们不执行该表达式并放弃记录赋值变量。此外，对于环境变量，我们可以使用命令Get-Variable来获取它们的正确值。

通过变量跟踪，我们可以正确获取包含变量的可还原脚本片段的还原结果。我们当前的变量跟踪实现仍有一些局限性，我们将在后续章节中详细讨论它们。

（4）Invoke-Expression 和 PowerShell

复杂的混淆脚本通常包含多层混淆，其典型特征是包含Invoke-Expression cmdlet或PowerShell。Invoke-Expression和PowerShell都可以将它们的字符串参数作为脚本运行。这意味着攻击者可以直接使用各种方法混淆脚本字符串。为了保持原始语义，他们只需要添加Invoke-Expression或PowerShell来调用混淆后的字符串。

处理多层混淆的关键是识别命令Invoke-Expression和PowerShell。然而，攻击者经常使用不同的方法来混淆这些命令。例如，混淆片段.($pshome[4]+$pshome[30]+'x'）等同于Invoke-Expression。我们使用变量追踪可以得到还原结果.('iex')，这是Invoke-Expression的常见格式之一。Iex是Invoke-Expression的别名。.可以调用字符串作为命令。Invoke-Expression的其他常见格式包括iex、'xxx' |iex和&'iex'。我们可以通过基于AST的还原以及变量跟踪来识别不同格式的Invoke-Expression。PowerShell可以使用参数-EncodedCommand执行Base64编码的命令。由于PowerShell的自动补全和大小写不敏感，该参数可以用于多种格式，如-e、-eNc等。我们将参数转换为小写并使用'-encodedcommand'.StartsWith($param)判断参数是否为-EncodedCommand。

针对多层混淆，我们将Invoke-Expression和PowerShell的字符串参数进行转换并反混淆。我们重复这个过程，直到脚本的还原结果不再变化。这样，我们就可以从经过多层混淆的脚本片段中得到原始脚本片段。

（5）脚本重构

我们基于 AST 的后序遍历重构反混淆脚本。当访问一个节点时，我们首先使用它的子节点的内容来更新它的内容。后序遍历确保在访问它时，它的所有子节点都已经处理完毕。如果其内容被混淆，我们将用其还原结果替换它。最终，当我们访问 AST 的根节点时，我们将获得整个反混淆脚本。我们将混淆后的脚本片段进行原地替换，以便反混淆脚本与混淆后的脚本语义一致。

假设一个脚本的内容是'a'+'b'+'c'，它的AST和重构过程如图4所示。当我们访问 'a'+'b' +'c' 的可还原节点时，我们用它的子节点的还原结果更新它的内容，并得到一个新的脚本片段 'ab' +'c' 。然后我们处理这块 'ab' +'c' 并用还原结果更新当前节点内容的记录。当我们访问 AST 的根节点时，我们将获得...