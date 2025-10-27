---
title: [AI安全论文] (37)CCS21 DeepAID：基于深度学习的异常检测（解释）
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501274&idx=1&sn=66f331dcd21faf0af18d06e3f0efd75a&chksm=cfcf7517f8b8fc01a40567b8eba774d42edbb3f9fbac3a602848850fc7388186c7e1d3e5aefe&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2025-01-29
fetch_date: 2025-10-06T20:09:20.922348
---

# [AI安全论文] (37)CCS21 DeepAID：基于深度学习的异常检测（解释）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDROvVWg43G0ibq13wddIGU6iaic5gQMyBbDkZTp0nUjzNc3EI1lMzic3JqPRDNd9icJkmqjibpXY6h1edQqg/0?wx_fmt=jpeg)

# [AI安全论文] (37)CCS21 DeepAID：基于深度学习的异常检测（解释）

原创

陈超帆

娜璋AI安全之家

> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koyCt0jxRGu7e9Yic09B3CmrBZ70xVJicDHicAK2icfWRXL561kJvJCY9zPw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

祝大家新春快乐，蛇年吉祥！

《娜璋带你读论文》系列主要是督促自己阅读优秀论文及听取学术讲座，并分享给大家，希望您喜欢。由于作者的英文水平和学术能力不高，需要不断提升，所以还请大家批评指正，非常欢迎大家给我留言评论，学术路上期待与您前行，加油。

该文是贵大0624团队论文学习笔记，分享者陈超帆同学，未来我们每周至少分享一篇论文笔记。前一篇博客介绍了Computers & Security2022的MPSAutodetect，提出基于堆叠去噪自编码器的恶意Powershell脚本检测模型。这篇文章将带来CCS’21清华大学的DeepAID，提出一种基于深度学习的异常检测模型，一个能够有效融合深度学习优势与可解释性机制，且具备良好适应性和扩展性的系统。本文将无监督模型的解释聚焦于寻找异常偏离正常数据的原因，使深度学习模型在安全领域的应用更具可解释性；并以 Distiller 用 FSM 整合专家知识与反馈，独特设计实现规则匹配、泛化及未知威胁检测，提升系统性能。由于我们还在不断成长和学习中，写得不好的地方还请海涵。希望这篇文章对您有所帮助，这些大佬真值得我们学习。fighting！

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROvVWg43G0ibq13wddIGU6iaicmvCUTp6AhUxFGICwf0XaWr2Z0gAbFEe2Nia7icXoyM2xLLvqglicxHjFQ/640?wx_fmt=png&from=appmsg)

```
原文作者：Dongqi Han, Zhiliang Wang, Wenqi Chen, et al. 原文标题：DeepAID: Interpreting and Improving Deep Learning-based Anomaly Detection in Security Applications 原文链接：https://dl.acm.org/doi/pdf/10.1145/3460120.3484589 发表会议：CCS 2021博客作者：贵大0624团队 陈超帆
```

**一.摘要**

无监督深度学习（DL）技术已被广泛应用于各种与安全相关的异常检测应用中，这是因为深度神经网络（DNN）具有检测不可预见威胁的巨大潜力和卓越性能。然而，由于缺乏可解释性，DL 模型在实践中的应用遇到了主要障碍。遗憾的是，现有的解释方法是针对有监督学习模型和/或非安全领域提出的，无法适应无监督 DL 模型，也无法满足安全领域的特殊要求。

本文提出了 DeepAID，这是一个通用框架，旨在解释安全领域中基于 DL 的异常检测系统，以及在解释的基础上提高这些系统的实用性。 文章首先为无监督 DNNs 提出了一种新颖的解释方法，即针对安全领域提出并解决具有特殊约束条件的精心设计的优化问题。然后，文章基于所提出的解释器和基于模型的扩展 Distiller 提供了几种应用，通过解决特定领域的问题来改进安全系统。文章将 DeepAID 应用于三类与安全相关的异常检测系统，并广泛评估了DeepAID的解释器与具有代表性的先前作品。实验结果表明，DeepAID 可以为无监督 DL 模型提供高质量的解释，同时满足安全领域的一些特殊要求。文章还提供了几个用例，说明 DeepAID 可以帮助安全操作员理解模型决策、诊断系统错误、向模型提供反馈并减少误报。

