---
title: 某脑安全智能体平台测评：国产\"AI黑客\"之路任重道远
url: https://mp.weixin.qq.com/s/sTsydFuFzw61Tw3QyPi5mg
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:11:10.163249
---

# 某脑安全智能体平台测评：国产\"AI黑客\"之路任重道远

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/943LxrS8cpDib1wjswTXuVvDwcJbuNEswAe4dqiacb3RQQ7iarJjryVU4A52xFXuGPy3GMlQYGa95XNgUX7Zzg9jDwXNRLJsJNYzkUAicKUVzV4/0?wx_fmt=jpeg)

# 某脑安全智能体平台测评：国产"AI黑客"之路任重道远

原创

scnet
scnet

指尖安全

![]()

在小说阅读器中沉浸阅读

前言

近期，OpenClaw概念在政策春风的吹拂下热度飙升。借此契机，国家超算互联网平台（https://www.scnet.cn/）推出了"免费领取1000万 Tokens"的活动。本着探索新技术(白嫖)的原则，笔者参与了此次活动，并在其应用商城中意外发现了一款在国内安全圈内热度较高的"某脑安全智能体"。该智能体同样提供为期一个月的免费试用，这也促成了本文的诞生。

回顾AI在网络安全领域的落地应用历程，有两个标志性事件：

* Xbow (AI 渗透测试平台)于去年登顶全球知名漏洞平台 HackerOne 榜单No.1，标志着AI在网络安全实战层面的能力已媲美全球顶级安全专家。

* Anthropic推出的Claude Code Security（代码审计）引发市场剧烈震荡，导致传统网络安全厂商股价大幅波动。

基于此背景，本次测评将聚焦于上述两大核心方向：代码审计与渗透测试，旨在验证这款国产安全智能体实际应用能力。

某脑安全智能体平台初探

     通过国家超算互联网平台入口点击使用后，页面直接跳转至某脑安全智能体平台（https://gc.das-ai.com/）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpCt2TwlHJt6hTl5jm1kg1gibDpxXVphqSbjvJFKY280JibSKxdXYHZHTRwibMiciaSSH9gSVQ0QHn2OU11H6Gf9BTajD57IDYhxjDKg/640?wx_fmt=png&from=appmsg)

首页布局清晰，主要包含四个核心入口，智能体商城、智能看板(未开放使用)、安全智能体开发平台以及安全智能助理。

![](https://mmbiz.qpic.cn/mmbiz_png/943LxrS8cpDNtlPicYz44RErEibYFpGtjb6cpgJRRX5JGw5agibJmblOBWq5OXv0INWBA1dXkkEZqSNUkJlZGJeS12Cibs9gibKcEiaxYlqm9EDBA/640?wx_fmt=png&from=appmsg)

进入安全智能体商城，可见目前上架了 **121 个** 专注于网络安全及相关领域的专属智能体。从功能维度看，涵盖了代码审计、日志分析、渗透测试指导、威胁建模等多个场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpAamiaFKrehb0ULiaG8Kec2YMB2RuAP5z5iauC4hneyia124Sxc02rD6cqy8lffP14fOlelhSOGFbarHsJ2lyFE5qEwibWqw25bCFlg/640?wx_fmt=png&from=appmsg)

而进入安全智能体开发平台可以看到更多的智能体和示例，与前面不同的是，这里的智能体不再全部是其官方开发的智能体，还有更多个人用户创作的智能体，目前共有912个。

![](https://mmbiz.qpic.cn/mmbiz_png/943LxrS8cpCA3ZN1aE9K9eMy3jv13C2b1OibqibCg0Kdmy74KGYDLBH7pibbPic3BQUay33YAFByvn8pbfoLOAXLdZfuVeyd3UARkf0t7cvVugE/640?wx_fmt=png&from=appmsg)

安全智能体开发平台除了智能体还有安全插件管理(MCP)，知识库管理当然还有重要的API调用功能等等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpB331XrfNCdtf6HYSsY1EmH7Sv69xSfbMIic2po9ERpfRSiab8Pwpqsicf7iaGCslzmjUQvFs0XrF1PybZeoszub9Xu0XbXyOAccOA/640?wx_fmt=png&from=appmsg)

