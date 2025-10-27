---
title: 2024年软件工程顶会Fuzz论文汇总
url: https://mp.weixin.qq.com/s?__biz=MzU1NTEzODc3MQ==&mid=2247487052&idx=1&sn=663a33a0340c0fd6fc66a54b63f2ff0c&chksm=fbd9a5f0ccae2ce64195fa1c2711aeb967e3b91e3ce3dff1eb6aaea8dcc43e93a71b2691068e&scene=58&subscene=0#rd
source: FuzzWiki
date: 2025-02-27
fetch_date: 2025-10-06T20:39:48.914272
---

# 2024年软件工程顶会Fuzz论文汇总

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JchE46RGRlqTsQsWYHawwgpiaf77QOqAicOdWqIIictglicia5n86z7twOicsr2D1HLWANGZTib6VRsGpC9u1Zhviah4GQ/0?wx_fmt=jpeg)

# 2024年软件工程顶会Fuzz论文汇总

原创

FuzzWiki

FuzzWiki

![](https://mmbiz.qpic.cn/mmbiz_gif/JchE46RGRlrUZWms7eNLlib7QVhhIN811IVGU202DKZXWTTkNyjjDnLIWX8ma5yd6GGIsTElWPEwe9GtiasOXmGQ/640?wx_fmt=gif)

软件工程领域顶会也涌现了许多fuzz方面的论文，其论文的创新性，质量与技术覆盖面不次于安全领域顶会。小编将2024年软工领域顶会中与fuzz技术相关的论文统计出来以供大家查阅，此次汇总涉及ICSE, ASE, FSE, ISSTA, OOPSLA五项会议。小编还将此次分享的论文在研究方向上进行了分类，以供大家参考。

# **ICSE**

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811tVicJqX3mr1pDLbKnWwU3Gf9KRP8PvqKOtv8uFv9Iy2E9pNl6v6lk3g/640?wx_fmt=png)

**EDEFuzz: A Web API Fuzzer for Excessive Data Exposures**

## **![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)作者：**

**Lianglu Pan; Shaanan Cohney; Toby Murray; Van-Thuan Pham**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)作者机构：**

**The University of Melbourne, Melbourne, Australia;**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)所属方向：**

API模糊测试

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN8110CvWfWvZeuLge8r6xj4mic5Bok9eWprKeZID3XoVFwmjVviaf0LJ6Bgw/640?wx_fmt=png)

API经常向客户端应用程序传输比需要的更多数据，在Web应用程序中，通常是通过公共通道进行的。这一问题被称为过度数据暴露（Excessive Data Exposure，EDE），是2019年OWASP排名第三的重要API漏洞。然而，研究和工业界缺乏有效的自动化工具来发现和修复此类问题，这也不足为奇，因为这个问题没有明确的测试标准：该漏洞不会通过明显的异常行为（例如程序崩溃或内存访问违规）表现出来。在这项工作中，我们开发了一种形态变换关系来解决这一挑战，并构建了第一个模糊测试工具——我们称之为EDEFuzz——用于系统地检测EDE漏洞。EDEFuzz能显著减少在手动检查和临时文本匹配技术中出现的假阴性，这些方法是当前最常用的检测方式。我们在Alexa前200名中的69个适用目标上测试了EDEFuzz，发现了33,365个潜在的泄露，证明了我们工具的广泛适用性和可扩展性。在一个更为严格的实验中，我们对澳大利亚的八个流行网站进行了测试，EDEFuzz以98.65%的高真阳性率、最小的配置需求，展示了其准确性和高效性。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811tBCuu1eXOKCX67skCHmGSps0mibFbx89M4SAtOjygdE78CicXX3RkZdQ/640?wx_fmt=png)

ECFuzz: Effective Configuration Fuzzing for Large-Scale Systems

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)作者：**

**Junqiang Li; Senyi Li; Keyao Li; Falin Luo; Hongfang Yu; Shanshan Li; Xiang Li**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)作者机构：**

**University of Electronic Science and Technology of China, Chengdu, China;**

**National University of Defense Technology, Hunan, China;**

**National Key Laboratory of Science and Technology on Information System Security, Beijing, China;**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)所属方向：**

大规模系统模糊测试

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN8110CvWfWvZeuLge8r6xj4mic5Bok9eWprKeZID3XoVFwmjVviaf0LJ6Bgw/640?wx_fmt=png)

大规模系统由于其大量的配置参数，包含了巨大的配置空间。这导致在探索配置空间时，配置参数之间会产生组合爆炸。现有的配置测试技术首先通过模糊测试生成不同的配置参数，然后将这些配置参数直接注入待测试程序中，以查找由配置引发的bug。然而，这些方法并未充分考虑大规模系统的复杂性，导致测试效果较低。本文提出了ECFuzz，一个有效的配置模糊测试工具，专为大规模系统设计。我们的核心方法包括：（i）多维配置生成策略。ECFuzz根据不同的依赖关系设计不同的变异策略，并从候选配置参数中选择多个配置参数，来有效地生成配置参数；（ii）面向单元测试的配置验证策略。ECFuzz将单元测试引入配置测试技术，在执行系统测试之前过滤掉不太可能引发错误的配置参数，并有效地验证生成的配置参数。我们在包括HCommon、HDFS、HBase、ZooKeeper和Alluxio等现实世界的大规模系统中进行了广泛的实验。评估结果表明，ECFuzz在发现由配置引发的崩溃bug方面非常有效。与最先进的配置测试工具（如ConfTest、ConfErr和ConfDiagDetector）相比，ECFuzz在注入相同的1000个测试用例时，发现了60.3%-67%的更多意外故障，且效率提升了1.87到2.63倍。此外，ECFuzz还暴露了14个先前未知的bug，其中5个已被确认。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811skRyYkedXJMEUcRhlSty1WkUuzxg8ibojJp1icjNm7Nib4KwdhSIC3ckQ/640?wx_fmt=png)

