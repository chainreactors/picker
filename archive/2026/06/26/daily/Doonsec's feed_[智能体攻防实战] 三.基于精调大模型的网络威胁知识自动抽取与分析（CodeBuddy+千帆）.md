---
title: [智能体攻防实战] 三.基于精调大模型的网络威胁知识自动抽取与分析（CodeBuddy+千帆）
url: https://mp.weixin.qq.com/s/Iwd2oDZIaTfwRrtXmWxlzA
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:46:03.209525
---

# [智能体攻防实战] 三.基于精调大模型的网络威胁知识自动抽取与分析（CodeBuddy+千帆）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe2GBCiapqPM2aibB6DxHnEv98vVs0YQV0SB6Ch4uiaxk9VLWgcZuIu5PvvjVI2hDDlQo6Hc92WmIjNJfmrorWDj6vZIDicPsTxKNaU/0?wx_fmt=jpeg)

# [智能体攻防实战] 三.基于精调大模型的网络威胁知识自动抽取与分析（CodeBuddy+千帆）

原创

Eastmount
Eastmount

娜璋AI安全之家

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**为了更好地分享AI Agent在网络安全领域的实践方法与应用经验，作者正式开启“智能体攻防实战”专栏。本专栏将围绕“大模型如何赋能网络安全攻防实践”和“大模型及智能体内生安全”这两个主题展开，重点关注AI Agent、AI Coding、自动化分析、入侵检测、威胁情报、漏洞研判与安全运营等方向，尝试将大模型的语义理解、代码生成、工具调用和安全知识推理能力融入真实安全任务中。通过系列化案例，专栏希望降低网络安全实验、算法复现和工具开发的实践门槛，为安全研究人员、开发者和初学者提供更加直观、可操作的技术参考。基础文章，希望对您有帮助。感恩分享的第15年，fighting！**

随着网络攻击活动呈现组织化、持续化和复杂化趋势，安全公告、威胁情报报告、漏洞通报及攻击行为描述等数据快速增长。传统依赖人工阅读、规则匹配和手工标注的威胁情报分析方法，在处理效率、知识抽取一致性和复杂语义理解等方面面临明显局限。大语言模型凭借较强的语义理解、上下文推理和结构化生成能力，为网络威胁知识自动抽取与智能分析提供了新的技术路径。本文以CodeBuddy为开发与实验工具，结合百度千帆精调大模型，系统介绍基于大模型的网络威胁实体与关系自动抽取实践。

文章首先介绍智能体赋能网络威胁自动分析的整体思路。随后，详细说明百度千帆大模型的服务创建、SFT精调、LoRA训练配置、数据集上传、模型发布与API调用流程。在此基础上，借助CodeBuddy完成本地代码开发与调试，构建少样本提示上下文，并调用精调大模型从MITRE ATT&CK威胁描述中自动识别攻击组织、恶意软件、攻击工具和攻击技术等实体，抽取“使用”等语义关系，最终将结果以JSONL格式保存，为后续威胁知识图谱构建、攻击行为关联分析和安全实战研判提供结构化数据支撑。希望这篇文章对您有帮助，最后感谢学生睿杰在实验调试与内容整理过程中给予的帮助，共勉！

代码开源地址：

* https://github.com/eastmountyxz/Agent-for-security

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe19KhJMichz1fNsubES8qznc7T9ngwrEzVK150zlebHpQUZmIZpfPkNm67dLpgzNewo4InD4ny3RV8icpBq6bpTMIIQyxllUZ2Ns/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

### 文章目录

* 一.智能体赋能的网络威胁自动分析
* 二.百度千帆大模型调用与配置
* 三.基于大模型的网络威胁自动抽取
* 四.Codebuddy赋能知识图谱构建
* 五.总结与展望

###

**前文赏析：**

