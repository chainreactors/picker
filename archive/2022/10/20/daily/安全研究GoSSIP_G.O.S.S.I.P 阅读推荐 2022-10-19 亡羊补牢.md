---
title: G.O.S.S.I.P 阅读推荐 2022-10-19 亡羊补牢
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247492961&idx=1&sn=1effd3e2c7e9989e1fd41f0be4dc28c7&chksm=c063cbb8f71442aeabc0aa65c6e3e86acbedd2d82529999b235f7254546c6ffca83535f662bc&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-10-20
fetch_date: 2025-10-03T20:23:45.049521
---

# G.O.S.S.I.P 阅读推荐 2022-10-19 亡羊补牢

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjx7tiaUEiaraRuWObSoDM3RyHXP3uKLP3BEKI0hibFTLL7ib8JiaJxNWCiaeNQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-10-19 亡羊补牢

原创

cascades

安全研究GoSSIP

什么样的特征能够代表一个漏洞？已有的基于代码相似性的漏洞分析工作，似乎并不能帮我们解释这个问题。今天我们推荐一篇由 KAIST 的 ProSysLab 发表在 CCS '22 上的工作 *Tracer: Signature-based Static Analysis for Detecting Recurring Vulnerabilities*，提出了一种基于污点分析的轨迹特征静态分析技术，用来寻找所谓的recurring vulnerability（反复出现的漏洞？）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjxtP0CWhdnauSIiczxUnPFPSNu0W4GHuYjx5V5uN1BJN3RkeM3cUicG4sQ/640?wx_fmt=png)

来自韩国的研究人员提出了这么一个问题：为什么有很多漏洞，成因都是一致的（例如都是integer overflow导致的越界访问），却一而再再而三地出现在软件代码中（小声地说，这时候确实应该去杀程序员祭天吧）。更为令人恼火的是，静态分析工具既然知道这种事情反复发生，那为什么做不到“前事不忘后事之师”？作者认为，当前主流静态分析方法对这一类重复出现的漏洞进行特性总结的时候，没有真正抓住漏洞的核心语义，而简单地依赖语法特征来生成所谓的“漏洞签名”，没法做到真正的广谱抗菌疗效好~

以下图为例，在2009年gimp中包含的一个典型的由整数溢出导致的实际分配内存过小，而最终导致缓冲区溢出的漏洞。相同模式的漏洞也在另两款软件中被发现（CVE-2017-16663 和 CVE-2017-16612，时间已经过去了8年，抗战都结束了）。仔细分析后面两个漏洞可以发现，即使是**相同模式的漏洞，在语法上往往有很大的区别**，单纯使用基于语法分析的相似性检测（例如基于clone detection）来发现漏洞，往往存在漏报。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjxolXD6e9mT0yMEWTZKrjLfh5LXNVdtViaB4DEmrNoe5utUO5GulyS84g/640?wx_fmt=png)

为了能够从语义层面去检测recurring vulnerability，作者在本文中设计了名为Tracer的分析系统，其工作流程如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjxkWtFs4Ribz8ZDicjSbGyZU2BFLnxkY8dfR8SCghbicUEBCoFWLAJelEkg/640?wx_fmt=png)

不论是已知的漏洞代码还是待分析的代码，Tracer 都会先**使用污点分析，提取出一种专门设计的特征向量**，并维护在特征数据库中。随后，Tracer 通过特征向量余弦相似性比对，判断出当前代码是否和曾经出现过的漏洞存在语义相似性，并更新特征数据库。特征向量提取的细节如下图所示。首先，需要根据历史漏洞信息 / 污点分析引擎，找到 source-sink 对，随后提取出对应的污点传播轨迹（可能有多条）。为了排除不相关的代码，Tracer 选择从数据依赖图（而不是控制流图）中提取轨迹。随后，Tracer 再为每条传播轨迹，在自定义的抽象域上生成对应的特征向量。从下图的实例可以看出来，（至少）在gimp和libXcursor上出现的两个相似的漏洞，其特征向量的相似度也很高。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjxyhoYvstxQVwdpfo5XGpXUBgicOh6ILN2ZgtjM1dgzH6ptWkHh9uvg8A/640?wx_fmt=png)

特征向量的定义和生成是 Tracer 的一大亮点。如下图所示，Tracer 的污点分析是建立在抽象域上的，每个变量的抽象值包含两个域：污点域（T）与值域（V）。在这样的抽象域上，Tracer 定义了一系列抽象语义，包括如何抽象 source-sink 点，如何将漏洞特征对应到具体数值（即上图所示的 0123）上等等。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjxIhEtesRAqATPFszYPZB3EEhzS9kBfPq77eltkIRetO0Msogr2wJXIw/640?wx_fmt=png)

Tracer 随后在抽象域上完成污点分析的后续流程，细节较多，故不在此赘述。最终，如下图所示，Tracer 得以形式化地描述如何报告一个污点分析的漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjxkRYWSOcbgHFIFVup5DgPDntVVYdHoialDlsEUR0c02mnCWZopg3Ib9Q/640?wx_fmt=png)

在抽象域的基础上，**Tracer 为污点分析支持的每类漏洞（包括整数溢出，缓冲区溢出，格式化字符串，命令注入）进行了实例化**。例如 Double-free 漏洞可以将两次 free 相同指针的函数调用看作是污点分析中的 source-sink 点。

Tracer 基于 Facebook 的开源静态分析框架 Infer 实现。实验部分，作者选取了 16 个 CVE，还对 Juliet 测试集和 OWASP 安全编码教程中的 5 个例子一起生成已知的漏洞特征。**随后从 Debian 软件包中选取了来自 16 个领域，共 273 个 C/C++ 软件包作为 Benchmark，并以 VUDDY，CCAligner，Devign 这三个工作作为对照。**

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjxg0sqUxhS81asicYqyIhrKmicqaMmF0uFicpbF8sxV0QsxPXlcvItqfbdA/640?wx_fmt=png)

如上表所示，**Tracer 共计在 67 个软件包中发现了 112 个新漏洞，对照组的三个工作仅能发现它们中的 10 个漏洞。**结合具体漏洞分析还可以发现，Tracer 不仅能根据历史漏洞特征找到新的漏洞，也能基于 Juliet 和 OWASP 这种人工合成的代码漏洞找到新漏洞。面向安全编码教程的程序分析，是不是新的思路打开了呢？

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjxY4S4dPbkBfFQmblAjsuDJNtWMbIW6da2icNKic5f1xhICYtNRicx7c7fw/640?wx_fmt=png)

此外，由于 Tracer 引入了自定义的程序高级特征（例如变量是否与常量进行了比较），从而可以避免如上图所示的两处误报。Tracer 与当前一些主流的分析工具的对比结果如下表所示。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjxmTdfS6JMZY8t1Wqgx4KuetSMsICia8Kib5EwCBPjQWXnr8ITG7XHvLZw/640?wx_fmt=png)

最后，作者对 Tracer 分析的时间和代码量也进行了统计。如下图所示，对于大部分程序来说，Tracer 的分析时间是可以接受的。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Fcdt1jNQSBJzy7jiciboVCjxaZibDgqvJFdCHHnPr3dKp7adZrHg7xtIxyE16ehI6Xv67ENa8ibp6Uicw/640?wx_fmt=png)

---

论文地址：https://prosys.kaist.ac.kr/publications/ccs22.pdf

论文Artifact：https://github.com/prosyslab/tracer

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