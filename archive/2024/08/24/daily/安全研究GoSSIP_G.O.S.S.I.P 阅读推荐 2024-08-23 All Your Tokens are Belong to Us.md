---
title: G.O.S.S.I.P 阅读推荐 2024-08-23 All Your Tokens are Belong to Us
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498719&idx=1&sn=18b75f41cf3a46e17cdd8d1c929cbad9&chksm=c063d506f7145c1074e58f19eb9376209fe4a9701b15a32eedf7eb12522cdf1a1cbb31bb1429&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-08-24
fetch_date: 2025-10-06T18:05:17.364324
---

# G.O.S.S.I.P 阅读推荐 2024-08-23 All Your Tokens are Belong to Us

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GltggnnXOFs7vspHsEMFcmrkGG9MbT9icWQVicQO6rxMKqCSbhKINbnA2P6KibmQCPOOExAw6TkRDUg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-08-23 All Your Tokens are Belong to Us

原创

石卡库

安全研究GoSSIP

今天我们要介绍的*All Your Tokens are Belong to Us: Demystifying Address Verification Vulnerabilities in Solidity Smart Contracts*是发表于USENIX Security 2024的论文。在这篇论文中，作者构建了一个基于字节码的检测工具`AVVerifier`，用来识别近几年智能合约中一种常见漏洞——*address verification vulnerability*，在此之前尚未有工具能够检测这一类漏洞。而这种漏洞允许攻击者操控合约状态，导致未经授权的操作和潜在的经济损失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GltggnnXOFs7vspHsEMFcm8ibs3xAAVBabzyKzVoaaPf18QKtwpiakM64NGXcW2UAMuPZEtyEQA7xA/640?wx_fmt=png&from=appmsg)

什么是address verification vulnerability漏洞呢，这要说到以太坊智能合约中基于白名单的地址验证。其实在以太坊中，使用白名单验证地址的合法性是一种常见的手段。目前被DeFi广泛应用的白名单验证方法主要有三种：

1. 硬编码对比，即要求传入地址和某个地址变量相等；
2. mapping验证，使用一个 *mapping* 结构来动态维护白名单地址的状态，例如`mapping(address => bool)`；
3. 硬编码地址枚举，即使用数组结构存储很多合法地址（可视为第一种的拓展）。

从字节码层面来看，这三种方法的表现都是相似的：首先合约会通过`CALLDATALOAD`加载一个地址，然后使用`JUMP I`进行判断，如果地址在白名单中，控制流则被定向到`fallthrough`，之后的流程会正常执行，否则`jumpdest`分支处理失败的`assertions`。

那为什么会出现address verification vulnerability漏洞？下面这个例子（Visor Finance开发的真实合约，在2021年12月21日被攻击）很好地展示了问题所在：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GltggnnXOFs7vspHsEMFcm4eicTNe1Jw86wVsYpiaq3ayF4NB9dAXMSH79gJkZdY2Fq4vC3e8anAnQ/640?wx_fmt=png&from=appmsg)

在函数`deposit`接受的三个参数中，有两个普通用户可控的地址类型的参数`from`和`to`，而从第16行的if条件判断开始的基本块中涉及到这两个参数，却没有做好检查，从而存在漏洞：攻击者通过事先部署一个攻击合约来调用漏洞合约中的deopsit函数，在执行到16行时，由于from参数是由攻击合约提供的，17行的检查可以通过，代码执行到18行再次调用了攻击合约里面的函数（delegatedTransferERC20），而这时候攻击合约可以让这个delegatedTransferERC20函数去再次调用漏洞合约的deposit函数，制造一个reentrancy，从而让漏洞合约中的第13行代码（计算shares）再次执行，从而让攻击者的收益翻倍。更具体的漏洞分析可以去看下面的文章：

> https://beosin.medium.com/two-vulnerabilities-in-one-function-the-analysis-of-visor-finance-exploit-a15735e2492