**二.引言及前置知识**

无监督深度学习（DL）技术已被广泛应用于各种与安全相关的异常检测应用中，这是因为深度神经网络（DNN）具有检测不可预见威胁的巨大潜力和卓越性能。然而，由于缺乏可解释性，DL 模型在实践中的应用遇到了主要障碍。遗憾的是，现有的解释方法是针对有监督学习模型和/或非安全领域提出的，无法适应无监督 DL 模型，也无法满足安全领域的特殊要求。

1.评估的安全系统

文章使用了三个安全系统Kitsune、DeepLog 和 GLGV来评估所提出的解释和改进方案。

* Kitsune使用的数据集主要来源于物联网（IoT）网络。这些数据集用于训练和评估基于表格数据的 Kitsune 系统在网络入侵检测方面的性能。地址：https://github.com/HuskyDG/magisk-files/releases
* DeepLog使用由 Hadoop 文件系统日志的关键数字序列组成的HDFS 数据集。通过对 HDFS 日志数据的分析，DeepLog 系统可以识别出不符合正常时间序列模式的异常情况，从而帮助检测和诊断文件系统中的问题。地址：https://github.com/Thijsvanede/DeepLog
* GLGV使用收集了真实内部计算机网络 58 天内的大量多源事件的 LANL - CMSCSE 数据集。GLGV 系统基于图数据，利用该数据集检测高级持续性威胁（APT）活动中的横向移动，通过构建认证图并分析图中的节点和边的关系来识别异常的认证行为。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROvVWg43G0ibq13wddIGU6iaic7X22a2MQXcOmib5JkGicVKIMfcr5ACMfztVQXRTychSMLtd6EuPnZoVQ/640?wx_fmt=png&from=appmsg)

代表性的深度学习解释器如下：

* 比较了多种代表性的深度学习解释器（包括 DeepAID）在支持无监督学习Support Unsupervised、不同数据类型、稳定性Stable、效率Efficient和鲁棒性Robust等方面的特性。可以看出DeepAID 在支持无监督学习、适应多种数据类型以及在稳定性、效率和鲁棒性方面都具有优势。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROvVWg43G0ibq13wddIGU6iaicgZMklicIs3gMvvkqib3xkmvlVfBicZicEiczylZ7xkW9B9x2HibBPfnJ686Q/640?wx_fmt=png&from=appmsg)

2.前置知识

（1）深度学习模型的可解释性问题

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROvVWg43G0ibq13wddIGU6iaicc5JNTZQZT3FEiaicf5cMb35nYsBcUEoMicHaRwPOibibJGQibQOuT5bUJGGw/640?wx_fmt=png&from=appmsg)

（2）为什么要用有限状态机(FSM)？

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROvVWg43G0ibq13wddIGU6iaiciblF1R4Y2Kv3FDlPWNtb34wiaPE5X0RzsvyR4cPFFOeV31DAHDIFHUGg/640?wx_fmt=png&from=appmsg)

异常检测系统现有工作：

* 基于重建的方法：利用深度学习模型（如自编码器 Autoencoder）对正常数据进行学习和重建，通过计算输入数据与重建数据之间的差异（如重建误差 RMSE）来检测异常。
* 基于分类的方法：将异常检测视为分类问题，通过训练分类模型来区分正常和异常数据。这些模型学习正常数据的特征和模式，将不符合这些模式的数据分类为异常。

现有工作的不足:

* 缺乏对异常的有效解释

  现有的深度学习异常检测方法大多仅关注检测精度，而忽略了解释能力，难以建立对系统决策的信任，也不利于根据异常情况采取针对性的措施。
* 不适用无监督学习

  现有针对深度学习模型的解释方法主要针对有监督学习模型和非安全领域，不适用于无监督深度学习模型在安全领域的应用。
* 模型可扩展性和适应性差

  许多现有模型在面对新的异常类型或数据分布变化时，难以快速适应和扩展。

因此，开发一个能够有效融合深度学习优势与可解释性机制，且具备良好适应性和扩展性的系统迫在眉睫。研究需求：

* 异常检测框架不仅能够准确检测异常，还能为检测结果提供有效的解释。
* 模型能够不断学习和更新，快速适应新出现的异常模式或数据分布的变化。

**三.本文框架**

