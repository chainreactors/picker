---
title: G.O.S.S.I.P 阅读推荐 2024-07-17 FITS
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498465&idx=1&sn=0450e2951212516dbeceebba94eb3f0e&chksm=c063d438f7145d2ed782250a3983b9a8ff7d766cc28452f18fb5bd9522cea17071b733808512&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-07-18
fetch_date: 2025-10-06T17:44:46.632611
---

# G.O.S.S.I.P 阅读推荐 2024-07-17 FITS

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21ELkB6RHe62WduEiaRolKNe4v3ZUE4u3SJypmC6U2aYBc3hLHd1iaUXeE8O8fPAyxd8qGfnBbVzRtRA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-07-17 FITS

原创

刘圃卓

安全研究GoSSIP

今天我们要为大家介绍来自ASPLOS 2023的论文*FITS: Inferring Intermediate Taint Sources for Effective Vulnerability Analysis of IoT Device Firmware*，论文介绍由第一作者刘圃卓亲自撰写~ 本文针对物联网固件提出了中间污点源（ITS）概念并设计ITS的推理方法，中间污点源可以缩短待分析路径从而降低固件污点分析的难度和开销，以发现更多固件中的安全漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ELkB6RHe62WduEiaRolKNe4dqvJD8lTG5wWiavYeNtDyJnq7ff7yf9woPsNuTCWpCnRHKDVWlAcFmQ/640?wx_fmt=png&from=appmsg)

---

## 研究背景

查找固件中的漏洞至关重要，因为任何固件漏洞都可能导致对物理物联网设备的网络攻击。静态污点分析是一种很有前途的技术，可用于查找嵌入式设备中的漏洞，例如 DTaint、Karonte 和 SaTc。它可以直接静态地应用于分析固件，实现高代码覆盖率，而无需模拟或分析真实的嵌入式设备。经典固件污点分析的工作流程包含三个主要步骤：

* 将接收用户数据的接口库函数（例如 recv、getenv、fgets）识别为污点源。
* 将可能导致缓冲区溢出或命令劫持的不安全库函数（例如 system、sprintf、strcpy）识别为汇聚点。
* 分析从污点源到汇聚点的数据流，并通过检查数据流上的污点数据是否未经清理就到达任何汇聚点来确定是否存在错误。

然而，即使使用最先进的技术，从污点源到汇聚点进行准确的数据流分析始终是应用固件污点分析的一个挑战性问题。原因是多方面的。

* 固件由多个二进制文件组成，用户输入（即污点源）经常跨二进制文件流动，这对于跟踪数据流来说是一个复杂的场景。例如，Web 服务器使用通用网关接口 (CGI) 调用其他二进制文件来处理用户请求。
* 即使在单个二进制文件中，数据别名、通过函数指针或跳转表的间接调用、剥离的调试信息等也进一步使数据流分析复杂化。
* 由于固件的多二进制性质和单个二进制文件的复杂性，从污点源到汇聚点的数据流可能过长，难以准确识别。过去，人们使用符号执行、值集分析和别名分析等技术在一定程度上缓解了这个问题。但代价是误报率和运行时开销增加，阻碍了在大型复杂的实际固件中进行污点分析的实用性。

为了提高污染数据流分析的有效性，我们不依赖于重量级技术，而是采取了不同的、新颖的视角：我们旨在缩短从污染源到汇聚点的数据流路径的长度，这可以显著降低现有数据流分析算法的分析问题的复杂性。为此，我们提出了中间污染源（ITS），以替代经典的污染源（CTS），后者是直接接收用户输入的接口库函数。ITS 是一个自定义函数（不是库函数），它处理通过库函数收到的用户输入并返回一部分输入供其他函数使用。如图1所示，ITS相比于CTS总是能缩短待分析路径长度。具体来说，ITS 的概念受到我们观察的启发：在连接互联网的物联网设备中处理用户输入的逻辑通常涉及三个步骤：

* 通过接口库函数接收结构化的用户输入，通常包含多个字段；
* 如果输入符合格式要求，则将用户输入保存到内存区域；
* 从内存区域获取一个或多个字段进行后续处理。