* [[智能体攻防实战] 一.大模型赋能网络入侵检测实战探索（CodeBuddy和d.run实现）](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247502909&idx=1&sn=efa7a5b44474921cb8788055d6f5a57a&scene=21#wechat_redirect)
* [[智能体攻防实战] 二.CodeBuddy赋能恶意代码分析与家族分类实践](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247502946&idx=1&sn=38d1088b04e7a97a9c3dd99134d1bcc5&scene=21#wechat_redirect)
* [智能体攻防实战] 三.基于精调大模型的网络威胁知识自动抽取与分析（CodeBuddy+千帆）

**传统安全专栏：**
![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1licntHY3QSNLt5bCicmSwickmMTElqQ8pAWkmQFMmMK2qp1gNQ9XK4bFNAo69RaREAL76e6oAmhTUsZ0GEoVDTgeP6u0GM9yRhM/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

---

# 一.智能体赋能的网络威胁自动分析

智能体赋能的网络威胁知识自动抽取与分析，旨在面向安全公告、威胁情报报告、漏洞通报、攻击日志及恶意代码分析结果等多源异构数据，构建集信息采集、语义理解、知识抽取、关联分析与辅助研判于一体的自动化处理机制。通过引入大语言模型、知识图谱、检索增强生成与工具调用能力，智能体可自主完成威胁实体识别、攻击关系抽取、技术战术映射、事件链重构及风险摘要生成，从非结构化数据中提取攻击组织、恶意软件、漏洞、基础设施、受害目标和攻击技战术等核心知识。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe0cMkSSJAd2iccgPiapduG3ibeibj3zZ8puFk3WNXm8kVoMQg37kAD4Twn4Wf9ibP2nic5p9LbMSRLzYiba2iagXuSFibdOJLLYGojpTRVc/640?wx_fmt=png&from=appmsg)

**(1) 多源网络威胁数据智能采集与预处理**
面向安全公告、漏洞通报、威胁情报报告、攻击日志、恶意代码分析结果、开源社区信息及安全厂商报告等多源异构数据，构建由智能体驱动的自动采集与预处理机制。智能体可根据预设任务目标，自主完成数据源发现、内容抓取、格式解析、文本清洗、去重归一和可信度初筛，并将非结构化、半结构化和结构化数据统一转换为标准化输入。该方向重点解决威胁数据来源分散、格式不统一、信息冗余和时效性不足等问题，为后续知识抽取与关联分析提供稳定的数据基础。

**(2) 网络威胁实体与关系自动抽取**
利用大语言模型、命名实体识别、关系抽取和提示工程等技术，从威胁文本中自动识别攻击组织、恶意软件、漏洞、攻击工具、基础设施、受害目标、攻击时间及攻击技战术等关键实体，并抽取“利用”“控制”“投递”“通信”“攻击”“归属”和“影响”等语义关系。智能体可根据不同情报类型动态选择抽取模板和分析策略，实现从长文本、复杂报告和跨段落描述中提取结构化威胁知识。该方向的核心目标是将原始安全文本转换为可计算、可关联和可验证的威胁知识单元。

**(3) 威胁知识规范化、对齐与融合**
针对不同来源中实体名称不一致、缩写混用、同名异义和重复描述等问题，构建威胁知识规范化与融合机制。智能体可结合上下文语义、规则库、历史知识图谱及外部安全知识库，对攻击组织、恶意软件、漏洞编号、域名、IP地址和攻击技术进行实体对齐与关系消歧，并对重复知识进行合并。通过引入MITRE ATT&CK、CVE、CAPEC等标准体系，可将抽取结果映射到统一的知识表示框架，形成具有一致语义和标准编码的网络威胁知识库。

**(4) 攻击链重构与技战术映射**
基于抽取后的实体、关系和时间信息，智能体进一步识别攻击活动之间的先后顺序、因果关系和阶段性特征，自动重构攻击链。通过将行为描述映射至MITRE ATT&CK中的战术、技术和子技术，可实现对初始访问、执行、持久化、权限提升、横向移动、数据窃取和命令控制等关键阶段的识别。该方向能够将零散的威胁线索组织为完整的攻击过程，为分析攻击路径、识别关键节点和判断攻击意图提供依据。

**(5) 威胁数据分析与实战辅助研判**
在结构化威胁知识基础上，智能体可进一步开展跨事件关联、相似攻击发现、攻击组织归属分析、基础设施聚类和威胁演化分析。通过综合时间、行为、工具、漏洞、网络资产和技战术特征，识别不同安全事件之间的潜在联系，并生成风险摘要、攻击画像和处置建议。该方向可直接服务于安全运营中心中的告警研判、威胁狩猎、攻击溯源、应急响应和防御策略制定，帮助分析人员快速从海量信息中定位高价值线索，提升复杂攻击事件的发现效率和响应能力。

---

# 二.百度千帆大模型调用与配置

下面利用百度千帆调用云端大模型实现威胁知识抽取，其具体过程如下所示：

**第一步，登录百度千帆（百度智能云），点击“立即体验”。**

* https://cloud.baidu.com/product-s/qianfan\_home

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe07ZZSCKAowgDTlF5auaHko8H3PgvAJyDhr5tv61EndciaxD4enP2MYIbuPu5BbYn8zkjtbh7WkaJfeQZeVqPN5Mz1SNTWSoiaTI/640?wx_fmt=png&from=appmsg)

**第二步，在模型广场中选择“模型服务”，点击“专属推理服务”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1GekwgUyTxicDibFQQe82shf383y3EsPib4jXeKrfYuluiaHqT4B7QpESyt9tUa4HSibd2FXGjmPhhOlmFBBRps2q97CqO4zVU52Po/640?wx_fmt=png&from=appmsg)