本文设计的框架如下图所示：

* 左侧是原始数据（如网络流量、系统日志等）的来源，这些数据通常是非结构化的，无法直接输入深度学习模型。因此，需要经过预处理和特征工程，将其转换为适合模型处理的格式（如表格、时间序列或图结构），然后输入到基于深度学习的异常检测系统中。
* 右边部分突出了 DeepAID 的两个核心模块，即Interpreter和Distiller。Interpreter 专注于为无监督深度学习模型中的异常提供解释，通过特定的技术和算法，帮助安全从业者理解异常发生的原因；Distiller 则作为基于 Interpreter 解释结果的扩展，进一步将这些解释和专家反馈提炼为有限状态机（FSM）模型，以提高安全系统的实用性，使其更易于理解、调试和优化。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROvVWg43G0ibq13wddIGU6iaic2xYlDOXdhyK4osmQFUqib8KpBpZ7RPG58tXCSFRkgRbrg5HVIuqYjsw/640?wx_fmt=png&from=appmsg)

本文的研究目标及创新点：

* 设计解决安全系统决策理解、诊断调整、误报减少等问题。
* 数据类型针对性处理：针对表格、时间序列和图数据这三种不同的数据类型，分别设计了独特的解释方法。
* 提升系统可解释性与实用性：将无监督模型的解释聚焦于寻找异常偏离正常数据的原因使深度学习模型在安全领域的应用更具可解释性。
* 模型的可扩展性：以 Distiller 用 FSM 整合专家知识与反馈，独特设计实现规则匹配、泛化及未知威胁检测，提升系统性能。

**四.具体实现**

1.DeepAID 的工作流程

具体工作流程如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROvVWg43G0ibq13wddIGU6iaicibuypzNyAIjO0IkdfEic3gybfIDQwVj2QEM5ibysiakTWWyOibtYEGrUl8g/640?wx_fmt=png&from=appmsg)

（1）第一部分，该系统的数据输入。
基于深度学习的异常检测系统对输入数据（如网络流量、系统日志等）进行处理，将对应的异常数据输入到 DeepAID 的 Interpreter 模块。

（2）第二部分，基于 Interpreter 结果的决策与操作。
Interpreter模块根据数据类型（表格、时间序列或图）采用相应的基于无监督的模型解释方法（即对于给定的异常Xo，inter找到一个被视为正常的参考x\*，关注异常偏离正常数据的原因并给出解释），再将这些解释以一种直观且易于理解的方式呈现给安全操作员。

安全操作员根据 Interpreter 提供的解释来判断模型决策是否合理。如果解释合理且符合他们对系统行为的预期，那么他们可以初步建立对模型决策的信任。除了理解已知的异常情况，Interpreter 还可能揭示一些之前未被发现或未被明确理解的系统行为模式或异常特征，这有助于发现潜在的安全风险或新的攻击模式。当解释结果不合理或与预期不符时，安全操作员可以利用这些信息深入诊断系统中可能存在的错误。例如，可能发现特征提取过程中的问题、模型过拟合或欠拟合现象，或者是数据本身存在的偏差等。

（3）第三部分，Distiller模块更新规则。
如果 Interpreter 的解释被认为是合理的，安全操作员可以进一步将这些解释结果提供给专家进行审查。专家根据自己的专业知识和经验，对解释结果给出反馈，这些反馈可以是对异常类型的确认、对系统行为的新见解，或者是对模型改进的建议等。这些反馈信息被输入到 Distiller 模块中。

Distiller 再根据专家反馈，将其转化为系统可以理解和应用的规则，并更新系统的内部模型（如有限状态机 FSM 模型）。DeepAID 还可以通过 Distiller 来帮助减少误报。当系统检测到一个异常并被标记为可能的误报时，Distiller 可以根据之前积累的规则和反馈信息，对该异常进行进一步的分析和判断。如果根据现有知识可以确定该异常为误报，系统可以采取相应的措施，如调整检测阈值、优化模型参数或改进特征工程等，以减少类似误报的出现。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROvVWg43G0ibq13wddIGU6iaicAvRVfOrms6nkvv38nD8o9icDAYIy2EnDlNOmSiaVb8LgA8Kb4470icy7w/640?wx_fmt=png&from=appmsg)

2.Distiller工作流程