图2显示了 ITS 的一个例子。函数 fn16 根据索引获取由库函数接收并存储在 src\_addr 中的用户输入，然后将相应的数据返回给其他函数进行进一步处理。ITS 是从 CTS 到汇聚点的数据流上的一个节点；它到汇聚点的距离总是比到 CTS 的距离短，从而降低了污点分析数据流的复杂性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ELkB6RHe62WduEiaRolKNe4SNW5kgibFQIz4icLqElw8ibalhicTuMpuXglBGS7iad9Tgyv3v2iaOtIuoMw/640?wx_fmt=png&from=appmsg)

图1 recv 和 sprintf 之间的危险数据函数调用图示例

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ELkB6RHe62WduEiaRolKNe4m129hEzVWnVJAoTEFgGuicEpvQhUSdzADCqeQeDgDXxp432qjl6jk5w/640?wx_fmt=png&from=appmsg)

图2 中间污点源fn16 示例

---

然而，确定剥离固件中的函数 Fn 是否可以归类为 ITS 并非易事。首先，ITS 没有像 CTS 那样的明确检测标准，并且具有多种实现，尤其是在不同设备供应商的固件中。其次，找到 ITS 不仅需要对 Fn 进行逆向工程以建模 Fn 的语义（即行为），还需要对其他函数进行逆向工程以了解 Fn 与其他函数之间的过程间数据和控制依赖关系。第三，固件通常剥离了调试信息和符号表，导致语义信息（例如变量和函数的名称）丢失，进一步加剧了理解 Fn 行为的技术难度。最后，通常不可能应用动态分析来查找 ITS，因为供应商对设备的保护措施（例如隐藏的调试接口和固件与硬件之间的非公共内存映射）使得很难获得表征 Fn 行为的运行时信息。

我们利用上述关于互联网连接的物联网设备如何处理用户输入的观察结果来推断 ITS。我们的见解是，ITS 函数应该读取内存以获取数据，从获取的数据中获取新数据，并通过返回值或指针返回新数据。因此，ITS 的行为类似于内存操作函数。考虑到有各种操作内存的标准库函数，例如 strncpy、memcmp 和 strstr，我们将这些函数的实现视为锚点，并分析锚点函数和自定义函数之间的相似性以识别 ITS。请注意，我们的目标是衡量锚点和自定义函数在行为方面的相似性，而不是代码本身；因此我们的工作不同于现有的测量二进制代码相似性的技术。此外，由于从嵌入式设备获取运行时信息的难度以及动态分析的低覆盖率问题，我们应用静态分析来提取结构和流特征来描述函数的静态和动态属性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ELkB6RHe62WduEiaRolKNe4b9DD6NibQA0xHnuPb0YPWnHYQgDiccN3SKJ23RiaUuzRmtxvlv3c54mNQ/640?wx_fmt=png&from=appmsg)

图3 锚函数示例

---

## 思路概述

为此，本文提出了 FITS 来自动推断 ITS。具体来说，FITS 用一种新颖的行为特征表示来表示每个函数，该表示可以捕获函数的静态和动态属性，并通过行为聚类和相似性评分将自定义函数评为污点源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ELkB6RHe62WduEiaRolKNe4G636MoOObUG8LSnjuQB7zRg98M7skxHcE8nL3GX02pAzb01Jj30h1A/640?wx_fmt=png&from=appmsg)

图4 FITS工作流程

---

1.预处理阶段：此阶段对固件进行解包，获取二进制文件，并选取包含网络接口的二进制文件作为分析目标，因为网络通信是物联网设备的主要网络威胁来源。然后，找到所选二进制文件所依赖的所有库。同时，通过标准库函数名将具有内存操作行为的库函数标识为锚函数。最后，将所选二进制文件和依赖库转换为中间语言（IR），以方便后续分析。

2.函数行为表示：为了推断 ITS，我们需要分析每个自定义函数和锚定函数的行为特征。为此，此阶段构建一个特征向量来表示函数的行为。但是，由于缺少语义信息，并且目前还没有相关工作，因此为剥离的二进制文件构建函数行为表示具有挑战性。为了应对这一挑战，我们设计了一种新的函数特征表示，称为行为特征向量 (BFV)。BFV 包括两类特征：

* 结构特征 (SF) 表示函数的静态属性，例如基本块的数量、循环的存在。
* 流特征 (FF) 表示函数的动态属性，例如函数参数是否控制循环或分支。