然而，这种漏洞却为什么没有被现实的智能合约漏洞分析检测工具发现呢？在反思已有的基于静态分析、符号执行和污点分析的工具存在的不足之处后，作者设计了`AVVerifier`：它基于静态 EVM 模拟的污点分析，通过对字节码的静态模拟来跟踪污点传播。它由三个组件组成：代码解析器、EVM模拟器和漏洞检测器。`AVVerifier`以智能合约的字节码作为输入，将其解析为控制流图（CFG），过滤出所有可疑函数作为候选，传递给模拟器。模拟器维护两种状态，一部分是EVM所需的数据结构，即堆栈、内存和存储；另一部分是收集到的污点信息。根据CFG，模拟器用操作码序列更新状态中的字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GltggnnXOFs7vspHsEMFcmcMic7suz2WoXQw8Vf50ibQGWuqs0mTmdsWyrseSEeRS0zJf3ucnj3pcA/640?wx_fmt=png&from=appmsg)

`AVVerifier`还采用基于启发式的路径选择方法来关注可能导致漏洞的路径。一旦完成对路径的分析，相应的状态就会发送到检测器。检测器中的三阶段检测策略根据漏洞特征排除误报和漏报，以确定当前合约是否存在address verification vulnerability漏洞。作者还在论文中详细的介绍了他们是如何启发式地构建污点分析时的路径，这些方法不仅有助于避免路径爆炸，还能降低工具的误报率。建议想深入学习的读者去阅读论文原文。

在实验环节中，为了验证`AVVerifier`的表现优于先前的工具，作者手动构建了含有20个真实案例的benchmark，和同类型的几个工具（Mythril、Ethainter、Jackal、ETHBMC）做对比。由于这些工具本身不具备检测address verification vulnerability的功能，作者还稍稍对它们进行了一点改造。从下图可以看出来`AVVerifier`无论是检测效率还是检测效果都优于其他工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GltggnnXOFs7vspHsEMFcmI929yve9GgiaGDTY9nPibbicoDPsRk362II6QCTUUrasWiadTUbP9qUuDQ/640?wx_fmt=png&from=appmsg)

更进一步，作者使用`AVVerifier`扫描了五百万个以太坊上的合约，标记了812个存在漏洞的合约。但是这里作者没有给出准确率的分析，而是做了个比较讨巧的比较，他们把`AVVerifier`和其他四个工具（作者基于Mythril、Ethainter、Jackal、ETHBMC的基础分析结果，为它们各自添加了address verification vulnerability检测功能）一起，拿来检测了这812个合约里面能找到源代码的369个合约，检测结果如下表所示。在召回率（recall，也就是表示检测工具的低漏报能力的指标）上，`AVVerifier`遥遥领先，同时在准确率（precision）上也有很好的保证，这说明`AVVerifier`在零漏报的基础上，基本上没有什么误报。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GltggnnXOFs7vspHsEMFcmiaBTZLhyLvuQLLJlffYotichJLPvNsq4tibkeKChAGOTNTN9OLIpbs74Q/640?wx_fmt=png&from=appmsg)

对于`AVVerifier`发现的348个确认存在漏洞的合约，作者勾勒了它们的部署时间图。从图中可以看到，漏洞合约数量随着时间越来越接近现在（2024年），每年出现的数量是不断增加的，这也从侧面反映出了以太坊的总体上升趋势，而中途的低谷与加密货币政策以及某些攻击事件有关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GltggnnXOFs7vspHsEMFcmHxuaJHbOjtN01r03RLfXVAfWujzNw15lycgLvzyQ2KCRRGuCSWR3zw/640?wx_fmt=png&from=appmsg)

最后，作者还把`AVVerifier`部署到BSC上，用于实时检测有没有可能真的捕捉到address verification vulnerability的现实攻击案例。2023年5月18日6时10分，工具检测到某个合约存在漏洞，在1.5小时后，果然有人发起了攻击交易，导致用户损失了3万美元。然而，由于缺乏自动漏洞响应机制，无法及时干预，作者只能眼睁睁地看着犯罪剧情发生而无法阻止（还不如自己先攻击算了）。

---

> 论文：https://www.usenix.org/system/files/usenixsecurity24-sun-tianle.pdf

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