**第三步，在弹出的界面中选择“创建推理服务”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe20fIsrZWFONRKwBcA3nGt0WKc49guJywQYoLsibn0vdZeZUR8pYsYDN2ibnbNAicvxjNnyAGdNn2783h85ib8p8nQ61pKnTUC7ic98/640?wx_fmt=png&from=appmsg)

**第四步，在创建的专属推理服务中填写服务名称“Eastmount\_CTI”，然后选择模型。**

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0yrIoicJbnnBAic8SAXz7p93lmGJx0g33OELZMfAVW7cpY5W4KyPeaWMAqhxrwryV6rE3brzvZKjudFQDFaavuGgmuxZylUYOSk/640?wx_fmt=png&from=appmsg)

大家既可以选择预制的各类大模型，也可以在“我的模型”中选择自己精调的模型。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe0d6gAaibudsQH0R1GRlzgFwQ1ZSfIBUXaPtE1EJs2Gky9nU71SP53A4L29XQD7ZycPBtzRhR9V85z83Pcx2eVnmZvkVkNaa9TI/640?wx_fmt=png&from=appmsg)

**第五步，在“模型精调”中点击“创建精调作业”，接着配置精调大模型。**

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe3EjWyFiaEkIVibOWs92WajYjyR2jyyYFH4Whjoc6pTendNX3j4UfpDyyScS8JvEp3l3JfglrJ9SaZD7PrAh1HiaiaKcDLsacc1MicU/640?wx_fmt=png&from=appmsg)

**第六步，设置精调作业内容。** 大模型精调选项包括：

* 模型精调方式
* 基本信息：作业、基础模型、基础模型版本
* 训练配置：增量训练、训练方法（全量更新、LoRA）、参数配置
* 数据配置：数据来源、数据格式、选择数据集、混合训练、验证集
* 资源配置
* 发布模型

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2NuDFlO44FYiafyyKDunGvQ2FfCllVibdusTvktf13d7JMLqFqmHfIIMXTVljr1tofI5Y8icpmFNCg3ebaIgCrKMvG5c7mxGBwUU/640?wx_fmt=png&from=appmsg)