表 1 列出了 FITS 中使用的特征的详细信息。为了计算这些特征，我们利用欠约束符号执行 (UCSE) 技术为每个函数生成控制流图 (CFG) 和调用图 (CG)。首先，我们对被分析函数（Fn）的 CFG 和 CG 进行图分析，以提取结构特征。其次，我们将到达定义数据流分析应用于 Fn 的 CFG，以了解 Fn 的参数如何影响其分支或循环，从而提取过程内流特征。第三，对于过程间流特征，我们分析对 Fn 的函数调用，并通过内存结构回溯以找到参数的来源。自定义函数和锚函数的 BFV 构成行为表示（BR），以供进一步分析。

3.污点源推理：此阶段对自定义函数和锚定函数之间的行为相似性进行评分，以推断 ITS。然而，直接对自定义函数进行评分可能会导致假阳性，因为特征维度的数量级差异。为此，我们首先对所有自定义函数进行聚类分析，并根据类别的统计特征筛选候选自定义函数。这样，一些可能导致假阳性的函数被丢弃。最后，用锚定函数对每个 ITS 候选函数进行评分，以推断 ITS。

> 表1 特征组成
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ELkB6RHe62WduEiaRolKNe4ib8X8gQTianGDAgDXK3ZUnuQmxXKS9m3BRZn29M5F9lYcEyuJSb6nG2A/640?wx_fmt=png&from=appmsg)

## 实验效果

我们对来自 5 家流行供应商的 59 个实际固件进行了 FITS 评估。结果表明，FITS 在每个固件中成功发现了至少一个 ITS，前 3 个精度为 89%。为了说明 ITS 有利于发现漏洞，我们将 ITS 添加到最先进的污点分析引擎 Karonte 中。与 Karonte 相比，在 ITS 的帮助下多发现了 15 个以的漏洞。此外，由于符号执行技术限制了 Karonte 的分析效率，我们实现了一个静态污点分析引擎。ITS 帮助静态引擎多发现了 339 个漏洞。在新版本固件中发现的 141 个漏洞中，有 67 个已经得到供应商的确认，其中 21 个已获得 CVE ID，这些漏洞的严重程度评定为较高（CVSS 评分大于 7.2），允许黑客对设备发起拒绝服务和远程代码执行等远程攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ELkB6RHe62WduEiaRolKNe40wkVbFgRNX8E7p2icX53GaUvP10odz3g7qgLJQmyaz0nLq51Ufj3N9g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ELkB6RHe62WduEiaRolKNe41mvHMju1yAXamQEwTje4WtU4A7XLIcUlIicg6AnaCq9hMia9CpUFumHg/640?wx_fmt=png&from=appmsg)

Case Study：为了说明推断的 ITS 在实际固件污点分析中的优势，我们以 CVE-2022-20825 为例。该漏洞使多个设备面临远程未经授权的任意代码执行攻击的风险，CVSS 评分为 9.8，由于其严重性已被媒体报道 。在对固件进行逆向分析和动态调试后，我们将库函数BIO\_read 确定为危险数据的来源。从 BIO\_read 到达汇聚点（strncpy）至少需要 11 个自定义函数调用和 50 多个库函数调用。在实际数据流分析中，这更为复杂，因为需要搜索更大的代码路径，并且分析还涉及别名分析和至少三个间接调用。虽然值集分析 和符号执行可以缓解这些问题，但它们可能会引入许多假阴性和显着的分析开销。例如，在不限制分析时间的情况下，Karonte 只能在 24 小时后分析深度为 4 的函数调用，而且内存和路径爆炸的问题使得继续分析变得十分困难。而使用 ITS 0x1d210 作为分析起点，只需要 2 个函数调用即可到达汇聚点，大大降低了数据流分析的开销和难度。

## 作者介绍

> 刘圃卓，2024年7月于中国科学院信息工程研究所取得博士学位，导师为孙利民研究员，主要研究方向为二进制程序分析与测试，目前就职于蚂蚁科技集团。

PS：滑铁卢大学 Chengnian Sun 教授（ https://cs.uwaterloo.ca/~cnsun/ ）招收博士生，对软件工程和编程语言感兴趣并有计划出国读博的同学请积极联系。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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