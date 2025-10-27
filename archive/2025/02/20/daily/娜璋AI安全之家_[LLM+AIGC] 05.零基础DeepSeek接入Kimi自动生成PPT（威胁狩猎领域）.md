---
title: [LLM+AIGC] 05.零基础DeepSeek接入Kimi自动生成PPT（威胁狩猎领域）
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501520&idx=1&sn=3341862984ccc75b3c729583c99086bc&chksm=cfcf761df8b8ff0b82c8a22b5a2707d5104e6da924efcd63aad588728f13a973a91954e24b2a&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2025-02-20
fetch_date: 2025-10-06T20:36:44.014123
---

# [LLM+AIGC] 05.零基础DeepSeek接入Kimi自动生成PPT（威胁狩猎领域）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUoMbh5vqTfpdxFV6apsYBp3MqM5ap305EAB0zrjnfxogMwfujZBJEB4Q/0?wx_fmt=jpeg)

# [LLM+AIGC] 05.零基础DeepSeek接入Kimi自动生成PPT（威胁狩猎领域）

原创

Eastmount

娜璋AI安全之家

> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![图片](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9RujXz10hUiaqGBEeGK2ibe0KUfwu5rBYEAnluHZ0cAKLqASZvicFRJJ3Mw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

近年来，人工智能技术火热发展，尤其随着ChatGPT和DeepSeek被提出，其能够基于在预训练阶段所见的模式、统计规律和知识来生成回答，还能根据聊天的上下文进行互动，真正像人类一样来聊天交流以及完成复杂的NLP任务。基于此，为更好地学习前沿AI知识，了解LLM和AIGC应用实战，本人开启了《LLM+AIGC》专栏，一方面作为在线笔记记录和分享自己的学习过程，另一方面期望帮助更多初学者以及对LLM感兴趣的同学。知识无价人有情，希望我们都能在人生路上开心快乐、共同成长。

该系列主要涵盖三方面：

* **原理篇**——以原理介绍和论文阅读为主
* **实战篇**——以编程构建自制LLM和RAG为主
* **应用篇**——以应用实践和Prompt探索为主

前一篇文章带领大家了解如何在WPS中接入DeepSeek，并实现智能办公，包括Word和Excel，方便我们编辑各种文案和处理表格。这篇文章将分享如何利用DeepSeek+Kimi自动生成PPT，以威胁情报为例进行探索，生成的效果真心不错。基础性文章，希望对初学者有所帮助！且看且珍惜，加油 O(∩\_∩)O

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPiajFNxJ8BvPfDR9ZAn5Jxg9IyCgTcbCiaoVHYBylibl3kSf6TDbEwezTnM9RWXy2hEtgckGDZzHFDA/640?wx_fmt=png&from=appmsg)

文章目录：

* **一.DeepSeek生成文案**
* **二.Kimi制作PPT**
* **三.总结**

前文赏析：

