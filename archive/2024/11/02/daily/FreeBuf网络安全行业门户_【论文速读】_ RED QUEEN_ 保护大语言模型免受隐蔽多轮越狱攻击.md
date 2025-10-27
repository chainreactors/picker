---
title: 【论文速读】| RED QUEEN: 保护大语言模型免受隐蔽多轮越狱攻击
url: https://www.freebuf.com/articles/network/414297.html
source: FreeBuf网络安全行业门户
date: 2024-11-02
fetch_date: 2025-10-06T19:16:58.458550
---

# 【论文速读】| RED QUEEN: 保护大语言模型免受隐蔽多轮越狱攻击

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

【论文速读】| RED QUEEN: 保护大语言模型免受隐蔽多轮越狱攻击

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

【论文速读】| RED QUEEN: 保护大语言模型免受隐蔽多轮越狱攻击

2024-11-01 17:30:29

所属地 北京

![](https://image.3001.net/images/20241101/1730453240_67249ef83b5236c1ded2b.jpg!small)

## **基本信息**

**原文标题：**RED QUEEN: Safeguarding Large Language Models against Concealed Multi-Turn Jailbreaking
**原文作者：**Yifan Jiang, Kriti Aggarwal, Tanmay Laud, Kashif Munir, Jay Pujara, Subhabrata Mukherjee
**作者单位：**Hippocratic AI，南加州大学信息科学研究所
**关键词：**RED QUEEN 攻击，多轮次越狱攻击，大语言模型（LLM），安全防护
**原文链接：**<https://arxiv.org/pdf/2409.17458v1>

**开源代码：**https://github.com/kriti-hippo/red\_queen

## **论文要点**

**论文简介：**本文提出了一种新的越狱攻击方法“RED QUEEN 攻击”，这种方法通过构建多轮次对话场景，将恶意意图隐蔽在看似为保护安全的请求之下。研究表明，现有的大语言模型（LLMs）在面对复杂的多轮次对话时，容易暴露出安全漏洞，尤其是恶意意图被巧妙伪装时。本文通过实验展示了 RED QUEEN 攻击的有效性，并揭示了在面对不同模型大小时，这种攻击的成功率差异。为了应对此类攻击，研究团队提出了名为“RED QUEEN GUARD”的防护策略，大大降低了攻击成功率，同时保持了模型的通用性能。
**研究目的：**随着大语言模型（LLM）在各个领域的广泛应用，它们的安全性问题变得愈加重要。尽管已有的越狱攻击方法大多基于单轮次对话且明确表达恶意意图，但这些方法并未完全反映现实世界的复杂性。在现实中，攻击者可能会通过多轮次对话逐步隐蔽其真实意图，使得模型难以检测并防护。本文的主要目标是提出一种能够隐蔽恶意意图的多轮次越狱攻击方法，并探索模型在此类攻击下的脆弱性。同时，研究团队还旨在设计一种简单有效的防护策略，帮助模型在面对此类攻击时保持安全。
**研究贡献：**
1. 提出了 RED QUEEN 攻击，这是首个构建多轮次场景并隐蔽恶意意图的越狱攻击方法，成功率较高。
2. 创建了一个包含56,000条多轮次攻击数据点的大规模数据集，涵盖14种有害类别和40种不同场景。
3. 对不同大小的四个代表性LLM模型家族进行了全面评估，并分析了不同轮次、场景和类别下攻击的有效性。
4. 提出了名为 RED QUEEN GUARD 的防护策略，通过对模型进行对抗性训练，使攻击成功率降至1%以下，同时保持模型在通用基准上的表现。

## **引言**

在大语言模型（LLM）的快速发展中，如何确保其安全性已成为关键问题。现有的越狱攻击大多依赖于单轮次的对话场景，通过明确表达恶意意图来诱导模型生成有害内容。然而，现实中的攻击者可能会采用更加隐蔽的方式，例如通过多轮次对话逐步暴露其恶意意图。

为了解决这一问题，本文提出了一种新的越狱攻击方法——RED QUEEN 攻击，该方法通过在多轮次对话中伪装善意请求，隐藏恶意意图，从而绕过模型的安全防护。本文还提出了一种防护策略 RED QUEEN GUARD，通过优化模型的防御能力，显著降低了攻击成功率。![](https://image.3001.net/images/20241101/1730453310_67249f3e7185666af5c6b.png!small)
目前的越狱攻击大多是通过精心设计的单轮次提示来引导模型产生有害内容，但这并不能完全反映真实世界中的复杂交互场景。例如，用户可能会通过多轮次的对话逐步暴露其恶意意图，而不是在对话开始时直接提出恶意请求。RED QUEEN 攻击通过多轮次对话场景的构建，能够有效隐蔽恶意意图，使得模型难以检测。

## **相关工作**

在 LLM 安全研究领域，红队测试（Red Teaming）是一种常见的安全评估方法，旨在通过模拟攻击者的视角，发现模型的潜在漏洞。现有的研究主要集中在单轮次越狱攻击上，设计各种提示来诱导模型产生有害内容。然而，这些攻击方法存在显著的局限性，因为它们无法捕捉到现实世界中的多轮次交互场景。为了解决这一问题，本文提出了 RED QUEEN 攻击，这是一种多轮次对话攻击方法，能够在伪装善意请求的同时隐藏恶意意图。

## **RED QUEEN攻击**

RED QUEEN 攻击通过在多轮次对话中隐藏恶意意图，诱导模型产生有害内容。攻击者通常会以“阻止他人进行有害行为”的名义提出请求，但实际上，他们是在寻求帮助完成恶意行动。通过这种方式，攻击者可以逐步获取模型的信任，并在对话后期引导模型生成详细的恶意计划。![](https://image.3001.net/images/20241101/1730453342_67249f5e0275e893aebd3.png!small)
RED QUEEN 攻击的关键在于多轮次的对话结构和恶意意图的隐蔽性。攻击者通过构建虚拟的多轮次对话场景，使得模型难以察觉恶意请求的真实目的。此外，研究表明，模型越大，越容易受到此类攻击的影响。实验结果显示，GPT-4 在此类攻击下的成功率高达87.62%。

## **实验设置**

在实验设置中，研究团队选用了四个代表性的大语言模型（LLM）家族的十个不同大小的模型进行评估，包括 GPT-4、Llama3、Qwen2 和 Mixtral，模型规模从 7B 到 405B 不等。实验主要测试了这些模型在面对 RED QUEEN 攻击时的表现。为了构建多轮次攻击场景，研究团队设计了 40 种不同的对话情境，涵盖了多个职业和关系背景，例如警察、律师、朋友和亲属等。在每个情境中，用户通过多轮次对话逐步隐藏恶意意图，诱导模型生成有害内容。![](https://image.3001.net/images/20241101/1730453359_67249f6f0b28fa6e37da3.png!small)
实验中，攻击数据集包含 56,000 条多轮次攻击数据点，涵盖 14 个有害类别，模型的响应被用来评估攻击成功率。同时，实验还通过不同轮次的对话结构（如单轮次、三轮次和五轮次）来分析多轮次结构对攻击成功率的影响。

## **实验结果**

实验结果表明，RED QUEEN 攻击在所有测试的大语言模型（LLM）上都表现出显著的有效性，尤其是在多轮次对话的隐蔽攻击场景中。GPT-4 的攻击成功率达到 87.62%，Llama3-70B 的成功率为 75.4%，显示出大模型在处理复杂对话时更容易受到攻击。这表明，模型规模越大，其推理和语言理解能力越强，反而更容易生成有害内容。![](https://image.3001.net/images/20241101/1730453369_67249f7968e248dc6090e.png!small)
实验还发现，随着对话轮次的增加，攻击成功率显著上升。例如，Llama3-70B 在五轮对话中的攻击成功率高达 77.11%，而在三轮对话中仅为 52.41%。此外，不同的攻击场景对成功率也有影响，职业背景（如警察、侦探）的场景中，模型更容易生成详细的恶意计划，而亲密关系场景（如朋友、亲属）下的攻击成功率相对较低。

## **防护策略**

为了解决 RED QUEEN 攻击带来的安全风险，研究团队提出了名为 RED QUEEN GUARD 的防护策略。该策略通过对抗性训练，使得模型能够更有效地识别并拒绝多轮次攻击中的恶意请求。在实验中，RED QUEEN GUARD 将攻击成功率降低到了1%以下，同时保持了模型在通用任务中的性能。

## **论文结论**

本文提出了一种全新的多轮次越狱攻击方法 RED QUEEN 攻击，揭示了当前主流大语言模型在面对隐蔽恶意请求时的脆弱性。通过实验验证，RED QUEEN 攻击在多个模型上表现出了较高的成功率，尤其是在大规模模型上更为明显。为了应对这一威胁，研究团队提出了 RED QUEEN GUARD 防护策略，大大降低了攻击成功率，为 LLM 的安全性提升提供了新的思路。
原作者：论文解读智能体校对：小椰风

# 网络安全技术

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

基本信息

论文要点

引言

相关工作

RED QUEEN攻击

实验设置

实验结果

防护策略

论文结论

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)