Deep AID 中的 Distiller 模型是由两个有限状态机构成。图 3 展示了 Distiller 模型的两个有限状态机如何协同实现对异常解释的建模以及根据专家反馈进行决策的过程。将解释向量(x°~ x )的每个维度的值范围划分为M个等长区间，这样总共会产生M×N个状态，其中N是特征维度数量。例如，如果有5个特征维度(N=5)，并且每个维度的值范围被划分为3个区间(M=3),那么第一个FSM就会有3×5=15个状态。

接着介绍这两个FSM分别对应的状态转移：

* 第一个 FSM 主要负责对异常解释进行建模，通过将异常解释映射到特定的状态序列，捕捉异常在不同特征维度上的特征模式。如果某个特征维度对异常判断的影响较大（即有效性高），那么它所对应的状态在转移过程中会更优先被考虑，而有效性较低的状态则在后续步骤中被涉及。也就是图3中的黑色箭头。
* 第二个 FSM 则专注于建立从异常解释到专家反馈的映射关系。一旦确定了异常解释在第一个FSM中的状态序列，就可以直接根据这个状态序列转移到对应的专家反馈状态，从而将异常解释与专家知识结合。
* 当第一个 FSM 确定了异常解释的状态序列后，第二个 FSM 根据这个状态序列直接转移到相应的专家反馈状态，从而实现将专家知识引入系统决策过程。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROvVWg43G0ibq13wddIGU6iaicXAtaicw1WHZfpwBSMibxCtWEfNlgxMBibWvbAugRGy94icwNICA4I2HsSg/640?wx_fmt=png&from=appmsg)

图4则是在实际的工作中，Distiller是如何根据专家反馈对规则进行迭代更新。过滤器Distiller根据专家反馈更新规则的流程如下：

* ①初始化阶段（Empty Distiller）：开始时，Distiller处于初始状态，没有任何已有的规则和反馈信息。
* ②更新规则（Update 1st rule）：当分析师遇到异常A1（例如IP扫描）时，首先通过DeepAID的解释器获取其解释（）。分析师根据自己的理解和经验将A1标记为“Scanning”，这就形成了一条新的规则（s1s2s3->r1）。③ 然后，Distiller根据这条规则更新其内部的两个有限状态机（FSM）的转移矩阵。在第一个FSM中，将与异常A1的解释向量对应的状态映射到新的反馈状态“Scanning”（r1），并更新相关的转移概率(按照重要性s1s2s3进行排序连接。由于此时s1s2s3仅仅被关联到Scanning攻击上，没有其他的可能性，所以概率都为1)。相同的在第二个FSM中，也相应地建立从到的转移关系。
* ③第一次测试异常（Test two anomalies）：接着对异常A1和A2进行测试。对于A1，其解释向量首先被映射到第一个FSM中的状态序列s1s2s3。然后，根据两个FSM中的转移概率，计算A1与各个反馈状态的匹配概率。在这个例子中，由于之前刚刚更新了规则，使得从s1s2s3到“Scanning”（）的转移概率很高，所以计算得出，这意味着Distiller非常确定A1属于“Scanning”类型的异常，与分析师的标记一致。对于A2，其解释向量映射到状态序列s4s5s3，计算得到概率为0.33，这表明A2与“Scanning”有一定的相似性，但匹配概率相对较低。这说明即使A2与A1不完全相同，但基于Distiller学习到的规则，它也能识别出A2可能具有类似的异常特征。
* ④第二次更新规则（Update 2nd rule）：分析师进一步分析A2，发现它实际上是“Port Scan”类型的异常，于是再次更新Distiller的规则，将A2的解释向量对应的状态s4s5s3映射到新的反馈状态“Port Scan”（r2），并更新两个FSM中的相应转移关系。
* ⑤第二次测试异常（Test two anomalies）：再次对A1和A2进行测试时，对于A1，映射到r1攻击的概率变成了0.83，因为s3同样可能出现在r2的特征序列中。而对于A2，现在计算映射到r2的攻击的概率变成了0.83，因为s3同样可能出现在r1的特征序列中。

**五.实验评估**

1.数据集

Kitsune

使用的数据集主要来源于物联网（IoT）网络。这些数据集用于训练和评估基于表格数据的 Kitsune 系统在网...