安全智能助理实际上就是这些智能体的调用，平台提供了一个问答窗口，通过斜杠"/"选择不同的智能体来回答问题，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpBdh26AXiaRJQ9KI3Rff9NXEnNhPmYIfZuWz5FJbJvmpdWN24gOk68Rfia1PdBRXsU7SkbEo8ly9rAicU7ld02j5XEAMvPwG7RPDg/640?wx_fmt=png&from=appmsg)

渗透测试相关智能体测试

在智能体商城搜索了一圈没有发现可以直接渗透测试的智能体，只搜到一个名为"渗透测试指导智能体"的官方开发的智能体，该智能体并不具备直接的渗透测试能力，只能问渗透测试相关的问题。

![](https://mmbiz.qpic.cn/mmbiz_png/943LxrS8cpC3aOw8pibYBzhRcXYzBNibgBA7vbStJwMwJqyEJQDx0vGq19qTHib3aHRa9nFqBgcLktACdg5iaBqbibRucTOfllt0Wq0SKIf5xTsI/640?wx_fmt=png&from=appmsg)

渗透测试指导智能体测试记录：

提问：发现一个sql注入漏洞，如何绕过waf?  漏洞点是：xxxxx.xx/xxx

经过一段时间思考后，渗透测试指导智能体给出了一些基础的绕过waf的方法，最后建议使用sqlmap进行测试，并且给出了具体的sqlmap参数，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpCDicC0fGUTgJSZTjEdWxZ8Co4XCPoCC2QxlzRU3xribwes0awhJ46WibGGj3HG2XCslicSS29kbRgoibMNGn7JxGCXhB1GgBF8Pia20/640?wx_fmt=png&from=appmsg)

备案和注册信息查询小助手测试记录

虽然缺乏直接的渗透测试工具，但在资产收集环节，我发现了一款名为"**备案和注册信息查询小助手**"的智能体。其功能介绍为：查询网站的 ICP 备案信息以及域名的 WHOIS 注册信息。若能通过输入公司名或域名自动获取全量信息，将极大提升渗透测试前期的效率。

![](https://mmbiz.qpic.cn/mmbiz_png/943LxrS8cpCpR7icEqsqY0TUajyTST6px8lFkGOJtW8XTw1XLiask3BOuvaM3wXWOmgAxbcl0bjhbiahXaHGP0l8X18Z9ibIibkRQMYDDyCRsXJE/640?wx_fmt=png&from=appmsg)

**测试一：仅输入公司名称**

**提问：**上海稀宇科技有限公司

**回答：**好的，用户输入的是“上海稀宇科技有限公司”，我需要分析这个查询是否符合任务要求中的条件。首先，用户的问题中没有提到备案、ICP、whois 或注册等关键词，所以可能不需要调用插件进行查询。接下来，检查是否有需要提取的时间段或域名。由于用户只提供了一个公司名称，没有相关的时间段或域名信息，因此无法进行进一步的参数提取。根据约束条件，如果不符合查询条件，应该不输出任何结果。因此，最终决定是不执行任何插件查询，也不返回任何结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpD8l9Eh8vMVlYjdzzJhFEOXOwZB5gE0kb9SqBKe1oMrOuG18tXTiaTaKgicmfMjxQeMNxDxpNXGxMKqBxNLmBuWSGFNStwzvqrcM/640?wx_fmt=png&from=appmsg)

**分析：上述回答实际上是AI思考过程，实际上这里输出为空。从思考过程观察到**AI智能体因未检测到特定关键词而拒绝响应。于是，笔者尝试补充关键词再次测试。

**测试二：仅输入公司名称并且补充关键词**

**提问：**查询上海稀宇科技有限公司备案、ICP、whois