* [[LLM+AIGC] 01.应用篇之中文ChatGPT初探及利用ChatGPT润色论文对比浅析](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247498715&idx=1&sn=25d1d966ac5dbfdf80cf7e06df977305&scene=21#wechat_redirect)
* [[LLM+AIGC] 02.零基础DeepSeek入门初探及云端搭建详解（ChatGPT对比）](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501379&idx=1&sn=57bd5ed7fef46854c0205d9afabc2479&scene=21#wechat_redirect)
* [[LLM+AIGC] 03.零基础DeepSeek云端（硅基流动、腾讯云、国家超算平台）搭建及API接入](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501451&idx=1&sn=c16c0d24477f33768dbbfe3732a473d3&scene=21#wechat_redirect)
* [[LLM+AIGC] 04.零基础DeepSeek接入WPS实现智能办公](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501493&idx=1&sn=1fc9b744b393a1fc45a2c700d0fef83b&scene=21#wechat_redirect)
* [LLM+AIGC] 05.零基础DeepSeek接入Kimi自动生成PPT（威胁狩猎领域）

---

# 一.DeepSeek生成文案

前文已经讲述过DeepSeek基础操作知识，本文直接利用它实现具体功能。

**第一步，打开DeepSeek并输入如下所示的提示词。**

> 提示词：
> 请您帮我撰写一份关于结合ATT&CK框架的威胁狩猎的PPT，要求结合攻击链给进行总结，包括能给网络安全小白科普，请您使用Markdown的形式输出PPT的内容。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUoZ4hU7GEiatvQCELz8SZbrAvKnItdumOq2UqcP4u0s3SJctId27nO2tQ/640?wx_fmt=png&from=appmsg)

**第二步，复制生成的内容，其结合ATT&CK框架开展威胁狩猎普及。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUoQMSibBHxwGA2wfTMiaHLA6icibcOCfBiahDibyTGl77EkdibEofHjxxc43NQQ/640?wx_fmt=png&from=appmsg)

生成结果如下图所示，Markdown格式。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUoLvdMSVKLHy0MFLdJXyJib14GSk4updYq49FIyyVKp1dpXlecgKzaj2g/640?wx_fmt=png&from=appmsg)

内容如下，其为PPT的大纲，可以看到生成内容包括了6个部分。

```
# 威胁狩猎与ATT&CK框架：从攻击链视角看网络安全

---

## 目录
1.**什么是ATT&CK框架？**
2.**威胁狩猎的核心目标**
3.**攻击链（Kill Chain）与ATT&CK的关联**
4.**ATT&CK如何赋能威胁狩猎？**
5.**实战案例：钓鱼攻击的狩猎分析**
6.**总结与行动建议**

---

## 1. 什么是ATT&CK框架？
-**MITRE ATT&CK**：对抗战术、技术和常识知识库（Adversarial Tactics, Techniques,and Common Knowledge）
-**核心作用**：标准化描述攻击者行为，覆盖攻击全生命周期。
-**关键结构**：
-**战术（Tactics）**：攻击目标（如“初始访问”“权限提升”）
-**技术（Techniques）**：具体实现方式（如“钓鱼附件”）
-**子技术（Sub-Techniques）**：更细分的操作步骤

---

## 2. 威胁狩猎的核心目标
-**主动防御**：不依赖告警，主动寻找潜伏威胁。
-**关键问题**：
- 攻击者是否已入侵？
- 他们用了哪些技术？
- 如何快速阻断？
-**与传统防御的区别**：
- 防火墙/IDS：基于已知规则
- 威胁狩猎：基于假设和异常行为分析

---

## 3. 攻击链与ATT&CK的关联
### **传统攻击链（Kill Chain）**
1. 侦查 → 武器化 → 投递 → 漏洞利用 → 安装 → 控制 → 行动
### **ATT&CK的战术阶段**
- 初始访问 → 执行 → 持久化 → 横向移动 → 数据窃取...
### **两者结合的意义**
- ATT&CK将攻击链拆解为**具体可检测的技术**，帮助狩猎者定位关键环节。

---

## 4. ATT&CK如何赋能威胁狩猎？
### **四步循环法**
1.**假设驱动**：基于ATT&CK技术提出假设（例如：“攻击者可能通过钓鱼邮件投递恶意文档”）
2.**数据收集**：关联日志（邮件日志、进程创建日志）
3.**分析验证**：搜索T1566（钓鱼附件）相关行为模式
4.**改进防御**：更新检测规则或修复漏洞

---

## 5. 实战案例：钓鱼攻击的狩猎分析
### **攻击链阶段**
-**初始访问**：钓鱼邮件（T1566）
-**执行**：诱导用户启用宏（T1059）
### **狩猎步骤**
1. 筛选异常邮件附件（.docm、.js）
2. 分析宏代码与子进程行为
3. 关联C2服务器通信日志
### **结果**
- 发现潜伏的Emotet木马，阻断横向移动

---

## 6. 总结与行动建议
### **ATT&CK的价值**
- 提供**通用语言**：统一安全团队沟通
- 实现**系统化狩猎**：从碎片化告警到完整攻击故事
### **给新手的建议**
1. 学习ATT&CK矩阵（https://attack.mitre.org/）
2. 从高风险技术（如T1059、T1078）入手
3. 利用开源工具（如Atomic Red Team模拟攻击）

---

## Q&A
**问题示例**：
- ATT&CK框架是否适用于中小企业？
- 如何区分正常行为和恶意行为？

---

# 感谢聆听！
**知行合一，主动防御**
```

最后给出相关的PPT制作建议。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUowq9aVS9MnYakYz7P8hPkJXJFqRwryykpITFecRGXLiaAubua6GfxYhg/640?wx_fmt=png&from=appmsg)

整体内容描述还不错，譬如：

* ATT&CK框架的核心构成

  包括战术（Tactics）、技术（Techniques）和子技术（Sub-Techniques）三个层次。战术是攻击者的最终目标，技术是实现战术的具体方法，子技术是对技术的进一步细化。
* 传统攻击链模型的阶段

  传统攻击链模型包括侦察、武器化、投递、漏洞利用、安装、控制和行动七个阶段。每个阶段都对应着攻击者不同的行为和目标，是网络安全防御的重要参考。