FuzzSlice: Pruning False Positives in Static Analysis Warnings through Function-Level Fuzzing

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)作者：**

**Aniruddhan Murali; Noble Saji Mathews; Mahmoud Alfadel; Meiyappan Nagappan; Meng Xu**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)作者机构：**

**University of Waterloo, Waterloo, Canada**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)所属方向：**

模糊测试辅助静态分析

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN8110CvWfWvZeuLge8r6xj4mic5Bok9eWprKeZID3XoVFwmjVviaf0LJ6Bgw/640?wx_fmt=png)

手动确认静态分析报告是一个艰巨的任务。因为警告数量庞大，并且其中的假阳性比例很高。已经有模糊测试技术被提出，用于验证静态分析警告。然而，一个主要的限制是，对整个项目进行模糊测试以覆盖所有静态分析警告是不现实的。这可能需要几天甚至更多的机器时间来增加代码覆盖率。

因此，我们提出了FuzzSlice，这是一个新颖的框架，可以自动修剪静态分析警告中的可能假阳性。与以前的工作主要集中在确认静态分析警告中的真阳性（这不可避免地需要端到端的模糊测试）不同，FuzzSlice专注于排除潜在的假阳性，这些假阳性在静态分析报告中占了大多数。我们工作的关键见解是，如果在给定时间预算内，在函数级别进行模糊测试时没有产生崩溃，那么该警告可能是一个假阳性。为实现这一目标，FuzzSlice首先生成函数级别的可编译代码切片。然后，FuzzSlice对这些代码切片进行模糊测试，而不是对整个二进制文件进行模糊测试，从而修剪掉可能的假阳性。FuzzSlice也不太可能错误地将真实的bug归类为假阳性，因为崩溃输入也可以在函数级别通过模糊测试重现。我们在Juliet合成数据集和真实世界的复杂C项目（包括openssl、tmux和openssh-portable）上评估了FuzzSlice。我们的评估显示，Juliet数据集中的真值包含864个假阳性，而FuzzSlice成功检测出了所有这些假阳性。对于这些开源代码库，我们能够让其中两个库的开发者独立标注这些警告。FuzzSlice自动识别了这两个库中开发者确认的53个假阳性中的33个。这意味着，FuzzSlice可以在开源代码库中减少62.26%的假阳性，在Juliet数据集中则可以100%减少假阳性。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN8118XUE9SI33jsGZh0VtwPiaHYntlQIkvYh6TmZupLEia7ibVsVn1uXPibCEw/640?wx_fmt=png)

**SpecBCFuzz: Fuzzing LTL Solvers with Boundary Conditions**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)作者：**

**Luiz Carvalho; Renzo Degiovanni; Maxime Cordy; Nazareno Aguirre; Yves Le Traon; Mike Papadakis**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)作者机构：**

**SnT, University of Luxembourg, Luxembourg;**

**Universidad Nacional de Río Cuarto and CONICET, Argentina**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)所属方向：**

LTL模糊测试

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN8110CvWfWvZeuLge8r6xj4mic5Bok9eWprKeZID3XoVFwmjVviaf0LJ6Bgw/640?wx_fmt=png)

本文提出了SpecBCFuzz，一种针对LTL求解器的模糊测试方法，旨在通过边界条件（BCs）来发现LTL求解器中的bug。边界条件是那些其（不）可满足性依赖于稀有轨迹的极端情况。SpecBCFuzz实现了一种基于搜索的算法，在测试LTL公式时赋予边界条件更高的权重。它结合了语法和语义相似度度量，探索与边界条件相关的公式周围的领域。我们在21种不同的配置（包括最新和过去的版本）下，对四个成熟的、最先进的LTL求解器（NuSMV、Black、Aalta和PLTL）进行了评估，这些求解器实现了多种满足性算法。SpecBCFuzz生成了368,716个触发bug的公式，在我们研究的21种求解器配置中，发现了18种bug。总体而言，SpecBCFuzz揭示了：在Aalta和PLTL中的健壮性问题（求解器给出的错误答案）；在NuSMV、Black和Aalta中的崩溃问题（如段错误）；在NuSMV和Aalta中的不稳定行为（在相同公式下求解器的不同响应）；在Black、Aalta和PLTL中的性能问题（同一公式下求解器不同版本之间的性能大幅下降）；以及在所有版本的NuSMV BDD中没有发现bug，表明后者目前是最稳健的求解器。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811QxdhvzWfib0wic7MzhaiaPiavNqibDLRRSJJv1cbcgYF8PjHwDwfHXMeklA/640?wx_fmt=png)

**RPG: Rust Library Fuzzing with Pool-based Fuzz Target Generation and Generic Support**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)作者：**

**Zhiwu Xu; Bohao Wu; Cheng Wen; Bin Zhang; Shengchao Qin; Mengda He**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)作者机构：**

**CSSE, Shenzhen University, Shenzhen, China;**

**Guangzhou Institute of Technology, Xidian University, Guangzhou, China;**

**Fermat Labs, Huawei, Hong Kong, China**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN811jkmEPTzZbSeY4zKk0fyuFPkF6mK8j9cKQ6AJNguMXUoa89OiaMC2wkA/640?wx_fmt=png)所属方向：**

Rust库模糊测试

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrUZWms7eNLlib7QVhhIN8110CvWfWvZeuLge8r6xj4mic5Bok9eWprKeZID3XoVFwmjVviaf0LJ6Bgw/640?wx_fmt=png)

Rust库在Rust基础的软件开发中...