（1）当前选择SFT精调方式和Meta-Llama-3-8B模型

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe3G7B0icrXibLBh0kGNKpltqMHD3geeWiazM9sfA0OvWrkS2eZZKZsrOGM49TkfV4z5picMdjoGhvIjStxC75BIjWTNA6Fx9TaMPeA/640?wx_fmt=png&from=appmsg)

（2）设置训练配置参数

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe2ibXibOxUmqlIDvcL3dnJSc5as61kNrbhttG13FF4YLBiburwx3lib1LdgGncq8tnibmBy36ibmQmVXzic1PdA2iaoxrA4xibOAPIEM6YI/640?wx_fmt=png&from=appmsg)

（3）数据配置如下，需要选择本地数据集

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe1ocj4T3hDsNBof2hv3LdD1y1xYYR02KRTUlFbwZb8nQj2AtR1l1zFibBN6W90gZfF4IDgneibXtIWG1CqV2LAVm2AwOhfGKhde4/640?wx_fmt=png&from=appmsg)

本地数据集如下图所示：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1fasTZnumXHzVoMXIzONP7Zy9pEicJQVIOtxVvLm2NpSnIRa43YfTFr609QTFdS3RlZBvu333xQmSW6f1EnXzqFVFvmTOepkws/640?wx_fmt=png&from=appmsg)

数据集展示如下，网络威胁数据集，读者可以从Github下载或自行采集。

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2TmSwwqibicT4fTWmVqHB08wkgUQOMANv3QibCj8zxe6mqk34TtPzp1y3xcmD3RwaJMCibKSDjLLBVsE5B9AxWDkYCgbMPpiauE3rg/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe2gaagY7RltE3nZHXVwbiaVd4tNXvHb8lwvrlAZq3ib0Ns2dR377vEAW8icmcibLQLatzv5icRVEb5M7dX22zBQFjvLMjrGUSpMtDNA/640?wx_fmt=png&from=appmsg)

（4）资源配置后发布模型

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe231UiclZAbVE8Pl1Y9Tlq2LVsx9Zeibqq6iaibq6RZiczWiaHC26DN27SSgAq9pDda1rfdmcZmGyRHNfoctn2wCKHKoMz4VhHtUhvus/640?wx_fmt=png&from=appmsg)

> 温馨提示：介绍完模型精调和通用数据集构建之后，我们又回到专属推理服务任务，继续后续流程。

**（7）从“我的模型”中选择已配置好的微调模型**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1ibj48MEDsPWsuBJmjOg705ib4ef3geicaoj3N7ru7IS4HqCsDqDJKYMevolUcG3iczOTnPv1vawxw90dHSrM0lcbj974BoPFsXk0/640?wx_fmt=png&from=appmsg)

**（8）创建专属推理服务，API地址需要设计一个自定义关键词用来调用API，如“test”**

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0nh5A88wXlZjSRsDuO88hBqeBJRHZyTlic1kCGSwq4TDV9IPBagpZkdFsJg4yBiaCGAibicrHcPtePssxNfWlETpe7l17uiaARdc8Q/640?wx_fmt=png&from=appmsg)

选择定时释放并提交创建。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe18kMiappMYMDHMmkSDev3RibDfJSJ2FI9E7nJNCUkqQGIUIotlwXXChv60hqVwFSTzkYvibABhYNLHicibs0hiczlttVsfAMlcicG9ibk/640?wx_fmt=png&from=appmsg)

开通成功如下所示，自此，百度千帆微调大模型创建成功。

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0YSrpzbDExcDR7cQfzbyhn4FuefoZq1RRVFibcFsiaP6QGd8tGWBYdrowIIiaia6ulbja0QfxbO6blW01d5Lv8QoEOJoLDaZjlKxM/640?wx_fmt=png&from=appmsg)

---

# 三.基于大模型的网络威胁自动抽取

**第一步，点击上线刚创建的精调大模型。**

![在这里...