* ATT&CK战术阶段与攻击链的对应关系

  ATT&CK框架中的战术阶段与攻击链模型的阶段存在对应关系，如初始访问对应投递阶段。这种对应关系使得安全人员可以从更细粒度的角度分析攻击行为，提高威胁检测的准确性。

---

# 二.Kimi制作PPT

接下来我们利用DeepSeek生成的PPT大概，智能化生成PPT。

> Kimi 是由中国人工智能公司\*\*月之暗面（Moonshot AI）\*\*开发的智能助手，定位于多模态、长文本处理和大模型推理领域的领先工具，旨在通过技术创新简化AI应用的门槛，服务于日常生活与专业场景。Kimi 的核心优势在于支持单次处理高达20万汉字的长文本，并能解析PDF、Word、Excel、网页等多种格式文件。用户可上传复杂文档，Kimi 能快速生成摘要、翻译内容，或通过问答形式提取关键信息。

**第一步，打开Kimi官方并进行登录。**

* https://kimi.moonshot.cn/

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUoIab5XCa4w7XwFz95BrH4Eb18MGic4kr9z0zs9ATe8qmEsnicnSadnCUg/640?wx_fmt=png&from=appmsg)

**第二步，点击kimi+，选择“PPT助手”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUowQbA5nsz6lSfpObmDUv6ZRKvpqhEaTRCSzlpaBRfxoNbyMUfJxQs8Q/640?wx_fmt=png&from=appmsg)

显示界面如下图所示：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUovOb9iaok4ul0icviaKpVbEPaxoTphbxyjo8QYHicVyVy4ILUgnwKTWNgsQ/640?wx_fmt=png&from=appmsg)

**第三步，输入DeepSeek生成的Markdown大纲。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUoAhlj3J1Akm5z577QYA9TILZeXzzp6KtUOibKibwEABNQicab5rIHXqPFQ/640?wx_fmt=png&from=appmsg)

Kimi大模型正在学习内容。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUo8UyNmWL0ZHVwnFuE3ia4hsYwsicGIZo6wTcXHKqMXXKuvXa842wGAssg/640?wx_fmt=png&from=appmsg)

**第四步，点击“一键生成PPT”按钮。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUoOWbSUsRxmUZdiaxN4ynVhfqVzlics84noU0kMInopnHuaT9UwJZmpKbw/640?wx_fmt=png&from=appmsg)

**第五步，选择PPT模版场景和风格。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUotaKCynoiavmCtU5J2I84RYJ2LlicsNXhaP0DNrhVnzAsWicJXVWRicpGTQ/640?wx_fmt=png&from=appmsg)

**第六步，点击“生成PPT”。由于是网络安全相关，选择总结汇报科技风格，并且黑色系列。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUoKFY0ibkSfVSPqFg0haw6b627L4YL2h539icge5jRuGPibYyTrCicejBzicQ/640?wx_fmt=png&from=appmsg)

生成的PPT内容如下，效果还真不错。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUo4hc3hSrkPZiagvwibFCaZviaAPAlWEdNavxDswj7oiaRM6iaibibch7lJ4kWw/640?wx_fmt=png&from=appmsg)

**第七步，点击“去编辑”，可以对生成的PPT进行修改。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUojtlMXqUR8ezZGcMsic0dW2uQSWszt5H89jJFS8Yh0e6cbpAA6pTb0pQ/640?wx_fmt=png&from=appmsg)

修改内容如下图所示：题目《威胁狩猎与ATT&CK框架：从攻击链视角看网络安全》，DeepSeek抓住了该PPT的核心。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUodXSbVAn1VgUJeWf2ibib6NBASM9TWRKePF7MWXx7REM08JppQnN2iaibRg/640?wx_fmt=png&from=appmsg)

**第八步，点击“放映”可以查看PPT每页的内容。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUoZFvZhq8Pvs5NXUXckE2P18jvkEK4gLdrMAydWDuDmp5614DBblLCLg/640?wx_fmt=png&from=appmsg)

该PPT包含融合ATT&CK框架的钓鱼攻击狩猎分析。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUooQz1JS1d6hyPtf8K8fibHotT1D1PicHSXFia7r6XTJyKlPent4FbKJ8NA/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUoEx0rGEzuoNTQia6p75nxicVhmlCjkLiaYemy5XDfCDiaxPXWNicpBySEcVg/640?wx_fmt=png&from=appmsg)

同时包括给新手的行动建议，该部分可以进一步丰富。

* 学习ATT&CK矩阵
* 利用开源工具进行模拟攻击
* 从高风险技术入手（包括TTP技战术）

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPjqKaE8j92W0R9K3xsbTUo0glibB...