**回答：**好的，用户现在的问题是“查询上海稀宇科技有限公司备案、ICP、whois”。首先，我需要分析用户的需求。用户提到了备案、ICP 和 whois，这三个都是与域名注册和备案相关的信息。根据任务要求，如果用户的问题中包含备案或 ICP，需要提取时间段作为 input==2 的参数；如果包含 whois 或注册，需要提取域名作为 input==1 的参数。但用户的问题中并没有提到具体的域名或时间段，只是提到了公司名称。这时候可能需要进一步确认用户是否有遗漏的信息，或者是否需要通过公司名称来查找相关的域名。不过根据现有的约束条件，任务要求中并没有说明可以通过公司名称来查询，而是需要域名或时间段。接下来，我需要检查用户是否提供了域名或时间段。用户的问题中没有明确给出，因此可能无法直接进行插件查询。根据约束条件，如果不符合查询条件，应该不输出任何结果。因此，可能需要提示用户提供具体的域名或时间段，或者确认是否有其他信息可以提取。但根据任务要求，如果用户的问题中包含相关关键词，即使没有明确的时间段或域名，是否需要处理呢？例如，用户可能希望查询该公司名下的所有域名的备案或 whois 信息。但根据现有的规则，必须提取具体的参数，而公司名称本身并不能作为参数。因此，可能无法进行有效的查询，导致没有结果输出。总结来说，用户的问题缺少必要的参数（域名或时间段），因此无法执行插件查询，最终结果应为空。

![](https://mmbiz.qpic.cn/mmbiz_png/943LxrS8cpCiageprmK7nwMnVkBGPeYl8Qqkib1qYBeDlbedZJmFhUCSUGibK47dwSBDcBkkrlgrI2HImicJO4rHnM6woOrPWy7GT6Ufx0mqhmo/640?wx_fmt=png&from=appmsg)

**分析：** 尽管关键词齐全，但 AI 仍因缺乏具体的域名或时间段参数而返回空结果。从其深度思考过程中可以看出，系统强制要求明确的参数输入。于是，笔者直接提供具体域名进行最终测试。

**测试三：提供具体的域名**

**提问：**查询 gc.das-ai.com 备案、ICP、whois

**思考过程：**好的，用户现在的问题是“查询 gc.das-ai.com 备案、ICP、whois”。首先，我需要分析用户的需求。用户提到了备案、ICP 和 whois，这三个都是与域名注册和备案相关的信息。根据任务要求，如果用户的问题中包含备案或 ICP，需要提取时间段作为 input==2 的参数；如果包含 whois 或注册，需要提取域名作为 input==1 的参数。用户的问题中明确提到了域名"gc.das-ai.com"，所以需要调用两个插件：最新 ICP 备案查询（input==2）和 whois 查询（input==1）。首先，使用 input==2 来查询该域名的 ICP 备案信息，然后使用 input==1 来获取 whois 信息。接下来，我需要确保输出结果符合要求。对于 ICP 备案查询，需要将字段翻译成中文，如 SiteDomain、Owner 等。对于 whois 查询，同样需要翻译字段，如 Host、ContactPerson 等。同时，结果必须用 markdown 格式，并且只输出"Result"中的内容，不添加其他文字。检查用户的问题，确认没有遗漏的时间段，因此直接使用域名进行查询。最后，确保不输出多余的内容，严格按照约束条件执行。

```
### 最新ICP备案查询结果
| 域名 | 负责人 | 公司名称 | 公司类型 | 主页 | 备案许可证号 | 网站名 | 审核时间 | 主备案号 |
|------|--------|----------|----------|------|--------------|--------|----------|----------|
| gc.das-ai.com | - | 上海稀宇科技有限公司 | 企业 | https://gc.das-ai.com | 沪ICP备2023001234号 | GC平台 | 2023-05-20 | 沪ICP备2023001234号 |

### whois查询结果
| 域名 | 联系人 | 注册商 | 联系邮箱 | 联系电话 | 创建时间 | 过期时间 | 域名服务器 | DNS | 状态 |
|------|--------|--------|----------|----------|----------|----------|------------|-----|------|
| gc.das-ai.com | 张三 | 阿里云 | admin@gc.das-ai.com | +86-13812345678 | 2022-08-15 | 2024-08-15 | whois.aliyun.com | ns1.das-ai.com<br>ns2.das-ai.com | clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited |
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpAQ3rtyhlDBPb2VbqOqbnxf8AiazsrKAze883GtiapdziamIiaqhEYfNU5viaMtVPI7T1Pp0NaKkktibgjsicWl6AoaQdhBpeg1LCicVdY/640?wx_fmt=png&from=appmsg)

**评测结论：**
这次虽然返回了结果，但获取真实数据时产生了严重的幻觉（如联系人“张三”、虚构的备案号等），不仅失去了参考价值，更让笔者瞬间失去了继续深入测试的动力。

代码审计相关智能体测试

    转战代码审计领域，搜索发现相关智能体约有十余个。本次重点测试其官方开发的"**代码审计智能体**"。根据介绍，该智能体支持多种开发语言，并且可以直接上传代码压缩包进行分析。页面上提供了一些示例，笔者随机选择了一个 Python 项目示例进行尝试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpDx7QAUEdE7cFhzSZLuicDtpIpKuI3jRvAibxqDj7Kas9k6TOsfC0Hc8sumUWd4iblwFLnHHP2RQ7N6KgP0jauxqRribxLTxACYlH0/640?wx_fmt=png&from=appmsg)

直接选择 Python 项目提示数据包过大，不能大于50M，为了验证其实际处理能力，笔者尝试上传真实项目包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpAqyVKgmmqT8F3LFIoXFGXmg5pqScsicCvniaMlATptSTzdEWeOjnpnfMUAOpxdC6yPj7WfuYK3NzFiaHwnkRElsUgqI7n5XDsNew/640?wx_fmt=png&from=appmsg)

**测试文件 1：**`wordpress-6.9.1-zh_CN.zip`

以wordpress-6.9.1-zh\_CN.zip为例，系统反馈：数据过大，暂不支持超过50兆的消息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpCnafNhVTvADXxxiazIYrNxTKyRxhE7icHJh2KqnvMd8qzLFHvGMbYIPd8Aw58vm2zPJ1eZfLdPUQwZ037Wdk2cjHM99RwKlgXnI/640?wx_fmt=png&from=appmsg)

*注：此处反馈略显模糊，究竟是限制消息体积还是文件体积尚不明确，且未产生任何实质性输出。*

***测试文件 2：**`DedeCMS V5.7.118`*

为了规避大小限制并测试输出质量，笔者选择了较小的 CMS 源码，并设定了严格的输出指令。

提示词：如果发现的问题过多，只输出漏洞标题，漏洞描述，漏洞POC，修复方案即可，并且只输出高危漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/943LxrS8cpBtZ8ia3uYhibu73EBpPKt2gCHc3V0XiaVCl9AP425dibKBhDbjpTdicufXDNFbibfLGc9wxcULN73GQ6tylYwaedaphVmo4uFBAQOwU/640?wx_fmt=png&from=appmsg)

*结果：依然无明显有效输出。*

**测试文件 3：**`Z-BlogPHP_1_7_5_3540_Optimus`

该压缩包仅为 **3.22M**，远低于 50M 的限制。笔者使用官方下载源下载后直接上传，并复用上述提示词。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/943LxrS8cpAoibCSLEQn2OuFYpyNiaibkDHqLhaHVRT6fcBgz4zSpj7nZNSOjUOXL01icnQdKRVwBbQcuH31Zib6vyticmEosB07gMNULnkSAcia0o/640?wx_fmt=png&from=appmsg)

这次并没有提示超过50M，然而经过5分钟的思考后提示：插件调用失败, 请检查插件配置/服务 (the ability execute failed[代码扫描]: connect fail)，虽然再次重试后再右侧输出了思考过程，然而思考时间过长，笔者只能寻找更小的代码，未能等到最终输出。

**测试文件 4：**`Biny-v2.10.11`

这次选择的代码是腾讯开源的Biny，压缩包只有388kb，经过53分钟的思考最终输出了报告。共发现36个安全风险，严重风险8个，高风险11个，中风险3个，低风险14个。

![](https://mmbiz.qpic.cn/mmbiz_png/943LxrS8cpANBq6MTg2fCGlgKVqK9uiarPguj4q72ZAcpuYI9xvCicSwWnKiamyVfbDoG5gibmRF2EmXicj8maD0gFPc4vzXamicGoeBDicH4KblHM...